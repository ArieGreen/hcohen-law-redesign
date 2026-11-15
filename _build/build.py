"""Rebuild the ח. כהן site in the chosen design (direction A: noir & gold).

All copy is taken verbatim from the mirrored original pages; this script only
changes markup structure and styling hooks. The one approved text change is the
accessibility statement (STATEMENT_UPDATES). Usage: python build.py <orig_dir> <out_dir>
"""
import glob
import hashlib
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
LEGAL_FILES = {'privacy.html', 'terms.html', 'cookies.html', 'accessibility.html'}
AREA_ICONS = {'religious-services.html': 'i-stone', 'labor.html': 'i-users', 'administrative.html': 'i-landmark',
              'tenders.html': 'i-stamp', 'kashrut.html': 'i-badge', 'collection.html': 'i-coins'}
# practice-area page blocks, keyed by their (original) heading
SECTION_KINDS = {'השירותים בתחום': 'services', 'בין הנושאים שבהם המשרד מטפל': 'topics', 'מסגרת הדין': 'law',
                 'דפי נושא': 'topic-pages', 'מאמרים בתחום': 'articles'}


def icon(name, cls='icon'):
    return f'<svg class="{cls}" aria-hidden="true"><use href="assets/img/icons.svg#{name}"/></svg>'


ARROW = icon('i-arrow')


def head_bg(src='towers-duo', pos=''):
    return (f'<div class="head-bg" aria-hidden="true"><img src="assets/img/{src}-1000.webp" srcset="assets/img/{src}-600.webp 600w, '
            f'assets/img/{src}-1000.webp 1000w" sizes="100vw" width="1000" height="1250" alt="" decoding="async" fetchpriority="high"></div>')


def read(name):
    return open(os.path.join(ORIG, name), encoding='utf8').read()


def soup_of(html):
    return BeautifulSoup(html, 'html.parser')


ORIG_INDEX = soup_of(read('index.html'))
PHONE_A = ORIG_INDEX.footer.find('a', href=re.compile('^tel:'))
PHONE_TXT, PHONE_HREF = PHONE_A.get_text(strip=True), PHONE_A['href']
TOC_LABEL = soup_of(read('article-mikvaot.html')).find('p', class_='toc-title').get_text(strip=True)
CONTACT_TXT = ORIG_INDEX.find('nav', id='main-nav').find('a', href='contact.html').get_text()


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
    f = str(ORIG_INDEX.find('footer', class_='site-footer'))
    m_cta = (f'<div class="m-cta" lang="he" dir="rtl"><a href="{PHONE_HREF}">{icon("i-phone")}<span dir="ltr">{PHONE_TXT}</span></a>'
             f'<a href="contact.html">{icon("i-chat")}{CONTACT_TXT}</a></div>')
    return f + '\n' + m_cta + f'\n<script src="assets/js/site.js?v={JSV}" defer></script>\n'


def new_head(head_html):
    h = re.sub(r'<link rel="preload"[^>]+>\n?', '', head_html)
    h = re.sub(r'assets/css/site\.css\?v=\w+', f'assets/css/site.css?v={V}', h)
    h = re.sub(r'assets/js/a11y-init\.js\?v=\w+', f'assets/js/a11y-init.js?v={V}', h)
    h = h.replace('content="#FAF6EE"', 'content="#0A101C"')
    pre = ('<link rel="preload" href="assets/fonts/noto-serif-hebrew-hebrew.woff2" as="font" type="font/woff2" crossorigin>\n'
           '<link rel="preload" href="assets/fonts/heebo-hebrew.woff2" as="font" type="font/woff2" crossorigin>\n')
    return h.replace('<link rel="stylesheet"', pre + '<link rel="stylesheet"', 1)


def toc_html(heads):
    items = ''
    for i, h in enumerate(heads, 1):
        h['id'] = h.get('id') or f's{i}'
        items += f'<li><a href="#{h["id"]}">{h.get_text(strip=True)}</a></li>'
    return f'<nav class="toc" aria-labelledby="toc-title"><p class="toc-title" id="toc-title">{TOC_LABEL}</p><ol>{items}</ol></nav>'


