"""Flow-pass chunks: contiguous units (speaker scenes, whole lore notes, item families, quest lines, UI screens).
Reads 03_working_draft.jsonl -> flow_chunks/f_NN.jsonl (~N rows each, never splitting a unit unless > N).
Usage: python 200_prep_flow_chunks.py [rows_per_chunk=220]"""
import json, os, re, io, sys
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(BASE, "flow_chunks"); os.makedirs(OUT, exist_ok=True)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 220
rows = [json.loads(l) for l in open(os.path.join(BASE, "03_working_draft.jsonl"), encoding="utf-8") if l.strip()]
rows = [r for r in rows if not r.get("skip") and not r.get("is_subtitle_cue") and r.get("ar")]
ORDER = {"dialogue": 0, "lore": 1, "item": 2, "quest": 3, "skill": 4, "ui_inline": 5, "ui_menu": 6, "ui_settings": 7, "system": 8, "system_online": 9, "achievement": 10}


def unit(r):
    c = r["category"]
    if c == "dialogue": return ("dialogue", r.get("speaker") or r["namespace"])
    if c == "lore": return ("lore", re.sub(r"_(Title|SubHead|Subhead|SubText|Subtext|Body\w*|BodyText\w*|Tile)$", "", r["key"]))
    if c == "quest": return ("quest", re.sub(r"_(Name|Desc|Objective\w*|QuestTopic|TurnIn\w*|WarTable\w*)$", "", r["key"]))
    if c in ("item", "skill"): return (c, r["namespace"])
    return (c, r["namespace"] or "inline")


units = defaultdict(list)
for r in rows: units[unit(r)].append(r)
keys = sorted(units, key=lambda u: (ORDER.get(u[0], 99), u[1]))
chunks, cur, curc = [], [], None
for u in keys:
    us = sorted(units[u], key=lambda r: r["key"])
    if len(us) > N:  # oversized unit (e.g. inline UI): split hard
        if cur: chunks.append(cur); cur = []
        for i in range(0, len(us), N): chunks.append(us[i:i + N])
        continue
    if cur and (len(cur) + len(us) > N) and (curc != u[0] or len(cur) >= N * 0.6):
        chunks.append(cur); cur = []
    cur.extend(us); curc = u[0]
if cur: chunks.append(cur)
for f in os.listdir(OUT): os.remove(os.path.join(OUT, f))
for i, ch in enumerate(chunks, 1):
    with open(os.path.join(OUT, f"f_{i:02d}.jsonl"), "w", encoding="utf-8") as f:
        for r in ch:
            f.write(json.dumps({"id": r["id"], "key": r["key"], "unit": "|".join(unit(r)), "category": r["category"], "speaker": r.get("speaker"),
                                "speaker_gender": r.get("speaker_gender"), "addressee": r.get("addressee"), "addressee_gender": r.get("addressee_gender"),
                                "source_en": r["source_en"], "placeholders": r["placeholders"], "max_chars_hint": r.get("max_chars_hint"), "ar": r["ar"]},
                               ensure_ascii=False) + "\n")
print("rows", len(rows), "units", len(units), "chunks", len(chunks))
for i, ch in enumerate(chunks, 1):
    cats = sorted({r["category"] for r in ch}); print(f"  f_{i:02d} {len(ch):4} {','.join(cats)} words={sum(len(r['source_en'].split()) for r in ch)}")
