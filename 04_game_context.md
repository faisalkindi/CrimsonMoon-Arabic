# Crimson Moon — Game Context for Arabic Localization

Source: game text only (`research/lore_notes.txt`, `research/quests_objectives.txt`, `research/items.txt`; a few gender checks against `research/dialogue_all.txt`). Row keys cited in backticks. UNCONFIRMED = text does not say it.

---

## 1. Plot synopsis

**Player.** You are a Nephilim, a human bonded to an Angel ("the angel who lives inside of me" `NPC_GALS_3_BodyText`; "Nephilim can call upon the power of their Angelic Lineage to transform" `Tutorial_Angel1_TextBody`). Nephilim are a post-war race of "towering giants of incredible strength, agility, and innate tallents for sorcery and angelic foresight" `TOLS_3_Body`. Some go "feral" when possessed by their Angel `FeralNephilim1BodyText`. Death is not final: Gallant was "resurrected. The angel who lives inside of me pulled me back" `NPC_GALS_3_BodyText`; the player "awoken from your coffin at the Order's hall, the Sanctus Clypeus" `MQCTS_Desc`.

**Structure.** Prologue ("The Trumpets Blown" `MQP_Name`): sent to Gildenarch "in response to an invasion by unknown forces", find Knight Captain Rendaen `MQP_Desc`, `MQP_Objective_3_Full`. Then the hub loop: wake in the Sanctus Clypeus, speak to Knight Commander Gallant Alexander at the War Table `MQCTS_Desc`, Mereda at the Library, Lotte Ananta at Treasury, Gajov Resnyk at the Forge `MQCOIC_1_Full`, `MQCOIC_2_Full`. Pick a Run at the War Table, gear up in the Armory, go through the Portal `Hublore_ArmoryGate_TextBody`, `Hublore_Teleporter1_TextBody`. A Run = "battle through random districts to reach the World Boss and acquire an Abraxas Stone" `LongRunFormat_Description`. Three Wards each end in a Dead God (World Boss); final ward is the Godsreach Spire `W4_Title`. Runs are called "Runs"/"Excursions"; FR uses "tentative".

**Threat.** "the Abraxas Stones, that bind the souls of powerful beings known as the Dead Gods. Deep within Gildenarch are ancient ruins harboring these wicked Stones. The Infernal Lost Legion and their servants have uncovered them and channeled their power into the twisted Godsreach Spire. A dire and imminent threat to our realm that tears apart the protective veil" `Hublore_AbraxasStones_TextBody`. Order's plan: "procure the Abraxas Stones, slay the Dead Gods within them, and sever the Spire from its power source" (same row). Three stones: E'frae the Dry Rot King (Southern Ward graveyard `W1_WB1_Description`), Mahkteah the Lord of Perdition (chamber beneath Shoreditch `W2_WB1_Description`), Aegoroth the Eye of the Abyss (final boss in the Spire, guarded by Felwyl the Ascended `W4_FB1_Description`, `W4_FB1_Description_True`). Ending state: "The Spire is halted, and the veil still stands yet it remains torn..." `MQPE3_Desc_Completed`.

**Villain plot (Solomon Moore).** Vampire industrialist from Nachtendale; Nachtstahl Steel Mills revived Grimhaven and reopened the Mystic Peaks mines `MMLS_6_BodyText`. Journal: "It has taken me over 20 years for my slow march through Gildenarch... Soon, the Rite of Desolation will begin again, the Infernal Legion shall have its new territories, and the insufferable traitors that I once called my siblings shall die... I shall see Leandra and Pervical once more" `MMLS_4_BodyText`. He manipulated the Archspire Chapter (replaced the Archbishop with Cardinal Mathias `MMLS_1_BodyText`; offered vampiric immortality to prison owner Caldwell `SPLS_4_BodyText`; funded the Godsreach Spire with 4,000,000 Drakes of Church money `ACLS_5_BodyText`), used Felwyl to seed the Reborn cult as "a sound and almost convincing inversion of the Lunitarian's premises on the Shattered Coil" `MMLS_2_BodyText`, and pushed Mathias into an Inquisition `ACLS_6_BodyText`, `FSLS_7_BodyText`. The Gala at the Spire completion `EALS_1_BodyText` is the massacre night: Clan Moore vampires hit Elk Grove Academy `ACLS_7_BodyText`; the clergy, converted to vampires, drink the Cardinal `ACLS_1_BodyText`; the ritual at the Spire tears the veil, and "Tonight, Eden dies" `ACLS_8_BodyText`. Solomon's farewell: "Valahk – Nor's forces have already taken the Celestial Mountains in Purgatory, so all that remains is for the veil to fall" `MMLS_10_BodyText`. Motive is revenge on the Church "after everything they had done to my family" `MMLS_4_BodyText`; he also claims "I am doing Eden a service by destroying the veil" since the Holy Lineage ordered the Abraxas research 400 years ago `MMLS_5_BodyText`.

**Hellgrowth / Reborn.** "Infernal Flora" from beyond the veil; the Reborn cult worships it as the "Garden", takes the "Red Gift"/"red bloom" `RKLS_7_BodyText`, and hosts grow into a shared organism `SPLS_5_BodyText`, `RKLS_1_BodyText`. Cult theology: "Lunarin is the Dragon! The Demiurge lives once more through the Church... The Church calls them Demons; we shall call them Shepherds!" `RCLS_1_Body`. Felwyl used it to build the Warden from ~29 men `Story_BehemothConstruction1_TextBody`. Demons turned on the cultists once through the gate `RKLS_10_BodyText`.

---

## 2. World history and cosmology

Calendar: in-game year 782 at present (`MMLS_4_Title` "5/7/782", `Story_PropertySiezure_TextBody`). Ordered from earliest:

