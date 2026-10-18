import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

chunks = re.split(r'\n###\s+', b1_text)[1:]

def clean_title(s):
    t = s.split('—')[0].strip()
    for em in ['🏠', '⭐', '🌙', '🕌', '📖', '🚗', '🦆', '🏥', '🐦', '👨‍👩‍👦', '🏡', '👩‍⚕️', '👨‍🎓', '🌍', '📚', '🏢', '⚖️', '🔢', '🧮', '🏫', '🎨', '🏛️']:
        t = t.replace(em, '').strip()
    return t

for idx in range(5, 12):
    c = chunks[idx]
    lines = [l.strip() for l in c.strip().split('\n') if l.strip()]
    print(f"\n=================== LESSON {idx+1}: {lines[0]} ===================")
    for l in lines:
        if any(k in l for k in ['#### ✍️', '- (', '- 📚', '- اقرأ', 'أجب', 'صل', 'امْلأ', 'ضع', 'حول', 'هات', 'أشر']):
            print("  ", l[:90])
