import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

def parse_book_exercises(fname, bnum):
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    sections = re.findall(r'<section class="unit-card"[^>]*id="([^"]+)"([\s\S]*?)</section>', html)
    print(f"\n=================== BOOK {bnum}: {len(sections)} SECTIONS ===================")
    
    book_ex = {}
    for uid, sec in sections:
        title_m = re.search(r'<h2 class="unit-title">[\s\S]*?<span>([^<]*)</span>\s*([^<]+)</h2>', sec)
        title = title_m.group(2).strip() if title_m else uid
        
        # Extract lines
        lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', sec)
        
        # Group lines into exercises
        exercises = []
        current_ex = None
        
        for ar_raw, ur_raw in lines:
            ar = re.sub(r'<[^>]+>', '', ar_raw).strip()
            ur = re.sub(r'<[^>]+>', '', ur_raw).strip() if ur_raw else ''
            
            # Check if this line is an exercise header
            # Pattern: 1-, 2-, تمرين, تمارين, ضع, املأ, تأمل, etc.
            is_hdr = bool(re.match(r'^(?:[🔹🐪👁️🚪📚⌚\s]*)(?:\(\d+\)|\d+[\-\.]|\(\s*[أ-ي]\s*\)|تمرين|تمارين|التدريب)', ar))
            if is_hdr and ('أجب' in ar or 'تأمل' in ar or 'ضع' in ar or 'أدخل' in ar or 'اقرأ' in ar or 'املأ' in ar or 'حوّل' in ar or 'هات' in ar or 'صُغ' in ar or 'تمرين' in ar or 'تمارين' in ar or 'كوّن' in ar or 'عَيّن' in ar or 'مَيّز' in ar):
                current_ex = {
                    'header_ar': ar,
                    'header_ur': ur,
                    'items': []
                }
                exercises.append(current_ex)
            elif current_ex is not None:
                # If we hit vocab section, stop
                if 'الكلمات الجديدة' in ar:
                    current_ex = None
                    continue
                # Add item to current exercise
                if ar and not re.match(r'^[=\-•\s]+$', ar):
                    current_ex['items'].append((ar, ur))
        
        book_ex[uid] = {
            'title': title,
            'exercises': exercises
        }
        total_items = sum(len(e['items']) for e in exercises)
        print(f"{uid:8} ({title[:30]}): {len(exercises)} exercises, {total_items} total exercise items")

    return book_ex

b1_ex = parse_book_exercises('transcriptions/Madinah-Book-1.html', 1)
b2_ex = parse_book_exercises('transcriptions/Madinah-Book-2.html', 2)
b3_ex = parse_book_exercises('transcriptions/Madinah-Book-3.html', 3)
