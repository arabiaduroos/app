import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Book 1 first
b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b1_text = text[b1_idx:b2_idx]
b2_text = text[b2_idx:b3_idx]
b3_text = text[b3_idx:]

print(f"Lengths: B1={len(b1_text)}, B2={len(b2_text)}, B3={len(b3_text)}")
