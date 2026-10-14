import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

secs = re.findall(r'<section class="unit-card"[^>]*id="([^"]+)"[\s\S]*?<h2 class="unit-title">[\s\S]*?<span>[^<]*</span>\s*([^<]+)</h2>', html)
for sid, title in secs:
    print(f"{sid:8} --> {title.strip()}")
