import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def parse_book(b_num):
    fname = f'transcriptions/Madinah-Book-{b_num}.html'
    content = open(fname, encoding='utf-8').read()
    
    sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)
    print(f"\n=======================================================")
    print(f" BOOK {b_num}: Total sections: {len(sections)}")
    print(f"=======================================================")
    
    units_info = []
    
    for s_idx, (s_id, s_html) in enumerate(sections, 1):
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            print(f"  [Skipping Muqaddima: {s_id}]")
            continue
            
        title_m = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else s_id
        
        # Extract all text lines and divs
        divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', s_html, re.DOTALL)
        
        # Look for exercises
        exercises = []
        current_ex = None
        
        for c, inner in divs:
            clean = re.sub(r'<[^>]+>', ' ', inner).strip()
            clean_ar = clean.split('\n')[0].strip()
            
            # Check if this div is an exercise header
            # Examples:
            # 1- أجب عن الأسئلة الآتية
            # 2- ضع علامة (صح)
            # ✍️ تـمـــــارين
            # تمرين (1)
            # اقرأ واكتب
            # أَدْخِلْ
            # كَوِّنْ
            
            is_num_ex = bool(re.match(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*(\([۱-۹\d]+\)|[۱-۹\d]+[\-\.\)])\s*(.*)', clean_ar))
            is_tamreen_tag = '✍️ تـم' in clean_ar or '✍️ تم' in clean_ar or 'التَّمْرِينُ' in clean_ar or 'تَمَارِين' in clean_ar or 'تمرين' in clean_ar
            is_new_instr = bool(re.match(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*(أَجِبْ|عَيِّنْ|امْلَأْ|حَوِّلْ|تَأَمَّلْ|اقْرَأْ|صَحِّحْ|هَاتِ|اخْتَرْ|أَدْخِلْ|كَوْن|صِلْ|ضَعْ|صِلْ|ابْنِ|اسْتَخْرِجْ)', clean_ar))
            
            # If it's a sub-question like (1) من أين هاشم؟, that belongs inside the exercise
            is_sub_q = bool(re.match(r'^\([1-9\d]\)\s*[\u0600-\u06ff]', clean_ar)) and not is_num_ex
            
            if is_tamreen_tag or (is_num_ex and not is_sub_q) or (is_new_instr and len(clean_ar) > 5 and not is_sub_q):
                if current_ex and current_ex['lines']:
                    exercises.append(current_ex)
                current_ex = {
                    'header': clean_ar,
                    'is_iqra': bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', clean_ar)),
                    'lines': []
                }
            elif current_ex:
                if 'الكلمات الجديدة' in clean_ar or c == 'vocab-table':
                    exercises.append(current_ex)
                    current_ex = None
                elif clean and clean != current_ex['header'] and len(clean) > 1:
                    current_ex['lines'].append(clean)
                    
        if current_ex and current_ex['lines']:
            exercises.append(current_ex)
            
        units_info.append({
            'section_id': s_id,
            'title': title,
            'exercises': exercises
        })
        
    return units_info

for b in [1, 2, 3]:
    units = parse_book(b)
    print(f"Book {b}: parsed {len(units)} units")
    for u in units[:5]:
        non_iqra = [e for e in u['exercises'] if not e['is_iqra']]
        print(f"  {u['section_id']} ({u['title']}): {len(u['exercises'])} total exercises, {len(non_iqra)} non-iqra")
        for idx, e in enumerate(non_iqra, 1):
            print(f"      Ex {idx}: {e['header'][:50]} ({len(e['lines'])} lines)")
