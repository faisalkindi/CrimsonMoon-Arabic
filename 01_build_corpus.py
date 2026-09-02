"""Artifact 2: tagged source corpus. Reads corpus_multilang.csv -> 01_corpus.jsonl.
Category by namespace/key shape; speaker from Verbals namespace; placeholders; skip flags."""
import csv, json, re, collections, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
PH = re.compile(r"\{[^{}]*\}|%[sdf]|<[^<>]+>")
NS_CAT = {
 "ST_Controls":"ui_settings","ST_ControllerSettings":"ui_settings","ST_Settings_AdvancedGraphics":"ui_settings",
 "GameSetting":"ui_settings","GameSettingValueDiscreteDynamic":"ui_settings","PMUI_RemapBindings":"ui_settings",
 "ST_PMUI_Settings_Actions":"ui_settings","FIRLAdapterDLSS":"ui_settings","FIRLAdapterXeSS":"ui_settings","FIRLAdapterFSR":"ui_settings",
 "ST_UI_GenericButtons":"ui_menu","ST_UI_Loadout":"ui_menu","ST_LoadOut":"ui_menu","ST_InventoryScreens":"ui_menu","ST_Inventory":"ui_menu",
 "ST_SortingType":"ui_menu","ST_ItemDetailLabels":"ui_menu","ST_Hud":"ui_menu","ST_GlobalString":"ui_menu","ST_DialogBoxStrings":"ui_menu",
 "ST_DialogText":"ui_menu","ST_DeathScreen":"ui_menu","ST_LoadingScreens":"ui_menu","ST_BossDefeatScreens":"ui_menu","ST_Rewards":"ui_menu",
 "ST_MissionModifierStrings":"system","ST_ArenaConfigurations":"system","AsyncLoadingScreen":"system","CloudSaveCompare":"system",
 "ST_YetiMultiplayerMessages":"system_online","ST_YetiSocialMessages":"system_online","ST_YetiAuthMessages":"system_online",
 "ST_YetiStorageMessages":"system_online","ST_YetiEntitleMentMessages":"system_online","ST_YetiActivityMessages":"system_online",
 "ST_YetiErrorDialogHeaders":"system_online","ST_PMUI_SocialManagementStrings":"system_online","ST_PMUI_BootUpFlow":"system_online","ST_AccountLinkFlow":"system_online",
 "ST_Achievements":"achievement",
 "ST_Armor":"item","ST_Weapons":"item","ST_Shields":"item","ST_Trinkets":"item","ST_Consumables":"item","ST_ConsumableDescriptions":"item",
 "ST_QuestItems":"item","ST_Blueprints":"item","ST_Vendors":"item","ST_AngelSigils":"item",
 "ST_Boons":"skill","ST_BoonDescriptions":"skill","ST_WeaponArts":"skill","ST_WeaponArtsDescription":"skill","ST_Attributes":"skill","ST_ATTRIBUTES":"skill",
 "ST_Quests":"quest","ST_Objectives":"quest","ST_WarTable":"quest","ST_InformationScrollData":"quest",
 "ST_LoreNotes":"lore","ST_LocationDiscovery":"lore","ST_LoreScrollMenu":"ui_menu","ST_BuildNotes":"skip_debug",
}
def classify(ns, key, en):
    if ns.startswith("Verbals/"): return "dialogue"
    if ns in NS_CAT: return NS_CAT[ns]
    if ns == "":
        if len(en) > 1500: return "legal"
        if re.search(r"Lorem ipsum|FIX Insert|^\s*$", en): return "skip_debug"
        if re.fullmatch(r"[\W\d_]*", en): return "skip_symbol"
        return "ui_inline"
    return "other"
SKIP_RE = re.compile(r"Lorem ipsum|FIX Insert|^\s*$|^[A-Z]{2,6}_[A-Za-z0-9_]+$")  # dev placeholders / key-as-text
rows = list(csv.DictReader(open("corpus_multilang.csv", encoding="utf-8")))
out, cats, spk = [], collections.Counter(), collections.Counter()
for r in rows:
    ns, key, en = r["namespace"], r["key"], r["en"]
    cat = classify(ns, key, en)
    speaker = ns.split("VC_Verbals")[1] if ns.startswith("Verbals/") else None
    if len(en) > 1500: cat = "legal"
    skip = cat.startswith("skip") or cat == "legal" or bool(SKIP_RE.search(en))
    cue = bool(re.search(r"_cue_\d+$", key))
    rec = {"id": f"{ns}|{key}", "namespace": ns, "key": key, "source_en": en,
           "fr": r["fr"], "es": r["es"], "it": r["it"],
           "category": cat, "speaker": speaker, "speaker_gender": None, "addressee": None, "addressee_gender": None,
           "scene_id": None, "line_order": None, "is_subtitle_cue": cue,
           "placeholders": PH.findall(en), "skip": skip,
           "max_chars_hint": 28 if cat in ("ui_menu","ui_settings","ui_inline") and len(en) <= 32 else None}
    out.append(rec); cats[cat] += 1
    if speaker: spk[speaker] += 1
with open("01_corpus.jsonl", "w", encoding="utf-8") as f:
    for o in out: f.write(json.dumps(o, ensure_ascii=False) + "\n")
print("rows", len(out), "skip", sum(o["skip"] for o in out))
for c, n in cats.most_common(): print(f"  {c:16}{n:6}  words {sum(len(o['source_en'].split()) for o in out if o['category']==c):7}")
assert len(out) == 8969 and all(o["placeholders"] == PH.findall(o["source_en"]) for o in out)