- **Eden** = the world/realm ("shaped Eden" `LPLS_1_BodyText`; "Eden's vampire clans" `VampiricHalberdDesc`).
- **The Coil / Shattered Coil.** Cosmological term: Reborn call this "veiled realm, the Shattered Coil. Prison for our shattered souls... before the wyrm forged our shackles" `Cult1BodyText`. "the ancient era of The Coil" `MMLS_8_BodyText`; "when the Coil was yet whole, war dominated the lands of Eden" `MahktenSwordDesc`. Angel Apothos: "the Throne will Coil its Lord And the Serpent will reawaken" `ALLS_2_Body`.
- **The Demiurge / the Dragon.** Lunitarian doctrine: the Sun is "the fire lit by the accursed dragon, the Demiurge"; Lunarin sits on "The Throne forged from the Demiurge's corpse" `LCLS_1_Body`. Heretics say Lunarin *is* the Dragon `RCLS_1_Body`.
- **War of the Gods / the Sundering.** Started by the Lord of Perdition; "the war that taught Eden its gods could bleed"; ended with gods bound in Abraxas Stones `LPLS_1_BodyText`. Also "the cosmic war which befel our realm" `LCLS_2_Body`; sword Axiom marks "the new world order that followed the War of the Gods" `AxiomDesc`. Lunarin "Ascendant to The Throne" `LCLS_1_Body`; Lunar Sentinels predate "Lunarin's ascendance to the Divine Throne" `LunarSentinelShieldDesc`.
- **The Dead Gods (bound in stones):**
  - **Mahkteah, Lord of Perdition** — "god of war"; his Mahktens "less a people than an appetite"; laughed when sealed `LPLS_1_BodyText`. Boss text: "colossal club mace" `MahktenCuirassDesc`. Nightmare of spiked riders and a chest-opened fiend with a club `LPLS_3_BodyText`.
  - **E'frae, the Dry Rot King** — formerly "Lord of the Wild from the Island of Saedrys"; the Dry Rot King is "his corpse" `DRLS_3_BodyText`. His people the Saedrics "did not die. They dried. Now they are the Rot Kin" `DRLS_1_BodyText`. Also "great father of the wild" `DRLS_2_BodyText`; "father of beasts" `Story_DryRotKing1_TextBody`. Items call the Rotkin "Stagkin" `RotkinShieldDesc`.
  - **Aegoroth, Eye of the Abyss** — worshippers pluck out their eyes; appears in dreams with "large, magnificent wings and many, many eyes" `AALS_2_BodyText`; "Seekers... blind scholars who dwelled in the deep dark" `ObsidianShardDesc`. Final boss `W4_FB1_Title`.
- **Sentinel Conflict of 234** and eradication of the Sentinels; Emperor Alonious of Saedrys abdicated to the Holy Lineage; faith "established by The Holy Lineage around 333" `LCLS_3_Body`. Imperial Conversion terms: old gods rejected, "All former faiths will hereby be known as paganus" `LCLS_2_Body`. "Last Will and Testament of the Sentinels" is a prophecy: "Then shall come the Soul Torn Beast" `ProphecyDescription`.
- **Lunitarian Church / Velchorian Empire / Holy Lineage.** Church seat is Luminar (`Vampires1SubHead` "Holy Lineage in Luminar"; also spelt "Illuminar" `ACLS_9_BodyTextv`). Nation/empire: Velchoria / "Velchorian Empire" `TOLS_1_Body`; also "Lunitarian Empire" `Story_PropertySiezure_TextBody`; one item says "Adamaic Empire" `FieryBroadswordDesc` (UNCONFIRMED whether same entity).
- **Saints.** St. Uriel of Caragus, "patron of the downtrodden" of the Great Reconstruction `LunitarianFaithSaintUrielBodyText`; St. Enoch (a wall) `FSLS_2_SubHead`; "The Saints frown upon me" `ACLS_4_BodyText`; the Pyresworn founded by an unnamed saint `FieryBroadswordOrnateDesc`.
- **Holy Phases** (liturgy): New Moon = Cleansing; Waxing = Celebrations; Full Moon = Illumination and Power; Waning = "Shedding of the old skin. The shattering of the coil"; Blue Moon = Gnosis; Blood Moon = scratched out, "rebirth" `LCLS_1_Body`.
- **Angels / Choir / Luderaeon.** "the High Daemons of Ludereon... constructed of a sort of 'Resonant Energy'"; Angelic Sigils invented by Archangel Maedrael, who may "not be of Ludereon" `MaedraelBodyText`. Quest "Children of Luderaeon" = Angelic Choir lore `SQCOL_Name`, `SQCOL_Objective_Full`. Angels "serve the Throne itself... the Divine... is dying" `ALLS_2_Body`. Named angels: Apothos (High Angel) `ALLS_1_Body`; Azrael `AngelAzraelRelicStaffDesc`; "Aegis" appears as a weapon name `AngelAegisPoleaxeCategory`.
- **Akyreon / Iridaeon / Infernal Legion.** Demons' realm: "Lost Akyreon, the realm of Aeons Given Flesh, who've been scorned by Archons of the Throne" `RCLS_1_Body`; "the Akyrians who occupy these halls" `DLLS_1_Body`; weapon "Akyreon's Tongue" `HellGrowthGlaive`. Quest name "Remnants of Akyreon" `SQROI_Name` vs older key "Remnants of Iridaeon" `RemnantsofIridaeonName`. "Infernal Lost Legion" `Hublore_AbraxasStones_TextBody`; "Infernus" is Hell `FSLS_7_BodyText`; "Purgatory" holds the Celestial Mountains `MMLS_10_BodyText`.
- **Rite of Desolation.** Past catastrophe, will "begin again" `MMLS_4_BodyText`; a text is "from after the Rite of Desolation" `TOLS_3_Subhead`. Details UNCONFIRMED.
- **Great Reconstruction.** Rebuilding era after the war; Nephilim went feral (Fire of Caragus 752, Sister Susan) `FeralNephilim1BodyText`.
- **Crimson Concordat.** Covenant between Holy Lineage, Velchoria, and Gallant Alexander: all Nephilim must join the Knights of the Crimson Moon, no children, total obedience; hierarchy and four Oaths (Divine, Moonlight, Midnight, Crimson) `TOLS_1_Body`. Items also mention a "Keeper's Oath" `KeepersOathCuirassDesc`. Followed by the Apostate Hunts `TOLS_2_Body`.
- **Battle of the Last Kingdoms.** Gallant killed Valahk-Nor, then the Church slaughtered the Nephilim `NPC_GALS_3_BodyText`, `MALS_2_Body`.
- **Cain and vampires.** Vampire clans keep "Cain's Covenant"/"the Pact"; "Cain is dead, and it is better he remains that way... we are free to use his blood" `MMLS_3_BodyText`, `MMLS_8_BodyText`.
- **Inquisition Act of 760** `Story_PropertySiezure_TextBody`; present crisis year 782.