def area_page(s, block):
    """Practice-area page: lead paragraphs + contents panel, then one designed block per heading."""
    prose = block.find('div', class_='prose', recursive=False)
    intro, sections, more, cur = [], [], [], None
    for el in [c for c in prose.children if getattr(c, 'name', None)]:
        if el.name == 'h2':
            cur = [el]; sections.append(cur)
        elif el.name == 'p' and el.get_text(strip=True).startswith('תחומים נוספים'):
            more.append(el)
        elif cur is None:
            intro.append(el)
        else:
            cur.append(el)
    toc = toc_html([sec[0] for sec in sections])
    out = (f'<div class="rs-top"><div class="container"><div class="lead-col">{"".join(str(e) for e in intro)}</div>{toc}</div></div>')
    for sec in sections:
        kind = SECTION_KINDS.get(sec[0].get_text(strip=True), 'plain')
        body = ''
        for el in sec[1:]:
            if el.name == 'ul' and kind in ('services', 'law'):
                for li in el.find_all('li', recursive=False):
                    li.insert(0, soup_of(icon('i-check' if kind == 'services' else 'i-book', 'icon li-ico')))
            body += str(el)
        out += f'<section class="rs-sec rs-{kind}"><div class="container">{sec[0]}{body}</div></section>'
    if more:
        out += f'<div class="rs-more"><div class="container">{"".join(str(p) for p in more)}</div></div>'
    block.replace_with(soup_of(out))


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
        ph['class'] = ph.get('class', []) + ['grain']
        ph.append(soup_of(head_bg()))
        ph.append(inner)
    if name.startswith('article-'):
        art = s.main.find('article')
        art['class'] = art.get('class', []) + ['article-layout']
    elif name in AREA_FILES:
        area_page(s, s.main.find('div', class_='block'))
    elif name.startswith('topic-'):
        block = s.main.find('div', class_='block')
        prose = block.find('div', class_='prose', recursive=False)
        prose.insert_before(soup_of(toc_html(prose.find_all('h2'))))
        block['class'] = block.get('class', []) + ['article-layout']
    elif name == 'areas.html':
        for li in s.main.select('ul.area-list > li'):
            href = li.find('h3').a['href']
            li.insert(0, soup_of(icon(AREA_ICONS.get(href, 'i-scroll'), 'icon area-ico')))
            more = li.find('a', class_='more')
            if more:
                more.append(soup_of(ARROW))
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
    btns = ''.join(f'<a class="btn{" solid" if i == 0 else ""}" href="{a["href"]}">{a.get_text(strip=True)}</a>'
                   for i, a in enumerate(hero.find('p', class_='hero-links').find_all('a')))

    intro = m.find('section', class_='home-intro')
    intro_h2 = intro.find('h2').decode_contents()
    intro_ps = ''.join(str(p) for p in intro.find('div', class_='intro-body').find_all('p'))
    intro_more = intro.find('a', class_='more')

    band = m.find('section', class_='band-dark')
    areas_h2 = band.find('h2').decode_contents()
    cards = ''
    for li in band.select('ul.area-list > li'):
        a = li.find('h3').find('a'); more = li.find('a', class_='more')
        cards += (f'<li><a href="{a["href"]}">{icon(AREA_ICONS[a["href"]], "icon area-ico")}<h3>{a.get_text(strip=True)}</h3>'
                  f'<p>{li.find("p").get_text(strip=True)}</p><span class="more">{more.decode_contents()}{ARROW}</span></a></li>')
    notary = band.find('p', class_='muted').get_text(strip=True)

    pubs = m.find('section', class_='home-pubs')
    pubs_h2 = pubs.find('h2').decode_contents()
    pub_cards = ''.join(f'<li><a href="{li.a["href"]}"><span class="meta">{li.find("div", class_="meta").get_text(strip=True)}</span>'
                        f'<span class="pt">{li.a.get_text(strip=True)}</span>{ARROW}</a></li>' for li in pubs.select('ul.pub-list > li'))
    all_more = pubs.find_all('a', class_='more')[-1]
    portrait_alt = soup_of(read('hagai-cohen.html')).find('div', class_='profile-photo').find('img')['alt']
    emblem = '<div class="orn" aria-hidden="true"><img src="assets/img/logo-mark.webp" alt="" width="223" height="240" loading="lazy"></div>'

    return f'''<main id="main" tabindex="-1">

<section class="hero grain" aria-labelledby="hero-title">
  <div class="head-bg"><img src="assets/img/bsr-towers-1000.webp" srcset="assets/img/bsr-towers-600.webp 600w, assets/img/bsr-towers-1000.webp 1000w" sizes="100vw" width="1000" height="1250" alt="{img["alt"]}" decoding="async" fetchpriority="high"></div>
  <div class="container">
    <img class="emblem" src="assets/img/logo-mark.webp" alt="" width="223" height="240">
    <h1 id="hero-title"><span class="h1-name">{h1_name}</span><span class="visually-hidden"> | </span><span class="tagline">{tagline}</span></h1>
    <div class="hero-actions">{btns}</div>
  </div>
  <p class="seal">{kicker}</p>
</section>

<section class="intro seam-arc" aria-labelledby="intro-h">
  <div class="container">
    <figure class="frame"><img src="assets/img/hagai-cohen-720.webp" srcset="assets/img/hagai-cohen-420.webp 420w, assets/img/hagai-cohen-720.webp 720w" sizes="(min-width: 900px) 38vw, 100vw" width="720" height="900" alt="{portrait_alt}" loading="lazy" decoding="async"></figure>
    <div>
      <h2 id="intro-h">{intro_h2}</h2>
      {intro_ps}
      <a class="lnk" href="{intro_more["href"]}">{intro_more.get_text(strip=True)}{ARROW}</a>
    </div>
  </div>
</section>

<section class="areas seam-seal" aria-labelledby="areas-h">
  <div class="container">
    <h2 class="sec-title" id="areas-h">{areas_h2}</h2>
    {emblem}
    <ul class="cards">{cards}</ul>
    <p class="notary">{notary}</p>
  </div>
</section>

<section class="pubs seam-dome" aria-labelledby="pubs-h">
  <div class="container">
    <h2 class="sec-title" id="pubs-h">{pubs_h2}</h2>
    {emblem}
    <ul class="pub-cards">{pub_cards}</ul>
    <p class="center"><a class="btn dark" href="{all_more["href"]}">{all_more.get_text(strip=True)}</a></p>
  </div>
</section>

</main>'''


def body_class(name, tag):
    cls = re.search(r'class="([^"]*)"', tag).group(1).split()
    if name.startswith('article-'):
        cls.append('page-article')
    if name.startswith('topic-'):
        cls.append('page-topic')
    if name in LEGAL_FILES:
        cls.append('page-legal')
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
