import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo = f.read()

b2_idx = cairo.find('## 📘')
b3_idx = cairo.find('## 📙')
b2_text = cairo[b2_idx:b3_idx]
b2_secs = re.split(r'\n###\s+', b2_text)[2:] # first 2 are header/intro

l1 = b2_secs[0]
lines = [l.strip() for l in l1.splitlines() if l.strip()]

print(f"Book 2 Lesson 1 has {len(lines)} lines.")
# Let's find numbered exercises
cur_ex = None
exercises = []
for line in lines:
    m = re.match(r'^(?:[^\w\(\)\[\]]*)([0-9]+)\s*[\-\.]\s*(.*)', line)
    if m:
        if cur_ex:
            exercises.append(cur_ex)
        cur_ex = {'num': m.group(1), 'title': m.group(2).strip(), 'lines': []}
    elif cur_ex:
        if line.startswith('#### 🗂️') or line.startswith('---'):
            exercises.append(cur_ex)
            cur_ex = None
        else:
            cur_ex['lines'].append(line)
if cur_ex:
    exercises.append(cur_ex)

print(f"Found {len(exercises)} exercises in Book 2 Lesson 1:")
for ex in exercises:
    print(f"Ex {ex['num']}: {ex['title'][:50]} | Lines: {len(ex['lines'])}")
    all_text = " ".join(ex['lines'])
    parts = re.findall(r'\(([0-9]+)\)\s*([^\(\)]+)', all_text)
    print(f"   Extracted {len(parts)} parts: {[p[1].strip()[:30] for p in parts[:3]]}")
