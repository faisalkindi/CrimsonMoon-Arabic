"""Blocking deterministic validator for Crimson Moon Arabic corpus. Nonzero exit on any failure.
Usage: python 40_qa_validate.py <corpus.jsonl> [--field ar]"""
import json, re, sys, csv, os, io
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
PH = re.compile(r"\{[^{}]*\}|%[sdf]|<[^<>]+>")
AR = re.compile(r"[؀-ۿ]")
ARABIC_INDIC = re.compile(r"[٠-٩]")
ASCII_PUNCT_MIX = re.compile(r"[؀-ۿ][ـ\s]*[,;?]|[,;?]\s*[؀-ۿ]")  # only when directly touching Arabic text
BIDI_MARKS = re.compile(r"[‎‏‪-‮⁦-⁩]")
DIALECT = re.compile(r"(?<![\w؀-ۿ])(عشان|إيش|ليش|شنو|هيك|هلق|كده|ازاي|عايز|بدي|وين|شلون|شي|اللي|هذي|هاي|سو|سوي|جيبها|جيبه|مو|مب|ماكو|أكو|وايد|شوي|شوية|إنت|انت|إنتي|هالشي|هالمرة|ودك|لين|حسيت|حاسس|رايح|ذيك|لسه|جابك|شوف|قرشين|يرتجف\s+لما|بكلمك|بيدي\s+لما)(?![\w؀-ۿ])")  # MSA-ambiguous tokens (لما، فيه، صح، كثير، هالك) deliberately excluded


def load_ui_lock():
    p = os.path.join(BASE, "ui_lock.csv")
    if not os.path.exists(p):
        return {}
    return {r["en"]: r["ar"] for r in csv.DictReader(open(p, encoding="utf-8")) if r["ar"]}


def load_glossary():
    g = {}
    for r in csv.DictReader(open(os.path.join(BASE, "05_glossary.csv"), encoding="utf-8")):
        if r["status"] == "approved" and r["approved_ar"]:
            g[r["source_term"]] = r["approved_ar"]
    return g


def main(path, field):
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    ui_lock, glossary = load_ui_lock(), load_glossary()
    err = defaultdict(list)
    seen = set()
    for r in rows:
        k = r["id"]; en = r["source_en"]; ar = (r.get(field) or "")
        if k in seen:
            err["duplicate_id"].append(k)
        seen.add(k)
        if r.get("skip"):
            continue
        if not ar.strip():
            err["empty_target"].append(k); continue
        if PH.findall(en) != PH.findall(ar):
            err["placeholder_mismatch"].append((k, PH.findall(en), PH.findall(ar)))
        if en.count("\n") != ar.count("\n"):
            err["newline_mismatch"].append(k)
        if AR.search(ar) and ASCII_PUNCT_MIX.search(ar):
            err["ascii_punct_in_arabic"].append(k)
        for num in ([] if r.get("is_subtitle_cue") else re.findall(r"\d+(?:[/:.]\d+)+|\d{2,}%?|\d%", en)):  # dates/ratios/multi-digit numbers verbatim; single digits may become words
            if num not in ar:
                err["number_changed"].append((k, num)); break
        if ARABIC_INDIC.search(ar):
            err["arabic_indic_digits"].append(k)
        if BIDI_MARKS.search(ar):
            err["stray_bidi_mark"].append(k)
        if re.search(r"[\ud800-\udfff�\x00-\x08\x0b\x0c\x0e-\x1f]", ar):
            err["corrupt_char"].append(k)
        if DIALECT.search(ar) and "dialect" not in (r.get("validator_exempt") or []):
            err["dialect_token"].append(k)
        if (len(en.strip()) > 3 and not AR.search(ar) and re.search(r"[A-Za-z]{4,}", ar)
                and not re.fullmatch(r"[A-Za-z0-9 ,.'\-:/%+()]+", en.strip()) and not PH.fullmatch(ar.strip())):
            err["untranslated_leakage"].append(k)
        if r.get("max_chars_hint") and len(ar) > r["max_chars_hint"] * 1.6:
            err["ui_length_overflow"].append((k, len(ar), ar[:40]))
        if en.strip() in ui_lock and ar.strip() != ui_lock[en.strip()]:
            err["ui_vocab_lock"].append((k, en.strip(), ar.strip(), ui_lock[en.strip()]))
        if r.get("is_subtitle_cue"):
            continue  # fragment of a full line: glossary/number/attestation are checked on the parent
        en_masked = en
        for term, tar in sorted(glossary.items(), key=lambda kv: -len(kv[0])):  # longest term wins; mask it so sub-terms don't fire
            hit = re.search(r"\b" + re.escape(term) + r"\b", en_masked)
            if hit:
                en_masked = re.sub(r"\b" + re.escape(term) + r"\b", "#" * len(term), en_masked)  # mask ALL occurrences
                core = re.sub(r"[ً-ْ]", "", re.sub(r"^ال", "", tar))  # article/harakat-insensitive
                stem = re.sub(r"[ةه]$", "", core.split()[0]); stem = stem[:4] if len(stem) > 4 else stem  # stem tolerates plurals/nisba (بركة/بركات, ملاك/ملائكي)
                if stem not in re.sub(r"[ً-ْ]", "", ar) and f"glossary:{term}" not in (r.get("validator_exempt") or []):
                    err["glossary_term_missing"].append((k, term, tar))
        if r.get("category") == "dialogue":
            att = r.get("attestations") or {}
            for a in ("speaker_gender_checked", "addressee_gender_checked", "voice_checked"):
                if not att.get(a):
                    err["missing_attestation"].append((k, a)); break
    total = sum(len(v) for v in err.values())
    print(f"Validated {len(rows)} rows ({field}).")
    for c, items in err.items():
        print(f"  {c}: {len(items)}")
        for it in items[:5]:
            print(f"    {it}")
    print("\nFAILED" if total else "\nPASSED", total)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    a = sys.argv[1:]; field = "ar"
    if "--field" in a:
        field = a[a.index("--field") + 1]; a = [x for x in a if x not in ("--field", field)]
    main(a[0] if a else os.path.join(BASE, "01_corpus.jsonl"), field)
