import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find "الدرس الأول" in Book 2 HTML
pos = text.find('الدَّرْسُ الأَوَّلُ')
if pos == -1:
    pos = text.find('الدرس الأول')
if pos == -1:
    pos = text.find('الدَّرْسُ')

print(f"Position: {pos}")
print(text[pos:pos+1500])
