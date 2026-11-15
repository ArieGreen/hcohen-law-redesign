"""Five desktop hero directions for the home page (same copy as the live site). Writes mockups/hero/h1..h5.html."""
import os
import sys

OUT = os.path.join(sys.argv[1], 'mockups', 'hero')
os.makedirs(OUT, exist_ok=True)
A = '../../assets'
NAME, TAG = 'ח. כהן - משרד עורכי דין', 'ייעוץ וייצוג לרשויות מקומיות, תאגידי מים, מועצות דתיות, חברות קדישא ומוסדות חינוך'
AREAS = [('שירותי דת וקבורה', 'rs-advisory', 'i-clipboard'), ('דיני עבודה במגזר הציבורי', 'labor-hearing', 'i-users'),
         ('משפט מנהלי', 'administrative', 'i-landmark'), ('מכרזים והתקשרויות', 'tenders', 'i-stamp'),
         ('רגולציה וכשרות', 'kashrut', 'i-badge'), ('אכיפת חיובים עבור רשויות ותאגידי מים', 'collection', 'i-coins')]


def ic(n):
    return f'<svg class="icon"><use href="{A}/img/icons.svg#{n}"/></svg>'


BTNS = '<div class="acts"><a class="b solid">תחומי ההתמחות</a><a class="b">מאמרים</a><a class="b">צור קשר</a></div>'
SINCE = '<p class="since"><small>מאז</small><b>2001</b></p>'
HEADER = f'''<header class="hdr"><a class="brand"><img src="{A}/img/logo-mark.webp" alt=""><span><b>ח. כהן</b><small>משרד עורכי דין ונוטריון</small></span></a>
<nav><a>אודות</a><a>תחומי התמחות</a><a>הצוות</a><a>מאמרים</a><a>צור קשר</a><a>English</a></nav><a class="call">{ic("i-phone")}077-7741818</a></header>'''

BASE = f'''@font-face{{font-family:Heebo;font-weight:100 900;src:url({A}/fonts/heebo-hebrew.woff2) format('woff2');unicode-range:U+0590-05FF,U+200C-2010}}
@font-face{{font-family:Heebo;font-weight:100 900;src:url({A}/fonts/heebo-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+2000-206F}}
:root{{--navy:#12294A;--navy2:#0B1C35;--ink:#0F1B2D;--ink2:#4A5568;--mist:#F3F5F8;--accent:#1F5FAD;--sky:#8DB4E2;--line:#E1E5EB}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Heebo,Arial;color:var(--ink);background:#fff;overflow:hidden}}
img{{display:block;max-width:100%}}a{{color:inherit;text-decoration:none;cursor:pointer}}
.icon{{width:1.2em;height:1.2em;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}}
.hdr{{height:84px;display:flex;align-items:center;gap:30px;padding:0 100px;border-bottom:1px solid var(--line);background:#fff;position:relative;z-index:5}}
.brand{{display:flex;gap:12px;align-items:center;margin-inline-end:auto}}.brand img{{width:44px}}.brand span{{display:flex;flex-direction:column;line-height:1.15}}
.brand b{{font-size:1.3rem;font-weight:800}}.brand small{{font-size:.78rem;color:var(--ink2)}}
.hdr nav{{display:flex;gap:26px;font-weight:500}}.call{{display:flex;gap:8px;align-items:center;background:var(--navy);color:#fff;padding:12px 18px;border-radius:6px;font-weight:700}}
h1{{margin:0;font-weight:800;letter-spacing:-.015em;line-height:1.02}}
.tag{{font-size:1.3rem;line-height:1.55;max-width:36ch;margin:22px 0 0}}
.acts{{display:flex;gap:12px;margin-top:36px}}.b{{display:inline-flex;align-items:center;min-height:54px;padding:0 26px;border-radius:6px;border:1.5px solid currentColor;font-weight:600}}
.since{{margin:0;display:flex;flex-direction:column;align-items:center;line-height:1;padding:16px 24px;border-radius:6px;background:#fff;color:var(--navy);box-shadow:0 20px 40px -18px rgba(0,0,0,.35)}}
.since small{{font-size:.9rem;color:var(--ink2);margin-bottom:6px}}.since b{{font-size:2.4rem;font-weight:800}}
.hero{{height:816px;position:relative;overflow:hidden}}
'''

V = {}

