"""Stage 5 prep: compute actual_text_changed from edit outputs (never trust editor flag); emit verify chunks (~90 rows).
Usage: python 140_diff_verify_prep.py translated/edit_*.jsonl"""
import json, glob, sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(BASE, "verify_chunks"); os.makedirs(OUT, exist_ok=True)
rows = [json.loads(l) for p in sys.argv[1:] for l in open(p, encoding="utf-8") if l.strip()]
wash, silent, changed = 0, 0, []
for r in rows:
    r["actual_text_changed"] = r["ar"] != r["ar_before"]
    if r.get("editor_claimed_changed") and not r["actual_text_changed"]: wash += 1; r["verdict_hint"] = "candidate_wash"
    if r["actual_text_changed"] and not r.get("editor_claimed_changed"): silent += 1; r["verdict_hint"] = "silent_change"
    if r["actual_text_changed"]: changed.append(r)
print(f"rows {len(rows)} actually_changed {len(changed)} claimed-but-identical(wash) {wash} silent-changes {silent}")
for i in range(0, len(changed), 90):
    with open(os.path.join(OUT, f"verify_{i//90+1:03d}.jsonl"), "w", encoding="utf-8") as f:
        for r in changed[i:i+90]: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("verify chunks", (len(changed) + 89) // 90)
