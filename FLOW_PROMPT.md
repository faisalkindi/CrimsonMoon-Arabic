You are running the FLOW PASS (Arabic prose quality) on the Arabic localization of Crimson Moon (gothic dark-fantasy souls-like, English original). The Arabic already exists, was edited for correctness, and passes a validator. Your job is not accuracy checking; it is making the Arabic READ like Arabic written first: rhythm, connectors, movement, voice continuity across a whole unit. Read each chunk's rows grouped by `unit` (a speaker's scene, one lore note, one item family, one quest line, one UI screen) as one passage before touching anything.

Read first: `C:\Users\Faisal\Ai\Mods Dev\CrimsonMoon-Mods\06_arabic_style_guide.md` (the "Mandatory flow pass" and LOCKED sections), `C:\Users\Faisal\Ai\Mods Dev\CrimsonMoon-Mods\05_glossary.csv` (status=approved renderings are frozen; keep them, inflect only as grammar requires), `C:\Users\Faisal\Ai\Mods Dev\CrimsonMoon-Mods\character_cards.yaml` (for dialogue rows, `speaker` names the card).

What to change (and only this):
1. Translationese sentence shape: Arabic carried on English clause order → recast with Arabic movement (verb-initial where natural, تقديم/تأخير for emphasis, clauses joined the Arabic way).
2. Connector poverty: chains of و → use ف، ثم، بل، لكن، إذ، حتى، أما…ف، لولا، وقد. One English sentence may become two Arabic ones, or two may join.
3. Rhythm and length: vary deliberately; lore/flavor wants short weighted clauses that land; UI wants terse verbal nouns.
4. Redundancy: cut copulas, dead pronouns, filler verbs Arabic implies.
5. Idiom over calque: a phrase that only makes sense by tracing the English fails; replace with the Arabic expression producing the same effect.
6. Voice continuity: one speaker sounds like one person across consecutive lines; a note reads in one hand.
7. Diacritics: shadda + genuinely disambiguating marks only; strip decorative case endings, never strip orthographic tanween (أيدٍ).
Register per row: dialogue = the speaker card's register (street NPCs stay clipped colloquial-flavored MSA, no dialect words; bosses/Solomon/Angel elevated; Gajov broken third-person); lore/items/quest names = elevated literary; skills/objectives/UI/system = plain, short. Player addressed masculine singular.

Untouchable: meaning and facts; every placeholder/tag in `placeholders` byte-identical, same count and order; same number of line breaks; numbers/dates verbatim; approved glossary terms; names (hard G = ق, V = ڤ); `max_chars_hint` rows must stay short; rows whose `ar` equals `source_en` (deliberately untranslated tokens) untouched.

Output: for chunk `f_NN.jsonl` write `C:\Users\Faisal\Ai\Mods Dev\CrimsonMoon-Mods\translated\flow_f_NN.jsonl`, one JSON object per input row, same order: id, source_en, ar_before, ar (final; identical if unchanged), editor_claimed_changed, reason (≤12 words, empty if unchanged), provenance {"stage":"flow","model":"claude-opus"}. Write with Python via Bash so escaping is exact. Self-check in Python before finishing: regex `\{[^{}]*\}|%[sdf]|<[^<>]+>` gives identical lists for ar and source_en, newline counts equal, row count equal. Process your assigned chunks in order, one output file per chunk. Report back only: per chunk rows/changed, and the 6 most instructive rewrites overall as `source_en → before → after`.
