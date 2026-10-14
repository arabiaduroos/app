import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for b_num in [1, 2, 3]:
    fname = f'transcriptions/Madinah-Book-{b_num}.html'
    content = open(fname, encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)
    print(f"\n==========================================")
    print(f"       BOOK {b_num}: {len(sections)} SECTIONS")
    print(f"==========================================")
    for s_id, s_html in sections[:5]:
        title_match = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip() if title_match else s_id
        
        # Find exercises / headings inside this section
        ex_headers = re.findall(r'<div class=[\"\']sec-hdr[\"\']>(.*?)</div>', s_html)
        if not ex_headers:
            ex_headers = re.findall(r'<div>(✍️\s*(?:تـمـــــارين|تَمَارِين|تمرين|التَّمْرِين)[^<]*)</div>', s_html)
        print(f"\n  Section: {s_id} | Title: {title}")
        print(f"    Exercise headers found ({len(ex_headers)}):")
        for eh in ex_headers[:6]:
            clean_eh = re.sub(r'<[^>]+>', ' ', eh).strip()
            print(f"      - {clean_eh}")
