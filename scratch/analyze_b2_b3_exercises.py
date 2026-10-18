import sys, re

sys.stdout.reconfigure(encoding='utf-8')

def normalize_ar(s):
    return re.sub(r'[\u0640\u064b-\u065f]', '', s)

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')
b2_text = text[b2_idx:b3_idx]
b3_text = text[b3_idx:]

def analyze_book(b_text, b_num):
    print(f"\n=======================================================")
    print(f"               BOOK {b_num} FULL EXERCISE AUDIT        ")
    print(f"=======================================================")
    sections = re.split(r'\n###\s+', b_text)
    
    for idx, s in enumerate(sections[1:], 1):
        lines = s.strip().split('\n')
        header = lines[0].strip()
        if 'مقدمة' in normalize_ar(header) or 'تمهيد' in normalize_ar(header):
            continue
        title = header.split('—')[0].strip()
        for em in ['🏠', '⭐', '🌙', '🕌', '📖', '🚗', '🦆', '🏥', '🐦', '👨‍👩‍👦', '🏡', '👩‍⚕️', '👨‍🎓', '🌍', '📚', '🏢', '⚖️', '🔢', '🧮', '🏫', '🎨', '🏛️', '💡', '🚫', '🏆']:
            title = title.replace(em, '').strip()
        subtitle = header.split('—')[1].strip() if '—' in header else ''
        
        exercises = []
        for line in lines[1:]:
            l_str = line.strip()
            norm = normalize_ar(l_str)
            
            # Check for exercise headers
            # (1) أجب, (2) ضع علامة, (3) تأمل, etc.
            m = re.match(r'^-\s*(?:[🔹🐪🏫👨‍🎓📖✍️\*\s]*)(?:📚\s*)?(?:\((\d+|[أ-ي])\)|(\d+|[أ-ي])\s*[-–\.:])\s*(.+)', l_str)
            if m:
                num = m.group(1) or m.group(2)
                desc = m.group(3).strip()
                norm_desc = normalize_ar(desc)
                if any(w in norm_desc for w in ['اجب', 'ضع', 'تامل', 'ادخل', 'اقرا', 'كون', 'حول', 'عين', 'استخرج', 'هات', 'صل', 'استعمل', 'صغ', 'اكتب', 'اضبط', 'بين', 'املا', 'اختر', 'اسند', 'انف', 'رد']):
                    exercises.append(f"Ex {num}: {desc[:60]}")
            elif 'تمرين' in norm and ('#' in l_str or l_str.startswith('-')):
                exercises.append(f"Ex: {l_str.replace('#', '').replace('✍️', '').strip()[:60]}")
                
        print(f"\n[{title}] — {subtitle} ({len(exercises)} exercises):")
        for ex in exercises:
            print(f"   • {ex}")

analyze_book(b2_text, 2)
analyze_book(b3_text, 3)
