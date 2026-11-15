"""Five mobile hero directions (390px). Same copy as the live site. Writes mockups/hero/m1..m5.html."""
import os
import sys

OUT = os.path.join(sys.argv[1], 'mockups', 'hero')
os.makedirs(OUT, exist_ok=True)
A = '../../assets'
NM, PR = 'ח. כהן', 'משרד עורכי דין'
TAG = 'ייעוץ וייצוג לרשויות מקומיות, תאגידי מים, מועצות דתיות, חברות קדישא ומוסדות חינוך'
AREAS = [('שירותי דת וקבורה', 'i-clipboard'), ('דיני עבודה במגזר הציבורי', 'i-users'), ('משפט מנהלי', 'i-landmark'),
         ('מכרזים והתקשרויות', 'i-stamp'), ('רגולציה וכשרות', 'i-badge'), ('אכיפת חיובים עבור רשויות ותאגידי מים', 'i-coins')]
PHOTO = f'{A}/img/bsr-day-1000.webp'
MARK = f'<img class="mk" src="{A}/img/logo-mark.webp" alt="">'


def ic(n):
    return f'<svg class="icon"><use href="{A}/img/icons.svg#{n}"/></svg>'


H1 = f'<h1><span class="nm">{NM}</span><span class="dash"> - </span><span class="pr">{PR}</span></h1>'
BTN = '<div class="acts"><a class="b solid">תחומי ההתמחות</a><a class="b">מאמרים</a><a class="b">צור קשר</a></div>'
HEADER = f'''<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp" alt=""><b>ח. כהן</b></a>
<a class="ib dark">{ic("i-phone")}</a><a class="ib">{ic("i-menu")}</a></header>'''
BAR = f'<div class="mbar"><a>{ic("i-phone")}077-7741818</a><a class="d">{ic("i-chat")}צור קשר</a></div>'

BASE = f'''@font-face{{font-family:Heebo;font-weight:100 900;src:url({A}/fonts/heebo-hebrew.woff2) format('woff2');unicode-range:U+0590-05FF,U+200C-2010}}
@font-face{{font-family:Heebo;font-weight:100 900;src:url({A}/fonts/heebo-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+2000-206F}}
:root{{--navy:#12294A;--navy2:#0B1C35;--ink:#0F1B2D;--ink2:#4A5568;--mist:#F3F5F8;--accent:#1F5FAD;--sky:#8DB4E2;--line:#E1E5EB}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Heebo,Arial;color:var(--ink);background:var(--mist);overflow:hidden;height:844px}}
img{{display:block;max-width:100%}}a{{color:inherit;text-decoration:none}}
.icon{{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;flex:none}}
.hdr{{height:72px;display:flex;align-items:center;gap:10px;padding:0 20px;background:#fff;border-bottom:1px solid var(--line);position:relative;z-index:5}}
.brand{{display:flex;align-items:center;gap:8px;margin-inline-end:auto;font-size:1.3rem;font-weight:800}}.brand img{{width:38px}}
.ib{{width:44px;height:44px;border-radius:6px;border:1px solid var(--line);display:grid;place-items:center}}.ib.dark{{background:var(--navy);color:#fff;border:0}}
h1{{margin:0;font-weight:800;letter-spacing:-.01em}}.dash{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}
.nm,.pr{{display:block}}
.tag{{margin:0;line-height:1.6}}
.acts{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}.b{{display:flex;align-items:center;justify-content:center;min-height:50px;border-radius:6px;border:1.5px solid currentColor;font-weight:600}}
.b.solid{{grid-column:1/-1}}
.mbar{{position:fixed;inset-inline:0;bottom:0;height:54px;display:grid;grid-template-columns:1fr 1fr;background:#fff;border-top:1px solid var(--line);z-index:9}}
.mbar a{{display:flex;align-items:center;justify-content:center;gap:8px;font-weight:600;color:var(--navy)}}.mbar .d{{background:var(--navy);color:#fff}}
'''

V = {}

