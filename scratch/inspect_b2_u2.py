import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
b2_u2 = re.search(r'<section[^>]*id=[\"\']b2_u2[\"\']>(.*?)</section>', content, re.DOTALL).group(1)

# Find all divs inside b2_u2
divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', b2_u2, re.DOTALL)
print(f"Total classed divs in b2_u2: {len(divs)}")
for c, inner in divs[:35]:
    clean = re.sub(r'<[^>]+>', ' ', inner).strip()
    if clean:
        print(f"[{c}] {clean[:90]}")
