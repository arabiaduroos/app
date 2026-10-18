import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

chunks = re.split(r'\n###\s+', b1_text)

print(f"Book 1 Chunks: {len(chunks)-1}")

for idx, c in enumerate(chunks[1:], 1):
    lines = [l.strip() for l in c.strip().split('\n') if l.strip()]
    header = lines[0]
    title = header.split('—')[0].strip()
    for em in ['🏠', '⭐', '🌙', '🕌', '📖', '🚗', '🦆', '🏥', '🐦', '👨‍👩‍👦', '🏡', '👩‍⚕️', '👨‍🎓', '🌍', '📚', '🏢', '⚖️', '🔢', '🧮', '🏫', '🎨', '🏛️']:
        title = title.replace(em, '').strip()
    print(f"\n[{idx}] {title} ({len(lines)} lines)")
