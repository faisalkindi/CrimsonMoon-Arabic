# Crimson Moon — speaker / cast notes (from `research/dialogue_all.txt`)

Source: 3,373 rows, 1,458 canonical (non-`_cue_`) lines, 20 speaker namespaces. FR column is only ~76% translated (1,105 canonical lines differ from EN; rest are EN fallback). Gender evidence below cites EN pronouns first, FR agreement second. Nothing guessed: no evidence = `unknown`.

**Namespace caveat.** A namespace is a *voice bank*, not strictly one speaker. `NPC_Solomon` contains reply lines clearly spoken by the Angel/Nephilim ("The Church has no control over my mind and neither do you Solomon", "Believe not his lies Nephilim", "Gallant will protect me", "Silence deceiver! Reveal yourself", "You misled the people of this city…" which also appears under `NPC_Angel_Male`). `NME_Boss_Felwyl_TA` contains "…were stronger than we could have anticipated, and thus deviation is... necessary" (reads as Solomon/Felwyl cutscene exchange). `NPC_Angel_Male` contains lines in the Nephilim's own voice ("Yes, Knight Commander. I understand.", "Humanity needs a savior. May as well be me.") — Angel and Nephilim share one body after the Soul Siphon, so first person is shared. Speaker gender for these stray lines is still masculine (Angel m, player m), so the Arabic result is unaffected, but translators should read each line, not trust the namespace for *who is addressed*.

---

## Player (the Nephilim) — how addressed, and gender

**Forms of address by speaker**
| Speaker | Terms used |
|---|---|
| Angel | Nephilim, "mighty Nephilim" |
| Gallant | Nephilim, Paladin, Knight, "my brother" |
| Librarian (Mereda) | Nephilim, knight, child, dear, brute, dog ("To war, dog") |
| Merchant (Lotte) | friend, mate, chap, sir, sonny, "the stray", "'alf breeds", "my favorite Nephilim" |
| Hub Monk | Nephilim (direct); "the Knight" / "the Nephilim" (third person, about the player) |
| Blacksmith (Gajov) | pup, "stray pup", "good pup", nephilim, friend, "strong one" |
| Solomon | Nephilim, "dear Nephilim", dog, hound, slave, "Another Nephilim for the slaughter" |
| Felwyl | Nephilim, Aether Spawn / aether-spawn, "the hound", "one of the Church's hounds" |
| Mahkteah | Nephilim, welp, "advocate of man", "Child of Luderaeon" |
| Valahk-Nor | wretch, creature, "Soul torn Aether-Spawn" |
| Door Priest | child, "You, he who is caught between realms", Nephilim |
| Door NPCs | stranger, beast, Nephilim, dear/darlin' (Female_3), Solomon (Female_2 mistakes player for Solomon), friend, "'alf breed", mate |

**EN evidence for player gender (masculine)**
- Gallant: "Nephilim, I am proud to call you my **brother**."
- Felwyl: "Your **brothers** await you in the garden."
- Librarian: "it's very sad what happened to your **brothers** out there."
- Door Priest: "You, **he** who is caught between realms."
- Door Female_2 addresses the player as **Solomon** ("Go on then, Solomon", "the man who captivated an entire city").

**FR agreement hits addressed to the player**

