# -*- coding: utf-8 -*-
import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)

def inspect_range(start_u, end_u):
    for u in range(start_u, end_u + 1):
        if u + 1 >= len(lessons):
            break
        l_text = lessons[u + 1]
        lines = re.findall(r'<div class="txt-line"><div>(.*?)</div>(?:<div class="ur">(.*?)</div>)?</div>', l_text)
        print(f"\n==================== UNIT {u} ====================")
        cur_t = None
        t_title = ""
        items = []
        for ar, ur in lines:
            clean_ar = re.sub(r'<[^>]+>', '', ar).strip()
            clean_ur = re.sub(r'<[^>]+>', '', ur).strip() if ur else ''
            norm_ar = re.sub(r'^[^\w\s\(\)\[\]\-]+', '', clean_ar)
            m = re.match(r'^([0-9]+)\s*-\s*(.*)', norm_ar)
            if m:
                if cur_t:
                    print(f"  Tamreen {cur_t} [{t_title[:45]}]: {len(items)} items")
                    for it_ar, it_ur in items[:3]:
                        print(f"     • {it_ar[:60]} | {it_ur[:60]}")
                cur_t = m.group(1)
                t_title = m.group(2).strip()
                items = []
            elif cur_t and clean_ar:
                items.append((clean_ar, clean_ur))
        if cur_t:
            print(f"  Tamreen {cur_t} [{t_title[:45]}]: {len(items)} items")
            for it_ar, it_ur in items[:3]:
                print(f"     • {it_ar[:60]} | {it_ur[:60]}")

if __name__ == '__main__':
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    inspect_range(start, end)
