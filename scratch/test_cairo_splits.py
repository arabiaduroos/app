import fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect Book 1 exercises lesson by lesson from Madinah-All-Books-Cairo.md
with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo_md = f.read()

# Let's see the sections for Book 1, 2, 3
b1_idx = cairo_md.find('## 📗')
b2_idx = cairo_md.find('## 📘')
b3_idx = cairo_md.find('## 📙')

b1_text = cairo_md[b1_idx:b2_idx]
b2_text = cairo_md[b2_idx:b3_idx]
b3_text = cairo_md[b3_idx:]

print(f"Book 1 text length: {len(b1_text):,} chars")
print(f"Book 2 text length: {len(b2_text):,} chars")
print(f"Book 3 text length: {len(b3_text):,} chars")
