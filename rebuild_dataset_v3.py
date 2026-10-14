# rebuild_dataset_v3.py
# Comprehensive dataset builder for Madinah Books 1, 2, and 3
# Implements:
# - Full restoration of Book 1 Lesson 1 (Man Haadha)
# - Book 1 Lesson 2 Near/Far emojis and vocab table
# - Book 1 Lesson 3 Grammar pairs, separated numbered sentences, vocab tables (<= 16 words)
# - Custom Tamreen drills: Tamreen 6, 7, 8, 9, 11, 12
# - Skipping of all "Iqra waktub" across Books 1, 2, 3
# - Clean picture prompt hints (What is this? / Who is this?)
# - Strict language separation (EN, UR, and Both)
# - Donkey emoji safe replacement (no [▯] box)

import json, os, re, random

random.seed(42)

raw_dataset = json.load(open('data/madinah_books.json', encoding='utf-8'))

def strip_tashkeel(s):
    if not s: return ''
    return re.sub(r'[\u064b-\u065f\u0670\u0640]', '', str(s)).strip()

def normalize_comp(s):
    cleaned = strip_tashkeel(s)
    cleaned = re.sub(r'[\.\،\,\?\؟\!\:\"\']', '', cleaned)
    return cleaned.strip()

def is_real_urdu(text):
    if not text: return False
    if re.search(r'[a-zA-Z]', str(text)): return False
    urdu_chars = r'[ٹڈڑںہےئےگچپژ]'
    urdu_words = r'\b(یہ|وہ|ہے|ہیں|کا|کی|کے|کو|سے|میں|پر|اور|کیا|کون|نہیں|ایک|جی|ہاں|والا|تھا|تھے|تھی|کر|رہا|رہے|رہی|کہا|بولا|پوچھا)\b'
    return bool(re.search(urdu_chars, str(text)) or re.search(urdu_words, str(text)))

