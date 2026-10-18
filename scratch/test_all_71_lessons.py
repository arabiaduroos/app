import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b1_secs = re.split(r'\n###\s+', text[b1_idx:b2_idx])[1:]
b2_secs = re.split(r'\n###\s+', text[b2_idx:b3_idx])[2:]
b3_secs = re.split(r'\n###\s+', text[b3_idx:])[2:]

B1_PAGES = {
    1: 5, 2: 12, 3: 14, 4: 21, 5: 27, 6: 33, 7: 39, 8: 42, 9: 47,
    10: 54, 11: 61, 12: 63, 13: 68, 14: 82, 15: 87, 16: 92, 17: 96,
    18: 100, 19: 105, 20: 109, 21: 114, 22: 117, 23: 120
}

B2_PAGES = {
    1: 5, 2: 12, 3: 18, 4: 26, 5: 30, 6: 36, 7: 46, 8: 55, 9: 59,
    10: 69, 11: 74, 12: 84, 13: 91, 14: 95, 15: 103, 16: 109, 17: 119,
    18: 127, 19: 133, 20: 138, 21: 144, 22: 153, 23: 154, 24: 161,
    25: 167, 26: 173, 27: 180, 28: 193, 29: 205, 30: 213, 31: 218
}

B3_PAGES = {
    1: 5, 2: 20, 3: 28, 4: 41, 5: 49, 6: 59, 7: 64, 8: 69, 9: 74,
    10: 83, 11: 89, 12: 96, 13: 104, 14: 113, 15: 118, 16: 132, 17: 141
}

def analyze_all_books():
    all_books_summary = []
    
    for b_num, (secs, p_map) in enumerate([(b1_secs, B1_PAGES), (b2_secs, B2_PAGES), (b3_secs, B3_PAGES)], 1):
        print(f"\n==================================================")
        print(f"               BOOK {b_num} (Lessons: {len(secs)})")
        print(f"==================================================")
        
        for l_idx, s in enumerate(secs, 1):
            lines = [l.strip() for l in s.split('\n') if l.strip()]
            header = lines[0]
            start_p = p_map.get(l_idx, 0)
            end_p = p_map.get(l_idx + 1, start_p + 4) - 1 if l_idx < len(secs) else (123 if b_num==1 else (223 if b_num==2 else 144))
            
            # Find all exercises using the clean regex
            ex_list = []
            for l in lines:
                clean = re.sub(r'^[^\w\(\)\[\]]+', '', l).strip()
                m = re.match(r'^([0-9]+)\s*[\-\.]\s*(.*)', clean)
                if m:
                    ex_num = m.group(1)
                    ex_title = m.group(2).lstrip('•').strip()
                    if len(ex_title) > 3 and not ex_title.startswith('http'):
                        ex_list.append((ex_num, ex_title))
                elif l.startswith('#### ✍️') and not any(k in l for k in ['تمارين', 'تـمـارين', 'تَمَارِيْن']):
                    t_name = re.sub(r'[#✍️\s]+', ' ', l).strip()
                    ex_list.append(('H', t_name))
                elif any(k in l for k in ['محمدٌ : يا محمدُ', 'اسم الولد', 'ابن خالد', 'الحروف الشمسية', 'الممنوع من الصرف']):
                    ex_list.append(('S', l.lstrip('- ').strip()))
            
            print(f"L{l_idx:2d} (pp. {start_p:3d}-{end_p:3d}): {header[:30]:30s} -> {len(ex_list)} exercises/snippets")

analyze_all_books()
