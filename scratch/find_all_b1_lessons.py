import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's split by lessons
lesson_pattern = re.compile(r'<div class="txt-line"><div>\s*(?:\([0-9]+\)\s*)?(الْدَّرْسُ|الدَّرْسُ|الدرس)\s+([^<]+)</div><div class="ur">([^<]+)</div></div>')
matches = list(lesson_pattern.finditer(html))
print(f"Total lesson matches in Book-1.html: {len(matches)}")

for i, m in enumerate(matches):
    print(f"  Lesson {i+1}: {m.group(1)} {m.group(2)}  |  {m.group(3)}")