# m1: navy full screen. photo cut diagonally at the top (echo of desktop), mark + name row, year as a quiet line beside the profession
V['m1'] = ('''
.hero{position:relative;height:718px;background:var(--navy);color:#fff;overflow:hidden}
.ph{height:250px;clip-path:polygon(0 0,100% 0,100% 72%,0 100%)}.ph img{width:100%;height:100%;object-fit:cover;object-position:35% 20%}
.edge{position:absolute;inset-inline:0;top:0;height:250px;background:var(--sky);clip-path:polygon(0 100%,100% 72%,100% 73.2%,0 101.2%)}
.c{padding:8px 22px 0}
.row{display:flex;align-items:center;gap:16px}.mk{width:78px}
.nm{font-size:3rem;line-height:1}.pr{font-size:1.35rem;font-weight:300;color:var(--sky);margin-top:4px}
.yr{display:flex;align-items:center;gap:10px;margin:18px 0 0;color:var(--sky);font-size:.95rem;font-weight:500}.yr::before{content:"";width:28px;height:2px;background:var(--sky)}
.tag{margin-top:14px;color:#D3DCEA;font-size:1.02rem}
.acts{margin-top:22px}.b{color:#fff;border-color:rgba(255,255,255,.45)}.b.solid{background:#fff;color:var(--navy);border-color:#fff}
''', lambda: f'''<section class="hero"><div class="ph"><img src="{PHOTO}"></div><div class="edge"></div><div class="c">
<div class="row">{MARK}{H1}</div><p class="yr">מאז 2001</p><p class="tag">{TAG}</p>{BTN}</div></section>''')

# m2: photo on top full width, white sheet rising with rounded top; year as a big faint number in the sheet corner behind the mark
V['m2'] = ('''
.hero{position:relative;height:718px}
.ph{height:300px}.ph img{width:100%;height:100%;object-fit:cover;object-position:35% 20%}
.sheet{position:absolute;inset-inline:0;top:262px;bottom:0;background:#fff;border-radius:22px 22px 0 0;padding:28px 22px 0;box-shadow:0 -10px 30px -12px rgba(0,0,0,.25);overflow:hidden}
.big{position:absolute;inset-inline-end:-6px;top:6px;font-size:6.4rem;font-weight:900;color:var(--mist);line-height:1;letter-spacing:-.03em;z-index:0}
.sheet>*{position:relative;z-index:1}
.row{display:flex;align-items:center;gap:14px}.mk{width:64px}
.nm{font-size:2.7rem;line-height:1;color:var(--navy)}.pr{font-size:1.25rem;font-weight:400;color:var(--accent);margin-top:4px}
.since{margin:6px 0 0;font-size:.85rem;color:var(--ink2);font-weight:500}
.tag{margin-top:16px;color:var(--ink2);font-size:1rem}
.acts{margin-top:22px;color:var(--navy)}.b.solid{background:var(--navy);color:#fff;border-color:var(--navy)}
''', lambda: f'''<section class="hero"><div class="ph"><img src="{PHOTO}"></div><div class="sheet"><span class="big" aria-hidden="true">2001</span>
<div class="row">{MARK}<div>{H1}<p class="since">מאז 2001</p></div></div><p class="tag">{TAG}</p>{BTN}</div></section>''')

# m3: full-screen photo with dark gradient, everything over it; year sits in the header strip of the text block as "since" ribbon line
V['m3'] = ('''
.hero{position:relative;height:718px;color:#fff;overflow:hidden}
.ph{position:absolute;inset:0}.ph img{width:100%;height:100%;object-fit:cover;object-position:38% 20%}
.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(11,28,53,.98) 0%,rgba(11,28,53,.9) 46%,rgba(11,28,53,.2) 78%,rgba(11,28,53,.1))}
.c{position:absolute;inset-inline:22px;bottom:30px}
.top{display:flex;align-items:center;justify-content:space-between;padding-bottom:14px;margin-bottom:18px;border-bottom:1px solid rgba(255,255,255,.25)}
.mk{width:60px}.yr{margin:0;text-align:center;line-height:1}.yr small{display:block;font-size:.8rem;color:var(--sky);margin-bottom:4px}.yr b{font-size:1.6rem;font-weight:800}
.nm{font-size:3.1rem;line-height:1}.pr{font-size:1.4rem;font-weight:300;color:var(--sky);margin-top:4px}
.tag{margin-top:14px;color:#D3DCEA;font-size:1rem}
.acts{margin-top:22px}.b{color:#fff;border-color:rgba(255,255,255,.5)}.b.solid{background:#fff;color:var(--navy);border-color:#fff}
''', lambda: f'''<section class="hero"><div class="ph"><img src="{PHOTO}"></div><div class="c">
<div class="top">{MARK}<p class="yr"><small>מאז</small><b>2001</b></p></div>{H1}<p class="tag">{TAG}</p>{BTN}</div></section>''')

