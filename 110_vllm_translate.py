"""Stage 2 primary draft via local vLLM (gemma4-12b-awq). Consumes batches/batch_NNN.json from 100_build_batches.py.
Writes translated/vllm_NNN.jsonl (one row per input: id, source_en, ar, needs_review, provenance).
Controls are masked as [[CTRL_n]] sentinels and restored; parity enforced; fallback to per-row retry.
Usage: python 110_vllm_translate.py [batch_glob]"""
import asyncio, glob, json, os, re, sys, time, io, urllib.request, urllib.error
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
URL = os.environ.get("VLLM_URL", "http://127.0.0.1:8000/v1/chat/completions")
MODEL = "gemma4-12b-awq"
CONCURRENCY = 16
CHUNK_FUNCTIONAL, CHUNK_DIALOGUE = 12, 6
PH = re.compile(r"\{[^{}]*\}|%[sdf]|<[^<>]+>")
PROMPT_VERSION = "cm-pilot-v1"

CONTEXT = open(os.path.join(BASE, "context_card.md"), encoding="utf-8").read() if os.path.exists(os.path.join(BASE, "context_card.md")) else ""


def mask(text, controls):
    m = []
    for i, c in enumerate(controls):
        s = f"[[CTRL_{i}]]"; text = text.replace(c, s, 1); m.append((s, c))
    return text.replace("\n", "[[NL]]"), m


def unmask(text, m):
    for s, c in m:
        text = text.replace(s, c)
    return text.replace("\\n", "[[NL]]").replace("[[NL]]", "\n")


