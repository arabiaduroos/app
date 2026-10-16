import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find Book 2
b2_pos = text.find('## 📘')
b3_pos = text.find('## 📙')

b2_text = text[b2_pos:b3_pos]
chapters = re.findall(r'(### [^\n]+)([\s\S]*?)(?=### |\Z)', b2_text)

print(f"Book 2 chapters count: {len(chapters)}")
for title, body in chapters[:3]:
    print("\n-------------------------")
    print("Chapter Title:", title)
    lines = body.split('\n')
    ex_idx = [i for i, l in enumerate(lines) if 'تمرين' in l or 'تمارين' in l]
    print("Exercise line indices:", ex_idx)
    if ex_idx:
        for l in lines[ex_idx[0]:ex_idx[0]+30]:
            if l.strip():
                print("  ", l[:90])