---

## 3. Factions and organizations

| Faction | One line | Key |
|---|---|---|
| Lunitarian Church (of Velchoria) | State religion of Lunarin; runs Inquisition, Crusaders | `TOLS_1_Body` |
| The Holy Lineage | Supreme rulers of the Church in Luminar | `Vampires1BodyText` |
| Archspire Chapter | Church chapter in Gildenarch; guards/studies the "Artifacts" (Abraxas Stones) | `ACLS_3_BodyText` |
| Knights / Order of the Crimson Moon | Nephilim order under Gallant, bound by Concordat | `TOLS_1_Body` |
| Specters | Moonlight-Oath Nephilim assassins abroad | `TOLS_2_Body` |
| Covenant Crusaders / Covenant Clerics | Church army; warrior-priests | `CrusaderLongswordDesc`, `CovenantClericShieldDesc` |
| Pyresworn | Lunitarian inquisitorial burning order | `FieryBroadswordOrnateDesc` |
| Lunar Sentinels | Pre-Church Lunarin worshippers, now heresy | `LunarSentinelShieldDesc` |
| Karsivite Orthodoxy | Allied pagan-converting sect in Karsiv | `GRLS_1_Body` |
| Velchorian Empire / Sovereign Sentries | Imperial crown; heron banner; Sentries answer to crown not Church | `SovereignsShieldDesc` |
| Nachtstahl Steel Mills | Solomon's company | `MMLS_6_BodyText` |
| Clan Moore | Solomon's vampire clan | `ACLS_7_BodyText` |
| Clan Telvaught, Clan Sirius, Clan Inari, Clan Harington (The Pale Rose) | Other vampire clans | `MMLS_8_BodyText` |
| The Reborn / Cult of the Reborn | Hellgrowth cult led by Prophet Felwyl | `FSLS_5_BodyText` |
| Infernal (Lost) Legion | Demon army under General Valahk-Nor | `Hublore_AbraxasStones_TextBody` |
| Nac-Fei Death Knights | Demon knights trafficking survivors | `Story_ScoutNote1_TextBody` |
| Mahktens | Extinct marauders of Mahkteah | `LPLS_1_BodyText` |
| Saedrics / Rot Kin / Stagkin | E'frae's dried people | `DRLS_1_BodyText` |
| Aegorothians / Seekers | Eyeless devotees of Aegoroth | `AALS_2_BodyText` |
| Fellow's Council | Elk Grove faculty body | `EALS_3_BodyText` |
| Champions of Litinstang / Phoenix Paladins of Belwayne | Armaean city-state Nephilim heroes / knights | `ChampionsSwordDesc`, `BelwayneSwordDesc` |
| Armaean mercenaries | Pagan sellswords "consorting with the Lord of Perdition" | `LPLS_2_BodyText` |

---

## 4. Places

- **Gildenarch** — the city, named for the Archspire Cathedral `W1_D3_Description`; inspired by rams of the Treveyan Highlands `RamsGloryDesc`. Wards: **Southern Ward** (former fishing hamlet `W1_Description`) with Forsaken Streets, Ramshorn Keep, Archspire Cathedral, Catacombs; **Grimhaven Ward** (industrial heart `W2_Description`; Red Dog District `MMLS_6_BodyText`) with Shoreditch Wall Tower/Prison; **Gilded Ward** (north, walled rich district `W3_Description`) with Elk Grove Academy, Moore Manor; **Godsreach Spire** `W4_Description`. Also Mill Ward, Pontoon Town `EALS_8_BodyText`, Castle Town outside Ramshorn `SQCL_1_Body`, Mystic Peaks mines west of city `MMLS_6_BodyText`.
- **Archspire Cathedral** — Lunitarian seat in Gildenarch `W1_D3_Description`. **St. Uriel's Chapel** with graveyard and "The Tree" `NightmareBodyText`.
- **Ramshorn Keep** — garrison, Tyrigon the dragon nests there `W1_D2_Description`; Ram's Head Tavern `RKLS_9_BodyText`.
- **Shoreditch Prison / Wall Tower** — owned by Caldwell; "the Lower" where prisoners are fed to the flora `SPLS_2_BodyText`; Valahk-Nor resurrected there `W2_D3_Description`.
- **Elk Grove Academy** — Felwyl's school and Gala site `W3_D1_Description`; Healing House, Seminary Hold, Halvern Room `ACLS_7_BodyText`, `EALS_7_BodyText`.
- **Moore Manor** — Solomon's home `W3_D3_Description`.
- **Godsreach Spire** — Church-funded "civic project", actually the veil-piercing engine `ACLS_5_BodyText`.
- **Sanctus Clypeus** — the Order's hall / hub `MQCTS_Desc`; contains Library, Armory, Treasury, Forge, Transmitorium, War Table, Hall of the Fallen, Orator.
- **Luminar / Illuminar** — Church capital `Vampires1SubHead`, `ACLS_9_BodyTextv`.
- **Nachtendale** — Solomon's home city; "Nachtendale's Sovereign" `SovereignSentryCuirassDesc`.
- **Velchoria** — the empire/kingdom; **Treveyan Highlands**, **Vulken Sea**, **Old Vineyards**, **Halt's Cross** `TarnishedBroadswordDesc`, `LeviathanGreatAxeDesc`, `EALS_6_BodyText`.
- **Karsiv** — pagan land; Ulsvelled (tribes) `GRLS_2_Body`; Gajov's homeland.
- **Armaea** — foreign region: city-states **Belwayne** (phoenix) and **Litinstang** (Champions, The Rose) `MMLS_7_BodyText`; Armaea Hills, Western Armaea `AALS_1_BodyText`, `DRLS_2_BodyText`; House Haedrik `HaedrikKnightCuirassDesc`.
- **Saedrys** — island; Alonious's seat; Kambrook village south of it `LCLS_2_Body`, `TOLS_2_Body`. Items spell it "Sadrys" `BroadswordDesc`.
- **Caragus** — site of the 752 Fire; St. Uriel's origin.
- **Norundiir** (east, Harrington House) `MMLS_8_BodyText`; **Acktin** (Gallowsway Keep) `MMLS_7_BodyText`; **Aurullian sun-courts** `PodaoSaberGlaiveDesc`; **Gildeus** (crypts, Revenant) `RevenantBladeDesc`; **Tiverna** (book title) `MALS_1_Body`.

