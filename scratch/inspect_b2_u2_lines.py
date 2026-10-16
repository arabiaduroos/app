import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find b2_u2
m = re.search(r'<section class="unit-card"[^>]*id="b2_u2"([\s\S]*?)</section>', html)
if m:
    sec = m.group(1)
    lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', sec)
    print(f"b2_u2 has {len(lines)} txt-lines:")
    for i, (ar, ur) in enumerate(lines):
        ar_clean = re.sub(r'<[^>]+>', '', ar).strip()
        ur_clean = re.sub(r'<[^>]+>', '', ur).strip() if ur else ''
        if any(w in ar_clean for w in ['تمرين', 'تمارين', '1-', '2-', '3-', '4-', '5-', '6-', '7-', '8-', '9-', '10-', '11-', '12-', '13-']) or i < 15 or i > len(lines) - 20:
            print(f"{i:2d}: {ar_clean[:70]}  -->  {ur_clean[:50]}")
