import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def scan_all_book_units(book_num):
    content = open(f'transcriptions/Madinah-Book-{book_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    print(f"\n==================== BOOK {book_num} (Units: {len(sections)-1}) ====================")
    
    for s_idx, (s_id, s_html) in enumerate(sections, 1):
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            continue
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        lines = re.findall(r'<div class=["\'](?:txt-line|heading|ar-title|ur)[^"\']*["\']>(.*?)</div>', s_html)
        exs = []
        for l in lines:
            t = re.sub(r'<[^>]+>', ' ', l).strip()
            # Strip emojis and bullets from start
            t_clean = re.sub(r'^[^\w\s\(\)\[\]\u0600-\u06ff]+', '', t).strip()
            t_clean = re.sub(r'^[•\-\*🔹👁️🐪⚡✍️📋📖🚗🚪🏨]+', '', t_clean).strip()
            
            # Check if it starts with a number or exercise command
            if re.match(r'^(?:\([۱-۹\d]+\)|[۱-۹\d]+[\-\.\)]|تمرين\s*\([۱-۹\d]+\)|✍️\s*تـ?مارين)', t_clean):
                exs.append((t_clean, t))
            elif any(t_clean.startswith(w) for w in ['أَجِبْ', 'أجب', 'عَيِّنْ', 'عيّن', 'امْلَأْ', 'املأ', 'حَوِّلْ', 'حوّل', 'تَأَمَّلْ', 'تأمل', 'صَحِّحْ', 'صحّح', 'هَاتِ', 'هات', 'اخْتَرْ', 'اختر', 'أَدْخِلْ', 'أدخل', 'كَوِّنْ', 'كوّن', 'صِلْ', 'صل', 'ضَعْ', 'ضع', 'ابْنِ', 'ابن', 'اسْتَخْرِجْ', 'استخرج', 'أَعْرِبْ', 'أعرب', 'صُغْ', 'صغ']):
                if len(t_clean) > 6:
                    exs.append((t_clean, t))
        
        # Deduplicate consecutive duplicates (e.g. ar and ur versions)
        dedup = []
        for c, raw in exs:
            if not dedup or dedup[-1][0] != c:
                dedup.append((c, raw))
                
        print(f"\n>>> {s_id} | {title} (Exercises: {len(dedup)})")
        for i, (c, raw) in enumerate(dedup[:8], 1):
            is_iqra = 'اقرأ واكتب' in c or 'اِقْرَأْ وَاكْتُبْ' in c
            flag = "[SKIP IQRA]" if is_iqra else "[KEEP]"
            print(f"    {flag} {i}: {c[:65]}")

scan_all_book_units(2)
scan_all_book_units(3)
