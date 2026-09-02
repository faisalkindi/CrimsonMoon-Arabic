"""Semantic review chunks (MS2 pattern): whole corpus, ~90 rows/chunk, plus one seeded control chunk with planted errors
so reviewer recall can be measured. Reads 03_working_draft.jsonl -> review_chunks/r_NNN.jsonl and review_chunks/r_900.jsonl.
Usage: python 210_prep_review_chunks.py [rows=90]"""
import json, os, io, sys, random, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(BASE, "review_chunks"); os.makedirs(OUT, exist_ok=True)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 90
rows = [json.loads(l) for l in open(os.path.join(BASE, "03_working_draft.jsonl"), encoding="utf-8") if l.strip()]
rows = [r for r in rows if not r.get("skip") and not r.get("is_subtitle_cue") and r.get("ar")]
ORDER = {"dialogue": 0, "lore": 1, "item": 2, "quest": 3, "skill": 4, "ui_inline": 5, "ui_menu": 6, "ui_settings": 7, "system": 8, "system_online": 9, "achievement": 10}
rows.sort(key=lambda r: (ORDER.get(r["category"], 99), r.get("speaker") or "", r["namespace"], r["key"]))
for f in os.listdir(OUT): os.remove(os.path.join(OUT, f))
FIELDS = ("id", "key", "category", "speaker", "speaker_gender", "addressee", "addressee_gender", "source_en", "fr", "placeholders", "ar")
n = 0
for i in range(0, len(rows), N):
    n += 1
    with open(os.path.join(OUT, f"r_{n:03d}.jsonl"), "w", encoding="utf-8") as f:
        for r in rows[i:i + N]: f.write(json.dumps({k: r.get(k) for k in FIELDS}, ensure_ascii=False) + "\n")
# seeded control chunk: 84 clean rows + 6 planted errors (answers kept out of the chunk)
random.seed(11)
pool = [r for r in rows if r["category"] in ("dialogue", "lore", "item", "quest") and len(r["source_en"]) > 40 and not r["placeholders"]]
ctrl = random.sample(pool, 90); answers = []
plants = [
    ("negation_flip", lambda a: a.replace("لا ", "", 1) if "لا " in a else a + " لا"),
    ("gender_flip", lambda a: re.sub(r"\bأنتَ\b", "أنتِ", a, 1) if "أنتَ" in a else a.replace("ك ", "كِ ", 1)),
    ("number_change", lambda a: re.sub(r"\d+", lambda m: str(int(m.group()) + 3), a, 1) if re.search(r"\d+", a) else a + " 7"),
    ("dropped_clause", lambda a: a.rsplit("،", 1)[0] if "،" in a else a.rsplit(" ", 3)[0]),
    ("wrong_name", lambda a: a.replace("قالانت", "سولومون", 1) if "قالانت" in a else a.replace("الجماعة", "الكنيسة", 1) if "الجماعة" in a else a + " سولومون"),
    ("dialect", lambda a: a.replace(" الذي ", " اللي ", 1) if " الذي " in a else "شوف، " + a),
]
for (kind, fn), r in zip(plants, random.sample(ctrl, 6)):
    before = r["ar"]; r = dict(r); r["ar"] = fn(before)
    if r["ar"] == before: r["ar"] = before + " …ولكن"; kind += "_fallback"
    answers.append({"id": r["id"], "kind": kind, "clean_ar": before, "planted_ar": r["ar"]})
    ctrl[[c["id"] for c in ctrl].index(r["id"])] = r
random.shuffle(ctrl)
with open(os.path.join(OUT, "r_900.jsonl"), "w", encoding="utf-8") as f:
    for r in ctrl: f.write(json.dumps({k: r.get(k) for k in FIELDS}, ensure_ascii=False) + "\n")
json.dump(answers, open(os.path.join(BASE, "seeded_control_answers.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("review chunks", n, "rows", len(rows), "+ control r_900 with", len(answers), "plants")
