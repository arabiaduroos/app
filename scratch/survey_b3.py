import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Split into books
parts = re.split(r'\n##\s+', text)
book3_text = ""
for p in parts:
    if 'الجزء الثالث' in p or 'الْجُزْءُ الثَّالِثُ' in p:
        book3_text = p
        break

print(f"Book 3 length: {len(book3_text)} chars")
# Split Book 3 into lessons
lessons = re.split(r'\n###\s+', book3_text)
print(f"Book 3 lessons found: {len(lessons)}")

for idx, l in enumerate(lessons[1:], 1):
    header = l.split('\n')[0]
    # Find all exercise lines
    ex_markers = re.findall(r'(\([0-9]+\)\s*•\s*[^\n]+|####\s*✍️[^\n]+)', l)
    print(f"\nLesson {idx}: {header[:60]}")
    print(f"  Total potential exercise items: {len(ex_markers)}")
    for em in ex_markers[:5]:
        print(f"    - {em[:80]}")
