import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b2_text = text[b2_idx:b3_idx]
b3_text = text[b3_idx:]

b2_chunks = re.split(r'\n###\s+', b2_text)
b3_chunks = re.split(r'\n###\s+', b3_text)

print(f"Book 2 Chunks: {len(b2_chunks)-1}")
for idx, c in enumerate(b2_chunks[1:], 1):
    lines = [l.strip() for l in c.strip().split('\n') if l.strip()]
    header = lines[0]
    print(f"  [{idx}] {header[:60]} ({len(lines)} lines)")

print(f"\nBook 3 Chunks: {len(b3_chunks)-1}")
for idx, c in enumerate(b3_chunks[1:], 1):
    lines = [l.strip() for l in c.strip().split('\n') if l.strip()]
    header = lines[0]
    print(f"  [{idx}] {header[:60]} ({len(lines)} lines)")
