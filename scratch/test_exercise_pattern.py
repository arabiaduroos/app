import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for b in [1, 2, 3]:
    content = open(f'transcriptions/Madinah-Book-{b}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    
    print(f"\n================ BOOK {b} ================")
    for s_id, s_html in sections:
        if 'مقدمة' in s_html[:400] or 'مُقَدِّمَة' in s_html[:400]:
            continue
            
        divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
        
        ex_headers = []
        for cls, inner in divs:
            if cls in ['ur', 'en']:
                continue
            clean = re.sub(r'<[^>]+>', '', inner).strip()
            norm = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+\s*', '', clean).strip()
            
            # Pattern: 1- or تمرين (1) or 1.
            m1 = re.match(r'^([۱-۹\d]+)\s*[\-\.]\s*(.*)', norm)
            m2 = re.match(r'^تمرين\s*\(?([۱-۹\d]+)\)?\s*[\:\-\.]?\s*(.*)', norm)
            
            if m1:
                num = int(m1.group(1).replace('۱','1').replace('۲','2').replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6').replace('۷','7').replace('۸','8').replace('۹','9'))
                instr = m1.group(2).strip()
                if len(instr) > 2:
                    ex_headers.append((num, instr, bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', norm))))
            elif m2:
                num = int(m2.group(1).replace('۱','1').replace('۲','2').replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6').replace('۷','7').replace('۸','8').replace('۹','9'))
                instr = m2.group(2).strip()
                ex_headers.append((num, instr or 'تمرين', bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', norm))))
                
        # Deduplicate consecutive identical numbers
        dedup = []
        for num, instr, iq in ex_headers:
            if not dedup or dedup[-1][0] != num:
                dedup.append((num, instr, iq))
                
        non_iqra = [e for e in dedup if not e[2]]
        print(f"[{s_id}]: {len(dedup)} total exercises, {len(non_iqra)} non-iqra. Numbers: {[e[0] for e in non_iqra]}")
