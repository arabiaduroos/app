import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

def extract_detailed_exercises(fname, bnum):
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    sections = re.findall(r'<section class="unit-card"[^>]*id="([^"]+)"([\s\S]*?)</section>', html)
    
    book_data = []
    for uid, sec in sections:
        if uid in ['b2_u1', 'b3_u1']: # skip muqaddimah
            continue
        
        m_num = int(re.search(r'u(\d+)', uid).group(1))
        unit_num = m_num - 1 # 1-indexed lesson number
        
        title_m = re.search(r'<h2 class="unit-title">[\s\S]*?<span>([^<]*)</span>\s*([^<]+)</h2>', sec)
        title = title_m.group(2).strip() if title_m else uid
        
        # Split by txt-lines
        lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', sec)
        
        ex_blocks = []
        cur_ex = None
        
        for ar_raw, ur_raw in lines:
            ar = re.sub(r'<[^>]+>', '', ar_raw).strip()
            ur = re.sub(r'<[^>]+>', '', ur_raw).strip() if ur_raw else ''
            
            if 'الكلمات الجديدة' in ar:
                if cur_ex:
                    ex_blocks.append(cur_ex)
                    cur_ex = None
                break
            
            # Check if line is an exercise heading
            # e.g. 1- أجب, 2- ضع, 3- تأمل, etc.
            is_hdr = bool(re.search(r'^(?:[🔹🐪👁️🚪📚⌚\s]*)(?:\(\d+\)|\d+[\-\.]|تمرين|تمارين|التدريب)', ar))
            has_verb = any(k in ar for k in ['أجب', 'تأمل', 'ضع', 'أدخل', 'اقرأ', 'املأ', 'حوّل', 'هات', 'صُغ', 'تمرين', 'تمارين', 'كوّن', 'عَيّن', 'مَيّز', 'استعمل', 'اضبط', 'اكتب', 'استخرج', 'بين'])
            
            if is_hdr and has_verb:
                if cur_ex:
                    ex_blocks.append(cur_ex)
                cur_ex = {
                    'header_ar': ar,
                    'header_ur': ur,
                    'items': []
                }
            elif cur_ex is not None:
                if ar and not re.match(r'^[=\-•\s]+$', ar):
                    cur_ex['items'].append({'ar': ar, 'ur': ur})
        
        if cur_ex:
            ex_blocks.append(cur_ex)
            
        book_data.append({
            'unit_num': unit_num,
            'uid': uid,
            'title': title,
            'exercises': ex_blocks
        })
        
    return book_data

b2_data = extract_detailed_exercises('transcriptions/Madinah-Book-2.html', 2)
print(f"Book 2 extracted: {len(b2_data)} units")
for u in b2_data:
    item_count = sum(len(e['items']) for e in u['exercises'])
    print(f"Unit {u['unit_num']:2d}: {len(u['exercises'])} exercises, {item_count} items")

with open('scratch/b2_raw_exercises.json', 'w', encoding='utf-8') as f:
    json.dump(b2_data, f, ensure_ascii=False, indent=2)

b3_data = extract_detailed_exercises('transcriptions/Madinah-Book-3.html', 3)
print(f"\nBook 3 extracted: {len(b3_data)} units")
for u in b3_data:
    item_count = sum(len(e['items']) for e in u['exercises'])
    print(f"Unit {u['unit_num']:2d}: {len(u['exercises'])} exercises, {item_count} items")

with open('scratch/b3_raw_exercises.json', 'w', encoding='utf-8') as f:
    json.dump(b3_data, f, ensure_ascii=False, indent=2)

print("\nSaved scratch/b2_raw_exercises.json and scratch/b3_raw_exercises.json")
