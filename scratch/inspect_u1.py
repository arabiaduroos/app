import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for b in [1, 2, 3]:
    content = open(f'transcriptions/Madinah-Book-{b}.html', encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)
    print(f"\n================ Book {b} first 3 sections ================")
    for s_id, s_html in sections[:3]:
        divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
        print(f"\n--- {s_id} ({len(divs)} divs) ---")
        for cls, d in divs:
            txt = re.sub(r'<[^>]+>', '', d).strip()
            if any(w in txt for w in ['تمرين', 'تمارين', 'اقرأ', 'ما هذا', 'أجب', 'املأ', 'تأمل', 'حوّل', 'عين']):
                print(f"  [{cls}]: {txt[:80]}")
