import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def analyze_book(b_num):
    html = open(f'transcriptions/Madinah-Book-{b_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', html, re.DOTALL)
    
    units = []
    for s_id, s_html in sections:
        if 'مقدمة' in s_html[:400] or 'مُقَدِّمَة' in s_html[:400]:
            continue
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
        
        # Scan exercises
        exercises = []
        cur_ex = None
        
        for cls, content in divs:
            clean = re.sub(r'<[^>]+>', ' ', content).strip()
            stripped = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+\s*', '', clean).strip()
            
            # Exercise numbered start:
            # 1- ... or تمرين (1) or 1. ... or (1) ...
            m = re.match(r'^(?:تمرين\s*)?([۱-۹\d]+)[\-\.\)]\s*(.*)', stripped)
            is_start_marker = bool(re.match(r'^(✍️\s*تـ?مارين|التَّمْرِينُ|التمارين)', stripped))
            
            # Check if command line like "أجب عن الأسئلة", "تأمل ما يلي", "املأ الفراغ"
            is_cmd = any(stripped.startswith(w) for w in [
                'أَجِبْ', 'أجب', 'عَيِّنْ', 'عيّن', 'امْلَأْ', 'املأ', 'حَوِّلْ', 'حوّل',
                'صَحِّحْ', 'صحّح', 'هَاتِ', 'هات', 'اخْتَرْ', 'اختر', 'أَدْخِلْ', 'أدخل',
                'كَوِّنْ', 'كوّن', 'صِلْ', 'صل', 'ضَعْ', 'ضع', 'ابْنِ', 'ابن', 'اسْتَخْرِجْ',
                'استخرج', 'أَعْرِبْ', 'أعرب', 'صُغْ', 'صغ', 'تَأَمَّلْ', 'تأمل', 'اقرأ المثال'
            ]) and len(stripped) > 8 and not re.match(r'^\([1-9\d]\)', stripped)
            
            if m:
                num = int(m.group(1).replace('۱','1').replace('۲','2').replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6').replace('۷','7').replace('۸','8').replace('۹','9'))
                instr = m.group(2).strip()
                is_iqra = bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', stripped))
                if cur_ex:
                    exercises.append(cur_ex)
                cur_ex = {
                    'num': num,
                    'instr': instr or stripped,
                    'is_iqra': is_iqra,
                    'items': []
                }
            elif is_cmd and not cur_ex:
                is_iqra = bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', stripped))
                cur_ex = {
                    'num': len(exercises) + 1,
                    'instr': stripped,
                    'is_iqra': is_iqra,
                    'items': []
                }
            elif cur_ex:
                if 'الكلمات الجديدة' in clean or cls == 'vocab-table':
                    exercises.append(cur_ex)
                    cur_ex = None
                elif clean and clean != cur_ex['instr'] and len(clean) > 2:
                    # filter out duplicated urdu/english subtitles if identical
                    if not (cls in ['ur', 'en'] and cur_ex['items'] and cur_ex['items'][-1] == clean):
                        cur_ex['items'].append(clean)
        if cur_ex:
            exercises.append(cur_ex)
            
        units.append({
            's_id': s_id,
            'title': title,
            'exercises': exercises
        })
    return units

for b in [2, 3]:
    units = analyze_book(b)
    print(f"\n================ BOOK {b} ({len(units)} units) ================")
    for u_idx, u in enumerate(units):
        non_iqra = [e for e in u['exercises'] if not e['is_iqra']]
        nums = [e['num'] for e in non_iqra]
        print(f"Unit {u_idx+1} ({u['title'][:20]}): {len(non_iqra)} non-iqra exercises: {nums}")
