# Crimson Moon — Arabic Style Guide (draft v0, to be locked by the pilot)

Base: reusable Arabic Style Guide (arabic-localization skill, Ch9) + MS2 calibration precedent. This file records Crimson Moon–specific decisions. Anything marked PILOT is a hypothesis until pilot review confirms it.

## Source
English is the original (US studio, Gridly pipeline, en = native locres). Case B (Ch2): use `fr`/`es`/`it` columns for gender/number/formality that English hides. Shipped localizations were AI-assisted then human-revised (Steam disclosure) — treat them as cross-reference only, never as authority on meaning.

## Register: SPLIT (PILOT)
The English text has at least three voices; Arabic mirrors the split rather than flattening it.
1. **Elevated literary فصحى راقية** — lore notes (letters, journals, scripture, "Litany of the Holy Phases", "Crimson Concordat"), boss taunts (Felwyl, Mahkteah, Valahk-Nor), Solomon Moore, the Angel, Door_Priest, item/armor/trinket descriptions, quest names. Semi-archaic, weighted, aphoristic. Not سجع.
2. **Plain فصحى ميسّرة** — all UI, settings, tutorial, system/online messages, achievement text, skill/boon mechanics text, quest objectives ("Defeat X throughout Gildenarch").
3. **Colloquial-flavored MSA (register, not dialect)** — street NPCs written in eye-dialect ("hidin'", "Ain't heard 'em", "s'shomeone"): Merchant (Lotte), Door_* NPCs, Drunk, Prisoner, DemoralizedWoman. Render as simple, clipped, warm/rough MSA with short sentences, contractions of meaning not of spelling, interjections (آه، يا هذا، حسنًا). Never actual dialect vocabulary (validator blocks عشان/ليش/كده etc.). Gajov the Blacksmith speaks broken third-person English ("Gajov forge blade!"): keep third-person self-reference and clipped syntax in Arabic (جاجوف يصنع السيف!).
Per-speaker register lives in `character_cards.yaml` and is injected by the batch compiler.

## Gender
- Player character (the Nephilim): FR uses masculine agreement for player address ("tu es prêt", 19 hits vs 14 feminine hits that are all about objects like "la Fureur est prête"). **Default player address = masculine** (PILOT; re-check once character-select screen is inspected in-game).
- Generic system prompts: gender-neutral phrasing (verbal nouns, يُرجى…) to avoid gendering the player where English does not.
- Every dialogue row must carry `speaker_gender` and `addressee_gender` before compile; the compiler rejects rows without them.
- One consistent register per speaker toward the same addressee; never alternate أنتَ/أنتم.

## Names and terms
- Transliterate person/place names; hard G = ق, V = ڤ. One frozen spelling per name in `05_glossary.csv`.
- Meaningful titles translate: Dry Rot King, Lord of Perdition, Order of the Crimson Moon, Dead Gods, Hellgrowth, Infernal Legion, Holy Lineage, Crimson Concordat, Knight Commander.
- **Nephilim**: the Arabic Quranic/biblical cognate is not a match in meaning. PILOT decision: transliterate نِفيليم (one word, stable) vs translate. Lock in pilot.
- Mechanics (freeze once): Soul Energy, Angelic Grace, Angel Ascension, Weapon Art, Boon, Trinket, Sigil, Blueprint, War Table, Loadout, Excursion, Skulls (difficulty), Hellrift, Nexus Gate, Purify, Abraxas Stone.

## UI vocabulary lock
Adopt the MS2 UI lock (Quit=خروج, Continue=متابعة, Back=رجوع, Cancel=إلغاء, Confirm=تأكيد, Apply=تطبيق, Settings=الإعدادات, Options=الخيارات, Restart=إعادة البدء, Reset=إعادة تعيين, On/Off=تشغيل/إيقاف, Yes/No=نعم/لا, Credits=الاعتمادات, Audio=الصوت, Default=الافتراضي, Accept=قبول, Close=إغلاق, New Game=لعبة جديدة, Save=حفظ). Stored in `ui_lock.csv`, validator-enforced. Extend with Crimson Moon buttons (Purify, Embark, Store, Loadout, War Table) after pilot.