def sanitize_emojis(obj):
    if isinstance(obj, str):
        # Replace Unicode 15 donkey 🫏 with safe 🐴
        return obj.replace('\U0001facf', '🐴').replace('🫏', '🐴')
    elif isinstance(obj, list):
        return [sanitize_emojis(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: sanitize_emojis(v) for k, v in obj.items()}
    return obj

def strip_speaker_and_annotations(s):
    if not s: return ''
    t = str(s).strip()
    t = re.sub(r'^[:：\.\s\•\-\–\—]+', '', t).strip()
    t = re.sub(r'^(موسى|حامد|المدرس|بشير|علي|الطالب|أحمد|عمار|سعيد|ياسر|بلال|خالد|عائشة|فاطمة|مريم|زينب|التاجر|أحد الطلاب|الطلاب|أحدهم|إحداهن|إحداهنّ|إ حداهنّ|إ حداهن|عباس|هشام|إبراهيم|يوسف|إسماعيل|إسحاق|يعقوب|هارون|داود|سليمان|أيوب|يونس|زكريا|يحيى|عيسى|محمد|المعلم|الأستاذ|الولد|الرجل|المرأة|البنت|الأب|الأم|العم|الخال|الجد|الجدة|الضيف|الصديق|الجار|الأبناء|الفَتَيات|الفِتْيَة|الفِتْيَـةُ|الفتاة|قال|قالت|قالـت)[\s]*[:：]\s*', '', t).strip()
    t = re.sub(r'^[^:：]{1,25}[:：]\s*', '', t).strip()
    t = re.sub(r'[\•\-\–\—]\s*[^:]{1,25}$', '', t).strip()
    t = re.sub(r'\([^\)]+\)$', '', t).strip()
    t = re.sub(r'^(Musa|Hamid|The teacher|Teacher|Bashir|Ali|The student|Student|Ahmad|Ammar|Said|Yasir|Bilal|Khalid|Aisha|Fatima|Maryam|Zainab|The merchant|One of the students|Students|One of them|Abbas|Hisham|The youths|The girls|Sons|Father|Mother|Brother|Sister|He said|She said|موسیٰ|حامد|استاد|بشیر|علی|طالب علم|احمد|عمار|سعید|یاسر|بلال|خالد|عائشہ|فاطمہ|مریم|زینب|تاجر|طلبہ|نوجوان لڑکے|نوجوان لڑکیاں|بیٹے|باپ|ماں|بھائی|بہن|اس نے کہا|اس نے کہی)[\s]*[:：\-]\s*', '', t, flags=re.IGNORECASE).strip()
    t = re.sub(r'^[:：\.\s\•\-\–\—]+', '', t).strip()
    return t

def is_blacklisted_header_or_meta(text):
    if not text: return True
    plain = strip_tashkeel(text).strip()
    if not plain or len(plain) < 2: return True
    cleaned = re.sub(r'^\s*[\(\[\{]?\s*[\d٠-٩]+\s*[\)\]\}]?\s*[-–—:]?\s*', '', plain).strip()
    
    blacklisted_patterns = [
        r'^الدرس\b', r'^الدرْس\b', r'^الدَرْس\b', r'^الدَّرْس\b',
        r'^تمرين\b', r'^تمارين\b', r'^تدريب\b', r'^تدريبات\b',
        r'^الوحدة\b', r'^الجزء\b', r'^الصفحة\b',
        r'^الكلمات الجديدة\b', r'^المفردات الجديدة\b',
        r'^قائمة\b', r'^مقدمة\b', r'^خاتمة\b',
        r'^اقرأ واكتب\b', r'^اقْرَأْ وَاكْتُبْ\b',
        r'عبد\s*الرحيم', r'الدكتور\s*ف', r'ف\.\s*عبد',
        r'الحروف\s*(القمرية|الشمسية)', r'الحُرُوف\s*(القَمَرِيَّة|الشَّمْسِيَّة)',
        r'بسم\s*الله', r'السلام\s*عليكم',
        r'^\d+$', r'^[\W_]+$'
    ]
    for pat in blacklisted_patterns:
        if re.search(pat, cleaned) or re.search(pat, plain):
            return True
            
    urdu_headers = [
        r'^\(?\d*\)?\s*(دسواں|پہلا|دوسرا|تیسرا|چوتھا|پانچواں|چھٹا|ساتواں|آٹھواں|نواں|گیارہواں|بارہواں|تیرہواں|چودہواں|پندرہواں|سولہواں|سترہواں|اٹھارہواں|انیسواں|بیسواں)\s*سبق',
        r'^\(?\d*\)?\s*سبق\s*\d+',
        r'^\(?\d*\)?\s*مشق\s*\d+',
        r'نئے الفاظ',
        r'حصہ سوم کا مقدمہ',
        r'شروع اللہ کے نام سے',
        r'عبد الرحیم'
    ]
    for upat in urdu_headers:
        if re.search(upat, str(text)):
            return True

    return False

TASHKEEL_REPLACEMENTS = {
    'ذهب الى السوق': 'ذَهَبَ إِلَى السُّوقِ',
    'ذهب إلى السوق': 'ذَهَبَ إِلَى السُّوقِ',
    'ذهب الى السوق.': 'ذَهَبَ إِلَى السُّوقِ.',
    'ذهب إلى السوق.': 'ذَهَبَ إِلَى السُّوقِ.',
    'خرج من الفصل': 'خَرَجَ مِنَ الْفَصْلِ',
    'خرج من الفصل.': 'خَرَجَ مِنَ الْفَصْلِ.',
    'رجع من المدرسة': 'رَجَعَ مِنَ الْمَدْرَسَةِ',
    'رجع من المدرسة.': 'رَجَعَ مِنَ الْمَدْرَسَةِ.',
    'دخل المسجد': 'دَخَلَ الْمَسْجِدَ',
    'دخل المسجد.': 'دَخَلَ الْمَسْجِدَ.',
}

def apply_clean_tashkeel(s):
    if not s: return ''
    clean = s.strip()
    return TASHKEEL_REPLACEMENTS.get(clean, clean)

def extract_clean_object_statement(line_text):
    if not line_text: return ''
    t = strip_speaker_and_annotations(line_text)
    if '؟' in t:
        parts = re.split(r'[\?؟]', t)
        for p in parts[1:]:
            p_strip = p.strip()
            if p_strip:
                sub = re.sub(r'^(نَعَمْ|لَا|نعم|لا)[\s،,]*', '', p_strip).strip()
                if sub and len(sub.split()) <= 4:
                    return sub
    if len(t.split()) <= 4:
        return t
    return ''

# Curated Pools for high quality distractors
STD_DEMO_POOL = {
    'هذا': ['هٰذَا بَيْتٌ', 'هٰذَا مَسْجِدٌ', 'هٰذَا بَابٌ', 'هٰذَا كِتَابٌ', 'هٰذَا قَلَمٌ', 'هٰذَا مِفْتَاحٌ', 'هٰذَا مَكْتَبٌ', 'هٰذَا سَرِيرٌ', 'هٰذَا كُرْسِيٌّ', 'هٰذَا قَمِيصٌ', 'هٰذَا نَجْمٌ'],
    'ذلك': ['ذٰلِكَ نَجْمٌ', 'ذٰلِكَ مَسْجِدٌ', 'ذٰلِكَ بَيْتٌ', 'ذٰلِكَ حِصَانٌ', 'ذٰلِكَ حِمَارٌ', 'ذٰلِكَ قِطٌّ', 'ذٰلِكَ سَرِيرٌ', 'ذٰلِكَ حَجَرٌ'],
    'هذه': ['هٰذِهِ سَيَّارَةٌ', 'هٰذِهِ مَلْعَقَةٌ', 'هٰذِهِ قِدْرٌ', 'هٰذِهِ بَقَرَةٌ', 'هٰذِهِ حَدِيقَةٌ', 'هٰذِهِ شَمْسٌ', 'هٰذِهِ عَيْنٌ', 'هٰذِهِ أُذُنٌ'],
    'تلك': ['تِلْكَ بَقَرَةٌ', 'تِلْكَ بَيْضَةٌ', 'تِلْكَ نَاقَةٌ', 'تِلْكَ شَمْسٌ', 'تِلْكَ سَيَّارَةٌ', 'تِلْكَ حَدِيقَةٌ']
}

PEOPLE_POOL = [
    'هٰذَا طَبِيبٌ', 'هٰذَا وَلَدٌ', 'هٰذَا طَالِبٌ', 'هٰذَا رَجُلٌ', 'هٰذَا تَاجِرٌ', 
    'هٰذَا مُدَرِّسٌ', 'هٰذَا إِمَامٌ', 'هٰذَا مُهَنactionْدِسٌ'
]

# Gather high quality sentence bank per book
BOOK_SENTENCE_BANKS = {1: [], 2: [], 3: []}
for book in raw_dataset['books']:
    b_num = book['book_num']
    for unit in book['units']:
        for blk in unit.get('blocks', []):
            txt = strip_speaker_and_annotations(blk.get('text', ''))
            ur = strip_speaker_and_annotations(blk.get('ur', ''))
            en = strip_speaker_and_annotations(blk.get('en', ''))
            if txt and not is_blacklisted_header_or_meta(txt):
                if is_real_urdu(ur) and len(txt.split()) <= 6:
                    BOOK_SENTENCE_BANKS[b_num].append((txt, ur, en))

# ==============================================================
# SPECIFIC DEDICATED TAMREENS BUILDER (BOOK 1)
# ==============================================================

def build_tamreen_6_questions():
    """Tamreen 6: Alif-Lam vs Tanween distinction (single pesh vs double pesh)."""
    drills = [
        {
            "word": "مَسْجِد",
            "meaning_ur": "کوئی مسجد (غیر معین)",
            "meaning_en": "A mosque (indefinite)",
            "correct": "مَسْجِدٌ",
            "distractors": ["مَسْجِدُ", "الْمَسْجِدٌ", "مَسْجِدٍ"],
            "explanation_ur": "الـ کے بغیر اسم پر تنوین (دو پیش: ـٌ) آتی ہے: مَسْجِدٌ",
            "explanation_en": "Without Alif-Lam, the indefinite noun takes tanween (double dammah): مَسْجِدٌ"
        },
        {
            "word": "الماء",
            "meaning_ur": "پانی (خاص / معین)",
            "meaning_en": "The water (definite)",
            "correct": "الْمَاءُ",
            "distractors": ["الْمَاءٌ", "مَاءُ", "الْمَاءِ"],
            "explanation_ur": "الـ داخل ہونے سے تنوین ختم ہو جاتی ہے اور صرف ایک پیش (ـُ) آتی ہے: الْمَاءُ",
            "explanation_en": "When Alif-Lam is prefixed, tanween drops and only a single dammah is used: الْمَاءُ"
        },
        {
            "word": "البيت",
            "meaning_ur": "گھر (خاص)",
            "meaning_en": "The house (definite)",
            "correct": "الْبَيْتُ",
            "distractors": ["الْبَيْتٌ", "بَيْتُ", "الْبَيْتِ"],
            "explanation_ur": "الـ کے ساتھ اسم پر تنوین نہیں آتی، صرف ایک پیش (ـُ) آتی ہے: الْبَيْتُ",
            "explanation_en": "Definite nouns with Alif-Lam never take tanween, only a single dammah: الْبَيْتُ"
        },
        {
            "word": "قلم",
            "meaning_ur": "ایک قلم (کوئی قلم)",
            "meaning_en": "A pen (indefinite)",
            "correct": "قَلَمٌ",
            "distractors": ["قَلَمُ", "الْقَلَمٌ", "قَلَمٍ"],
            "explanation_ur": "الـ کے بغیر اسم تنوین لیتا ہے: قَلَمٌ",
            "explanation_en": "Without Alif-Lam, the noun takes tanween: قَلَمٌ"
        },
        {
            "word": "الكلب",
            "meaning_ur": "کتا (معین)",
            "meaning_en": "The dog (definite)",
            "correct": "الْكَلْبُ",
            "distractors": ["الْكَلْبٌ", "كَلْبُ", "الْكَلْبِ"],
            "explanation_ur": "الـ والے اسم کے آخر میں ایک پیش ہوتی ہے: الْكَلْبُ",
            "explanation_en": "The noun with Alif-Lam ends with a single dammah: الْكَلْبُ"
        }
    ]
    qs = []
    for d in drills:
        opts = [d['correct']] + d['distractors']
        random.shuffle(opts)
        qs.append({
            "type": "fill_blank",
            "badge_ar": "تَمْرِينُ ضَبْطِ الْأَوَاخِرِ (التَّنْوِين وَ أَلْ)",
            "badge_ur": "مشق ٦: الـ اور تنوین کا فرق (اعراب کا درست انتخاب)",
            "badge_en": "Tamreen 6: Alif-Lam vs Tanween (Ending Vowels)",
            "emoji": "⚖️",
            "strict_tashkeel": True,
            "prompt_ar": f"اخْتَرِ الضَّبْطَ الصَّحِيحَ: ({d['word']})",
            "prompt_ur": f"درست اعراب (پیش یا دو پیش) کا انتخاب کریں: ({d['meaning_ur']})",
            "prompt_en": f"Choose the correct vowel ending: ({d['meaning_en']})",
            "hint_ur": d['meaning_ur'],
            "hint_en": d['meaning_en'],
            "options": opts,
            "answer": d['correct'],
            "explanation_ur": d['explanation_ur'],
            "explanation_en": d['explanation_en']
        })
    return qs

def build_tamreen_7_questions():
    """Tamreen 7: Sentences with and without Alif-Lam tested with Urdu/English sentence."""
    drills = [
        {
            "ur": "میز ٹوٹی ہوئی ہے۔",
            "en": "The desk is broken.",
            "emoji": "🗄️",
            "correct": "الْمَكْتَبُ مَكْسُورٌ .",
            "distractors": ["مَكْتَبٌ مَكْسُورٌ .", "الْمَكْتَبُ الْمَكْسُورُ .", "مَكْتَبٌ الْمَكْسُورُ ."],
            "explanation_ur": "مبتدا معرفہ (الْمَكْتَبُ) اور خبر نکرہ (مَكْسُورٌ) ہوتی ہے: الْمَكْتَبُ مَكْسُورٌ",
            "explanation_en": "The subject is definite (الْمَكْتَبُ) and the predicate is indefinite (مَكْسُورٌ): الْمَكْتَبُ مَكْسُورٌ"
        },
        {
            "ur": "کتاب نئی ہے اور قلم پرانا ہے۔",
            "en": "The book is new and the pen is old.",
            "emoji": "📚",
            "correct": "الْكِتَابُ جَدِيدٌ وَالْقَلَمُ قَدِيمٌ .",
            "distractors": [
                "كِتَابٌ جَدِيدٌ وَقَلَمٌ قَدِيمٌ .",
                "الْكِتَابُ الْجَدِيدُ وَالْقَلَمُ الْقَدِيمُ .",
                "الْكِتَابُ جَدِيدٌ وَالْقَلَمُ الْقَدِيمُ ."
            ],
            "explanation_ur": "دونوں جملوں میں مبتدا معرفہ باللام اور خبر نکرہ ہے: الْكِتَابُ جَدِيدٌ وَالْقَلَمُ قَدِيمٌ",
            "explanation_en": "Both clauses have definite subjects with Al- and indefinite predicates: الْكِتَابُ جَدِيدٌ وَالْقَلَمُ قَدِيمٌ"
        },
        {
            "ur": "پانی ٹھنڈا ہے۔",
            "en": "The water is cold.",
            "emoji": "💧",
            "correct": "الْمَاءُ بَارِدٌ .",
            "distractors": ["مَاءٌ بَارِدٌ .", "الْمَاءُ الْبَارِدُ .", "مَاءٌ الْبَارِدُ ."],
            "explanation_ur": "درست جملہ: الْمَاءُ بَارِدٌ (پانی ٹھنڈا ہے)",
            "explanation_en": "Correct sentence: الْمَاءُ بَارِدٌ (The water is cold)"
        },
        {
            "ur": "قمیض میلی ہے۔",
            "en": "The shirt is dirty.",
            "emoji": "👕",
            "correct": "الْقَمِيصُ وَسِخٌ .",
            "distractors": ["قَمِيصٌ وَسِخٌ .", "الْقَمِيصُ الْوَسِخُ .", "قَمِيصٌ الْوَسِخُ ."],
            "explanation_ur": "درست جملہ: الْقَمِيصُ وَسِخٌ (قمیض میلی ہے)",
            "explanation_en": "Correct sentence: الْقَمِيصُ وَسِخٌ (The shirt is dirty)"
        }
    ]
    qs = []
    for d in drills:
        opts = [d['correct']] + d['distractors']
        random.shuffle(opts)
        qs.append({
            "type": "meaning_choice",
            "badge_ar": "تَمْرِينُ الْجُمْلَةِ الاسْمِيَّةِ (الْمُبْتَدَأ وَالْخَبَر)",
            "badge_ur": "مشق ٧: جملہ اسمیہ کا درست عربی ترجمہ",
            "badge_en": "Tamreen 7: Nominal Sentence Translation",
            "emoji": d['emoji'],
            "prompt_ar": d['correct'],
            "prompt_ur": f"اس اردو جملے کا درست عربی انتخاب کریں: «{d['ur']}»",
            "prompt_en": f"Select the correct Arabic translation: \"{d['en']}\"",
            "hint_ur": d['ur'],
            "hint_en": d['en'],
            "options": opts,
            "answer": d['correct'],
            "explanation_ur": d['explanation_ur'],
            "explanation_en": d['explanation_en']
        })
    return qs

def build_tamreen_8_questions():
    """Tamreen 8: Fill in the blank with suitable adjective from given pool."""
    # Book words: جَمِيلٌ ، وَسِخٌ ، مَفْتُوحٌ ، حَارٌّ ، ثَقِيلٌ ، خَفِيفٌ
    drills = [
        {
            "prompt": "الْحَجَرُ [ ＿＿＿ ] .",
            "answer": "ثَقِيلٌ",
            "meaning_ur": "پتھر بھاری ہے۔",
            "meaning_en": "The stone is heavy.",
            "emoji": "🪨",
            "distractors": ["خَفِيفٌ", "حَارٌّ", "مَفْتُوحٌ"]
        },
        {
            "prompt": "الْبَابُ [ ＿＿＿ ] .",
            "answer": "مَفْتُوحٌ",
            "meaning_ur": "دروازہ کھلا ہے۔",
            "meaning_en": "The door is open.",
            "emoji": "🚪",
            "distractors": ["مَكْسُورٌ", "حَارٌّ", "ثَقِيلٌ"]
        },
        {
            "prompt": "الْقَمَرُ [ ＿＿＿ ] .",
            "answer": "جَمِيلٌ",
            "meaning_ur": "چاند خوبصورت ہے۔",
            "meaning_en": "The moon is beautiful.",
            "emoji": "🌙",
            "distractors": ["وَسِخٌ", "حَارٌّ", "مَفْتُوحٌ"]
        },
        {
            "prompt": "الْوَرَقُ [ ＿＿＿ ] .",
            "answer": "خَفِيفٌ",
            "meaning_ur": "کاغذ ہلکا ہے۔",
            "meaning_en": "The paper is light.",
            "emoji": "📄",
            "distractors": ["ثَقِيلٌ", "حَارٌّ", "وَسِخٌ"]
        },
        {
            "prompt": "الْمِنْدِيلُ [ ＿＿＿ ] .",
            "answer": "وَسِخٌ",
            "meaning_ur": "رومال میلا ہے۔",
            "meaning_en": "The handkerchief is dirty.",
            "emoji": "🧣",
            "distractors": ["حَارٌّ", "ثَقِيلٌ", "خَفِيفٌ"]
        },
        {
            "prompt": "اللَّبَنُ [ ＿＿＿ ] .",
            "answer": "حَارٌّ",
            "meaning_ur": "دودھ گرم ہے۔",
            "meaning_en": "The milk is hot.",
            "emoji": "🥛",
            "distractors": ["مَفْتُوحٌ", "ثَقِيلٌ", "خَفِيفٌ"]
        }
    ]
    qs = []
    for d in drills:
        opts = [d['answer']] + d['distractors']
        random.shuffle(opts)
        qs.append({
            "type": "fill_blank",
            "badge_ar": "تَمْرِينُ مَلْءِ الْفَرَاغِ بِالْوَصْفِ الْمُنَاسِبِ",
            "badge_ur": "مشق ٨: خالی جگہ میں مناسب صفت منتخب کریں",
            "badge_en": "Tamreen 8: Fill the Blank with Suitable Adjective",
            "emoji": d['emoji'],
            "prompt_ar": d['prompt'],
            "prompt_ur": f"خالی جگہ کے لیے مناسب لفظ منتخب کریں: ({d['meaning_ur']})",
            "prompt_en": f"Choose the appropriate adjective: ({d['meaning_en']})",
            "hint_ur": d['meaning_ur'],
            "hint_en": d['meaning_en'],
            "options": opts,
            "answer": d['answer'],
            "explanation_ur": f"درست جواب: {d['prompt'].replace('[ ＿＿＿ ]', d['answer'])} ({d['meaning_ur']})",
            "explanation_en": f"Correct: {d['prompt'].replace('[ ＿＿＿ ]', d['answer'])} ({d['meaning_en']})"
        })
    return qs

def build_tamreen_9_questions():
    """Tamreen 9: Fill in the blank with suitable subject noun."""
    drills = [
        {
            "prompt": "[ ＿＿＿ ] نَظِيفٌ .",
            "answer": "الْمِنْدِيلُ",
            "meaning_ur": "رومال صاف ہے۔",
            "meaning_en": "The handkerchief is clean.",
            "emoji": "🧣",
            "distractors": ["الْحَجَرُ", "النَّجْمُ", "اللَّبَنُ"]
        },
        {
            "prompt": "[ ＿＿＿ ] مَكْسُورٌ .",
            "answer": "الْقَلَمُ",
            "meaning_ur": "قلم ٹوٹا ہوا ہے۔",
            "meaning_en": "The pen is broken.",
            "emoji": "🖊️",
            "distractors": ["الْمَاءُ", "الْقَمَرُ", "اللَّبَنُ"]
        },
        {
            "prompt": "[ ＿＿＿ ] بَارِدٌ .",
            "answer": "الْمَاءُ",
            "meaning_ur": "پانی ٹھنڈا ہے۔",
            "meaning_en": "The water is cold.",
            "emoji": "💧",
            "distractors": ["الْحَجَرُ", "الْقَمِيصُ", "الْكِتَابُ"]
        },
        {
            "prompt": "[ ＿＿＿ ] بَعِيدٌ .",
            "answer": "النَّجْمُ",
            "meaning_ur": "ستارہ دور ہے۔",
            "meaning_en": "The star is far.",
            "emoji": "⭐",
            "distractors": ["الْبَيْتُ", "الْمَكْتَبُ", "الْبَابُ"]
        },
        {
            "prompt": "[ ＿＿＿ ] وَاقِفٌ .",
            "answer": "الْمُدَرِّسُ",
            "meaning_ur": "استاد کھڑے ہیں۔",
            "meaning_en": "The teacher is standing.",
            "emoji": "🧑‍🏫",
            "distractors": ["الْقَلَمُ", "الْمَاءُ", "الْحَجَرُ"]
        }
    ]
    qs = []
    for d in drills:
        opts = [d['answer']] + d['distractors']
        random.shuffle(opts)
        qs.append({
            "type": "fill_blank",
            "badge_ar": "تَمْرِينُ مَلْءِ الْفَرَاغِ بِالْمُبْتَدَإِ الْمُنَاسِبِ",
            "badge_ur": "مشق ٩: خالی جگہ میں مناسب مبتدا منتخب کریں",
            "badge_en": "Tamreen 9: Fill the Blank with Suitable Subject",
            "emoji": d['emoji'],
            "prompt_ar": d['prompt'],
            "prompt_ur": f"خالی جگہ میں مناسب اسم کا انتخاب کریں: ({d['meaning_ur']})",
            "prompt_en": f"Select the suitable subject noun: ({d['meaning_en']})",
            "hint_ur": d['meaning_ur'],
            "hint_en": d['meaning_en'],
            "options": opts,
            "answer": d['answer'],
            "explanation_ur": f"درست جواب: {d['prompt'].replace('[ ＿＿＿ ]', d['answer'])} ({d['meaning_ur']})",
            "explanation_en": f"Correct: {d['prompt'].replace('[ ＿＿＿ ]', d['answer'])} ({d['meaning_en']})"
        })
    return qs

def build_tamreen_11_questions():
    """Tamreen 11 (Book 1 Unit 4): Prepositions fill in the blank (فِي، عَلَى، مِنْ، إِلَى)."""
    drills = [
        {
            "prompt": "الْكِتَابُ [ ＿＿＿ ] الْمَكْتَبِ .",
            "answer": "عَلَى",
            "meaning_ur": "کتاب میز پر ہے۔",
            "meaning_en": "The book is on the desk.",
            "emoji": "📖",
            "options": ["عَلَى", "فِي", "مِنْ", "إِلَى"]
        },
        {
            "prompt": "الطَّالِبُ [ ＿＿＿ ] الْفَصْلِ .",
            "answer": "فِي",
            "meaning_ur": "طالب علم کلاس میں ہے۔",
            "meaning_en": "The student is in the classroom.",
            "emoji": "👨‍🎓",
            "options": ["فِي", "عَلَى", "مِنْ", "إِلَى"]
        },
        {
            "prompt": "ذَهَبَ حَامِدٌ [ ＿＿＿ ] الْجَامِعَةِ .",
            "answer": "إِلَى",
            "meaning_ur": "حامد یونیورسٹی گیا۔",
            "meaning_en": "Hamid went to the university.",
            "emoji": "🚶",
            "options": ["إِلَى", "مِنْ", "فِي", "عَلَى"]
        },
        {
            "prompt": "خَرَجَ الْمُدِيرُ [ ＿＿＿ ] الْمَدْرَسَةِ .",
            "answer": "مِنَ",
            "meaning_ur": "پرنسپل اسکول سے نکلے۔",
            "meaning_en": "The principal exited from the school.",
            "emoji": "🏫",
            "options": ["مِنَ", "إِلَى", "فِي", "عَلَى"]
        }
    ]
    qs = []
    for d in drills:
        opts = list(d['options'])
        random.shuffle(opts)
        qs.append({
            "type": "fill_blank",
            "badge_ar": "تَمْرِينُ حُرُوفِ الْجَرِّ (فِي، عَلَى، مِنْ، إِلَى)",
            "badge_ur": "مشق ١١: خالی جگہ میں مناسب حرف جار منتخب کریں",
            "badge_en": "Tamreen 11: Fill Blanks with Suitable Preposition",
            "emoji": d['emoji'],
            "prompt_ar": d['prompt'],
            "prompt_ur": f"خالی جگہ میں درست حرفِ جار کا انتخاب کریں: ({d['meaning_ur']})",
            "prompt_en": f"Choose the correct preposition: ({d['meaning_en']})",
            "hint_ur": d['meaning_ur'],
            "hint_en": d['meaning_en'],
            "options": opts,
            "answer": d['answer'],
            "explanation_ur": f"درست جواب: {d['prompt'].replace('[ ＿＿＿ ]', d['answer'])} ({d['meaning_ur']})",
            "explanation_en": f"Correct: {d['prompt'].replace('[ ＿＿＿ ]', d['answer'])} ({d['meaning_en']})"
        })
    return qs

def build_tamreen_12_question():
    """Tamreen 12 (Book 1 Unit 3): Two-column matching drill directly from the book!"""
    return {
        "type": "pair_match",
        "badge_ar": "تَمْرِينُ التَّوْفِيقِ بَيْنَ الْقَائِمَتَيْنِ (أ) وَ (ب)",
        "badge_ur": "مشق ۱۲: کالم (الف) اور کالم (ب) کا درست جوڑ ملائیں",
        "badge_en": "Tamreen 12: Match Column (A) with Column (B)",
        "emoji": "📋",
        "prompt_ar": "اخْتَرْ كَلِمَةً مِنَ الْقَائِمَةِ (ب) تُنَاسِبُ كَلِمَةً فِي الْقَائِمَةِ (أ):",
        "prompt_ur": "کالم (الف) کے لفظ پر کلک کریں اور پھر کالم (ب) میں اس کی مناسب خبر منتخب کریں:",
        "prompt_en": "Click a word in Column (A) then match its fitting word in Column (B):",
        "hint_ur": "ہر مبتدا کے لیے اس کی درست صفت ملائیں",
        "hint_en": "Match each subject noun to its correct predicate",
        "pairs": [
            {
                "left_ar": "الطَّالِبُ",
                "right": "مَرِيضٌ",
                "left_ur": "طالب علم",
                "right_ur": "بیمار ہے",
                "left_en": "The student",
                "right_en": "is sick"
            },
            {
                "left_ar": "الدُّكَّانُ",
                "right": "مَفْتُوحٌ",
                "left_ur": "دکان",
                "right_ur": "کھلی ہے",
                "left_en": "The shop",
                "right_en": "is open"
            },
            {
                "left_ar": "التُّفَّاحُ",
                "right": "لَذِيذٌ",
                "left_ur": "سیب",
                "right_ur": "لذیذ ہے",
                "left_en": "The apple",
                "right_en": "is delicious"
            },
            {
                "left_ar": "الْمَاءُ",
                "right": "حَارٌّ",
                "left_ur": "پانی",
                "right_ur": "گرم ہے",
                "left_en": "The water",
                "right_en": "is hot"
            },
            {
                "left_ar": "الْحَجَرُ",
                "right": "ثَقِيلٌ",
                "left_ur": "پتھر",
                "right_ur": "بھاری ہے",
                "left_en": "The stone",
                "right_en": "is heavy"
            },
            {
                "left_ar": "الْقَلَمُ",
                "right": "مَكْسُورٌ",
                "left_ur": "قلم",
                "right_ur": "ٹوٹا ہوا ہے",
                "left_en": "The pen",
                "right_en": "is broken"
            }
        ],
        "answer": "matched",
        "explanation_ur": "ماشاءاللہ! آپ نے کالم (الف) اور (ب) کے تمام جوڑ بالکل درست ملا لیے ہیں۔",
        "explanation_en": "Excellent! You matched all pairs in Column A and Column B correctly."
    }

# Load the exact clean lesson blocks for Units 1, 2, and 3 from patch_book1_lessons.py
from patch_book1_lessons import clean_u1_blocks, clean_u2_blocks, clean_u3_blocks

clean_books = []

for book in raw_dataset['books']:
    b_num = book['book_num']
    clean_units = []

    for unit in book['units']:
        u_num = unit['unit_num']
        unit_emoji = sanitize_emojis(unit.get('emoji', '📖'))

        # Check if this is Unit 1, 2, or 3 of Book 1
        if b_num == 1 and u_num == 1:
            lesson_blocks = sanitize_emojis(clean_u1_blocks)
        elif b_num == 1 and u_num == 2:
            lesson_blocks = sanitize_emojis(clean_u2_blocks)
        elif b_num == 1 and u_num == 3:
            lesson_blocks = sanitize_emojis(clean_u3_blocks)
        else:
            # Process normal unit blocks, skipping all exercises and iqra waktub
            lesson_blocks = []
            for blk in unit.get('blocks', []):
                sec = blk.get('section', 'lesson')
                btype = blk.get('type')
                raw_t = blk.get('text', '').strip()

                is_ex = (sec == 'exercises') or (btype == 'exercise_line') or bool(re.search(r'^(تمارين|تمرين|التدريبات|اقرأ واكتب|اقْرَأْ وَاكْتُبْ)', raw_t))
                if is_ex:
                    continue

                clean_blk = dict(blk)
                if btype == 'emoji_grid':
                    clean_cards = []
                    for c in blk.get('cards', []):
                        cc = dict(c)
                        c_txt = strip_speaker_and_annotations(cc.get('text', ''))
                        c_ur = strip_speaker_and_annotations(cc.get('ur', ''))
                        c_en = strip_speaker_and_annotations(cc.get('en', ''))
                        cc['text'] = c_txt
                        cc['ur'] = c_ur
                        cc['en'] = c_en
                        clean_cards.append(cc)
                    clean_blk['cards'] = sanitize_emojis(clean_cards)
                    lesson_blocks.append(clean_blk)
                else:
                    spk = blk.get('speaker', '')
                    clean_t = strip_speaker_and_annotations(raw_t)
                    clean_ur = strip_speaker_and_annotations(blk.get('ur', ''))
                    clean_en = strip_speaker_and_annotations(blk.get('en', ''))

                    if not spk and ':' in raw_t:
                        m = re.match(r'^([^:]{1,20}):\s*(.*)$', raw_t)
                        if m:
                            spk = m.group(1).strip()
                            clean_t = strip_speaker_and_annotations(m.group(2))

                    clean_blk['speaker'] = spk
                    clean_blk['text'] = clean_t
                    clean_blk['ur'] = clean_ur
                    clean_blk['en'] = clean_en
                    clean_blk = sanitize_emojis(clean_blk)

                    if clean_t and not is_blacklisted_header_or_meta(clean_t):
                        lesson_blocks.append(clean_blk)

        # GATHER ITEMS FOR EXERCISES
        unit_visuals = []
        unit_sentences = []
        unit_dialogues = []

        for idx, blk in enumerate(lesson_blocks):
            btype = blk.get('type')
            txt = blk.get('text', '').strip()
            ur = blk.get('ur', '').strip()
            en = blk.get('en', '').strip()

            if is_blacklisted_header_or_meta(txt):
                continue

            if btype == 'emoji_grid':
                for c in blk.get('cards', []):
                    c_st = extract_clean_object_statement(c.get('text', ''))
                    c_ur = strip_speaker_and_annotations(c.get('ur', ''))
                    c_en = strip_speaker_and_annotations(c.get('en', ''))
                    if c.get('emoji') and c_st and not is_blacklisted_header_or_meta(c_st):
                        unit_visuals.append((c_st, c_ur, c_en, c['emoji']))
            elif btype == 'illustrated_line':
                em = blk.get('emoji', unit_emoji)
                c_st = extract_clean_object_statement(txt)
                if c_st and not is_blacklisted_header_or_meta(c_st):
                    unit_visuals.append((c_st, ur, en, em))
            elif btype == 'dialogue':
                if '؟' in txt:
                    q_iso = txt.split('؟')[0].strip() + '؟'
                    if q_iso and not is_blacklisted_header_or_meta(q_iso):
                        ans_text = None
                        ans_ur = None
                        ans_en = None
                        for nxt_idx in range(idx + 1, min(idx + 4, len(lesson_blocks))):
                            nxt_blk = lesson_blocks[nxt_idx]
                            nxt_clean = strip_speaker_and_annotations(nxt_blk.get('text', ''))
                            if nxt_clean and not is_blacklisted_header_or_meta(nxt_clean) and '؟' not in nxt_clean:
                                ans_text = nxt_clean
                                ans_ur = strip_speaker_and_annotations(nxt_blk.get('ur', ''))
                                ans_en = strip_speaker_and_annotations(nxt_blk.get('en', ''))
                                break
                        if ans_text:
                            unit_dialogues.append({
                                'q_text': q_iso,
                                'q_ur': ur,
                                'q_en': en,
                                'emoji': blk.get('speaker_emoji') or unit_emoji,
                                'ans_text': ans_text,
                                'ans_ur': ans_ur,
                                'ans_en': ans_en
                            })
                else:
                    if txt and 10 <= len(txt) <= 65 and 2 <= len(txt.split()) <= 8 and '؟' not in txt:
                        unit_sentences.append((txt, ur, en, blk.get('speaker_emoji') or unit_emoji))
            elif btype in ['text', 'vocab_row', 'table_row']:
                if txt and 10 <= len(txt) <= 65 and 2 <= len(txt.split()) <= 8 and '•' not in txt and not txt.startswith('=') and not is_blacklisted_header_or_meta(txt) and '؟' not in txt:
                    unit_sentences.append((txt, ur, en, unit_emoji))

        # EXERCISES GENERATION
        questions = []

        # If Book 1 Unit 3: Add dedicated Tamreen 6, 7, 8, 9, 12!
        if b_num == 1 and u_num == 3:
            questions.extend(build_tamreen_6_questions()[:3])  # 3 questions for Tamreen 6
            questions.extend(build_tamreen_7_questions()[:2])  # 2 questions for Tamreen 7
            questions.extend(build_tamreen_8_questions()[:3])  # 3 questions for Tamreen 8
            questions.extend(build_tamreen_9_questions()[:2])  # 2 questions for Tamreen 9
            questions.append(build_tamreen_12_question())       # Tamreen 12 Column Match!

        # If Book 1 Unit 4: Add dedicated Tamreen 11!
        elif b_num == 1 and u_num == 4:
            questions.extend(build_tamreen_11_questions())

        # For all other units (and to complement):
        if len(questions) < 5:
            # 1. Visual Object / Person Identification Drill (Image 1 fix: concise hint!)
            for ar_txt, ur, en, em in unit_visuals:
                if len(questions) >= 4: break
                clean_txt = strip_tashkeel(ar_txt)
                first_word = clean_txt.split()[0] if clean_txt.split() else 'هذا'
                is_person = any(w in clean_txt for w in ['طبيب', 'مدرس', 'طالب', 'ولد', 'رجل', 'تاجر', 'طبيبة', 'ممرضة', 'بنت', 'إمام', 'شيخ', 'مهندس'])
                if first_word in ['هذا', 'هٰذَا']: 
                    prompt_ar = "مَنْ هٰذَا؟" if is_person else "مَا هٰذَا؟"
                    hint_ur_clean = "یہ کون ہے؟" if is_person else "یہ کیا ہے؟"
                    hint_en_clean = "Who is this?" if is_person else "What is this?"
                elif first_word in ['ذلك', 'ذٰلِكَ']: 
                    prompt_ar = "مَنْ ذٰلِكَ؟" if is_person else "مَا ذٰلِكَ؟"
                    hint_ur_clean = "وہ کون ہے؟" if is_person else "وہ کیا ہے؟"
                    hint_en_clean = "Who is that?" if is_person else "What is that?"
                elif first_word in ['هذه', 'هٰذِهِ']: 
                    prompt_ar = "مَنْ هٰذِهِ؟" if is_person else "مَا هٰذِهِ؟"
                    hint_ur_clean = "یہ کون ہے؟" if is_person else "یہ کیا ہے؟"
                    hint_en_clean = "Who is this?" if is_person else "What is this?"
                elif first_word in ['تلك', 'تِلْكَ']: 
                    prompt_ar = "مَنْ تِلْكَ؟" if is_person else "مَا تِلْكَ؟"
                    hint_ur_clean = "وہ کون ہے؟" if is_person else "وہ کیا ہے؟"
                    hint_en_clean = "Who is that?" if is_person else "What is that?"
                else: 
                    prompt_ar = "اخْتَرْ الْعِبَارَةَ الصَّحِيحَةَ لِلصُّورَةِ:"
                    hint_ur_clean = ur
                    hint_en_clean = en

                pool = PEOPLE_POOL if is_person else STD_DEMO_POOL.get(first_word, STD_DEMO_POOL['هذا'])
                cands = [item for item in pool if normalize_comp(item) != normalize_comp(clean_txt) and not is_blacklisted_header_or_meta(item)]
                random.shuffle(cands)
                opts = [ar_txt] + cands[:3]
                if len(opts) == 4 and not any('؟' in o or ':' in o for o in opts):
                    random.shuffle(opts)
                    questions.append({
                        "type": "emoji_choice",
                        "badge_ar": "تَمْرِينُ التَّعَرُّفِ عَلَى الصُّوَرِ",
                        "badge_ur": "مشق: تصویر کی پہچان",
                        "badge_en": "Exercise: Picture Identification",
                        "emoji": em,
                        "prompt_ar": prompt_ar,
                        "prompt_ur": f"تصویر {em} دیکھ کر درست جواب منتخب کریں:",
                        "prompt_en": f"Look at picture {em} and choose the correct answer:",
                        "hint_ur": hint_ur_clean,
                        "hint_en": hint_en_clean,
                        "options": opts,
                        "answer": ar_txt,
                        "explanation_ur": f"درست جواب: {ar_txt}" + (f" ({ur})" if ur else ""),
                        "explanation_en": f"Correct: {ar_txt}" + (f" ({en})" if en else "")
                    })

            # 2. Sentence Builder Drill
            pool_sentences = unit_visuals + unit_sentences
            for ar_txt, ur, en, em in pool_sentences:
                if len(questions) >= 6: break
                if '؟' in ar_txt or ':' in ar_txt or is_blacklisted_header_or_meta(ar_txt): continue
                if re.search(r'[a-zA-Z]', ar_txt) or re.search(r'[ٹڈڑںہےئےگچپژ]', ar_txt): continue
                ar_clean_txt = apply_clean_tashkeel(ar_txt)
                words = ar_clean_txt.split()
                if 2 <= len(words) <= 5 and 10 <= len(ar_clean_txt) <= 50 and '•' not in ar_clean_txt:
                    shuffled = list(words)
                    random.shuffle(shuffled)
                    questions.append({
                        "type": "sentence_builder",
                        "badge_ar": "تَمْرِينُ تَرْكِيبِ الْجُمْلَةِ",
                        "badge_ur": "مشق: جملہ سازی",
                        "badge_en": "Exercise: Sentence Builder",
                        "emoji": em,
                        "prompt_ar": "رَتِّبِ الْكَلِمَاتِ لِتَكْوِينِ جُمْلَةٍ مُفِيدَةٍ:",
                        "prompt_ur": "الفاظ کو ترتیب دے کر درست عربی جملہ بنائیں:",
                        "prompt_en": "Arrange the word tiles to form the correct sentence:",
                        "hint_ur": ur,
                        "hint_en": en,
                        "tiles": shuffled,
                        "answer": ar_clean_txt,
                        "explanation_ur": f"درست جملہ: {ar_clean_txt}" + (f" ({ur})" if ur else ""),
                        "explanation_en": f"Correct sentence: {ar_clean_txt}" + (f" ({en})" if en else "")
                    })
                    break

            # 3. Translation Drill
            trans_candidates = [it for it in pool_sentences if is_real_urdu(it[1]) and '؟' not in it[0] and ':' not in it[0] and not is_blacklisted_header_or_meta(it[0]) and 10 <= len(it[0]) <= 65]
            if trans_candidates and len(questions) < 7:
                m_txt, m_ur, m_en, m_em = trans_candidates[0]
                m_txt = apply_clean_tashkeel(m_txt)
                distractors_ur = []
                for other_txt, other_ur, other_en in BOOK_SENTENCE_BANKS.get(b_num, []):
                    if is_real_urdu(other_ur) and normalize_comp(other_ur) != normalize_comp(m_ur):
                        if other_ur not in distractors_ur:
                            distractors_ur.append(other_ur)
                    if len(distractors_ur) >= 6: break
                if len(distractors_ur) >= 3:
                    final_opts = [m_ur] + distractors_ur[:3]
                    random.shuffle(final_opts)
                    questions.append({
                        "type": "meaning_choice",
                        "badge_ar": "تَمْرِينُ تَرْجَمَةِ الْمَعْنَى",
                        "badge_ur": "مشق: ترجمہ کا انتخاب",
                        "badge_en": "Exercise: Meaning Translation",
                        "emoji": m_em,
                        "prompt_ar": m_txt,
                        "prompt_ur": "اس عربی عبارت کا درست اردو ترجمہ منتخب کریں:",
                        "prompt_en": "Select the correct translation of this sentence:",
                        "hint_ur": m_ur,
                        "hint_en": m_en,
                        "options": final_opts,
                        "answer": m_ur,
                        "explanation_ur": f"درست ترجمہ: {m_ur}",
                        "explanation_en": f"Correct translation: {m_en}"
                    })

        clean_unit = dict(unit)
        clean_unit['emoji'] = unit_emoji
        clean_unit['blocks'] = sanitize_emojis(lesson_blocks)
        clean_unit['questions'] = sanitize_emojis(questions)
        clean_unit['line_count'] = len(lesson_blocks)
        clean_units.append(clean_unit)

    clean_book = dict(book)
    clean_book['units'] = clean_units
    clean_books.append(clean_book)

clean_dataset = {"books": clean_books}
clean_dataset = sanitize_emojis(clean_dataset)

with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(clean_dataset, f, ensure_ascii=False, indent=2)

with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write('window.MADINAH_DATA = ' + json.dumps(clean_dataset, ensure_ascii=False) + ';\n')

print("SUCCESS: Full Clean Dataset v3 generated!")
total_u = sum(len(b['units']) for b in clean_books)
total_b = sum(sum(len(u['blocks']) for u in b['units']) for b in clean_books)
total_q = sum(sum(len(u['questions']) for u in b['units']) for b in clean_books)
print(f"Total units: {total_u}")
print(f"Total pure lesson blocks: {total_b}")
print(f"Total exercise questions: {total_q}")
print(f"Book 1 Unit 1 questions: {len(clean_books[0]['units'][0]['questions'])}")
print(f"Book 1 Unit 2 questions: {len(clean_books[0]['units'][1]['questions'])}")
print(f"Book 1 Unit 3 questions: {len(clean_books[0]['units'][2]['questions'])}")
print(f"Book 1 Unit 4 questions: {len(clean_books[0]['units'][3]['questions'])}")
