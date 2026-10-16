import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for bnum, fname in [(1, 'transcriptions/Madinah-Book-1.html'), 
                    (2, 'transcriptions/Madinah-Book-2.html'), 
                    (3, 'transcriptions/Madinah-Book-3.html')]:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    units = re.findall(r'<section class="unit-card"[^>]*id="([^"]+)"', html)
    tamreens = re.findall(r'تمرين|تمارين|التدريب', html)
    txt_lines = re.findall(r'<div class="txt-line">', html)
    print(f'Book {bnum}: {len(units)} unit sections, {len(tamreens)} tamreen mentions, {len(txt_lines)} text lines')

# Also check Madinah-All-Books-Cairo.md
with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    md = f.read()

md_h2 = re.findall(r'^##\s+(.*)', md, re.MULTILINE)
md_h3 = re.findall(r'^###\s+(.*)', md, re.MULTILINE)
md_h4 = re.findall(r'^####\s+(.*)', md, re.MULTILINE)
print(f'Markdown: {len(md_h2)} books, {len(md_h3)} chapters, {len(md_h4)} subheadings/tamreens')
for h in md_h2:
    print('  Book:', h)
print(f'First 10 chapters: {md_h3[:10]}')