| Gender | Hits | Examples (speaker → FR) |
|---|---|---|
| masculine | 28 | Angel "Vous êtes maintenant **prêt**", "Lève-toi, **puissant** Nephilim", "sans y être **préparé**", "Soyez **prudent**" · Gajov "Reviens quand tu seras **prêt**", "Sois **fort**", "Mon **ami**", "Ce toutou est **doué**" · Gallant "Tu es **prévenu**", "Ce que tu es **devenu**", "Tu es plus **fort**", "Sois **impitoyable**, mais pas **imprudent**", "Vous êtes **allé** plus loin", "**Prêt** pour un vrai combat ?" · Librarian "tu es plutôt **doué**", "mon **cher**" (x2), "Tu es **confus**", "Tu es **curieux**", "Où étais-tu **passé**", "**Celui** qui mettra fin à la Foi" · Lotte "**Prêt** à relever le défi ?", "Sois pas **surpris**", "vous êtes **fauché**", "**monsieur**", "mon **pote**/mon **ami**" · Solomon "Tu n'es pas **fatigué**" · Felwyl "Tes **frères** t'attendent" · Female_2 "vous êtes finalement **revenu**" |
| feminine | 4 | Librarian "Ils t'ont **tuée** ? Je suis vraiment désolée, **ma chère**" (one line; its sibling variant says "Ils vous ont **tué**… désolé, ma chère" — contradictory within itself) · Librarian "Remets-les… **mon cher**" vs. same speaker "**ma chère**" · Female_3_2D "**ma chère**" (x2, translating "dear"/"darlin'") |
| explicit both | 1 | Librarian "Vous êtes **celui ou celle** qui a survécu au Siphon d'Âme" |

