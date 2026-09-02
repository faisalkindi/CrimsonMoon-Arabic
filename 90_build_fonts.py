"""Merge SST Arabic Medium glyphs INTO Crimson Moon's own UI fonts (Asul x2, CrimsonText x5) so Latin design
survives and Arabic renders. Ported from MortalShell2 82+84+85 (proven on UE5.6):
  merge Arabic subset (scaled to target upem) -> restore ORIGINAL vertical metrics (UE BoundingBox layout reads
  head yMax/yMin) -> lower yMin only, for Arabic descender room -> wrap [u32 size][ttf][u32 0].
CJK Noto faces untouched. Output staged into build/ar_mod (same IoStore triple as the locres).
Usage: python 90_build_fonts.py"""
import io, os, struct, sys
from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, Options
from fontTools.merge import Merger
from fontTools.ttLib.scaleUpem import scale_upem
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
SST = r"C:\Users\Faisal\Ai\Mods Dev\_shared\fonts\SST-Arabic-Medium_sanitized.ttf"
SRC_DIR = os.path.join(BASE, "extract", "pak", "CrimsonMoonNG", "Content", "UI", "Fonts")
STAGE = os.path.join(BASE, "build", "ar_mod", "CrimsonMoonNG", "Content", "UI", "Fonts")
WORK = os.path.join(BASE, "font_build"); os.makedirs(WORK, exist_ok=True); os.makedirs(STAGE, exist_ok=True)
FACES = ["FontFace_Asul_Bold", "FontFace_Asul_Regular", "FontFace_CrimsonText_BoldItalic", "FontFace_CrimsonText_Italic",
         "FontFace_CrimsonText_Regular", "FontFace_CrimsonText_SemiBold", "FontFace_CrimsonText_SemiBoldItalic"]
# engine faces used by Font_Subtitles (Roboto family) — same merge, different path
ENGINE_SRC = os.path.join(BASE, "extract", "pak", "Engine", "Content", "EngineFonts", "Faces")
ENGINE_STAGE = os.path.join(BASE, "build", "ar_mod", "Engine", "Content", "EngineFonts", "Faces")
ENGINE_FACES = ["RobotoRegular", "RobotoBold", "RobotoItalic", "RobotoBoldItalic", "RobotoLight", "RobotoTiny"]
ARABIC = list(range(0x0600, 0x0700)) + list(range(0x0750, 0x0780)) + list(range(0x08A0, 0x0900)) + \
         list(range(0xFB50, 0xFE00)) + list(range(0xFE70, 0xFF00)) + [0x200C, 0x200D, 0x200E, 0x200F]
MARGIN = 40


def unwrap(raw):
    n = struct.unpack("<I", raw[:4])[0]; return raw[4:4 + n]


def wrap(b):
    return struct.pack("<I", len(b)) + b + struct.pack("<I", 0)


def arabic_subset(upem):
    f = TTFont(SST)
    o = Options(); o.layout_features = ["*"]; o.notdef_outline = True; o.recalc_bounds = False; o.drop_tables = []
    s = Subsetter(options=o); s.populate(unicodes=ARABIC); s.subset(f)
    if f["head"].unitsPerEm != upem: scale_upem(f, upem)
    p = os.path.join(WORK, f"sst_arabic_{upem}.ttf"); f.save(p); return p


def deepest_arabic(font):
    glyf = font["glyf"]; low = 0
    for cp, gn in font.getBestCmap().items():
        if (0x0600 <= cp <= 0x06FF or 0xFB50 <= cp <= 0xFEFF) and gn in glyf:
            g = glyf[gn]
            if g.numberOfContours != 0 and hasattr(g, "yMin") and g.yMin < low: low = g.yMin
    return low


def build(face, src_dir=None, stage=None):
    src_dir = src_dir or SRC_DIR; stage = stage or STAGE; os.makedirs(stage, exist_ok=True)
    orig_ttf = unwrap(open(os.path.join(src_dir, face + ".ufont"), "rb").read())
    orig_p = os.path.join(WORK, face + ".orig.ttf"); open(orig_p, "wb").write(orig_ttf)
    orig = TTFont(orig_p, recalcBBoxes=False, recalcTimestamp=False)
    assert "CFF " not in orig, f"{face} is CFF; wholesale replace needed"
    upem = orig["head"].unitsPerEm
    merged = Merger().merge([orig_p, arabic_subset(upem)])
    buf = io.BytesIO(); merged.save(buf)
    m = TTFont(io.BytesIO(buf.getvalue()), recalcBBoxes=False, recalcTimestamp=False)
    # restore original vertical metrics (baseline position under BoundingBox layout)
    for k in ("yMax", "yMin", "xMax", "xMin"): setattr(m["head"], k, getattr(orig["head"], k))
    for k in ("ascent", "descent", "lineGap"): setattr(m["hhea"], k, getattr(orig["hhea"], k))
    for k in ("sTypoAscender", "sTypoDescender", "sTypoLineGap", "usWinAscent", "usWinDescent"):
        if hasattr(orig["OS/2"], k): setattr(m["OS/2"], k, getattr(orig["OS/2"], k))
    # descender room: lower yMin only (yMax = baseline anchor untouched)
    need = deepest_arabic(m) - MARGIN; old_ymin = m["head"].yMin
    if need < m["head"].yMin:
        m["head"].yMin = need; m["hhea"].descent = min(m["hhea"].descent, need)
        m["OS/2"].usWinDescent = max(m["OS/2"].usWinDescent, abs(need)); m["OS/2"].sTypoDescender = min(m["OS/2"].sTypoDescender, need)
    out = io.BytesIO(); m.save(out)
    open(os.path.join(stage, face + ".ufont"), "wb").write(wrap(out.getvalue()))
    chk = TTFont(io.BytesIO(out.getvalue()), recalcBBoxes=False); cm = chk.getBestCmap()
    print(f"{face:36} upem={upem} latin={0x41 in cm} arabic={0x627 in cm and 0xFE8E in cm or 0x627 in cm} glyphs={len(cm)} yMax={chk['head'].yMax} yMin {old_ymin}->{chk['head'].yMin} bytes={len(out.getvalue())}")
    assert 0x627 in cm and 0x41 in cm


if __name__ == "__main__":
    for face in FACES: build(face)
    for face in ENGINE_FACES: build(face, ENGINE_SRC, ENGINE_STAGE)
    print("staged", len(FACES) + len(ENGINE_FACES), "fonts")
