import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect Lesson 1 to 5 of Book 1 line by line to make sure our parser captures every single exercise and snippet
with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

chunks = re.split(r'\n###\s+', b1_text)[1:]

for idx in range(5):
    c = chunks[idx]
    lines = [l.strip() for l in c.strip().split('\n') if l.strip()]
    print(f"\n=================== LESSON {idx+1}: {lines[0]} ===================")
    for l in lines:
        if any(k in l for k in ['#### ✍️', '- (', '- 📚', '- اقرأ', 'محمدٌ', 'آمِنَـةُ', 'اِسمٌ', 'ابْنٌ', 'أجب', 'صل', 'امْلأ']):
            print("  ", l[:90])