def call(prompt, max_tokens, retries=3):
    err = None; budget = max_tokens
    for a in range(retries):
        body = json.dumps({"model": MODEL, "messages": [{"role": "user", "content": prompt}],
                           "temperature": 0, "max_tokens": budget}).encode()
        req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                return json.load(r)["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            err = e
            if e.code == 400 and budget > 256: budget //= 2
            time.sleep(2 * (a + 1))
        except Exception as e:
            err = e; time.sleep(2 * (a + 1))
    raise RuntimeError(f"vLLM failed: {err}")


def build_prompt(job, entries):
    dialogue = job["speaker"] is not None
    rows_txt = "\n".join(f"{sid}: {mask(r['source_en'], r['placeholders'])[0]}" for sid, r in entries)
    meta = []
    for sid, r in entries:
        d = [f"id={sid}", f"category={r['category']}"]
        if r["placeholders"]: d.append(f"controls={json.dumps(mask(r['source_en'], r['placeholders'])[1], ensure_ascii=False)}")
        if r.get("fr"): d.append(f"fr_reference={json.dumps(r['fr'][:200], ensure_ascii=False)}")
        if r.get("max_chars_hint"): d.append(f"max_chars≈{r['max_chars_hint']}")
        if dialogue:
            d.append(f"speaker={r['speaker']}({r['speaker_gender']}) addressee={r['addressee']}({r['addressee_gender']})")
        meta.append(" | ".join(d))
    gloss = "\n".join(f"- {g['en']} → {g['ar']}" for g in job["glossary"]) or "- (none approved yet)"
    card = f"\nSpeaker card:\n{job['character_card']}\n" if job.get("character_card") else ""
    kind = ("These are contiguous dialogue lines from ONE speaker in order. Keep one consistent voice; verbs/adjectives agree with the speaker's gender; every 'you' agrees with the addressee's gender."
            if dialogue else "These are standalone UI/system/item/skill/quest strings. Concise, consistent, player-facing function first.")
    rules = "\n".join(f"{i+1}. {x}" for i, x in enumerate(job["rules"]))
    return f"""Translate the English game strings below into natural Arabic for the game Crimson Moon (gothic dark-fantasy action RPG).

Register for this batch: {job['register']}.
{kind}
{card}
Rules:
{rules}
7. Use the French reference only to recover gender/number/formality that English hides; English is the source of truth.
8. Copy every [[CTRL_n]] and [[NL]] sentinel exactly, same position, order and count ([[NL]] is a line break; never write a literal \n). Never translate, delete, duplicate, or move one.
9. Return exactly one line per input: `id: translation`. Same ids, same order. No markdown, no commentary, no blank lines.
10. If a row is genuinely ambiguous, still translate it but append the marker ⟦REVIEW⟧ at the end of that line.

Approved glossary (use exactly, inflect only as grammar requires):
{gloss}

Game context:
{CONTEXT}

Input rows:
{rows_txt}

Metadata by id (context only, do not echo):
{chr(10).join(meta)}
"""


def parse(text, ids):
    out = {}
    for line in text.splitlines():
        line = line.strip()
        if ":" not in line: continue
        sid, _, t = line.partition(":")
        sid = sid.strip()
        if sid in ids and sid not in out: out[sid] = t.strip()
    return out if list(out) == ids else None


async def run_chunk(job, entries, sem):
    ids = [sid for sid, _ in entries]
    prompt = build_prompt(job, entries)
    est_prompt_tokens = len(prompt) // 3  # ponytail: rough mixed en/ar estimate; tokenizer-exact if it ever bites
    budget = min(2000, sum(len(r["source_en"]) * 2 + 60 for _, r in entries) + 200)
    if est_prompt_tokens + budget > 3800:
        if len(entries) > 1:
            half = len(entries) // 2
            a = await run_chunk(job, entries[:half], sem); b = await run_chunk(job, entries[half:], sem)
            return {**a, **b}
        budget = max(200, 3800 - est_prompt_tokens)
    try:
        async with sem:
            raw = await asyncio.to_thread(call, prompt, budget)
    except RuntimeError:
        if len(entries) > 1:
            half = len(entries) // 2
            a = await run_chunk(job, entries[:half], sem); b = await run_chunk(job, entries[half:], sem)
            return {**a, **b}
        return {ids[0]: None}
    parsed = parse(raw, ids)
    results = {}
    if parsed is None:
        if len(entries) > 1:
            half = len(entries) // 2
            a = await run_chunk(job, entries[:half], sem); b = await run_chunk(job, entries[half:], sem)
            return {**a, **b}
        results[ids[0]] = None
        return results
    for sid, r in entries:
        t = parsed[sid]; review = "⟦REVIEW" in t; t = re.sub(r"⟦REVIEW[^⟧]*⟧?", "", t).strip()
        _, m = mask(r["source_en"], r["placeholders"]); t = unmask(t, m)
        if PH.findall(t) != r["placeholders"]:
            results[sid] = {"ar": t, "needs_review": True, "note": "placeholder_parity_failed"}
        else:
            results[sid] = {"ar": t, "needs_review": review, "note": ""}
    return results


async def run_batch(path, sem):
    job = json.load(open(path, encoding="utf-8"))
    size = CHUNK_DIALOGUE if job["speaker"] else CHUNK_FUNCTIONAL
    entries = [(f"r{i}", r) for i, r in enumerate(job["rows"])]
    chunks = [entries[i:i + size] for i in range(0, len(entries), size)]
    res = {}
    for part in await asyncio.gather(*[run_chunk(job, c, sem) for c in chunks]): res.update(part)
    import hashlib
    tag = hashlib.md5("".join(r["id"] for r in job["rows"]).encode()).hexdigest()[:8]
    out = os.path.join(BASE, "translated", f"vllm_{job['group'][:24]}_{tag}.jsonl")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        for sid, r in entries:
            x = res.get(sid) or {"ar": "", "needs_review": True, "note": "empty_after_retry"}
            f.write(json.dumps({"id": r["id"], "source_en": r["source_en"], "category": r["category"], "speaker": r.get("speaker"),
                                "ar": x["ar"], "needs_review": x["needs_review"], "note": x["note"],
                                "provenance": {"stage": "primary", "model": MODEL, "prompt": PROMPT_VERSION,
                                               "intent_localization_required": True, "batch": job["batch"]}},
                               ensure_ascii=False) + "\n")
    empty = sum(1 for sid in res if not res[sid])
    print(f"batch {job['batch']:03d} {job['group']:28} rows {len(entries):3} empty {empty} review {sum(1 for v in res.values() if v and v['needs_review'])}")


async def main(pattern):
    sem = asyncio.Semaphore(CONCURRENCY)
    files = sorted(glob.glob(pattern))
    t0 = time.time()
    await asyncio.gather(*[run_batch(f, sem) for f in files])
    print(f"done {len(files)} batches in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "batches", "batch_*.json")))
