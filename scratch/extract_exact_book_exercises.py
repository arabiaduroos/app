import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

# Split by "### "
sections = re.split(r'\n###\s+', b1_text)

print(f"Total sections in Book 1: {len(sections)-1}")

b1_curriculum = []

for idx, s in enumerate(sections[1:], 1):
    lines = s.strip().split('\n')
    header = lines[0].strip()
    title = header.split('—')[0].replace('🏠', '').replace('⭐', '').replace('🌙', '').replace('🕌', '').replace('📖', '').replace('🚗', '').replace('🦆', '').replace('🏥', '').replace('🐦', '').replace('👨‍👩‍👦', '').replace('🏡', '').replace('👩‍⚕️', '').replace('👨‍🎓', '').replace('🌍', '').replace('👩‍🎓', '').replace('📚', '').replace('🏢', '').replace('⚖️', '').replace('🔢', '').replace('🧮', '').replace('🏫', '').replace('🎨', '').replace('🏛️', '').strip()
    subtitle = header.split('—')[1].strip() if '—' in header else ''
    
    # We want to identify every single exercise block
    exercises = []
    
    # Walk through lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect exercise starters
        # 1. "#### ✍️ تمرين (X)"
        # 2. "- (X) أجب..."
        # 3. "- (X) أضف..."
        # 4. "- 📚 (X) اقرأ..."
        # 5. "- 📚 - اقرأ..."
        # 6. "- (X) كون..."
        # 7. "- (X) صَحِّحْ..."
        # 8. "- (X) محمدٌ : يا محمدُ" (snippet)
        # 9. "- (X) اِسمٌ : ..." (snippet)
        # 10. "- اقرأ ما يلي..."
        is_ex = False
        ex_label = ""
        
        if line.startswith('#### ✍️') and not 'تـمـــــارين' in line and not 'تَمَارِيْنُ' in line and not 'تـمـــارين' in line:
            is_ex = True
            ex_label = line.replace('#', '').replace('✍️', '').strip()
        elif re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', line):
            m = re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', line)
            num = m.group(1)
            rest = m.group(2).strip()
            # If rest has instruction or is snippet
            if any(w in rest for w in ['أجب', 'أضف', 'اقرأ', 'اِقْرَأْ', 'كون', 'كوّن', 'صَحِّحْ', 'صحح', 'تأمل', 'اختر', 'املأ', 'اِمْلَأْ', 'هات', 'صل', 'استخرج', 'أدخل', 'حول', 'عين', 'اضبط', 'ضع', 'محمدٌ', 'اِسمٌ', 'اِبْنٌ', 'فيصل']):
                is_ex = True
                ex_label = f"({num}) {rest}"
        elif line.startswith('- 📚') and any(w in line for w in ['اقرأ', 'اِقرأ', 'اِقْرَأْ']):
            is_ex = True
            ex_label = line.lstrip('- 📚').strip()
        elif line.startswith('- اقرأ ما يلي') or line.startswith('- اقرأ المثال'):
            is_ex = True
            ex_label = line.lstrip('- ').strip()
            
        if is_ex:
            # Collect items until next exercise or section end
            items = []
            j = i + 1
            while j < len(lines):
                next_l = lines[j].strip()
                if (next_l.startswith('#### ✍️') and not any(k in next_l for k in ['تـمـــــارين', 'تَمَارِيْنُ', 'تـمـــارين'])) or \
                   (re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', next_l) and any(w in next_l for w in ['أجب', 'أضف', 'اقرأ', 'اِقْرَأْ', 'كون', 'كوّن', 'صَحِّحْ', 'صحح', 'تأمل', 'اختر', 'املأ', 'اِمْلَأْ', 'هات', 'صل', 'استخرج', 'أدخل', 'حول', 'عين', 'اضبط', 'ضع', 'محمدٌ', 'اِسمٌ', 'اِبْنٌ'])) or \
                   (next_l.startswith('- 📚') and any(w in next_l for w in ['اقرأ', 'اِقرأ', 'اِقْرَأْ'])) or \
                   next_l.startswith('- اقرأ ما يلي') or next_l.startswith('#### 🗂️') or next_l.startswith('---'):
                    break
                if next_l.startswith('- '):
                    clean_it = next_l.lstrip('- ').strip()
                    if clean_it:
                        items.append(clean_it)
                j += 1
            exercises.append({
                'label': ex_label,
                'items_count': len(items),
                'sample_items': items[:3]
            })
            i = j - 1
        i += 1
        
    b1_curriculum.append({
        'lesson_num': idx,
        'title': title,
        'subtitle': subtitle,
        'exercises': exercises
    })

print("=== BOOK 1 COMPLETE CURRICULUM SUMMARY ===")
for l in b1_curriculum:
    print(f"\n[Lesson {l['lesson_num']}] {l['title']} — {l['subtitle']} ({len(l['exercises'])} exercises):")
    for k, ex in enumerate(l['exercises'], 1):
        print(f"   Ex {k}: {ex['label'][:65]} -> {ex['items_count']} items")
