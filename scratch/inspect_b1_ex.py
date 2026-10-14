import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-1.html', encoding='utf-8').read()
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)

for s_id, s_html in sections[:10]:
    print(f"\n=== Section {s_id} ===")
    divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
    for cls, inner in divs:
        clean = re.sub(r'<[^>]+>', '', inner).strip()
        if any(w in clean for w in ['تمرين', 'تمارين', 'اقرأ', 'أجب', 'املأ', 'صل', 'ضع']):
            print(f"  [{cls}]: {clean[:60]}")
