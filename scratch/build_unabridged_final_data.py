import json, re, sys, os, random

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo_md = f.read()

# Authoritative printed pages
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

# Helpers
def make_vocalization_opts(correct_word):
    clean = correct_word.strip()
    base = re.sub(r'[\u064b-\u0652]$', '', clean)
    opt_damma = base + 'ُ'
    opt_kasra = base + 'ِ'
    opt_fatha = base + 'َ'
    opt_tanween = base + 'ٌ' if not clean.startswith('ال') else base + 'ُ'
    
    opts = [clean]
    for c in [opt_kasra, opt_damma, opt_fatha, opt_tanween, base + 'ْ']:
        if c != clean and c not in opts:
            opts.append(c)
        if len(opts) == 4:
            break
    while len(opts) < 4:
        opts.append(base + 'ـ')
    random.shuffle(opts)
    return opts

def make_sentence_reading_opts(ar_text, ur_trans, en_trans):
    ur_base = ur_trans or ar_text
    en_base = en_trans or ar_text
    correct_opt = f"{ur_base} • {en_base}"
    distractor_templates = [
        ("یہ چیز اسکول میں ہے", "This is in the school"),
        ("وہ قلم میز پر ہے", "That pen is on the desk"),
        ("استاد کلاس روم سے نکلے", "The teacher left the classroom"),
        ("طالب علم یونیورسٹی میں گیا", "The student went to the university"),
        ("یہ ایک خوبصورت کتاب ہے", "This is a beautiful book"),
        ("گھر مسجد کے قریب ہے", "The house is near the mosque")
    ]
    opts = [correct_opt]
    for ur_d, en_d in distractor_templates:
        cand = f"{ur_d} • {en_d}"
        if cand != correct_opt and cand not in opts:
            opts.append(cand)
        if len(opts) == 4:
            break
    random.shuffle(opts)
    return opts

def make_mcq_opts(correct_ans, alt_pool):
    opts = [correct_ans]
    for alt in alt_pool:
        if alt != correct_ans and alt not in opts:
            opts.append(alt)
        if len(opts) == 4:
            break
    defaults = ["نَعَمْ", "لَا", "صَحِيحٌ", "خَاطِئٌ", "فِي الْمَسْجِدِ", "عَلَى الْمَكْتَبِ", "فِي الْبَيْتِ"]
    for d in defaults:
        if len(opts) >= 4: break
        if d != correct_ans and d not in opts:
            opts.append(d)
    random.shuffle(opts)
    return opts

b1_idx = cairo_md.find('## 📗')
b2_idx = cairo_md.find('## 📘')
b3_idx = cairo_md.find('## 📙')

b1_secs = re.split(r'\n###\s+', cairo_md[b1_idx:b2_idx])[1:]
b2_secs = re.split(r'\n###\s+', cairo_md[b2_idx:b3_idx])[2:]
b3_secs = re.split(r'\n###\s+', cairo_md[b3_idx:])[2:]

def extract_exercises_from_lines(lines, default_page=5):
    cur_ex = None
    exercises = []
    for idx, line in enumerate(lines):
        clean = re.sub(r'^[^\w\(\)\[\]]+', '', line).strip()
        m_num = re.match(r'^(?:(?:\(([0-9]+|[۱-۹]+)\)|([0-9]+|[۱-۹]+))\s*[\-\.]?\s*)(.*)', clean)
        if m_num and any(w in m_num.group(3) for w in ['أجب', 'أضف', 'اقرأ', 'اِقْرَأْ', 'كون', 'كوّن', 'صَحِّحْ', 'صحح', 'تأمل', 'اختر', 'املأ', 'اِمْلَأْ', 'هات', 'صل', 'استخرج', 'أدخل', 'حول', 'عين', 'اضبط', 'ضع', 'ما هذه', 'صلاة', 'إقرأ', 'أكمل', 'ثنّ', 'ثَنِّ']):
            if cur_ex:
                exercises.append(cur_ex)
            num = m_num.group(1) or m_num.group(2)
            cur_ex = {'num': num, 'desc': m_num.group(3).lstrip('•').strip(), 'lines': [], 'line_idx': idx}
        elif cur_ex:
            if line.startswith('#### 🗂️') or line.startswith('---'):
                exercises.append(cur_ex)
                cur_ex = None
            else:
                cur_ex['lines'].append(line)
    if cur_ex:
        exercises.append(cur_ex)
    return exercises

def process_exercise_to_questions(ex, b_num, u_idx, t_num, p_val):
    raw_t = " ".join(ex['lines'])
    parts = re.findall(r'\(([0-9]+|[۱-۹]+)\)\s*([^\(\)]+)', raw_t)
    if not parts:
        clean_lines = [l.lstrip('-• 📚').strip() for l in ex['lines'] if len(l.strip()) > 3 and not l.startswith('####')]
        parts = [(str(i), l) for i, l in enumerate(clean_lines, 1)]
    if not parts:
        parts = [('1', ex['desc'])]
    
    questions = []
    alt_pool = [x[1].strip() for x in parts if x[1].strip()]
    for p_idx, (p_num, p_text) in enumerate(parts, 1):
        p_clean = p_text.strip().rstrip('.•-')
        q_id = f"b{b_num}_u{u_idx}_t{t_num}_q{p_idx}"
        q_type = "mcq"
        if any(w in ex['desc'] for w in ['ضبط', 'اضبط']):
            q_type = "vocalization"
            options = make_vocalization_opts(p_clean)
        elif any(w in ex['desc'] for w in ['املأ', 'الفراغ', 'ضع']):
            q_type = "fill_blank"
            options = make_mcq_opts(p_clean, alt_pool)
        elif any(w in ex['desc'] for w in ['أجب']):
            q_type = "dialogue_qa"
            options = make_mcq_opts(p_clean, alt_pool)
        else:
            q_type = "sentence_reading"
            options = make_mcq_opts(p_clean, alt_pool)
            
        questions.append({
            "id": q_id,
            "book": b_num,
            "unit_num": u_idx,
            "tamreen_num": t_num,
            "badge_ar": f"التَّمْرِينُ ({t_num})",
            "badge_ur": f"مشق ({t_num}): سوال ({p_idx})",
            "badge_en": f"Exercise ({t_num}): Question ({p_idx})",
            "tamreen_title_ar": ex['desc'][:70],
            "tamreen_title_ur": f"مشق ({t_num}): {ex['desc'][:50]}",
            "tamreen_title_en": f"Exercise ({t_num}): {ex['desc'][:50]}",
            "grammar_goal_ur": f"کتاب {b_num}، سبق {u_idx} کی مشق ({t_num}) کا فہم و حل۔",
            "grammar_goal_en": f"Practice drill for Book {b_num}, Lesson {u_idx}, Exercise {t_num}.",
            "type": q_type,
            "strict_tashkeel": True,
            "prompt_ar": f"({p_idx}) {p_clean}",
            "prompt_ur": f"سوال ({p_idx}): کتاب کے مطابق صحیح جواب منتخب کریں۔",
            "prompt_en": f"Question ({p_idx}): Choose the correct answer according to the lesson.",
            "answer": p_clean,
            "options": options,
            "emoji": "✍️",
            "hint_ur": "سبق کے قواعد کے مطابق حل کریں۔",
            "hint_en": "Solve according to the rules of this lesson.",
            "explanation_ur": f"کتاب کے مطابق درست جواب '{p_clean}' ہے۔",
            "explanation_en": f"According to the textbook, the correct answer is '{p_clean}'."
        })
    return questions

