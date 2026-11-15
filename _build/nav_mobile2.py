"""Three more mobile header + menu directions (n4..n6). Reuses the base, hero and helpers from nav_mobile.py."""
import os
import runpy
import sys

ns = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nav_mobile.py'), run_name='lib')
A, ic, BASE, HERO, CONTACT, NAV, ICONS, AREAS = (ns[k] for k in ('A', 'ic', 'BASE', 'HERO', 'CONTACT', 'NAV', 'ICONS', 'AREAS'))
OUT = os.path.join(sys.argv[1], 'mockups', 'nav')
V = {}

# n4: transparent header over the photo; menu drops from the top as a navy panel: links in two columns + practice areas as chips
V['n4'] = ('''
.hdr{position:absolute;inset-inline:0;top:0;z-index:6;height:72px;display:flex;align-items:center;gap:8px;padding:0 16px;color:#fff;background:linear-gradient(rgba(11,28,53,.75),rgba(11,28,53,0))}
.brand{display:flex;align-items:center;gap:10px;margin-inline-end:auto;text-shadow:0 1px 8px rgba(0,0,0,.4)}.brand img{width:38px}.brand b{font-size:1.3rem;font-weight:800}
.ib{width:42px;height:42px;border-radius:10px;display:grid;place-items:center;background:rgba(255,255,255,.16);backdrop-filter:blur(8px)}.ib.call{background:#fff;color:var(--navy)}
.ph{height:300px}
.menu{position:absolute;inset-inline:0;top:0;z-index:5;background:var(--navy2);color:#fff;padding:86px 20px 22px;display:none;border-radius:0 0 22px 22px;box-shadow:0 30px 60px -20px rgba(0,0,0,.6)}
.open .menu{display:block}.open .hdr{background:none}
.menu .main{display:grid;grid-template-columns:1fr 1fr;gap:0 18px}
.menu .main a{display:block;padding:13px 0;font-size:1.25rem;font-weight:800;border-bottom:1px solid rgba(255,255,255,.12)}
.lab{margin:20px 0 10px;color:var(--sky);font-size:.85rem;font-weight:600}
.chips{display:flex;flex-wrap:wrap;gap:8px}.chips a{padding:8px 12px;border-radius:999px;border:1px solid rgba(141,180,226,.4);font-size:.88rem}
.menu .row2{display:grid;grid-template-columns:1fr auto;gap:10px;margin-top:20px}
.menu .ph2{display:flex;align-items:center;justify-content:center;gap:10px;height:50px;border-radius:10px;background:#fff;color:var(--navy);font-weight:800}
.menu .en{display:grid;place-items:center;padding:0 18px;border-radius:10px;border:1px solid rgba(255,255,255,.3);font-weight:600}
''', lambda o: f'''<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp"><b>ח. כהן</b></a>
<a class="ib">{ic("i-access")}</a><a class="ib call">{ic("i-phone")}</a><a class="ib">{ic("i-menu") if not o else "✕"}</a></header>
<nav class="menu"><div class="main">{"".join(f"<a>{t}</a>" for t in NAV)}</div>
<p class="lab">תחומי התמחות</p><div class="chips">{"".join(f"<a>{t}</a>" for t in AREAS)}</div>
<div class="row2"><a class="ph2">{ic("i-phone")}077-7741818</a><a class="en">English</a></div></nav>''')

