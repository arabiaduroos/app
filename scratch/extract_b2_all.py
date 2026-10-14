import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def extract_unit_exercises(book_num):
    content = open(f'transcriptions/Madinah-Book-{book_num}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    
    results = {}
    
    for s_id, s_html in sections:
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            continue
            
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        
        # Get all lines
        divs = re.findall(r'<div class=["\'](?:txt-line|heading|ar-title)[^"\']*["\']>(.*?)</div>', s_html)
        if not divs:
            divs = re.findall(r'<div class=["\'](?:txt-line|ur)[^"\']*["\']>(.*?)</div>', s_html)
            
        clean_lines = [re.sub(r'<[^>]+>', ' ', d).strip() for d in divs]
        clean_lines = [l for l in clean_lines if l and not l.startswith('(') or any(c in l for c in 'أبتثجحخدذرزسشصضطظعغفقكلمنهوي')]
        
        results[s_id] = {
            'title': title,
            'lines_count': len(clean_lines),
            'sample_lines': clean_lines[:40]
        }
        
    return results

b2_data = extract_unit_exercises(2)
print(f"Book 2 units: {len(b2_data)}")
for sid, d in list(b2_data.items())[:10]:
    print(f"--- {sid}: {d['title']} ({d['lines_count']} lines) ---")
    for l in d['sample_lines'][:10]:
        if any(kw in l for kw in ['تمرين', 'تمارين', 'أجب', 'تأمل', 'عَيِّنْ', 'عيّن', 'اقرأ', 'هات', 'استخرج', 'ضع', 'املأ', 'حوّل', '1-', '2-', '3-', '4-']):
            print("   ", l[:80])
