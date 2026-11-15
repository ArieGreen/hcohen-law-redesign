"""Three directions for the home page practice-areas section (same copy). Writes mockups/areas/p1..p3.html."""
import os
import sys

OUT = os.path.join(sys.argv[1], 'mockups', 'areas')
os.makedirs(OUT, exist_ok=True)
A = '../../assets'
H2, NOTARY, MORE = 'תחומי התמחות', 'המשרד מעניק גם שירותים נוטריוניים.', 'קרא עוד'
AREAS = [('שירותי דת וקבורה', 'מועצות דתיות, חברות קדישא, בתי עלמין, מקוואות ורבני ערים.', 'rs-advisory', 'i-clipboard'),
         ('דיני עבודה במגזר הציבורי', 'ייצוג המעסיק: שימועים, סיום העסקה, תקינה ובתי הדין לעבודה.', 'labor-hearing', 'i-users'),
         ('משפט מנהלי', 'עתירות, השגות ועררים, החלטות גופים ציבוריים וניגוד עניינים.', 'administrative', 'i-landmark'),
         ('מכרזים והתקשרויות', 'מקוואות, בתי עלמין, אחזקה, ועדות מכרזים ופטורים ממכרז.', 'tenders', 'i-stamp'),
         ('רגולציה וכשרות', 'חוק איסור הונאה בכשרות, אגרות, משגיחים ואכיפה.', 'kashrut', 'i-badge'),
         ('אכיפת חיובים עבור רשויות ותאגידי מים', 'ארנונה, מים וביוב, הוצאה לפועל, כינוס נכסים וחדלות פירעון.', 'collection', 'i-coins')]


def ic(n, c='icon'):
    return f'<svg class="{c}"><use href="{A}/img/icons.svg#{n}"/></svg>'


def img(k):
    return f'{A}/img/stock/{k}-800.webp'


BASE = f'''@font-face{{font-family:Heebo;font-weight:100 900;src:url({A}/fonts/heebo-hebrew.woff2) format('woff2');unicode-range:U+0590-05FF,U+200C-2010}}
@font-face{{font-family:Heebo;font-weight:100 900;src:url({A}/fonts/heebo-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+2000-206F}}
:root{{--navy:#12294A;--navy2:#0B1C35;--ink:#0F1B2D;--ink2:#4A5568;--mist:#F3F5F8;--accent:#1F5FAD;--sky:#8DB4E2;--line:#E1E5EB}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Heebo,Arial;color:var(--ink);background:#fff}}
img{{display:block;max-width:100%}}a{{color:inherit;text-decoration:none}}ul{{list-style:none;margin:0;padding:0}}h2,h3,p{{margin:0}}
.icon{{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;flex:none}}
.wrap{{width:min(100% - 40px,1240px);margin:0 auto}}@media(min-width:900px){{.wrap{{width:min(100% - 112px,1240px)}}}}
h2{{font-weight:800;letter-spacing:-.01em;font-size:clamp(2.1rem,4vw,3.4rem)}}
.more{{display:inline-flex;align-items:center;gap:8px;font-weight:700;font-size:.95rem}}
'''
V = {}

# p1: index with a large photo that follows the active row (desktop); rows with a thumbnail on phones
V['p1'] = ('''
.sec{background:var(--mist);padding:110px 0}
.head{display:flex;justify-content:space-between;align-items:end;gap:20px;margin-bottom:44px}.head p{color:var(--ink2);margin:0}
.grid{display:grid;grid-template-columns:7fr 5fr;gap:56px;align-items:start}
.rows li a{display:grid;grid-template-columns:1fr auto;gap:6px 24px;align-items:center;padding:24px 4px;border-bottom:1px solid #D5DBE4}
.rows li:first-child a{border-top:1px solid #D5DBE4}
.rows h3{font-size:1.65rem;font-weight:800;color:var(--navy)}.rows p{grid-column:1;color:var(--ink2);font-size:1rem}
.rows .arr{grid-column:2;grid-row:1/span 2;width:48px;height:48px;border-radius:50%;display:grid;place-items:center;border:1px solid #C9D2DE;color:var(--navy)}
.rows li.on a{background:#fff;padding-inline:24px;border-radius:10px;border-color:transparent;box-shadow:0 18px 40px -24px rgba(15,27,45,.4)}
.rows li.on h3{color:var(--accent)}.rows li.on .arr{background:var(--navy);color:#fff;border-color:var(--navy)}
.rows .th{display:none}
.pic{position:sticky;top:40px;border-radius:12px;overflow:hidden;aspect-ratio:4/5;box-shadow:0 30px 60px -30px rgba(15,27,45,.5)}
.pic img{width:100%;height:100%;object-fit:cover}
.pic .cap{position:absolute;inset-inline:0;bottom:0;padding:22px 26px;background:linear-gradient(transparent,rgba(11,28,53,.85));color:#fff;font-weight:800;font-size:1.3rem}
.notary{margin-top:28px;color:var(--ink2)}
@media(max-width:899px){.sec{padding:64px 0}.head{flex-direction:column;align-items:flex-start;margin-bottom:24px}.grid{grid-template-columns:1fr;gap:0}.pic{display:none}
.rows li a{grid-template-columns:72px 1fr;padding:16px 0;gap:4px 14px}.rows .th{display:block;grid-row:1/span 2;width:72px;height:72px;border-radius:10px;object-fit:cover}
.rows h3{font-size:1.15rem}.rows p{grid-column:2;font-size:.9rem}.rows .arr{display:none}.rows li.on a{padding-inline:0;background:none;box-shadow:none}.rows li.on h3{color:var(--navy)}}
''', lambda: f'''<section class="sec"><div class="wrap"><div class="head"><h2>{H2}</h2><p>{NOTARY}</p></div><div class="grid"><ul class="rows">
{"".join(f'<li class="{"on" if i==0 else ""}"><a><img class="th" src="{img(k)}"><h3>{t}</h3><p>{d}</p><span class="arr">{ic("i-arrow")}</span></a></li>' for i,(t,d,k,_) in enumerate(AREAS))}
</ul><div class="pic"><img src="{img(AREAS[0][2])}"><span class="cap">{AREAS[0][0]}</span></div></div></div></section>''')

