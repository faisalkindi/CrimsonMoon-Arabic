"""Batch compiler: every row leaves with compiled context (card, glossary hits, rules). Ch6 order.
Usage: python 100_build_batches.py [corpus.jsonl] [id_filter.txt]"""
import json, os, re, csv, io, sys
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "batches")
PLAN = {  # category -> (register, priority)  lower = earlier
    "ui_settings": ("plain", 1), "ui_menu": ("plain", 1), "ui_inline": ("plain", 1),
    "system": ("plain", 2), "system_online": ("plain", 2), "achievement": ("plain", 2),
    "item": ("elevated", 3), "skill": ("plain", 3),
    "quest": ("elevated", 4), "lore": ("elevated", 5),
    "dialogue": ("per_speaker", 6),
}
MAX_ROWS, MAX_CHARS = 60, 9000
RULES = [
    "Preserve every placeholder/tag byte-for-byte, same count and order: {0} <Header>...</> <IA_Dodge/> \\n.",
    "Never translate or alter id/key.",
    "Intent-first: how would this speaker say this in natural Arabic, here? Never mirror English word order or idiom.",
    "Modern Standard Arabic only; no dialect tokens. Arabic punctuation ، ؛ ؟. Western digits 0-9.",
    "Names transliterate (hard G = ق, V = ڤ) unless glossary says translate.",
    "Uncertain row: set needs_review=true and say why. Never guess.",
]


def load_glossary():
    p = os.path.join(BASE, "05_glossary.csv")
    return [(r["source_term"], r["approved_ar"], r["type"]) for r in csv.DictReader(open(p, encoding="utf-8"))
            if r["status"] == "approved" and r["approved_ar"]]


def load_cards():
    p = os.path.join(BASE, "character_cards.yaml")
    if not os.path.exists(p):
        return {}
    cards, cur, buf = {}, None, []
    for line in open(p, encoding="utf-8").read().splitlines():
        if line and not line[0].isspace() and line.rstrip().endswith(":") and not line.startswith("#"):
            if cur:
                cards[cur] = "\n".join(buf).strip()
            cur, buf = line.rstrip()[:-1], []
        elif cur:
            buf.append(line)
    if cur:
        cards[cur] = "\n".join(buf).strip()
    return cards


def main(src, filt=None):
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))
    rows = [json.loads(l) for l in open(src, encoding="utf-8") if l.strip()]
    rows = [r for r in rows if not r.get("skip") and not r.get("is_subtitle_cue")]
    if filt:
        rows = [r for r in rows if r["id"] in filt]
    glossary, cards = load_glossary(), load_cards()
    groups = defaultdict(list)
    for r in rows:
        reg, prio = PLAN.get(r["category"], ("plain", 9))
        key = (prio, f"dialogue__{r['speaker']}") if reg == "per_speaker" else (prio, r["category"])
        groups[key].append(r)
    bid, manifest = 0, []
    for (prio, g) in sorted(groups):
        grows = groups[(prio, g)]
        spk = g.split("__", 1)[1] if g.startswith("dialogue__") else None
        if spk:
            grows.sort(key=lambda r: (r.get("scene_id") or "", r.get("line_order") or 0, r["key"]))
            for r in grows:
                if not r.get("speaker_gender") or not r.get("addressee_gender"):
                    raise SystemExit(f"REJECT: dialogue row {r['id']} missing speaker/addressee gender")
        card = cards.get(spk) if spk else None
        if spk and not card:
            raise SystemExit(f"REJECT: dialogue speaker {spk} has no character card")
        m = re.search(r"register:\s*(\S+)", card) if card else None
        reg = m.group(1) if m else PLAN.get(g, ("plain", 9))[0]
        chunk, chars = [], 0

        def flush():
            nonlocal chunk, chars, bid
            if not chunk:
                return
            bid += 1
            blob = " ".join(x["source_en"] for x in chunk)
            terms = [{"en": t, "ar": a, "type": ty} for t, a, ty in glossary
                     if re.search(r"\b" + re.escape(t) + r"\b", blob)]
            job = {"batch": bid, "group": g, "speaker": spk, "register": reg, "character_card": card,
                   "glossary": terms, "rules": RULES,
                   "rows": [{"id": x["id"], "source_en": x["source_en"], "fr": x.get("fr"),
                             "category": x["category"], "speaker": x.get("speaker"),
                             "speaker_gender": x.get("speaker_gender"), "addressee": x.get("addressee"),
                             "addressee_gender": x.get("addressee_gender"), "placeholders": x["placeholders"],
                             "max_chars_hint": x.get("max_chars_hint")} for x in chunk]}
            with open(os.path.join(OUT, f"batch_{bid:03d}.json"), "w", encoding="utf-8") as f:
                json.dump(job, f, ensure_ascii=False, indent=1)
            manifest.append({"batch": bid, "group": g, "speaker": spk, "register": reg, "rows": len(chunk)})
            chunk, chars = [], 0

        for r in grows:
            L = len(r["source_en"])
            if chunk and (len(chunk) >= MAX_ROWS or chars + L > MAX_CHARS):
                flush()
            chunk.append(r); chars += L
        flush()
    with open(os.path.join(BASE, "batches_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("batches", len(manifest), "rows", sum(m["rows"] for m in manifest))


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "01_corpus.jsonl")
    filt = set(open(sys.argv[2], encoding="utf-8").read().split()) if len(sys.argv) > 2 else None
    main(src, filt)
