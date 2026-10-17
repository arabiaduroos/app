import sys

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('### 🔗 الدَّرْسُ التَّاسِعُ')
next_idx = text.find('### 🧩 الدَّرْسُ الْعَاشِرُ')

l65 = text[idx:next_idx]
tam_idx = l65.find('#### ✍️ تمــارين')
tam_text = l65[tam_idx:]

lines = tam_text.split('\n')
for i, line in enumerate(lines[:58]):
    sys.stdout.buffer.write(f"{i}: {line}\n".encode('utf-8'))