# 1. Editorial split on white: giant navy title, photo in a tall frame that bleeds off the edge, area list as an index
V['h1'] = ('עריכתי לבן', '''
.hero{display:grid;grid-template-columns:52% 48%;background:#fff}
.txt{padding:96px 100px 0 40px;display:flex;flex-direction:column}
.txt h1{font-size:5.6rem;color:var(--navy)}.tag{color:var(--ink2)}
.acts .b{color:var(--navy)}.acts .solid{background:var(--navy);color:#fff;border-color:var(--navy)}
.idx{margin-top:auto;margin-bottom:56px;border-top:1px solid var(--line);display:grid;grid-template-columns:1fr 1fr;gap:0 32px}
.idx a{display:flex;align-items:center;gap:12px;padding:14px 0;border-bottom:1px solid var(--line);font-weight:600;color:var(--navy)}.idx .icon{color:var(--accent)}
.pic{position:relative;margin:48px 0 48px 0}.pic img{width:100%;height:100%;object-fit:cover;object-position:62% 20%;border-radius:0 10px 10px 0}
.pic .since{position:absolute;inset-inline-start:-40px;bottom:60px}
''', lambda: f'''<section class="hero"><div class="txt"><h1>{NAME}</h1><p class="tag">{TAG}</p>{BTNS}
<nav class="idx">{"".join(f"<a>{ic(i)}{t}</a>" for t,_,i in AREAS)}</nav></div>
<div class="pic"><img src="{A}/img/bsr-day-1920.webp">{SINCE}</div></section>''')

# 2. Diagonal: navy text panel cut at an angle over a full photo, sky-blue rule, stat column
V['h2'] = ('אלכסון', '''
.hero{background:var(--navy2)}
.photo{position:absolute;inset:0}.photo img{width:100%;height:100%;object-fit:cover;object-position:62% 18%}
.panel{position:absolute;inset:0;background:var(--navy);clip-path:polygon(38% 0,100% 0,100% 100%,52% 100%);}
.panel::before{content:"";position:absolute;inset:0;background:linear-gradient(135deg,rgba(31,95,173,.35),rgba(11,28,53,0) 60%)}
.edge{position:absolute;inset:0;background:var(--sky);clip-path:polygon(37.4% 0,38% 0,52% 100%,51.4% 100%)}
.txt{position:absolute;inset-inline-start:100px;top:150px;width:560px;color:#fff}
.txt h1{font-size:5.4rem}.tag{color:#C9D5E6}.acts .b{color:#fff;border-color:rgba(255,255,255,.5)}.acts .solid{background:#fff;color:var(--navy);border-color:#fff}
.since{position:absolute;inset-inline-end:100px;top:70px}
.strip{position:absolute;inset-inline-start:100px;bottom:56px;display:flex;gap:10px;flex-wrap:wrap;width:620px}
.strip a{display:flex;gap:8px;align-items:center;padding:10px 16px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:500;font-size:.95rem}.strip .icon{color:var(--sky)}
''', lambda: f'''<section class="hero"><div class="photo"><img src="{A}/img/bsr-day-1920.webp"></div><div class="panel"></div><div class="edge"></div>{SINCE}
<div class="txt"><h1>{NAME}</h1><p class="tag">{TAG}</p>{BTNS}</div>
<nav class="strip">{"".join(f"<a>{ic(i)}{t}</a>" for t,_,i in AREAS)}</nav></section>''')

# 3. Typographic: huge title across the full width on mist, a wide photo band under it, buttons on the band
V['h3'] = ('טיפוגרפי', '''
.hero{background:var(--mist);padding:70px 100px 0}
.hero h1{font-size:7.4rem;color:var(--navy);white-space:nowrap}
.row{display:flex;justify-content:space-between;align-items:end;margin-top:24px}
.row .tag{margin:0;color:var(--ink2);font-size:1.35rem}.acts{margin:0}.acts .b{color:var(--navy)}.acts .solid{background:var(--navy);color:#fff;border-color:var(--navy)}
.band{position:relative;margin:48px -100px 0;height:430px}.band img{width:100%;height:100%;object-fit:cover;object-position:50% 22%}
.band .since{position:absolute;inset-inline-start:100px;top:28px}
.band .chips{position:absolute;inset-inline:100px;bottom:28px;display:grid;grid-template-columns:repeat(6,1fr);gap:10px}
.chips a{background:rgba(255,255,255,.94);border-radius:6px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;font-weight:600;font-size:.9rem;color:var(--navy);box-shadow:0 12px 30px -16px rgba(0,0,0,.4)}.chips .icon{color:var(--accent)}
''', lambda: f'''<section class="hero"><h1>{NAME}</h1><div class="row"><p class="tag">{TAG}</p>{BTNS}</div>
<div class="band"><img src="{A}/img/bsr-day-1920.webp">{SINCE}<nav class="chips">{"".join(f"<a>{ic(i)}{t}</a>" for t,_,i in AREAS)}</nav></div></section>''')

