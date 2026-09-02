"""Merge stage outputs into 03_working_draft.jsonl: corpus rows + ar from translated/*.jsonl (later stages override earlier)."""
import json, glob, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
rows = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(BASE, "01_corpus.jsonl"), encoding="utf-8")}
n = 0
for stage in ["vllm", "cues", "edit", "verify", "qa", "flow", "review"]:
    for f in sorted(glob.glob(os.path.join(BASE, "translated", f"{stage}_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            r = json.loads(l); t = rows.get(r["id"])
            if not t: continue
            t["ar"] = r.get("final_ar", r.get("ar", "")); t.setdefault("provenance", []).append(r.get("provenance", {"stage": stage}))
            if r.get("needs_review"): t["needs_review"] = True
            if r.get("attestations"): t["attestations"] = r["attestations"]
            n += 1
with open(os.path.join(BASE, "03_working_draft.jsonl"), "w", encoding="utf-8") as f:
    for t in rows.values(): f.write(json.dumps(t, ensure_ascii=False) + "\n")
print("merged", n, "translated rows")
