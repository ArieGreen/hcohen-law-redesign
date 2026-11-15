"""More title-block directions on hero 2b, all built around the HC mark. Same words."""
import os, sys
P = sys.argv[1]
src = open(os.path.join(P, 'mockups', 'hero', 'h2b.html'), encoding='utf8').read()
OLD = '<h1>ח. כהן - משרד עורכי דין</h1>'
MK = '<img class="mk" src="../../assets/img/logo-mark.webp" alt="">'
FULL = '<img class="full" src="../../assets/img/logo-full.webp" alt="">'
HIDE = '.dash{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}'
NAME = '<span class="nm">ח. כהן</span><span class="dash"> - </span><span class="pr">משרד עורכי דין</span>'
V = {
 # t4: the HC mark as a huge faint watermark filling the panel behind the text, name heavy, profession light
 't4': (f'<h1 class="t4">{NAME}</h1>', '<img class="wm" src="../../assets/img/logo-mark.webp" alt="">',
        HIDE + '.wm{position:absolute;inset-inline-start:120px;top:50%;transform:translateY(-58%);width:560px;opacity:.07;filter:grayscale(1) brightness(3);pointer-events:none}'
        '.t4 .nm{display:block;font-size:7.2rem;line-height:.95}.t4 .pr{display:block;font-size:2.4rem;font-weight:300;color:var(--sky);margin-top:12px}'),
 # t5: the full logo (with H. COHEN LAW FIRM) on a white plate, name and profession beside it
 't5': (f'<h1 class="t5">{NAME}</h1>', '',
        HIDE + '.txt{top:120px}.t5{display:block}'
        '.t5::before{content:"";display:block;width:150px;height:158px;margin-bottom:28px;border-radius:8px;background:#fff url(../../assets/img/logo-full.webp) center/112px no-repeat;box-shadow:0 20px 40px -18px rgba(0,0,0,.5)}'
        '.t5 .nm{display:block;font-size:6rem;line-height:1}.t5 .pr{display:block;font-size:2rem;font-weight:400;color:#DCE6F3;margin-top:10px}'),
 # t6: name block framed: thin sky frame open on one side, mark on the frame's corner
 't6': (f'<h1 class="t6">{MK}{NAME}</h1>', '',
        HIDE + '.t6{position:relative;display:block;padding:44px 44px 36px;border:1px solid rgba(141,180,226,.55);border-inline-start:0;border-radius:0 0 0 0}'
        '.t6 .mk{position:absolute;top:-38px;inset-inline-end:36px;width:76px;padding:6px;background:var(--navy)}'
        '.t6 .nm{display:block;font-size:6.6rem;line-height:1}.t6 .pr{display:block;font-size:2.3rem;font-weight:300;color:var(--sky);margin-top:10px}'),
 # t7: large mark + name on one row, profession and founding year as a second row ("since" moves off the photo into the panel)
 't7': (f'<h1 class="t7">{MK}<span class="col"><span class="nm">ח. כהן</span><span class="dash"> - </span><span class="pr">משרד עורכי דין</span></span></h1>', '',
        HIDE + ''
        '.t7{display:flex;align-items:center;gap:28px;padding-bottom:28px;border-bottom:1px solid rgba(255,255,255,.2)}'
        '.t7 .mk{width:150px;filter:drop-shadow(0 10px 28px rgba(0,0,0,.45))}.t7 .col{display:flex;flex-direction:column}'
        '.t7 .nm{font-size:6.4rem;line-height:.95}.t7 .pr{font-size:2.1rem;font-weight:300;color:var(--sky);margin-top:10px}'
        '.tag{margin-top:26px}'),
}
for k, (h1, extra, css) in V.items():
    out = src.replace(OLD, h1).replace('<div class="txt">', extra + '<div class="txt">').replace('</style>', css + '</style>')
    open(os.path.join(P, 'mockups', 'hero', k + '.html'), 'w', encoding='utf8').write(out)
print('ok')
