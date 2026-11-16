"""Team page layout sketches: the real team page with a CSS variant injected (the site itself is not modified).

Usage: python team_options.py <site_dir> <out_dir>      site served at http://127.0.0.1:8765/
Writes t1..t5-desktop.png (1440) and t1..t5-phone.png (390). Lawyers without a photo keep their initials.
"""
import os
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

site, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
P = 'html body.page-team .people'
LI = P + ' > li:nth-child(n)'
ONE = P + ' > li:first-child'

# shared reset: every person is a card with a 4:5 portrait on top
BASE = f"""
{P} {{ display: grid; gap: 28px; grid-auto-rows: auto; grid-template-columns: repeat(3, 1fr); }}
{LI} {{ grid-column: auto; grid-row: auto; display: flex; flex-direction: column; align-items: stretch; gap: 0; padding: 0; margin: 0;
  background: #fff; color: #12294A; border: 1px solid #DDE3EC; border-radius: 8px; overflow: hidden; text-align: start; min-height: 0; box-shadow: 0 18px 34px -28px rgba(11, 28, 53, .55); }}
{LI} .person-photo {{ grid-row: auto; grid-column: auto; width: 100%; height: auto; min-height: 0; aspect-ratio: 4 / 5; border-radius: 0; border: 0; margin: 0;
  clip-path: none; background: linear-gradient(160deg, #1D3D6B, #0B1C35); color: #8DB4E2; font-size: 3.2rem; font-weight: 800; display: grid; place-items: center; align-self: auto; }}
{LI} .person-photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 10%; }}
{LI} h2 {{ grid-column: auto; align-self: auto; margin: 0; padding: 18px 20px 0; border: 0; font-size: 1.22rem; line-height: 1.2; color: #12294A; }}
{LI} h2 a {{ color: inherit; }}
{LI} .role {{ grid-column: auto; align-self: auto; margin: 0; padding: 4px 20px 20px; border: 0; color: #4D5B70; font-size: .95rem; }}
@media (max-width: 699px) {{
  {P} {{ grid-template-columns: repeat(2, 1fr); gap: 14px; }}
  {ONE} {{ grid-column: 1 / -1; }}
  {LI} h2 {{ font-size: 1.05rem; padding: 12px 14px 0; }}
  {LI} .role {{ padding: 2px 14px 14px; font-size: .88rem; }}
  {LI} .person-photo {{ font-size: 2.2rem; }}
  {ONE} .person-photo {{ aspect-ratio: 4 / 3; }}
}}
"""

FOUNDER_BANNER = f"""
@media (min-width: 700px) {{
  {ONE} {{ grid-column: 1 / -1; display: grid; grid-template-columns: 300px 1fr; grid-template-rows: 1fr 1fr; gap: 0 48px; background: linear-gradient(120deg, #12294A, #0B1C35); border: 0; }}
  {ONE} .person-photo {{ grid-row: 1 / span 2; aspect-ratio: auto; height: 340px; clip-path: polygon(0 0, 100% 0, 100% 100%, 14% 100%); }}
  {ONE} h2 {{ align-self: end; padding: 0; font-size: 2.7rem; color: #fff; }}
  {ONE} .role {{ align-self: start; padding: 14px 0 0; margin-top: 12px; border-top: 1px solid rgba(141, 180, 226, .35); justify-self: start; color: #C5D2E4; font-size: 1.1rem; }}
}}
"""

