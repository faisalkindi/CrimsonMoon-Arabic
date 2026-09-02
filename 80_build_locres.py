"""Build ar/Game.locres (locres v3) from 03_working_draft.jsonl using the en locres as structural template.
Keeps namespace/key hashes from the source file; rebuilds the string table deduplicated by text so keys that
shared one English string may carry different Arabic. Rows with skip=true or empty ar fall back to English.
Usage: python 80_build_locres.py [out_dir]"""
import json, struct, os, io, sys
from collections import OrderedDict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "extract/pak/CrimsonMoonNG/Content/Localization/Game/en/Game.locres")


def rstr(f):
    n = struct.unpack("<i", f.read(4))[0]
    if n < 0: return f.read(-n * 2)[:-2].decode("utf-16le")
    return f.read(n)[:-1].decode("utf-8") if n else ""


def wstr(s):
    if s == "": return struct.pack("<i", 0)
    if all(ord(c) < 128 for c in s):
        b = s.encode() + b"\0"; return struct.pack("<i", len(b)) + b
    b = s.encode("utf-16le") + b"\0\0"; return struct.pack("<i", -(len(b) // 2)) + b


def parse(path):
    f = open(path, "rb"); magic = f.read(16); ver = f.read(1)[0]; assert ver == 3
    off = struct.unpack("<q", f.read(8))[0]; f.read(4); nsc = struct.unpack("<I", f.read(4))[0]
    cur = f.tell(); f.seek(off); n = struct.unpack("<I", f.read(4))[0]
    strings = []
    for _ in range(n): strings.append(rstr(f)); f.read(4)
    f.seek(cur); ns_list = []
    for _ in range(nsc):
        nh = struct.unpack("<I", f.read(4))[0]; ns = rstr(f); kc = struct.unpack("<I", f.read(4))[0]; keys = []
        for _ in range(kc):
            kh = struct.unpack("<I", f.read(4))[0]; key = rstr(f); sh = struct.unpack("<I", f.read(4))[0]; idx = struct.unpack("<i", f.read(4))[0]
            keys.append((kh, key, sh, strings[idx]))
        ns_list.append((nh, ns, keys))
    return magic, ns_list


def build(ns_list, translate):
    table, index = OrderedDict(), {}
    body = bytearray()
    entries = 0
    for nh, ns, keys in ns_list:
        body += struct.pack("<I", nh) + wstr(ns) + struct.pack("<I", len(keys))
        for kh, key, sh, en in keys:
            text = translate(ns, key, en)
            if text not in index:
                index[text] = len(table); table[text] = 0
            table[text] += 1
            body += struct.pack("<I", kh) + wstr(key) + struct.pack("<I", sh) + struct.pack("<i", index[text]); entries += 1
    head = bytearray(b"\x0e\x14\x74\x75\x67\x4a\x03\xfc\x4a\x15\x90\x9d\xc3\x37\x7f\x1b") + b"\x03"
    strings = struct.pack("<I", len(table))
    for text, rc in table.items(): strings += wstr(text) + struct.pack("<I", rc)
    off = 17 + 8 + 4 + 4 + len(body)
    return bytes(head) + struct.pack("<q", off) + struct.pack("<I", entries) + struct.pack("<I", len(ns_list)) + bytes(body) + strings


if __name__ == "__main__":
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "build", "ar_mod", "CrimsonMoonNG", "Content", "Localization", "Game", "ar")
    magic, ns_list = parse(SRC)
    draft = {r["id"]: r for r in (json.loads(l) for l in open(os.path.join(BASE, "03_working_draft.jsonl"), encoding="utf-8") if l.strip())}
    stats = {"ar": 0, "fallback_en": 0}
    def translate(ns, key, en):
        r = draft.get(f"{ns}|{key}")
        if r and not r.get("skip") and r.get("ar"):
            stats["ar"] += 1; return r["ar"]
        stats["fallback_en"] += 1; return en
    data = build(ns_list, translate)
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "Game.locres"), "wb").write(data)
    # self-check: re-parse and compare a few
    m2, ns2 = parse(os.path.join(out_dir, "Game.locres"))
    assert m2 == magic and sum(len(k) for _, _, k in ns2) == sum(len(k) for _, _, k in ns_list)
    sample = [(ns, key, t) for _, ns, keys in ns2 for _, key, _, t in keys][:3]
    print("written", os.path.join(out_dir, "Game.locres"), len(data), "bytes", stats, "sample:", sample)
