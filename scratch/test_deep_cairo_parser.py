import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all lesson boundaries in Cairo.md
# Book 1: from "## 📗" to "## 📘"
# Book 2: from "## 📘" to "## 📙"
# Book 3: from "## 📙" to end
b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b1_text = text[b1_idx:b2_idx]
b2_text = text[b2_idx:b3_idx]
b3_text = text[b3_idx:]

def parse_book_lessons(b_text, b_num):
    # Split by "### "
    parts = re.split(r'\n###\s+', b_text)
    lessons = []
    cumulative_tamreen_count = 0
    
    for p in parts[1:]:
        p_lines = p.strip().split('\n')
        header = p_lines[0].strip()
        # Clean title
        title_ar = header.split('—')[0].replace('🏠', '').replace('⭐', '').replace('🌙', '').replace('🕌', '').replace('📜', '').replace('🚗', '').replace('💡', '').replace('🚫', '').replace('🏆', '').replace('⚖️', '').replace('🏛️', '').strip()
        
        # Find exercises
        # An exercise can start with "#### ✍️", or "(1)", "(2)", "📚", or "اقرأ"
        tamreens = []
        current_tam = None
        
        for line in p_lines[1:]:
            l = line.strip()
            # Check if this line is an exercise header
            # Patterns:
            # #### ✍️ تمرين (1)
            # - (1) أجب عن الأسئلة الآتية:
            # - (2) أضف الكلمة الأولى إلى الثانية:
            # - 📚 (3) اقرأ واكتب مع ضبط أواخر الكلمات.
            # - (4) اقـرأ؟
            # - 📚 - اقرأ واكتب مع ضبط أواخر الكلمات:
            # - (5) كون جملاً مفيدة...
            # - (6) صَحِّحْ التركيبات...
            # - (7) محمدٌ : يا محمدُ
            # - (8) اِقرأْ المثال الآتي...
            # - (9) اِسمٌ : اِسْمُ الولد...
            is_tam = False
            tam_name = ""
            
            if l.startswith('#### ✍️ تمرين') or l.startswith('#### ✍️ تمـرين') or l.startswith('#### ✍️ التَّمْرِينُ'):
                is_tam = True
                tam_name = l.replace('#', '').replace('✍️', '').strip()
            elif re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', l):
                m = re.match(r'^-\s*(?:📚\s*)?\((\d+)\)\s*(.+)', l)
                is_tam = True
                tam_name = f"تمرين ({m.group(1)}): {m.group(2).strip()}"
            elif l.startswith('- 📚') and any(k in l for k in ['اقرأ', 'اِقرأ', 'اِقْرَأْ']):
                is_tam = True
                tam_name = l.lstrip('- 📚').strip()
            elif l.startswith('- اقرأ ما يلي مراعيا') or l.startswith('- اقرأ ما يلي'):
                is_tam = True
                tam_name = l.lstrip('- ').strip()
                
            if is_tam:
                cumulative_tamreen_count += 1
                current_tam = {
                    'local_num': len(tamreens) + 1,
                    'cumulative_num': cumulative_tamreen_count,
                    'header': tam_name,
                    'items': []
                }
                tamreens.append(current_tam)
            elif current_tam is not None and l.startswith('- ') and not l.startswith('#### 🗂️'):
                clean_item = l.lstrip('- ').strip()
                if clean_item and not clean_item.startswith('---'):
                    current_tam['items'].append(clean_item)
                    
        lessons.append({
            'title': title_ar,
            'raw_header': header,
            'tamreens': tamreens
        })
        
    return lessons

b1_lessons = parse_book_lessons(b1_text, 1)
print(f"Book 1: {len(b1_lessons)} lessons")
for i, l in enumerate(b1_lessons[:6]):
    print(f"\n--- Lesson {i+1}: {l['title']} ({len(l['tamreens'])} Tamreens) ---")
    for t in l['tamreens']:
        print(f"  [Tamreen {t['cumulative_num']} (Local {t['local_num']})]: {t['header'][:65]} ({len(t['items'])} items)")
