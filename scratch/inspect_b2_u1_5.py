import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)

for s_id, s_html in sections[1:6]: # skip muqaddima (index 0)
    print(f"\n==========================================")
    print(f"Section: {s_id}")
    print(f"==========================================")
    divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', s_html, re.DOTALL)
    for c, inner in divs:
        clean = re.sub(r'<[^>]+>', ' ', inner).strip()
        first = clean.split('\n')[0].strip()
        if re.search(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*(\([۱-۹\d]+\)|[۱-۹\d]+[\-\.\)])\s*(.+)', first) or '✍️ تم' in first:
            print(f"[{c}] {first[:90]}")
