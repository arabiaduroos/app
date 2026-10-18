import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Normalize arabic
def norm_ar(s):
    return re.sub(r'[\u0640\u064b-\u065f]', '', s)

# Let's write a parser for each book
b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b1_text = text[b1_idx:b2_idx]
b2_text = text[b2_idx:b3_idx]
b3_text = text[b3_idx:]

print("Ready to process books.")
