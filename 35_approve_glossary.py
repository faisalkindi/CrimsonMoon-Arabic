"""Human-approved glossary lock (Faisal, 2026-09-01): Nephilim=transliterate, Order=الجماعة, Archspire=أرشسباير,
mechanic list from 07_pilot_findings.md §4, names by rule (hard G=ق, V=ڤ). Terms not listed stay pending."""
import csv, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
A = {
    # race / core
    "Nephilim": "نيفيليم", "Angel": "الملاك", "Angelic Sigil": "الختم الملائكي", "Angelic Grace": "النعمة الملائكية",
    "Angel Ascension": "الصعود الملائكي", "Angel Sense": "حاسة الملاك", "Soul Energy": "طاقة الروح",
    "Weapon Art": "فنّ السلاح", "Boon": "بركة", "Trinket": "حِلية", "Blueprint": "مخطط", "Mana": "المانا",
    "Stamina": "القدرة على التحمل", "Skulls": "جماجم", "Hellrift": "صدع الجحيم", "Nexus Gate": "بوابة النكسس",
    "Purify": "تطهير", "Loadout": "التجهيزات", "Bounty": "مكافأة", "War Table": "طاولة الحرب", "Excursion": "جولة",
    "Abraxas Stone": "حجر أبراكساس", "Dead Gods": "الآلهة الميتة", "Drakes": "دريكس",
    # factions / story
    "Order of the Crimson Moon": "جماعة القمر القرمزي", "Knights of the Crimson Moon": "فرسان القمر القرمزي",
    "Lunitarian Church": "الكنيسة اللونيتارية", "Lunitarian": "لونيتاري", "Lunarin": "لوناران",
    "Holy Lineage": "السلالة المقدّسة", "Crimson Concordat": "الميثاق القرمزي", "Crimson Oath": "العهد القرمزي",
    "Divine Oath": "العهد الإلهي", "Moonlight Oath": "عهد ضوء القمر", "Midnight Oath": "عهد منتصف الليل", "Keeper's Oath": "عهد الحافظ",
    "Infernal Legion": "الفيلق الجهنّمي", "Hellgrowth": "النماء الجهنّمي", "Red Bloom": "الإزهار الأحمر", "Red Gift": "الهبة الحمراء",
    "The Garden": "الحديقة", "The Reborn": "المولودون من جديد", "Shepherds": "الرعاة",
    "Apostate": "المرتد", "Apostate Hunts": "صيد المرتدين", "Specters": "الأشباح", "Inquisition": "محاكم التفتيش", "Inquisitor": "المفتّش",
    "Cardinal": "الكاردينال", "Archbishop": "رئيس الأساقفة", "Bishop": "الأسقف", "Scribe": "الكاتب",
    "The Veil": "الحجاب", "Purgatory": "المطهر", "Celestial Mountains": "الجبال السماوية",
    "Rite of Desolation": "طقس الخراب", "Great Reconstruction": "إعادة الإعمار الكبرى", "War of the Gods": "حرب الآلهة",
    "Sentinels": "الرقباء", "Rot Kin": "أهل العفن", "Feral": "متوحّش", "Death Knights": "فرسان الموت",
    "Cultists": "أتباع الطائفة", "Feral Vampires": "مصاصو الدماء المتوحشون", "Imps": "العفاريت", "Undead Captains": "قادة الموتى الأحياء",
    "Holy Phases": "الأطوار المقدّسة", "Blood Moon": "القمر الدموي", "Gallow's Wraith": "شبح المشنقة",
    "Lore Scrolls": "لفائف المعرفة", "Legendary Scraps": "قصاصات أسطورية", "Crescent Tags": "شارات الهلال",
    "Divine Ember": "الجمرة الإلهية", "Revenant Crown": "تاج العائد", "Cipher Fragment": "شظية الشيفرة",
    "Knight Commander": "قائد الفرسان", "The Divine": "الإله", "Divine Throne": "العرش الإلهي",
    # bosses
    "Dry Rot King": "ملك العفن الجاف", "E'frae": "إفراي", "Lord of Perdition": "سيّد الهلاك", "Mahkteah": "ماكتيا", "Mahkten": "ماكتن",
    "Eye of the Abyss": "عين الهاوية", "Aegoroth": "إيقوروث", "The Warden": "الحارس", "Tyrigon": "تيريقون",
    "Valahk-Nor": "ڤالاك-نور", "Felwyl": "فِلويل", "The Withered": "الذابل", "The Ascended": "الصاعد",
    # places
    "Gildenarch": "قيلدنارك", "Archspire": "أرشسباير", "Archspire Cathedral": "كاتدرائية أرشسباير",
    "Southern Ward": "الحي الجنوبي", "Gilded Ward": "الحي المذهّب", "Grimhaven": "قريمهاڤن", "Forsaken Streets": "الشوارع المهجورة",
    "Ramshorn Keep": "حصن رامزهورن", "Shoreditch Prison": "سجن شورديتش", "Elk Grove Academy": "أكاديمية إلك قروڤ",
    "Moore Manor": "قصر مور", "Godsreach Spire": "برج قودزريتش", "Sanctus Clypeus": "سانكتوس كليبيوس",
    "Luderaeon": "لوديرايون", "Akyreon": "أكيريون", "Velchoria": "ڤلتشوريا", "Velchorian Empire": "الإمبراطورية الڤلتشورية",
    "Luminar": "لومينار", "Karsiv": "كارسيف", "Armaea": "أرميا", "Belwayne": "بيلواين", "Litinstang": "ليتنستانق",
    "Nachtendale": "ناختنديل", "Saedrys": "سايدريس", "Caragus": "كاراقوس", "Treveyan": "تريڤيان", "Nachtstahl": "ناختشتال",
    "Eden": "إيدن", "Clan Moore": "عشيرة مور", "Telvaught": "تلڤوت",
    # characters
    "Gallant": "قالانت", "Solomon Moore": "سولومون مور", "Cardinal Mathias": "الكاردينال ماثياس", "Mereda": "ميريدا",
    "Lotte Ananta": "لوتّه أنانتا", "Gajov": "قاجوف", "Nahnias": "ناهنياس", "Lesandra": "ليساندرا", "Anya": "آنيا",
    "Selandris": "سيلاندريس", "Alonious": "ألونيوس", "Ciaran Telvaught": "كيران تلڤوت", "Irvine Gaertner": "إرڤين قارتنر",
    "Siron": "سيرون", "Maedrael": "مايدرايل", "Apothos": "أبوثوس", "Nac-Fei": "ناك-فاي",
}
EXTRA = [("the Order", "faction", "translate", "الجماعة", "short form of Order of the Crimson Moon; NOT النظام/التنظيم/الأمر"),
         ("Sigil", "mechanic", "translate", "ختم", "NOT رمز"), ("Run", "mechanic", "translate", "جولة", "as a mission attempt"),
         ("Chapter", "faction", "translate", "مجمع", "ecclesiastical body, NOT فصل"), ("Solomon", "character", "transliterate", "سولومون", ""),
         ("Mathias", "character", "transliterate", "ماثياس", ""), ("Lotte", "character", "transliterate", "لوتّه", "male merchant"),
         ("Abraxas", "story", "transliterate", "أبراكساس", "")]
p = os.path.join(BASE, "05_glossary.csv")
rows = list(csv.DictReader(open(p, encoding="utf-8")))
have = {r["source_term"] for r in rows}
n = 0
for r in rows:
    if r["source_term"] in A:
        r["approved_ar"], r["status"] = A[r["source_term"]], "approved"; n += 1
for t, ty, st, ar, note in EXTRA:
    if t not in have:
        rows.append({"source_term": t, "type": ty, "should_translate": st, "approved_ar": ar, "status": "approved", "notes": note}); n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["source_term", "type", "should_translate", "approved_ar", "status", "notes"])
    w.writeheader(); w.writerows(rows)
missing = [k for k in A if k not in have]
print("approved", n, "pending", sum(1 for r in rows if r["status"] == "pending"), "not-in-csv", missing)
