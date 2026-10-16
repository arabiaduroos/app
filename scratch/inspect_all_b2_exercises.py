import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section class="unit-card"[^>]*id="([^"]+)"([\s\S]*?)</section>', html)

print(f"Total sections in Book 2 HTML: {len(sections)}")

for uid, sec in sections:
    # Skip muqaddimah
    if uid == 'b2_u1':
        continue
    m_num = int(re.search(r'b2_u(\d+)', uid).group(1))
    real_unit_num = m_num - 1 # 1-based lesson number
    
    title_m = re.search(r'<h2 class="unit-title">[\s\S]*?<span>([^<]*)</span>\s*([^<]+)</h2>', sec)
    title = title_m.group(2).strip() if title_m else uid
    
    # Extract txt-lines
    lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', sec)
    
    # Find all exercise headers
    ex_list = []
    for i, (ar_raw, ur_raw) in enumerate(lines):
        ar = re.sub(r'<[^>]+>', '', ar_raw).strip()
        ur = re.sub(r'<[^>]+>', '', ur_raw).strip() if ur_raw else ''
        
        # Check if line looks like an exercise header
        if re.search(r'^(?:[🔹🐪👁️🚪📚⌚\s]*)(?:\d+[\-\.]|تمرين|تمارين|ضع|املأ|تأمل|أدخل|حوّل|هات|صُغ|عَيّن|مَيّز|كوّن|أجب)', ar):
            if any(k in ar for k in ['أجب', 'تأمل', 'ضع', 'أدخل', 'اقرأ', 'املأ', 'حوّل', 'هات', 'صُغ', 'تمرين', 'تمارين', 'كوّن', 'عَيّن', 'مَيّز', 'استعمل', 'اضبط', 'اكتب']):
                ex_list.append((i, ar, ur))
    
    print(f"\nUnit {real_unit_num:2d} (id: {uid}, title: {title[:25]}): {len(lines)} txt lines, {len(ex_list)} exercises found:")
    for idx, ar, ur in ex_list[:6]:
        print(f"   [{idx:2d}] {ar[:60]}  -->  {ur[:40]}")