# Detailed Book 1 Builder
def build_book_1_complete():
    b1_units = []
    b1_source_units = master_data['books'][0]['units']
    
    for u_idx in range(1, 24):
        src_u = b1_source_units[u_idx - 1] if u_idx - 1 < len(b1_source_units) else {}
        u_copy = dict(src_u)
        p_start = B1_PAGES[u_idx]
        p_end = B1_PAGES.get(u_idx + 1, p_start + 4) - 1 if u_idx < 23 else 123
        
        curriculum_flow = []
        unit_questions = []
        
        preview_text = ""
        for bl in u_copy.get('blocks', []):
            if bl.get('text'):
                preview_text = bl['text'][:120]
                break
        
        # Nas-ud-Dars
        curriculum_flow.append({
            "id": f"b1_u{u_idx}_item_nas",
            "type": "nasuddars",
            "item_order": 1,
            "title_ar": "نَصُّ الدَّرْسِ (الْقِرَاءَةُ وَالْمُطَالَعَةُ)",
            "title_ur": "سبق کا متن و مطالعہ",
            "title_en": "Lesson Reading & Core Text",
            "page": p_start,
            "preview": preview_text or u_copy.get('title_ar', '')
        })
        
        s = b1_secs[u_idx - 1] if u_idx - 1 < len(b1_secs) else ""
        lines = [l.strip() for l in s.split('\n') if l.strip()]
        
        # Specific overrides for Lessons 1, 3, 4, 5
        if u_idx == 1:
            # Lesson 1 snippets and tamreens
            curriculum_flow.append({
                "id": "b1_u1_snip1", "type": "qaida", "item_order": 2,
                "title_ar": "قَاعِدَةٌ: اسْمُ الإِشَارَةِ لِلْمُذَكَّرِ الْقَرِيبِ (هٰذَا)",
                "title_ur": "قاعدہ: اسم اشارہ برائے مذکر قریب (هٰذَا: یہ)",
                "title_en": "Rule Snippet: Demonstrative for Near Masculine (هٰذَا - This)",
                "page": 5,
                "rule_summary_ur": "اسم اشارہ 'هٰذَا' نزدیک کی مذکر چیز کی طرف اشارہ کرنے کے لیے استعمال ہوتا ہے، جیسے: هٰذَا بَيْتٌ۔",
                "rule_summary_en": "'هٰذَا' points to near masculine objects (e.g. هٰذَا بَيْتٌ).",
                "examples": [
                    {"ar": "هٰذَا بَيْتٌ", "ur": "یہ ایک گھر ہے", "en": "This is a house"},
                    {"ar": "هٰذَا مَسْجِدٌ", "ur": "یہ ایک مسجد ہے", "en": "This is a mosque"},
                    {"ar": "هٰذَا بَابٌ", "ur": "یہ ایک دروازہ ہے", "en": "This is a door"},
                    {"ar": "هٰذَا كِتَابٌ", "ur": "یہ ایک کتاب ہے", "en": "This is a book"}
                ]
            })
            # T1: 6 questions
            curriculum_flow.append({
                "id": "b1_u1_t1", "type": "tamreen", "item_order": 3, "tamreen_num": 1,
                "title_ar": "تَمْرِين (١): مَا هٰذَا؟ — التَّعَرُّفُ عَلَى الصُّوَرِ",
                "title_ur": "مشق (1): تصویر دیکھ کر پہچانیں (مَا هٰذَا؟)",
                "title_en": "Exercise (1): Identify objects (مَا هٰذَا؟)",
                "page": 7, "question_count": 6
            })
            t1_items = [
                ("🔑", "مَا هٰذَا؟", "هٰذَا مِفْتَاحٌ", "یہ کیا ہے؟", "What is this?", "یہ ایک چابی ہے", "This is a key", ["هٰذَا مِفْتَاحٌ", "هٰذَا كِتَابٌ", "هٰذَا قَلَمٌ", "هٰذَا بَابٌ"]),
                ("📖", "مَا هٰذَا؟", "هٰذَا كِتَابٌ", "یہ کیا ہے؟", "What is this?", "یہ ایک کتاب ہے", "This is a book", ["هٰذَا كِتَابٌ", "هٰذَا مِفْتَاحٌ", "هٰذَا قَلَمٌ", "هٰذَا بَيْتٌ"]),
                ("🖊️", "مَا هٰذَا؟", "هٰذَا قَلَمٌ", "یہ کیا ہے؟", "What is this?", "یہ ایک قلم ہے", "This is a pen", ["هٰذَا قَلَمٌ", "هٰذَا كِتَابٌ", "هٰذَا كُرْسِيٌّ", "هٰذَا بَابٌ"]),
                ("🚪", "مَا هٰذَا؟", "هٰذَا بَابٌ", "یہ کیا ہے؟", "What is this?", "یہ ایک دروازہ ہے", "This is a door", ["هٰذَا بَابٌ", "هٰذَا بَيْتٌ", "هٰذَا مَسْجِدٌ", "هٰذَا مِفْتَاحٌ"]),
                ("🏠", "مَا هٰذَا؟", "هٰذَا بَيْتٌ", "یہ کیا ہے؟", "What is this?", "یہ ایک گھر ہے", "This is a house", ["هٰذَا بَيْتٌ", "هٰذَا مَسْجِدٌ", "هٰذَا بَابٌ", "هٰذَا سَرِيرٌ"]),
                ("🪑", "مَا هٰذَا؟", "هٰذَا كُرْسِيٌّ", "یہ کیا ہے؟", "What is this?", "یہ ایک کرسی ہے", "This is a chair", ["هٰذَا كُرْسِيٌّ", "هٰذَا سَرِيرٌ", "هٰذَا مَكْتَبٌ", "هٰذَا بَابٌ"])
            ]
            for q_idx, it in enumerate(t1_items, 1):
                unit_questions.append({
                    "id": f"b1_u1_t1_q{q_idx}", "book": 1, "unit_num": 1, "tamreen_num": 1,
                    "badge_ar": "التَّمْرِينُ (١)", "badge_ur": "مشق (١): اسم اشارہ قریب", "badge_en": "Exercise (1): Demonstrative هٰذا",
                    "tamreen_title_ar": "مَا هٰذَا؟ — التَّعَرُّفُ عَلَى الصُّوَرِ", "tamreen_title_ur": "تصویر دیکھ کر پہچانیں (مَا هٰذَا؟)", "tamreen_title_en": "Identify objects (مَا هٰذَا؟)",
                    "grammar_goal_ur": "اسم اشارہ 'هٰذَا' کا صحیح استعمال اور اشیاء کی پہچان۔", "grammar_goal_en": "Accurate usage of demonstrative هٰذا.",
                    "type": "illustrated_qa", "strict_tashkeel": True,
                    "prompt_ar": f"{it[0]} {it[1]}", "prompt_ur": f"{it[3]} ({it[5]})", "prompt_en": f"{it[4]} ({it[6]})",
                    "answer": it[2], "options": it[7], "emoji": it[0], "hint_ur": it[5], "hint_en": it[6],
                    "explanation_ur": f"صحیح جواب '{it[2]}' ہے کیونکہ اشارہ نزدیک کی مذکر شے کی طرف ہے۔",
                    "explanation_en": f"Correct answer is '{it[2]}' pointing to near masculine noun."
                })
            # T2: 4 questions
            curriculum_flow.append({
                "id": "b1_u1_t2", "type": "tamreen", "item_order": 4, "tamreen_num": 2,
                "title_ar": "تَمْرِين (٢): أَهٰذَا...؟ — أَسْئِلَةُ التَّصْدِيقِ (نَعَمْ / لَا)",
                "title_ur": "مشق (2): تصدیقی سوالات (نَعَمْ اور لَا کے ساتھ)",
                "title_en": "Exercise (2): Verification questions (نَعَمْ / لَا)",
                "page": 8, "question_count": 4
            })
            t2_items = [
                ("🕌", "أَهٰذَا بَيْتٌ؟", "لَا، هٰذَا مَسْجِدٌ.", ["لَا، هٰذَا مَسْجِدٌ.", "نَعَمْ، هٰذَا بَيْتٌ.", "هٰذَا مِفْتَاحٌ.", "هٰذَا بَابٌ."], "کیا یہ گھر ہے؟", "Is this a house?"),
                ("🔑", "أَهٰذَا مِفْتَاحٌ؟", "نَعَمْ، هٰذَا مِفْتَاحٌ.", ["نَعَمْ، هٰذَا مِفْتَاحٌ.", "لَا، هٰذَا قَلَمٌ.", "هٰذَا كِتَابٌ.", "لَا، هٰذَا بَيْتٌ."], "کیا یہ چابی ہے؟", "Is this a key?"),
                ("👕", "أَهٰذَا قَمِيصٌ؟", "نَعَمْ، هٰذَا قَمِيصٌ.", ["نَعَمْ، هٰذَا قَمِيصٌ.", "لَا، هٰذَا مَسْجِدٌ.", "هٰذَا سَرِيرٌ.", "لَا، هٰذَا مِفْتَاحٌ."], "کیا یہ قمیض ہے؟", "Is this a shirt?"),
                ("⭐", "أَهٰذَا نَجْمٌ؟", "نَعَمْ، هٰذَا نَجْمٌ.", ["نَعَمْ، هٰذَا نَجْمٌ.", "لَا، هٰذَا قَمَرٌ.", "هٰذَا كُرْسِيٌّ.", "لَا، هٰذَا بَابٌ."], "کیا یہ ستارہ ہے؟", "Is this a star?")
            ]
            for q_idx, it in enumerate(t2_items, 1):
                unit_questions.append({
                    "id": f"b1_u1_t2_q{q_idx}", "book": 1, "unit_num": 1, "tamreen_num": 2,
                    "badge_ar": "التَّمْرِينُ (٢)", "badge_ur": "مشق (٢): تصدیق و نفی", "badge_en": "Exercise (2): Verification",
                    "tamreen_title_ar": "أَهٰذَا...؟ — أَسْئِلَةُ التَّصْدِيقِ (نَعَمْ / لَا)", "tamreen_title_ur": "تصدیقی سوالات (نَعَمْ اور لَا کے ساتھ)", "tamreen_title_en": "Verification questions (نَعَمْ / لَا)",
                    "grammar_goal_ur": "استفہام تصدیقی 'أَ' کا جواب نَعَمْ یا لَا سے دینا۔", "grammar_goal_en": "Answering verification questions using نَعَمْ or لَا.",
                    "type": "verification_qa", "strict_tashkeel": True,
                    "prompt_ar": f"{it[0]} {it[1]}", "prompt_ur": it[4], "prompt_en": it[5],
                    "answer": it[2], "options": it[3], "emoji": it[0], "hint_ur": "تصویر دیکھ کر تصدیق یا نفی کریں۔", "hint_en": "Observe image to verify.",
                    "explanation_ur": f"صحیح جواب '{it[2]}' ہے۔", "explanation_en": f"Correct answer is '{it[2]}'."
                })
            # T3: 9 sentences
            curriculum_flow.append({
                "id": "b1_u1_t3", "type": "tamreen", "item_order": 5, "tamreen_num": 3,
                "title_ar": "تَمْرِين (٣): اقْرَأْ وَاكْتُبْ — تَمْرِينُ ضَبْطِ الْكَلِمَاتِ",
                "title_ur": "مشق (3): پڑھیں اور اعراب کے ساتھ لکھیں",
                "title_en": "Exercise (3): Read and write with proper vowels",
                "page": 9, "question_count": 9
            })
            t3_sentences = [
                ("هٰذَا مَكْتَبٌ.", "یہ ایک میز ہے", "This is a desk", "🗄️"),
                ("هٰذَا مَسْجِدٌ.", "یہ ایک مسجد ہے", "This is a mosque", "🕌"),
                ("هٰذَا قَلَمٌ.", "یہ ایک قلم ہے", "This is a pen", "🖊️"),
                ("هٰذَا سَرِيرٌ.", "یہ ایک پلنگ ہے", "This is a bed", "🛏️"),
                ("مَا هٰذَا؟ هٰذَا كُرْسِيٌّ.", "یہ کیا ہے؟ یہ ایک کرسی ہے", "What is this? This is a chair", "🪑"),
                ("أَهٰذَا بَيْتٌ؟ لَا، هٰذَا مَسْجِدٌ.", "کیا یہ گھر ہے؟ نہیں، یہ مسجد ہے", "Is this a house? No, this is a mosque", "🕌"),
                ("مَا هٰذَا؟ هٰذَا مِفْتَاحٌ.", "یہ کیا ہے؟ یہ چابی ہے", "What is this? This is a key", "🔑"),
                ("هٰذَا كِتَابٌ.", "یہ ایک کتاب ہے", "This is a book", "📖"),
                ("هٰذَا بَابٌ.", "یہ ایک دروازہ ہے", "This is a door", "🚪")
            ]
            for q_idx, sent in enumerate(t3_sentences, 1):
                unit_questions.append({
                    "id": f"b1_u1_t3_q{q_idx}", "book": 1, "unit_num": 1, "tamreen_num": 3,
                    "badge_ar": "التَّمْرِينُ (٣)", "badge_ur": "مشق (٣): قراءت و کتابت", "badge_en": "Exercise (3): Reading & Writing",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ — تَمْرِينُ ضَبْطِ الْكَلِمَاتِ", "tamreen_title_ur": "پڑھیں اور اعراب کے ساتھ لکھیں", "tamreen_title_en": "Read and write with proper vowels",
                    "grammar_goal_ur": "اسم اشارہ کے جملوں کی درست قراءت اور تنوین کا تلفظ۔", "grammar_goal_en": "Reading demonstratives with tanween.",
                    "type": "sentence_reading", "strict_tashkeel": True,
                    "prompt_ar": f"{sent[3]} اقْرَأْ وَتَرْجِمْ: {sent[0]}", "prompt_ur": f"جملے کا صحیح ترجمہ منتخب کریں: ({sent[0]})", "prompt_en": f"Select translation: ({sent[0]})",
                    "answer": f"{sent[1]} • {sent[2]}", "options": make_sentence_reading_opts(sent[0], sent[1], sent[2]), "emoji": sent[3], "hint_ur": sent[1], "hint_en": sent[2],
                    "explanation_ur": f"جملہ '{sent[0]}' کا اردو ترجمہ '{sent[1]}' ہے۔", "explanation_en": f"Sentence '{sent[0]}' translates to '{sent[2]}'."
                })
            # Snippet 3
            curriculum_flow.append({
                "id": "b1_u1_snip3", "type": "qaida", "item_order": 6,
                "title_ar": "قَاعِدَةٌ: الِاسْتِفْهَامُ عَنِ الْعَاقِلِ بِـ (مَنْ هٰذَا؟)",
                "title_ur": "قاعدہ: عاقل کے لیے سوال (مَنْ هٰذَا؟: یہ کون ہے؟)",
                "title_en": "Rule Snippet: Questioning Rational Beings (مَنْ هٰذَا؟)",
                "page": 10,
                "rule_summary_ur": "انسانوں کے بارے میں سوال کے لیے 'مَنْ' (کون) استعمال ہوتا ہے، جبکہ بے جان کے لیے 'مَا' (کیا) آتا ہے۔",
                "rule_summary_en": "'مَنْ هٰذَا؟' is used exclusively for rational beings.",
                "examples": [
                    {"ar": "مَنْ هٰذَا؟ هٰذَا طَبِيبٌ", "ur": "یہ کون ہے؟ یہ ڈاکٹر ہے۔", "en": "Who is this? This is a doctor."},
                    {"ar": "مَنْ هٰذَا؟ هٰذَا وَلَدٌ", "ur": "یہ کون ہے؟ یہ لڑکا ہے۔", "en": "Who is this? This is a boy."}
                ]
            })
            # T4: 10 questions
            curriculum_flow.append({
                "id": "b1_u1_t4", "type": "tamreen", "item_order": 7, "tamreen_num": 4,
                "title_ar": "تَمْرِين (٤): اقْرَأْ وَاكْتُبْ — التَّفْرِيقُ بَيْنَ الْعَاقِلِ وَغَيْرِهِ",
                "title_ur": "مشق (4): عاقل اور غیر عاقل میں تفریق کی مشق",
                "title_en": "Exercise (4): Distinguishing Rational & Non-Rational",
                "page": 11, "question_count": 10
            })
            t4_items = [
                ("🖊️", "مَا هٰذَا؟ هٰذَا قَلَمٌ.", "یہ کیا ہے؟ یہ قلم ہے", "What is this? This is a pen"),
                ("🐕", "هٰذَا كَلْبٌ.", "یہ ایک کتا ہے", "This is a dog"),
                ("👨‍⚕️", "مَنْ هٰذَا؟ هٰذَا طَبِيبٌ.", "یہ کون ہے؟ یہ ڈاکٹر ہے", "Who is this? This is a doctor"),
                ("🐪", "هٰذَا جَمَلٌ.", "یہ ایک اونٹ ہے", "This is a camel"),
                ("🐈", "أَهٰذَا كَلْبٌ؟ لَا، هٰذَا قِطٌّ.", "کیا یہ کتا ہے؟ نہیں، یہ بلی ہے", "Is this a dog? No, this is a cat"),
                ("🐓", "أَهٰذَا دِيكٌ؟ نَعَمْ.", "کیا یہ مرغ ہے؟ جی ہاں", "Is this a rooster? Yes"),
                ("🐎", "أَهٰذَا حِصَانٌ؟ نَعَمْ، هٰذَا حِصَانٌ.", "کیا یہ گھوڑا ہے؟ جی ہاں، یہ گھوڑا ہے", "Is this a horse? Yes, this is a horse"),
                ("🧻", "مَا هٰذَا؟ هٰذَا مِنْدِيلٌ.", "یہ کیا ہے؟ یہ رومال ہے", "What is this? This is a handkerchief"),
                ("👨‍🏫", "مَنْ هٰذَا؟ هٰذَا مُدَرِّسٌ.", "یہ کون ہے؟ یہ استاد ہے", "Who is this? This is a teacher"),
                ("🧑‍💼", "مَنْ هٰذَا؟ هٰذَا تَاجِرٌ.", "یہ کون ہے؟ یہ تاجر ہے", "Who is this? This is a merchant")
            ]
            for q_idx, it in enumerate(t4_items, 1):
                unit_questions.append({
                    "id": f"b1_u1_t4_q{q_idx}", "book": 1, "unit_num": 1, "tamreen_num": 4,
                    "badge_ar": "التَّمْرِينُ (٤)", "badge_ur": "مشق (٤): عاقل و غیر عاقل", "badge_en": "Exercise (4): Rational vs Inanimate",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ — التَّفْرِيقُ بَيْنَ الْعَاقِلِ وَغَيْرِهِ", "tamreen_title_ur": "عاقل اور غیر عاقل میں تفریق کی مشق", "tamreen_title_en": "Distinguishing Rational & Non-Rational",
                    "grammar_goal_ur": "عاقل (مَنْ) اور غیر عاقل (مَا) کے سوال و جواب کی فہم۔", "grammar_goal_en": "Understanding rational (مَنْ) vs non-rational (مَا).",
                    "type": "sentence_reading", "strict_tashkeel": True,
                    "prompt_ar": f"{it[0]} اقْرَأْ وَتَرْجِمْ: {it[1]}", "prompt_ur": f"صحیح مفہوم منتخب کریں: ({it[1]})", "prompt_en": f"Select translation: ({it[1]})",
                    "answer": f"{it[2]} • {it[3]}", "options": make_sentence_reading_opts(it[1], it[2], it[3]), "emoji": it[0], "hint_ur": it[2], "hint_en": it[3],
                    "explanation_ur": f"جملہ '{it[1]}' کا مفہوم: {it[2]}۔", "explanation_en": f"Sentence '{it[1]}' means: {it[3]}."
                })
                
        elif u_idx == 4:
            # Lesson 4 explicit 11 items and 85 questions
            # Tamreen 1 Part A: 11 questions
            curriculum_flow.append({
                "id": "b1_u4_t1", "type": "tamreen", "item_order": 2, "tamreen_num": 1,
                "title_ar": "تَمْرِين (١): أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ (فَهْمُ النَّصِّ أ)",
                "title_ur": "مشق (1): پہلے حصے کے سوالات کے جوابات دیں", "title_en": "Exercise (1): Comprehension Questions (Part A)",
                "page": 22, "question_count": 11
            })
            l4_t1_items = [
                ("أَيْنَ الْكِتَابُ؟", "هُوَ عَلَى الْمَكْتَبِ.", ["هُوَ عَلَى الْمَكْتَبِ.", "هُوَ فِي الْغُرْفَةِ.", "هِيَ عَلَى السَّرِيرِ.", "هُوَ فِي الْمَطْبَخِ."], "📖 🗄️", "کتاب کہاں ہے؟", "Where is the book?"),
                ("أَيْنَ مُحَمَّدٌ؟", "هُوَ فِي الْغُرْفَةِ.", ["هُوَ فِي الْغُرْفَةِ.", "هُوَ فِي الْحَمَّامِ.", "هُوَ عَلَى الْمَكْتَبِ.", "هِيَ فِي الْمَطْبَخِ."], "👦 🛋️", "محمد کہاں ہے؟", "Where is Muhammad?"),
                ("أَيْنَ السَّاعَةُ؟", "هِيَ عَلَى السَّرِيرِ.", ["هِيَ عَلَى السَّرِيرِ.", "هُوَ عَلَى الْمَكْتَبِ.", "هِيَ فِي الْغُرْفَةِ.", "هُوَ فِي الْحَمَّامِ."], "⌚ 🛏️", "گھڑی کہاں ہے؟", "Where is the watch?"),
                ("أَيْنَ يَاسِرٌ؟", "هُوَ فِي الْحَمَّامِ.", ["هُوَ فِي الْحَمَّامِ.", "هُوَ فِي الْغُرْفَةِ.", "هِيَ فِي الْمَطْبَخِ.", "هُوَ عَلَى الْمَكْتَبِ."], "🔹 🚿", "یاسر کہاں ہے؟", "Where is Yasir?"),
                ("أَيْنَ آمِنَةُ؟", "هِيَ فِي الْمَطْبَخِ.", ["هِيَ فِي الْمَطْبَخِ.", "هِيَ فِي الْغُرْفَةِ.", "هُوَ فِي الْحَمَّامِ.", "هُوَ عَلَى السَّرِيرِ."], "🔹 🍳", "آمنہ کہاں ہے؟", "Where is Aminah?"),
                ("أَآمِنَةُ فِي الْغُرْفَةِ؟", "لَا، هِيَ فِي الْمَطْبَخِ.", ["لَا، هِيَ فِي الْمَطْبَخِ.", "نَعَمْ، هِيَ فِي الْغُرْفَةِ.", "هِيَ عَلَى السَّرِيرِ.", "لَا، هُوَ فِي الْحَمَّامِ."], "🛋️ 🍳", "کیا آمنہ کمرے میں ہے؟", "Is Aminah in the room?"),
                ("أَيَاسِرٌ فِي الْمَطْبَخِ؟", "لَا، هُوَ فِي الْحَمَّامِ.", ["لَا، هُوَ فِي الْحَمَّامِ.", "نَعَمْ، هُوَ فِي الْمَطْبَخِ.", "هُوَ فِي الْغُرْفَةِ.", "لَا، هِيَ فِي الْمَطْبَخِ."], "🔹 🚿", "کیا یاسر باورچی خانے میں ہے؟", "Is Yasir in the kitchen?"),
                ("مَنْ فِي الْغُرْفَةِ؟", "مُحَمَّدٌ فِي الْغُرْفَةِ.", ["مُحَمَّدٌ فِي الْغُرْفَةِ.", "يَاسِرٌ فِي الْغُرْفَةِ.", "آمِنَةُ فِي الْغُرْفَةِ.", "الْمُدَرِّسُ فِي الْغُرْفَةِ."], "🛋️ 👦", "کمرے میں کون ہے؟", "Who is in the room?"),
                ("وَمَنْ فِي الْحَمَّامِ؟", "يَاسِرٌ فِي الْحَمَّامِ.", ["يَاسِرٌ فِي الْحَمَّامِ.", "مُحَمَّدٌ فِي الْحَمَّامِ.", "آمِنَةُ فِي الْحَمَّامِ.", "الْمُدِيرُ فِي الْحَمَّامِ."], "🔹 🚿", "اور غسل خانے میں کون ہے؟", "And who is in the bathroom?"),
                ("مَاذَا عَلَى الْمَكْتَبِ؟", "الْكِتَابُ عَلَى الْمَكْتَبِ.", ["الْكِتَابُ عَلَى الْمَكْتَبِ.", "السَّاعَةُ عَلَى الْمَكْتَبِ.", "الْقَلَمُ فِي الْحَقِيبَةِ.", "الْوَرَقُ فِي الدُّرْجِ."], "🗄️ 📖", "میز پر کیا ہے؟", "What is on the desk?"),
                ("مَاذَا عَلَى السَّرِيرِ؟", "السَّاعَةُ عَلَى السَّرِيرِ.", ["السَّاعَةُ عَلَى السَّرِيرِ.", "الْكِتَابُ عَلَى السَّرِيرِ.", "الْقَمِيصُ عَلَى السَّرِيرِ.", "الْمِنْدِيلُ عَلَى السَّرِيرِ."], "🛏️ ⌚", "پلنگ پر کیا ہے؟", "What is on the bed?")
            ]
            for q_idx, it in enumerate(l4_t1_items, 1):
                unit_questions.append({
                    "id": f"b1_u4_t1_q{q_idx}", "book": 1, "unit_num": 4, "tamreen_num": 1,
                    "badge_ar": "التَّمْرِينُ (١)", "badge_ur": "مشق (١): فہمِ سبق", "badge_en": "Exercise (1): Comprehension",
                    "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ (فَهْمُ النَّصِّ أ)", "tamreen_title_ur": "پہلے حصے کے سوالات کے جوابات دیں", "tamreen_title_en": "Comprehension Questions (Part A)",
                    "grammar_goal_ur": "حروفِ جارّہ اور ضمائر کے ساتھ سبق کے فہم کے جوابات دینا۔", "grammar_goal_en": "Lesson comprehension using prepositions.",
                    "type": "dialogue_qa", "strict_tashkeel": True,
                    "prompt_ar": f"{it[3]} {it[0]}", "prompt_ur": it[4], "prompt_en": it[5],
                    "answer": it[1], "options": it[2], "emoji": it[3].split()[0], "hint_ur": "سبق کے متن کے مطابق جواب دیں۔", "hint_en": "Answer based on text.",
                    "explanation_ur": f"سبق کے متن کے مطابق: {it[1]}۔", "explanation_en": f"According to text: {it[1]}."
                })
            
            # Tamreen 2: 13 words
            curriculum_flow.append({
                "id": "b1_u4_t2", "type": "tamreen", "item_order": 3, "tamreen_num": 2,
                "title_ar": "تَمْرِين (٢): اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ",
                "title_ur": "مشق (2): حرفِ جر کے اثر کے ساتھ آخری اعراب کا ضبط", "title_en": "Exercise (2): Read & write with correct case endings",
                "page": 22, "question_count": 13
            })
            l4_t2_words = [
                ("الْمَدْرَسَةُ", "اسم مرفوع بالضمة"), ("فِي الْمَدْرَسَةِ", "اسم مجرور بالكسرة لوجود حرف الجر 'فِي'"),
                ("فِي الْبَيْتِ", "اسم مجرور بالكسرة لوجود 'فِي'"), ("الْبَيْتُ", "اسم مرفوع بالضمة"),
                ("الْغُرْفَةُ", "اسم مرفوع بالضمة"), ("الْحَمَّامُ", "اسم مرفوع بالضمة"),
                ("فِي الْمَطْبَخِ", "اسم مجرور بالكسرة"), ("الْمَكْتَبُ", "اسم مرفوع بالضمة"),
                ("عَلَى الْمَكْتَبِ", "اسم مجرور بالكسرة لوجود 'عَلَى'"), ("عَلَى الْكُرْسِيِّ", "اسم مجرور بالكسرة"),
                ("السَّرِيرُ", "اسم مرفوع بالضمة"), ("عَلَى الْكِتَابِ", "اسم مجرور بالكسرة"),
                ("فِي الْمَسْجِدِ", "اسم مجرور بالكسرة")
            ]
            for q_idx, w in enumerate(l4_t2_words, 1):
                unit_questions.append({
                    "id": f"b1_u4_t2_q{q_idx}", "book": 1, "unit_num": 4, "tamreen_num": 2,
                    "badge_ar": "التَّمْرِينُ (٢)", "badge_ur": "مشق (٢): ضبط اعراب", "badge_en": "Exercise (2): Case Endings",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ", "tamreen_title_ur": "حرفِ جر کے اثر کے ساتھ آخری اعراب کا ضبط", "tamreen_title_en": "Case endings with prepositions",
                    "grammar_goal_ur": "حرفِ جر کے بعد اسم کو مجرور کرنا۔", "grammar_goal_en": "Applying genitive kasrah after prepositions.",
                    "type": "vocalization", "strict_tashkeel": True,
                    "prompt_ar": f"مَا هُوَ الضَّبْطُ الصَّحِيحُ: ({w[0]})؟", "prompt_ur": f"صحیح اعراب والا کلمہ منتخب کریں: ({w[0]})", "prompt_en": f"Select correct vocalization: ({w[0]})",
                    "answer": w[0], "options": make_vocalization_opts(w[0]), "emoji": "✍️", "hint_ur": w[1], "hint_en": "Check preposition.",
                    "explanation_ur": f"اعراب کی وجہ: {w[1]}۔", "explanation_en": f"Rule: {w[1]}."
                })
                
            # Tamreen 3: 10 sentences
            curriculum_flow.append({
                "id": "b1_u4_t3", "type": "tamreen", "item_order": 4, "tamreen_num": 3,
                "title_ar": "تَمْرِين (٣): اقْرَأْ وَاكْتُبْ — جُمَلُ الْجَرِّ وَالْمَجْرُورِ",
                "title_ur": "مشق (3): پڑھیں اور لکھیں (جار و مجرور کے جملے)", "title_en": "Exercise (3): Prepositional sentences",
                "page": 22, "question_count": 10
            })
            l4_t3_sentences = [
                ("الطَّالِبُ فِي الْجَامِعَةِ.", "طالب علم یونیورسٹی میں ہے", "The student is in the university", "🎓"),
                ("الرَّجُلُ فِي الْمَسْجِدِ.", "آدمی مسجد میں ہے", "The man is in the mosque", "🕌"),
                ("أَيْنَ التَّاجِرُ؟ هُوَ فِي الدُّكَّانِ.", "تاجر کہاں ہے؟ وہ دکان میں ہے", "Where is the merchant? He is in the shop", "🧑‍💼"),
                ("الْقَلَمُ عَلَى الْمَكْتَبِ.", "قلم میز پر ہے", "The pen is on the desk", "🖊️"),
                ("أَيْنَ زَيْنَبُ؟ هِيَ فِي الْغُرْفَةِ.", "زینب کہاں ہے؟ وہ کمرے میں ہے", "Where is Zainab? She is in the room", "🛋️"),
                ("أَيْنَ الْوَرَقُ؟ هُوَ عَلَى الْمَكْتَبِ.", "کاغذ کہاں ہے؟ وہ میز پر ہے", "Where is the paper? It is on the desk", "📄"),
                ("أَيْنَ الْمُدَرِّسُ؟ هُوَ فِي الْفَصْلِ.", "استاد کہاں ہیں؟ وہ کلاس روم میں ہیں", "Where is the teacher? He is in the classroom", "👨‍🏫"),
                ("أَيْنَ يَاسِرٌ؟ هُوَ فِي الْمِرْحَاضِ.", "یاسر کہاں ہے؟ وہ واش روم میں ہے", "Where is Yasir? He is in the toilet", "🔹"),
                ("الشَّمْسُ وَالْقَمَرُ فِي السَّمَاءِ.", "سورج اور چاند آسمان میں ہیں", "The sun and the moon are in the sky", "☀️ 🌙"),
                ("مَنْ فِي الْفَصْلِ؟", "کلاس روم میں کون ہے؟", "Who is in the classroom?", "🏫")
            ]
            for q_idx, sent in enumerate(l4_t3_sentences, 1):
                unit_questions.append({
                    "id": f"b1_u4_t3_q{q_idx}", "book": 1, "unit_num": 4, "tamreen_num": 3,
                    "badge_ar": "التَّمْرِينُ (٣)", "badge_ur": "مشق (٣): جملوں کا فہم", "badge_en": "Exercise (3): Sentence Comprehension",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ — جُمَلُ الْجَرِّ وَالْمَجْرُورِ", "tamreen_title_ur": "پڑھیں اور لکھیں (جار و مجرور کے جملے)", "tamreen_title_en": "Prepositional sentences",
                    "grammar_goal_ur": "حروفِ جارّہ کے جملوں کا ترجمہ اور فہم۔", "grammar_goal_en": "Prepositional phrases.",
                    "type": "sentence_reading", "strict_tashkeel": True,
                    "prompt_ar": f"{sent[3]} اقْرَأْ وَتَرْجِمْ: {sent[0]}", "prompt_ur": f"صحیح ترجمہ منتخب کریں: ({sent[0]})", "prompt_en": f"Select translation: ({sent[0]})",
                    "answer": f"{sent[1]} • {sent[2]}", "options": make_sentence_reading_opts(sent[0], sent[1], sent[2]), "emoji": sent[3].split()[0], "hint_ur": sent[1], "hint_en": sent[2],
                    "explanation_ur": f"جملہ '{sent[0]}' کا ترجمہ: '{sent[1]}'۔", "explanation_en": f"Translation: '{sent[2]}'."
                })
                
            # Snippet: Muhammad vs Aminah (16 names)
            curriculum_flow.append({
                "id": "b1_u4_snip1", "type": "qaida", "item_order": 5,
                "title_ar": "قَاعِدَةٌ: مُحَمَّدٌ vs آمِنَةُ — الْمَمْنُوعُ مِنَ الصَّرْفِ (أَعْلَامُ الإِنَاثِ)",
                "title_ur": "قاعدہ: مذکر کے نام بمقابلہ مؤنث کے نام (تنوین بمقابلہ ضمہ واحدہ)",
                "title_en": "Rule Snippet: Male Names (Tanween) vs Female Diptotes (No Tanween)",
                "page": 23,
                "rule_summary_ur": "مردوں کے عربی نام عام طور پر منصرف ہوتے ہیں (مُحَمَّدٌ)، جبکہ عورتوں کے نام غیر منصرف (ممنوع من الصرف) ہوتے ہیں اور ان پر تنوین نہیں آتی (آمِنَةُ)۔",
                "rule_summary_en": "Masculine proper names take tanween (مُحَمَّدٌ); feminine proper names are diptotes ending in single dammah (آمِنَةُ).",
                "examples": [
                    {"ar": "مُحَمَّدٌ vs آمِنَةُ", "ur": "محمد (تنوین کے ساتھ) بمقابلہ آمنہ (بغیر تنوین)", "en": "Muhammad vs Aminah"},
                    {"ar": "خَالِدٌ vs زَيْنَبُ", "ur": "خالد (تنوین کے ساتھ) بمقابلہ زینب (بغیر تنوین)", "en": "Khalid vs Zainab"}
                ]
            })
            
            # Tamreen 4: 14 names
            curriculum_flow.append({
                "id": "b1_u4_t4", "type": "tamreen", "item_order": 6, "tamreen_num": 4,
                "title_ar": "تَمْرِين (٤): اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ (أَعْلَامُ الْمُذَكَّرِ وَالْمُؤَنَّثِ)",
                "title_ur": "مشق (4): مذکر اور مؤنث ناموں کے آخری اعراب کا ضبط", "title_en": "Exercise (4): Proper names vocalization",
                "page": 23, "question_count": 14
            })
            l4_t4_names = [
                ("حَامِدٌ", True, "مذکر نام ہے، تنوین آئے گی"), ("زَيْنَبُ", False, "مؤنث نام ہے، ممنوع من الصرف ہے"),
                ("آمِنَةُ", False, "مؤنث نام ہے"), ("عَمَّارٌ", True, "مذکر نام ہے"),
                ("سَعِيدٌ", True, "مذکر نام ہے"), ("فَاطِمَةُ", False, "مؤنث نام ہے"),
                ("مَرْيَمُ", False, "مؤنث نام ہے"), ("عَلِيٌّ", True, "مذکر نام ہے"),
                ("خَالِدٌ", True, "مذکر نام ہے"), ("عَبَّاسٌ", True, "مذکر نام ہے"),
                ("عَائِشَةُ", False, "مؤنث نام ہے"), ("مُحَمَّدٌ", True, "مذکر نام ہے"),
                ("صَفِيَّةُ", False, "مؤنث نام ہے"), ("خَدِيجَةُ", False, "مؤنث نام ہے")
            ]
            for q_idx, nm in enumerate(l4_t4_names, 1):
                clean_base = re.sub(r'[\u064b-\u0652]$', '', nm[0])
                opts = [nm[0], clean_base + ('ُ' if nm[1] else 'ٌ'), clean_base + 'ِ', clean_base + 'َ']
                random.shuffle(opts)
                unit_questions.append({
                    "id": f"b1_u4_t4_q{q_idx}", "book": 1, "unit_num": 4, "tamreen_num": 4,
                    "badge_ar": "التَّمْرِينُ (٤)", "badge_ur": "مشق (٤): ضبط اعلام", "badge_en": "Exercise (4): Proper Names",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ (أَعْلَامُ الْمُذَكَّرِ وَالْمُؤَنَّثِ)",
                    "tamreen_title_ur": "مذکر اور مؤنث ناموں کے آخری اعراب کا ضبط", "tamreen_title_en": "Proper names vocalization",
                    "grammar_goal_ur": "مذکر پر تنوین اور مؤنث پر ضمہ واحدہ کا اطلاق۔", "grammar_goal_en": "Applying tanween vs single dammah.",
                    "type": "vocalization", "strict_tashkeel": True,
                    "prompt_ar": f"مَا هُوَ الضَّبْطُ الصَّحِيحُ: ({clean_base})؟",
                    "prompt_ur": f"صحیح اعراب منتخب کریں: ({clean_base})", "prompt_en": f"Select vocalization: ({clean_base})",
                    "answer": nm[0], "options": opts, "emoji": "🧑" if nm[1] else "🧕",
                    "hint_ur": nm[2], "hint_en": "Check male/female rule.",
                    "explanation_ur": f"قاعدہ: {nm[2]}۔ درست تلفظ '{nm[0]}' ہے۔", "explanation_en": f"Rule: {nm[2]}."
                })
                
            # Nasuddars Part B
            curriculum_flow.append({
                "id": "b1_u4_nas_b", "type": "nasuddars", "item_order": 7,
                "title_ar": "نَصُّ الدَّرْسِ (الْقِسْمُ ب — حِوَارُ مِنْ وَإِلَى)",
                "title_ur": "سبق کا متن (حصہ دوم — حوار مِنْ اور إِلَى)", "title_en": "Lesson Text (Part B — Dialogue)",
                "page": 24, "preview": "المدرس: من أين أنت؟ محمد: أنا من اليابان..."
            })
            
            # Tamreen 1 Part B: 6 questions
            curriculum_flow.append({
                "id": "b1_u4_t5", "type": "tamreen", "item_order": 8, "tamreen_num": 5,
                "title_ar": "تَمْرِين (١ — ب): أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ (حِوَارُ مِنْ وَإِلَى)",
                "title_ur": "مشق (1 — ب): حوار مِنْ اور إِلَى کے مطابق سوالات کے جوابات دیں", "title_en": "Exercise (1 — Part B): Dialogue Comprehension",
                "page": 25, "question_count": 6
            })
            l4_t5_items = [
                ("مِنْ أَيْنَ أَنْتَ؟", "أَنَا مِنَ الْيَابَانِ.", ["أَنَا مِنَ الْيَابَانِ.", "أَنَا مِنَ الصِّينِ.", "أَنَا مِنَ الْهِنْدِ.", "أَنَا مِنَ الْفِلِبِّينِ."], "🇯🇵", "تم کہاں سے ہو؟", "Where are you from?"),
                ("أَأَنْتَ مِنَ الْفِلِبِّينِ؟", "لَا، أَنَا مِنَ الْيَابَانِ.", ["لَا، أَنَا مِنَ الْيَابَانِ.", "نَعَمْ، أَنَا مِنَ الْفِلِبِّينِ.", "أَنَا مِنَ الصِّينِ.", "هُوَ مِنَ الْهِنْدِ."], "🇵🇭", "کیا تم فلپائن سے ہو؟", "Are you from the Philippines?"),
                ("مَنْ مِنَ الصِّينِ؟", "عَمَّارٌ مِنَ الصِّينِ.", ["عَمَّارٌ مِنَ الصِّينِ.", "مُحَمَّدٌ مِنَ الصِّينِ.", "حَامِدٌ مِنَ الصِّينِ.", "عَبَّاسٌ مِنَ الصِّينِ."], "🇨🇳", "چین سے کون ہے؟", "Who is from China?"),
                ("مِنْ أَيْنَ حَامِدٌ؟", "هُوَ مِنَ الْهِنْدِ.", ["هُوَ مِنَ الْهِنْدِ.", "هُوَ مِنَ الْيَابَانِ.", "هُوَ مِنَ الصِّينِ.", "أَنَا مِنَ الْفِلِبِّينِ."], "🇮🇳", "حامد کہاں سے ہے؟", "Where is Hamid from?"),
                ("أَيْنَ ذَهَبَ عَبَّاسٌ؟", "ذَهَبَ إِلَى الْمُدِيرِ.", ["ذَهَبَ إِلَى الْمُدِيرِ.", "ذَهَبَ إِلَى الْمِرْحَاضِ.", "ذَهَبَ إِلَى الْفَصْلِ.", "ذَهَبَ إِلَى السُّوقِ."], "👨‍💼", "عباس کہاں گیا؟", "Where did Abbas go?"),
                ("أَذَهَبَ عَلِيٌّ إِلَى الْمُدِيرِ؟", "لَا، ذَهَبَ إِلَى الْمِرْحَاضِ.", ["لَا، ذَهَبَ إِلَى الْمِرْحَاضِ.", "نَعَمْ، ذَهَبَ إِلَى الْمُدِيرِ.", "ذَهَبَ إِلَى الْفَصْلِ.", "خَرَجَ مِنَ الْمَدْرَسَةِ."], "🔹", "کیا علی مدیر کے پاس گیا؟", "Did Ali go to the principal?")
            ]
            for q_idx, it in enumerate(l4_t5_items, 1):
                unit_questions.append({
                    "id": f"b1_u4_t5_q{q_idx}", "book": 1, "unit_num": 4, "tamreen_num": 5,
                    "badge_ar": "التَّمْرِينُ (١ — ب)", "badge_ur": "مشق (١ — ب): حوار", "badge_en": "Exercise (1 — Part B): Dialogue",
                    "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ (حِوَارُ مِنْ وَإِلَى)", "tamreen_title_ur": "حوار مِنْ اور إِلَى کے مطابق سوالات کے جوابات دیں", "tamreen_title_en": "Dialogue Comprehension (Part B)",
                    "grammar_goal_ur": "حوار کے سوالات کا صحیح جواب دینا۔", "grammar_goal_en": "Dialogue comprehension.",
                    "type": "dialogue_qa", "strict_tashkeel": True,
                    "prompt_ar": f"{it[3]} {it[0]}", "prompt_ur": it[4], "prompt_en": it[5],
                    "answer": it[1], "options": it[2], "emoji": it[3], "hint_ur": "مکالمے کے مطابق جواب منتخب کریں۔", "hint_en": "Dialogue based.",
                    "explanation_ur": f"مکالمے کے مطابق: {it[1]}۔", "explanation_en": f"According to dialogue: {it[1]}."
                })
                
            # Tamreen 2 Part B: 9 phrases
            curriculum_flow.append({
                "id": "b1_u4_t6", "type": "tamreen", "item_order": 9, "tamreen_num": 6,
                "title_ar": "تَمْرِين (٢ — ب): اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ (مِنْ وَإِلَى)",
                "title_ur": "مشق (2 — ب): مِنْ اور إِلَى کے ساتھ الفاظ کے اعراب کا ضبط", "title_en": "Exercise (2 — Part B): Case endings with مِنْ and إِلَى",
                "page": 25, "question_count": 9
            })
            l4_t6_phrases = [
                ("الْغُرْفَةُ", "مرفوع بالضمة"), ("مِنَ الْغُرْفَةِ", "مجرور بالكسرة بعد 'مِنْ'"),
                ("مِنَ الْحَمَّامِ", "مجرور بالكسرة بعد 'مِنْ'"), ("الْمِرْحَاضُ", "مرفوع بالضمة"),
                ("إِلَى الْمِرْحَاضِ", "مجرور بالكسرة بعد 'إِلَى'"), ("الْيَابَانُ", "مرفوع بالضمة"),
                ("الْفِلِبِّينُ", "مرفوع بالضمة"), ("مِنَ الْهِنْدِ", "مجرور بالكسرة بعد 'مِنْ'"),
                ("إِلَى الصِّينِ", "مجرور بالكسرة بعد 'إِلَى'")
            ]
            for q_idx, ph in enumerate(l4_t6_phrases, 1):
                unit_questions.append({
                    "id": f"b1_u4_t6_q{q_idx}", "book": 1, "unit_num": 4, "tamreen_num": 6,
                    "badge_ar": "التَّمْرِينُ (٢ — ب)", "badge_ur": "مشق (٢ — ب): اعراب", "badge_en": "Exercise (2 — Part B): Case Endings",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ (مِنْ وَإِلَى)", "tamreen_title_ur": "مِنْ اور إِلَى کے ساتھ الفاظ کے اعراب کا ضبط", "tamreen_title_en": "Case endings with مِنْ and إِلَى",
                    "grammar_goal_ur": "حروفِ جارّہ کے بعد اسم کو مجرور کرنا۔", "grammar_goal_en": "Applying genitive kasrah after 'min' and 'ila'.",
                    "type": "vocalization", "strict_tashkeel": True,
                    "prompt_ar": f"مَا هُوَ الضَّبْطُ الصَّحِيحُ: ({ph[0]})؟", "prompt_ur": f"صحیح اعراب منتخب کریں: ({ph[0]})", "prompt_en": f"Select correct vocalization: ({ph[0]})",
                    "answer": ph[0], "options": make_vocalization_opts(ph[0]), "emoji": "✍️", "hint_ur": ph[1], "hint_en": "Grammar rule.",
                    "explanation_ur": f"ضابطہ: {ph[1]}۔", "explanation_en": f"Rule: {ph[1]}."
                })
                
            # Tamreen 3 Part B: 7 sentences
            curriculum_flow.append({
                "id": "b1_u4_t7", "type": "tamreen", "item_order": 10, "tamreen_num": 7,
                "title_ar": "تَمْرِين (٣ — ب): اقْرَأْ وَاكْتُبْ — جُمَلُ الأَفْعَالِ مَعَ حُرُوفِ الْجَرِّ",
                "title_ur": "مشق (3 — ب): افعال اور حروفِ جارّہ کے جملے پڑھیں اور لکھیں", "title_en": "Exercise (3 — Part B): Verbs with Prepositions",
                "page": 25, "question_count": 7
            })
            l4_t7_sentences = [
                ("مِنْ أَيْنَ فَاطِمَةُ؟ هِيَ مِنَ الْهِنْدِ.", "فاطمہ کہاں سے ہے؟ وہ ہندوستان سے ہے", "Where is Fatimah from? She is from India", "🇮🇳"),
                ("خَرَجَ الْمُدَرِّسُ مِنَ الْفَصْلِ وَذَهَبَ إِلَى الْمُدِيرِ.", "استاد کلاس روم سے نکلے اور مدیر کے پاس گئے", "The teacher left the classroom and went to the principal", "👨‍🏫 🏫"),
                ("ذَهَبَ التَّاجِرُ إِلَى الدُّكَّانِ.", "تاجر دکان کی طرف گیا", "The merchant went to the shop", "🧑‍💼"),
                ("خَرَجَ حَامِدٌ مِنَ الْغُرْفَةِ وَذَهَبَ إِلَى الْحَمَّامِ.", "حامد کمرے سے نکلا اور غسل خانے گیا", "Hamid left the room and went to the bathroom", "🛋️ 🚿"),
                ("مَنْ خَرَجَ مِنَ الْفَصْلِ؟", "کلاس روم سے کون نکلا؟", "Who left the classroom?", "🏫"),
                ("خَرَجَ الطَّالِبُ مِنَ الْمَدْرَسَةِ وَذَهَبَ إِلَى السُّوقِ.", "طالب علم اسکول سے نکلا اور بازار گیا", "The student left the school and went to the market", "🎒 🏪"),
                ("خَدِيجَةُ مِنَ الصِّينِ وَخَالِدٌ مِنَ الْيَابَانِ.", "خدیجہ چین سے ہے اور خالد جاپان سے ہے", "Khadijah is from China and Khalid is from Japan", "🇨🇳 🇯🇵")
            ]
            for q_idx, sent in enumerate(l4_t7_sentences, 1):
                unit_questions.append({
                    "id": f"b1_u4_t7_q{q_idx}", "book": 1, "unit_num": 4, "tamreen_num": 7,
                    "badge_ar": "التَّمْرِينُ (٣ — ب)", "badge_ur": "مشق (٣ — ب): جملوں کا فہم", "badge_en": "Exercise (3 — Part B): Sentences",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ — جُمَلُ الأَفْعَالِ مَعَ حُرُوفِ الْجَرِّ", "tamreen_title_ur": "افعال اور حروفِ جارّہ کے جملے پڑھیں اور لکھیں", "tamreen_title_en": "Verbs with prepositions",
                    "grammar_goal_ur": "فعل اور حروفِ جارّہ کے جملوں کی تفہیم۔", "grammar_goal_en": "Verbs paired with prepositions.",
                    "type": "sentence_reading", "strict_tashkeel": True,
                    "prompt_ar": f"{sent[3]} اقْرَأْ وَتَرْجِمْ: {sent[0]}", "prompt_ur": f"صحیح ترجمہ منتخب کریں: ({sent[0]})", "prompt_en": f"Select translation: ({sent[0]})",
                    "answer": f"{sent[1]} • {sent[2]}", "options": make_sentence_reading_opts(sent[0], sent[1], sent[2]), "emoji": sent[3].split()[0], "hint_ur": sent[1], "hint_en": sent[2],
                    "explanation_ur": f"جملہ '{sent[0]}' کا اردو ترجمہ: '{sent[1]}'۔", "explanation_en": f"Translation: '{sent[2]}'."
                })
                
            # Tamreen 4 Part B: 5 fill-in-blanks
            curriculum_flow.append({
                "id": "b1_u4_t8", "type": "tamreen", "item_order": 11, "tamreen_num": 8,
                "title_ar": "تَمْرِين (٤ — ب): ضَعْ فِي الْفَرَاغِ حَرْفَ جَرٍّ مُنَاسِباً (مِنْ، إِلَى، فِي، عَلَى)",
                "title_ur": "مشق (4 — ب): خالی جگہ میں مناسب حرفِ جر لگائیں", "title_en": "Exercise (4 — Part B): Fill in prepositions",
                "page": 26, "question_count": 5
            })
            l4_t8_blanks = [
                ("الْكِتَابُ ..... الْمَكْتَبِ.", "عَلَى", ["عَلَى", "فِي", "مِنْ", "إِلَى"], "کتاب میز پر ہے۔", "The book is on the desk."),
                ("الطَّالِبُ ..... الْفَصْلِ.", "فِي", ["فِي", "عَلَى", "إِلَى", "مِنْ"], "طالب علم کلاس روم میں ہے۔", "The student is in the classroom."),
                ("ذَهَبَ حَامِدٌ ..... الْجَامِعَةِ.", "إِلَى", ["إِلَى", "مِنْ", "فِي", "عَلَى"], "حامد یونیورسٹی کی طرف گیا۔", "Hamid went to the university."),
                ("خَرَجَ الْمُدِيرُ ..... الْمَدْرَسَةِ.", "مِنَ", ["مِنَ", "إِلَى", "فِي", "عَلَى"], "مدیر اسکول سے نکلے۔", "The principal left the school."),
                ("ذَهَبَ مُحَمَّدٌ ..... الصِّينِ ..... الْيَابَانِ.", "مِنَ الصِّينِ إِلَى", ["مِنَ الصِّينِ إِلَى", "إِلَى الصِّينِ فِي", "فِي الصِّينِ عَلَى", "عَلَى الصِّينِ مِنْ"], "محمد چین سے جاپان گیا۔", "Muhammad went from China to Japan.")
            ]
            for q_idx, bl in enumerate(l4_t8_blanks, 1):
                unit_questions.append({
                    "id": f"b1_u4_t8_q{q_idx}", "book": 1, "unit_num": 4, "tamreen_num": 8,
                    "badge_ar": "التَّمْرِينُ (٤ — ب)", "badge_ur": "مشق (٤ — ب): املأ الفراغ", "badge_en": "Exercise (4 — Part B): Fill in the Blank",
                    "tamreen_title_ar": "ضَعْ فِي الْفَرَاغِ حَرْفَ جَرٍّ مُنَاسِباً", "tamreen_title_ur": "خالی جگہ میں مناسب حرفِ جر لگائیں", "tamreen_title_en": "Fill blanks with prepositions",
                    "grammar_goal_ur": "درست حرفِ جارّہ کا انتخاب کرنا۔", "grammar_goal_en": "Selecting correct preposition.",
                    "type": "fill_blank", "strict_tashkeel": True,
                    "prompt_ar": f"ضَعْ حَرْفَ جَرٍّ مُنَاسِباً: {bl[0]}", "prompt_ur": f"خالی جگہ میں مناسب حرفِ جر لگائیں: ({bl[3]})", "prompt_en": f"Choose preposition: ({bl[4]})",
                    "answer": bl[1], "options": bl[2], "emoji": "✍️", "hint_ur": bl[3], "hint_en": bl[4],
                    "explanation_ur": f"صحیح جواب '{bl[1]}' ہے۔", "explanation_en": f"Correct answer is '{bl[1]}'."
                })
                
        elif u_idx == 5:
            # Lesson 5 explicit 12 items and 87 questions
            curriculum_flow = [
                {
                    "id": "b1_u5_nas", "type": "nasuddars", "item_order": 1,
                    "title_ar": "نَصُّ الدَّرْسِ (حِوَارُ الإِضَافَةِ: كِتَابُ مَنْ هٰذَا؟)",
                    "title_ur": "سبق کا متن و مکالمہ (حوار الإضافة)", "title_en": "Lesson Reading & Core Text",
                    "page": 27, "preview": "سَعِيدٌ: أَكِتَابُ مُحَمَّدٍ هٰذَا يَا يَاسِرُ؟ يَاسِرٌ: لَا، هٰذَا كِتَابُ حَامِدٍ..."
                },
                {
                    "id": "b1_u5_t1", "type": "tamreen", "item_order": 2, "tamreen_num": 1,
                    "title_ar": "تَمْرِين (١): أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ (فَهْمُ حِوَارِ الإِضَافَةِ)",
                    "title_ur": "مشق (1): مکالمہ اضافہ کے سوالات کے جوابات دیں", "title_en": "Exercise (1): Dialogue Comprehension",
                    "page": 27, "question_count": 3
                },
                {
                    "id": "b1_u5_t2", "type": "tamreen", "item_order": 3, "tamreen_num": 2,
                    "title_ar": "تَمْرِين (٢): أَضِفِ الْكَلِمَةَ الأُولَى إِلَى الثَّانِيَةِ (صِيَاغَةُ الْمُضَافِ وَالْمُضَافِ إِلَيْهِ)",
                    "title_ur": "مشق (2): پہلے کلمے کو دوسرے کی طرف مضاف کریں (14 سوالات)", "title_en": "Exercise (2): Annex First Word to Second (14 Questions)",
                    "page": 28, "question_count": 14
                },
                {
                    "id": "b1_u5_t3", "type": "tamreen", "item_order": 4, "tamreen_num": 3,
                    "title_ar": "تَمْرِين (٣): اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ (ضَبْطُ الإِضَافَةِ)",
                    "title_ur": "مشق (3): مضاف اور مضاف الیہ کے اعراب کا ضبط (10 تراکیب)", "title_en": "Exercise (3): Case Endings in Idafah (10 Phrases)",
                    "page": 29, "question_count": 10
                },
                {
                    "id": "b1_u5_t4", "type": "tamreen", "item_order": 5, "tamreen_num": 4,
                    "title_ar": "تَمْرِين (٤): اقْرَأْ — قِرَاءَةُ جُمَلِ الإِضَافَةِ وَاسْتِيعَابُهَا",
                    "title_ur": "مشق (4): جملہ ہائے اضافہ کی قراءت اور فہم (20 جملے)", "title_en": "Exercise (4): Read Idafah Sentences (20 Sentences)",
                    "page": 29, "question_count": 20
                },
                {
                    "id": "b1_u5_t5", "type": "tamreen", "item_order": 6, "tamreen_num": 5,
                    "title_ar": "تَمْرِين (٥): كَوِّنْ جُمَلاً مُفِيدَةً بِمَلْءِ الْفَرَاغِ بِمُضَافٍ مُنَاسِبٍ",
                    "title_ur": "مشق (5): خالی جگہ میں مناسب مضاف لگائیں (10 سوالات)", "title_en": "Exercise (5): Fill in Blanks with Mudaf (10 Questions)",
                    "page": 30, "question_count": 10
                },
                {
                    "id": "b1_u5_t6", "type": "tamreen", "item_order": 7, "tamreen_num": 6,
                    "title_ar": "تَمْرِين (٦): صَحِّحِ التَّرْكِيبَاتِ التَّالِيَةَ (أَخْطَاءُ التَّعْرِيفِ وَالتَّنْوِينِ)",
                    "title_ur": "مشق (6): غلط مرکبات کی تصحیح کریں (6 سوالات)", "title_en": "Exercise (6): Error Correction (6 Questions)",
                    "page": 31, "question_count": 6
                },
                {
                    "id": "b1_u5_snip1", "type": "qaida", "item_order": 8,
                    "title_ar": "قَاعِدَةٌ: يَاءُ النِّدَاءِ (مُحَمَّدٌ : يَا مُحَمَّدُ)",
                    "title_ur": "قاعدہ: حرفِ ندا (يَا) اور منادیٰ کا ضمہ پر مبنی ہونا", "title_en": "Rule Snippet: Vocative Particle (يَا) Drops Tanween",
                    "page": 31,
                    "rule_summary_ur": "حرفِ ندا 'يَا' کے بعد منادیٰ سے تنوین گر جاتی ہے اور وہ ضمہ پر مبنی ہوتا ہے، جیسے: مُحَمَّدٌ -> يَا مُحَمَّدُ۔",
                    "rule_summary_en": "The vocative particle 'يَا' drops tanween and leaves a single dammah.",
                    "examples": [
                        {"ar": "مُحَمَّدٌ -> يَا مُحَمَّدُ", "ur": "محمد -> اے محمد!", "en": "Muhammad -> O Muhammad!"},
                        {"ar": "شَيْخٌ -> يَا شَيْخُ", "ur": "شیخ -> اے شیخ!", "en": "Shaykh -> O Shaykh!"}
                    ]
                },
                {
                    "id": "b1_u5_t7", "type": "tamreen", "item_order": 9, "tamreen_num": 7,
                    "title_ar": "تَمْرِين (٧): اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ (الْمُنَادَى)",
                    "title_ur": "مشق (7): منادیٰ کے آخری اعراب کا ضبط (9 کلمات)", "title_en": "Exercise (7): Case Endings of Vocative (9 Items)",
                    "page": 31, "question_count": 9
                },
                {
                    "id": "b1_u5_t8", "type": "tamreen", "item_order": 10, "tamreen_num": 8,
                    "title_ar": "تَمْرِين (٨): اقْرَأِ الْمِثَالَ ثُمَّ كَوِّنْ أَسْئِلَةً مِثْلَهُ (كِتَابُ مَنْ هٰذَا؟)",
                    "title_ur": "مشق (8): مثال کی طرح سوالات بنائیں (كِتَابُ مَنْ هٰذَا؟) (4 سوالات)", "title_en": "Exercise (8): Possessive Questions (4 Questions)",
                    "page": 31, "question_count": 4
                },
                {
                    "id": "b1_u5_snip2", "type": "qaida", "item_order": 11,
                    "title_ar": "قَاعِدَةٌ: اسْمٌ وَابْنٌ (قَوَاعِدُ نُطْقِ هَمْزَةِ الْوَصْلِ)",
                    "title_ur": "قاعدہ: 'اسم' اور 'ابن' میں ہمزۃ الوصل کا نطق", "title_en": "Rule Snippet: Hamzatul Wasl in 'Ism' and 'Ibn'",
                    "page": 32,
                    "rule_summary_ur": "کلمہ 'اسْمٌ' اور 'ابْنٌ' کی ہمزہ وصل کی ہے جو درمیان میں گر جاتی ہے۔",
                    "rule_summary_en": "Hamzah in 'Ism' and 'Ibn' is Hamzatul Wasl.",
                    "examples": [
                        {"ar": "اسْمُ الْوَلَدِ مُحَمَّدٌ", "ur": "لڑکے کا نام محمد ہے", "en": "The boy's name is Muhammad"}
                    ]
                },
                {
                    "id": "b1_u5_t9", "type": "tamreen", "item_order": 12, "tamreen_num": 9,
                    "title_ar": "تَمْرِين (٩): اقْرَأْ مَا يَلِي مُرَاعِياً قَوَاعِدَ نُطْقِ هَمْزَةِ الْوَصْلِ",
                    "title_ur": "مشق (9): ہمزۃ الوصل کے قواعد کی رعایت کرتے ہوئے پڑھیں (7 جملے)", "title_en": "Exercise (9): Rules of Hamzatul Wasl (7 Sentences)",
                    "page": 32, "question_count": 7
                }
            ]
            
            # T1: 3
            t1_qs = [
                ("أَيْنَ كِتَابُ مُحَمَّدٍ؟", "هُوَ عَلَى مَكْتَبِ الْمُدَرِّسِ.", ["هُوَ عَلَى مَكْتَبِ الْمُدَرِّسِ.", "هُوَ تَحْتَ الْمَكْتَبِ.", "هُوَ فِي الْحَقِيبَةِ.", "هُوَ فِي الْغُرْفَةِ."], "کتاب کہاں ہے؟", "Where is Muhammad's book?"),
                ("أَيْنَ كِتَابُ عَمَّارٍ؟", "هُوَ تَحْتَ الْمَكْتَبِ.", ["هُوَ تَحْتَ الْمَكْتَبِ.", "هُوَ عَلَى مَكْتَبِ الْمُدَرِّسِ.", "هُوَ فِي الْمَسْجِدِ.", "هُوَ فِي الْبَيْتِ."], "عمار کی کتاب کہاں ہے؟", "Where is Ammar's book?"),
                ("أَيْنَ حَقِيبَةُ الْمُدَرِّسِ؟", "هِيَ تَحْتَ الْمَكْتَبِ.", ["هِيَ تَحْتَ الْمَكْتَبِ.", "هِيَ عَلَى الْكُرْسِيِّ.", "هِيَ فِي السَّيَّارَةِ.", "هِيَ فِي الْفَصْلِ."], "استاد کا بستہ کہاں ہے؟", "Where is the teacher's bag?")
            ]
            for q_idx, it in enumerate(t1_qs, 1):
                unit_questions.append({
                    "id": f"b1_u5_t1_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 1,
                    "badge_ar": "التَّمْرِينُ (١)", "badge_ur": "مشق (١): فہمِ سبق", "badge_en": "Exercise (1): Comprehension",
                    "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ", "tamreen_title_ur": "مکالمہ اضافہ کے سوالات کے جوابات دیں", "tamreen_title_en": "Dialogue Comprehension",
                    "grammar_goal_ur": "مرکب اضافی کے ساتھ سبق کے سوالات کا جواب دینا۔", "grammar_goal_en": "Idafah comprehension.",
                    "type": "dialogue_qa", "strict_tashkeel": True,
                    "prompt_ar": it[0], "prompt_ur": it[3], "prompt_en": it[4],
                    "answer": it[1], "options": it[2], "emoji": "📖", "hint_ur": "متن کے مطابق جواب دیں۔", "hint_en": "Dialogue based.",
                    "explanation_ur": f"مکالمے کے مطابق: {it[1]}۔", "explanation_en": f"According to dialogue: {it[1]}."
                })
            # T2: 14
            t2_pairs = [
                ("قَلَمٌ + حَامِدٌ", "قَلَمُ حَامِدٍ", ["قَلَمُ حَامِدٍ", "قَلَمٌ حَامِدٍ", "قَلَمُ حَامِدٌ", "اَلْقَلَمُ حَامِدٍ"]),
                ("مِفْتَاحٌ + الْبَيْتُ", "مِفْتَاحُ الْبَيْتِ", ["مِفْتَاحُ الْبَيْتِ", "مِفْتَاحٌ الْبَيْتِ", "اَلْمِفْتَاحُ الْبَيْتِ", "مِفْتَاحُ الْبَيْتُ"]),
                ("بَيْتٌ + عَبَّاسٌ", "بَيْتُ عَبَّاسٍ", ["بَيْتُ عَبَّاسٍ", "بَيْتٌ عَبَّاسٍ", "بَيْتُ عَبَّاسٌ", "اَلْبَيْتُ عَبَّاسٍ"]),
                ("دُكَّانٌ + التَّاجِرُ", "دُكَّانُ التَّاجِرِ", ["دُكَّانُ التَّاجِرِ", "دُكَّانٌ التَّاجِرِ", "اَلدُّكَّانُ التَّاجِرِ", "دُكَّانُ التَّاجِرُ"]),
                ("غُرْفَةٌ + عَلِيٌّ", "غُرْفَةُ عَلِيٍّ", ["غُرْفَةُ عَلِيٍّ", "غُرْفَةٌ عَلِيٍّ", "غُرْفَةُ عَلِيٌّ", "اَلْغُرْفَةُ عَلِيٍّ"]),
                ("بَيْتٌ + الْمُهَنْدِسُ", "بَيْتُ الْمُهَنْدِسِ", ["بَيْتُ الْمُهَنْدِسِ", "بَيْتٌ الْمُهَنْدِسِ", "اَلْبَيْتُ الْمُهَنْدِسِ", "بَيْتُ الْمُهَنْدِسُ"]),
                ("دَفْتَرٌ + سَعِيدٌ", "دَفْتَرُ سَعِيدٍ", ["دَفْتَرُ سَعِيدٍ", "دَفْتَرٌ سَعِيدٍ", "دَفْتَرُ سَعِيدٌ", "اَلدَّفْتَرُ سَعِيدٍ"]),
                ("اسْمٌ + الطَّالِبُ", "اسْمُ الطَّالِبِ", ["اسْمُ الطَّالِبِ", "اسْمٌ الطَّالِبِ", "اَلِاسْمُ الطَّالِبِ", "اسْمُ الطَّالِبُ"]),
                ("مِنْدِيلٌ + يَاسِرٌ", "مِنْدِيلُ يَاسِرٍ", ["مِنْدِيلُ يَاسِرٍ", "مِنْدِيلٌ يَاسِرٍ", "مِنْدِيلُ يَاسِرٌ", "اَلْمِنْدِيلُ يَاسِرٍ"]),
                ("كِتَابٌ + اللَّهُ", "كِتَابُ اللَّهِ", ["كِتَابُ اللَّهِ", "كِتَابٌ اللَّهِ", "اَلْكِتَابُ اللَّهِ", "كِتَابُ اللَّهُ"]),
                ("قَمِيصٌ + عَمَّارٌ", "قَمِيصُ عَمَّارٍ", ["قَمِيصُ عَمَّارٍ", "قَمِيصٌ عَمَّارٍ", "قَمِيصُ عَمَّارٌ", "اَلْقَمِيصُ عَمَّارٍ"]),
                ("بِنْتٌ + الطَّبِيبُ", "بِنْتُ الطَّبِيبِ", ["بِنْتُ الطَّبِيبِ", "بِنْتٌ الطَّبِيبِ", "اَلْبِنْتُ الطَّبِيبِ", "بِنْتُ الطَّبِيبُ"]),
                ("سَرِيرٌ + خَالِدٌ", "سَرِيرُ خَالِدٍ", ["سَرِيرُ خَالِدٍ", "سَرِيرٌ خَالِدٍ", "سَرِيرُ خَالِدٌ", "اَلسَّرِيرُ خَالِدٍ"]),
                ("مِفْتَاحٌ + السَّيَّارَةُ", "مِفْتَاحُ السَّيَّارَةِ", ["مِفْتَاحُ السَّيَّارَةِ", "مِفْتَاحٌ السَّيَّارَةِ", "اَلْمِفْتَاحُ السَّيَّارَةِ", "مِفْتَاحُ السَّيَّارَةُ"])
            ]
            for q_idx, it in enumerate(t2_pairs, 1):
                unit_questions.append({
                    "id": f"b1_u5_t2_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 2,
                    "badge_ar": "التَّمْرِينُ (٢)", "badge_ur": "مشق (٢): صیاغت مضاف", "badge_en": "Exercise (2): Idafah Formation",
                    "tamreen_title_ar": "أَضِفِ الْكَلِمَةَ الأُولَى إِلَى الثَّانِيَةِ", "tamreen_title_ur": "پہلے کلمے کو دوسرے کی طرف مضاف کریں", "tamreen_title_en": "Annex First Word to Second",
                    "grammar_goal_ur": "مضاف سے تنوین گرانا اور مضاف الیہ کو مجرور کرنا۔", "grammar_goal_en": "Dropping tanween from mudaf and applying kasrah.",
                    "type": "transformation", "strict_tashkeel": True,
                    "prompt_ar": f"أَضِفِ الْكَلِمَةَ الأُولَى إِلَى الثَّانِيَةِ: ({it[0]})",
                    "prompt_ur": f"صحیح مرکب اضافی منتخب کریں: ({it[0]})", "prompt_en": f"Choose correct Idafah construction: ({it[0]})",
                    "answer": it[1], "options": it[2], "emoji": "🔗",
                    "hint_ur": "مضاف پر تنوین نہیں آتی، مضاف الیہ مجرور ہوتا ہے۔", "hint_en": "Mudaf drops tanween; mudaf ilayh is genitive.",
                    "explanation_ur": f"صحیح مرکب اضافی '{it[1]}' ہے۔", "explanation_en": f"Correct Idafah is '{it[1]}'."
                })
            # T3: 10
            t3_phrases = [
                ("بَابُ الْمَدْرَسَةِ", "مضاف مرفوع اور مضاف الیہ مجرور بالكسرة"), ("حِمَارُ الرَّجُلِ", "مضاف مرفوع اور مضاف الیہ مجرور"),
                ("بَيْتُ حَامِدٍ", "مضاف مرفوع اور مضاف الیہ مجرور"), ("سَيَّارَةُ الْمُدِيرِ", "مضاف مرفوع اور مضاف الیہ مجرور"),
                ("مِنْدِيلُ عَمَّارٍ", "مضاف مرفوع اور مضاف الیہ مجرور"), ("اسْمُ الطَّالِبِ", "مضاف مرفوع اور مضاف الیہ مجرور"),
                ("بَيْتُ اللَّهِ", "مضاف مرفوع اور اسم الجلالة مجرور"), ("فِي كِتَابِ اللَّهِ", "حرف جر کی وجہ سے مجرور"),
                ("مِنْ بَيْتِ الْمُدَرِّسِ", "حرف جر کی وجہ سے مجرور"), ("عَلَى مَكْتَبِ الْمُدِيرِ", "حرف جر کی وجہ سے مجرور")
            ]
            for q_idx, it in enumerate(t3_phrases, 1):
                unit_questions.append({
                    "id": f"b1_u5_t3_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 3,
                    "badge_ar": "التَّمْرِينُ (٣)", "badge_ur": "مشق (٣): ضبط اعراب", "badge_en": "Exercise (3): Case Endings",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ", "tamreen_title_ur": "مضاف اور مضاف الیہ کے اعراب کا ضبط", "tamreen_title_en": "Idafah Case Endings",
                    "grammar_goal_ur": "مرکب اضافی میں اعراب کا صحیح تعین۔", "grammar_goal_en": "Case endings in possessive phrases.",
                    "type": "vocalization", "strict_tashkeel": True,
                    "prompt_ar": f"مَا هُوَ الضَّبْطُ الصَّحِيحُ: ({it[0]})؟", "prompt_ur": f"صحیح اعراب والی ترکیب منتخب کریں: ({it[0]})", "prompt_en": f"Select correctly vocalized phrase: ({it[0]})",
                    "answer": it[0], "options": make_vocalization_opts(it[0]), "emoji": "✍️", "hint_ur": it[1], "hint_en": "Idafah rules.",
                    "explanation_ur": f"ضابطہ: {it[1]}۔", "explanation_en": f"Rule: {it[1]}."
                })
            # T4: 20
            t4_sentences = [
                ("أَيْنَ بَيْتُ الْمُدَرِّسِ؟ هُوَ بَعِيدٌ.", "استاد کا گھر کہاں ہے؟ وہ دور ہے۔", "Where is the teacher's house? It is far."),
                ("الْقُرْآنُ كِتَابُ اللَّهِ.", "قرآن اللہ کی کتاب ہے۔", "The Quran is the book of Allah."),
                ("الْكَعْبَةُ بَيْتُ اللَّهِ.", "کعبہ اللہ کا گھر ہے۔", "The Kaaba is the house of Allah."),
                ("مُحَمَّدٌ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ رَسُولُ اللَّهِ.", "محمد صلی اللہ علیہ وسلم اللہ کے رسول ہیں۔", "Muhammad is the messenger of Allah."),
                ("خَرَجَ الْمُدَرِّسُ مِنْ غُرْفَةِ الْمُدِيرِ.", "استاد مدیر کے کمرے سے نکلے۔", "The teacher came out of the principal's room."),
                ("هٰذَا بَيْتُ حَامِدٍ وَذٰلِكَ بَيْتُ خَالِدٍ.", "یہ حامد کا گھر ہے اور وہ خالد کا گھر ہے۔", "This is Hamid's house and that is Khalid's house."),
                ("ابْنُ عَمَّارٍ طَالِبٌ وَابْنُ يَاسِرٍ تَاجِرٌ.", "عمار کا بیٹا طالب علم ہے اور یاسر کا بیٹا تاجر ہے۔", "Ammar's son is a student and Yasir's son is a merchant."),
                ("بَيْتُ الْمُدَرِّسِ بَعِيدٌ وَبَيْتُ التَّاجِرِ قَرِيبٌ.", "استاد کا گھر دور ہے اور تاجر کا گھر قریب ہے۔", "The teacher's house is far and the merchant's house is near."),
                ("هٰذَا مِفْتَاحُ السَّيَّارَةِ، أَيْنَ مِفْتَاحُ الْبَيْتِ؟", "یہ گاڑی کی چابی ہے، گھر کی چابی کہاں ہے؟", "This is the car key, where is the house key?"),
                ("مَنْ أَنْتَ يَا وَلَدُ؟ أَنَا ابْنُ عَبَّاسٍ.", "اے لڑکے تم کون ہو؟ میں عباس کا بیٹا ہوں۔", "Who are you, boy? I am the son of Abbas."),
                ("وَابْنُ مَنْ هُوَ؟ هُوَ ابْنُ خَالِدٍ.", "اور وہ کس کا بیٹا ہے؟ وہ خالد کا بیٹا ہے۔", "And whose son is he? He is the son of Khalid."),
                ("أَيْنَ مَسْجِدُ رَسُولِ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ؟ هُوَ فِي الْمَدِينَةِ الْمُنَوَّرَةِ.", "رسول اللہ کی مسجد کہاں ہے؟ وہ مدینہ منورہ میں ہے۔", "Where is the Mosque of the Messenger? It is in Madinah."),
                ("بِنْتُ حَامِدٍ فِي الْمَدْرَسَةِ وَبِنْتُ مُحَمَّدٍ فِي الْجَامِعَةِ.", "حامد کی بیٹی اسکول میں ہے اور محمد کی بیٹی یونیورسٹی میں ہے۔", "Hamid's daughter is in school and Muhammad's daughter is in university."),
                ("اسْمُ الْمُدَرِّسِ سَعِيدٌ وَاسْمُ الْمُهَنْدِسِ خَلِيلٌ.", "استاد کا نام سعید ہے اور انجینئر کا نام خلیل ہے۔", "The teacher's name is Said and the engineer's name is Khalil."),
                ("عَمُّ الطَّالِبِ غَنِيٌّ.", "طالب علم کے چچا مالدار ہیں۔", "The student's uncle is rich."),
                ("بَابُ الْمَسْجِدِ مَفْتُوحٌ وَبَابُ الْمَدْرَسَةِ مُغْلَقٌ.", "مسجد کا دروازہ کھلا ہے اور اسکول کا دروازہ بند ہے۔", "The mosque door is open and the school door is closed."),
                ("خَالُ حَامِدٍ فَقِيرٌ.", "حامد کے ماموں غریب ہیں۔", "Hamid's maternal uncle is poor."),
                ("سَيَّارَةُ عَبَّاسٍ فِي الشَّارِعِ.", "عباس کی گاڑی سڑک پر ہے۔", "Abbas's car is on the street."),
                ("ابْنُ مَنْ أَنْتَ؟ أَنَا ابْنُ الْمُدَرِّسِ.", "تم کس کے بیٹے ہو؟ میں استاد کا بیٹا ہوں۔", "Whose son are you? I am the son of the teacher."),
                ("أَيْنَ الْكَلْبُ؟ هُوَ تَحْتَ السَّيَّارَةِ.", "کتا کہاں ہے؟ وہ گاڑی کے نیچے ہے۔", "Where is the dog? It is under the car.")
            ]
            for q_idx, it in enumerate(t4_sentences, 1):
                unit_questions.append({
                    "id": f"b1_u5_t4_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 4,
                    "badge_ar": "التَّمْرِينُ (٤)", "badge_ur": "مشق (٤): جملوں کا فہم", "badge_en": "Exercise (4): Sentence Reading",
                    "tamreen_title_ar": "اقْرَأْ — قِرَاءَةُ جُمَلِ الإِضَافَةِ وَاسْتِيعَابُهَا", "tamreen_title_ur": "جملہ ہائے اضافہ کی قراءت اور فہم", "tamreen_title_en": "Idafah Sentences Reading",
                    "grammar_goal_ur": "مرکب اضافی کے جملوں کا فہم۔", "grammar_goal_en": "Idafah sentences.",
                    "type": "sentence_reading", "strict_tashkeel": True,
                    "prompt_ar": f"اقْرَأْ وَتَرْجِمْ: {it[0]}", "prompt_ur": f"صحیح ترجمہ منتخب کریں: ({it[0]})", "prompt_en": f"Select translation: ({it[0]})",
                    "answer": f"{it[1]} • {it[2]}", "options": make_sentence_reading_opts(it[0], it[1], it[2]), "emoji": "📖", "hint_ur": it[1], "hint_en": it[2],
                    "explanation_ur": f"جملہ '{it[0]}' کا اردو ترجمہ: '{it[1]}'۔", "explanation_en": f"Translation: '{it[2]}'."
                })
            # T5: 10
            t5_blanks = [
                ("..... الْبَيْتِ مُغْلَقٌ.", "بَابُ", ["بَابُ", "قَلَمُ", "كِتَابُ", "سَرِيرُ"], "گھر کا دروازہ بند ہے۔", "The door of the house is closed."),
                ("أَيْنَ ..... السَّيَّارَةِ؟", "مِفْتَاحُ", ["مِفْتَاحُ", "بَابُ", "دَفْتَرُ", "قَمِيصُ"], "گاڑی کی چابی کہاں ہے؟", "Where is the car key?"),
                ("مُحَمَّدٌ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ ..... اللَّهِ.", "رَسُولُ", ["رَسُولُ", "بَيْتُ", "مَسْجِدُ", "قَلَمُ"], "محمد اللہ کے رسول ہیں۔", "Muhammad is the messenger of Allah."),
                ("..... الطَّبِيبِ بَعِيدٌ.", "بَيْتُ", ["بَيْتُ", "قَلَمُ", "مِفْتَاحُ", "مِنْدِيلُ"], "ڈاکٹر کا گھر دور ہے۔", "The doctor's house is far."),
                ("الْقُرْآنُ ..... اللَّهِ.", "كِتَابُ", ["كِتَابُ", "بَابُ", "سَيَّارَةُ", "دُكَّانُ"], "قرآن اللہ کی کتاب ہے۔", "The Quran is the book of Allah."),
                ("خَدِيجَةُ ..... حَامِدٍ.", "بِنْتُ", ["بِنْتُ", "ابْنُ", "عَمُّ", "خَالُ"], "خدیجہ حامد کی بیٹی ہے۔", "Khadijah is Hamid's daughter."),
                ("أَنَا ..... الْمُدَرِّسِ.", "ابْنُ", ["ابْنُ", "بِنْتُ", "سَيَّارَةُ", "بَيْتُ"], "میں استاد کا بیٹا ہوں۔", "I am the son of the teacher."),
                ("..... الطَّالِبِ مَكْسُورٌ.", "قَلَمُ", ["قَلَمُ", "بَيْتُ", "مَسْجِدُ", "سَيَّارَةُ"], "طالب علم کا قلم ٹوٹا ہوا ہے۔", "The student's pen is broken."),
                ("بَابُ ..... مَفْتُوحٌ.", "الْمَسْجِدِ", ["الْمَسْجِدِ", "الْمَسْجِدُ", "مَسْجِدٌ", "الْمَسْجِدَ"], "مسجد کا دروازہ کھلا ہے۔", "The mosque door is open."),
                ("خَرَجَ الْمُدَرِّسُ مِنْ ..... الْمُدِيرِ.", "غُرْفَةِ", ["غُرْفَةِ", "غُرْفَةُ", "غُرْفَةً", "غُرْفَةٌ"], "استاد مدیر کے کمرے سے نکلے۔", "The teacher left the principal's room.")
            ]
            for q_idx, it in enumerate(t5_blanks, 1):
                unit_questions.append({
                    "id": f"b1_u5_t5_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 5,
                    "badge_ar": "التَّمْرِينُ (٥)", "badge_ur": "مشق (٥): املأ الفراغ", "badge_en": "Exercise (5): Fill in Blanks",
                    "tamreen_title_ar": "كَوِّنْ جُمَلاً مُفِيدَةً بِمَلْءِ الْفَرَاغِ بِمُضَافٍ مُنَاسِبٍ", "tamreen_title_ur": "خالی جگہ میں مناسب مضاف لگائیں", "tamreen_title_en": "Fill blanks with mudaf",
                    "grammar_goal_ur": "سیاق کے مطابق مضاف کا انتخاب۔", "grammar_goal_en": "Contextual mudaf.",
                    "type": "fill_blank", "strict_tashkeel": True,
                    "prompt_ar": f"اِمْلَأِ الْفَرَاغَ: {it[0]}", "prompt_ur": f"خالی جگہ میں مناسب کلمہ لگائیں: ({it[3]})", "prompt_en": f"Fill blank: ({it[4]})",
                    "answer": it[1], "options": it[2], "emoji": "✍️", "hint_ur": it[3], "hint_en": it[4],
                    "explanation_ur": f"صحیح کلمہ '{it[1]}' ہے۔", "explanation_en": f"Correct word is '{it[1]}'."
                })
            # T6: 6
            t6_corrections = [
                ("اَلْقَلَمُ الطَّالِبِ", "قَلَمُ الطَّالِبِ", ["قَلَمُ الطَّالِبِ", "اَلْقَلَمُ الطَّالِبُ", "قَلَمٌ الطَّالِبِ", "اَلْقَلَمِ طَالِبٍ"], "مضاف پر الف لام نہیں آتا"),
                ("بَابَ السَّيَّارَةِ", "بَابُ السَّيَّارَةِ", ["بَابُ السَّيَّارَةِ", "بَابِ السَّيَّارَةِ", "اَلْبَابُ السَّيَّارَةِ", "بَابٌ السَّيَّارَةِ"], "مبتدأ مرفوع ہوتا ہے"),
                ("بِنْتُ حَامِدٌ", "بِنْتُ حَامِدٍ", ["بِنْتُ حَامِدٍ", "بِنْتٌ حَامِدٍ", "اَلْبِنْتُ حَامِدٌ", "بِنْتُ حَامِدًا"], "مضاف الیہ ہمیشہ مجرور ہوتا ہے"),
                ("الرَّسُولُ اللَّهِ", "رَسُولُ اللَّهِ", ["رَسُولُ اللَّهِ", "الرَّسُولُ اللَّهُ", "رَسُولٌ اللَّهِ", "رَسُولِ اللَّهِ"], "مضاف پر الف لام داخل نہیں ہوتا"),
                ("اسْمُ الْوَلَدُ", "اسْمُ الْوَلَدِ", ["اسْمُ الْوَلَدِ", "اَلِاسْمُ الْوَلَدِ", "اسْمٌ الْوَلَدُ", "اسْمِ الْوَلَدَ"], "مضاف الیہ مجرور ہوتا ہے"),
                ("ابْنُ لِلْمُدَرِّسِ", "ابْنُ الْمُدَرِّسِ", ["ابْنُ الْمُدَرِّسِ", "اَلِابْنُ لِلْمُدَرِّسِ", "ابْنٌ لِلْمُدَرِّسِ", "ابْنِ الْمُدَرِّسُ"], "اضافت میں لام الجر نہیں آتا")
            ]
            for q_idx, it in enumerate(t6_corrections, 1):
                unit_questions.append({
                    "id": f"b1_u5_t6_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 6,
                    "badge_ar": "التَّمْرِينُ (٦)", "badge_ur": "مشق (٦): تصحیح اغلاط", "badge_en": "Exercise (6): Error Correction",
                    "tamreen_title_ar": "صَحِّحِ التَّرْكِيبَاتِ التَّالِيَةَ", "tamreen_title_ur": "غلط مرکبات کی تصحیح کریں", "tamreen_title_en": "Error Correction",
                    "grammar_goal_ur": "اضافت کی غلطیوں کی درستی۔", "grammar_goal_en": "Idafah error correction.",
                    "type": "correction", "strict_tashkeel": True,
                    "prompt_ar": f"صَحِّحِ التَّرْكِيبَ: ({it[0]})", "prompt_ur": f"درست صورت منتخب کریں: ({it[0]})", "prompt_en": f"Select corrected phrase: ({it[0]})",
                    "answer": it[1], "options": it[2], "emoji": "⚠️", "hint_ur": it[3], "hint_en": "Observe mudaf rules.",
                    "explanation_ur": f"وجہ: {it[3]}۔ درست صورت: '{it[1]}' ہے۔", "explanation_en": f"Rule: {it[3]}."
                })
            # T7: 9
            t7_vocatives = [
                ("يَا عَلِيُّ", "علی -> یا علی", ["يَا عَلِيُّ", "يَا عَلِيٌّ", "يَا عَلِيًّا", "يَا عَلِيٍّ"]),
                ("يَا عَبَّاسُ", "عباس -> یا عباس", ["يَا عَبَّاسُ", "يَا عَبَّاسٌ", "يَا عَبَّاسًا", "يَا عَبَّاسٍ"]),
                ("يَا شَيْخُ", "شیخ -> یا شیخ", ["يَا شَيْخُ", "يَا شَيْخٌ", "يَا شَيْخًا", "يَا شَيْخٍ"]),
                ("يَا رَجُلُ", "رجل -> یا رجل", ["يَا رَجُلُ", "يَا رَجُلٌ", "يَا رَجُلاً", "يَا رَجُلٍ"]),
                ("يَا يَاسِرُ", "یاسر -> یا یاسر", ["يَا يَاسِرُ", "يَا يَاسِرٌ", "يَا يَاسِرًا", "يَا يَاسِرٍ"]),
                ("يَا عَمَّارُ", "عمار -> یا عمار", ["يَا عَمَّارُ", "يَا عَمَّارٌ", "يَا عَمَّارًا", "يَا عَمَّارٍ"]),
                ("يَا دُكْتُورُ", "دكتور -> یا دكتور", ["يَا دُكْتُورُ", "يَا دُكْتُورٌ", "يَا دُكْتُورًا", "يَا دُكْتُورٍ"]),
                ("يَا أُسْتَاذُ", "أستاذ -> یا أستاذ", ["يَا أُسْتَاذُ", "يَا أُسْتَاذٌ", "يَا أُسْتَاذًا", "يَا أُسْتَاذٍ"]),
                ("يَا وَلَدُ", "ولد -> یا ولد", ["يَا وَلَدُ", "يَا وَلَدٌ", "يَا وَلَدًا", "يَا وَلَدٍ"])
            ]
            for q_idx, it in enumerate(t7_vocatives, 1):
                unit_questions.append({
                    "id": f"b1_u5_t7_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 7,
                    "badge_ar": "التَّمْرِينُ (٧)", "badge_ur": "مشق (٧): ضبط منادیٰ", "badge_en": "Exercise (7): Vocative Case",
                    "tamreen_title_ar": "اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ (الْمُنَادَى)", "tamreen_title_ur": "منادیٰ کے آخری اعراب کا ضبط", "tamreen_title_en": "Vocative Case Endings",
                    "grammar_goal_ur": "منادیٰ کو ضمہ واحدہ دینا۔", "grammar_goal_en": "Applying single dammah to vocative.",
                    "type": "vocalization", "strict_tashkeel": True,
                    "prompt_ar": f"مَا هُوَ الضَّبْطُ الصَّحِيحُ: ({it[0]})؟", "prompt_ur": f"صحیح منادیٰ منتخب کریں: ({it[0]})", "prompt_en": f"Select vocative: ({it[0]})",
                    "answer": it[0], "options": it[2], "emoji": "🗣️", "hint_ur": it[1], "hint_en": "Drops tanween.",
                    "explanation_ur": f"حرفِ ندا کے بعد تنوین گر جاتی ہے: '{it[0]}'۔", "explanation_en": f"Drops tanween: '{it[0]}'."
                })
            # T8: 4
            t8_items = [
                ("قَلَمٌ", "قَلَمُ مَنْ هٰذَا؟", ["قَلَمُ مَنْ هٰذَا؟", "قَلَمٌ مَنْ هٰذَا؟", "اَلْقَلَمُ مَنْ هٰذَا؟", "قَلَمِ مَنْ هٰذَا؟"], "یہ کس کا قلم ہے؟", "Whose pen is this?"),
                ("قَمِيصٌ", "قَمِيصُ مَنْ هٰذَا؟", ["قَمِيصُ مَنْ هٰذَا؟", "قَمِيصٌ مَنْ هٰذَا؟", "اَلْقَمِيصُ مَنْ هٰذَا؟", "قَمِيصِ مَنْ هٰذَا؟"], "یہ کس کی قمیض ہے؟", "Whose shirt is this?"),
                ("بَيْتٌ", "بَيْتُ مَنْ هٰذَا؟", ["بَيْتُ مَنْ هٰذَا؟", "بَيْتٌ مَنْ هٰذَا؟", "اَلْبَيْتُ مَنْ هٰذَا؟", "بَيْتِ مَنْ هٰذَا؟"], "یہ کس کا گھر ہے؟", "Whose house is this?"),
                ("سَرِيرٌ", "سَرِيرُ مَنْ هٰذَا؟", ["سَرِيرُ مَنْ هٰذَا؟", "سَرِيرٌ مَنْ هٰذَا؟", "اَلسَّرِيرُ مَنْ هٰذَا؟", "سَرِيرِ مَنْ هٰذَا؟"], "یہ کس کا پلنگ ہے؟", "Whose bed is this?")
            ]
            for q_idx, it in enumerate(t8_items, 1):
                unit_questions.append({
                    "id": f"b1_u5_t8_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 8,
                    "badge_ar": "التَّمْرِينُ (٨)", "badge_ur": "مشق (٨): سوالِ ملکیت", "badge_en": "Exercise (8): Possessive Questioning",
                    "tamreen_title_ar": "اقْرَأِ الْمِثَالَ ثُمَّ كَوِّنْ أَسْئِلَةً مِثْلَهُ", "tamreen_title_ur": "مثال کی طرح سوالات بنائیں", "tamreen_title_en": "Form Questions Like Example",
                    "grammar_goal_ur": "اسم کو 'مَنْ' کی طرف مضاف کرنا۔", "grammar_goal_en": "Annexing to 'man'.",
                    "type": "transformation", "strict_tashkeel": True,
                    "prompt_ar": f"كَوِّنْ سُؤَالاً لِـ ({it[0]}) مِثْلَ: (كِتَابُ مَنْ هٰذَا؟)", "prompt_ur": f"صحیح سوالیہ جملہ منتخب کریں: ({it[3]})", "prompt_en": f"Choose question: ({it[4]})",
                    "answer": it[1], "options": it[2], "emoji": "❓", "hint_ur": it[3], "hint_en": it[4],
                    "explanation_ur": f"صحیح جملہ '{it[1]}' ہے۔", "explanation_en": f"Correct question is '{it[1]}'."
                })
            # T9: 7
            t9_sentences = [
                ("ابْنُ مُحَمَّدٍ فِي الْعِرَاقِ وَابْنُ مَحْمُودٍ فِي دِمَشْقَ.", "ابن (ابتداء میں اِبْنُ، درمیان میں وَبْنُ)", "Ibn (initial vs connected)"),
                ("خَرَجَ ابْنُ الطَّبِيبِ مِنَ الْبَيْتِ.", "خرج ابن (خَرَجَبْنُ)", "Kharaja-bnu"),
                ("ذَهَبَ ابْنُ التَّاجِرِ إِلَى السُّوقِ.", "ذهب ابن (ذَهَبَبْنُ)", "Dhahaba-bnu"),
                ("اسْمُ الْمُهَنْدِسِ فَيْصَلٌ وَاسْمُ الطَّبِيبِ مَسْعُودٌ.", "اسم (اِسْمُ ابتداء میں، درمیان میں وَسْمُ)", "Ism (initial vs connected)"),
                ("مَا اسْمُ الرَّجُلِ؟", "ما اسم (مَسْمُ الرَّجُلِ)", "Masmu-r-rajul"),
                ("ابْنُ مَنْ أَنْتَ؟ أَنَا ابْنُ الْوَزِيرِ.", "ابن (اِبْنُ ابتداء میں، أَنَبْنُ درمیان میں)", "Ana-bnu-l-wazeer"),
                ("وَاسْمُ الطَّالِبِ سَمِيرٌ.", "واسم (وَسْمُ الطَّالِبِ)", "Wasmu-t-talibi")
            ]
            for q_idx, it in enumerate(t9_sentences, 1):
                unit_questions.append({
                    "id": f"b1_u5_t9_q{q_idx}", "book": 1, "unit_num": 5, "tamreen_num": 9,
                    "badge_ar": "التَّمْرِينُ (٩)", "badge_ur": "مشق (٩): ہمزۃ الوصل", "badge_en": "Exercise (9): Hamzatul Wasl",
                    "tamreen_title_ar": "اقْرَأْ مَا يَلِي مُرَاعِياً قَوَاعِدَ نُطْقِ هَمْزَةِ الْوَصْلِ", "tamreen_title_ur": "ہمزۃ الوصل کے قواعد کی رعایت کرتے ہوئے پڑھیں", "tamreen_title_en": "Rules of Hamzatul Wasl",
                    "grammar_goal_ur": "ہمزۃ الوصل کا نطق۔", "grammar_goal_en": "Phonetics of Hamzatul Wasl.",
                    "type": "sentence_reading", "strict_tashkeel": True,
                    "prompt_ar": f"اقْرَأْ مُرَاعِياً هَمْزَةَ الْوَصْلِ: {it[0]}", "prompt_ur": f"ہمزۃ الوصل کے تلفظ کا ضابطہ منتخب کریں: ({it[0]})", "prompt_en": f"Select phonetic rule: ({it[0]})",
                    "answer": it[1], "options": [it[1], "ہمزہ ہمیشہ ساکن پڑھی جائے گی", "ہمزہ ہر حالت میں لکھی اور بولی جائے گی", "ہمزہ پر پیش پڑھی جائے گی"],
                    "emoji": "🗣️", "hint_ur": it[1], "hint_en": it[2],
                    "explanation_ur": f"قاعدہ: {it[1]}۔", "explanation_en": f"Rule: {it[2]}."
                })
        else:
            # Generic extraction for other Book 1 units
            exercises = extract_exercises_from_lines(lines, p_start)
            if not exercises:
                exercises.append({'num': '1', 'desc': 'تَمْرِينُ الدَّرْسِ الشَّامِلُ', 'lines': lines[5:15], 'line_idx': 5})
            for e_idx, ex in enumerate(exercises, 1):
                t_num = int(re.sub(r'\D', '', str(ex['num'])) or e_idx)
                ratio = ex.get('line_idx', e_idx) / max(len(lines), 1)
                p_val = p_start + int(ratio * (p_end - p_start + 1))
                p_val = min(p_val, p_end)
                qs = process_exercise_to_questions(ex, 1, u_idx, t_num, p_val)
                unit_questions.extend(qs)
                curriculum_flow.append({
                    "id": f"b1_u{u_idx}_t{t_num}", "type": "tamreen",
                    "item_order": len(curriculum_flow) + 1, "tamreen_num": t_num,
                    "title_ar": f"تَمْرِين ({t_num}): {ex['desc'][:60]}", "title_ur": f"مشق ({t_num}): {ex['desc'][:60]}",
                    "title_en": f"Exercise ({t_num}): {ex['desc'][:60]}", "page": p_val, "question_count": len(qs)
                })
                
        u_copy['curriculum_flow'] = curriculum_flow
        u_copy['questions'] = unit_questions
        b1_units.append(u_copy)
    return b1_units

print("Building Book 1 with explicit lessons...")
b1_final = build_book_1_complete()

print("Building Book 2...")
from compile_complete_master_dataset import build_book_2
b2_final = build_book_2()

print("Building Book 3...")
from compile_complete_master_dataset import build_book_3
b3_final = build_book_3()

# Summary
b1_count = sum(len(u['questions']) for u in b1_final)
b2_count = sum(len(u['questions']) for u in b2_final)
b3_count = sum(len(u['questions']) for u in b3_final)
grand_total = b1_count + b2_count + b3_count

print(f"\n==========================================")
print(f"📗 Book 1 Units: {len(b1_final)}, Total Questions: {b1_count}")
print(f"📘 Book 2 Units: {len(b2_final)}, Total Questions: {b2_count}")
print(f"📙 Book 3 Units: {len(b3_final)}, Total Questions: {b3_count}")
print(f"🌟 GRAND TOTAL QUESTIONS ACROSS 71 UNITS: {grand_total}")
print(f"==========================================\n")

# Save to data/madinah_books.json
master_data['books'][0]['units'] = b1_final
master_data['books'][1]['units'] = b2_final
master_data['books'][2]['units'] = b3_final

with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print("Saved data/madinah_books.json successfully!")
