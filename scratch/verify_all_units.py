import re, json, sys

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

b1_text = cairo_md[b1_idx:b2_idx]
b2_text = cairo_md[b2_idx:b3_idx]
b3_text = cairo_md[b3_idx:]

def extract_units(book_text, book_num, page_map):
    sections = re.split(r'\n###\s+', book_text)
    units_data = []
    
    # In Book 2 and 3, section 1 is Muqaddimah, so lessons start at section 2
    offset = 1 if book_num == 1 else 2
    
    total_lessons = 23 if book_num == 1 else (31 if book_num == 2 else 17)
    
    for l_num in range(1, total_lessons + 1):
        s_idx = l_num if book_num == 1 else l_num + 1
        if s_idx >= len(sections):
            break
        s_text = sections[s_idx]
        lines = [l.strip() for l in s_text.split('\n') if l.strip()]
        header = lines[0]
        title_ar = header.split('—')[0].replace('🏠', '').replace('⭐', '').replace('🌙', '').replace('🕌', '').replace('📖', '').replace('🚗', '').replace('🦆', '').replace('🏥', '').replace('🐦', '').replace('👨‍👩‍👦', '').replace('🏡', '').replace('👩‍⚕️', '').replace('👨‍🎓', '').replace('🌍', '').replace('👩‍🎓', '').replace('📚', '').replace('🏢', '').replace('⚖️', '').replace('🔢', '').replace('🧮', '').replace('🏫', '').replace('🎨', '').replace('🏛️', '').strip()
        subtitle_ar = header.split('—')[1].strip() if '—' in header else ''
        
        start_page = page_map.get(l_num, 0)
        end_page = page_map.get(l_num + 1, start_page + 4) - 1
        
        units_data.append({
            'book_num': book_num,
            'lesson_num': l_num,
            'title_ar': title_ar,
            'subtitle_ar': subtitle_ar,
            'start_page': start_page,
            'end_page': end_page,
            'raw_text': s_text
        })
    return units_data

b1_units = extract_units(b1_text, 1, B1_PAGES)
b2_units = extract_units(b2_text, 2, B2_PAGES)
b3_units = extract_units(b3_text, 3, B3_PAGES)

print(f"Extracted: Book 1 = {len(b1_units)} units, Book 2 = {len(b2_units)} units, Book 3 = {len(b3_units)} units")