**Conclusion:** the player is masculine. 28 masculine vs 4 feminine; every feminine hit is "ma chère" rendering EN "dear/darlin'" (a translator reflex, and contradicted in the same speaker's other lines) plus one stray "tuée". One line hedges with "celui ou celle". Default `addressee_gender = m` for all player-directed lines.

---

## NPC_Angel_Male — the player's guardian Angel
- **Name:** UNCONFIRMED. Gallant's line "Nahnias fights beside you now. Never take that loyalty for granted." may name the Angel, but nothing ties "Nahnias" to the Angel explicitly.
- **Role:** the player's bound Angel; shares the body after the Soul Siphon ("I've felt part of me slowly merge with you"). Narrates exploration, quest hints, combat callouts, and lore commentary.
- **Gender:** m (namespace `_Male`; text has no self-pronoun. FR self-refs are gender-neutral: "Je suis à tes côtés, pour toujours"). Treat as masculine per the namespace.
- **Addresses:** the player (Nephilim), occasionally enemies (Solomon, Valahk-Nor). FR mixes *vous* (tutorial/mission lines) and *tu* (field lines).
- **Relationship:** protector-companion, increasingly fused with the player: "I am by your side, always." "I will not hurt you. I swear to protect you and guide you on your quest."
- **Voice:** formal, earnest, reflective; poses rhetorical questions about faith and institutions; frequently plural "we/us/our" (shared body). Some lines are the Nephilim's own voice.
- **Register:** elevated, sober. **Profanity:** none.
- **Representative lines:**
  1. "Nephilim, remember my voice. This is your angel speaking. Our orders are to regroup with Knight Captain Rendaen and your comrades within Gildenarch. Get to work."
  2. "I am at full strength. My power is yours to wield."
  3. "Does power truly corrupt or does it reveal what truly lies within our hearts?"
  4. "They call you sin. I call you salvation."
  5. "The Church, the Academy, the ruling class. Every institution failed these people."

## NPC_Blacksmith — Gajov
- **Name:** Gajov (self-named constantly). Surname "Resnyk" does NOT appear anywhere in the corpus — UNCONFIRMED.
- **Role:** the Order's blacksmith; a Karsivite vampire ("They call me animal. But Gajov no animal"), conscripted by Gallant; worships Vodor / "Lady Vodor" and "Pack in the sky".
- **Gender:** m. EN: Gajov "Bring Gajov what **he** need"; Librarian "see the Blacksmith. **He's** one himself"; Monk "the wolf-boy", "**He** was working anyway". FR: "Gajov est **prêt**".
- **Addresses:** the player ("pup"), Gallant, Mereda ("Lady Mereda"), Vodor (prayer).
- **Relationship:** gruff mentor/quartermaster; warms up over time ("You're like Gallant. Gajov trust you." "You... thank you... pup.").
- **Voice:** broken English, third-person self-reference, dropped articles and copulas, imperative fragments, dog metaphors (pup/fetch/toy), growls and grunts in stage directions. Occasionally full grammatical sentences in lore lines ("Dragon bones were highly sought after by Karsivites. Allow Gajov to show you why.").
- **Register:** comic-menacing, blunt. **Profanity:** none (threat: "Nice neck. Come closer Gajov hungry.").
- **Representative lines:**
  1. "Bring Gajov material, Gajov forge. Understand?"
  2. "Good pup. Now, buy new toy. Kill gods."
  3. "No touch sword! ...Not ready. More hit."
  4. "Fire speak to Gajov. Gajov listen."
  5. "By Vodor and Pack in the sky! Mighty fangs for a true dire wolf of Karsiv!"

## NPC_Librarian — Mereda
- **Name:** Mereda (cross-referenced, never self-named): Gallant "speak with Mereda, the Order's archivist"; Angel "Mereda should be done studying that text" ↔ Librarian "Give me some time to study it"; Monk "The Nephilim and Librarian are much in each other's company" ↔ "You spend long hours with the Librarian… what **she** has you reading". Surname unknown.
- **Role:** the Order's archivist; immortal ("Written over one hundred years ago. When I was still mortal."), conscripted by the Faith; deciphers texts, forges requisitions with Lotte; romantic subtext with the player per Gallant.
- **Gender:** f. EN: Monk "what **she** reads by it"; Merchant "**lass** has been waitin'", "**She's** in on it"; Gallant "when **her** and I had just met". FR: "**Contente** de te revoir, chevalier"; "Je suis vraiment **désolée**". (One FR variant has "désolé" — translation inconsistency.)
- **Addresses:** the player (knight / child / Nephilim / brute / dear / dog), Gajov (via player).
- **Relationship:** dry, condescending scholar who grows fond; pays in "powerful magic".
- **Voice:** archaic-literary tics ("'Tis", "'fore all is lost", "what bringith", "Tell him I sent ye"), bookish sarcasm, exposition monologues; irritable when interrupted.
- **Register:** elevated / archaic with comic bite. **Profanity:** none (insults: brute, dog, stupid).
- **Representative lines:**
  1. "What am I reading? You're curious for a Nephilim. 'Tis a story about the Infernal Legion."
  2. "Are you addled or just stupid?"
  3. "Having trouble finding that tome? Hmm... Look around. Books look much like the rectangular objects in this room."
  4. "Do not be afraid Nephilim. I was there to witness the first of your kind."
  5. "We need more information, knight. To Gildenarch with you. Make haste, 'fore all is lost."

## NPC_Merchant — Lotte Ananta
- **Name:** Lotte Ananta. EN self-names as "Lotte"/"ol' Lotte"; FR: "Car moi, **Lotte Ananta**, je suis là pour te fournir…". Librarian: "Lotte. One of the most wanted thieves in Eden."
- **Role:** potion/trinket vendor; former master thief, cursed by a Cathedral artifact to be grotesquely bloated and immobile ("Used to fit through a keyhole, me. Now I AM the keyhole."), technically dead ("Not bad for a dead man"). Questline: locket, chalice, crew's fate, lost love Aleria Hawthorn.
- **Gender:** m. EN: Angel "Lotte's been busy… lets check in with **him**"; Monk "Lotte cannot leave **his** chair"; Merchant "you're talking to the **man** who did"; stage direction "{counting coin under **his** breath}". FR: "je me suis **retrouvé**", "je suis **du coin**", "**un** chat de gouttière".
- **Addresses:** the player (friend/mate/chap/sir), Gajov ("Gajov, mate").
- **Relationship:** transactional patter that turns into genuine friendship ("I consider you a dear friend").
- **Voice:** London-ish cockney: dropped g's ("lookin'", "nickin'"), dropped h's ("'ere", "'alf"), "innit", "cor", "ya/yer", "skint", "git", "wanker", "sod", "Toffs"; salesman patter; self-deprecating fat jokes; sudden sincerity.
- **Register:** comic-plain, streetwise. **Profanity:** mild-moderate (bloody, bastard, wanker, sod, ass, "Screw me").
- **Representative lines:**
  1. "Ain't no charity 'ere sir. We've nuff to worry about without Lotte running out of the good stuff."
  2. "Felwyl the Withered. Lich. Wanker. Good luck, friend."
  3. "Ya killed the Dry Rot King? A DEAD GOD? Mate. Mental, that. Absolutely mental."
  4. "If I had a soul left to swear on, I'd swear on it for ya."
  5. "A profit a day keeps the Divine away."

## NPC_Hub_Monk_1 — unnamed brother of the Sanctus
- **Name:** UNCONFIRMED (never named; refers to "the brothers", "the Faith").
- **Role:** monk of the Lunitarian Faith stationed in the Order's hub; keeper of registers, candles, plates; ex-novice under Gallant in the Crusade; nervous observer and gossip.
- **Gender:** m. EN: implicit only (monk among "the brothers"). FR: "Je ne devrais pas me sentir **soulagé** quand ils échouent."
- **Addresses:** the player (Nephilim), often speaking *about* the player in third person ("The Knight is back. The bells were rung.").
- **Relationship:** wary, superstitious, quietly sympathetic; suspicious of Merchant and smith.
- **Voice:** aphoristic, liturgical repetition ("Lunarin watches. Lunarin keeps. Lunarin remembers."), flat declaratives, understatement, "I am told… I am told." refrain, "The brothers do not speak of this."
- **Register:** elevated, formal, deadpan-unsettling. **Profanity:** none.
- **Representative lines:**
  1. "The Faith permits silence. The Faith does not permit absence. Find the line between."
  2. "The Merchant pays for his keep in souls. We are told this is metaphor. We are told this is metaphor."
  3. "Gallant Alexander is, by all the proper measures, a great man. He is also the first Nephilim. The two things must be held together."
  4. "I counted my fingers. I counted them twice."
  5. "Touch the doorframe before you cross it. Lunarin does not enter rooms he was not invited to."

## NPC_Gallant — Gallant Alexander
- **Name:** Gallant Alexander (Angel: "Seek Gallant Alexander, the Knight Commander of the order"; Librarian: "The Knight Gallant Alexander").
- **Role:** Knight Commander of the Order of the Crimson Moon; the first Nephilim (~300 years old); led the Apostate Hunts; slayer of Valahk-Nor.
- **Gender:** m. EN: Monk "Older than **he** looks"; Solomon "**He** who helped enslave…"; Gallant "Nephilim, I am proud to call you my brother". FR: "j'ai été **tué** par une vampire amoureuse", "Je serai **prêt**".
- **Addresses:** the player (Nephilim / Paladin / Knight), Mereda.
- **Relationship:** commander → surrogate elder brother; "I want you by my side when it comes."
- **Voice:** military terse: short imperatives, maxims ("Be ruthless, not reckless." "Failure is information. Use it."), occasional weary gallows humour; contract-board one-liners.
- **Register:** plain-commanding, laconic. **Profanity:** none.
- **Representative lines:**
  1. "Death is not failure. Staying down is."
  2. "The church fills cathedrals. We fill graves."
  3. "Your angel is strong. You are stronger. Keep that balance. I've seen what happens when it tips."
  4. "What you've become - the Church has no name for it. I do. It's called whole."
  5. "Come back breathing."

## NPC_Solomon — Solomon Moore
- **Name:** Solomon Moore (Librarian: "letters from Solomon Moore. This 'philanthropist'…").
- **Role:** antagonist; ex-clergyman turned industrialist, architect of the Godsreach Spire; servant of Cain; lost wife Deliliah and son to crusaders; voice from the Spire tempting the player.
- **Gender:** m. EN: Angel "Solomon may have a point, but **he** isn't right"; Solomon "my dearest Deliliah… my son"; Female_2 "the **man** who promised to rebuild Gildenarch". FR: neutral.
- **Addresses:** the player (Nephilim/dog/hound/slave), the Angel, Gallant (rhetorically), Felwyl.
- **Relationship:** tempter/manipulator offering "freedom" from the Church.
- **Voice:** polished rhetoric, philosophical monologue, sneering condescension, rhetorical questions ("Hmm?"), long exposition.
- **Register:** elevated, menacing-persuasive. **Profanity:** none.
- **Representative lines:**
  1. "Sheep want Shepherds; they don't care if they're led to the pastures or the slaughter."
  2. "Go on, bring that stone back to the Church. Be a good slave! Your orders are to do, not to think."
  3. "Any end can justify the means dear Nephilim. One day soon you will learn this!"
  4. "Welcome back, hound."
  5. "Humans are merely narrative animals; they care not for what truly is, but for how something feels."
- Note: this bank also holds Angel/Nephilim replies (see caveat above) — assign speaker line-by-line.

## NME_Boss_Felwyl_TA / NME_Boss_Felwyl_TW — Felwyl the Withered
- **Name:** Felwyl the Withered (Merchant), lich; ex-teacher at the library (Monk).
- **Role:** boss; master of the Garden / Red Bloom / Hellgrowth; ally-then-rival of Solomon; aspires to be "new Lord of Akyreon". TA = ascended/late form, TW = withered/early form.
- **Gender:** m. EN: Gallant "Felwyl came back. Of course **he** did… you put **him** in the ground"; Solomon "**he** had plans of **his** own". FR: "Je suis le **maître** des dieux morts", "le **nouveau** seigneur d'Akyreon".
- **Addresses:** the player (Nephilim / Aether Spawn / hound), Solomon.
- **Voice:** grandiose, botanical death imagery (Garden, Bloom, vines, viscera, carrion), languid contempt ("This again?", "Persistent as always.").
- **Register:** menacing-elevated. **Profanity:** none.
- **Representative lines:**
  1. "Kneel Nephilim, before the new Lord of Akyreon!"
  2. "I'll seal that coffin of yours beneath a forest of flesh and bone."
  3. "Your soul shall make a fine addition to my Garden."
  4. "The Garden's vines foretold your arrival. That one of the Church's hounds yet persists in this stirring city."
  5. "You vanquish a shell, nothing more."

## NME_Boss_Mahkteah — Mahkteah, Lord of Perdition
- **Name:** Mahkteah (Gallant: "the Stone of War, shackles the soul of Mahkteah, the Lord of Perdition"; Librarian: "once known as the God of War").
- **Role:** dead god of war, bound in the Stone of War; boss.
- **Gender:** m. EN: Librarian "the story of Mahkteah before **his** fall"; "Lord". FR: neutral.
- **Addresses:** the player (Nephilim / welp / advocate of man).
- **Voice:** honour-bound warrior bravado; relishes combat; taunts about legend and honour.
- **Register:** archaic-menacing, martial. **Profanity:** none.
- **Representative lines:**
  1. "Honor my domain, in victory or death!"
  2. "The fabled power of the Nephilim! You honor me with this fight!"
  3. "Shattered Coil or no. War's been the only constant in these long ages past."
  4. "Get off your knees welp."
  5. "Like a brilliant flame your fury is gone."

## NPC_Valahk — Valahk-Nor
- **Name:** Valahk-Nor (Angel: "slay Valahk-Nor once more"; Solomon: "slayer of Valahk - Nor").
- **Role:** demon general of Cain's Infernal Legion, slain by Gallant long ago; returns as a boss.
- **Gender:** m. EN: Monk "Valahk-Nor frightened children once. **He** frightens none tonight." FR: neutral.
- **Addresses:** the player (wretch / creature / Aether-Spawn), his Legion.
- **Voice:** war-cry declaratives, contempt for the player's "Aeonic blood", obsessed with Gallant's legacy.
- **Register:** menacing-archaic. **Profanity:** none.
- **Representative lines:**
  1. "Akyreon will be avenged!"
  2. "I shall delight in the defilement of your corpse."
  3. "Where is your Commander?! You mock his legacy!"
  4. "Your blood is an abomination of the Astral tide."
  5. "To your coffin wretch!"

## NPC_Door_Advocate — "the Advocate"
- **Name:** self-styled "the Advocate"; personal name UNCONFIRMED.
- **Role:** last lucid soul absorbed into the Garden; grants a virulent blade if struck.
- **Gender:** unknown. EN has no pronoun for self ("I am the Advocate"); FR has one translated line, gender-neutral ("Tu nous as rendu un grand service").
- **Addresses:** the player.
- **Voice:** solemn, prophetic, first-person testimony.
- **Register:** elevated. **Profanity:** none.
- **Representative lines:**
  1. "Listen to my words. Hear me. I am the Advocate. All that remains of a lucid independent soul in the Garden."
  2. "The Garden was a trap. A promise of unity, an escape from suffering."
  3. "Thrust your blade into me and I shall grant you a virulent blade. Toxic to all, including the Hellgrowth."
  4. "It is inevitable that my strength will wane, and I will be lost."
  5. "You. Come. Seek me at the end of these halls."

## NPC_Door_DemoralizedWoman
- **Name:** UNCONFIRMED (unnamed).
- **Role:** ghost-loop widow behind a door; husband was a bell-ringer taken by the Inquisition; gives armory key.
- **Gender:** f. EN: namespace + "M'man used to ring the cathedral bells… **his** key", "You're the one what stole m'**husband's** key!". FR: neutral.
- **Addresses:** the player (stranger / beast / Nephilim).
- **Voice:** rural dialect: "ain't", "ta" (to), "m'" (my), "'nough", "reckon", dropped g's; time-loop dread.
- **Register:** plain-rustic, mournful. **Profanity:** none.
- **Representative lines:**
  1. "I ain't openin' m'door just ta die polite."
  2. "I ain't speakin' to you, beast! Church folk done 'nough harm 'round here."
  3. "Tell me true, Nephilim... When you walk away from this cursed door... Am I still here?"
  4. "If you come back again an' I say the same things... pretend you ain't heard 'em before. I reckon it helps a body keep sane."
  5. "Thank you kindly. I'll manage for now."

## NPC_Door_Drunk
- **Name:** UNCONFIRMED (unnamed).
- **Role:** looping drunk squatter behind a door; comic relief.
- **Gender:** unknown. EN: no self-pronoun ("A man who doesn't try to take away my drinks" describes the player). FR: 2 translated lines, neutral.
- **Addresses:** the player (bartender / Nephilim).
- **Voice:** slurred ("s'shomeone", "'member"), hiccups, nonsense song, "Oi".
- **Register:** comic-plain. **Profanity:** mild ("I'll be damned").
- **Representative lines:**
  1. "Oi—oi—there y'are... bartender! Took ya long enough, I'm runnin' dry over 'ere."
  2. "I'm fine! I'm perfectly—perfectly operational."
  3. "They sendin' Nephilim to evict us now? Heh. I ain't scared of you."
  4. "Truth is... I stopped drinkin' a bit earlier, just to test it. That's when the walls started breathin'."
  5. "Oh, the whale is a fish with really big nose and he eats all the socks and he wears all the clothes. (hiccup)"

## NPC_Door_Female_1
- **Name:** UNCONFIRMED (unnamed).
- **Role:** dead woman looping "about to run for it"; explains the Flower Folk / church purge backstory.
- **Gender:** f. EN: namespace + "Don't suppose you've seen a **woman** bolt from this door already, have you? Feels like I remember runnin'" (describing herself). FR CONTRADICTS: "je suis **surpris**", "j'ai été **emporté**" (masculine agreement — translator error; go with EN).
- **Addresses:** the player.
- **Voice:** working-class dialect: "ain't", "ta", "'em", "lemme", "did'n it", "bloody", "daft"; brittle humour.
- **Register:** plain-rustic. **Profanity:** mild-moderate ("bloody", "pissed off").
- **Representative lines:**
  1. "I ain't breathin', am I? No ache in my knee. No hunger neither. Just this door. And you knock'n on't."
  2. "Well go on then! Go stab some o' them beasts with that fancy sword of yours and distract 'em so I can get outta here."
  3. "Funny thing about fear... you think it keeps you alive... But what if it just keeps you here?"
  4. "We're all slaves ta somethin', aren't we?"
  5. "Whole city went mad, did'n it? I think I went with it."

## NPC_Door_Female_2 — Solomon's would-be fiancée
- **Name:** UNCONFIRMED (unnamed; not Deliliah, who died on the pyre).
- **Role:** aristocratic Academy ghost who mistakes the player for Solomon; demands a proper ring; holds Solomon's stolen seal.
- **Gender:** f. EN: "If you mean to ask for my **hand**, Solomon", "my love", "the darling of the entire city… present me with a peasant's band?". FR: addresses player as "vous êtes finalement **revenu**" (m, as Solomon).
- **Addresses:** the player *as Solomon* (masculine addressee, name "Solomon", "my dear lord", "my love").
- **Voice:** haughty court diction, precise grammar, disdain ("vulgar", "wretched", "trinket").
- **Register:** elevated-comic (society snob). **Profanity:** none.
- **Representative lines:**
  1. "A proper proposal deserves a proper jewel. Something radiant... something the whole court would whisper about."
  2. "Go on then, Solomon. Do try not to embarrass yourself."
  3. "I've endured this dreadful garden long enough, my love. I refuse to let these vulgar vines claim me before you've asked properly."
  4. "And yet you present me with a peasant's band? Keep your miserable proposal!"
  5. "The great Solomon... undone by his own admirers."

## NPC_Door_Female_3_2D
- **Name:** UNCONFIRMED (unnamed).
- **Role:** woman merged with her house/door by Hellgrowth roots; flirtatious innuendo about knocking.
- **Gender:** f. EN: namespace; "darlin'", "dear" (addressing player); no self-pronoun. FR: "ma chère" (feminine *addressee*, not speaker). Speaker gender rests on the namespace label plus the coquettish framing — no textual pronoun.
- **Addresses:** the player (dear / darlin').
- **Voice:** warm, chuckling, double entendre, "ya", dropped g's, "Oh, ho ho ho".
- **Register:** comic-plain, flirtatious. **Profanity:** none.
- **Representative lines:**
  1. "Oh, ho ho ho—mind the knock there, darlin'. Haha! The door's in a sensitive mood today."
  2. "Go on then... give it a PROPER knock. No need to be shy with me now."
  3. "Strange thing about doors, dear... the more you knock, the more they open up to you."
  4. "But the house and I sorted it out. We share the rooms now. Very civil arrangement."
  5. "Most folk just bang like savages, hahaha!"

## NPC_Door_Male1
- **Name:** UNCONFIRMED (unnamed).
- **Role:** hidden survivor watching demons drag people off; tells player to scram.
- **Gender:** m. EN: namespace only; no self-pronoun. FR: "Tu vas griller **ma couverture**" (neutral). Masculine per namespace label.
- **Addresses:** the player ("mate").
- **Voice:** cockney-ish: "Oi", "Ye daft mate?", "'nuff", "knackers", dropped g's.
- **Register:** plain-street. **Profanity:** mild ("god knows where", "knackers").
- **Representative lines:**
  1. "Oi, scram. You'll blow my cover."
  2. "Ye daft mate? Them horned knackers been draggin' folk off and takin' 'em off to god knows where."
  3. "I see 'em passin' every night with some hapless fool kickin' and screamin'"
  4. "Funny 'nuff they don't discriminate against whether or not they're live or dead. A body's a body to 'em."

## NPC_Door_Priest
- **Name:** UNCONFIRMED (unnamed; not Mathias — "Mathias was slain").
- **Role:** damned Lunitarian priest who confesses the Church's fear of the Nephilim; unlocks the soul-siphon / "gnosis" progression; hub of the Purgatory replay mechanic.
- **Gender:** m. EN: "I knew **men** more sinful than you… **We** trusted them"; "we were misguided, fearful **men**"; addresses the player "he who is caught between realms". FR: 4 translated lines, neutral.
- **Addresses:** the player (child / Nephilim / "he who is caught between realms").
- **Voice:** confessional, theological, paternal ("My my child. You are delightfully... sinful.").
- **Register:** elevated-clerical. **Profanity:** "To hell with the Order…".
- **Representative lines:**
  1. "You, he who is caught between realms. Take this opportunity to achieve great strength."
  2. "The Lunitarians feared the Nephilim. Thus we shackled your souls and brainwashed your kind."
  3. "You are not fallen, nor cursed, but blessed. You are the next stage of humanity. Perhaps our guardians."
  4. "I may be damned, but you have potential to save us all."
  5. "I've nothing left to offer you. I shall spend my eternity in great contemplation of the Divine."

## NPC_Door_Prisoner
- **Name:** UNCONFIRMED (unnamed).
- **Role:** self-confessed killer content in his/her Shoreditch cell (Nachstahl Steel / Caldewels lore); taunts the player.
- **Gender:** unknown. EN: no self-pronoun ("Only enough room for one and my chamber pot"). FR: 7 translated lines, neutral ("bâtard" is the player insult).
- **Addresses:** the player (friend / "'alf breed").
- **Voice:** manic cackling, ALL-CAPS outbursts, "betwixt", "me own", "'alf".
- **Register:** comic-menacing, unhinged. **Profanity:** mild ("hell").
- **Representative lines:**
  1. "Ha! Looks like you're in a bit of a bind, no? Stuck out there, while I'm safe in here! Hehehe!"
  2. "I earned this cell! You hear me?! How many souls and broken bones—worth it. All of it worth it!"
  3. "My damnation is my safety. My soul stuck betwixt the horrors of this world and my mind."
  4. "YOU WON'T STOP THEM. NO ONE CAN STOP THEM. THEY'VE ALREADY WON!"
  5. "You've your own chains, and I've got mine. Learn to embrace your lot, lean into it, its aalll we got!"

---

## Speaker → gender summary
| Namespace | Name | Gender | Evidence type |
|---|---|---|---|
| NPC_Angel_Male | UNCONFIRMED (Nahnias?) | m | namespace only |
| NPC_Blacksmith | Gajov (surname unconfirmed) | m | EN he/his + FR "prêt" |
| NPC_Librarian | Mereda | f | EN she/lass/her + FR "Contente", "désolée" |
| NPC_Merchant | Lotte Ananta | m | EN him/his/man + FR "retrouvé", "un chat" |
| NPC_Hub_Monk_1 | UNCONFIRMED | m | FR "soulagé" |
| NPC_Gallant | Gallant Alexander | m | EN he/him/brother + FR "tué", "prêt" |
| NPC_Solomon | Solomon Moore | m | EN he/man |
| NME_Boss_Felwyl_TA/TW | Felwyl the Withered | m | EN he/him + FR "maître", "nouveau seigneur" |
| NME_Boss_Mahkteah | Mahkteah | m | EN his/Lord |
| NPC_Valahk | Valahk-Nor | m | EN he |
| NPC_Door_Advocate | UNCONFIRMED | unknown | none |
| NPC_Door_DemoralizedWoman | UNCONFIRMED | f | EN husband/m'man + namespace |
| NPC_Door_Drunk | UNCONFIRMED | unknown | none |
| NPC_Door_Female_1 | UNCONFIRMED | f | EN "a woman bolt from this door" + namespace (FR contradicts, treat as error) |
| NPC_Door_Female_2 | UNCONFIRMED | f | EN "my hand", "my love" + namespace |
| NPC_Door_Female_3_2D | UNCONFIRMED | f | namespace + flirtatious framing; no pronoun |
| NPC_Door_Male1 | UNCONFIRMED | m | namespace only |
| NPC_Door_Priest | UNCONFIRMED | m | EN "we… fearful men" |
| NPC_Door_Prisoner | UNCONFIRMED | unknown | none |