---

## 5. Named characters

Gender evidence quoted; FR agreement noted where EN lacks pronouns.

| Name | Role / allegiance | Gender + evidence | Status |
|---|---|---|---|
| **Gallant Alexander** | Knight Commander, Order of the Crimson Moon; "Gallow's Wraith"; killed Valahk-Nor | Male: "The Knight Commander himself famously led the slaughter" `TOLS_2_Body`; signs "Yours, Gallant" to "My Mereda" `NPC_GALS_3_BodyText` | Resurrected Nephilim; executed by Church once `MALS_2_Body`, alive now |
| **Mereda** | Librarian, Lore Mistress of the Order; former Elk Grove magician; Gallant's lover | Female: "Lore Mistress" `Hublore_Librarian1_TextBody`; "a woman named Mereda. She was an alumna" `RCLS_2_Body`; "old witch's heart" `MALS_3_Body` | Alive; possibly ancient ("since my sky went black at the beginning of time" `MALS_3_Body`) |
| **Lotte Ananta** | Merchant of the Order; ex-thief cursed by a Church artifact; spirit can leave body | Male: "Return Lotte's locket to him" `SQTL_Objective_2_Full`; "his old crew" `SQTC_Desc`; FR "le mystérieux Lotte" `Hublore_Merchant1_TextBody` | Alive, cursed ("the state he's in now" `LALS_3_Body`) |
| **Gajov Resnyk** | Blacksmith of the Order; Karsivite, "raised by wolves", conscripted vampire | Male: "Bring Gajov what he need" (dialogue 2335); "vampiric blacksmith" `Hublore_Blacksmith2_TextBody` | Vampire, alive; speaks broken third-person English |
| **Solomon Moore** | Antagonist; vampire lord of Clan Moore; Nachtstahl owner | Male: "Solomon was always bold... his point" `CorrespondenceMathias2BodyText` | Vampire; left for the Spire `MMLS_10_BodyText` |
| **Cardinal (Edmund) Mathias** | Cardinal of Archspire Chapter, age 36; Prefect of the Doctrine; boss | Male: "he has the stomach" no; use "close friend of the Archbishop... Requires time" `MMLS_7_BodyText`; "His Eminence, Cardinal Mathias" `EALS_1_BodyText` | Killed by vampiric clergy `ACLS_1_BodyText`; fought as boss (undead/vampire UNCONFIRMED) |
| **Felwyl** (Master/Lord/Prophet Felwyl; "Fewyl" typo) | Elk Grove master, Reborn prophet, Solomon's partner; bosses "The Withered"/"The Ascended" | Male: "he was always an odd one" `RCLS_2_Body`; "His voice of honey" `RKLS_7_BodyText` | Alive as monster/lich ("Lichdom" `SQLD_Name`) |
| **Lunarin** | God of the Church | Male: "Lunarin and his Holy Radiance... He who commands legions" `LCLS_1_Body` | Deity; "he is dying" per Apothos `ALLS_2_Body` |
| **Archbishop Dorion** | Head of Archspire Chapter before Mathias | Male: "his skepticism... he is far too stubborn" `MMLS_1_BodyText` | Ill/diagnosed `CorrespondenceSolomon2BodyText`; fate UNCONFIRMED |
| **Bishop Aaron** | Bishop writing to Scribe Siron | UNCONFIRMED (only "Bishop Aaron to Scribe Siron" `CorrespondenceArtifactSubHead`) | UNCONFIRMED |
| **Scribe Siron** | Scribe of the Archspire; liaison to Karsivite Orthodoxy | Male: "men like you" `GRLS_1_Body` | UNCONFIRMED |
| **Ciaran Telvaught** | Clan Telvaught vampire, warns Solomon about the Pact | UNCONFIRMED (letter only, `MMLS_3_SubHead`) | Vampire |
| **Peter Garrus Telvaught** | Professor, leads Clan Telvaught | Male: "Professor" + FR "Dirigée par le professeur" `MMLS_8_BodyText` | Vampire; clan "first to die" |
| **Delilah Hexxus Sirus** | Matron, founded Clan Sirius; traitor to Cain | Female: "Matron"; FR "Traîtresse" `MMLS_8_BodyText` | Vampire |
| **Aaron Chester Inari** | Occultist, Inari Weaponry, Clan Inari | Male: FR "occultiste et propriétaire" (masc.) `MMLS_8_BodyText` | Vampire |
| **Margarette Harrington** | Madam, Harrington House, Clan Harington | Female: "Madam" `MMLS_8_BodyText` | Vampire |
| **Lord Erington** | Telvaught lord killed by Clan Moore for Scirax | Male: "Lord" `SciraxDesc` | Dead |
| **Cain** | Progenitor of vampires | Male: "Cain is dead... his blood" `MMLS_3_BodyText` | Dead |
| **General Valahk-Nor** (also "Valahk Nor", "General Valahk") | Infernal Legion general, boss | Male: "run my sword through Valahk-Nor's throat... his head" `NPC_GALS_2_BodyText` | Killed by Gallant, resurrected `W2_D3_Description` |
| **Tyrigon** | Dragon boss at Ramshorn | UNCONFIRMED (no pronoun) | Alive dragon |
| **The Warden** | Flesh construct made from ~29 men | Referred to as "it"/"the subject" `WardenBodyText` | Construct |
| **Flesh-Wrought Egregore** | Elk Grove boss | UNCONFIRMED | Abomination |
| **Mahkteah** | Dead God of war | Male: "He was the god of war" `LPLS_1_BodyText` | Dead God, bound |
| **E'frae** | Dead God, Lord of the Wild | Male: "his corpse" `DRLS_3_BodyText` | Dead/rotting god |
| **Aegoroth** | Dead God, Eye of the Abyss | Male: "Aegoroth himself" `AALS_2_BodyText` | Dead God |
| **Archangel Maedrael** | Inventor of Angelic Sigils | Male: "the Archangel himself" `MaedraelBodyText` | UNCONFIRMED |
| **Apothos** | High Angel bound by ritual | Male: "Apothos was none too pleased... it had taken over him" (him = Renault) — angel gender UNCONFIRMED `ALLS_2_Body` | Angel |
| **Father Renault** | Priest-magician channeling Apothos | Male: "Father"; "his smoldering corpse" `ALLS_2_Body` | Dead (incinerated) |
| **Emperor Alonious** ("Alonius" in FR) | Emperor of Saedrys who abdicated | Male: "his crown" `LCLS_2_Body` | Historical |
| **St. Uriel of Caragus** | Saint, patron of downtrodden | Male: "Holy is he" `LunitarianFaithSaintUrielBodyText` | Dead saint |
| **Gelwyn Argyle** | High Orator; hub narrator | UNCONFIRMED; FR "grand orateur" masc. `Hublore_Orator1_TextBody` | Dead ("from beyond the grave") |
| **Sir Aldus Geory** | Inquisitor appointed by Mathias | Male: "Sir"; "he has the stomach" `CorrespondenceMathias2BodyText` | Alive at time of notice |
| **Knight Captain Rendaen** | Player's captain in prologue | UNCONFIRMED; FR "le capitaine" `MQP_Objective_3_Full` | UNCONFIRMED |
| **Selandris** | Apostate Nephilim, "Oathbreaker" | UNCONFIRMED `ApostasyTurnInName` | Apostate |
| **Sylvia Lochart, Markus Dianas, Yaron Volkart** | Chapter Masters of the Order | Sylvia female (name only), others UNCONFIRMED `TOLS_1_Body` | UNCONFIRMED |
| **Irvine Gaertner** ("Brother Irvine") | Nephilim scout | Male: "Brother Irvine" `Story_ScoutNote1_TextBody` | UNCONFIRMED |
| **Sister Ryker** | Nephilim scout | Female: "the stubborn lass... She followed" `Story_ScoutNote2_TextBody` | UNCONFIRMED |
| **Jemison Caldwell / H. Caldwell** | Prison owner, age 47; sold Shoreditch for vampirism | Male: "his perversely selfish nature" `MMLS_7_BodyText` | Turned vampire (implied) |
| **Sergio Von Kulkan** | Vicariate Administrative Consultant | UNCONFIRMED `ACLS_5_BodyText` (a "Sergio" also authored *Metaphysics of Being* `DLLS_3_Body`, link UNCONFIRMED) | — |
| **Krytori** | Cultist relieved of post at Ramshorn | UNCONFIRMED `MMLS_9_BodyText` | — |
| **Calum** | Reborn servant writing to Felwyl | UNCONFIRMED `RKLS_10_BodyText` | — |
| **Cyras, Cyron, Elanore, Theodis, Merric** | Clan Moore vampires at the Academy | Elanore with "the nurse" (female-coded, UNCONFIRMED); others UNCONFIRMED `ACLS_7_BodyText`, `CorrespondenceVampires2BodyText` | Vampires |
| **Lesandra** | Diarist watching Helene taken; "Lesandra's Diary" | Female name; text has "me window", no pronoun `RKLS_6_BodyText` — UNCONFIRMED | Likely infected ("let you in") |
| **Helene** | Girl of seventeen taken and returned | Female: "she swung her door open" `RKLS_6_BodyText` | Undead/infected |
| **Tabitha** | Wife of Charles | Female: FR "punie" `RKLS_3_BodyText` | UNCONFIRMED |
| **Charles** | Tabitha's husband, took the Red Gift | Male: "Oh Charles... he lay asleep" `RKLS_3_BodyText` | Infected |
| **Anya** | Wife of Tomas, prisoner at Shoreditch | Female: "Your Anya"; FR "Retourné à l'expéditrice" `SPLS_9_SubHead` | Alive |
| **Tomas / Lily** | Anya's husband (prisoner) / child | Tomas male ("Tomas, my love... your wrist") `SPLS_9_BodyText` | Tomas "deceased / transferred / unaccounted" |
| **Toby Carrick, Magda Rooke, Hux Pennant** | Lotte's old crew | Magda female (name), rest UNCONFIRMED `SQTC_Objective_*` | Fates are quest objectives |
| **Aleria Hawthorne** | Woman Lotte seeks | Female: "a woman named Aleria Hawthorne" `SQCR_Desc` | Escaped `SQCR_Objective_2_Full` |
| **Cornelius Halhurst / Vespera Halhurst** | Father / daughter, Gala guests | Cornelius male ("a man you may not recall"); Vespera female ("She is a vivid girl") `EALS_10_BodyText` | UNCONFIRMED |
| **Master Auber, Mr. Calder, Pelham** | Cellar master, butler, assistant | Auber male ("I am not an old man yet"); Calder "Mr." `EALS_6_BodyText` | UNCONFIRMED |
| **Marn, Bevan, Halt** | Groundskeeper, boy, apothecary | Bevan male ("He is a good boy") `EALS_9_BodyText`; Marn UNCONFIRMED | — |
| **Marvenne, Hollis, Old Korbel, H., Asher** | Elk Grove faculty | Marvenne female ("she had had words"); H./Asher UNCONFIRMED `EALS_3_BodyText` | Marvenne missing |
| **Wensleigh** | Felwyl's favoured student | UNCONFIRMED; FR "Mon cher Wensleigh" masc. `EALS_2_BodyText` | — |
| **B. C.** | Speaker recruiting founders for Moore | UNCONFIRMED `EALS_7_BodyText` | — |
| **Devereaux, Halhurst, Old Pellaby, Tannig, Anderson, Vivienne, Father Olm, Edmund, Madame Auvern, Haedriks** | Society names | Vivienne female; "The Devereaux woman" female `EALS_5_BodyText`; Father Olm male | — |
| **Dr. "M." / Vauron** | Physicians | UNCONFIRMED `EALS_8_BodyText` | — |
| **Father Ortney, Father Shepherd** | Priests | Male ("Father") `FSLS_5_BodyText`, `Vampires1BodyText` | — |
| **Cretchys, Aeryn** | Deserting guards | UNCONFIRMED `Inquisition1BodyText` | — |
| **Elias Godwin** | Butcher, accuser | Male: "the man's butcher heap" `FSLS_6_BodyText` | — |
| **Daerun Bogmire** | Deserting sentry, bitten | Male: "a man" implied; UNCONFIRMED pronoun `FSLS_3_BodyText` | Dying/turning |
| **Natalia, Erin** | Siblings fleeing infected parents | Erin male ("his will"); Natalia female name `RCLS_3_Body` | — |
| **Lilian** | Told to stay inside | UNCONFIRMED `SurvivorCorrespondence1BodyText` | — |
| **Viktyr** | Blamed soldier in FTUE cave | Male: "I hope he dies first" `FTUECamp_BodyText` | — |
| **Dardin** | Watch relief at Ramshorn | UNCONFIRMED `RKLS_8_BodyText` | — |
| **Leandra, Pervical** | Solomon's lost family | UNCONFIRMED `MMLS_4_BodyText` | Dead (implied) |
| **Sir Camden** | Vermillion Knight of Belwayne | Male: "Sir" `SirCamdensHelmetDesc` | — |
| **Abraxas Godsbane** | Wizard tied to the Stones | UNCONFIRMED `SQAGB_Objective_Full` | — |
| **Vodor** | Karsivite deity ("Totem of Vodor"; "By Vodor and Pack in the sky!") | UNCONFIRMED `SQTOV_Name` | Deity |
| **Aemar** | Meeting place, not a person `SPLS_4_BodyText` | — | — |

