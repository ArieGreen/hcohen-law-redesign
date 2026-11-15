"""Title-block variants on top of hero option 2b. Same words: 'ח. כהן - משרד עורכי דין'."""
import os, sys
P = sys.argv[1]
src = open(os.path.join(P, 'mockups', 'hero', 'h2b.html'), encoding='utf8').read()
OLD = '<h1>ח. כהן - משרד עורכי דין</h1>'
assert OLD in src
LOGO = '<img class="mk" src="../../assets/img/logo-mark.webp" alt="">'
V = {
 # t1: weight contrast. name huge and heavy, the profession light and sky-blue, a vertical sky rule beside the block
 't1': ('<h1 class="t1"><span class="nm">ח. כהן</span><span class="dash"> - </span><span class="pr">משרד עורכי דין</span></h1>',
        '.txt{border-inline-start:3px solid var(--sky);padding-inline-start:36px;margin-inline-start:-39px}'
        '.t1 .nm{display:block;font-size:7rem;line-height:.95}.t1 .dash{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}'
        '.t1 .pr{display:block;font-size:2.6rem;font-weight:300;color:var(--sky);margin-top:14px;letter-spacing:.01em}'),
 # t2: the gold HC mark beside the name, profession set smaller on a rule under it
 't2': (f'<h1 class="t2">{LOGO}<span class="nm">ח. כהן</span><span class="dash"> - </span><span class="pr">משרד עורכי דין</span></h1>',
        '.t2{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:0 22px}'
        '.t2 .mk{grid-row:1;width:92px;filter:drop-shadow(0 6px 20px rgba(0,0,0,.35))}.t2 .nm{grid-row:1;font-size:6.4rem;line-height:1}'
        '.t2 .dash{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}'
        '.t2 .pr{grid-column:1/-1;margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,.25);font-size:1.9rem;font-weight:500;color:#DCE6F3}'),
 # t3: name and profession on one line, the dash turned into a sky-blue bar, profession in outline weight
 't3': ('<h1 class="t3"><span class="nm">ח. כהן</span><span class="dash"> - </span><span class="pr">משרד עורכי דין</span></h1>',
        '.t3{font-size:4.6rem;line-height:1.05}.t3 .dash{display:inline-block;width:56px;height:6px;margin:0 18px .28em;vertical-align:middle;background:var(--sky);border-radius:3px;color:transparent;overflow:hidden;font-size:0}'
        '.t3 .pr{display:block;font-weight:300;color:#fff;opacity:.92}'),
}
for k, (h1, css) in V.items():
    out = src.replace(OLD, h1).replace('</style>', css + '</style>')
    open(os.path.join(P, 'mockups', 'hero', k + '.html'), 'w', encoding='utf8').write(out)
print('ok')
