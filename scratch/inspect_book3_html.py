import sys
import re

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-3.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="b3_u10"')
next_idx = content.find('id="b3_u11"', idx)
lesson9_html = content[idx:next_idx]

# strip HTML tags
plain_text = re.sub(r'<[^>]+>', '\n', lesson9_html)
lines = [l.strip() for l in plain_text.split('\n') if l.strip()]

print(f"Total lines: {len(lines)}")
# Write lines to a file to examine
with open(r'scratch/lesson9_html_text.txt', 'w', encoding='utf-8') as out:
    for line in lines:
        out.write(line + '\n')

print("Wrote lines to scratch/lesson9_html_text.txt. First 30 lines:")
for l in lines[:30]:
    sys.stdout.buffer.write((l + '\n').encode('utf-8'))

print("\nLast 30 lines:")
for l in lines[-30:]:
    sys.stdout.buffer.write((l + '\n').encode('utf-8'))
