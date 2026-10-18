import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b1_secs = re.split(r'\n###\s+', text[b1_idx:b2_idx])[1:]
b2_secs = re.split(r'\n###\s+', text[b2_idx:b3_idx])[2:] # Skip Muqaddimah
b3_secs = re.split(r'\n###\s+', text[b3_idx:])[2:] # Skip Muqaddimah

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

# Let's write a function to parse a book's lessons into tamreens and snippets
def parse_book(secs, b_num, page_map):
    book_results = []
    
    for l_idx, s in enumerate(secs, 1):
        lines = [l.strip() for l in s.split('\n') if l.strip()]
        header = lines[0]
        # Clean header
        clean_title = re.sub(r'[^\w\s\(\)\u0600-\u06ff—\-\:]', '', header).strip()
        parts = clean_title.split('—')
        title_ar = parts[0].strip()
        topic_desc = parts[1].strip() if len(parts) > 1 else ""
        
        start_p = page_map.get(l_idx, 0)
        end_p = page_map.get(l_idx + 1, start_p + 4) - 1 if l_idx < len(secs) else (123 if b_num==1 else (223 if b_num==2 else 144))
        
        # Scan lines to find tamreens and snippets
        items = []
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check for exercise header or snippet
            is_tamreen = False
            tam_name = ""
            tam_desc = ""
            
            # Pattern 1: "#### ✍️ تمرين (X)"
            if line.startswith('#### ✍️') and not any(k in line for k in ['تـمـــــارين', 'تَمَارِيْنُ', 'تـمـــارين', 'تَمَـارِيْن', 'تمارين']):
                is_tamreen = True
                tam_name = re.sub(r'[#✍️\s]+', ' ', line).strip()
            # Pattern 2: "- 1- أجب..." or "- (1) أجب..."
            elif re.match(r'^-\s*(?:[0-9]+|[۱-۹]+|\([0-9]+\))\s*[\-\.]\s*(.*)', line):
                m = re.match(r'^-\s*([0-9]+|[۱-۹]+|\([0-9]+\))\s*[\-\.]\s*(.*)', line)
                is_tamreen = True
                t_num = m.group(1).strip('()')
                tam_name = f"تَمْرِين ({t_num})"
                tam_desc = m.group(2).strip()
            # Pattern 3: "- (X) ..."
            elif re.match(r'^-\s*\(([0-9]+|[۱-۹]+)\)\s*(.*)', line):
                m = re.match(r'^-\s*\(([0-9]+|[۱-۹]+)\)\s*(.*)', line)
                is_tamreen = True
                t_num = m.group(1)
                tam_name = f"تَمْرِين ({t_num})"
                tam_desc = m.group(2).strip()
            # Pattern 4: Grammatical snippets
            elif any(k in line for k in ['محمدٌ : يا محمدُ', 'اِسمٌ :', 'اِبْنٌ :', 'الحروف القمرية والحروف الشمسية', 'الممنوع من الصرف', 'تأمل ما يلي', 'تأمل المثال', 'هذه أمثلة', 'إسناد']):
                if not line.startswith('####'):
                    is_tamreen = True
                    tam_name = "قَاعِدَةٌ نَحْوِيَّةٌ (Snippet)"
                    tam_desc = line.lstrip('- ').strip()
            # Pattern 5: "اقرأ واكتب" or "اقرأ ما يلي"
            elif line.startswith('- 📚') or line.startswith('- اقرأ') or line.startswith('- اِقْرَأْ'):
                is_tamreen = True
                tam_name = "تَمْرِينُ الْقِرَاءَةِ وَالضَّبْطِ (Reading Drill)"
                tam_desc = line.lstrip('- 📚').strip()
                
            if is_tamreen:
                # Gather content lines for this exercise
                sub_lines = []
                j = i + 1
                while j < len(lines):
                    next_l = lines[j]
                    if next_l.startswith('#### ✍️') or next_l.startswith('#### 🗂️') or next_l.startswith('---'):
                        break
                    if re.match(r'^-\s*(?:[0-9]+|[۱-۹]+|\([0-9]+\))\s*[\-\.]\s*(.*)', next_l) or \
                       re.match(r'^-\s*\(([0-9]+|[۱-۹]+)\)\s*(أجب|أضف|اقرأ|اِقْرَأْ|كوّن|كون|صَحِّحْ|صحح|تأمل|اختر|املأ|اِمْلَأْ|هات|صل|ضع|عين|أدخل|حول)', next_l) or \
                       any(k in next_l for k in ['محمدٌ : يا محمدُ', 'اِسمٌ :', 'اِبْنٌ :', 'الحروف القمرية والحروف الشمسية']):
                        break
                    sub_lines.append(next_l)
                    j += 1
                
                # Count questions in sub_lines
                # 1. Count numbered sub-items like (1), (2), (3)...
                content_blob = " ".join(sub_lines)
                numbered = re.findall(r'\(([0-9]+|[۱-۹]+)\)', content_blob)
                num_count = len(set(numbered)) if numbered else 0
                
                # If no (1), (2)... count list items or bullet points
                if num_count == 0:
                    bullet_count = sum(1 for sl in sub_lines if sl.startswith('- ') and len(sl) > 5)
                    # or count comma-separated words in reading drill
                    words = [w for w in re.split(r'[,،•\.\s]+', content_blob) if len(w) > 2 and not w.startswith('http')]
                    if 'واكتب مع ضبط' in (tam_name + tam_desc) or 'ضبط أواخر' in (tam_name + tam_desc):
                        count = max(bullet_count, len(words))
                    else:
                        count = max(bullet_count, 1)
                else:
                    count = num_count
                    
                # Clean description
                if not tam_desc and sub_lines:
                    tam_desc = sub_lines[0].lstrip('- 📚').strip()
                    
                items.append({
                    'name': tam_name,
                    'desc': tam_desc[:90],
                    'count': count,
                    'sample': content_blob[:120]
                })
                i = j - 1
            i += 1
            
        book_results.append({
            'lesson_num': l_idx,
            'title_ar': title_ar,
            'topic': topic_desc,
            'start_page': start_p,
            'end_page': end_p,
            'items': items
        })
    return book_results

b1_res = parse_book(b1_secs, 1, B1_PAGES)
print("Book 1 parsed:", len(b1_res), "lessons")
for l in b1_res[:5]:
    print(f"\n[L{l['lesson_num']}] {l['title_ar']} (pp. {l['start_page']}-{l['end_page']}): {len(l['items'])} tamreens/snippets")
    for it in l['items'][:4]:
        print(f"   - {it['name']}: {it['desc'][:50]} -> {it['count']} qs")
