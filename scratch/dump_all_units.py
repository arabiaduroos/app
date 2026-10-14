import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def dump_book_exercises(book_num):
    content = open(f'transcriptions/Madinah-Book-{book_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    print(f"\n==================== BOOK {book_num} ====================")
    
    for s_idx, (s_id, s_html) in enumerate(sections, 1):
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            continue
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        # Look for exercises
        lines = re.findall(r'<div class=["\'](?:txt-line|heading|ar-title|ur)[^"\']*["\']>(.*?)</div>', s_html)
        exs = []
        for l in lines:
            t = re.sub(r'<[^>]+>', ' ', l).strip()
            # If line starts with a number or contains tamreen keywords
            if re.match(r'^(?:[۱-۹\d]+[\-\.\)]\s*[\u0600-\u06ff]|✍️\s*تـ?مارين|تمرين\s*\([۱-۹\d]+\))', t):
                exs.append(t)
            elif any(t.startswith(w) for w in ['أَجِبْ', 'أجب', 'عَيِّنْ', 'عيّن', 'امْلَأْ', 'املأ', 'حَوِّلْ', 'حوّل', 'تَأَمَّلْ', 'تأمل', 'صَحِّحْ', 'صحّح', 'هَاتِ', 'هات', 'اخْتَرْ', 'اختر', 'أَدْخِلْ', 'أدخل', 'كَوِّنْ', 'كوّن', 'صِلْ', 'صل', 'ضَعْ', 'ضع', 'ابْنِ', 'ابن', 'اسْتَخْرِجْ', 'استخرج']):
                if len(t) > 6 and not re.match(r'^\([1-9\d]\)', t):
                    exs.append(t)
        
        print(f"\n>>> {s_id} | {title} (Found {len(exs)} exercises)")
        for i, ex in enumerate(exs, 1):
            is_iqra = 'اقرأ واكتب' in ex or 'اِقْرَأْ وَاكْتُبْ' in ex
            tag = "[SKIP IQRA]" if is_iqra else "[KEEP]"
            print(f"    {tag} ({i}) {ex[:70]}")

dump_book_exercises(2)
dump_book_exercises(3)
