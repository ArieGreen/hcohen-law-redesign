"""Second round of desktop team page layouts (bolder): the real page with the people list restyled (site not modified).

Usage: python team_options3.py <out_dir> [key ...]      site served at http://127.0.0.1:8765/
Writes option-6..10.png at 1440px width (1.5x). The list class is renamed in the page so no site rule applies to it.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

out, only = sys.argv[1], sys.argv[2:]
os.makedirs(out, exist_ok=True)

BASE = """
.ppl { list-style: none; margin: 0; padding: 0; }
.ppl .person-photo { width: 100%; height: auto; aspect-ratio: auto; border-radius: 0; border: 0; margin: 0; overflow: hidden; display: grid; place-items: center; background: linear-gradient(160deg, #1D3D6B, #0B1C35); color: #8DB4E2; font-weight: 800; }
.ppl img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 10%; display: block; }
.ppl h2 { margin: 0; font-size: 1.2rem; line-height: 1.2; font-weight: 700; color: #12294A; }
.ppl h2 a { color: inherit; text-decoration: none; }
.ppl .role { color: #4D5B70; font-size: .95rem; }
"""
BLEED = "background: #0B1C35; box-shadow: 0 0 0 100vmax #0B1C35; clip-path: inset(0 -100vmax);"

V = {
    # 6: slanted strip. Seven parallelogram portraits on navy, echoing the site's diagonals
    '6': f"""
.ppl {{ display: flex; gap: 12px; padding: 72px 44px 64px; {BLEED} }}
.ppl > li {{ flex: 1 1 0; min-width: 0; }}
.ppl > li:first-child {{ flex-grow: 1.7; }}
.ppl .person-photo {{ height: 470px; transform: skewX(-8deg); font-size: 2.2rem; border-bottom: 4px solid #8DB4E2; }}
.ppl .person-photo img, .ppl .person-photo span {{ transform: skewX(8deg) scale(1.16); }}
.ppl h2 {{ color: #fff; font-size: 1rem; margin-top: 22px; padding-inline-start: 34px; }}
.ppl .role {{ color: #AFBCD0; font-size: .86rem; margin-top: 4px; padding-inline-start: 34px; }}
.ppl > li:first-child h2 {{ font-size: 1.55rem; }}
.ppl > li:first-child .role {{ font-size: .98rem; }}
""",
    # 7: accordion. Narrow slices with vertical names; the one under the pointer opens wide (founder open by default)
    '7': """
.ppl { display: flex; gap: 8px; height: 580px; }
.ppl > li { position: relative; flex: 0 0 118px; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; }
.ppl > li:first-child { flex: 1 1 auto; padding: 0 40px 40px; }
.ppl .person-photo { position: absolute; inset: 0; width: auto; height: auto; font-size: 1.9rem; align-items: start; }
.ppl .person-photo span { margin-top: 110px; }
.ppl .person-photo::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11, 28, 53, 0) 34%, rgba(11, 28, 53, .96) 100%); }
.ppl > li:first-child .person-photo::after { background: linear-gradient(200deg, rgba(11, 28, 53, 0) 45%, rgba(11, 28, 53, .95) 100%); }
.ppl h2, .ppl .role { position: relative; z-index: 1; color: #fff; }
.ppl > li:nth-child(n+2) h2 { padding: 0 12px 20px; font-size: .95rem; line-height: 1.3; }
.ppl > li:nth-child(n+2) h2::before { content: ""; display: block; width: 26px; height: 3px; margin-bottom: 10px; background: #8DB4E2; }
.ppl > li:nth-child(n+2) .role { display: none; }
.ppl > li:first-child h2 { font-size: 3rem; }
.ppl > li:first-child h2::before { content: ""; display: block; width: 56px; height: 4px; margin-bottom: 16px; background: #8DB4E2; }
.ppl > li:first-child .role { font-size: 1.15rem; color: #C5D2E4; margin-top: 8px; }
""",
    # 8: wall of faces. Edge to edge, no gaps, lawyers in the firm's blue, founder in full colour
    '8': """
.ppl { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); width: 100vw; margin-inline: calc(50% - 50vw); }
.ppl > li { position: relative; height: 400px; display: flex; flex-direction: column; justify-content: flex-end; padding: 0 28px 26px; overflow: hidden; }
.ppl > li:first-child { grid-column: span 2; padding: 0 48px 40px; }
.ppl .person-photo { position: absolute; inset: 0; width: auto; height: auto; font-size: 3.4rem; background: #1B3F73; box-shadow: inset 0 0 0 1px rgba(141, 180, 226, .22); }
.ppl > li:nth-child(n+2) .person-photo img { filter: grayscale(1) contrast(1.12) brightness(1.08); mix-blend-mode: luminosity; }
.ppl > li:first-child { background: linear-gradient(120deg, #12294A, #0B1C35); align-items: flex-end; justify-content: center; padding: 0 56px; }
.ppl > li:first-child .person-photo { inset: 0 0 0 46%; clip-path: polygon(0 0, 100% 0, 100% 100%, 12% 100%); }
.ppl > li:first-child .person-photo::after { display: none; }
.ppl > li:first-child h2::before { content: ""; display: block; width: 56px; height: 4px; margin-bottom: 16px; background: #8DB4E2; }
.ppl > li:first-child .person-photo img { object-position: 50% 12%; }
.ppl .person-photo::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11, 28, 53, 0) 46%, rgba(11, 28, 53, .9) 100%); }
.ppl h2, .ppl .role { position: relative; z-index: 1; color: #fff; }
.ppl h2 { font-size: 1.45rem; font-weight: 800; }
.ppl .role { color: #C5D2E4; margin-top: 4px; }
.ppl > li:first-child h2 { font-size: 2.6rem; }
.ppl > li:first-child .role { font-size: 1.12rem; }
""",
    # 9: stage. Founder in the centre, the lawyers stepping back on both sides
    '9': f"""
.ppl {{ display: flex; justify-content: center; align-items: flex-start; padding: 76px 0 70px; background: radial-gradient(ellipse 60% 70% at 50% 42%, #1F4A86 0%, #0B1C35 72%); box-shadow: 0 0 0 100vmax #0B1C35; clip-path: inset(0 -100vmax); }}
.ppl > li {{ position: relative; flex: 0 0 214px; margin-inline: -16px; text-align: center; transform-origin: 50% 190px; }}
.ppl .person-photo {{ aspect-ratio: 4 / 5; font-size: 2.6rem; border-radius: 6px; box-shadow: 0 30px 50px -20px rgba(0, 0, 0, .75), 0 0 0 1px rgba(141, 180, 226, .35); }}
.ppl h2 {{ color: #fff; margin-top: 20px; font-size: 1.1rem; }}
.ppl .role {{ color: #AFBCD0; margin-top: 4px; font-size: .9rem; }}
.ppl > li:nth-child(1) {{ order: 4; flex-basis: 330px; z-index: 5; margin-top: -26px; }}
.ppl > li:nth-child(1) .person-photo {{ box-shadow: 0 40px 60px -20px rgba(0, 0, 0, .8), 0 0 0 2px #8DB4E2; }}
.ppl > li:nth-child(1) h2 {{ font-size: 1.9rem; margin-top: 26px; }}
.ppl > li:nth-child(1) .role {{ font-size: 1.05rem; }}
.ppl > li:nth-child(2) {{ order: 1; transform: scale(.74); z-index: 1; }}
.ppl > li:nth-child(3) {{ order: 2; transform: scale(.86); z-index: 2; }}
.ppl > li:nth-child(4) {{ order: 3; transform: scale(.97); z-index: 3; }}
.ppl > li:nth-child(5) {{ order: 5; transform: scale(.97); z-index: 3; }}
.ppl > li:nth-child(6) {{ order: 6; transform: scale(.86); z-index: 2; }}
.ppl > li:nth-child(7) {{ order: 7; transform: scale(.74); z-index: 1; }}
.ppl > li:nth-child(2) h2, .ppl > li:nth-child(7) h2 {{ font-size: 1.3rem; }}
.ppl > li:nth-child(3) h2, .ppl > li:nth-child(6) h2 {{ font-size: 1.2rem; }}
""",
    # 10: typographic. Founder portrait full height on one side, big names in ruled rows on the other
    '10': """
.ppl { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr); column-gap: 72px; }
.ppl > li:first-child { grid-column: 1; grid-row: 1 / span 6; position: relative; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; padding: 0 40px 40px; min-height: 690px; }
.ppl > li:first-child .person-photo { position: absolute; inset: 0; width: auto; height: auto; }
.ppl > li:first-child .person-photo::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11, 28, 53, 0) 48%, rgba(11, 28, 53, .95) 100%); }
.ppl > li:first-child h2, .ppl > li:first-child .role { position: relative; z-index: 1; color: #fff; }
.ppl > li:first-child h2 { font-size: 3rem; }
.ppl > li:first-child h2::before { content: ""; display: block; width: 56px; height: 4px; margin-bottom: 16px; background: #8DB4E2; }
.ppl > li:first-child .role { color: #C5D2E4; font-size: 1.12rem; margin-top: 8px; }
.ppl > li:nth-child(n+2) { grid-column: 2; display: grid; grid-template-columns: minmax(0, 1fr) 132px; grid-template-rows: 1fr 1fr; column-gap: 24px; align-items: center; border-bottom: 1px solid #C9D2DE; }
.ppl > li:nth-child(2) { border-top: 3px solid #12294A; }
.ppl > li:nth-child(n+2) .person-photo { grid-column: 2; grid-row: 1 / span 2; height: 98px; font-size: 1.5rem; border-radius: 6px; clip-path: polygon(14% 0, 100% 0, 100% 100%, 0 100%); }
.ppl > li:nth-child(n+2) .person-photo img { object-position: 50% 22%; }
.ppl > li:nth-child(n+2) h2 { grid-column: 1; grid-row: 1; align-self: end; font-size: 2rem; font-weight: 800; letter-spacing: -.01em; }
.ppl > li:nth-child(n+2) .role { grid-column: 1; grid-row: 2; align-self: start; color: #1F5FAD; font-weight: 600; margin-top: 4px; }
""",
}

PREP = """() => {
  const ul = document.querySelector('.people'); ul.className = 'ppl';
  ul.querySelectorAll('img').forEach(i => { i.loading = 'eager'; });
}"""


def badge(path, label):
    im = Image.open(path).convert('RGB')
    d = ImageDraw.Draw(im)
    r = 46
    x, y = 40, im.height - 40 - 2 * r
    d.ellipse((x, y, x + 2 * r, y + 2 * r), fill='#1F5FAD', outline='#ffffff', width=4)
    f = ImageFont.truetype('arialbd.ttf', 52 if len(label) == 1 else 44)
    w = d.textlength(label, font=f)
    d.text((x + r - w / 2, y + r - (31 if len(label) == 1 else 26)), label, font=f, fill='#ffffff')
    im.save(path)


with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome')
    ctx = b.new_context(viewport={'width': 1440, 'height': 900}, device_scale_factor=1.5, reduced_motion='reduce', bypass_csp=True)
    pg = ctx.new_page()
    for k, css in sorted(V.items(), key=lambda kv: int(kv[0])):
        if only and k not in only:
            continue
        pg.goto('http://127.0.0.1:8765/team.html', wait_until='load')
        pg.evaluate(PREP)
        pg.add_style_tag(content=BASE + css)
        pg.evaluate("document.querySelector('.a11y-btn')?.remove()")
        pg.wait_for_timeout(1500)
        if pg.evaluate('document.documentElement.scrollWidth>innerWidth'):
            print('OVERFLOW', k)
        bottom = pg.evaluate("Math.round(document.querySelector('.ppl').getBoundingClientRect().bottom+scrollY)")
        f = os.path.join(out, f'option-{k}.png')
        pg.screenshot(path=f, full_page=True)
        im = Image.open(f)
        im.crop((0, 0, im.width, min(im.height, int((bottom + 70) * 1.5)))).save(f)
        badge(f, k)
        print(k, Image.open(f).size)
    b.close()
