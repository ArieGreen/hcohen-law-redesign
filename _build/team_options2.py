"""Desktop team page layouts for the client to choose from: the real page with the people list restyled (site not modified).

Usage: python team_options2.py <out_dir> [key ...]      site served at http://127.0.0.1:8765/
Writes option-1..5.png at 1440px width (1.5x). The list class is renamed in the page so no site rule applies to it.
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

V = {
    # 1: mosaic. Names over the photographs, founder tile double size
    '1': """
.ppl { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 14px; }
.ppl > li { position: relative; display: flex; flex-direction: column; justify-content: flex-end; aspect-ratio: 4 / 5; padding: 0 16px 16px; border-radius: 8px; overflow: hidden; }
.ppl > li:first-child { grid-column: span 2; grid-row: span 2; aspect-ratio: auto; padding: 0 30px 30px; }
.ppl .person-photo { position: absolute; inset: 0; width: auto; height: auto; font-size: 3rem; }
.ppl .person-photo::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11, 28, 53, 0) 50%, rgba(11, 28, 53, .94) 100%); }
.ppl h2, .ppl .role { position: relative; z-index: 1; }
.ppl h2 { color: #fff; font-size: 1.08rem; }
.ppl h2::before { content: ""; display: block; width: 34px; height: 3px; margin-bottom: 10px; background: #8DB4E2; }
.ppl .role { color: #C5D2E4; font-size: .88rem; margin-top: 3px; }
.ppl > li:first-child h2 { font-size: 2.2rem; }
.ppl > li:first-child .role { font-size: 1.05rem; margin-top: 6px; }
""",
    # 2: round portraits on white, founder centred above
    '2': """
.ppl { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 52px 18px; }
.ppl > li { display: flex; flex-direction: column; align-items: center; text-align: center; }
.ppl > li:first-child { grid-column: 1 / -1; }
.ppl .person-photo { width: 158px; height: 158px; border-radius: 50%; font-size: 2.3rem; box-shadow: 0 0 0 5px #fff, 0 0 0 6px #C7D3E3, 0 24px 34px -22px rgba(11, 28, 53, .6); }
.ppl h2 { margin-top: 20px; font-size: 1.08rem; }
.ppl .role { margin-top: 4px; }
.ppl > li:first-child .person-photo { width: 250px; height: 250px; box-shadow: 0 0 0 6px #fff, 0 0 0 8px #8DB4E2, 0 30px 44px -26px rgba(11, 28, 53, .7); }
.ppl > li:first-child h2 { margin-top: 26px; font-size: 2.2rem; }
.ppl > li:first-child .role { font-size: 1.08rem; }
""",
    # 3: one strip of seven tall columns, no gaps
    '3': """
.ppl { display: flex; border-radius: 8px; overflow: hidden; box-shadow: 0 30px 50px -34px rgba(11, 28, 53, .7); }
.ppl > li { flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; background: #0B1C35; border-inline-start: 1px solid rgba(141, 180, 226, .28); }
.ppl > li:first-child { flex-grow: 1.75; border: 0; }
.ppl .person-photo { height: 430px; font-size: 2.3rem; border-bottom: 3px solid #8DB4E2; }
.ppl h2 { color: #fff; font-size: 1rem; padding: 18px 14px 0; }
.ppl .role { color: #AFBCD0; font-size: .85rem; padding: 5px 14px 20px; }
.ppl > li:first-child h2 { font-size: 1.5rem; padding-inline: 22px; }
.ppl > li:first-child .role { font-size: .95rem; padding-inline: 22px; }
""",
    # 4: directory. Horizontal cards in two columns under a founder banner
    '4': """
.ppl { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 22px 26px; }
.ppl > li { display: grid; grid-template-columns: 150px minmax(0, 1fr); grid-template-rows: 1fr 1fr; column-gap: 28px; background: #fff; border: 1px solid #DDE3EC; border-radius: 8px; overflow: hidden; box-shadow: 0 18px 34px -28px rgba(11, 28, 53, .55); }
.ppl .person-photo { grid-row: 1 / span 2; height: 172px; font-size: 2rem; clip-path: polygon(0 0, 100% 0, 100% 100%, 16% 100%); }
.ppl h2 { align-self: end; font-size: 1.35rem; }
.ppl .role { align-self: start; margin-top: 6px; padding-top: 8px; border-top: 2px solid #8DB4E2; justify-self: start; }
.ppl > li:first-child { grid-column: 1 / -1; grid-template-columns: 300px minmax(0, 1fr); column-gap: 48px; background: linear-gradient(120deg, #12294A, #0B1C35); border: 0; }
.ppl > li:first-child .person-photo { height: 320px; clip-path: polygon(0 0, 100% 0, 100% 100%, 12% 100%); }
.ppl > li:first-child h2 { color: #fff; font-size: 2.6rem; }
.ppl > li:first-child .role { color: #C5D2E4; font-size: 1.1rem; margin-top: 12px; padding-top: 14px; border-top: 1px solid rgba(141, 180, 226, .4); }
""",
    # 5: dark gallery. Seven equal framed portraits on navy, four and three
    '5': """
.ppl { display: flex; flex-wrap: wrap; justify-content: center; gap: 52px 44px; padding: 64px 0 72px; background: #0B1C35; box-shadow: 0 0 0 100vmax #0B1C35; clip-path: inset(0 -100vmax); }
.ppl > li { width: calc((100% - 3 * 44px) / 4 - 12px); text-align: center; }
.ppl .person-photo { aspect-ratio: 4 / 5; font-size: 2.8rem; background: #16335C; overflow: visible; position: relative; }
.ppl .person-photo::before { content: ""; position: absolute; inset: 12px -12px -12px 12px; border: 1px solid #8DB4E2; pointer-events: none; }
.ppl .person-photo img, .ppl .person-photo span { position: relative; z-index: 1; }
.ppl h2 { color: #fff; margin-top: 34px; font-size: 1.15rem; }
.ppl .role { color: #AFBCD0; margin-top: 5px; font-size: .92rem; }
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
    f = ImageFont.truetype('arialbd.ttf', 52)
    w = d.textlength(label, font=f)
    d.text((x + r - w / 2, y + r - 31), label, font=f, fill='#ffffff')
    im.save(path)


with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome')
    ctx = b.new_context(viewport={'width': 1440, 'height': 900}, device_scale_factor=1.5, reduced_motion='reduce', bypass_csp=True)
    pg = ctx.new_page()
    for k, css in sorted(V.items()):
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
