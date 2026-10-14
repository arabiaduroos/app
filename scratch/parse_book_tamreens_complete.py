import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def parse_full_exercises(b_num):
    html = open(f'transcriptions/Madinah-Book-{b_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', html, re.DOTALL)
    
    units = []
    for s_id, s_html in sections:
        if 'مقدمة' in s_html[:400] or 'مُقَدِّمَة' in s_html[:400]:
            continue
            
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
        
        exercises = []
        cur_ex = None
        
        for cls, inner in divs:
            if cls in ['vocab-table']:
                if cur_ex:
                    exercises.append(cur_ex)
                    cur_ex = None
                continue
                
            clean = re.sub(r'<[^>]+>', ' ', inner).strip()
            clean = re.sub(r'\s+', ' ', clean)
            norm = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+\s*', '', clean).strip()
            
            if 'الكلمات الجديدة' in norm:
                if cur_ex:
                    exercises.append(cur_ex)
                    cur_ex = None
                continue
                
            # Exercise header detection:
            # 1- or (1) with command or تمرين (1) or 1.
            m1 = re.match(r'^([۱-۹\d]+)\s*[\-\.]\s*(.*)', norm)
            m2 = re.match(r'^(?:✍️\s*)?تمرين\s*\(?([۱-۹\d]+)\)?\s*[\:\-\.]?\s*(.*)', norm)
            m3 = re.match(r'^\(([۱-۹\d]+)\)\s*([أ-ي].*)', norm) if any(w in norm for w in ['أجب', 'ضع', 'املأ', 'حوّل', 'تأمل', 'اقرأ', 'صل', 'كون', 'عين', 'استخرج', 'هات']) else None
            
            m = m1 or m2 or m3
            
            if m and len(m.group(2).strip()) > 3:
                num = int(m.group(1).replace('۱','1').replace('۲','2').replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6').replace('۷','7').replace('۸','8').replace('۹','9'))
                instr = m.group(2).strip()
                is_iqra = bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', norm))
                
                # Check if duplicate from translation
                if cur_ex and cur_ex['num'] == num and (cls in ['ur', 'en'] or instr in cur_ex['instr'] or cur_ex['instr'] in instr):
                    if cls == 'ur' and not cur_ex.get('instr_ur'):
                        cur_ex['instr_ur'] = instr
                    elif cls == 'en' and not cur_ex.get('instr_en'):
                        cur_ex['instr_en'] = instr
                    continue
                    
                if cur_ex:
                    exercises.append(cur_ex)
                    
                cur_ex = {
                    'num': num,
                    'instr': instr,
                    'is_iqra': is_iqra,
                    'items': []
                }
            elif cur_ex:
                if cls in ['ur', 'en']:
                    # Translation of previous item
                    if cur_ex['items']:
                        last = cur_ex['items'][-1]
                        if cls == 'ur' and 'ur' not in last:
                            last['ur'] = clean
                        elif cls == 'en' and 'en' not in last:
                            last['en'] = clean
                else:
                    if len(clean) > 2 and clean != cur_ex['instr']:
                        cur_ex['items'].append({'ar': clean})
                        
        if cur_ex:
            exercises.append(cur_ex)
            
        units.append({
            's_id': s_id,
            'title': title,
            'exercises': exercises
        })
    return units

for b in [1, 2, 3]:
    units = parse_full_exercises(b)
    print(f"\n================ Book {b}: {len(units)} Units ================")
    for u_idx, u in enumerate(units[:6]):
        non_iq = [e for e in u['exercises'] if not e['is_iqra']]
        print(f"Unit {u_idx+1} ({u['title'][:20]}): {len(non_iq)} non-iqra exercises")
        for e in non_iq:
            print(f"    Tamreen {e['num']}: {e['instr'][:40]} ({len(e['items'])} items)")
