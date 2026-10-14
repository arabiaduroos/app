import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def extract_all_book_tamreens(b_num):
    content = open(f'transcriptions/Madinah-Book-{b_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    
    book_exs = {}
    
    for s_id, s_html in sections:
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            continue
            
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        # Split into divs
        divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
        
        unit_tamreens = []
        cur_t = None
        
        for c, inner in divs:
            clean = re.sub(r'<[^>]+>', ' ', inner).strip()
            # Remove emojis and bullet points
            stripped = re.sub(r'^[^\w\s\(\)\[\]\u0600-\u06ff]+', '', clean).strip()
            stripped = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+', '', stripped).strip()
            
            # Check for exercise header like:
            # 1- أجب عن الأسئلة الآتية
            # 2- صحح ما يلي
            # تمرين (1)
            # ✍️ تمارين
            m_num = re.match(r'^(?:تمرين\s*)?([۱-۹\d]+)[\-\.\)]\s*(.*)', stripped)
            is_tamreen_start = bool(re.match(r'^(✍️\s*تـ?مارين|التَّمْرِينُ|التمارين)', stripped))
            is_cmd = any(stripped.startswith(w) for w in ['أَجِبْ', 'أجب', 'عَيِّنْ', 'عيّن', 'امْلَأْ', 'املأ', 'حَوِّلْ', 'حوّل', 'صَحِّحْ', 'صحّح', 'هَاتِ', 'هات', 'اخْتَرْ', 'اختر', 'أَدْخِلْ', 'أدخل', 'كَوِّنْ', 'كوّن', 'صِلْ', 'صل', 'ضَعْ', 'ضع', 'ابْنِ', 'ابن', 'اسْتَخْرِجْ', 'استخرج', 'أَعْرِبْ', 'أعرب', 'صُغْ', 'صغ', 'تَأَمَّلْ', 'تأمل']) and len(stripped) > 8 and not re.match(r'^\([1-9\d]\)', stripped)
            
            if m_num:
                t_idx = int(m_num.group(1).replace('۱','1').replace('۲','2').replace('۳','3').replace('۴','4').replace('۵','5').replace('۶','6').replace('۷','7').replace('۸','8').replace('۹','9'))
                instr = m_num.group(2).strip()
                if cur_t:
                    unit_tamreens.append(cur_t)
                cur_t = {
                    'num': t_idx,
                    'header': clean,
                    'instr': instr or clean,
                    'is_iqra': bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', clean)),
                    'items': []
                }
            elif (is_cmd or is_tamreen_start) and not cur_t:
                cur_t = {
                    'num': len(unit_tamreens) + 1,
                    'header': clean,
                    'instr': clean,
                    'is_iqra': bool(re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', clean)),
                    'items': []
                }
            elif cur_t:
                # If it's another numbered exercise
                if 'الكلمات الجديدة' in clean or c == 'vocab-table':
                    unit_tamreens.append(cur_t)
                    cur_t = None
                elif clean and clean != cur_t['header'] and len(clean) > 2:
                    cur_t['items'].append(clean)
                    
        if cur_t:
            unit_tamreens.append(cur_t)
            
        book_exs[s_id] = {
            'title': title,
            'tamreens': unit_tamreens
        }
        
    return book_exs

for b in [1, 2, 3]:
    b_data = extract_all_book_tamreens(b)
    print(f"\n====================== BOOK {b} ({len(b_data)} units) ======================")
    for sid, info in list(b_data.items())[:6]:
        non_iqra = [t for t in info['tamreens'] if not t['is_iqra']]
        print(f"{sid} ({info['title']}): Total {len(info['tamreens'])} Tamreens, {len(non_iqra)} non-iqra")
        for t in non_iqra:
            print(f"    Tamreen {t['num']}: {t['header'][:50]} ({len(t['items'])} items)")
