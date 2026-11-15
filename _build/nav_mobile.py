"""Three mobile header + menu directions (390px), each rendered closed and open. Same nav labels and contact details as the site."""
import os
import sys

OUT = os.path.join(sys.argv[1], 'mockups', 'nav')
os.makedirs(OUT, exist_ok=True)
A = '../../assets'
NAV = ['אודות', 'תחומי התמחות', 'הצוות', 'מאמרים', 'צור קשר']
ICONS = ['i-briefcase', 'i-key', 'i-users', 'i-book', 'i-chat']


def ic(n, c='icon'):
    return f'<svg class="{c}"><use href="{A}/img/icons.svg#{n}"/></svg>'


BASE = f'''@font-face{{font-family:Heebo;font-weight:100 900;src:url({A}/fonts/heebo-hebrew.woff2) format('woff2');unicode-range:U+0590-05FF,U+200C-2010}}
@font-face{{font-family:Heebo;font-weight:100 900;src:url({A}/fonts/heebo-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+2000-206F}}
:root{{--navy:#12294A;--navy2:#0B1C35;--ink:#0F1B2D;--ink2:#4A5568;--mist:#F3F5F8;--accent:#1F5FAD;--sky:#8DB4E2;--line:#E1E5EB}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Heebo,Arial;color:var(--ink);background:var(--navy);height:844px;overflow:hidden;position:relative}}
img{{display:block;max-width:100%}}a{{color:inherit;text-decoration:none}}ul{{list-style:none;margin:0;padding:0}}
.icon{{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;flex:none}}
/* hero context (as on the site) */
.ph{{height:250px;clip-path:polygon(0 0,100% 0,100% 72%,0 100%)}}.ph img{{width:100%;height:100%;object-fit:cover;object-position:35% 20%}}
.c{{padding:6px 20px;color:#fff}}.row{{display:flex;align-items:center;gap:16px}}.row img{{width:72px}}
.nm{{display:block;font-size:2.9rem;font-weight:800;line-height:1}}.pr{{display:block;font-size:1.3rem;font-weight:300;color:var(--sky)}}
.yr{{color:var(--sky);margin:14px 0 0}}.tag{{color:#D3DCEA;line-height:1.6;margin:12px 0 0}}
.acts{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:20px}}.b{{min-height:50px;border-radius:6px;border:1.5px solid rgba(255,255,255,.45);display:grid;place-items:center;color:#fff;font-weight:600}}.b.s{{grid-column:1/-1;background:#fff;color:var(--navy)}}
'''
HERO = f'''<div class="ph"><img src="{A}/img/bsr-day-1000.webp"></div><div class="c"><div class="row"><img src="{A}/img/logo-mark.webp"><div><span class="nm">ח. כהן</span><span class="pr">משרד עורכי דין</span></div></div>
<p class="yr">— מאז 2001</p><p class="tag">ייעוץ וייצוג לרשויות מקומיות, תאגידי מים, מועצות דתיות, חברות קדישא ומוסדות חינוך</p>
<div class="acts"><a class="b s">תחומי ההתמחות</a><a class="b">מאמרים</a><a class="b">צור קשר</a></div></div>'''
CONTACT = ('<p class="adr">דרך בן גוריון 2, רמת גן · מגדלי ב.ס.ר, קומה 9</p>')

V = {}

