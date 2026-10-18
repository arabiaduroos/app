import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

def scan_book_html(file_path, book_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract all txt-line divs
    # Format: <div class="txt-line"><div>...</div><div class="ur">...</div></div>
    pattern = re.compile(r'<div class="txt-line"><div>(.*?)</div><div class="ur">(.*?)</div></div>', re.DOTALL)
    matches = pattern.findall(html)

    lessons = []
    current_lesson = None
    current_ex = None

    # Regex for lesson headers
    # e.g. الدرس الأول, الدرس الثاني, الدَّرْسُ الثَّالِثُ
    lesson_re = re.compile(r'^(?:🔹\s*)?(?:📖\s*)?(?:[0-9٠-٩]+\s*-\s*)?(الْدَّرْسُ|الدَّرْسُ|الدرس)\s+([^\n<]+)', re.IGNORECASE)
    
    # Regex for exercises
    # e.g. تمارين, تَمَارِينُ, 1- أجب, 2- اقرأ, تمرين (1)
    ex_num_re = re.compile(r'^(?:[🔹\s*|🐪|🏫|👨‍🎓|📖|✍️|\*]*)([0-9٠-٩]+|[أ-ي])\s*[-–\.:]\s*(.+)', re.IGNORECASE)
    tamreen_word_re = re.compile(r'(تمارين|تَمَارِينُ|تَمْرِينٌ|التَّمْرِينُ|تمرين)', re.IGNORECASE)

    for ar, ur in matches:
        ar_clean = re.sub(r'<[^>]+>', '', ar).strip()
        ur_clean = re.sub(r'<[^>]+>', '', ur).strip()
        
        # Check if lesson header
        l_match = lesson_re.search(ar_clean)
        if l_match and not 'يشترك' in ar_clean and not 'خطوات' in ar_clean:
            title = l_match.group(0).strip()
            # If not duplicate
            if not current_lesson or current_lesson['title'] != title:
                current_lesson = {
                    'title': title,
                    'title_ur': ur_clean,
                    'exercises': []
                }
                lessons.append(current_lesson)
                current_ex = None
                continue

        if current_lesson:
            # Check if this line is an exercise heading
            # Case A: Explicit exercise number like "1- أجب عن الأسئلة الآتية" or "2- ضع علامة"
            ex_match = ex_num_re.search(ar_clean)
            if ex_match:
                ex_num = ex_match.group(1).strip()
                ex_inst = ex_match.group(2).strip()
                # filter out sub-questions like (1) or bullet points that are not top-level instructions
                if not ar_clean.startswith('(') and any(w in ex_inst for w in ['أجب', 'اقرأ', 'تأمل', 'أدخل', 'ضع', 'املأ', 'حول', 'عين', 'استخرج', 'هات', 'صل', 'كون', 'استعمل', 'صغ', 'اكتب', 'اضبط', 'بين']):
                    current_ex = {
                        'num': ex_num,
                        'instruction_ar': ex_inst,
                        'instruction_ur': ur_clean,
                        'items_count': 0
                    }
                    current_lesson['exercises'].append(current_ex)
                    continue
            elif 'تمرين' in ar_clean:
                current_ex = {
                    'num': str(len(current_lesson['exercises']) + 1),
                    'instruction_ar': ar_clean,
                    'instruction_ur': ur_clean,
                    'items_count': 0
                }
                current_lesson['exercises'].append(current_ex)
                continue

            if current_ex:
                current_ex['items_count'] += 1

    return lessons

b1 = scan_book_html('transcriptions/Madinah-Book-1.html', 'Book 1')
b2 = scan_book_html('transcriptions/Madinah-Book-2.html', 'Book 2')
b3 = scan_book_html('transcriptions/Madinah-Book-3.html', 'Book 3')

print(f"Book 1: {len(b1)} lessons found")
for l in b1[:5]:
    print(f"  {l['title']} -> {len(l['exercises'])} exercises")
    for ex in l['exercises']:
        print(f"    [{ex['num']}] {ex['instruction_ar'][:50]}")

print(f"\nBook 2: {len(b2)} lessons found")
for l in b2[:5]:
    print(f"  {l['title']} -> {len(l['exercises'])} exercises")
    for ex in l['exercises']:
        print(f"    [{ex['num']}] {ex['instruction_ar'][:50]}")

print(f"\nBook 3: {len(b3)} lessons found")
for l in b3[:5]:
    print(f"  {l['title']} -> {len(l['exercises'])} exercises")
    for ex in l['exercises']:
        print(f"    [{ex['num']}] {ex['instruction_ar'][:50]}")
