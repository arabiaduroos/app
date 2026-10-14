import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def get_exercises_for_book(b_num):
    fname = f'transcriptions/Madinah-Book-{b_num}.html'
    content = open(fname, encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)
    
    book_results = []
    
    for s_id, s_html in sections:
        # Check if muqaddima
        if 'مُقَدِّمَة' in s_html[:500]:
            continue
            
        title_match = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip() if title_match else s_id
        
        # Split section into divs
        divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', s_html, re.DOTALL)
        
        exercises = []
        current_ex = None
        
        for c, inner in divs:
            clean = re.sub(r'<[^>]+>', ' ', inner).strip()
            clean_ar = clean.split('\n')[0].strip()
            
            # Check if this div is an exercise header
            is_hdr = c == 'sec-hdr' or bool(re.search(r'^(✍️\s*)?(تـمـــــارين|تَمَارِين|تمرين|التَّمْرِين|تمرین|تدريب)', clean))
            is_new_num = bool(re.search(r'^\(?[۱-۹\d]+[\)\-\.]\s*(أَجِبْ|عَيِّنْ|امْلَأْ|حَوِّلْ|تَأَمَّلْ|اقْرَأْ|صَحِّحْ|هَاتِ|اخْتَرْ|أَدْخِلْ|كَوْن|صِلْ|ضَعْ)', clean))
            
            if is_hdr or is_new_num:
                if current_ex and current_ex['items']:
                    exercises.append(current_ex)
                current_ex = {
                    'header': clean_ar,
                    'items': []
                }
            elif current_ex:
                if 'الكلمات الجديدة' in clean or c == 'vocab-table':
                    exercises.append(current_ex)
                    current_ex = None
                elif clean and clean != current_ex['header'] and not clean.startswith('(') and len(clean) > 2:
                    current_ex['items'].append(clean)
                elif clean and re.match(r'^\(?[\d۱-۹\)]', clean):
                    current_ex['items'].append(clean)
        
        if current_ex and current_ex['items']:
            exercises.append(current_ex)
            
        book_results.append({
            'section_id': s_id,
            'title': title,
            'exercises': exercises
        })
        
    return book_results

for b in [1, 2, 3]:
    res = get_exercises_for_book(b)
    print(f"\n==========================================")
    print(f"  BOOK {b}: {len(res)} UNITS")
    print(f"==========================================")
    for u in res:
        # filter out iqra waktub
        valid_ex = [e for e in u['exercises'] if not re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', e['header'])]
        print(f"Unit {u['section_id']}: {u['title']} -> {len(valid_ex)} non-iqra exercises (total {len(u['exercises'])})")
        for e_idx, e in enumerate(valid_ex, 1):
            print(f"    Ex {e_idx}: {e['header'][:60]} ({len(e['items'])} items)")