# n1: navy header that continues the hero; menu = full-screen navy sheet with big links
V['n1'] = ('''
.hdr{height:68px;display:flex;align-items:center;gap:8px;padding:0 16px;background:var(--navy);border-bottom:1px solid rgba(255,255,255,.12);color:#fff;position:relative;z-index:6}
.brand{display:flex;align-items:center;gap:10px;margin-inline-end:auto}.brand img{width:36px}.brand b{font-size:1.25rem;font-weight:800}
.ib{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;border:1px solid rgba(255,255,255,.25)}.ib.call{background:#fff;color:var(--navy);border:0}
.menu{position:absolute;inset:68px 0 0;background:var(--navy2);color:#fff;padding:22px 24px;display:none;flex-direction:column;z-index:5}
.open .menu{display:flex}
.menu li a{display:flex;justify-content:space-between;align-items:center;padding:18px 0;font-size:1.9rem;font-weight:800;border-bottom:1px solid rgba(255,255,255,.1)}
.menu li a .icon{color:var(--sky);width:24px;height:24px}
.menu .en{margin-top:18px;color:var(--sky);font-weight:600}
.menu .foot{margin-top:auto;padding-top:20px;border-top:1px solid rgba(141,180,226,.35)}
.menu .ph2{display:flex;align-items:center;justify-content:center;gap:10px;height:54px;border-radius:8px;background:#fff;color:var(--navy);font-weight:800;font-size:1.15rem}
.adr{color:var(--sky);font-size:.9rem;text-align:center;margin:12px 0 0}
''', lambda o: f'''<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp"><b>ח. כהן</b></a>
<a class="ib">{ic("i-access")}</a><a class="ib call">{ic("i-phone")}</a><a class="ib">{ic("i-menu") if not o else "✕"}</a></header>
<nav class="menu"><ul>{"".join(f"<li><a>{t}{ic('i-arrow')}</a></li>" for t in NAV)}</ul><a class="en">English</a>
<div class="foot"><a class="ph2">{ic("i-phone")}077-7741818</a>{CONTACT}</div></nav>''')

# n2: white header, rounded; menu = bottom sheet with icon tiles + contact buttons
V['n2'] = ('''
body{background:var(--navy)}
.hdr{position:relative;z-index:6;margin:10px 12px 0;height:60px;display:flex;align-items:center;gap:8px;padding:0 8px 0 12px;background:#fff;border-radius:14px;box-shadow:0 10px 30px -14px rgba(0,0,0,.5)}
.wrap{margin-top:-70px}
.brand{display:flex;align-items:center;gap:8px;margin-inline-end:auto}.brand img{width:34px}.brand b{font-size:1.2rem;font-weight:800}.brand small{display:block;font-size:.68rem;color:var(--ink2);font-weight:500}
.ib{width:42px;height:42px;border-radius:10px;display:grid;place-items:center;background:var(--mist);color:var(--navy)}.ib.call{background:var(--navy);color:#fff}
.ph{height:270px}
.scrim{position:absolute;inset:0;background:rgba(11,28,53,.55);display:none;z-index:7}.open .scrim{display:block}
.menu{position:absolute;inset-inline:0;bottom:0;z-index:8;background:#fff;border-radius:22px 22px 0 0;padding:12px 18px 22px;display:none}
.open .menu{display:block}
.grab{width:44px;height:5px;border-radius:3px;background:var(--line);margin:0 auto 16px}
.menu ul{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.menu li a{display:flex;flex-direction:column;gap:12px;padding:18px 16px;border-radius:12px;background:var(--mist);font-weight:700;font-size:1.05rem;color:var(--navy)}
.menu li a .icon{color:var(--accent);width:26px;height:26px}
.menu li:last-child a{background:var(--navy);color:#fff}.menu li:last-child .icon{color:var(--sky)}
.menu .en{display:block;text-align:center;margin:14px 0;color:var(--accent);font-weight:600}
.menu .ph2{display:flex;align-items:center;justify-content:center;gap:10px;height:54px;border-radius:10px;border:1.5px solid var(--navy);color:var(--navy);font-weight:800;font-size:1.1rem}
.adr{color:var(--ink2);font-size:.85rem;text-align:center;margin:10px 0 0}
''', lambda o: f'''<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp"><span><b>ח. כהן</b><small>משרד עורכי דין ונוטריון</small></span></a>
<a class="ib">{ic("i-access")}</a><a class="ib call">{ic("i-phone")}</a><a class="ib">{ic("i-menu")}</a></header><div class="wrap"></div>
<div class="scrim"></div><nav class="menu"><div class="grab"></div><ul>{"".join(f"<li><a>{ic(i)}{t}</a></li>" for t,i in zip(NAV,ICONS))}<li><a>{ic("i-map")}English</a></li></ul>
<a class="ph2" style="margin-top:14px">{ic("i-phone")}077-7741818</a>{CONTACT}</nav>''')

