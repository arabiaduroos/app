import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect all lessons of Book 1 in Cairo.md
b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

# Split by lesson headers
lesson_chunks = re.split(r'\n###\s+', b1_text)

print(f"Total chunks in Book 1: {len(lesson_chunks)}")

for idx, chunk in enumerate(lesson_chunks[1:], 1):
    lines = chunk.strip().split('\n')
    header = lines[0].strip()
    print(f"\n=======================================================")
    print(f"LESSON {idx}: {header}")
    print(f"=======================================================")
    
    # print lines that look like exercises
    for l in lines:
        l_s = l.strip()
        if any(keyword in l_s for keyword in ['تمرين', 'تَمْرِين', 'تمـرين', 'تَمَارِيْن', 'أجب', 'اقرأ', 'اِقْرَأ', 'اِمْلَأ', 'أضف', 'صَحِّح', 'كون', 'هات', 'صل', 'تأمل']):
            if l_s.startswith('#') or l_s.startswith('- (') or l_s.startswith('- 📚') or l_s.startswith('- اقرأ'):
                print(" ", l_s[:100])
