"""Merge dual-pass review findings (review_findings/A_r_*.jsonl, B_r_*.jsonl) into one review-stage patch.
Rules: control chunk r_900 is scored, never applied. Per row, prefer a finding both passes agree on, else the
critical/high-confidence one, else pass A. Frozen-term guard: a fix that removes an approved glossary rendering the
row previously had is rejected. Placeholder/newline parity enforced. Output translated/review_zz_findings.jsonl.
Usage: python 220_apply_findings.py"""
import json, glob, os, re, csv, io, sys
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__)); FD = os.path.join(BASE, "review_findings")
PH = re.compile(r"\{[^{}]*\}|%[sdf]|<[^<>]+>")
gl = {r["source_term"]: r["approved_ar"] for r in csv.DictReader(open(os.path.join(BASE, "05_glossary.csv"), encoding="utf-8")) if r["status"] == "approved"}
draft = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(BASE, "03_working_draft.jsonl"), encoding="utf-8") if l.strip()}

# --- control scoring
answers = {a["id"]: a for a in json.load(open(os.path.join(BASE, "seeded_control_answers.json"), encoding="utf-8"))}
for p in "AB":
    f = os.path.join(FD, f"{p}_r_900.jsonl")
    if os.path.exists(f):
        found = {json.loads(l)["id"] for l in open(f, encoding="utf-8") if l.strip()}
        hits = [a["kind"] for i, a in answers.items() if i in found]
        print(f"control pass {p}: found {len(hits)}/{len(answers)} plants {hits}; extra findings {len(found - set(answers))}")
    else:
        print(f"control pass {p}: no file")

# --- collect findings
by_row = defaultdict(list)
for f in glob.glob(os.path.join(FD, "*_r_*.jsonl")):
    if "_r_900" in f: continue
    p = os.path.basename(f)[0]
    for l in open(f, encoding="utf-8"):
        if not l.strip(): continue
        x = json.loads(l); x["pass"] = p; by_row[x["id"]].append(x)


def ok(row, fix):
    en = row["source_en"]
    if PH.findall(fix) != row["placeholders"] or en.count("\n") != fix.count("\n"): return "parity"
    cur = re.sub(r"[ً-ْ]", "", row.get("ar") or ""); new = re.sub(r"[ً-ْ]", "", fix)
    for t, a in gl.items():
        if re.search(r"\b" + re.escape(t) + r"\b", en):
            stem = re.sub(r"[ةه]$", "", re.sub(r"^ال", "", re.sub(r"[ً-ْ]", "", a)).split()[0]); stem = stem[:4] if len(stem) > 4 else stem
            if stem in cur and stem not in new: return f"frozen:{t}"
    return None


out, rej, stats = [], [], defaultdict(int)
for rid, fs in by_row.items():
    row = draft.get(rid)
    if not row or row.get("skip"): continue
    fs = [x for x in fs if x.get("ar_fixed") and x["ar_fixed"] != row.get("ar")]
    if not fs: continue
    both = {x["pass"] for x in fs} == {"A", "B"}
    fs.sort(key=lambda x: (x["pass"] != "A", x.get("severity") != "critical", x.get("confidence") != "high"))
    pick = None
    for x in fs:
        why = ok(row, x["ar_fixed"])
        if why: rej.append((rid, x["pass"], why)); continue
        pick = x; break
    if not pick: continue
    stats["agreed" if both else f"only_{pick['pass']}"] += 1; stats[pick.get("severity", "?")] += 1
    out.append({"id": rid, "source_en": row["source_en"], "ar_before": row.get("ar"), "ar": pick["ar_fixed"],
                "reason": f"[{pick['pass']}{'+' if both else ''}/{pick.get('severity')}] {pick.get('reason','')}",
                "provenance": {"stage": "review", "model": "opus" if pick["pass"] == "A" else "sonnet", "both_passes": both},
                "attestations": row.get("attestations")})
with open(os.path.join(BASE, "translated", "review_zz_findings.jsonl"), "w", encoding="utf-8") as f:
    for o in out: f.write(json.dumps(o, ensure_ascii=False) + "\n")
print("rows with findings", len(by_row), "applied", len(out), dict(stats), "rejected", len(rej))
for r in rej[:10]: print("  rejected", r)