# m4: light. name first (big, navy), photo as a rounded card under it with the year as a caption chip at the photo's foot, buttons last
V['m4'] = ('''
.hero{height:718px;background:#fff;padding:26px 22px 0}
.row{display:flex;align-items:center;gap:14px}.mk{width:62px}
.nm{font-size:2.9rem;line-height:1;color:var(--navy)}.pr{font-size:1.3rem;font-weight:300;color:var(--accent);margin-top:4px}
.tag{margin-top:14px;color:var(--ink2);font-size:1rem}
.ph{position:relative;margin-top:18px;height:200px;border-radius:12px;overflow:hidden}.ph img{width:100%;height:100%;object-fit:cover;object-position:35% 20%}
.cap{position:absolute;inset-inline-start:12px;bottom:12px;margin:0;display:flex;align-items:center;gap:8px;padding:8px 14px;border-radius:999px;background:rgba(255,255,255,.94);color:var(--navy);font-weight:700;font-size:.9rem}
.cap::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--accent)}
.acts{margin-top:18px;color:var(--navy)}.b.solid{background:var(--navy);color:#fff;border-color:var(--navy)}
''', lambda: f'''<section class="hero"><div class="row">{MARK}{H1}</div><p class="tag">{TAG}</p>
<div class="ph"><img src="{PHOTO}"><p class="cap">מאז 2001</p></div>{BTN}</section>''')

# m5: split card: navy top half with mark centred + name, white lower half with tagline and buttons; year centred between two rules under the name
V['m5'] = ('''
.hero{position:relative;height:718px}
.ph{height:190px}.ph img{width:100%;height:100%;object-fit:cover;object-position:35% 20%}
.card{position:absolute;inset-inline:16px;top:150px;border-radius:12px;overflow:hidden;box-shadow:0 24px 50px -24px rgba(11,28,53,.55);background:#fff}
.top{background:var(--navy);color:#fff;text-align:center;padding:24px 20px 20px}
.mk{width:66px;margin:0 auto 10px}.nm{font-size:2.8rem;line-height:1}.pr{font-size:1.3rem;font-weight:300;color:var(--sky);margin-top:4px}
.yr{display:flex;align-items:center;justify-content:center;gap:12px;margin:14px 0 0;color:var(--sky);font-size:.9rem;font-weight:600}
.yr::before,.yr::after{content:"";width:34px;height:1px;background:rgba(141,180,226,.6)}
.bot{padding:18px 20px 20px}.tag{color:var(--ink2);font-size:1rem;text-align:center}
.acts{margin-top:18px;color:var(--navy)}.b.solid{background:var(--navy);color:#fff;border-color:var(--navy)}
''', lambda: f'''<section class="hero"><div class="ph"><img src="{PHOTO}"></div><div class="card"><div class="top">{MARK}{H1}<p class="yr">מאז 2001</p></div>
<div class="bot"><p class="tag">{TAG}</p>{BTN}</div></div></section>''')

for k, (css, body) in V.items():
    html = (f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex"><title>{k}</title><style>{BASE}{css}</style></head><body>{HEADER}{body()}{BAR}</body></html>')
    open(os.path.join(OUT, k + '.html'), 'w', encoding='utf8').write(html)
print('ok')