## Punctuation, numbers, layout
- Arabic `،` `؛` `؟`; ellipsis single `…`; `؟` only for real questions.
- **Western digits 0-9 mandatory.** Validator blocks ٠-٩. Note: culture code `ar` may make ICU format engine numbers as Arabic-Indic; verify in-game with a numeric HUD/inventory screen. If it does, ship as `ar-MA` (MS2 precedent) and re-run the marker test.
- UI labels ≤ ~28 chars; respect `\n` exactly; watch terse HUD tokens (XP:, Lvl) for overflow.
- Rich text `<Header>…</>`, `<Emphasize>…</>`, input icons `<IA_Dodge/>`, args `{0}` `{ButtonText}` byte-identical.
- Subtitle cue rows (`_cue_N`) are fragments of the full line: translate the full line first, then split the Arabic at the same semantic breaks so cues concatenate to the full translation.

## Forbidden
Calques, dialect vocabulary, ASCII `?,;` inside Arabic, altered placeholders, translated debug/`FIX Insert`/Lorem ipsum rows, translated EULA/privacy legal rows (kept English; flagged `legal`), over-formal filler.

## Mandatory flow pass
After translation, before validation: contiguous-text pass (whole scene / whole note) for Arabic rhythm, connectors (ف، ثم، بل، إذ، أما…ف), redundancy cuts, idiom over calque, voice continuity. Light diacritics only on frozen lore terms and genuinely ambiguous words.

## LOCKED 2026-09-01 (Faisal)
- Nephilim = نيفيليم (transliterated; vocative أيها النيفيليم). "the Order" short form = **الجماعة** (full: جماعة القمر القرمزي). Archspire = أرشسباير. Player address masculine. Register split confirmed. Street NPCs = clipped MSA, no dialect. Mechanic list in `07_pilot_findings.md` §4 approved; all in `05_glossary.csv` status=approved.
- Stage cues: (growl)=(زمجرة) (grunt)=(همهمة) (laughs)=(يضحك) (sighs)=(يتنهد) — Gajov's cues never أنين (whimper).
- Diacritics: shadda + disambiguating marks only; no case-ending tanween on archaic speakers.
- UI: Execute (finisher) = إجهاز; Run/Excursion = جولة; Bindings = تعيينات.

## LOCKED 2026-09-02 (Faisal, pending-term round)
Block=صدّ · Parry=ردّ · Dodge=مراوغة · Crusader=الصليبي · Cain=قابيل (ميثاق قابيل) · Azrael=عزرائيل · St. Uriel=القديس أوريل · St. Enoch=القديس أخنوخ · Bishop Aaron=الأسقف هارون · Paladin=فارس مقدّس · District=المنطقة (Ward stays الحي) · The Coil=الطوق (Shattered Coil=الطوق المتحطّم) · Infernus=الجحيم · The Sundering=التمزّق · Demiurge=الديميورج · Transmitorium=غرفة الترسيخ · Pyresworn=قسم المحرقة · Karsivite Orthodoxy=الأرثوذكسية الكارسيفية · Prefect=أمين العقيدة · Advocate=الداعية · Infernal Flora=النباتات الجهنّمية · Flesh-Wrought Egregore=الإيقريقور المصاغ من اللحم · Covenant Cleric=كاهن الميثاق · Stamina=التحمّل (short form everywhere) · Lotte stays لوتّه · Lore Scrolls stays لفائف المعرفة · converged 10 approved (Physical Damage, Marked, HUD, Lives, Knight Terrors, Demon/Undead Brutes, Lunar Sentinel, Verdigris, Saedric).
