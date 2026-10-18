import json, re, sys, os, random

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

# Load existing dataset
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Load Cairo transcription
with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo_md = f.read()

# Load Manifest
with open(r'C:\Users\Person\.gemini\antigravity\brain\871510d4-1766-4c62-b894-0270b402a9f3\madinah_curriculum_tamreens_manifest.md', 'r', encoding='utf-8') as f:
    manifest_md = f.read()

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

# Distractor generators
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

# Split sections
b1_idx = cairo_md.find('## 📗')
b2_idx = cairo_md.find('## 📘')
b3_idx = cairo_md.find('## 📙')

b1_secs = re.split(r'\n###\s+', cairo_md[b1_idx:b2_idx])[1:]
b2_secs = re.split(r'\n###\s+', cairo_md[b2_idx:b3_idx])[2:]
b3_secs = re.split(r'\n###\s+', cairo_md[b3_idx:])[2:]

# Function to extract exercises and subquestions from section lines
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

# Function to process an exercise into questions
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
        
        # Determine question type
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
            "badge_ur": f"مشق ({t_num}): تمرين ({p_idx})",
            "badge_en": f"Exercise ({t_num}): Drill ({p_idx})",
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

# Build Book 2
def build_book_2():
    b2_units = []
    b2_source_units = master_data['books'][1]['units']
    
    for u_idx in range(1, 32):
        src_u = b2_source_units[u_idx - 1] if u_idx - 1 < len(b2_source_units) else {}
        u_copy = dict(src_u)
        p_start = B2_PAGES.get(u_idx, 5)
        p_end = B2_PAGES.get(u_idx + 1, p_start + 4) - 1 if u_idx < 31 else 223
        
        curriculum_flow = []
        unit_questions = []
        
        # 1. Lesson Reading Text
        preview_text = ""
        for bl in u_copy.get('blocks', []):
            if bl.get('text'):
                preview_text = bl['text'][:120]
                break
        
        curriculum_flow.append({
            "id": f"b2_u{u_idx}_item_nas",
            "type": "nasuddars",
            "item_order": 1,
            "title_ar": "نَصُّ الدَّرْسِ (الْحِوَارُ وَالْقِرَاءَةُ)",
            "title_ur": "سبق کا متن و مکالمہ",
            "title_en": "Lesson Reading & Dialogue",
            "page": p_start,
            "preview": preview_text or u_copy.get('title_ar', '')
        })
        
        # Parse exercises from section
        s = b2_secs[u_idx - 1] if u_idx - 1 < len(b2_secs) else ""
        lines = [l.strip() for l in s.split('\n') if l.strip()]
        exercises = extract_exercises_from_lines(lines, p_start)
        
        for e_idx, ex in enumerate(exercises, 1):
            t_num = int(re.sub(r'\D', '', str(ex['num'])) or e_idx)
            ratio = ex['line_idx'] / max(len(lines), 1)
            p_val = p_start + int(ratio * (p_end - p_start + 1))
            p_val = min(p_val, p_end)
            
            qs = process_exercise_to_questions(ex, 2, u_idx, t_num, p_val)
            unit_questions.extend(qs)
            
            curriculum_flow.append({
                "id": f"b2_u{u_idx}_t{t_num}",
                "type": "tamreen",
                "item_order": len(curriculum_flow) + 1,
                "tamreen_num": t_num,
                "title_ar": f"تَمْرِين ({t_num}): {ex['desc'][:60]}",
                "title_ur": f"مشق ({t_num}): {ex['desc'][:60]}",
                "title_en": f"Exercise ({t_num}): {ex['desc'][:60]}",
                "page": p_val,
                "question_count": len(qs)
            })
            
        # Review Lessons Snippets in Book 2
        if u_idx == 22:
            curriculum_flow.append({
                "id": f"b2_u22_qaida",
                "type": "qaida",
                "item_order": len(curriculum_flow) + 1,
                "title_ar": "قَاعِدَةٌ: حَالَاتُ الْفِعْلِ الْمُضَارِعِ الثَّلَاثُ (الْمَرْفُوعُ وَالْمَنْصُوبُ وَالْمَجْزُومُ)",
                "title_ur": "قاعدہ: فعل مضارع کی تینوں حالتیں (مرفوع، منصوب، مجزوم) تمام ضمائر کے ساتھ",
                "title_en": "Rule Snippet: Three Moods of Present Tense Verb with All Pronouns",
                "page": 153,
                "rule_summary_ur": "فعل مضارع کی تین حالتیں ہوتی ہیں: مرفوع (ضمہ یا ثبوت نون)، منصوب (فتحة یا حذف نون)، اور مجزوم (سکون یا حذف نون)۔",
                "rule_summary_en": "The present tense verb (المضارع) has three moods: Marfoo (nominative), Mansoob (subjunctive), and Majzoom (jussive).",
                "examples": [
                    {"ar": "هُوَ يَذْهَبُ / لَنْ يَذْهَبَ / لَمْ يَذْهَبْ", "ur": "وہ جاتا ہے / وہ ہرگز نہیں جائے گا / وہ نہیں گیا", "en": "He goes / He will not go / He did not go"},
                    {"ar": "هُمْ يَذْهَبُونَ / لَنْ يَذْهَبُوا / لَمْ يَذْهَبُوا", "ur": "وہ سب جاتے ہیں / وہ ہرگز نہیں جائیں گے / وہ نہیں گئے", "en": "They go / They will not go / They did not go"}
                ]
            })
        elif u_idx == 24:
            curriculum_flow.append({
                "id": f"b2_u24_qaida",
                "type": "qaida",
                "item_order": len(curriculum_flow) + 1,
                "title_ar": "قَاعِدَةٌ: مُرَاجَعَةٌ شَامِلَةٌ لِقَوَاعِدِ الْعَدَدِ وَالْمَعْدُودِ (١ - ١٠٠)",
                "title_ur": "قاعدہ: 1 سے 100 تک گنتی اور معدود کے قواعد کا مکمل خلاصہ",
                "title_en": "Rule Snippet: Comprehensive Master Reference for Numbers 1 to 100",
                "page": 161,
                "rule_summary_ur": "1 اور 2 صفت بنتے ہیں۔ 3 سے 10 تک عدد معدود کے الٹ جنس میں آتا ہے اور معدود جمع مجرور ہوتا ہے۔ 11 سے 19 تک دونوں جز مبنی بر فتحہ ہوتے ہیں اور معدود مفرد منصوب ہوتا ہے۔ 20 سے 90 عقود ہیں اور معدود مفرد منصوب ہوتا ہے۔ 100 اور 1000 میں معدود مفرد مجرور ہوتا ہے۔",
                "rule_summary_en": "1-2 agree as adjectives; 3-10 take opposite gender with plural genitive; 11-19 take singular accusative; 20-90 take singular accusative; 100 and 1000 take singular genitive.",
                "examples": [
                    {"ar": "ثَلَاثَةُ رِجَالٍ / ثَلَاثُ نِسَاءٍ", "ur": "تین مرد / تین عورتیں", "en": "Three men / Three women"},
                    {"ar": "أَحَدَ عَشَرَ كَوْكَبًا", "ur": "گیارہ ستارے", "en": "Eleven stars"}
                ]
            })
            
        u_copy['curriculum_flow'] = curriculum_flow
        u_copy['questions'] = unit_questions
        b2_units.append(u_copy)
        
    return b2_units

