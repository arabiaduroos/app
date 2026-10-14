import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-1.html', encoding='utf-8') as f:
    content = f.read()

d1 = content.find('🏠 الدَّرْسُ الْأَوَّلُ')
d2 = content.find('⭐ الدَّرْسُ الثَّانِي')
lesson1_html = content[d1:d2]
print('Length of lesson 1 html:', len(lesson1_html))

# Let's inspect the HTML snippet
lines = [line.strip() for line in lesson1_html.splitlines() if line.strip()]
print('Total non-empty lines:', len(lines))
for line in lines[:60]:
    clean = re.sub(r'<[^>]+>', '', line).strip()
    if clean:
        print(' -', clean[:80])
