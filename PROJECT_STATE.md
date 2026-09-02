# Crimson Moon — Arabic Localization — PROJECT_STATE

Updated: 2026-09-01 (Phase 1 recon)

## Game
- Path: `F:\SteamLibrary\steamapps\common\Crimson Moon` (32 GB)
- Exe: `CrimsonMoonNG/Binaries/Win64/CrimsonMoonNGSteam-Win64-Shipping.exe`, build `++CM+release-CL-160034` (2026-08-20)
- Developer: ProbablyMonsters (custom engine plugins under `Engine/Plugins/ProbablyMonsters`, Yeti services, PMUI, Gridly loc plugin). UI built on Lyra (`Content/UI/LyraUI`).
- Source language: **English** (dev = US studio, Gridly config, en locres is the source). Other 7 cultures fully translated (same row count).

## Recon answers (6 questions)
1. Engine: UE5, most likely **5.6** (utoc TOC version `ReplaceIoChunkHashWithIoHash`, container header `SoftPackageReferencesOffset`, exe strings mention up to UE5.6). Confirm via marker test.
2. Pak format: `CrimsonMoonNG-Windows.pak` V11 (Fnv64BugFix), mount `../../../`, Oodle, **path hash seed `B0924AB5`**, 2497 entries (ini/locres/ufont/ttf/res/png). IoStore `.utoc`/`.ucas` 31 GB, 98,959 chunks, 62,400 packages, Oodle, `global.ucas` 4 MB.
3. Encryption: **none** (encrypted index false, GUID zero).
4. usmap: not yet generated (needed only for cooked-asset edits: fonts/widgets/StringTables via UAssetGUI/retoc to-legacy). TODO.
5. Text storage: **locres** at `CrimsonMoonNG/Content/Localization/Game/<culture>/Game.locres` (locres v3, inside the .pak). 8,969 rows / ~88.9k words / 516k chars, 81 namespaces. Also 33 StringTable assets under `Content/Data/StringTables/` (ST_*) — cooked, but their text is already collected into locres. Subtitles for .bk2 movies = loose `.srt` in `Content/Movies` (per-language, 8 langs).
6. Culture slot: **RESOLVED 2026-09-01 — no hijack needed.** Dropping `ar/Game.locres` registers a native "Arabic" entry in the Lyra language picker; game auto-selected it (Windows locale ar). Marker `[AR]` visible on every settings string. Screenshot `build/marker_test_pass.png`.

## Fonts
- Game UI: `Content/UI/Fonts/` — Font_Asul (Asul Regular/Bold), Font_Crimson_Text (5 faces), Font_Subtitles, plus NotoSansJP/SC fallback faces; 50+ TextStyle_Asul* assets.
- PMUI_SocialManagement plugin ships NotoSans faces (Bengali/Devanagari/JP/KR/SC/Thai) — **no Arabic face anywhere in game content**. Engine Slate has `NotoNaskhArabicUI-Regular.ttf` (engine fallback only).
- Plan: SST Arabic Medium (sanitized) injected as fallback into Font_Asul / Font_Crimson_Text / Font_Subtitles composite fonts.

## Corpus shape (en)
- Dialogue: `Verbals/VC_VerbalsNPC_*` namespaces (Merchant 542, Angel_Male 462, Librarian 449, Hub_Monk_1 426, Gallant 323, Solomon 306, Blacksmith 251, Door_* NPCs, boss taunts) — scene-split, needs speaker/addressee gender pass.
- System/items: ST_LoreNotes 378, ST_Objectives 358, ST_Armor 276, ST_Quests 219, ST_BoonDescriptions 192, ST_Trinkets 145, ST_WarTable 107, ST_Weapons 92, ST_WeaponArts 65 ...
- Empty namespace 2,476 rows (widget-inline text = UI).
- Placeholders: `{0}` `{1}` `{ButtonText}` `{Count}`, rich text `<Header>…</>`, `<Emphasize>`, input icons `<IA_Dodge/>` etc.

## Delivery (VERIFIED 2026-09-01)
- IoStore triple `zzz_<Name>_P.{pak,ucas,utoc}` in `Content/Paks/`; `.ucas`/`.utoc` = renamed copies of `global.*`; pak V11, mount `../../../`, Oodle, seed **decimal 2962377397** (= 0xB0924AB5; repak `-p` takes decimal only). Script: `build_mod.sh <staging> <Name>`.
- Locres v3 rewrite tool: `locres_tool.py` (keeps entry table, rewrites string array).
- Shipping build writes no `Saved/Logs` — engine version still unconfirmed (5.6 likely); no log-based diagnostics available, marker tests only.
- Currently installed: `zzz_ArabicMarker_P` (ar = en with `[AR] ` prefix). Remove before shipping.
- Config: `Slate.DefaultTextFlowDirection=0` (Auto, never 2).

