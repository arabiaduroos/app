import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

b1_chunks = re.split(r'\n###\s+', b1_text)[1:]

def clean_title(s):
    t = s.split('—')[0].strip()
    for em in ['🏠', '⭐', '🌙', '🕌', '📖', '🚗', '🦆', '🏥', '🐦', '👨‍👩‍👦', '🏡', '👩‍⚕️', '👨‍🎓', '🌍', '📚', '🏢', '⚖️', '🔢', '🧮', '🏫', '🎨', '🏛️']:
        t = t.replace(em, '').strip()
    return t

b1_table = []

for idx, c in enumerate(b1_chunks, 1):
    lines = [l.strip() for l in c.strip().split('\n') if l.strip()]
    header = clean_title(lines[0])
    
    # We will parse this lesson's lines and extract all tamreens and snippets
    # Let's inspect what's inside
    current_entry = None
    
    for l in lines[1:]:
        # Detect tamreens or snippets
        # Let's look for known patterns
        pass

print("Script template ready.")
