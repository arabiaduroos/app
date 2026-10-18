import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

# We will build a complete python script to scan every lesson across all 3 books
# and output exact rows for the table.

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's verify how each book is partitioned
b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b1_raw = text[b1_idx:b2_idx]
b2_raw = text[b2_idx:b3_idx]
b3_raw = text[b3_idx:]

print(f"B1 raw: {len(b1_raw)}, B2 raw: {len(b2_raw)}, B3 raw: {len(b3_raw)}")
