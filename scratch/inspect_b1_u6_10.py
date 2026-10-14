import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-1.html', encoding='utf-8').read()
sections = re.findall(r'<section[^>]*id=[\"\'](b1_u[6-9]|b1_u10)[\"\']>(.*?)</section>', content, re.DOTALL)

for s_id, s_html in sections:
    t_m = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
    title = re.sub(r'<[^>]+>', '', t_m.group(1)).strip() if t_m else s_id
    divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', s_html, re.DOTALL)
    print(f"\n==========================================")
    print(f"{s_id}: {title}")
    print(f"==========================================")
    for c, inner in divs:
        clean = re.sub(r'<[^>]+>', ' ', inner).strip()
        first = clean.split('\n')[0].strip()
        if re.search(r'^(✍️\s*)?(تـمـــــارين|تَمَارِين|تمرين|التَّمْرِين|\(?[۱-۹\d]+[\)\-\.]\s*)', first):
            print(f"[{c}] {clean[:100]}")