Named character count (rows above, counting grouped rows individually): **~95**.

---

## 6. Tone and register

**(a) Lore notes** — archaic/biblical, elevated, often letter form; dialect in commoner notes.
- "He who hath fallen upward unperished know this / We are the light that cast your shadows as well as your god's." `ALLS_1_Body`
- "The Mahktens were his faithful, less a people than an appetite, gathered from every war-torn corner of Eden." `LPLS_1_BodyText`
- "It is not death, exactly, death is an ending, this is a slow forgetting of how to be alive." `DRLS_1_BodyText`
- Dialect: "I heard 'em again. Yelling and screaming from the Keep. No doubt drunk as usual... But ever since the new Cap'n it's… different." `RKLS_2_BodyText`; "Thank gods never looked my way, but she screamed hell." `RKLS_6_BodyText`
- Dry Victorian wit: "Marvenne has no family abroad." `EALS_3_BodyText`; "I said the moon is not noticed if one is properly dressed." `EALS_5_BodyText`
- Horror ledger: "Cooking for forty. Feeding twelve. Where is the food going. I will not ask. I will not ask. I will not ask." `SPLS_8_BodyText`
- Profanity: mild ("bastards" `FSLS_1_BodyText`, "damn well" `RCLS_2_Body`, "Screw Lotte" `SQCL_2_Body`, "bloated pig's corpse of a city" `RCLS_2_Body`).

