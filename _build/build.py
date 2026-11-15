"""Rebuild the ח. כהן site in the new design.

All copy is taken verbatim from the mirrored original pages; this script only
changes markup structure and styling hooks. Usage: python build.py <orig_dir> <out_dir>
"""
import glob
import hashlib
import math
import os
import re
import sys

from bs4 import BeautifulSoup

ORIG, OUT = sys.argv[1], sys.argv[2]
V = hashlib.md5(open(os.path.join(OUT, 'assets', 'css', 'site.css'), 'rb').read()).hexdigest()[:10]
JSV = hashlib.md5(open(os.path.join(OUT, 'assets', 'js', 'site.js'), 'rb').read()).hexdigest()[:10]
STATEMENT_UPDATES = {
    'עדכון אחרון: 7.11.2026': 'עדכון אחרון: 15.11.2026',
    'באתר אין אנימציות, תוכן נע או תוכן מהבהב.':
        'באתר יש אנימציות עדינות וקצרות בלבד: הופעה הדרגתית של תוכן בטעינת העמוד ובגלילה. '
        'אין באתר תוכן מהבהב ואין תוכן שנע ברציפות. מי שהגדיר "הפחתת תנועה" במערכת ההפעלה לא יראה אנימציות, '
        'ואפשר לעצור את כל האנימציות בכפתור "עצירת אנימציות" בתפריט הנגישות.',
    'תפריט נגישות: הגדלת טקסט, ניגודיות גבוהה, הדגשת קישורים וגופן קריא.':
        'תפריט נגישות: הגדלת טקסט, ניגודיות גבוהה, הדגשת קישורים, גופן קריא ועצירת אנימציות.',
}
AREA_FILES = {'religious-services.html', 'labor.html', 'administrative.html', 'tenders.html', 'kashrut.html', 'collection.html'}


