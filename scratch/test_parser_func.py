import re, json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

# Author's TOC start pages
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

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo_md = f.read()

b1_idx = cairo_md.find('## 📗')
b2_idx = cairo_md.find('## 📘')
b3_idx = cairo_md.find('## 📙')

b1_secs = re.split(r'\n###\s+', cairo_md[b1_idx:b2_idx])[1:]
b2_secs = re.split(r'\n###\s+', cairo_md[b2_idx:b3_idx])[2:]
b3_secs = re.split(r'\n###\s+', cairo_md[b3_idx:])[2:]

def parse_lesson_items(sec_text, start_page, end_page, book_num, lesson_num):
    lines = [l.strip() for l in sec_text.split('\n') if l.strip()]
    items = []
    
    # We step through the text and extract all exercises and snippets
    # Calculate approximate page progression
    total_lines = len(lines)
    
    i = 0
    while i < len(lines):
        line = lines[i]
        clean = re.sub(r'^[^\w\(\)\[\]]+', '', line).strip()
        
        # Approximate page number within lesson
        line_ratio = i / max(total_lines, 1)
        est_page = start_page + int(line_ratio * (end_page - start_page + 1))
        est_page = min(est_page, end_page)
        
        is_ex = False
        badge = ""
        desc = ""
        
        # Match numbered exercise "1-", "2-", "(1)", etc.
        m_num = re.match(r'^(?:(?:\(([0-9]+|[۱-۹]+)\)|([0-9]+|[۱-۹]+))\s*[\-\.]\s*)(.*)', clean)
        if m_num:
            num = m_num.group(1) or m_num.group(2)
            rest = m_num.group(3).lstrip('•').strip()
            if len(rest) > 2 and not rest.startswith('http'):
                is_ex = True
                badge = f"تَمْرِين ({num})"
                desc = rest
        elif line.startswith('#### ✍️') and not any(k in line for k in ['تمارين', 'تـمـارين', 'تَمَارِيْن']):
            is_ex = True
            badge = re.sub(r'[#✍️\s]+', ' ', line).strip()
            desc = "تمرين كتابي وتطبيقي"
        elif any(k in line for k in ['محمدٌ : يا محمدُ', 'اسم الولد', 'ابن خالد', 'الحروف الشمسية', 'الممنوع من الصرف', 'تأمل ما يلي', 'تأمل المثال', 'هذه أمثلة', 'إسناد']):
            is_ex = True
            badge = "قَاعِدَةٌ / ضَابِطٌ (Snippet)"
            desc = line.lstrip('- •').strip()
        elif line.startswith('- 📚') or (line.startswith('- اقرأ') and not is_ex):
            is_ex = True
            badge = "تَمْرِينُ قِرَاءَةٍ وَضَبْطٍ (Reading Drill)"
            desc = line.lstrip('- 📚').strip()
            
        if is_ex:
            # Collect following sub-lines until next exercise
            sub_lines = []
            j = i + 1
            while j < len(lines):
                next_l = lines[j]
                clean_next = re.sub(r'^[^\w\(\)\[\]]+', '', next_l).strip()
                if re.match(r'^(?:(?:\(([0-9]+|[۱-۹]+)\)|([0-9]+|[۱-۹]+))\s*[\-\.]\s*)', clean_next) or \
                   (next_l.startswith('#### ✍️') and not any(k in next_l for k in ['تمارين', 'تـمـارين', 'تَمَارِيْن'])) or \
                   any(k in next_l for k in ['محمدٌ : يا محمدُ', 'اسم الولد', 'ابن خالد', 'الحروف الشمسية', 'الممنوع من الصرف', 'تأمل ما يلي', 'تأمل المثال', 'هذه أمثلة', 'إسناد']) or \
                   next_l.startswith('- 📚') or next_l.startswith('#### 🗂️') or next_l.startswith('---'):
                    break
                sub_lines.append(next_l)
                j += 1
                
            # Count questions / parts in sub_lines
            content = " ".join(sub_lines)
            nums = set(re.findall(r'\(([0-9]+|[۱-۹]+)\)', content))
            count = len(nums)
            if count == 0:
                bullets = sum(1 for sl in sub_lines if sl.startswith('- ') and len(sl) > 5)
                words = [w for w in re.split(r'[,،•\.\s]+', content) if len(w) > 2 and not w.startswith('http')]
                if 'ضبط' in (badge + desc):
                    count = max(bullets, len(words), 1)
                else:
                    count = max(bullets, 1)
            
            # Refine description
            clean_desc = re.sub(r'[^\w\s\(\)\[\]\u0600-\u06ff\-\:\.\،\؟]', '', desc).strip()
            if not clean_desc and sub_lines:
                clean_desc = re.sub(r'[^\w\s\(\)\[\]\u0600-\u06ff\-\:\.\،\؟]', '', sub_lines[0]).strip()
            if not clean_desc:
                clean_desc = "تدريب تطبيقي على الدرس"
                
            items.append({
                'book_num': book_num,
                'lesson_num': lesson_num,
                'page': est_page,
                'badge': badge,
                'desc': clean_desc[:85],
                'count': count
            })
            i = j - 1
        i += 1
        
    return items

print("Parser function ready.")
