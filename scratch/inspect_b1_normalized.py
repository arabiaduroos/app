import sys, re

sys.stdout.reconfigure(encoding='utf-8')

def normalize_ar(s):
    # Remove tashkeel and tatweel
    return re.sub(r'[\u0640\u064b-\u065f]', '', s)

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b1_text = text[b1_idx:b2_idx]

sections = re.split(r'\n###\s+', b1_text)

cumulative_ex_counter = 0

print("=== RE-INSPECTING ALL 23 LESSONS OF BOOK 1 WITH TATWEEL REMOVED ===")

for idx, s in enumerate(sections[1:], 1):
    lines = s.strip().split('\n')
    header = lines[0].strip()
    title = header.split('—')[0].strip()
    for em in ['🏠', '⭐', '🌙', '🕌', '📖', '🚗', '🦆', '🏥', '🐦', '👨‍👩‍👦', '🏡', '👩‍⚕️', '👨‍🎓', '🌍', '📚', '🏢', '⚖️', '🔢', '🧮', '🏫', '🎨', '🏛️']:
        title = title.replace(em, '').strip()
        
    print(f"\n=======================================================")
    print(f"LESSON {idx}: {title}")
    print(f"=======================================================")
    
    lesson_exercises = []
    current_ex = None
    
    for line in lines[1:]:
        l_str = line.strip()
        norm = normalize_ar(l_str)
        
        # Check if line indicates an exercise
        is_ex = False
        ex_name = ""
        
        if 'تمرين' in norm or 'تمارين' in norm:
            is_ex = True
            ex_name = l_str.replace('#', '').replace('✍️', '').strip()
        elif re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', l_str):
            m = re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', l_str)
            ex_num = m.group(1)
            ex_text = m.group(2)
            norm_ex = normalize_ar(ex_text)
            if any(w in norm_ex for w in ['اجب', 'اضف', 'اقرا', 'كون', 'صحح', 'تامل', 'اختر', 'املا', 'هات', 'صل', 'استخرج', 'ادخل', 'حول', 'عين', 'اضبط', 'ضع', 'محمد', 'اسم', 'ابن', 'فيصل']):
                is_ex = True
                ex_name = f"({ex_num}) {ex_text}"
        elif l_str.startswith('- 📚') and any(w in norm for w in ['اقرا']):
            is_ex = True
            ex_name = l_str.lstrip('- 📚').strip()
        elif l_str.startswith('- اقرأ ما يلي') or l_str.startswith('- اقرأ المثال'):
            is_ex = True
            ex_name = l_str.lstrip('- ').strip()
            
        if is_ex:
            cumulative_ex_counter += 1
            current_ex = {
                'cum_id': cumulative_ex_counter,
                'name': ex_name,
                'lines': []
            }
            lesson_exercises.append(current_ex)
        elif current_ex is not None and l_str.startswith('- ') and not l_str.startswith('#### 🗂️'):
            clean_item = l_str.lstrip('- ').strip()
            if clean_item and not clean_item.startswith('---'):
                current_ex['lines'].append(clean_item)
                
    for ex in lesson_exercises:
        print(f"  [Tamreen {ex['cum_id']}]: {ex['name'][:65]} ({len(ex['lines'])} items)")