# p2: asymmetric bento on white: the core area (religious services) as a big photo tile, the rest as icon tiles; phone: big tile + 2-col tiles
V['p2'] = ('''
.sec{background:#fff;padding:110px 0}
.head{margin-bottom:40px}.head h2{color:var(--navy)}
.bento{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:minmax(210px,auto);gap:16px}
.t{position:relative;border-radius:14px;overflow:hidden;padding:26px;display:flex;flex-direction:column;background:var(--mist)}
.t .icon{width:34px;height:34px;color:var(--accent);margin-bottom:auto}
.t h3{font-size:1.25rem;font-weight:800;color:var(--navy);margin-top:22px}.t p{color:var(--ink2);font-size:.95rem;margin-top:6px}
.t .more{color:var(--accent);margin-top:14px}
.big{grid-column:span 2;grid-row:span 2;color:#fff;padding:34px;justify-content:flex-end}
.big img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.big::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(11,28,53,.95),rgba(11,28,53,.15) 70%)}
.big>*:not(img){position:relative;z-index:1}.big h3{color:#fff;font-size:2.1rem}.big p{color:#D3DCEA;font-size:1.05rem}.big .more{color:#fff}
.dark{background:var(--navy)}.dark h3{color:#fff}.dark p{color:#C9D5E6}.dark .icon,.dark .more{color:var(--sky)}
.wide{grid-column:span 2}
.notary{grid-column:span 2;background:none;border:1.5px dashed #C9D2DE;justify-content:center;align-items:center;text-align:center;color:var(--ink2);font-weight:600}
@media(max-width:899px){.sec{padding:64px 0}.bento{grid-template-columns:1fr 1fr;grid-auto-rows:auto;gap:12px}
.big{grid-column:span 2;grid-row:auto;min-height:320px;padding:24px}.big h3{font-size:1.6rem}
.t{padding:18px}.t h3{font-size:1.02rem;margin-top:16px}.t p{display:none}.t .more{font-size:.85rem}.wide,.notary{grid-column:span 2}.wide p{display:block}}
''', lambda: f'''<section class="sec"><div class="wrap"><div class="head"><h2>{H2}</h2></div><div class="bento">
<a class="t big"><img src="{img(AREAS[0][2])}">{ic(AREAS[0][3])}<h3>{AREAS[0][0]}</h3><p>{AREAS[0][1]}</p><span class="more">{MORE}{ic("i-arrow")}</span></a>
{"".join(f'<a class="t{" dark" if i in (1,4) else ""}{" wide" if i==5 else ""}">{ic(n)}<h3>{t}</h3><p>{d}</p><span class="more">{MORE}{ic("i-arrow")}</span></a>' for i,(t,d,k,n) in enumerate(AREAS) if i)}
<div class="t notary">{NOTARY}</div></div></div></section>''')

# p3: navy section, cards whose photo is cut on the hero's diagonal with the sky edge, icon on the cut; phone: horizontal swipe row
V['p3'] = ('''
.sec{background:var(--navy);color:#fff;padding:110px 0;overflow:hidden}
.head{display:flex;justify-content:space-between;align-items:end;margin-bottom:44px}.head p{color:var(--sky);font-weight:600}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.c{position:relative;background:#fff;color:var(--ink);border-radius:12px;overflow:hidden;display:flex;flex-direction:column}
.c .ph{position:relative;height:190px}.c .ph img{width:100%;height:100%;object-fit:cover;clip-path:polygon(0 0,100% 0,100% 74%,0 100%)}
.c .ph::after{content:"";position:absolute;inset:0;background:var(--sky);clip-path:polygon(0 100%,100% 74%,100% 76.5%,0 102.5%)}
.c .ib{position:absolute;inset-inline-start:22px;bottom:-6px;width:54px;height:54px;border-radius:50%;background:var(--navy);color:#fff;display:grid;place-items:center;box-shadow:0 10px 20px -8px rgba(0,0,0,.4);z-index:1}
.c .bd{padding:22px 24px 24px;display:flex;flex-direction:column;flex:1}
.c h3{font-size:1.3rem;font-weight:800;color:var(--navy)}.c p{color:var(--ink2);font-size:.95rem;margin-top:8px;flex:1}.c .more{color:var(--accent);margin-top:16px}
@media(max-width:899px){.sec{padding:64px 0}.head{flex-direction:column;align-items:flex-start;gap:8px;margin-bottom:26px}
.cards{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;margin:0 -20px;padding:0 20px 8px;scrollbar-width:none}.c{flex:0 0 82%;scroll-snap-align:start}}
''', lambda: f'''<section class="sec"><div class="wrap"><div class="head"><h2>{H2}</h2><p>{NOTARY}</p></div><div class="cards">
{"".join(f'<a class="c"><div class="ph"><img src="{img(k)}"><span class="ib">{ic(n)}</span></div><div class="bd"><h3>{t}</h3><p>{d}</p><span class="more">{MORE}{ic("i-arrow")}</span></div></a>' for t,d,k,n in AREAS)}
</div></div></section>''')

for k, (css, body) in V.items():
    html = (f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex"><title>{k}</title><style>{BASE}{css}</style></head><body>{body()}</body></html>')
    open(os.path.join(OUT, k + '.html'), 'w', encoding='utf8').write(html)
print('ok')