V = {
    # 1: founder banner, then one row of five portrait cards
    't1': BASE + FOUNDER_BANNER + f"""
@media (min-width: 700px) {{ {P} {{ grid-template-columns: repeat(5, 1fr); gap: 24px; }} }}
{P} > li:nth-child(n+2) .person-photo {{ border-bottom: 3px solid #8DB4E2; }}
""",
    # 2: six equal cards, three in a row; the founder is first and navy
    't2': BASE + f"""
@media (min-width: 700px) {{ {P} {{ max-width: 1040px; margin-inline: auto; gap: 32px; }} }}
{LI} .person-photo {{ clip-path: polygon(0 0, 100% 0, 100% 92%, 0 100%); }}
{ONE} {{ background: linear-gradient(160deg, #12294A, #0B1C35); border-color: #0B1C35; }}
{ONE} h2 {{ color: #fff; }}
{ONE} .role {{ color: #C5D2E4; }}
@media (max-width: 699px) {{ {ONE} {{ grid-column: auto; }} {ONE} .person-photo {{ aspect-ratio: 4 / 5; }} }}
""",
    # 4: mosaic, names over the photographs, founder tile double size, logo tile closes the grid
    't4': BASE + f"""
@media (min-width: 700px) {{
  {P} {{ grid-template-columns: repeat(5, 1fr); gap: 14px; }}
  {ONE} {{ grid-column: span 2; grid-row: span 2; }}
  {P}::after {{ content: ""; border-radius: 8px; background: #0B1C35 url(assets/img/logo-mark.webp) center / 44% no-repeat; }}
  {ONE} h2 {{ font-size: 2.1rem; padding: 0 28px; }}
  {ONE} .role {{ font-size: 1.05rem; padding: 6px 28px 26px; }}
}}
{LI} {{ display: grid; grid-template-columns: minmax(0, 1fr); grid-template-rows: 1fr auto auto; border: 0; }}
{P} > li:nth-child(n+2) {{ aspect-ratio: 4 / 5; }}
{LI} .person-photo {{ grid-area: 1 / 1 / 4 / 2; width: 100%; height: 100%; aspect-ratio: auto; position: relative; }}
{LI} .person-photo::after {{ content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11, 28, 53, 0) 48%, rgba(11, 28, 53, .93) 100%); }}
{LI} h2 {{ grid-area: 2 / 1 / 3 / 2; position: relative; z-index: 1; color: #fff; padding: 0 16px; font-size: 1.12rem; }}
{LI} .role {{ grid-area: 3 / 1 / 4 / 2; position: relative; z-index: 1; color: #C5D2E4; padding: 3px 16px 16px; font-size: .9rem; }}
{LI} h2::before {{ content: ""; display: block; width: 34px; height: 3px; background: #8DB4E2; margin-bottom: 10px; }}
""",
    # 5: round portraits, founder centred above
    't5': BASE + f"""
{P} {{ gap: 44px 20px; }}
@media (min-width: 700px) {{ {P} {{ grid-template-columns: repeat(5, 1fr); }} }}
{LI} {{ background: none; border: 0; box-shadow: none; overflow: visible; align-items: center; text-align: center; }}
{LI} .person-photo {{ width: min(100%, 176px); aspect-ratio: 1; border-radius: 50%; overflow: hidden; box-shadow: 0 0 0 5px #fff, 0 0 0 6px #C7D3E3, 0 24px 34px -22px rgba(11, 28, 53, .6); font-size: 2.6rem; }}
{LI} h2 {{ padding: 20px 0 0; font-size: 1.15rem; }}
{LI} .role {{ padding: 4px 0 0; }}
{ONE} {{ grid-column: 1 / -1; }}
{ONE} .person-photo {{ width: 250px; box-shadow: 0 0 0 6px #fff, 0 0 0 8px #8DB4E2, 0 30px 44px -26px rgba(11, 28, 53, .7); }}
{ONE} h2 {{ font-size: 2.2rem; padding-top: 26px; }}
{ONE} .role {{ font-size: 1.08rem; }}
@media (max-width: 699px) {{ {ONE} .person-photo {{ aspect-ratio: 1; width: 190px; }} {ONE} h2 {{ font-size: 1.6rem; }} {LI} .person-photo {{ width: 128px; }} }}
""",
    # 6: founder banner three columns wide with one lawyer beside it, four lawyers below
    't6': BASE + FOUNDER_BANNER + f"""
@media (min-width: 700px) {{
  {P} {{ grid-template-columns: repeat(4, 1fr); gap: 26px; }}
  {ONE} {{ grid-column: span 3; grid-template-columns: 44% 1fr; gap: 0 40px; }}
  {ONE} .person-photo {{ height: 100%; }}
  {ONE} h2 {{ font-size: 2.5rem; }}
}}
{P} > li:nth-child(n+2) .person-photo {{ border-bottom: 3px solid #8DB4E2; }}
""",
    # 3: today's structure (founder beside a list), with real portraits in the list
    't3': f"""
{P} > li:nth-child(n+2) .person-photo {{ width: 76px; height: 76px; border-radius: 8px; border: 0; background: linear-gradient(160deg, #1D3D6B, #0B1C35); color: #8DB4E2; font-size: 1.3rem; font-weight: 800; overflow: hidden; }}
{P} > li:nth-child(n+2) .person-photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 8%; }}
{P} > li:nth-child(n+2) {{ grid-template-columns: 76px 1fr; gap: 2px 20px; padding-block: 14px; }}
@media (min-width: 1000px) {{ {P} {{ grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); }} {P} > li:nth-child(n+2) h2 {{ font-size: 1.35rem; }} }}
""",
}

SWAP = "document.querySelectorAll('.people img').forEach(i=>{if(i.src.includes('hila-fried'))i.src='mockups/team/hila-720.webp';if(i.src.includes('hagai'))i.src='assets/img/hagai-cohen-720.webp'})"

with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome')
    for w, h, s, tag in ((1440, 900, 1, 'desktop'), (390, 844, 2, 'phone')):
        ctx = b.new_context(viewport={'width': w, 'height': h}, device_scale_factor=s, reduced_motion='reduce', bypass_csp=True)
        pg = ctx.new_page()
        for k, css in sorted(V.items()):
            if len(sys.argv) > 3 and k not in sys.argv[3:]:
                continue
            pg.goto('http://127.0.0.1:8765/team.html', wait_until='networkidle')
            pg.evaluate(SWAP)
            pg.add_style_tag(content=css)
            pg.wait_for_timeout(500)
            if pg.evaluate('document.documentElement.scrollWidth>innerWidth'):
                print('OVERFLOW', k, w)
            box = pg.evaluate("(()=>{const r=document.querySelector('.people').getBoundingClientRect();return Math.round(r.bottom+scrollY)})()")
            f = os.path.join(out, f'{k}-{tag}.png')
            pg.screenshot(path=f, full_page=True)
            im = Image.open(f)
            im = im.crop((0, 0, im.width, min(im.height, (box + 60) * s)))
            if s == 2:
                im = im.resize((im.width // 2, im.height // 2))
            im.save(f)
            print(k, tag, im.size)
        ctx.close()
    b.close()