# n5: centred logo (menu on one side, call on the other); menu = full-screen white page, big navy links, navy contact block
V['n5'] = ('''
.hdr{height:72px;display:grid;grid-template-columns:52px 1fr 52px;align-items:center;padding:0 12px;background:#fff;position:relative;z-index:6;border-bottom:1px solid var(--line)}
.brand{display:flex;flex-direction:column;align-items:center;line-height:1}.brand img{width:40px}.brand small{font-size:.66rem;color:var(--ink2);margin-top:3px}
.ib{width:44px;height:44px;display:grid;place-items:center;color:var(--navy);border-radius:50%;border:1px solid var(--line)}.ib.call{justify-self:end;background:var(--navy);color:#fff;border:0}
.menu{position:absolute;inset:72px 0 0;z-index:5;background:#fff;display:none;flex-direction:column;padding:10px 24px 0}
.open .menu{display:flex}
.menu li a{display:flex;align-items:baseline;gap:14px;padding:15px 0;font-size:2rem;font-weight:800;color:var(--navy)}
.menu li a::after{content:"";flex:1;height:1px;background:var(--line);transform:translateY(-.35em)}
.menu .en{color:var(--accent);font-weight:700;margin-top:6px;display:flex;gap:16px;align-items:center}
.blk{margin:auto -24px 0;background:var(--navy);color:#fff;padding:22px 24px 26px}
.blk .ph2{display:flex;align-items:center;gap:12px;font-size:1.5rem;font-weight:800}.blk .ph2 .icon{color:var(--sky);width:26px;height:26px}
.blk .adr{color:var(--sky);margin:8px 0 0;font-size:.9rem}
''', lambda o: f'''<header class="hdr"><a class="ib">{ic("i-menu") if not o else "✕"}</a><a class="brand"><img src="{A}/img/logo-mark.webp"><small>ח. כהן · משרד עורכי דין</small></a><a class="ib call">{ic("i-phone")}</a></header>
<nav class="menu"><ul>{"".join(f"<li><a>{t}</a></li>" for t in NAV)}</ul><a class="en">English<span>{ic("i-access")}</span></a>
<div class="blk"><a class="ph2">{ic("i-phone")}077-7741818</a>{CONTACT}</div></nav>''')

# n6: app style: slim header + bottom tab bar with the five pages; the practice-areas tab opens a sheet with the six areas
V['n6'] = ('''
.hdr{height:60px;display:flex;align-items:center;gap:8px;padding:0 16px;background:#fff;border-bottom:1px solid var(--line);position:relative;z-index:6}
.brand{display:flex;align-items:center;gap:10px;margin-inline-end:auto}.brand img{width:34px}.brand b{font-size:1.2rem;font-weight:800;color:var(--navy)}.brand small{display:block;font-size:.68rem;color:var(--ink2);font-weight:500}
.ib{width:40px;height:40px;display:grid;place-items:center;color:var(--navy);border-radius:10px;background:var(--mist)}.ib.call{background:var(--navy);color:#fff}
.tabs{position:absolute;inset-inline:0;bottom:0;z-index:9;height:70px;display:grid;grid-template-columns:repeat(5,1fr);background:#fff;border-top:1px solid var(--line);box-shadow:0 -8px 24px -14px rgba(0,0,0,.25)}
.tabs a{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;font-size:.72rem;font-weight:600;color:var(--ink2);text-align:center;line-height:1.15}.tabs .icon{width:22px;height:22px}
.tabs a.on{color:var(--accent)}.tabs a.on::before{content:"";position:absolute;top:0;width:34px;height:3px;border-radius:2px;background:var(--accent)}
.scrim{position:absolute;inset:0;background:rgba(11,28,53,.55);display:none;z-index:7}.open .scrim{display:block}
.sheet{position:absolute;inset-inline:0;bottom:70px;z-index:8;background:#fff;border-radius:20px 20px 0 0;padding:10px 18px 14px;display:none}
.open .sheet{display:block}.grab{width:44px;height:5px;border-radius:3px;background:var(--line);margin:0 auto 12px}
.sheet h3{margin:0 0 6px;color:var(--navy);font-size:1.1rem}
.sheet a{display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--line);font-weight:600;color:var(--navy)}.sheet a .icon{color:var(--accent);width:18px;height:18px}
''', lambda o: f'''<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp"><span><b>ח. כהן</b><small>משרד עורכי דין ונוטריון</small></span></a>
<a class="ib">{ic("i-access")}</a><a class="ib call">{ic("i-phone")}</a></header>
<div class="scrim"></div><div class="sheet"><div class="grab"></div><h3>תחומי התמחות</h3>{"".join(f"<a>{t}{ic('i-arrow')}</a>" for t in AREAS)}</div>
<nav class="tabs">{"".join(f'<a class="{"on" if (o and i == 1) else ""}">{ic(n)}{t}</a>' for i, (t, n) in enumerate(zip(NAV, ICONS)))}</nav>''')

for k, (css, body) in V.items():
    for state in ('closed', 'open'):
        o = state == 'open'
        html = (f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<meta name="robots" content="noindex"><title>{k}</title><style>{BASE}{css}</style></head><body class="{"open" if o else ""}">{body(o)}{HERO}</body></html>')
        open(os.path.join(OUT, f'{k}-{state}.html'), 'w', encoding='utf8').write(html)
print('ok')
