import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

for b_num in [1, 2, 3]:
    fname = f'transcriptions/Madinah-Book-{b_num}.html'
    content = open(fname, encoding='utf-8').read()
    sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']>(.*?)</section>', content, re.DOTALL)
    
    print(f"\n=======================================================")
    print(f"               BOOK {b_num} TAMREEN SURVEY")
    print(f"=======================================================")
    
    unit_count = 0
    for s_id, s_html in sections:
        if 'مُقَدِّمَة' in s_html[:400] or 'مقدمة' in s_html[:400]:
            continue
        unit_count += 1
        t_m = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
        title = re.sub(r'<[^>]+>', '', t_m.group(1)).strip() if t_m else s_id
        
        # Split text into exercise chunks
        lines = [re.sub(r'<[^>]+>', ' ', d).strip() for d in re.findall(r'<div class=[\"\'](?:txt-line|sec-hdr)[\"\']>(.*?)</div>', s_html, re.DOTALL)]
        
        # Find lines that are exercises
        tamreens = []
        cur_t = None
        
        for l in lines:
            if not l: continue
            # check if line starts a tamreen
            is_start = bool(re.match(r'^[🐪👨‍🎓👨‍🏫📖📗👁️🔹✍️📋⚡\s]*(\([۱-۹\d]+\)|[۱-۹\d]+[\-\.\)])\s*(.+)', l))
            is_tag = '✍️ تـم' in l or '✍️ تم' in l or 'تَمَارِين' in l or 'تمرين' in l or 'التَّمْرِين' in l
            
            if is_start or is_tag:
                if cur_t:
                    tamreens.append(cur_t)
                cur_t = {'header': l.split('\n')[0].strip(), 'items': []}
            elif cur_t:
                if 'الكلمات الجديدة' in l:
                    tamreens.append(cur_t)
                    cur_t = None
                else:
                    cur_t['items'].append(l)
        if cur_t:
            tamreens.append(cur_t)
            
        # Filter out iqra waktub
        kept_t = [t for t in tamreens if not re.search(r'اقرأ واكتب|اِقْرَأْ وَاكْتُبْ', t['header'])]
        print(f"\nUnit {unit_count} [{s_id}] {title}: {len(kept_t)} Tamreens kept (out of {len(tamreens)})")
        for i, t in enumerate(kept_t, 1):
            hdr = t['header']
            # summarize items
            items_count = len(t['items'])
            print(f"   Tamreen {i}: {hdr[:65]} ({items_count} items)")
