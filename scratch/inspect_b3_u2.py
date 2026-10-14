import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-3.html', encoding='utf-8').read()
m = re.search(r'<section[^>]*id=["\']b3_u2["\']>(.*?)</section>', content, re.DOTALL)
if m:
    s_html = m.group(1)
    divs = re.findall(r'<div class=["\']([^"\']+)["\']>(.*?)</div>', s_html, re.DOTALL)
    print(f"b3_u2 div count: {len(divs)}")
    classes = set(c for c, _ in divs)
    print("classes:", classes)
    for idx, (c, text) in enumerate(divs[:25]):
        clean = re.sub(r'<[^>]+>', ' ', text).strip()
        print(f"{idx} [{c}]: {clean[:80]}")
