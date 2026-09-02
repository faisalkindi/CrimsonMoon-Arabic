"""Render 05_glossary_rationale.md into a bilingual review page (build/glossary.html)."""
import re, os, html, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
md = open(os.path.join(BASE, "05_glossary_rationale.md"), encoding="utf-8").read().splitlines()
AR = re.compile(r"[؀-ۿ]")


def inline(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    # wrap Arabic runs so they get the Arabic face + RTL isolation
    return re.sub(r"([؀-ۿ][؀-ۿ\s،؛؟\-ـًٌٍَُِّْ]*)", r'<span class="ar">\1</span>', s)


out, i, sec_id, nav = [], 0, 0, []
in_table, table_rows = False, []


def flush_table():
    global table_rows, in_table
    if not table_rows: return
    head, body = table_rows[0], table_rows[2:]
    cols = [c.strip() for c in head.strip("|").split("|")]
    out.append('<div class="tablewrap"><table><thead><tr>' + "".join(f"<th>{html.escape(c)}</th>" for c in cols) + "</tr></thead><tbody>")
    for r in body:
        cells = [c.strip() for c in r.strip("|").split("|")]
        tds = []
        for j, c in enumerate(cells):
            cls = ' class="arcell"' if AR.search(c) and j == 1 else (' class="num"' if re.fullmatch(r"\d+", c) else "")
            tds.append(f"<td{cls}>{inline(c)}</td>")
        out.append("<tr>" + "".join(tds) + "</tr>")
    out.append("</tbody></table></div>")
    table_rows = []; in_table = False


while i < len(md):
    line = md[i]
    if line.startswith("|"):
        in_table = True; table_rows.append(line); i += 1; continue
    if in_table: flush_table()
    if line.startswith("# "): i += 1; continue
    m = re.match(r"^(#{2,3}) (.*)", line)
    if m:
        lvl = len(m.group(1)); sec_id += 1; title = m.group(2)
        aid = f"s{sec_id}"; nav.append((lvl, title, aid))
        out.append(f'<h{lvl} id="{aid}">{inline(title)}</h{lvl}>'); i += 1; continue
    if line.startswith("- "):
        items = []
        while i < len(md) and md[i].startswith("- "): items.append(md[i][2:]); i += 1
        out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
    if re.match(r"^\d+\. ", line):
        items = []
        while i < len(md) and re.match(r"^\d+\. ", md[i]): items.append(re.sub(r"^\d+\. ", "", md[i])); i += 1
        out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); continue
    if line.strip() == "---" or not line.strip(): i += 1; continue
    out.append(f"<p>{inline(line)}</p>"); i += 1
if in_table: flush_table()

navhtml = "".join(f'<a class="l{l}" href="#{a}">{html.escape(re.sub(r" \(\d+\)$", "", t))}</a>' for l, t, a in nav)
approved = sum(1 for l in md if l.startswith("|") and "|" in l[1:] and AR.search(l))
page = f"""<title>Crimson Moon Arabic Glossary</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Source+Sans+3:wght@400;600&family=Noto+Naskh+Arabic:wght@400;600&display=swap">
<style>
:root{{--bg:#F2F1EF;--panel:#FBFAF8;--ink:#1B1A21;--muted:#5E5A66;--line:#D9D5CF;--accent:#A11C2B;--gold:#8C6D1F;--code:#E9E5DF;
  --serif:'Cormorant Garamond',Georgia,serif;--sans:'Source Sans 3','Segoe UI',system-ui,sans-serif;--arabic:'Noto Naskh Arabic','Segoe UI',Tahoma,sans-serif;}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#17151C;--panel:#1F1C25;--ink:#ECE8E1;--muted:#A9A3B0;--line:#332F3B;--accent:#E0475A;--gold:#D2B15A;--code:#2A2631;}}}}
:root[data-theme="dark"]{{--bg:#17151C;--panel:#1F1C25;--ink:#ECE8E1;--muted:#A9A3B0;--line:#332F3B;--accent:#E0475A;--gold:#D2B15A;--code:#2A2631;}}
body{{background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.5;margin:0}}
.wrap{{display:grid;grid-template-columns:230px minmax(0,1fr);gap:40px;max-width:1380px;margin:0 auto;padding:36px 28px 80px}}
nav{{position:sticky;top:20px;align-self:start;max-height:calc(100vh - 40px);overflow:auto;font-size:13px;border-right:1px solid var(--line);padding-right:16px}}
nav a{{display:block;color:var(--muted);text-decoration:none;padding:3px 0}}nav a.l2{{color:var(--ink);font-weight:600;margin-top:12px;font-family:var(--serif);font-size:16px}}nav a.l3{{padding-left:10px}}nav a:hover,nav a:focus{{color:var(--accent);outline:none}}
header{{margin-bottom:28px;border-bottom:2px solid var(--accent);padding-bottom:18px}}
header h1{{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.05;margin:0 0 6px;text-wrap:balance}}
header p{{margin:0;color:var(--muted);max-width:70ch}}
.stats{{display:flex;gap:28px;margin-top:14px;font-variant-numeric:tabular-nums}}.stats b{{font-family:var(--serif);font-size:28px;font-weight:600;display:block;line-height:1}}.stats span{{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
main h2{{font-family:var(--serif);font-size:32px;font-weight:600;margin:48px 0 10px;text-wrap:balance}}
main h3{{font-family:var(--serif);font-size:22px;font-weight:600;margin:30px 0 8px;color:var(--accent)}}
main p{{max-width:75ch}}
.tablewrap{{overflow-x:auto;background:var(--panel);border:1px solid var(--line)}}
table{{border-collapse:collapse;width:100%;font-size:14px}}th{{text-align:left;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--line);background:var(--panel);position:sticky;top:0}}
td{{padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}}tr:last-child td{{border-bottom:0}}
td:first-child{{font-weight:600;white-space:nowrap}}
.arcell{{font-family:var(--arabic);font-size:19px;direction:rtl;text-align:right;white-space:nowrap;color:var(--accent);font-weight:600}}
.ar{{font-family:var(--arabic);font-size:1.15em;unicode-bidi:isolate;direction:rtl;display:inline-block}}
.num{{font-variant-numeric:tabular-nums;text-align:right;color:var(--muted)}}
code{{font-family:ui-monospace,Consolas,monospace;font-size:.9em;background:var(--code);padding:1px 5px;border-radius:3px}}
ul,ol{{max-width:80ch}}li{{margin:4px 0}}
main h2:nth-of-type(3),main h2:nth-of-type(3)~h3{{color:var(--gold)}}
@media (max-width:900px){{.wrap{{grid-template-columns:1fr}}nav{{position:static;border:0;padding:0;max-height:none;columns:2}}}}
@media (prefers-reduced-motion:no-preference){{html{{scroll-behavior:smooth}}}}
</style>
<div class="wrap"><nav>{navhtml}</nav><main>
<header><h1>Crimson Moon Arabic Glossary</h1><p>Every frozen term with what it is in the game and why it reads the way it does. Pending terms list the candidates and a recommendation; the decision is Faisal's. Arabic in <span class="ar">قرمزي</span> is the approved rendering.</p>
<div class="stats"><div><b>188</b><span>approved</span></div><div><b>0</b><span>pending</span></div><div><b>8,686</b><span>rows translated</span></div></div></header>
{''.join(out)}
</main></div>"""
p = os.path.join(BASE, "build", "glossary.html"); open(p, "w", encoding="utf-8").write(page); print("wrote", p, len(page))
