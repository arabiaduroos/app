import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def extract_unit_exercises(book_num):
    content = open(f'transcriptions/Madinah-Book-{book_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    
    units_data = []
    
    for s_id, s_html in sections:
        if 'مقدمة' in s_html[:400] or 'مُقَدِّمَة' in s_html[:400]:
            continue
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        # Parse divs
        divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
        
        exercises = []
        cur_ex = None
        
        for cls, d_html in divs:
            clean = re.sub(r'<[^>]+>', ' ', d_html).strip()
            clean = re.sub(r'\s+', ' ', clean)
            norm = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+\s*', '', clean).strip()
            
            # Check for exercise header
            # Formats in files:
            # 1- أجب عن الأسئلة الآتية
            # (1) عين المعرب من المبني
            # تمرين (1)
            # 1. ...
            m_num = re.match(r'^(?:تمرين\s*)?([۱-۹\d]+)[\-\.\)]\s*(.*)', norm)
            if not m_num:
                m_num = re.match(r'^\(([۱-۹\d]+)\)\s*(.*)', norm)
                
            is_start_keyword = any(norm.startswith(k) for k in [
                'أَجِبْ', 'أجب', 'عَيِّنْ', 'عيّن', 'امْلَأْ', 'املأ', 'حَوِّلْ', 'حوّل',
                'صَحِّحْ', 'صحّح', 'هَاتِ', 'هات', 'اخْتَرْ', 'اختر', 'أَدْخِلْ', 'أدخل',
                'كَوِّنْ', 'كوّن', 'صِلْ', 'صل', 'ضَعْ', 'ضع', 'ابْنِ', 'ابن', 'اسْتَخْرِجْ',
                'استخرج', 'أَعْرِبْ', 'أعرب', 'صُغْ', 'صغ', 'تَأَمَّلْ', 'تأمل', 'اقرأ المثال'
            ]) and len(norm) > 10 and not re.match(r'^\([1-9\d]\)\s*$', norm)
            
            is_iqra = bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', norm))
            
            if m_num and len(m_num.group(2).strip()) > 3:
                num = int(m_num.group(1).replace('۱','1').replace('۲','2').replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6').replace('۷','7').replace('۸','8').replace('۹','9'))
                instr = m_num.group(2).strip()
                
                # Check if duplicate header from ur/en
                if cur_ex and cur_ex['num'] == num and (instr in cur_ex['instr'] or cur_ex['instr'] in instr):
                    continue
                    
                if cur_ex:
                    exercises.append(cur_ex)
                cur_ex = {
                    'num': num,
                    'instr': instr,
                    'is_iqra': is_iqra,
                    'items': []
                }
            elif is_start_keyword and not cur_ex:
                cur_ex = {
                    'num': len(exercises) + 1,
                    'instr': norm,
                    'is_iqra': is_iqra,
                    'items': []
                }
            elif cur_ex:
                if 'الكلمات الجديدة' in norm or cls == 'vocab-table':
                    exercises.append(cur_ex)
                    cur_ex = None
                elif norm and norm != cur_ex['instr'] and len(norm) > 2:
                    # Ignore pure duplicates
                    if not (cur_ex['items'] and cur_ex['items'][-1] == norm):
                        cur_ex['items'].append(norm)
                        
        if cur_ex:
            exercises.append(cur_ex)
            
        units_data.append({
            's_id': s_id,
            'title': title,
            'exercises': exercises
        })
    return units_data

for b in [1, 2, 3]:
    units = extract_unit_exercises(b)
    print(f"\n====================== BOOK {b}: {len(units)} Units ======================")
    for u_idx, u in enumerate(units):
        non_iq = [e for e in u['exercises'] if not e['is_iqra']]
        print(f"Unit {u_idx+1} ({u['title'][:25]}): {len(non_iq)} valid exercises (Numbers: {[e['num'] for e in non_iq]})")
        for e in non_iq[:3]:
            print(f"    Ex {e['num']}: {e['instr'][:50]} | items: {len(e['items'])}")
