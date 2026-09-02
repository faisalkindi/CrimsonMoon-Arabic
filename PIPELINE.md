# Pipeline notes (for contributors)

Working files, not needed to play. Everything player-facing is in the README and the Releases page.

## Layout

| Path | What |
|---|---|
| `PROJECT_STATE.md` | Running log: recon, decisions, every stage with dates |
| `01_corpus.jsonl` | Tagged source corpus (category, speaker, genders, placeholders, skip flags) |
| `03_working_draft.jsonl`, `04_final_corpus_v0.2.jsonl` | Merged Arabic corpus with per-row provenance |
| `04_game_context.md`, `04b_corpus_speaker_notes.md`, `character_cards.yaml` | World, cast, voices, gender evidence |
| `05_glossary.csv`, `05_glossary_rationale.md` | Frozen terminology (188 terms) and why |
| `06_arabic_style_guide.md` | Register, gender, punctuation, locked decisions |
| `07_pilot_findings.md` | Pilot results and rules folded into the pipeline |
| `translated/` | Stage outputs: `vllm_*` primary, `edit_*`, `verify_*`, `flow_*`, `qa_*`, `review_*`, `cues_*` |
| `review_findings/` | Dual-pass semantic review findings (A / B) |
| `installer/` | .NET 8 WinForms installer source |
| `release/` | Store texts and media |

## Stages (numbered scripts)

1. `01_build_corpus.py` tag corpus → `20_apply_cast.py` speaker/addressee genders
2. `100_build_batches.py` compile context-rich batches → `110_vllm_translate.py` primary draft (local vLLM)
3. Editorial pass (~400-row chunks) → `140_diff_verify_prep.py` → verify pass (~90-row chunks)
4. `200_prep_flow_chunks.py` → flow pass (contiguous scenes and notes)
5. `210_prep_review_chunks.py` → dual semantic review with a seeded control chunk → `220_apply_findings.py`
6. `50_mechanical_fix.py` deterministic sweep · `40_qa_validate.py` blocking validator · `70_derive_cues.py` subtitle cues
7. `80_build_locres.py` locres · `90_build_fonts.py` fonts · `build_mod.sh` pack + install

## Rebuilding

Needs the game installed (Steam), `repak`, Python 3 with `fontTools`, `arabic_reshaper`, `python-bidi`, `Pillow`, and the SST Arabic Medium font. Game files, extracted assets and built binaries are not committed.

- Extract: `repak unpack` the base pak for `Localization/**`, `UI/Fonts/**`, `Engine/Content/EngineFonts/Faces/**` into `extract/pak/`.
- Fonts: `python 90_build_fonts.py` (merges Arabic glyphs into Asul, Crimson Text and the engine Roboto faces, restores original vertical metrics, adds descender room).
- Locres: `python 80_build_locres.py` from `03_working_draft.jsonl`.
- Pack + install: `bash build_mod.sh build/ar_mod zzz_Arabic_P` (V11, mount `../../../`, Oodle, path-hash seed 2962377397 = 0xB0924AB5; `.ucas`/`.utoc` are renamed copies of `global.*`).
- Installer: `cd installer && dotnet publish -c Release -r win-x64 --self-contained -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true -o publish` after regenerating `payload.zip` from `build/`.

## Validator rules

Placeholder and line-break parity, Arabic punctuation, Western digits only, no bidi marks, no dialect tokens, no untranslated leakage, UI-lock vocabulary, approved-glossary presence (longest-term masking, stem match), dialogue attestations, number/date preservation, per-row exemptions via `validator_exempt`.
