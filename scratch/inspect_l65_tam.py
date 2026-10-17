import sys

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('### 🔗 الدَّرْسُ التَّاسِعُ')
next_idx = text.find('### 🧩 الدَّرْسُ الْعَاشِرُ')

l65 = text[idx:next_idx]
tam_idx = l65.find('#### ✍️ تمــارين')
tam_text = l65[tam_idx:]

# print lines that start with numbers or headers or bullet points
lines = tam_text.split('\n')
for i, line in enumerate(lines):
    line_s = line.strip()
    if line_s.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '-', '*', '#', '•')):
        sys.stdout.buffer.write(f"{i}: {line_s[:100]}\n".encode('utf-8'))