# Build Book 3
def build_book_3():
    b3_units = []
    b3_source_units = master_data['books'][2]['units']
    
    for u_idx in range(1, 18):
        src_u = b3_source_units[u_idx - 1] if u_idx - 1 < len(b3_source_units) else {}
        u_copy = dict(src_u)
        p_start = B3_PAGES.get(u_idx, 5)
        p_end = B3_PAGES.get(u_idx + 1, p_start + 5) - 1 if u_idx < 17 else 144
        
        curriculum_flow = []
        unit_questions = []
        
        # 1. Lesson Reading Text
        preview_text = ""
        for bl in u_copy.get('blocks', []):
            if bl.get('text'):
                preview_text = bl['text'][:120]
                break
        
        curriculum_flow.append({
            "id": f"b3_u{u_idx}_item_nas",
            "type": "nasuddars",
            "item_order": 1,
            "title_ar": "نَصُّ الدَّرْسِ (الْحِوَارُ وَالنُّصُوصُ النَّحْوِيَّةُ)",
            "title_ur": "سبق کا متن و نحوی مطالعہ",
            "title_en": "Lesson Reading & Advanced Dialogue",
            "page": p_start,
            "preview": preview_text or u_copy.get('title_ar', '')
        })
        
        if u_idx == 9:
            # PRESERVE existing 93 unabridged questions for Book 3 Lesson 9!
            existing_qs = src_u.get('questions', [])
            unit_questions = existing_qs
            
            # Map into curriculum_flow
            t_map = {}
            for q in existing_qs:
                t_num = q.get('tamreen_num', 1)
                if t_num not in t_map:
                    t_map[t_num] = {
                        'title_ar': q.get('tamreen_title_ar', f"تَمْرِين ({t_num})"),
                        'title_ur': q.get('tamreen_title_ur', f"مشق ({t_num})"),
                        'title_en': q.get('tamreen_title_en', f"Exercise ({t_num})"),
                        'count': 0
                    }
                t_map[t_num]['count'] += 1
                
            for t_num, t_data in sorted(t_map.items()):
                curriculum_flow.append({
                    "id": f"b3_u9_t{t_num}",
                    "type": "tamreen",
                    "item_order": len(curriculum_flow) + 1,
                    "tamreen_num": t_num,
                    "title_ar": f"تَمْرِين ({t_num}): {t_data['title_ar'][:60]}",
                    "title_ur": f"مشق ({t_num}): {t_data['title_ur'][:60]}",
                    "title_en": f"Exercise ({t_num}): {t_data['title_en'][:60]}",
                    "page": 74 + t_num // 2,
                    "question_count": t_data['count']
                })
        else:
            # Parse exercises from section
            s = b3_secs[u_idx - 1] if u_idx - 1 < len(b3_secs) else ""
            lines = [l.strip() for l in s.split('\n') if l.strip()]
            exercises = extract_exercises_from_lines(lines, p_start)
            
            for e_idx, ex in enumerate(exercises, 1):
                t_num = int(re.sub(r'\D', '', str(ex['num'])) or e_idx)
                ratio = ex['line_idx'] / max(len(lines), 1)
                p_val = p_start + int(ratio * (p_end - p_start + 1))
                p_val = min(p_val, p_end)
                
                qs = process_exercise_to_questions(ex, 3, u_idx, t_num, p_val)
                unit_questions.extend(qs)
                
                curriculum_flow.append({
                    "id": f"b3_u{u_idx}_t{t_num}",
                    "type": "tamreen",
                    "item_order": len(curriculum_flow) + 1,
                    "tamreen_num": t_num,
                    "title_ar": f"تَمْرِين ({t_num}): {ex['desc'][:60]}",
                    "title_ur": f"مشق ({t_num}): {ex['desc'][:60]}",
                    "title_en": f"Exercise ({t_num}): {ex['desc'][:60]}",
                    "page": p_val,
                    "question_count": len(qs)
                })
                
        u_copy['curriculum_flow'] = curriculum_flow
        u_copy['questions'] = unit_questions
        b3_units.append(u_copy)
        
    return b3_units

if __name__ == '__main__':
    b1_final_units = build_book_1()
    b2_final_units = build_book_2()
    b3_final_units = build_book_3()

    total_b1_qs = sum(len(u['questions']) for u in b1_final_units)
    total_b2_qs = sum(len(u['questions']) for u in b2_final_units)
    total_b3_qs = sum(len(u['questions']) for u in b3_final_units)

    print(f"Book 1 compiled: {len(b1_final_units)} units, {total_b1_qs} total questions.")
    print(f"Book 2 compiled: {len(b2_final_units)} units, {total_b2_qs} total questions.")
    print(f"Book 3 compiled: {len(b3_final_units)} units, {total_b3_qs} total questions.")
    print(f"ALL BOOKS GRAND TOTAL QUESTIONS: {total_b1_qs + total_b2_qs + total_b3_qs}")

