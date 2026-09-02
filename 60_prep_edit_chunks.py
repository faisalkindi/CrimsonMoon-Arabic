"""Build <batch>_draft.jsonl from working draft, run mechanical fix, annotate validator issues, split into edit chunks.
Usage: python 60_prep_edit_chunks.py <ids.txt> <tag> [chunk_rows=400]"""
import json, re, csv, os, io, sys, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
PH = re.compile(r"\{[^{}]*\}|%[sdf]|<[^<>]+>"); AR = re.compile(r"[؀-ۿ]")
ids_file, tag = sys.argv[1], sys.argv[2]; N = int(sys.argv[3]) if len(sys.argv) > 3 else 400
ids = set(open(ids_file, encoding="utf-8").read().split())
subprocess.run([sys.executable, os.path.join(BASE, "130_merge_draft.py")], check=True)
rows = [json.loads(l) for l in open(os.path.join(BASE, "03_working_draft.jsonl"), encoding="utf-8") if l.strip()]
sub = [r for r in rows if r["id"] in ids]
draft = os.path.join(BASE, f"{tag}_draft.jsonl"); fixed = os.path.join(BASE, f"{tag}_draft_fixed.jsonl")
open(draft, "w", encoding="utf-8").write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in sub))
subprocess.run([sys.executable, os.path.join(BASE, "50_mechanical_fix.py"), draft, fixed], check=True)
rows = [json.loads(l) for l in open(fixed, encoding="utf-8")]
gl = {r["source_term"]: r["approved_ar"] for r in csv.DictReader(open(os.path.join(BASE, "05_glossary.csv"), encoding="utf-8")) if r["status"] == "approved"}
for r in rows:
    iss = []; en, ar = r["source_en"], r.get("ar", "")
    if not ar and not r.get("skip"): iss.append("empty")
    if PH.findall(ar) != r["placeholders"]: iss.append("placeholder_mismatch")
    if en.count("\n") != ar.count("\n"): iss.append("newline_mismatch")
    if len(en.strip()) > 3 and not AR.search(ar) and re.search(r"[A-Za-z]{4,}", ar): iss.append("untranslated_or_should_skip")
    enm = en
    for t, a in sorted(gl.items(), key=lambda kv: -len(kv[0])):
        h = re.search(r"\b" + re.escape(t) + r"\b", enm)
        if h:
            enm = enm[:h.start()] + "#" * len(t) + enm[h.end():]
            core = re.sub(r"[ً-ْ]", "", re.sub(r"^ال", "", a)).split()[0]
            if core not in re.sub(r"[ً-ْ]", "", ar): iss.append(f"glossary:{t}={a}")
    if r.get("max_chars_hint") and len(ar) > r["max_chars_hint"] * 1.6: iss.append("too_long_for_ui")
    r["validator_issues"] = iss
rows.sort(key=lambda r: (r["category"], r.get("speaker") or "", r["namespace"], r["key"]))
os.makedirs(os.path.join(BASE, "edit_chunks"), exist_ok=True)
n = 0
for i in range(0, len(rows), N):
    n += 1
    with open(os.path.join(BASE, "edit_chunks", f"{tag}_{n:02d}.jsonl"), "w", encoding="utf-8") as f:
        for r in rows[i:i + N]:
            f.write(json.dumps({k: r.get(k) for k in ("id", "source_en", "fr", "category", "speaker", "speaker_gender", "addressee_gender",
                                                      "addressee", "gender_evidence", "placeholders", "max_chars_hint", "ar", "validator_issues", "skip")}, ensure_ascii=False) + "\n")
print(f"{tag}: rows {len(rows)} chunks {n} rows_with_issues {sum(1 for r in rows if r['validator_issues'])} empty {sum(1 for r in rows if 'empty' in r['validator_issues'])}")
