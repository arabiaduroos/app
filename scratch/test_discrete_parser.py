import re, json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo_md = f.read()

b2_idx = cairo_md.find('## 📘')
b3_idx = cairo_md.find('## 📙')
b2_secs = re.split(r'\n###\s+', cairo_md[b2_idx:b3_idx])[2:]

# Test on Book 2 Lesson 1
sec1 = b2_secs[0]
lines = sec1.split('\n')

exercises = []
cur_ex = None

for l in lines:
    clean = re.sub(r'^[^\w\(\)\[\]]+', '', l).strip()
    m = re.match(r'^([0-9]+)\s*[\-\.]\s*(.*)', clean)
    if m:
        if cur_ex:
            exercises.append(cur_ex)
        cur_ex = {
            'num': m.group(1),
            'desc': m.group(2).lstrip('•').strip(),
            'lines': []
        }
    elif cur_ex:
        if l.startswith('#### 🗂️') or l.startswith('---'):
            exercises.append(cur_ex)
            cur_ex = None
        else:
            cur_ex['lines'].append(l)

if cur_ex:
    exercises.append(cur_ex)

print(f"Book 2 Lesson 1: Found {len(exercises)} discrete exercises!")
for ex in exercises:
    content = " ".join(ex['lines'])
    nums = set(re.findall(r'\(([0-9]+|[۱-۹]+)\)', content))
    count = len(nums) if nums else max(len([l for l in ex['lines'] if len(l.strip())>5]), 1)
    print(f"  Ex {ex['num']}: {ex['desc'][:60]} -> {count} items")
