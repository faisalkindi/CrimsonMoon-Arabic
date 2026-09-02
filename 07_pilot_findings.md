# Pilot findings (Ch4 step 6) — 2026-09-01

Pilot: 310 mixed rows (`pilot_ids.txt`), route = mandatory local vLLM primary (gemma4-12b-awq, WSL2) → independent Sonnet editorial (3 agents, 61/309 rows changed) → deterministic validator (PASSED) → fresh Opus diff-verify (52 improvement, 8 regression, 1 wash). Output `pilot_final.jsonl`. Not yet: human linguistic review (Faisal), Sonnet Arabic QA pass, in-game QA (blocked on Arabic font).

## What the pilot proved
- Local 12B draft is usable as a primary: 0 empty rows after retries, placeholder parity failures 1/310, meaning errors caught by editor ~7% of rows. Throughput ~1 row/s at concurrency 16.
- Validator catches real defects (duplicated tag, UI-lock misses). Enforcement works.
- Speaker gender injection works: Door_Female_1 lines came out feminine; Librarian feminine self-reference held.
- Editors fix agreement well (باب/برج masculine, الكنيسة feminine singular, the Divine singular).

## Defect classes found (become rules)
| Class | Example | Enforcement |
|---|---|---|
| Name transliteration drift | Gallant جالانت vs قالانت; Aegoroth أجيوروث; Velchoria فيلتشوريا | approved glossary spellings + mechanical sweep + validator `glossary_term_missing` |
| "the Order" mistranslated / inconsistent | الأمر (=command) ×4, النظام ×8, التنظيم, رتبة | glossary lock (decision below) |
| Mechanic term genericized | Sigil → رمز instead of ختم | glossary lock |
| Over-vocalization | full tashkeel on Librarian/boss lines | style rule: shadda + disambiguating marks only; mechanical strip of case-ending tanween |
| Wrong sense of UI verb | Execute → تنفيذ (should be إجهاز finisher); Back → عودة | ui_lock.csv extended |
| Editor over-reach | respelling names not in glossary (Belwayne بلوين), inconsistent standardization between editors | glossary lock removes editor discretion; verify stage catches rest |
| Stage cues | (grunt) → أنين (whimper) | card `preserve` list + cue table in style guide |

## Decisions needed (glossary lock — human)
1. **Nephilim**: transliterate. Proposed frozen form: **نيفيليم** (no ال when used as a vocative/name: "أيها النيفيليم" ok). Draft produced 3 spellings.
2. **The Order** (short form of Order of the Crimson Moon): proposed **الجماعة** (جماعة القمر القرمزي) — avoids النظام (regime/system) and التنظيم (organization, modern political overtone) and الأمر (wrong). Alternative: **الرهبنة** (monastic order, fits "monastic military organization").
3. **Archspire**: FR kept it untranslated. Proposed transliteration **آرتشسباير**? Options: أرشسباير (5 rows) / أركسباير (2). Recommend **أرشسباير**.
4. **Sigil** = ختم, **Boon** = بركة, **Trinket** = حِلية, **Weapon Art** = فنّ السلاح, **Soul Energy** = طاقة الروح, **Angelic Grace** = النعمة الملائكية, **Angel Ascension** = الصعود الملائكي, **Run/Excursion** = جولة, **Skulls** = جماجم, **War Table** = طاولة الحرب, **Hellgrowth** = النماء الجهنّمي, **Dead Gods** = الآلهة الميتة, **Lunitarian Church** = الكنيسة اللونيتارية, **Holy Lineage** = السلالة المقدّسة, **Dry Rot King** = ملك العفن الجاف, **Lord of Perdition** = سيّد الهلاك, **Gallow's Wraith** = شبح المشنقة, **Chapter** (ecclesiastical) = مجمع, **Paladin** = بالادين? or فارس مقدّس.
5. **Player address**: masculine (FR 28 vs 4 evidence). Confirm.
6. **Culture code**: keep `ar` (marker test shows "Arabic" in picker) unless in-game numbers render ٠-٩; then `ar-MA`.
7. **Eye-dialect NPCs** (Lotte, Door_*): clipped colloquial-flavored MSA, no dialect vocabulary. Confirm.
8. **Register split**: elevated for lore/boss/Solomon/items/quest names; plain for UI/system/objectives. Confirm.

## Rules folded into pipeline already
- `[[NL]]` newline masking; placeholder regex without newline; output naming by group hash.
- Legal rows (>1500 chars) skipped, kept English.
- Compiler rejects dialogue rows without card/gender.
