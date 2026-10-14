import sys, re
sys.stdout.reconfigure(encoding='utf-8')

b2_html = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
sec = re.search(r'<section[^>]*id=["\']b2_u27["\']>(.*?)</section>', b2_html, re.DOTALL).group(1)

divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', sec, re.DOTALL)
for cls, inner in divs:
    clean = re.sub(r'<[^>]+>', ' ', inner).strip()
    clean = re.sub(r'\s+', ' ', clean)
    if cls not in ['ur', 'en']:
        print(f"[{cls}]: {clean[:80]}")
