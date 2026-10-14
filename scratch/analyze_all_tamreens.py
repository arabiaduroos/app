import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

for b in [1, 2, 3]:
    content = open(f'transcriptions/Madinah-Book-{b}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    print(f"\n=================== BOOK {b} ({len(sections)} sections) ===================")
    unit_idx = 0
    for s_id, s_html in sections:
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            continue
        unit_idx += 1
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        # Find all divs
        divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
        
        # Scan for exercise markers
        tamreens = []
        cur_t = None
        for cls, d_inner in divs:
            clean = re.sub(r'<[^>]+>', ' ', d_inner).strip()
            clean_no_emoji = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+\s*', '', clean).strip()
            
            # Exercise header detection:
            # 1- ...
            # تمرين (1)
            # 1. ...
            m = re.match(r'^(?:تمرين\s*)?([۱-۹\d]+)[\-\.\)]\s*(.*)', clean_no_emoji)
            if m:
                t_num = int(m.group(1).replace('۱','1').replace('۲','2').replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6').replace('۷','7').replace('۸','8').replace('۹','9'))
                instr = m.group(2).strip()
                if cur_t:
                    tamreens.append(cur_t)
                cur_t = {
                    'num': t_num,
                    'instr': instr or clean_no_emoji,
                    'is_iqra': bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', clean_no_emoji)),
                    'items': []
                }
            elif cur_t:
                if 'الكلمات الجديدة' in clean or cls == 'vocab-table':
                    tamreens.append(cur_t)
                    cur_t = None
                elif clean and len(clean) > 2 and clean != cur_t['instr']:
                    cur_t['items'].append(clean)
        if cur_t:
            tamreens.append(cur_t)
            
        non_iqra = [t for t in tamreens if not t['is_iqra']]
        print(f"Unit {unit_idx} [{s_id}] ({title[:25]}): {len(tamreens)} total tamreens, {len(non_iqra)} non-iqra")
        for t in non_iqra:
            print(f"   Ex {t['num']}: {t['instr'][:45]} ({len(t['items'])} items)")
