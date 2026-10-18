import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's write an accurate parser for Cairo.md that splits by "### "
# Each "### " is a chapter!
sections = re.split(r'\n###\s+', text)
print(f"Total sections: {len(sections)}")

book_map = {1: [], 2: [], 3: []}
current_book = 1

for s in sections[1:]:
    lines = s.strip().split('\n')
    header = lines[0].strip()
    
    # Check if book marker in section
    if '## 📘' in s:
        current_book = 2
    elif '## 📙' in s:
        current_book = 3
        
    # Check if introduction or lesson
    if 'مُقَدِّمَة' in header or 'تَمْهِيد' in header:
        continue
        
    title_clean = header.split('—')[0].strip()
    for em in ['🏠', '⭐', '🌙', '🕌', '📖', '🚗', '🦆', '🏥', '🐦', '👨‍👩‍👦', '🏡', '👩‍⚕️', '👨‍🎓', '🌍', '👩‍🎓', '📚', '🏢', '⚖️', '🔢', '🧮', '🏫', '🎨', '🏛️', '📜', '💡', '🚫', '🏆']:
        title_clean = title_clean.replace(em, '').strip()
        
    subtitle = header.split('—')[1].strip() if '—' in header else ''
    
    # Extract exercises
    # Exercises in Cairo.md are marked with "#### ✍️", "- (1)", "- 📚", "- اقرأ", etc.
    ex_list = []
    curr_ex = None
    
    for l in lines[1:]:
        l_str = l.strip()
        
        # Check if line is an exercise title or instruction
        is_ex_header = False
        ex_title = ""
        
        if l_str.startswith('#### ✍️ تمرين') or l_str.startswith('#### ✍️ تمـرين') or l_str.startswith('#### ✍️ التَّمْرِينُ') or l_str.startswith('#### ✍️ تَمَارِيْنُ') or l_str.startswith('#### ✍️ تـمـــــارين') or l_str.startswith('#### ✍️ تـمـــارين'):
            is_ex_header = True
            ex_title = l_str.replace('#', '').replace('✍️', '').strip()
        elif re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', l_str):
            m = re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', l_str)
            num_str = m.group(1)
            desc_str = m.group(2).strip()
            # Check if this is an instruction (like أجب، أضف، اقرأ، كون، صحح، تأمل، اختر)
            if any(w in desc_str for w in ['أجب', 'أضف', 'اقرأ', 'اِقْرَأْ', 'كون', 'كوّن', 'صَحِّحْ', 'صحح', 'تأمل', 'اختر', 'املأ', 'اِمْلَأْ', 'هات', 'صل', 'استخرج', 'أدخل', 'حول', 'عين', 'اضبط']):
                is_ex_header = True
                ex_title = f"({num_str}) {desc_str}"
        elif l_str.startswith('- 📚') and any(w in l_str for w in ['اقرأ', 'اِقرأ', 'اِقْرَأْ']):
            is_ex_header = True
            ex_title = l_str.lstrip('- 📚').strip()
        elif l_str.startswith('- اقرأ ما يلي') or l_str.startswith('- اقرأ المثال'):
            is_ex_header = True
            ex_title = l_str.lstrip('- ').strip()
            
        if is_ex_header:
            curr_ex = {
                'title': ex_title,
                'items': []
            }
            ex_list.append(curr_ex)
        elif curr_ex is not None and l_str.startswith('- ') and not l_str.startswith('#### 🗂️'):
            item_text = l_str.lstrip('- ').strip()
            if item_text and not item_text.startswith('---'):
                curr_ex['items'].append(item_text)
                
    book_map[current_book].append({
        'header': header,
        'title': title_clean,
        'subtitle': subtitle,
        'exercises': ex_list
    })

print(f"Book 1: {len(book_map[1])} lessons")
print(f"Book 2: {len(book_map[2])} lessons")
print(f"Book 3: {len(book_map[3])} lessons")
