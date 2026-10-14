import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)

print("BOOK 2 SECTIONS:")
for s_idx, (s_id, s_html) in enumerate(sections, 1):
    if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
        print(f"Skipping muqaddima: {s_id}")
        continue
    t_m = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
    title = re.sub(r'<[^>]+>', '', t_m.group(1)).strip() if t_m else s_id
    
    # Extract headers
    lines = [re.sub(r'<[^>]+>', ' ', d).strip() for d in re.findall(r'<div class=[\"\'](?:txt-line|sec-hdr)[\"\']>(.*?)</div>', s_html, re.DOTALL)]
    ex_hdrs = []
    for l in lines:
        l_first = l.split('\n')[0].strip()
        m = re.match(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*([۱-۹\d]+)[\-\.]\s*(.+)', l_first)
        if m and len(m.group(2)) > 5 and not re.match(r'^\(?\d', m.group(2)):
            ex_hdrs.append(f"{m.group(1)}- {m.group(2)[:50]}")
        elif '✍️ تم' in l_first or 'تمرين' in l_first:
            ex_hdrs.append(l_first[:50])
            
    print(f"Unit {s_idx-1} [{s_id}] {title}: {len(ex_hdrs)} exercise headers")
    for h in ex_hdrs[:6]:
        print(f"    * {h}")
