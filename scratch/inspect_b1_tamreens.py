import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-1.html', encoding='utf-8').read()
sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)

for s_idx, (s_id, s_html) in enumerate(sections, 1):
    title_m = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else s_id
    
    divs = re.findall(r'<div class=[\"\']([^\"\']+)[\"\']>(.*?)</div>', s_html, re.DOTALL)
    print(f"\n==========================================")
    print(f"Book 1 Unit {s_idx} ({s_id}): {title}")
    print(f"==========================================")
    
    for c, inner in divs:
        clean = re.sub(r'<[^>]+>', ' ', inner).strip()
        clean_ar = clean.split('\n')[0].strip()
        if re.search(r'(تمرين|تَمْرِين|التَّمْرِين|تمارين|تدريب|اقرأ واكتب|امْلَأ|صل بين|ضع في الفراغ)', clean_ar):
            print(f"[{c}] {clean_ar[:80]}")
