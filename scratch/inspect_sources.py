import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo = f.read()

pos_l4 = cairo.find('### 🕌 الدَّرْسُ الرَّابِعُ')
pos_l5 = cairo.find('### 📖 الدَّرْسُ الْخَامِسُ')
pos_l6 = cairo.find('### 🚗 الدَّرْسُ السَّادِسُ')

print("=== LESSON 4 IN CAIRO.MD ===")
print(cairo[pos_l4:pos_l5])
