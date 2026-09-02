"""Stage 1 (partial): fill speaker_gender / addressee / addressee_gender on dialogue rows from character_cards.yaml.
Per-line speaker reassignment for mixed voice banks (NPC_Solomon, NPC_Angel_Male) is a later LLM pass; method recorded per row."""
import json, re, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
cards, cur = {}, None
for line in open(os.path.join(BASE, "character_cards.yaml"), encoding="utf-8"):
    if line and not line[0].isspace() and line.rstrip().endswith(":") and not line.startswith("#"):
        cur = line.rstrip()[:-1]; cards[cur] = {}
    elif cur:
        m = re.match(r"\s+(\w+):\s*(.*)", line)
        if m: cards[cur][m.group(1)] = m.group(2).split("#")[0].strip().strip('"')
rows = [json.loads(l) for l in open(os.path.join(BASE, "01_corpus.jsonl"), encoding="utf-8")]
n = 0
for r in rows:
    if r["category"] != "dialogue": continue
    c = cards.get(r["speaker"])
    if not c: raise SystemExit(f"no card for {r['speaker']}")
    r["speaker_gender"] = c.get("gender", "unknown")
    r["addressee"] = "player"; r["addressee_gender"] = c.get("addressee_gender_default", "m")
    r["gender_method"] = "card_default"; n += 1
with open(os.path.join(BASE, "01_corpus.jsonl"), "w", encoding="utf-8") as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
from collections import Counter
print("dialogue rows tagged", n, Counter(r["speaker_gender"] for r in rows if r["category"]=="dialogue"))