## Workspace
- `en_source.csv` (namespace,key,en) — 8,969 rows
- `extract/pak/` — Config + all locres (Game/Engine/Online/XeSS)
- `extract/pak_list.txt`
- Tools: repak `Ai/Tools/repak`, retoc 0.1.5 `Ai/Mods Dev/CodeVein2-Mods/tools/retoc`, UAssetGUI `Ai/Tools/UAssetGUI`

## Next
1. Font: get Arabic glyphs rendering — usmap → edit Font_Asul / Font_Crimson_Text / Font_Subtitles composite fonts (add SST Arabic Medium fallback) → IoStore triple via retoc to-zen; test with real Arabic string in ar locres.
2. usmap via Dumper-7/UE4SS for font/widget edits.
3. Foundation artifacts (Ch3): tagged corpus with speaker_gender from `Verbals/VC_*` speaker names, game-context file, glossary, style guide, validator.
4. Pilot 200–500 lines (UI + one NPC scene).


## Method track (arabic-localization skill) — status 2026-09-01 22:20
Foundation artifacts (Ch3):
1. File audit — DONE (this file, recon section).
2. Tagged source corpus — DONE `01_build_corpus.py` → `01_corpus.jsonl` (8,969 rows; categories dialogue 3373 / ui_inline 2327 / quest 741 / item 687 / system_online 401 / skill 380 / lore 378 / ui_menu 278 / ui_settings 173 / achievement 64 / system 17; 192 skip rows = legal EULA/privacy, Lorem ipsum, FIX Insert, symbols). `speaker` from Verbals namespace; `speaker_gender`/`addressee_gender`/`scene_id` to be filled from cast pass.
3. Game-context file — IN PROGRESS (agent lore-context → `04_game_context.md`; cast agent → `04b_corpus_speaker_notes.md` + `character_cards.yaml`). Interim `context_card.md` used for pilot prompts.
4. Glossary — `05_glossary.csv` raw candidates (1,115 proper nouns + 46 mechanics, all `pending`, `approved_ar` empty by design). Curate after pilot + lore agent.
5. Style guide — `06_arabic_style_guide.md` draft v0 (split register, masculine player default per FR evidence, Western digits, UI lock in `ui_lock.csv`).
6. QA validator — `40_qa_validate.py` blocking (placeholder parity, newline parity, ASCII punct, Arabic-Indic digits, bidi marks, dialect tokens, leakage, UI length, UI lock, approved glossary, dialogue attestations). Verified: caught 3 real defects in pilot draft.
7. Enforcement package — `100_build_batches.py` (compiler: rejects dialogue without card/gender; injects card, glossary hits, rules), `110_vllm_translate.py` (stage 2 primary via local vLLM gemma4-12b-awq, sentinel-masked controls, parity check, split-on-overflow), `130_merge_draft.py`, `140_diff_verify_prep.py`.

Pilot COMPLETE through stage 5 (see `07_pilot_findings.md`): vLLM primary → 3 Sonnet editors (61 changes) → validator PASSED → Opus verify (52/8/1). Awaiting human glossary decisions + Sonnet Arabic QA + in-game QA (font).

Pilot (Ch4 step 6, Ch12 route = mandatory local vLLM primary): 310 rows selected (`pilot_ids.txt`: 210 functional + 100 dialogue across 7 speakers). Functional half drafted (210 rows, ~4 min incl. retries; 1 empty legal row now skipped; 1 duplicated tag; 2 UI-lock misses; name transliteration drift جالانت vs ق rule). Editorial pass running (Sonnet agents edit-ui / edit-content). Dialogue half blocked on `character_cards.yaml` (gender) — compiler enforces.

vLLM server: WSL2 `~/vllm-env`, model `~/models/gemma-4-12B-it-AWQ-INT4` served as `gemma4-12b-awq` on 127.0.0.1:8000 (`--max-model-len 4096`). Start command in `arabic-localization` skill Ch19.

Open decisions for pilot review: Nephilim rendering (نيفيليم transliteration proposed); `ar` vs `ar-MA` culture code (ICU digit risk); player gender default (masculine, FR evidence 19 vs 0 true feminine hits); street-NPC eye-dialect strategy (register not dialect).

