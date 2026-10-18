import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Lesson 5 in Cairo.md from "الدَّرْسُ الْخَامِسُ" to "الدَّرْسُ السَّادِسُ"
p5 = text.find('الدَّرْسُ الْخَامِسُ')
p6 = text.find('الدَّرْسُ السَّادِسُ')
l5_text = text[p5:p6]

print("=== EXACT FULL TEXT OF LESSON 5 IN CAIRO.MD ===")
print(l5_text)
