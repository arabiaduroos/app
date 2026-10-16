import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

for uid in ['b2_u23', 'b2_u25']:
    m = re.search(r'<section class="unit-card"[^>]*id="' + uid + r'"([\s\S]*?)</section>', html)
    if m:
        print(f"=== {uid} ===")
        lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', m.group(1))
        for ar, ur in lines:
            print("  AR:", re.sub(r'<[^>]+>', '', ar).strip())
            print("  UR:", re.sub(r'<[^>]+>', '', ur).strip() if ur else '')
