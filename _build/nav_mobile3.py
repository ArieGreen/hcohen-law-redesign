"""Three more mobile header + menu directions (n7..n9). The accessibility button always stays visible in the header,
also while the menu is open. Reuses base, hero and helpers from nav_mobile.py."""
import os
import runpy
import sys

ns = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nav_mobile.py'), run_name='lib')
A, ic, BASE, HERO, CONTACT, NAV, ICONS, AREAS = (ns[k] for k in ('A', 'ic', 'BASE', 'HERO', 'CONTACT', 'NAV', 'ICONS', 'AREAS'))
OUT = os.path.join(sys.argv[1], 'mockups', 'nav')
V = {}

# n7: two-tier header: a slim navy utility strip (accessibility, English, phone number) over a white bar with logo + name;
#     menu opens below the header as a navy page, practice areas unfolded under their item
V['n7'] = ('''
.util{height:34px;display:flex;align-items:center;gap:14px;padding:0 16px;background:var(--navy2);color:#fff;font-size:.82rem;position:relative;z-index:7}
.util .a11{display:flex;align-items:center;gap:6px;color:#fff;background:var(--accent);height:26px;padding:0 10px;border-radius:999px;font-weight:600}.util .a11 .icon{width:16px;height:16px}
.util .tel{margin-inline-start:auto;display:flex;align-items:center;gap:6px;font-weight:700;letter-spacing:.02em}.util .tel .icon{width:15px;height:15px;color:var(--sky)}
.util .en{color:var(--sky);font-weight:600}
.hdr{height:62px;display:flex;align-items:center;gap:10px;padding:0 16px;background:#fff;position:relative;z-index:7;box-shadow:0 6px 18px -12px rgba(0,0,0,.35)}
.brand{display:flex;align-items:center;gap:10px;margin-inline-end:auto}.brand img{width:38px}.brand b{display:block;font-size:1.2rem;font-weight:800;color:var(--navy);line-height:1.1}.brand small{font-size:.7rem;color:var(--ink2)}
.tog{display:flex;align-items:center;gap:8px;height:42px;padding:0 14px;border-radius:999px;background:var(--navy);color:#fff;font-weight:700;font-size:.9rem}
.menu{position:absolute;inset:96px 0 0;z-index:6;background:var(--navy);color:#fff;padding:12px 22px 0;display:none;flex-direction:column}
.open .menu{display:flex}
.menu .top>li>a{display:flex;justify-content:space-between;align-items:center;padding:15px 0;font-size:1.45rem;font-weight:800;border-bottom:1px solid rgba(255,255,255,.12)}
.menu .top>li>a .icon{color:var(--sky)}
.menu .has>a{border:0!important;padding-bottom:6px!important}
.sub{display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:4px 0 14px;border-bottom:1px solid rgba(255,255,255,.12)}
.sub a{padding:9px 10px;border-radius:8px;background:rgba(255,255,255,.07);font-size:.86rem;line-height:1.3;color:#DCE6F3}
.mfoot{margin:auto -22px 0;padding:16px 22px 22px;background:var(--navy2)}
.mfoot .adr{color:var(--sky);margin:0;font-size:.88rem}
''', lambda o: f'''<div class="util"><a class="a11">{ic("i-access")}נגישות</a><a class="en">English</a><a class="tel">{ic("i-phone")}077-7741818</a></div>
<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp"><span><b>ח. כהן</b><small>משרד עורכי דין ונוטריון</small></span></a>
<a class="tog">{ic("i-menu") if not o else "✕"}<span>תפריט</span></a></header>
<nav class="menu"><ul class="top"><li><a>אודות{ic("i-arrow")}</a></li><li class="has"><a>תחומי התמחות</a><div class="sub">{"".join(f"<a>{t}</a>" for t in AREAS)}</div></li>
<li><a>הצוות{ic("i-arrow")}</a></li><li><a>מאמרים{ic("i-arrow")}</a></li><li><a>צור קשר{ic("i-arrow")}</a></li></ul>
<div class="mfoot">{CONTACT}</div></nav>''')