def arc(cls='', a0=40, a1=320):
    """The brand device: an open arc of the logo's C, drawn as a real SVG path (angles in degrees, clockwise)."""
    p = lambda a: (50 + 49 * math.cos(math.radians(a)), 50 + 49 * math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return (f'<svg class="{("arc " + cls).strip()}" viewBox="0 0 100 100" aria-hidden="true" focusable="false">'
            f'<path d="M{x0:.2f} {y0:.2f}A49 49 0 {large} 1 {x1:.2f} {y1:.2f}"/></svg>')


def icon(name):
    return f'<svg class="icon" aria-hidden="true"><use href="assets/img/icons.svg#{name}"/></svg>'


def read(name):
    return open(os.path.join(ORIG, name), encoding='utf8').read()


def soup_of(html):
    return BeautifulSoup(html, 'html.parser')


ORIG_INDEX = soup_of(read('index.html'))
PHONE_A = ORIG_INDEX.footer.find('a', href=re.compile('^tel:'))
PHONE_TXT, PHONE_HREF = PHONE_A.get_text(strip=True), PHONE_A['href']
TOC_LABEL = soup_of(read('article-mikvaot.html')).find('p', class_='toc-title').get_text(strip=True)


def header(cur):
    h = soup_of(str(ORIG_INDEX.find('header', class_='site-header')))
    skip = ORIG_INDEX.find('a', class_='skip-link')
    box = h.header.find('div', class_='container')
    box['class'] = ['container', 'header-row']
    brand, toggle, nav = box.find('a', class_='brand'), box.find('button', class_='nav-toggle'), box.find('nav')
    for a in nav.find_all('a'):
        if a['href'] == cur or (a['href'] == 'areas.html' and cur in AREA_FILES):
            a['aria-current'] = 'page'
    call = soup_of(f'<a class="header-call" href="{PHONE_HREF}">{icon("i-phone")}<span class="num" dir="ltr">{PHONE_TXT}</span></a>')
    box.clear()
    for el in (brand, nav, call, toggle):
        box.append(el)
    return str(skip) + '\n' + str(h) + '\n'


def footer():
    f = soup_of(str(ORIG_INDEX.find('footer', class_='site-footer')))
    f.footer.insert(0, soup_of(arc('', 200, 470)))
    m_cta = (f'<div class="m-cta" lang="he" dir="rtl"><a href="{PHONE_HREF}">{icon("i-phone")}<span dir="ltr">{PHONE_TXT}</span></a>'
             f'<a href="contact.html">{icon("i-chat")}{ORIG_INDEX.find("nav", id="main-nav").find("a", href="contact.html").get_text()}</a></div>')
    return str(f) + '\n' + m_cta + f'\n<script src="assets/js/site.js?v={JSV}" defer></script>\n'


def new_head(head_html):
    h = re.sub(r'<link rel="preload"[^>]+>\n?', '', head_html)
    h = re.sub(r'assets/css/site\.css\?v=\w+', f'assets/css/site.css?v={V}', h)
    h = re.sub(r'assets/js/a11y-init\.js\?v=\w+', f'assets/js/a11y-init.js?v={V}', h)
    h = h.replace('content="#FAF6EE"', 'content="#0E1B30"')
    pre = ('<link rel="preload" href="assets/fonts/david-700-hebrew.woff2" as="font" type="font/woff2" crossorigin>\n'
           '<link rel="preload" href="assets/fonts/heebo-hebrew.woff2" as="font" type="font/woff2" crossorigin>\n')
    return h.replace('<link rel="stylesheet"', pre + '<link rel="stylesheet"', 1)


def transform_main(name, main_html):
    s = soup_of(main_html)
    ph = s.main.find('div', class_='page-head')
    if ph:
        h1, crumbs, leads = ph.find('h1'), ph.find('nav', class_='breadcrumbs'), ph.find_all('p', class_='lead')
        inner = s.new_tag('div', attrs={'class': 'container'})
        for el in [crumbs, h1, *leads]:
            if el:
                inner.append(el.extract())
        ph.clear()
        ph.append(soup_of(arc('', 125, 415)))
        ph.append(inner)
    if name.startswith('article-'):
        art = s.main.find('article')
        art['class'] = art.get('class', []) + ['article-layout']
    elif name in AREA_FILES or name.startswith('topic-'):
        # same "בעמוד זה" contents panel the article pages use, built from this page's own headings
        block = s.main.find('div', class_='block')
        prose = block.find('div', class_='prose', recursive=False)
        heads = prose.find_all('h2')
        label = TOC_LABEL
        items = ''
        for i, h in enumerate(heads, 1):
            h['id'] = h.get('id') or f's{i}'
            items += f'<li><a href="#{h["id"]}">{h.get_text(strip=True)}</a></li>'
        prose.insert_before(soup_of(f'<nav class="toc" aria-labelledby="toc-title"><p class="toc-title" id="toc-title">{label}</p><ol>{items}</ol></nav>'))
        block['class'] = block.get('class', []) + ['article-layout']
    elif name == 'accessibility.html':
        # approved by the client (15.11.2026): the redesign adds light animations
        for el in s.main.find_all(['li', 'p']):
            t = el.get_text(strip=True)
            if t in STATEMENT_UPDATES:
                el.string = STATEMENT_UPDATES[t]
    for img in s.main.find_all('img', src=re.compile('bsr-towers')):
        img['src'] = img['src'].replace('bsr-towers', 'towers-duo')
        if img.get('srcset'):
            img['srcset'] = img['srcset'].replace('bsr-towers', 'towers-duo')
    return str(s.main)


def home_main():
    m = ORIG_INDEX.main
    hero = m.find('section', class_='home-hero')
    img = hero.find('img')
    kicker = hero.find('p', class_='hero-kicker').get_text(strip=True)
    h1 = hero.find('h1')
    h1_name = h1.contents[0].strip()
    tagline = h1.find('span', class_='tagline').get_text(strip=True)
    links = hero.find('p', class_='hero-links').find_all('a')
    btns = ''.join(f'<a class="btn {"btn-gold" if i == 0 else "btn-line"}" href="{a["href"]}">{a.get_text(strip=True)}</a>'
                   for i, a in enumerate(links))

    intro = m.find('section', class_='home-intro')
    intro_h2 = intro.find('h2').decode_contents()
    intro_ps = ''.join(str(p) for p in intro.find('div', class_='intro-body').find_all('p'))
    intro_more = intro.find('a', class_='more')

    band = m.find('section', class_='band-dark')
    areas_h2 = band.find('h2').decode_contents()
    rows = ''
    for li in band.select('ul.area-list > li'):
        a = li.find('h3').find('a'); more = li.find('a', class_='more')
        rows += (f'<li><a href="{a["href"]}"><h3 class="ix-name">{a.get_text(strip=True)}</h3>'
                 f'<span class="ix-desc">{li.find("p").get_text(strip=True)}</span>'
                 f'<span class="ix-more">{more.decode_contents()}{icon("i-arrow")}</span></a></li>')
    notary = band.find('p', class_='muted').get_text(strip=True)

    pubs = m.find('section', class_='home-pubs')
    pubs_h2 = pubs.find('h2').decode_contents()
    items = [(li.find('div', class_='meta').get_text(strip=True), li.find('a')) for li in pubs.select('ul.pub-list > li')]
    lead_meta, lead_a = items[0]
    pub_rows = ''.join(f'<li><a href="{a["href"]}"><p class="meta">{meta}</p><span class="t">{a.get_text(strip=True)}</span></a></li>'
                       for meta, a in items[1:])
    all_more = pubs.find_all('a', class_='more')[-1]

    portrait_alt = soup_of(read('hagai-cohen.html')).find('div', class_='profile-photo').find('img')['alt']

    return f'''<main id="main" tabindex="-1">

<section class="hero" aria-labelledby="hero-title">
  <div class="hero-media">
    <img src="assets/img/towers-duo-1000.webp" srcset="assets/img/towers-duo-600.webp 600w, assets/img/towers-duo-1000.webp 1000w" sizes="(min-width: 900px) 60vw, 100vw" width="1000" height="1250" alt="{img["alt"]}" decoding="async" fetchpriority="high">
  </div>
  {arc("hero-arc", 35, 325)}
  <div class="container hero-content">
    <h1 id="hero-title"><span class="h1-name">{h1_name}</span><span class="visually-hidden"> | </span><span class="tagline">{tagline}</span></h1>
    <div class="hero-actions">{btns}</div>
  </div>
  <div class="hero-since"><div class="container"><p>{kicker}</p></div></div>
</section>

<section class="inside" aria-labelledby="intro-h">
  <div class="container grid12">
    <div class="inside-text">
      <h2 id="intro-h">{intro_h2}</h2>
      {intro_ps}
      <p class="inside-links"><a class="link-arrow" href="{intro_more["href"]}">{intro_more.get_text(strip=True)}{icon("i-arrow")}</a></p>
    </div>
    <figure class="portrait">
      {arc("", 195, 345)}
      <div class="portrait-frame"><img src="assets/img/hagai-cohen-720.webp" srcset="assets/img/hagai-cohen-420.webp 420w, assets/img/hagai-cohen-720.webp 720w" sizes="(min-width: 900px) 34vw, 100vw" width="720" height="900" alt="{portrait_alt}" loading="lazy" decoding="async"></div>
    </figure>
  </div>
</section>

<section class="areas-index" aria-labelledby="areas-h">
  <div class="container">
    <h2 id="areas-h">{areas_h2}</h2>
    <ul class="index-list">{rows}</ul>
    <p class="notary">{notary}</p>
  </div>
</section>

<section class="pubs-home" aria-labelledby="pubs-h">
  <div class="slab">
    <div class="container grid12">
      <h2 id="pubs-h">{pubs_h2}</h2>
      <article class="lead-pub">
        <p class="meta">{lead_meta}</p>
        <h3><a href="{lead_a["href"]}">{lead_a.get_text(strip=True)}</a></h3>
      </article>
      <ul class="pub-rows">{pub_rows}</ul>
      <p class="pubs-more"><a class="link-arrow" href="{all_more["href"]}">{all_more.get_text(strip=True)}{icon("i-arrow")}</a></p>
    </div>
  </div>
</section>

</main>'''


def body_class(name, tag):
    cls = re.search(r'class="([^"]*)"', tag).group(1).split()
    if name.startswith('article-'):
        cls.append('page-article')
    if name.startswith('topic-'):
        cls.append('page-topic')
    return f'<body class="{" ".join(cls)}">'


def build():
    files = sorted(glob.glob(os.path.join(ORIG, '*.html')))
    for path in files:
        name = os.path.basename(path)
        html = read(name)
        head = html[:html.index('<body')]
        btag = re.search(r'<body[^>]*>', html).group(0)
        main = re.search(r'<main[\s\S]*?</main>', html).group(0)
        main = home_main() if name == 'index.html' else transform_main(name, main)
        out = new_head(head) + body_class(name, btag) + '\n' + header(name) + '\n' + main + '\n\n' + footer() + '</body>\n</html>\n'
        open(os.path.join(OUT, name), 'w', encoding='utf8', newline='\n').write(out)
    print('built', len(files), 'pages; css', V)


build()
