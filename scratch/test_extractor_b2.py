import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def get_clean_text(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def extract_section_exercises(s_html):
    divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
    
    # Locate where exercises start
    # Usually indicated by sec-hdr with "تمارين" or first numbered line after lesson
    ex_list = []
    cur_ex = None
    
    in_exercises_zone = False
    
    for cls, inner in divs:
        if cls == 'vocab-table':
            if cur_ex:
                ex_list.append(cur_ex)
                cur_ex = None
            continue
            
        clean = get_clean_text(inner)
        norm = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+\s*', '', clean).strip()
        
        if 'الكلمات الجديدة' in norm:
            if cur_ex:
                ex_list.append(cur_ex)
                cur_ex = None
            in_exercises_zone = False
            continue
            
        if 'تمارين' in norm or 'التمارين' in norm or 'التَّمْرِينُ' in norm:
            in_exercises_zone = True
            
        # Match exercise start: e.g. "1- ", "2- ", "تمرين (1)"
        m1 = re.match(r'^([۱-۹\d]+)\s*[\-\.]\s*(.*)', norm)
        m2 = re.match(r'^(?:✍️\s*)?تمرين\s*\(?([۱-۹\d]+)\)?\s*[\:\-\.]?\s*(.*)', norm)
        
        # In Book 1/3, sometimes "(1) أجب..."
        m3 = None
        if in_exercises_zone and re.match(r'^\(([۱-۹\d]+)\)\s*([أ-ي].*)', norm):
            m_tmp = re.match(r'^\(([۱-۹\d]+)\)\s*([أ-ي].*)', norm)
            cmd_words = ['أجب', 'ضع', 'املأ', 'حوّل', 'تأمل', 'اقرأ', 'صل', 'كون', 'عين', 'استخرج', 'هات', 'صغر', 'أدخل']
            if any(cw in m_tmp.group(2) for cw in cmd_words):
                m3 = m_tmp
                
        m = m1 or m2 or m3
        
        if m and len(m.group(2).strip()) > 3:
            num = int(m.group(1).replace('۱','1').replace('۲','2').replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6').replace('۷','7').replace('۸','8').replace('۹','9'))
            instr = m.group(2).strip()
            
            # Skip if this is an item under current exercise (e.g. sub-items with parenthesis)
            if cur_ex and m1 and not in_exercises_zone:
                in_exercises_zone = True
                
            # Check if duplicate from ur/en
            if cur_ex and cur_ex['num'] == num and (cls in ['ur', 'en'] or instr == cur_ex['instr_ar']):
                if cls == 'ur':
                    cur_ex['instr_ur'] = instr
                elif cls == 'en':
                    cur_ex['instr_en'] = instr
                continue
                
            if cur_ex:
                ex_list.append(cur_ex)
                
            is_iqra = bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', norm))
            cur_ex = {
                'num': num,
                'instr_ar': instr,
                'instr_ur': '',
                'instr_en': '',
                'is_iqra': is_iqra,
                'items': []
            }
        elif cur_ex:
            if cls == 'ur':
                if cur_ex['items'] and 'ur' not in cur_ex['items'][-1]:
                    cur_ex['items'][-1]['ur'] = clean
                elif not cur_ex['instr_ur']:
                    cur_ex['instr_ur'] = clean
            elif cls == 'en':
                if cur_ex['items'] and 'en' not in cur_ex['items'][-1]:
                    cur_ex['items'][-1]['en'] = clean
                elif not cur_ex['instr_en']:
                    cur_ex['instr_en'] = clean
            else:
                if len(clean) > 2 and clean != cur_ex['instr_ar']:
                    cur_ex['items'].append({'ar': clean})
                    
    if cur_ex:
        ex_list.append(cur_ex)
        
    return ex_list

b2_html = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
sections = [s for s in re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', b2_html, re.DOTALL) if 'مقدمة' not in s[1][:400] and 'مُقَدِّمَة' not in s[1][:400]]

print(f"Total Book 2 sections: {len(sections)}")
for idx, (s_id, s_html) in enumerate(sections[:5]):
    exs = extract_section_exercises(s_html)
    non_iq = [e for e in exs if not e['is_iqra']]
    print(f"\nUnit {idx+1} ({s_id}): {len(non_iq)} non-iqra exercises")
    for e in non_iq:
        print(f"   Ex {e['num']}: {e['instr_ar'][:45]} | items: {len(e['items'])}")
