import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

m23 = re.search(r'<section class="unit-card"[^>]*id="b2_u23"([\s\S]*?)</section>', html)
if m23:
    print("=== b2_u23 content ===")
    lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', m23.group(1))
    for ar, ur in lines:
        print("AR:", re.sub(r'<[^>]+>', '', ar).strip())

m25 = re.search(r'<section class="unit-card"[^>]*id="b2_u25"([\s\S]*?)</section>', html)
if m25:
    print("\n=== b2_u25 content ===")
    lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', m25.group(1))
    for ar, ur in lines[:15]:
        print("AR:", re.sub(r'<[^>]+>', '', ar).strip())
