import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def analyze_book_tamreens(b_num):
    content = open(f'transcriptions/Madinah-Book-{b_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)
    
    print(f"\n==========================================")
    print(f"       ANALYZING BOOK {b_num}")
    print(f"==========================================")
    
    for s_id, s_html in sections:
        if 'مُقَدِّمَة' in s_html[:500]:
            continue
        title_m = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else s_id
        
        # Look for numbered exercises within this section
        divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', s_html, re.DOTALL)
        
        exercises = []
        for c, inner in divs:
            clean = re.sub(r'<[^>]+>', ' ', inner).strip()
            clean_ar = clean.split('\n')[0].strip()
            # Match lines like "1- أجب عن الأسئلة" or "تمرين (1)" or "تأمل"
            m = re.match(r'^[🐪👨‍🎓👨‍🏫📖👁️🔹✍️\s]*([۱-۹\d]+)[\-\.]\s*(.*)', clean_ar)
            if m:
                num = m.group(1)
                text = m.group(2).strip()
                if len(text) > 4 and not re.match(r'^\(?\d', text):
                    exercises.append((num, text))
            elif '✍️ تمرين' in clean_ar or '✍️ تمـرين' in clean_ar:
                exercises.append(('T', clean_ar))
                
        print(f"\n{s_id}: {title} -> {len(exercises)} numbered exercises")
        seen = set()
        for num, text in exercises:
            if text[:40] not in seen:
                seen.add(text[:40])
                print(f"   [{num}] {text[:65]}")

analyze_book_tamreens(2)
analyze_book_tamreens(3)
