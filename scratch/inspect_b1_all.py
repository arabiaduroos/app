import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo = f.read()

b1_idx = cairo.find('## 📗')
b2_idx = cairo.find('## 📘')
b1_text = cairo[b1_idx:b2_idx]
lessons = re.split(r'\n###\s+', b1_text)[1:]

print("=== LESSON 1 ===")
print(lessons[0][:1500])

print("\n=== LESSON 2 ===")
print(lessons[1][:1500])

print("\n=== LESSON 3 ===")
print(lessons[2][:1500])
