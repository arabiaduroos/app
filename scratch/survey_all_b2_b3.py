import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def survey(b_num):
    content = open(f'transcriptions/Madinah-Book-{b_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    print(f"\n================ BOOK {b_num} (Sections: {len(sections)}) ================")
    
    for s_id, s_html in sections:
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            print(f"Skipping Muqaddima: {s_id}")
            continue
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        # Look for tamreen headers
        # in HTML, tamreens are often in <div class="txt-line"> or similar
        lines = re.findall(r'<div class=["\'](?:txt-line|ar|heading|ar-title)[^"\']*["\']>(.*?)</div>', s_html)
        tamreens = []
        for l in lines:
            txt = re.sub(r'<[^>]+>', '', l).strip()
            # Look for numbered exercise like "1-", "2-", "تمرين", "تمارين", etc.
            if re.match(r'^(✍️\s*تـ?مارين|[۱-۹\d]+[\-\.\)]\s*[\u0600-\u06ff]|تمرين\s*\([۱-۹\d]+\))', txt):
                tamreens.append(txt)
            elif any(txt.startswith(w) for w in ['أَجِبْ', 'عَيِّنْ', 'امْلَأْ', 'حَوِّلْ', 'تَأَمَّلْ', 'اقْرَأْ وَاكْتُبْ', 'صَحِّحْ', 'هَاتِ', 'اخْتَرْ', 'أَدْخِلْ', 'كَوِّنْ']):
                if len(txt) > 8 and not re.match(r'^\([1-9\d]\)', txt):
                    tamreens.append(txt)
                    
        print(f"{s_id:8s}: {title[:35]:35s} -> Found {len(tamreens)} potential Tamreens")
        for idx, t in enumerate(tamreens[:5], 1):
            is_iqra = 'اقرأ واكتب' in t or 'اِقْرَأْ وَاكْتُبْ' in t
            flag = "[SKIP IQRA]" if is_iqra else "[KEEP]"
            print(f"     {flag} {idx}: {t[:60]}")

survey(2)
survey(3)
