# Crimson Moon — Arabic Localization

Complete Arabic localization mod for **Crimson Moon** (ProbablyMonsters, Unreal Engine 5, Steam build 1.0.0.160034): every string in `Game.locres` (8,600+ rows), the intro and ending cinematic subtitles, and Arabic glyphs merged into the game's own fonts. Ships as an IoStore patch triple plus two `.srt` files; no original game file is modified.

Player-facing description and install steps: [`release/dist/NEXUS_DESCRIPTION.md`](release/dist/NEXUS_DESCRIPTION.md).

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
| `review_findings/` | Dual-pass semantic review findings (A = Opus, B = Sonnet) |
| `installer/` | .NET 8 WinForms installer source |
| `release/` | Nexus texts and media |

## Pipeline (numbered scripts)

1. `01_build_corpus.py` tag corpus → `20_apply_cast.py` speaker/addressee genders
2. `100_build_batches.py` compile context-rich batches → `110_vllm_translate.py` primary draft (local vLLM)
3. Editorial pass (Sonnet subagents, ~400-row chunks) → `140_diff_verify_prep.py` → verify pass (Opus, ~90-row chunks)
4. `200_prep_flow_chunks.py` → flow pass (Opus, contiguous scenes/notes)
5. `210_prep_review_chunks.py` → dual semantic review with seeded control chunk → `220_apply_findings.py`
6. `50_mechanical_fix.py` deterministic sweep · `40_qa_validate.py` blocking validator · `70_derive_cues.py` subtitle cues
7. `80_build_locres.py` locres · `90_build_fonts.py` fonts · `build_mod.sh` pack + install

Game files, extracted assets and built binaries are not committed. Rebuild needs the game installed, `repak`, `fontTools`, and the SST Arabic font.

## Font

SST Arabic Medium (Samsung) glyphs are merged into the shipped faces for non-commercial use only.
