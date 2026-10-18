import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

def clean_title(s):
    t = s.split('—')[0].strip()
    for em in ['🏠', '⭐', '🌙', '🕌', '📖', '🚗', '🦆', '🏥', '🐦', '👨‍👩‍👦', '🏡', '👩‍⚕️', '👨‍🎓', '🌍', '📚', '🏢', '⚖️', '🔢', '🧮', '🏫', '🎨', '🏛️', '💡', '🚫', '🏆', '⏳', '🎯', '🍎', '🕐', '📊', '🌟', '🔄', '🚌', '📅', '📋', '📣', '🛑', '🍂', '✈️', '🔮', '⚡', '📐', '👥', '💯', '👑', '🕰️', '🗣️', '🚶', '🕋', '🤝', '✨', '📜', '🔨', '📍', '🔑', '🔍', '🔗', '🧩', '🏗️', '🧭', '⚙️', '🎁', '쌍']:
        t = t.replace(em, '').strip()
    return t

# Let's inspect Book 1 first and write its table
b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b1_text = text[b1_idx:b2_idx]
b2_text = text[b2_idx:b3_idx]
b3_text = text[b3_idx:]

b1_chunks = re.split(r'\n###\s+', b1_text)[1:]

print(f"B1 Chunks: {len(b1_chunks)}")
