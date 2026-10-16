import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_book = None
current_chapter = None
chapters = []

for line in lines:
    line_s = line.strip()
    if line_s.startswith('## 📗') or line_s.startswith('## 📘') or line_s.startswith('## 📙'):
        current_book = line_s
    elif line_s.startswith('### '):
        current_chapter = {
            'book': current_book,
            'title': line_s,
            'tamreens': []
        }
        chapters.append(current_chapter)
    elif line_s.startswith('#### ✍️') or line_s.startswith('#### ') or 'تمرين' in line_s or 'تمارين' in line_s:
        if current_chapter and line_s.startswith('#'):
            current_chapter['tamreens'].append(line_s)

print(f"Total chapters found in Markdown: {len(chapters)}")
for i, ch in enumerate(chapters):
    print(f"{i+1:2d}. {ch['title'][:55]} | Tamreens marked: {len(ch['tamreens'])}")
    if ch['tamreens']:
        print(f"    {ch['tamreens'][:5]}")