# 4. Mosaic: text on navy, the six practice areas as a photo mosaic on the other side (the work itself is the image)
V['h4'] = ('פסיפס תחומים', '''
.hero{display:grid;grid-template-columns:44% 56%;background:var(--navy)}
.txt{padding:130px 100px 0 56px;color:#fff}.txt h1{font-size:5rem}.tag{color:#C9D5E6}
.acts .b{color:#fff;border-color:rgba(255,255,255,.5)}.acts .solid{background:#fff;color:var(--navy);border-color:#fff}
.txt .since{display:inline-flex;margin-top:56px;background:rgba(255,255,255,.08);color:#fff;box-shadow:none;border:1px solid rgba(255,255,255,.2)}.txt .since small{color:var(--sky)}
.mos{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr);gap:6px;padding:6px 6px 6px 0}
.mos a{position:relative;overflow:hidden;border-radius:4px}.mos img{width:100%;height:100%;object-fit:cover;filter:saturate(.85)}
.mos a::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(11,28,53,.9),rgba(11,28,53,.05) 60%)}
.mos span{position:absolute;z-index:1;inset-inline:18px;bottom:18px;color:#fff;font-weight:700;font-size:1.1rem;line-height:1.3;display:flex;gap:10px;align-items:flex-end}.mos .icon{color:var(--sky);flex:none}
.mos a:first-child{grid-row:span 2}
''', lambda: f'''<section class="hero"><div class="txt"><h1>{NAME}</h1><p class="tag">{TAG}</p>{BTNS}{SINCE}</div>
<div class="mos">{"".join(f'<a><img src="{A}/img/stock/{img}-800.webp"><span>{ic(i)}{t}</span></a>' for t,img,i in AREAS[:5])}</div></section>''')

# 5. Layered collage on light: big towers photo + founder portrait overlapping it, text and buttons on the other side
V['h5'] = ('קולאז׳ שכבות', '''
.hero{background:linear-gradient(90deg,#fff 0 58%,var(--mist) 58%)}
.txt{position:absolute;inset-inline-start:100px;top:150px;width:520px}.txt h1{font-size:5.2rem;color:var(--navy)}.tag{color:var(--ink2)}
.acts .b{color:var(--navy)}.acts .solid{background:var(--navy);color:#fff;border-color:var(--navy)}
.big{position:absolute;inset-inline-end:100px;top:70px;width:600px;height:560px;border-radius:10px;overflow:hidden;box-shadow:0 40px 80px -40px rgba(11,28,53,.55)}
.big img{width:100%;height:100%;object-fit:cover;object-position:60% 18%}
.por{position:absolute;inset-inline-end:560px;top:400px;width:250px;height:310px;border-radius:10px;overflow:hidden;border:8px solid #fff;box-shadow:0 30px 60px -30px rgba(11,28,53,.6)}
.por img{width:100%;height:100%;object-fit:cover;object-position:50% 15%}
.hero .since{position:absolute;inset-inline-end:130px;top:580px;background:var(--navy);color:#fff}.hero .since small{color:var(--sky)}
.dots{position:absolute;inset-inline-end:60px;top:40px;width:160px;height:160px;background-image:radial-gradient(var(--accent) 1.6px,transparent 1.6px);background-size:16px 16px;opacity:.35}
.line{position:absolute;inset-inline-start:100px;bottom:70px;display:flex;gap:28px;color:var(--navy);font-weight:600}.line a{display:flex;gap:8px;align-items:center}.line .icon{color:var(--accent)}
''', lambda: f'''<section class="hero"><div class="dots"></div><div class="big"><img src="{A}/img/bsr-day-1920.webp"></div>
<div class="por"><img src="{A}/img/hagai-cohen-720.webp"></div>{SINCE}
<div class="txt"><h1>{NAME}</h1><p class="tag">{TAG}</p>{BTNS}</div>
<nav class="line">{"".join(f"<a>{ic(i)}{t}</a>" for t,_,i in AREAS[:4])}</nav></section>''')

for key, (title, css, body) in V.items():
    html = (f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="robots" content="noindex"><title>{title}</title>'
            f'<style>{BASE}{css}</style></head><body>{HEADER}{body()}</body></html>')
    open(os.path.join(OUT, key + '.html'), 'w', encoding='utf8').write(html)
print('written', list(V))
