"""Variants of hero option 2 (diagonal): different treatments for the practice-area row."""
import os, re, sys
P = sys.argv[1]
src = open(os.path.join(P, 'mockups', 'hero', 'h2.html'), encoding='utf8').read()
strip_html = re.search(r'<nav class="strip">.*?</nav>', src, re.S).group(0)
links = re.findall(r'<a>(<svg.*?</svg>)(.*?)</a>', strip_html, re.S)
V = {
 # a. clean: no area row at all, text block vertically centred
 'h2a': ('', '.strip{display:none}.txt{top:50%;transform:translateY(-50%)}'),
 # b. full-width bar along the bottom of the hero, crossing photo and panel, six equal cells
 'h2b': ('<nav class="bar">' + ''.join(f'<a>{i}<span>{t}</span></a>' for i, t in links) + '</nav>',
         '.strip{display:none}.txt{top:130px}'
         '.bar{position:absolute;inset-inline:0;bottom:0;display:grid;grid-template-columns:repeat(6,1fr);background:#fff;box-shadow:0 -10px 30px -12px rgba(0,0,0,.35)}'
         '.bar a{display:flex;align-items:center;gap:12px;height:96px;padding:0 22px;color:var(--navy);font-weight:700;font-size:.95rem;line-height:1.3;border-inline-start:1px solid var(--line)}'
         '.bar a:first-child{border:0;padding-inline-start:100px}.bar .icon{width:28px;height:28px;color:var(--accent);flex:none}'),
 # c. quiet index under the buttons: two columns of text links with thin rules, inside the navy panel
 'h2c': ('<nav class="idx">' + ''.join(f'<a>{t}<svg class="icon ar"><use href="../../assets/img/icons.svg#i-arrow"/></svg></a>' for _, t in links) + '</nav>',
         '.strip{display:none}.txt{top:110px}'
         '.idx{position:absolute;inset-inline-start:100px;bottom:52px;width:600px;display:grid;grid-template-columns:1fr 1fr;gap:0 36px;border-top:1px solid rgba(255,255,255,.2)}'
         '.idx a{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.14);color:#fff;font-weight:500;font-size:.98rem}'
         '.idx .ar{color:var(--sky);width:18px;height:18px}'),
}
for k, (html, css) in V.items():
    out = src.replace('</style>', css + '</style>').replace('</section>', html + '</section>', 1)
    open(os.path.join(P, 'mockups', 'hero', k + '.html'), 'w', encoding='utf8').write(out)
print('ok')