**(b) Quest / UI text** — terse imperative, Souls-like flavour blurbs.
- "Traverse the corrupted streets of Gildenarch and search for the first Abraxas Stone." `MQPE1_Desc`
- "What was once interred for fear of its incendiary truth has brought the world to its knees." `W1_WB1_Description`
- "Foes undetectable. Proceed with caution." `Enemies_Ward_W3_D3`
- Player-voice topics: "Knight Commander. I am ready to serve." `MQCTS_Objective_Topic_1`

**(c) Item descriptions** — laconic, ironic, three-beat.
- "Most of the breaks are old; most of the bodies are older." `BrokenIronSwordDesc`
- "The hammers with the most marks are rarely returned with their wielder." `NephilimWarhammerDesc`
- "Twenty seconds of saintly violence. Enough for the work, never enough for the war." `Crusader'sMightElixir`
- "Gajov's recipe. He calls it 'no die paste' and refuses to elaborate." `HardeningOil`
- Gajov's own voice is broken third-person: "Bring Gajov material, Gajov forge. Understand?" (dialogue 2327). Preserve this quirk.

Humor: dark and deadpan ("beef-mancy" `FSLS_6_BodyText`; "They will all confess to something."). Register tiers matter for Arabic: liturgy/prophecy (fusha, elevated), aristocratic letters (formal), commoner notes (colloquial-flavoured but keep MSA per project rules), UI (neutral imperative).

