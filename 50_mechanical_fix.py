"""Stage 4 deterministic post-process. Idempotent; per-row audit log; never touches placeholders.
Sweeps known-bad name/term variants to approved spellings, ASCII punctuation inside Arabic, ellipsis runs, literal \\n.
Usage: python 50_mechanical_fix.py <in.jsonl> <out.jsonl>"""
import json, re, sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
PH = re.compile(r"\{[^{}]*\}|%[sdf]|<[^<>]+>")
VARIANTS = {  # bad -> approved (order matters: longer first)
    "النيفيليم": "النيفيليم", "النيفليم": "النيفيليم", "نيفليم": "نيفيليم", "نفيليم": "نيفيليم",
    "جالانت": "قالانت", "غالانت": "قالانت", "غاجوف": "قاجوف", "جاجوف": "قاجوف", "ماتياس": "ماثياس",
    "أجيوروث": "إيقوروث", "أيجوروث": "إيقوروث", "إيجوروث": "إيقوروث",
    "فيلتشوريا": "ڤلتشوريا", "ڤيلتشوريا": "ڤلتشوريا", "ڤلكوريا": "ڤلتشوريا", "فلكوريا": "ڤلتشوريا",
    "أرمايا": "أرميا", "بلوين": "بيلواين", "ليتينستانغ": "ليتنستانق", "ليتنستانغ": "ليتنستانق",
    "أركسباير": "أرشسباير", "آرشسباير": "أرشسباير", "أرشسبير": "أرشسباير",
    "غيلدنارك": "قيلدنارك", "جيلدنارك": "قيلدنارك", "غيلدينارك": "قيلدنارك",
    "أرشيفية التنظيم": "أرشيفية الجماعة", "أرشيفية النظام": "أرشيفية الجماعة",
    "إيغريغور": "إيقريقور", "الإيغريغور": "الإيقريقور", "المجاهد": "الصليبي", "المجاهدين": "الصليبيين", " كاين": " قابيل", "ميثاق كين": "ميثاق قابيل",
    "القدرة على التحمل": "التحمّل", "القدرة على التحمّل": "التحمّل", "جهاز الإرسال": "غرفة الترسيخ", "الطوق المتصدّع": "الطوق المتحطّم",
    "اللولب المتصدّع": "الطوق المتحطّم", "اللفيفة المحطّمة": "الطوق المتحطّم", "اللولب": "الطوق", "اللفيفة": "الطوق",
    "قروڈ": "قروڤ", "أورييل": "أوريل", "ماجدا": "ماقدا", "طيف المشنقة": "شبح المشنقة", "الكويل": "الطوق",
    "إيقريقور اللحم المصاغ": "الإيقريقور المصاغ من اللحم", "الإيقريقور المنسوج من اللحم": "الإيقريقور المصاغ من اللحم",
    "إيقريقور مصوغ من لحم": "الإيقريقور المصاغ من اللحم", "الإيقريقور المصنوع من اللحم": "الإيقريقور المصاغ من اللحم",
    "فالاهك": "ڤالاك", "إلك غروف": "إلك قروڤ", "الوصية الموبوءة": "الوصية المحذوفة",
}
import csv
UI_LOCK = {r["en"]: r["ar"] for r in csv.DictReader(open(os.path.join(BASE, "ui_lock.csv"), encoding="utf-8"))} if os.path.exists(os.path.join(BASE, "ui_lock.csv")) else {}
ORDER_CTX = re.compile(r"(?<=\b)(النظام|التنظيم)(?=\b)")  # only swept when source mentions "the Order"
AUDIT = []


def fix(row):
    src, ar = row["source_en"], row.get("ar") or ""
    if not ar: return ar
    orig = ar
    ph_before = PH.findall(ar)
    for bad, good in sorted(VARIANTS.items(), key=lambda kv: -len(kv[0])):
        if bad != good and bad in ar: ar = ar.replace(bad, good)
    if re.search(r"\bOrder\b", src) and not re.search(r"in order|out of order|world order|Order (of|in|to) (?!the Crimson)", src):
        ar = ORDER_CTX.sub("الجماعة", ar)
    ar = re.sub(r"\s*⟦REVIEW[^⟧]*⟧?", "", ar)  # leaked model annotation
    ar = ar.replace("\\n", "\n")
    ar = re.sub(r"\.{2,}", "…", ar); ar = re.sub(r"…{2,}", "…", ar)
    # ASCII punctuation adjacent to Arabic -> Arabic punctuation (never inside placeholders: mask first)
    masked = []
    def _m(m): masked.append(m.group(0)); return f"\x00{len(masked)-1}\x00"
    tmp = PH.sub(_m, ar)
    tmp = re.sub(r"(?<=[؀-ۿ])\s*,", "،", tmp); tmp = re.sub(r"(?<=[؀-ۿ])\s*;", "؛", tmp)
    tmp = re.sub(r"(?<=[؀-ۿ])\s*\?", "؟", tmp)
    tmp = re.sub(r"\s+([،؛؟!.])", r"\1", tmp); tmp = re.sub(r"  +", " ", tmp)
    ar = re.sub(r"\x00(\d+)\x00", lambda m: masked[int(m.group(1))], tmp)
    if PH.findall(ar) != ph_before: return orig  # never alter placeholders
    # known model defect: sentinel AND literal tag both emitted -> adjacent duplicate tags. Collapse only if it restores parity.
    want = PH.findall(src)
    if PH.findall(ar) != want:
        cand = re.sub(r"(<[^<>]+>)\1", r"\1", ar)
        if PH.findall(cand) == want: ar = cand
    if src.strip() in UI_LOCK and ar.strip() != UI_LOCK[src.strip()]: ar = UI_LOCK[src.strip()]
    if ar != orig: AUDIT.append({"id": row["id"], "before": orig, "after": ar})
    return ar


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    rows = [json.loads(l) for l in open(src, encoding="utf-8") if l.strip()]
    for r in rows:
        r["ar"] = fix(r)
    with open(dst, "w", encoding="utf-8") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(os.path.join(BASE, "50_mechanical_fix_audit.jsonl"), "a", encoding="utf-8") as f:
        for a in AUDIT: f.write(json.dumps(a, ensure_ascii=False) + "\n")
    print(f"rows {len(rows)} changed {len(AUDIT)}")
    # self-check: idempotent
    again = sum(1 for r in rows if fix(dict(r)) != r["ar"])
    assert again == 0, f"not idempotent: {again}"