# n8: emblem header: the HC mark sits in a white circle that hangs below the bar onto the photo; menu opens as a circle
#     growing from the menu button (navy), links centred and large
V['n8'] = ('''
.hdr{height:64px;display:grid;grid-template-columns:auto auto 1fr auto auto;align-items:center;gap:8px;padding:0 14px;background:#fff;position:relative;z-index:7;box-shadow:0 4px 14px -8px rgba(0,0,0,.25)}
.ib{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--line);color:var(--navy)}
.ib.call{background:var(--navy);color:#fff;border:0}.ib.a11{background:var(--accent);color:#fff;border:0}
.emb{position:absolute;left:50%;top:22px;transform:translateX(-50%);z-index:8;width:84px;height:84px;border-radius:50%;background:#fff;display:grid;place-items:center;box-shadow:0 10px 24px -10px rgba(0,0,0,.45);border:3px solid #fff;outline:1px solid var(--sky);outline-offset:-8px}
.emb img{width:54px}
.menu{position:absolute;inset:64px 0 0;z-index:6;background:radial-gradient(circle at 92% 4%,#17345E,var(--navy2) 70%);color:#fff;display:none;flex-direction:column;align-items:center;padding:70px 24px 0;text-align:center}
.open .menu{display:flex}
.menu li a{display:block;padding:12px 0;font-size:2rem;font-weight:800}
.menu li a:hover{color:var(--sky)}
.menu .dot{width:6px;height:6px;border-radius:50%;background:var(--sky);margin:6px auto}
.menu .en{margin-top:14px;padding:8px 18px;border:1px solid rgba(141,180,226,.5);border-radius:999px;color:var(--sky);font-weight:600}
.menu .ph2{margin-top:auto;margin-bottom:26px;display:flex;align-items:center;gap:10px;padding:14px 24px;border-radius:999px;background:#fff;color:var(--navy);font-weight:800;font-size:1.15rem}
.open .emb{top:22px}
''', lambda o: f'''<header class="hdr"><a class="ib">{ic("i-menu") if not o else "✕"}</a><a class="ib a11">{ic("i-access")}</a>
<a class="emb"><img src="{A}/img/logo-mark.webp"></a><span></span><a class="ib call">{ic("i-phone")}</a></header>
<nav class="menu"><ul>{"<li class='dot'></li>".join(f"<li><a>{t}</a></li>" for t in NAV)}</ul><a class="en">English</a>
<a class="ph2">{ic("i-phone")}077-7741818</a></nav>''')

# n9: header in two colours joined by the hero's diagonal: white logo side, navy action side with a sky edge;
#     menu drops as a navy sheet whose top edge repeats the diagonal
V['n9'] = ('''
.hdr{height:66px;display:flex;align-items:center;position:relative;z-index:7;background:#fff;overflow:hidden}
.hdr::before{content:"";position:absolute;inset:0;background:var(--navy);clip-path:polygon(0 0,46% 0,40% 100%,0 100%)}
.hdr::after{content:"";position:absolute;inset:0;background:var(--sky);clip-path:polygon(46% 0,47.2% 0,41.2% 100%,40% 100%)}
.brand{position:relative;z-index:1;display:flex;align-items:center;gap:10px;padding:0 16px;margin-inline-end:auto}.brand img{width:38px}.brand b{display:block;font-size:1.2rem;font-weight:800;color:var(--navy);line-height:1.1}.brand small{font-size:.68rem;color:var(--ink2)}
.acts2{position:relative;z-index:1;display:flex;gap:8px;padding:0 12px}
.ib{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;color:#fff;background:rgba(255,255,255,.12)}.ib.call{background:#fff;color:var(--navy)}
.menu{position:absolute;inset-inline:0;top:66px;z-index:6;display:none;color:#fff}
.open .menu{display:block}
.menu .sheet{background:var(--navy);padding:34px 22px 22px;clip-path:polygon(0 0,40% 0,46% 22px,100% 22px,100% 100%,0 100%);margin-top:-22px;padding-top:52px}
.menu li a{display:grid;grid-template-columns:30px 1fr auto;align-items:center;gap:12px;padding:14px 0;font-size:1.25rem;font-weight:700;border-bottom:1px solid rgba(255,255,255,.12)}
.menu li a .icon{color:var(--sky)}.menu li a .ar{width:18px;height:18px;color:rgba(255,255,255,.5)}
.menu .row2{display:grid;grid-template-columns:1fr auto;gap:10px;margin-top:18px}
.menu .ph2{display:flex;align-items:center;justify-content:center;gap:10px;height:50px;border-radius:10px;background:#fff;color:var(--navy);font-weight:800}
.menu .en{display:grid;place-items:center;padding:0 18px;border-radius:10px;border:1px solid rgba(255,255,255,.3);font-weight:600}
.menu .adr{color:var(--sky);font-size:.85rem;text-align:center;margin:12px 0 0}
.scrim{position:absolute;inset:0;background:rgba(11,28,53,.5);z-index:5;display:none}.open .scrim{display:block}
''', lambda o: f'''<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp"><span><b>ח. כהן</b><small>משרד עורכי דין ונוטריון</small></span></a>
<div class="acts2"><a class="ib">{ic("i-access")}</a><a class="ib call">{ic("i-phone")}</a><a class="ib">{ic("i-menu") if not o else "✕"}</a></div></header>
<div class="scrim"></div><nav class="menu"><div class="sheet"><ul>{"".join(f"<li><a>{ic(i)}<span>{t}</span>{ic('i-arrow','icon ar')}</a></li>" for t, i in zip(NAV, ICONS))}</ul>
<div class="row2"><a class="ph2">{ic("i-phone")}077-7741818</a><a class="en">English</a></div>{CONTACT}</div></nav>''')

for k, (css, body) in V.items():
    for state in ('closed', 'open'):
        o = state == 'open'
        html = (f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<meta name="robots" content="noindex"><title>{k}</title><style>{BASE}{css}</style></head><body class="{"open" if o else ""}">{body(o)}{HERO}</body></html>')
        open(os.path.join(OUT, f'{k}-{state}.html'), 'w', encoding='utf8').write(html)
print('ok')
