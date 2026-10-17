import sys
import re

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('### 🔗 الدَّرْسُ التَّاسِعُ')
next_idx = text.find('### 🧩 الدَّرْسُ الْعَاشِرُ')

l65 = text[idx:next_idx]
print(f"Lesson 65 text length: {len(l65)}")

# Find all headers in l65
headers = re.findall(r'^(#+)\s+(.*?)$', l65, re.MULTILINE)
for h in headers:
    sys.stdout.buffer.write(f"{h[0]} {h[1]}\n".encode('utf-8'))
