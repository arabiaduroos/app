import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-3.html', encoding='utf-8').read()
m = re.search(r'<section[^>]*id=["\']b3_u2["\']>(.*?)</section>', content, re.DOTALL)
if m:
    s_html = m.group(1)
    lines = re.findall(r'<div class=["\']txt-line["\']>(.*?)</div>', s_html, re.DOTALL)
    for i in range(80, 120):
        if i < len(lines):
            clean = re.sub(r'<[^>]+>', ' ', lines[i]).strip()
            print(f"{i}: {clean}")
