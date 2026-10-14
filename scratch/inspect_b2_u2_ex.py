import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
b2_u2 = re.search(r'<section[^>]*id=[\"\']b2_u2[\"\']>(.*?)</section>', content, re.DOTALL).group(1)

divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', b2_u2, re.DOTALL)
for i, (c, inner) in enumerate(divs[35:85], 36):
    clean = re.sub(r'<[^>]+>', ' ', inner).strip()
    if clean:
        print(f"{i} [{c}] {clean[:100]}")
