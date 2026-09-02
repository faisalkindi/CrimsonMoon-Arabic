"""Derive `_cue_N` subtitle fragments from the full-line Arabic. Cues concatenate (with spaces) to the full line.
Strategy: split Arabic at sentence/clause punctuation into N parts proportional to the English cue lengths;
if the Arabic has fewer natural breaks than cues, fall back to word-count proportional split.
Rows that cannot be split cleanly (placeholder inside a cue boundary) are marked needs_review.
Usage: python 70_derive_cues.py  -> translated/cues_derived.jsonl"""
import json, re, os, io, sys
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
PH = re.compile(r"\{[^{}]*\}|%[sdf]|<[^<>]+>")
rows = [json.loads(l) for l in open(os.path.join(BASE, "03_working_draft.jsonl"), encoding="utf-8") if l.strip()]
by_id = {r["id"]: r for r in rows}
groups = defaultdict(list)
for r in rows:
    m = re.match(r"(.+)_cue_(\d+)$", r["key"])
    if m: groups[(r["namespace"], m.group(1))].append((int(m.group(2)), r))
out, ok, review, nofull = [], 0, 0, 0
for (ns, base), cues in groups.items():
    cues.sort()
    full = by_id.get(f"{ns}|{base}")
    if not full or not full.get("ar"):
        nofull += 1; continue
    ar = PH.sub(lambda m: m.group(0).replace(" ", ""), full["ar"].strip()); n = len(cues)  # keep spaced placeholders atomic
    en_lens = [max(1, len(c["source_en"].split())) for _, c in cues]; tot = sum(en_lens)
    # candidate break points: after punctuation
    pieces = [p for p in re.split(r"(?<=[،؛؟!.…])\s+", ar) if p]
    if len(pieces) >= n:  # merge pieces into n groups proportional to English word share
        parts, i = [], 0
        for k in range(n):
            target = round(len(ar.split()) * en_lens[k] / tot) if k < n - 1 else None
            buf = []
            while i < len(pieces) and (target is None or not buf or len(" ".join(buf).split()) < target):
                if k < n - 1 and len(pieces) - i <= n - k - 1: break
                buf.append(pieces[i]); i += 1
            parts.append(" ".join(buf))
        if i < len(pieces): parts[-1] = (parts[-1] + " " + " ".join(pieces[i:])).strip()
    else:  # word-proportional
        words = ar.split(); parts, i = [], 0
        for k in range(n):
            cnt = round(len(words) * en_lens[k] / tot) if k < n - 1 else len(words) - i
            parts.append(" ".join(words[i:i + cnt])); i += cnt
    for j in range(1, len(parts)):  # empty tail part: borrow the last word of the previous part
        if not parts[j] and parts[j - 1].split():
            w = parts[j - 1].split(); parts[j - 1] = " ".join(w[:-1]); parts[j] = w[-1]
    # placeholders/stage cues must sit in the cue whose English carries them: move them across parts if needed
    for j, (_, c) in enumerate(cues):
        for ph in [x.replace(" ", "") for x in PH.findall(c["source_en"])]:
            if ph not in parts[j]:
                for k in range(len(parts)):
                    if k != j and ph in parts[k]:
                        parts[k] = parts[k].replace(ph, "", 1).strip(); parts[j] = (ph + " " + parts[j]).strip(); break
    flag = any(not p for p in parts) or any(PH.findall(p) != PH.findall(c["source_en"]) for p, (_, c) in zip(parts, cues))
    parts = [p.replace("", " ") for p in parts]
    for p, (_, c) in zip(parts, cues):
        out.append({"id": c["id"], "source_en": c["source_en"], "ar": p, "needs_review": flag,
                    "attestations": full.get("attestations"), "provenance": {"stage": "cue_derive", "from": full["id"]}})
    review += flag; ok += not flag
with open(os.path.join(BASE, "translated", "cues_derived.jsonl"), "w", encoding="utf-8") as f:
    for o in out: f.write(json.dumps(o, ensure_ascii=False) + "\n")
print(f"cue groups {len(groups)} derived_ok {ok} needs_review {review} missing_full {nofull} rows {len(out)}")
