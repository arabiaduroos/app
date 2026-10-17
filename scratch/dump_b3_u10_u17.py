# -*- coding: utf-8 -*-
import re, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('transcriptions/Madinah-Book-3.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)
for u in range(10, 18):
    if u + 1 >= len(lessons):
        break
    l_text = lessons[u + 1]
    title_m = re.search(r'(الدَّرْسُ\s+[^\n<]+)', l_text)
    t = title_m.group(1) if title_m else f'Unit {u}'
    print(f"\n==================== {t} ====================")
    lines = re.findall(r'<div class="txt-line"><div>(.*?)</div>(?:<div class="ur">(.*?)</div>)?</div>', l_text)
    for ar, ur in lines[:12]:
        clean_ar = re.sub(r'<[^>]+>', '', ar).strip()
        clean_ur = re.sub(r'<[^>]+>', '', ur).strip() if ur else ''
        if clean_ar:
            print(f"  AR: {clean_ar}")
            if clean_ur:
                print(f"  UR: {clean_ur}")
