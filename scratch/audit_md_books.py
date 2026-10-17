import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Split into books
book_splits = re.split(r'##\s+.*?دُرُوسُ اللُّغَةِ الْعَرَبِيَّةِ.*?الْجُزْءُ\s+([^\n]+)', text)

print(f"Book splits found: {len(book_splits)}")
# Let's inspect where the books start
b1_idx = text.find('الْجُزْءُ الْأَوَّلُ')
b2_idx = text.find('الْجُزْءُ الثَّانِي')
b3_idx = text.find('الْجُزْءُ الثَّالِثُ')

print(f"B1 at {b1_idx}, B2 at {b2_idx}, B3 at {b3_idx}")

# Check lessons in each book
b1_text = text[b1_idx:b2_idx]
b2_text = text[b2_idx:b3_idx]
b3_text = text[b3_idx:]

for b_name, b_txt in [("Book 1", b1_text), ("Book 2", b2_text), ("Book 3", b3_text)]:
    lessons = re.findall(r'^###\s+(.*?)$', b_txt, re.MULTILINE)
    tamreens = re.findall(r'####\s+✍️\s*(.*?)$', b_txt, re.MULTILINE)
    print(f"\n{b_name}: {len(lessons)} lessons, {len(tamreens)} tamreen headers in markdown")
    for i, l in enumerate(lessons[:5]):
        print(f"  Lesson {i+1}: {l[:60]}")
