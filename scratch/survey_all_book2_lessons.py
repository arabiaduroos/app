# -*- coding: utf-8 -*-
import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)
for i in range(2, len(lessons)):
    l_text = lessons[i]
    title_match = re.search(r'(الدَّرْسُ\s+[^\n<]+)', l_text)
    t = title_match.group(1) if title_match else f'L{i-1}'
    print(f'\n=== Unit {i-1}: {t} ===')
    lines = re.findall(r'<div class="txt-line"><div>(.*?)</div>(?:<div class="ur">(.*?)</div>)?</div>', l_text)
    cur_tam = None
    items = []
    for ar, ur in lines:
        clean_ar = re.sub(r'<[^>]+>', '', ar).strip()
        clean_ur = re.sub(r'<[^>]+>', '', ur).strip() if ur else ''
        norm_ar = re.sub(r'^[^\w\s\(\)\[\]\-]+', '', clean_ar)
        m = re.match(r'^([0-9]+)\s*-\s*(.*)', norm_ar)
        if m:
            if cur_tam and items:
                print(f"   Tamreen {cur_tam}: {len(items)} items")
            cur_tam = m.group(1)
            tam_title = m.group(2).strip()
            print(f'   [Tamreen {cur_tam}] {tam_title[:60]}')
            items = []
        elif cur_tam is not None and clean_ar:
            items.append((clean_ar, clean_ur))
    if cur_tam and items:
        print(f"   Tamreen {cur_tam}: {len(items)} items")
