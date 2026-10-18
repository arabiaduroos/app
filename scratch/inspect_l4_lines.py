import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo = f.read()

b1_idx = cairo.find('## 📗')
b2_idx = cairo.find('## 📘')
b1_text = cairo[b1_idx:b2_idx]
import re
b1_secs = re.split(r'\n###\s+', b1_text)[1:]

l4 = b1_secs[3]
lines = [l.strip() for l in l4.splitlines() if l.strip()]

for i, line in enumerate(lines[30:70], 30):
    print(f"{i}: {line[:70]}")
