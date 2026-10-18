import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

# Let's inspect Lesson 1, 2, 3, 4, 6, 7, 8 in detail
sections = re.split(r'\n###\s+', b1_text)

for idx in [1, 2, 3, 4, 6, 7, 8]:
    s = sections[idx]
    lines = s.strip().split('\n')
    header = lines[0].strip()
    print(f"\n=======================================================")
    print(f"FULL EXERCISES INSPECTION: {header}")
    print(f"=======================================================")
    
    in_tamreen = False
    for l in lines:
        l_s = l.strip()
        if 'تَمَارِيْن' in l_s or 'تـمـــــارين' in l_s or 'تـمـــارين' in l_s or 'تمارين' in l_s or 'تَمْرِين' in l_s:
            in_tamreen = True
            print(">>>", l_s)
        elif in_tamreen:
            if l_s.startswith('#### 🗂️') or l_s.startswith('### '):
                in_tamreen = False
            elif l_s.startswith('- (') or l_s.startswith('#### ✍️') or l_s.startswith('- 📚') or l_s.startswith('- اقرأ') or l_s.startswith('- ضع') or l_s.startswith('- أجب'):
                print("   ", l_s[:90])
