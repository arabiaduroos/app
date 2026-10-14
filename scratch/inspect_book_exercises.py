import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

for b in [1, 2, 3]:
    html = open(f'transcriptions/Madinah-Book-{b}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', html, re.DOTALL)
    
    print(f"\n==========================================")
    print(f"       ANALYSIS OF BOOK {b}")
    print(f"==========================================")
    
    for s_id, s_html in sections:
        if 'مقدمة' in s_html[:400] or 'مُقَدِّمَة' in s_html[:400]:
            continue
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        # Get all divs
        divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
        
        print(f"\n[{s_id}] {title}")
        
        # Look for exercises
        current_tamreen = None
        for cls, content in divs:
            clean = re.sub(r'<[^>]+>', ' ', content).strip()
            # Clean emoji/bullets at start
            norm = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+\s*', '', clean).strip()
            
            # Check if this div is an exercise title / instruction
            # e.g.: "1- أجب عن الأسئلة الآتية:", "تمرين (1)", "2- اقرأ المثال ثم...", "املأ الفراغ..."
            is_num_ex = re.match(r'^(?:تمرين\s*)?([۱-۹\d]+)[\-\.\)]\s*(.*)', norm)
            is_general_ex = (cls in ['exercise-title', 'tamreen-title'] or 'تمارين' in norm or 'التَّمْرِينُ' in norm)
            
            if is_num_ex:
                t_num = is_num_ex.group(1)
                t_instr = is_num_ex.group(2)
                is_iqra = bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', norm))
                current_tamreen = f"Tamreen {t_num}: {t_instr[:40]}... (is_iqra={is_iqra})"
                print(f"   --> {current_tamreen}")
            elif is_general_ex and not current_tamreen:
                is_iqra = bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', norm))
                current_tamreen = f"Exercise: {norm[:40]}... (is_iqra={is_iqra})"
                print(f"   --> {current_tamreen}")
            elif 'الكلمات الجديدة' in norm:
                current_tamreen = None
