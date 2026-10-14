import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
b2_u2 = re.search(r'<section[^>]*id=[\"\']b2_u2[\"\']>(.*?)</section>', content, re.DOTALL).group(1)

# Find all lines with numbers followed by dash
divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', b2_u2, re.DOTALL)
for c, inner in divs:
    clean = re.sub(r'<[^>]+>', ' ', inner).strip()
    clean_ar = clean.split('\n')[0].strip()
    m = re.match(r'^[🐪👨‍🎓👨‍🏫📖👁️🔹✍️\s]*([۱-۹\d]+)[\-\.]\s*(.*)', clean_ar)
    if m:
        num = m.group(1)
        rest = m.group(2)
        if len(rest) > 5 and not re.match(r'^\(?\d', rest):
            print(f"Exercise {num}: {rest[:80]}")
