import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
# Find sections
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', content, re.DOTALL)

for s_id, s_html in sections[1:4]:
    print(f"\n=== Section: {s_id} ===")
    divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
    for cls, inner in divs:
        clean = re.sub(r'<[^>]+>', '', inner).strip()
        if any(kw in clean for kw in ['تمرين', 'تمارين', 'أجب عن', 'تأمل ما', 'املأ', 'حوّل', 'أدخل', 'صل', 'كون']):
            print(f"  Class: [{cls}] -> {clean[:80]}")