---

## 7. Glossary candidates

| Term | Definition | Recommendation |
|---|---|---|
| Nephilim | Angel-bonded warrior race; player | transliterate (also biblical; `decide` if using نفيليم vs Qur'anic echo) |
| Angel / Angelic Sigil / Angelic Grace | Bonded spirit; inscribed form; transform meter | translate |
| Lunarin | The Church's god | transliterate |
| Lunitarian(s) / Lunitarian Church | Followers / state church | transliterate root + translate "Church" |
| The Divine / Divine Throne | Title for the god / seat | translate |
| The Holy Lineage | Ruling body of the Church | translate |
| Archspire (Cathedral / Chapter) | Gildenarch cathedral and chapter | decide (FR kept "Archspire") |
| Gildenarch | The city | transliterate |
| Southern Ward / Grimhaven Ward / Gilded Ward | Districts | translate "Ward"; transliterate Grimhaven |
| Forsaken Streets | District | translate |
| Ramshorn Keep | Garrison | decide (FR "château de Ramshorn") |
| Shoreditch Prison / Wall Tower | Prison | transliterate Shoreditch + translate |
| Elk Grove Academy | School | decide (FR transliterated) |
| Moore Manor | Solomon's house | transliterate Moore + translate |
| Godsreach Spire | Veil-piercing tower | decide (FR "Flèche de Godsreach") |
| Sanctus Clypeus | Order hall (Latin) | transliterate |
| Transmitorium | Sigil-inscribing device | decide |
| War Table | Mission select | translate |
| Run / Excursion | A mission attempt | translate |
| Abraxas Stone(s) | Soul-prisons of the Dead Gods | decide (Abraxas transliterated; also a wizard "Abraxas Godsbane") |
| Dead God(s) | Bound elder gods | translate |
| Dry Rot King / E'frae | Dead God 1 | translate title; transliterate name |
| Lord of Perdition / Mahkteah / Mahkten(s) | Dead God 2 and his people | translate title; transliterate |
| Eye of the Abyss / Aegoroth | Dead God 3 | translate title; transliterate |
| The Warden | Flesh construct boss | translate |
| Flesh-Wrought Egregore | Boss | translate ("Egregore" decide) |
| Tyrigon | Dragon boss | transliterate |
| Valahk-Nor | Demon general | transliterate (normalize hyphen) |
| Felwyl (the Withered / the Ascended) | Boss | transliterate + translate epithets |
| Infernal Legion / Infernal Lost Legion | Demon army | translate |
| Hellgrowth / Infernal Flora / Red Bloom / Red Gift / the Garden | Cult organism and its rites | translate (keep one fixed term per variant) |
| The Reborn (Cult) | Hellgrowth cult | translate |
| Shepherds | Cult name for demons | translate |
| Crimson Concordat | Church–Nephilim treaty | translate |
| Knights / Order of the Crimson Moon | Player faction | translate |
| Oaths: Divine, Moonlight, Midnight, Crimson, Keeper's | Order ranks | translate |
| Apostate / Apostate Hunts / Specters | Rebel Nephilim / purges / assassins | translate |
| Crusader / Covenant Cleric / Covenant Crusaders | Church soldiers | translate |
| Inquisition / Inquisitor / Pyresworn | Church persecution | translate |
| Cardinal / Archbishop / Bishop / Scribe / Prefect | Clerical titles | translate |
| The Veil | Barrier between realms | translate |
| The Coil / Shattered Coil | Cosmic prison-world concept | decide |
| Demiurge / the Dragon / the wyrm | Creator-villain in doctrine | translate |
| Eden | The world | decide (Arabic عدن has religious weight) |
| Luderaeon / Ludereon | Angel realm | transliterate (normalize spelling) |
| Akyreon / Iridaeon / Akyrians | Demon realm / people | transliterate (normalize) |
| Infernus / Purgatory / Celestial Mountains | Afterlife geography | translate |
| Rite of Desolation | Apocalyptic event | translate |
| Great Reconstruction | Post-war era | translate |
| War of the Gods / the Sundering | Primordial war | translate |
| Sentinels / Lunar Sentinels | Eradicated pre-Church order | translate |
| Velchoria / Velchorian Empire | Nation | transliterate + translate |
| Luminar | Capital | transliterate |
| Karsiv / Karsivite Orthodoxy | Pagan land / sect | transliterate + translate |
| Armaea / Armaean; Belwayne; Litinstang; Nachtendale; Saedrys; Caragus; Treveyan | Places | transliterate |
| Saedrics / Rot Kin / Stagkin | E'frae's people | translate Rot Kin; decide Saedric |
| Cain / Cain's Covenant / the Pact | Vampire progenitor and law | transliterate (قابيل decide) + translate |
| Clan Moore / Telvaught / Sirius / Inari / Harington | Vampire clans | transliterate |
| Feral (vampire / Nephilim) | Uncontrolled state | translate |
| Death Knights / Nac-Fei / Knight Terrors / Demon Brutes / Imps / Undead Captains | Enemy types | translate (Nac-Fei transliterate) |
| Soul Energy | Alchemical resource | translate |
| Drakes | Currency | transliterate |
| Holy Phases (New/Waxing/Full/Waning/Blue/Blood Moon) | Liturgy | translate |
| St. Uriel / St. Enoch | Saints | decide (Qur'anic/biblical equivalents exist) |
| Archangel Maedrael / Apothos / Azrael | Angels | transliterate (Azrael = عزرائيل decide) |
| Gallow's Wraith | Gallant's epithet | translate |
| Lore Scrolls / Legendary Scraps / Crescent Tags / Divine Ember / Revenant Crown / Cipher Fragment | Quest items | translate |
| Nachtstahl Steel Mills | Company | transliterate Nachtstahl |
| Weapon Arts / Boons / Mana / Angel Ascension | Systems | translate |

Count: **~75 glossary rows** (many bundle 2–5 variants).

---

## 8. Open questions and contradictions

1. **Name spelling drift:** Felwyl / "Fewyl" (`MMLS_10_BodyText`, `MMLS_2_BodyText`) / "Felwil" (`Story_BehemothConstruction1_TextBody`); Valahk-Nor / "Valahk – Nor" / "Valahk Nor" / "General Valahk"; Luderaeon (`SQCOL_Name`) vs Ludereon (`MaedraelBodyText`); Akyreon (`SQROI_Name`) vs Iridaeon (`RemnantsofIridaeonName`); Luminar vs "Illuminar" (`ACLS_9_BodyTextv`); Saedrys vs "Sadrys" (`BroadswordDesc`); Harington vs Harrington; Sirius vs Sirus; Caldwell vs "Cadwell" (`SPLS_2_Title`); Alonious vs FR "Alonius"; Rot Kin / Rotkin / Stagkin; "Archspire" vs "Arschpire" (`W1_WB1_Description`). Need one canonical Arabic form each.
2. **Placeholders and debug rows** must not be translated as content: "FIX Insert Sub Heading"/"FIX Insert Title" (7+ rows, e.g. `CorrespondenceMathias1SubHead`), "FIX Insert Description Here" (`BackIntoTheFrayTurnInDesc`), "Placeholder for New Controls" (`Tutorial_BasicControls_TextBody`), key-as-text rows (`MQPE1_Objective_Full`, `SQGS_III_Objective_Full`, `MMLS_9_SubHead` = "MMLS_10_BodyText"), "afd" (`SQDM_Objective_TurnIn`), "H A A" title (`ALLS_1_Title`, FR expands to "Le Grand Ange Apothos"), "Level Select (DEBUG)".
3. **EN typos to decide whether to fix in translation:** "Cardianl" `Cult3SubHead`, "Remeber" `SQCL_1_Title`, "Hisotical" `DRLS_1_SubHead`, "HIstorical" `LPLS_1_Subhead`, "Greaet Reconstruction" `FeralNephilim1BodyText`, "Shoredtich" `SQCL_2_Body`, "Ramsorn" `SQCR_Objective_1_Full`, "Hellrfit" `EQHR_Objective_3_Full`, "Acadamy" `SQGB_Desc`, "stange" (x2), "Aothos" `ALLS_2_Body`, "Where WIll Still Stands" `MQPE3_Name`, "siezure", garbled `LPLS_2_BodyText` ("repuation", "recipee", "Figureo", "tongith").
4. **Cardinal Mathias's fate vs boss:** confession says clergy drank his blood and he died `ACLS_1_BodyText`; Cardinal's staff says he "carried his into the Archspire Cathedral on the night Solomon's vampires walked through the doors he had unlocked himself" `CardinalsStaffDesc` (complicit). He is a boss and his Soul Energy is forged `SQDM_Desc`. Is he vampire, undead, or possessed? UNCONFIRMED; affects epithets.
5. **Empire naming:** "Velchorian Empire", "Lunitarian Empire", "kingdoms of Velchoria", and "Adamaic Empire" (`FieryBroadswordDesc`) — same polity? UNCONFIRMED.
6. **Duplicate rows with divergent text:** `DLLS_3_Body` vs `ALLS_3_Body` (same passage, "crystallized into abominable transience" vs "crystallized into form"); `ACLS_7_BodyText` vs `CorrespondenceVampires1BodyText` (one adds "and their ferals"); `Nightmare` / `Story_Nightmare1` / `LPLS_3` share the opening line. Translate consistently.
7. **Mereda's age/nature:** Elk Grove alumna and Gallant's youthful lover, yet "I shed my youth with the stars... since my sky went black at the beginning of time" `MALS_3_Body`. Human, immortal, or Nephilim? UNCONFIRMED; affects honorifics.
8. **Lotte Ananta gender** is male in EN/FR objectives, but the name reads feminine in Arabic; keep masculine agreement.
9. **"Sergio"**: author of *Metaphysics of Being* (`DLLS_3_Body`) and "Sergio Von Kulkan" the finance consultant (`ACLS_5_BodyText`) — same person? UNCONFIRMED.
10. **Gala date vs. notice dates:** Spire Gala "upon the Eve of the New Moon" `EALS_1_BodyText`; property notices dated 5/4/782 and 5/8/782; Solomon's journal 5/7/782 says "the Gala is this evening" `MMLS_4_BodyText`. Consistent enough, but "5/7" is M/D (FR renders "7 mai"), so date-format convention needed.
11. **Vodor** — "By Vodor and Pack in the sky!" (dialogue 2367) suggests Karsivite wolf-deity; totem quest text is minimal. UNCONFIRMED.
12. **"Tree" / woman chained** at St. Uriel's `NightmareBodyText` vs the "Soul Torn Beast" prophecy `ProphecyDescription` — never resolved in text.
