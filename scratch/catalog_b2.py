# -*- coding: utf-8 -*-
"""
Analysis of all 31 lessons in Book 2:
Extracts every exercise and its numbered items.
"""
import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)

book2_catalog = []

for i in range(2, len(lessons)):
    l_text = lessons[i]
    title_match = re.search(r'(الدَّرْسُ\s+[^\n<]+)', l_text)
    title = title_match.group(1) if title_match else f"Lesson {i-1}"
    
    # Split text into lines
    lines = re.findall(r'<div class="txt-line"><div>(.*?)</div>(?:<div class="ur">(.*?)</div>)?</div>', l_text)
    
    # Identify exercises
    ex_list = []
    current_ex = None
    
    for ar, ur in lines:
        clean_ar = re.sub(r'<[^>]+>', '', ar).strip()
        clean_ur = re.sub(r'<[^>]+>', '', ur).strip() if ur else ''
        # Strip leading emojis
        norm_ar = re.sub(r'^[\u2600-\u27bf\U0001f300-\U0001f9ff\s]+', '', clean_ar)
        
        # Check if exercise header: e.g. '1- ', '2- ', 'التمرين الأول'
        m = re.match(r'^([0-9]+)\s*-\s*(.*)', norm_ar)
        if m:
            num = int(m.group(1))
            t_title = m.group(2).strip()
            current_ex = {
                "num": num,
                "title_ar": t_title,
                "title_ur": clean_ur,
                "items": []
            }
            ex_list.append(current_ex)
        elif current_ex is not None:
            if clean_ar and not clean_ar.startswith('####') and not clean_ar.startswith('(' + str(i-1) + ')'):
                current_ex["items"].append({"ar": clean_ar, "ur": clean_ur})
                
    book2_catalog.append({
        "unit_num": i-1,
        "title": title,
        "exercises": ex_list
    })

print(f"Cataloged {len(book2_catalog)} lessons for Book 2.")
for c in book2_catalog:
    items_total = sum(len(e["items"]) for e in c["exercises"])
    print(f"Lesson {c['unit_num']:2d} ({c['title'][:22]}): {len(c['exercises'])} exercises, {items_total} total items")
    for e in c['exercises'][:3]:
        print(f"   [Ex {e['num']}] {e['title_ar'][:50]} ({len(e['items'])} items)")
