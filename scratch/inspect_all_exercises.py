import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def analyze_html_book(b_num):
    content = open(f'transcriptions/Madinah-Book-{b_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)
    
    book_data = []
    
    for s_id, s_html in sections:
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            continue
            
        t_m = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', t_m.group(1)).strip() if t_m else s_id
        
        # We want to identify every single exercise block
        # In the HTML, exercises are inside div class='txt-line' or 'sec-hdr' or 'dlg-row'
        divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', s_html, re.DOTALL)
        
        ex_list = []
        cur_ex = None
        
        for c, inner in divs:
            clean = re.sub(r'<[^>]+>', ' ', inner).strip()
            # clean may contain Urdu translations or emojis
            first_line = clean.split('\n')[0].strip()
            
            # Check if this div signals a new exercise
            # Pattern: 1-, 2-, (1), تمرين (1), ✍️ تـمـارين, etc.
            is_new_ex = False
            ex_header_text = ""
            
            # Match "1- ..." or "تمرين 1" or "التَّمْرِينُ الْأَوَّلُ" or "تمرين (1)"
            m_num = re.match(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*(\([۱-۹\d]+\)|[۱-۹\d]+[\-\.\)])\s*(.+)', first_line)
            m_tamreen = re.match(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*(التَّمْرِينُ|تمرين|تَمْرِين|تدريب|التدريب)\s*(\([۱-۹\d]+\)|[۱-۹\d]+)?[:\s]*(.*)', first_line)
            
            # Also verbs starting instructions
            m_verb = re.match(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*(أَجِبْ|عَيِّنْ|امْلَأْ|حَوِّلْ|تَأَمَّلْ|اقْرَأْ|صَحِّحْ|هَاتِ|اخْتَرْ|أَدْخِلْ|كَوْن|صِلْ|ضَعْ|ابْنِ|اسْتَخْرِجْ|صَغِّر|أَكْمِلْ)\s*(.*)', first_line)
            
            if m_num:
                num_str = m_num.group(1)
                rest = m_num.group(2).strip()
                # Check if it's a subquestion like "(1) من أين أنت؟" inside an existing exercise
                # Subquestions usually have question marks or are short noun phrases
                if cur_ex and re.match(r'^\([1-9\d]+\)', num_str) and not re.search(r'أجب|عين|امْلَأ|حول|تأمل|اقرأ|صحح|هات|اختر|أدخل|كون|صل|ضع|ابن|استخرج', rest):
                    # Subquestion
                    cur_ex['items'].append(first_line)
                else:
                    is_new_ex = True
                    ex_header_text = first_line
            elif m_tamreen:
                is_new_ex = True
                ex_header_text = first_line
            elif m_verb and len(first_line) > 10:
                # Could be exercise if it starts with an imperative verb and cur_ex doesn't have this header
                if not cur_ex or (cur_ex and first_line not in cur_ex['header']):
                    is_new_ex = True
                    ex_header_text = first_line
                    
            if is_new_ex:
                if cur_ex:
                    ex_list.append(cur_ex)
                cur_ex = {
                    'header': ex_header_text,
                    'is_iqra': bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', ex_header_text)),
                    'items': []
                }
            elif cur_ex:
                if 'الكلمات الجديدة' in clean or c == 'vocab-table':
                    ex_list.append(cur_ex)
                    cur_ex = None
                elif clean and clean != cur_ex['header'] and len(clean) > 1:
                    cur_ex['items'].append(clean)
                    
        if cur_ex:
            ex_list.append(cur_ex)
            
        book_data.append({
            'unit_id': s_id,
            'title': title,
            'exercises': ex_list
        })
        
    return book_data

for b in [1, 2, 3]:
    b_data = analyze_html_book(b)
    total_non_iqra = sum(len([e for e in u['exercises'] if not e['is_iqra']]) for u in b_data)
    print(f"Book {b}: {len(b_data)} units, {total_non_iqra} non-iqra exercises")
