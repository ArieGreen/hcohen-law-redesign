"""Card images created with AI (Gemini) by the site owner: crop to the 800:534 card ratio and save as webp.

Usage: python ai_images.py <src_dir> <site_dir>   (src files are named <key>.png)
"""
import os
import sys

from PIL import Image

src, site = sys.argv[1], sys.argv[2]
out = os.path.join(site, 'assets', 'img', 'ai')
os.makedirs(out, exist_ok=True)
for f in sorted(os.listdir(src)):
    key, ext = os.path.splitext(f)
    if ext.lower() not in ('.png', '.jpg', '.jpeg', '.webp'):
        continue
    im = Image.open(os.path.join(src, f)).convert('RGB')
    w, h = im.size
    th = round(w * 534 / 800)
    if th <= h:
        top = (h - th) // 2
        im = im.crop((0, top, w, top + th))
    else:
        tw = round(h * 800 / 534)
        left = (w - tw) // 2
        im = im.crop((left, 0, left + tw, h))
    if im.width > 1200:
        im = im.resize((1200, 801), Image.LANCZOS)
    im.save(os.path.join(out, key + '.webp'), 'WEBP', quality=86, method=6)
    print(key, im.size, os.path.getsize(os.path.join(out, key + '.webp')) // 1024, 'KB')
