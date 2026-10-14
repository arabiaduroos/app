import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def extract_unit_exercises(s_html):
    divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', s_html, re.DOTALL)
    exercises = []
    cur_ex = None
    
    for c, inner in divs:
        clean = re.sub(r'<[^>]+>', ' ', inner).strip()
        first = clean.split('\n')[0].strip()
        
        # Check if exercise header
        is_num = bool(re.match(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*(\([۱-۹\d]+\)|[۱-۹\d]+[\-\.\)])\s*(.+)', first))
        is_tamreen = '✍️ تـم' in first or '✍️ تم' in first or 'تمرين' in first or 'تَمَارِين' in first or 'التَّمْرِين' in first
        
        # Check if it's sub-question
        is_sub = bool(re.match(r'^\([1-9\d]+\)\s*[\u0600-\u06ff]', first)) and not is_num
        
        if (is_tamreen or (is_num and not is_sub)):
            # Check if this is a command verb or exercise intro
            if cur_ex:
                exercises.append(cur_ex)
            cur_ex = {
                'header': first,
                'is_iqra': bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', first)),
                'items': []
            }
        elif cur_ex:
            if 'الكلمات الجديدة' in first or c == 'vocab-table':
                exercises.append(cur_ex)
                cur_ex = None
            elif clean and clean != cur_ex['header'] and len(clean) > 1:
                cur_ex['items'].append(clean)
                
    if cur_ex:
        exercises.append(cur_ex)
        
    return [e for e in exercises if not e['is_iqra']]

for b_num in [1, 2, 3]:
    content = open(f'transcriptions/Madinah-Book-{b_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)
    
    total_u = 0
    total_ex = 0
    total_items = 0
    
    for s_id, s_html in sections:
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            continue
        total_u += 1
        exs = extract_unit_exercises(s_html)
        total_ex += len(exs)
        for e in exs:
            total_items += len(e['items'])
            
    print(f"Book {b_num}: {total_u} units, {total_ex} genuine exercises, {total_items} items")