## Batch loop status 2026-09-01 23:05
- Glossary LOCKED by Faisal (146 approved, 21 pending): Nephilim=نيفيليم, the Order=الجماعة, Archspire=أرشسباير, mechanic list. `35_approve_glossary.py` is the audit of what was approved.
- Pilot: QA pass (Sonnet, 32 fixes) → validator PASSED. Final in `03_working_draft.jsonl` (qa stage). Human linguistic read + in-game QA still owed.
- Batch 1 UI (2,777 rows): vLLM 177 s → mechanical (`50_mechanical_fix.py`: variants, UI lock, adjacent-dup tag collapse) → 7 Sonnet editors (edit_chunks/b1_*) running.
- Batch 2 system/online/achievement (479): drafted, 2 editors running.
- Batch 3 item/skill (1,067): drafting in background.
- Next: verify stage per batch (Opus on changed rows), merge, then batch 4 quest (741), batch 5 lore (378), batch 6 dialogue (3,373; needs per-line speaker pass for NPC_Solomon/NPC_Angel_Male voice banks + scene ordering).
- Validator glossary matcher: longest-term-wins masking, article/clitic/harakat-insensitive.

## 2026-09-01 23:15 — batch loop progress
- Batch 1 UI (2,777) and Batch 2 system (479): primary → mechanical → edit → verify → merge → validator PASSED. Finals `b1_final.jsonl`, `b2_final.jsonl` (also in `03_working_draft.jsonl`).
- Batch 3 item/skill (1,067): editors 02/03 done, 01 pending → then verify.
- Batch 4+5 quest/lore (1,081): drafted; 5 editors running (lore with flow pass).
- Batch 6a dialogue single-speaker banks (1,161 non-cue rows): drafting. Stage-1 speaker resolution running on NPC_Solomon/NPC_Angel_Male (768 rows) → batch 6b.
- Corpus skip now 274 (legal, dev tokens, format-only `{Stat}: {X}`, editor-recommended).
- Validator tuned: longest-term masking (all occurrences), stem match for plurals/nisba, ASCII punct only when touching Arabic, corrupt-char check.
- Pending human glossary calls (30 pending rows): Block/Parry/Dodge, Crusader (draft المجاهد — jihad connotation), Covenant Cleric, Paladin, Physical Damage/Marked/HUD/Lives (editors' unifications), Eden, Cain, saints, Azrael, Egregore, Coil.
- Subtitle cue rows (`_cue_N`, ~1,900) not yet translated: derive by splitting the full-line Arabic (planned script).

## 2026-09-01 23:20 — near-complete first pass
- Coverage: 8,694 / 8,695 translatable rows carry Arabic (274 skip). Batches 1,2,3,6a + cues PASS validator. Batch 4+5 (quest/lore) and 6b (mixed banks) in verify/edit.
- Cues: `70_derive_cues.py` splits full-line Arabic into `_cue_N` fragments (554/555 clean). Validator treats cue rows as fragments.
- Locres builder: `80_build_locres.py` → `build/ar_mod/.../ar/Game.locres` (string table rebuilt per key; English fallback for skip rows). Ship via `build_mod.sh build/ar_mod zzz_Arabic_P` (replaces marker mod).
- Recurring model defect classes now enforced: Church≠الجماعة (approved term), dialect tokens list, Gildenarch/Grimhaven confusion (glossary), Spire vs Archspire, tanween strip on archaic speakers, ⟦REVIEW⟧ leak strip.
- Still owed before "done" (Ch15 gates): human linguistic read (Faisal), pending glossary decisions (34), in-game QA (blocked on Arabic font), TM append only after those.

## 2026-09-01 23:30 — v0.1 FULL PASS ASSEMBLED
- Whole corpus validator: PASSED (8,969 rows; 283 skip; all dialogue rows carry attestations).
- Snapshot `04_final_corpus_v0.1.jsonl`. Locres built by `80_build_locres.py`; installed as `zzz_Arabic_P.{pak,ucas,utoc}` (marker mod removed).
- Provenance per row in `provenance` list (primary/edit/verify/qa/cue_derive). Patch files `translated/qa_zz_*` merge last by design.
- NOT done (Ch15 gates): human linguistic read; 37 pending glossary terms; in-game QA — Arabic glyphs cannot render until the font track ships (Font_Asul/Crimson_Text/Subtitles need an Arabic fallback face).
- In-game load test 2026-09-01 23:35: `ar` selectable, locres loads, every label swaps, no crash — text INVISIBLE (no Arabic glyphs in Asul/Crimson Text/Subtitles fonts). Language dialog then unusable, so the triple was UNINSTALLED; rebuild+install with `bash build_mod.sh build/ar_mod zzz_Arabic_P` once the font mod exists. Game's saved language may still be `ar` (falls back to English without the mod).

## 2026-09-01 23:40 — FONT TRACK SHIPPED (v0.1 playable)
- `90_build_fonts.py`: SST Arabic Medium (sanitized) glyphs merged INTO Asul x2 + CrimsonText x5 (Latin kept), original vertical metrics restored, yMin lowered for descenders, wrapped .ufont. No usmap, no UAssetGUI needed — .ufont payloads live in the pak and override via the `_P` triple.
- Installed `zzz_Arabic_P` = 7 fonts + ar locres. In-game: title, main menu, settings tabs (RTL-mirrored), controller map, save slots all render shaped Arabic. Screenshots `build/qa_0*.png`. Clean exit (no crash dir / event log).
- Not yet seen in-game: subtitles font (Font_Subtitles composite — may reference a Noto face), HUD in gameplay, dialogue boxes, lore scroll layout, mixed-direction strings with placeholders. Faisal to play the tutorial with the mod and report.
- Known visible glossary gap: LB and LT both labelled صد (Block vs Parry pending).
- vLLM server still running in WSL (background job); stop with `wsl -- pkill -f vllm` when done.

## 2026-09-02 05:00 — flow pass + glossary lock
- MS2-style flow pass done: 35 chunks, 12 Opus agents, 2,574 / 6,771 rows reshaped (`translated/flow_f_*.jsonl`, stage `flow`). Many gender/agreement/meaning fixes surfaced too.
- Faisal decided all 36 pending terms (AskUserQuestion rounds) → glossary 188 approved / 0 pending; style guide LOCKED 2026-09-02 section. Mechanical variants extended; 255 rows swept (`translated/qa_zz_mech_0902.jsonl`). 78 rows in Sonnet conformance pass (`conform-0902`).
- Next: merge → cues → validate → `210_prep_review_chunks.py` → dual semantic review (Opus pass A + Sonnet pass B, 90-row chunks, seeded control r_900) → apply findings → rebuild → Faisal gameplay QA.
- Open small calls: "The Stricken Testament" (الموبوءة vs المشطوبة), "Lichdom" rendering.

## 2026-09-02 05:25 — v0.2 INSTALLED (flow + glossary lock + dual semantic review)
- Dual semantic review done: 76 chunks × 90 rows; pass A Opus (8 agents) 6/6 on seeded control, pass B Sonnet (4 agents, spawned sub-workers that collided on files but final state verified) 5/6. 515 rows with findings, 510 applied (139 critical), 4 rejected by frozen-term guard (`220_apply_findings.py`, stage `review`, files `translated/review_zz_*`).
- Whole corpus validator PASSED. Snapshot `04_final_corpus_v0.2.jsonl`. Built + installed `zzz_Arabic_P` (7 merged fonts + locres, 8,664 Arabic rows, 305 English fallbacks incl. 22 dev strings reviewers reverted).
- Cinematic subtitles translated and installed: `Content/Movies/Intro_ar.srt`, `CINE_EndGame_ar.srt` (loader picks `_<culture>.srt`? unverified in-game).
- Remaining: Faisal gameplay QA (subtitles font, HUD, dialogue boxes, lore scrolls, overflow), layout fixes, installer/Nexus, SST licence note. Systemic notes from reviewers not yet swept: تطهير doing Purify+Clear+Cleanse; Scrap 4 renderings; heretic vs Apostate (المرتد); Paladin vocative in Gallant lines.

## 2026-09-02 10:15 — subtitles font fix
- Faisal QA: all text renders except subtitles = "????". Cause: `Font_Subtitles` composite references ENGINE faces `/Engine/EngineFonts/Faces/Roboto{Regular,Bold,Italic,BoldItalic}` (+NotoSansJP/SC), not the game faces. Fix: same SST merge into 6 Roboto engine faces, staged under `build/ar_mod/Engine/Content/EngineFonts/Faces/`, mod now 13 fonts + locres (14 entries). Installed; awaiting retest.

## 2026-09-02 10:25 — v0.2.1 installed
- Faisal confirmed subtitles render after Roboto engine-face merge. Sweep done: Paladin=فارس مقدّس in 10 rows, Scrap=قصاصة, Cleanse/Clear/Purge distinct from Purify (glossary +6 terms: Heretic, Heresy, Clear, Cleanse, Purge, Scrap), 8 other-sense rows exempted. Validator PASSED; rebuilt + installed (14 entries).
- Remaining: Faisal layout QA notes; installer/Nexus/licence.

## 2026-09-02 10:30 — RELEASE PACKAGE v0.2
- Installer: `installer/` (.NET 8 WinForms, ported from MS2; AppId 4317690; payload = triple + 2 srt; installs to Paks + Movies; headless `--detect/--install/--uninstall` verified on a fake root). Published `release/dist/Crimson Moon Arabic Installer.exe` (69 MB) + `CrimsonMoon_Arabic_Installer.zip` + `CrimsonMoon_Arabic_Manual.zip` (files in game-relative paths).
- Nexus: `release/dist/NEXUS_DESCRIPTION.md` (AR+EN), `SHORT_DESCRIPTION.txt`; media `release/media/00_thumbnail_1920x1080.jpg`, `01_header_1400x400.jpg`, `02..04` screenshots, `logo_crimson.png` (logo red #f83830 from title screen). Installer screenshot (05) still to capture when game not fullscreen.