# n3: white header with a thin sky rule; menu = side drawer from the right with the practice areas listed under their item
AREAS = ['שירותי דת וקבורה', 'דיני עבודה במגזר הציבורי', 'משפט מנהלי', 'מכרזים והתקשרויות', 'רגולציה וכשרות', 'אכיפת חיובים עבור רשויות ותאגידי מים']
V['n3'] = ('''
.hdr{height:68px;display:flex;align-items:center;gap:8px;padding:0 16px;background:#fff;border-bottom:3px solid var(--sky);position:relative;z-index:4}
.brand{display:flex;align-items:center;gap:10px;margin-inline-end:auto}.brand img{width:38px}.brand b{font-size:1.25rem;font-weight:800;color:var(--navy)}
.ib{width:42px;height:42px;display:grid;place-items:center;color:var(--navy)}.ib.call{border-radius:50%;background:var(--navy);color:#fff}
.burger{display:flex;flex-direction:column;gap:5px;width:42px;align-items:center}.burger i{display:block;width:22px;height:2px;background:var(--navy);border-radius:2px}.burger i:nth-child(2){width:14px;align-self:flex-end;margin-inline-end:10px}
.scrim{position:absolute;inset:0;background:rgba(11,28,53,.6);display:none;z-index:7}.open .scrim{display:block}
.menu{position:absolute;top:0;bottom:0;inset-inline-start:0;width:86%;z-index:8;background:#fff;display:none;flex-direction:column;box-shadow:20px 0 50px -20px rgba(0,0,0,.5)}
.open .menu{display:flex}
.mhead{display:flex;align-items:center;justify-content:space-between;padding:0 18px;height:68px;background:var(--navy);color:#fff}.mhead img{width:36px}
.menu ul.top{padding:6px 22px}.menu .top>li>a{display:block;padding:14px 0;font-size:1.25rem;font-weight:800;color:var(--navy);border-bottom:1px solid var(--line)}
.sub{padding:6px 0 10px;border-bottom:1px solid var(--line)}.sub a{display:flex;align-items:center;gap:10px;padding:7px 0;color:var(--ink2);font-size:.95rem}.sub a::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--accent)}
.menu .top>li.has>a{border:0;padding-bottom:4px}
.mfoot{margin-top:auto;padding:16px 22px 22px;background:var(--mist)}
.mfoot .ph2{display:flex;align-items:center;justify-content:center;gap:10px;height:52px;border-radius:8px;background:var(--navy);color:#fff;font-weight:800}
.adr{color:var(--ink2);font-size:.85rem;text-align:center;margin:10px 0 0}
''', lambda o: f'''<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp"><b>ח. כהן</b></a>
<a class="ib">{ic("i-access")}</a><a class="ib call">{ic("i-phone")}</a><a class="ib burger"><i></i><i></i><i></i></a></header>
<div class="scrim"></div><nav class="menu"><div class="mhead"><img src="{A}/img/logo-mark.webp"><span>✕</span></div>
<ul class="top"><li><a>אודות</a></li><li class="has"><a>תחומי התמחות</a><div class="sub">{"".join(f"<a>{t}</a>" for t in AREAS)}</div></li>
<li><a>הצוות</a></li><li><a>מאמרים</a></li><li><a>צור קשר</a></li><li><a>English</a></li></ul>
<div class="mfoot"><a class="ph2">{ic("i-phone")}077-7741818</a>{CONTACT}</div></nav>''')

for k, (css, body) in V.items():
    for state in ('closed', 'open'):
        o = state == 'open'
        html = (f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<meta name="robots" content="noindex"><title>{k}</title><style>{BASE}{css}</style></head><body class="{"open" if o else ""}">{body(o)}{HERO}</body></html>')
        open(os.path.join(OUT, f'{k}-{state}.html'), 'w', encoding='utf8').write(html)
print('ok')
