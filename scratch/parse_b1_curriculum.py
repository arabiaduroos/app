import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect Book 1 exercises from HTML and cross-reference with PDF
with open('transcriptions/Madinah-Book-1.html', 'r', encoding='utf-8') as f:
    b1_html = f.read()

# Split Book 1 into lessons
b1_units = re.findall(r'<section class="unit-card" id="b1_u(\d+)">([\s\S]*?)(?=</section>)', b1_html)
print(f"Book 1 units: {len(b1_units)}")

# For each unit, extract all lines and identify all tamreens and snippets
b1_data = []

# Lesson page starts from author TOC
b1_pages = {
    1: 5, 2: 12, 3: 14, 4: 21, 5: 27, 6: 33, 7: 39, 8: 42, 9: 47,
    10: 54, 11: 61, 12: 63, 13: 68, 14: 82, 15: 87, 16: 92, 17: 96,
    18: 100, 19: 105, 20: 109, 21: 114, 22: 117, 23: 120
}

for u_num, u_content in b1_units:
    u_num = int(u_num)
    start_p = b1_pages.get(u_num, 0)
    end_p = b1_pages.get(u_num + 1, 124) - 1 if u_num < 23 else 123
    
    # Extract unit title
    m_t = re.search(r'<h2 class="unit-title">([\s\S]*?)</h2>', u_content)
    title = re.sub(r'<[^>]+>', '', m_t.group(1)).strip() if m_t else f"Unit {u_num}"
    
    print(f"\n--- Book 1 Unit {u_num}: {title} (pp. {start_p}-{end_p}) ---")
    
    # Find all divs with class "txt-line", "sec-hdr", "illus-line", "emoji-grid"
    # To understand all parts
    lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>', u_content)
    
    # Let's see what exercises/snippets are in this lesson
    cur_label = ""
    cur_items = []
    
    for l in lines:
        clean = re.sub(r'<[^>]+>', '', l).strip()
        # Check if line is an exercise header or snippet header
        # E.g. (1) أجب..., (2) اقرأ..., اقرأ واكتب..., محمد : يا محمد, اسم : اسم الولد..., etc.
        is_hdr = False
        if re.match(r'^\(?\d+\)?\s*(أجب|أضف|اقرأ|اِقْرَأْ|كوّن|كون|صَحِّحْ|صحح|تأمل|اختر|املأ|اِمْلَأْ|هات|صل|ضع|عين|أدخل|حول)', clean):
            is_hdr = True
        elif 'اقرأ واكتب' in clean or 'اقرأ ما يلي' in clean or 'اقرأ المثال' in clean:
            is_hdr = True
        elif clean.startswith('(أ)') or clean.startswith('(ب)') or clean.startswith('(ج)'):
            is_hdr = True
        elif 'يا محمد' in clean or 'اسم الولد' in clean or 'ابن خالد' in clean or 'الحروف الشمسية' in clean:
            is_hdr = True
            
        if is_hdr:
            if cur_label and cur_items:
                print(f"  * {cur_label[:50]} -> {len(cur_items)} items")
            cur_label = clean
            cur_items = []
        else:
            if cur_label:
                cur_items.append(clean)
                
    if cur_label and cur_items:
        print(f"  * {cur_label[:50]} -> {len(cur_items)} items")
