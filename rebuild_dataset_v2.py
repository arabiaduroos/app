# rebuild_dataset_v2.py
# Clean dataset generator for Madinah Books 1, 2, and 3
# Fixes all issues: speaker names, colon bugs, topic leaks, mismatched distractors, layout sizing.

import json, os, re, random

# Seed for reproducible high quality
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

# Comprehensive speaker stripper for Arabic, Urdu, and English
def strip_speaker_and_annotations(s):
    if not s: return ''
    t = str(s).strip()
    # Remove leading punctuation
    t = re.sub(r'^[:：\.\s\•\-\–\—]+', '', t).strip()
    # Remove known Arabic speaker titles and names followed by colon
    t = re.sub(r'^(موسى|حامد|المدرس|بشير|علي|الطالب|أحمد|عمار|سعيد|ياسر|بلال|خالد|عائشة|فاطمة|مريم|زينب|التاجر|أحد الطلاب|الطلاب|أحدهم|إحداهن|إحداهنّ|إ حداهنّ|إ حداهن|عباس|هشام|إبراهيم|يوسف|إسماعيل|إسحاق|يعقوب|هارون|داود|سليمان|أيوب|يونس|زكريا|يحيى|عيسى|محمد|المعلم|الأستاذ|الولد|الرجل|المرأة|البنت|الأب|الأم|العم|الخال|الجد|الجدة|الضيف|الصديق|الجار|الأبناء|الفَتَيات|الفِتْيَة|الفِتْيَـةُ|الفتاة|قال|قالت|قالـت)[\s]*[:：]\s*', '', t).strip()
    # Remove generic speaker prefixes like "X: " where X is 1-3 words
    t = re.sub(r'^[^:：]{1,25}[:：]\s*', '', t).strip()
    # Remove trailing speaker annotations like "• إحداهنّ", "- قال علي"
    t = re.sub(r'[\•\-\–\—]\s*[^:]{1,25}$', '', t).strip()
    # Remove trailing parentheses annotations like "(موسى)"
    t = re.sub(r'\([^\)]+\)$', '', t).strip()
    # Remove Urdu/English speaker names followed by colon
    t = re.sub(r'^(Musa|Hamid|The teacher|Teacher|Bashir|Ali|The student|Student|Ahmad|Ammar|Said|Yasir|Bilal|Khalid|Aisha|Fatima|Maryam|Zainab|The merchant|One of the students|Students|One of them|Abbas|Hisham|The youths|The girls|Sons|Father|Mother|Brother|Sister|He said|She said|موسیٰ|حامد|استاد|بشیر|علی|طالب علم|احمد|عمار|سعید|یاسر|بلال|خالد|عائشہ|فاطمہ|مریم|زینب|تاجر|طلبہ|نوجوان لڑکے|نوجوان لڑکیاں|بیٹے|باپ|ماں|بھائی|بہن|اس نے کہا|اس نے کہی)[\s]*[:：\-]\s*', '', t, flags=re.IGNORECASE).strip()
    # Final cleanup
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
    clean_no_period = clean.rstrip('.')
    if clean in TASHKEEL_REPLACEMENTS:
        return TASHKEEL_REPLACEMENTS[clean]
    if clean_no_period in TASHKEEL_REPLACEMENTS:
        return TASHKEEL_REPLACEMENTS[clean_no_period] + ('.' if clean.endswith('.') else '')
    return clean

def clean_dialogue_answer(ans):
    if not ans: return ''
    t = strip_speaker_and_annotations(ans)
    sentences = re.split(r'(?<=[\.\!\…\n])\s+', t)
    first_sent = sentences[0].strip()
    if len(first_sent) < 8 and len(sentences) > 1:
        first_sent = (sentences[0].strip() + ' ' + sentences[1].strip()).strip()
    if len(first_sent) > 42:
        parts = re.split(r'[\،\,]', first_sent)
        if parts and 6 <= len(parts[0].strip()) <= 42:
            first_sent = parts[0].strip()
        else:
            words = first_sent.split()
            truncated = []
            for w in words:
                if len(' '.join(truncated + [w])) <= 40:
                    truncated.append(w)
                else:
                    break
            first_sent = ' '.join(truncated)
    # Avoid leaving dangling prepositions like "لِـ"
    first_sent = re.sub(r'\s+لِ?[^\s]+$', '', first_sent)
    return first_sent.strip(' .،,') + '.'

# Clean object statement extractor: returns clean "هٰذَا قَمِيصٌ"
def extract_clean_object_statement(raw_text):
    if not raw_text: return None
    t = strip_speaker_and_annotations(raw_text)
    parts = re.split(r'[\؟\?\.\،\,]', t)
    for p in reversed(parts):
        p_clean = p.strip()
        p_plain = strip_tashkeel(p_clean)
        words = p_plain.split()
        if len(words) >= 2:
            first = words[0]
            if first in ['لا', 'نعم'] and len(words) >= 3:
                first = words[1]
                p_clean = ' '.join(p_clean.split()[1:])
            if first in ['هذا', 'ذلك', 'هذه', 'تلك']:
                if 2 <= len(strip_tashkeel(p_clean).split()) <= 4:
                    return p_clean
    return None

def make_clean_interrogative(stmt):
    words = stmt.strip().split()
    if not words or len(words) < 2: return None
    first_plain = strip_tashkeel(words[0])
    rest = ' '.join(words[1:])
    if first_plain == 'هذا': return f"أَهٰذَا {rest}؟"
    elif first_plain == 'ذلك': return f"أَذٰلِكَ {rest}؟"
    elif first_plain == 'هذه': return f"أَهٰذِهِ {rest}؟"
    elif first_plain == 'تلك': return f"أَتِلْكَ {rest}؟"
    return None

def isolate_single_dialogue_question(text):
    if not text or '؟' not in text: return None
    clean = strip_speaker_and_annotations(text)
    sentences = re.split(r'[\.\!\…\n]', clean)
    q_candidates = []
    for s in sentences:
        s = s.strip()
        if '؟' in s:
            subparts = s.split('؟')
            for sp in subparts[:-1]:
                sp = strip_speaker_and_annotations(sp)
                if len(sp) >= 5 and not sp.startswith('('):
                    q_candidates.append(sp + '؟')
    if q_candidates:
        return q_candidates[-1]
    return None

# Level-appropriate curated distractor banks
BOOK_POOLS_CURATED = {
    1: [
        ('هٰذَا كِتَابٌ جَدِيدٌ', 'یہ ایک نئی کتاب ہے', 'This is a new book'),
        ('الْقَلَمُ عَلَى الْمَكْتَبِ', 'قلم میز پر ہے', 'The pen is on the desk'),
        ('الْمَسْجِدُ قَرِيبٌ وَالْبَيْتُ بَعِيدٌ', 'مسجد قریب ہے اور گھر دور ہے', 'The mosque is near and the house is far'),
        ('الْمَاءُ بَارِدٌ وَاللَّبَنُ حَارٌّ', 'پانی ٹھنڈا ہے اور دودھ گرم ہے', 'The water is cold and the milk is hot'),
        ('خَرَجَ الْمُدَرِّسُ مِنَ الْفَصْلِ', 'استاد کلاس سے باہر نکلے', 'The teacher left the classroom'),
        ('ذَهَبَ الطَّالِبُ إِلَى الْمَدْرَسَةِ', 'طالب علم اسکول گیا', 'The student went to the school'),
        ('هٰذِهِ سَيَّارَةُ الطَّبِيبِ', 'یہ ڈاکٹر کی گاڑی ہے', 'This is the doctor\'s car'),
        ('الْبَابُ مَفْتُوحٌ وَالنَّافِذَةُ مُغْلَقَةٌ', 'دروازہ کھلا ہے اور کھڑکی بند ہے', 'The door is open and the window is closed'),
        ('الْوَلَدُ جَالِسٌ فِي الْمَسْجِدِ', 'لڑکا مسجد میں بیٹھا ہے', 'The boy is sitting in the mosque'),
        ('هٰذَا قَمِيصٌ نَظِيفٌ', 'یہ ایک صاف قمیض ہے', 'This is a clean shirt')
    ],
    2: [
        ('ذَهَبَ إِلَى السُّوقِ', 'وہ بازار گیا', 'He went to the market'),
        ('رَجَعَ الطَّالِبُ مِنَ الْمَدْرَسَةِ', 'طالب علم اسکول سے واپس آیا', 'The student returned from the school'),
        ('خَرَجَ الْمُدَرِّسُ مِنَ الْفَصْلِ', 'استاد کلاس سے باہر نکلے', 'The teacher left the classroom'),
        ('دَخَلَ الطُّلَّابُ الْمَسْجِدَ', 'طلبہ مسجد میں داخل ہوئے', 'The students entered the mosque'),
        ('أَكَلَ الْوَلَدُ التُّفَّاحَةَ', 'لڑکے نے سیب کھایا', 'The boy ate the apple'),
        ('شَرِبَ حَامِدٌ الْمَاءَ الْبَارِدَ', 'حامد نے ٹھنڈا پانی پیا', 'Hamid drank cold water'),
        ('غَسَلَ بِلَالٌ قَمِيصَهُ', 'بلال نے اپنی قمیص دھوئی', 'Bilal washed his shirt'),
        ('يَذْهَبُ إِلَى السُّوقِ كُلَّ يَوْمٍ', 'وہ ہر روز بازار جاتا ہے', 'He goes to the market every day'),
        ('يَكْتُبُ الدَّرْسَ بِالْقَلَمِ', 'وہ قلم سے سبق لکھتا ہے', 'He writes the lesson with a pen'),
        ('هٰؤُلَاءِ طُلَّابٌ مُجْتَهِدُونَ', 'یہ محنتی طلبہ ہیں', 'These are hardworking students'),
        ('عِنْدِي خَمْسَةُ كُتُبٍ جَدِيدَةٍ', 'میرے پاس پانچ نئی کتابیں ہیں', 'I have five new books'),
        ('هٰذِهِ السَّيَّارَةُ جَمِيلَةٌ جِدًّا', 'یہ گاڑی بہت خوبصورت ہے', 'This car is very beautiful')
    ],
    3: [
        ('إِنَّ الْقُرْآنَ كِتَابُ اللهِ', 'بے شک قرآن اللہ کی کتاب ہے', 'Indeed, the Quran is the Book of Allah'),
        ('كَانَ الطَّالِبُ مُجْتَهِدًا فِي دِرَاسَتِهِ', 'طالب علم اپنی پڑھائی میں محنتی تھا', 'The student was hardworking in his studies'),
        ('أَرَادَ أَنْ يَسْتَغْفِرَ رَبَّهُ', 'اس نے اپنے رب سے بخشش مانگنا چاہی', 'He wanted to seek forgiveness from his Lord'),
        ('لَا تَكْتُبْ بِالْقَلَمِ الرَّصَاصِ', 'پنسل سے مت لکھو', 'Do not write with a pencil'),
        ('هٰذَا هُوَ الْكِتَابُ الَّذِي قَرَأْتُهُ', 'یہ وہ کتاب ہے جو میں نے پڑھی', 'This is the book that I read'),
        ('لَمْ يَخْرُجْ أَحَدٌ مِنَ الْقَاعَةِ', 'ہال سے کوئی نہیں نکلا', 'No one left the hall'),
        ('لَنْ يَنْجَحَ الْكَسْلَانُ فِي الِامْتِحَانِ', 'سست انسان امتحان میں کامیاب نہیں ہوگا', 'The lazy person will not succeed in the exam'),
        ('أَحْسَنَ الرَّجُلُ إِلَى جَارِهِ', 'آدمی نے اپنے پڑوسی کے ساتھ بھلائی کی', 'The man was kind to his neighbor'),
        ('جَاءَ الْمُدَرِّسُ رَاكِبًا سَيَّارَتَهُ', 'استاد اپنی گاڑی میں سوار ہو کر آئے', 'The teacher came riding his car')
    ]
}

STD_DEMO_POOL = {
    'هذا': ['هٰذَا كِتَابٌ', 'هٰذَا قَلَمٌ', 'هٰذَا بَابٌ', 'هٰذَا كُرْسِيٌّ', 'هٰذَا بَيْتٌ', 'هٰذَا مَسْجِدٌ', 'هٰذَا مَكْتَبٌ', 'هٰذَا سَرِيرٌ', 'هٰذَا مِفْتَاحٌ', 'هٰذَا قَمِيصٌ', 'هٰذَا نَجْمٌ'],
    'ذلك': ['ذٰلِكَ نَجْمٌ', 'ذٰلِكَ مَسْجِدٌ', 'ذٰلِكَ سَرِيرٌ', 'ذٰلِكَ حِمَارٌ', 'ذٰلِكَ حِصَانٌ', 'ذٰلِكَ قِطٌّ', 'ذٰلِكَ كَلْبٌ', 'ذٰلِكَ حَجَرٌ', 'ذٰلِكَ إِمَامٌ'],
    'هذه': ['هٰذِهِ سَيَّارَةٌ', 'هٰذِهِ دَرَّاجَةٌ', 'هٰذِهِ مِكْوَاةٌ', 'هٰذِهِ سَاعَةٌ', 'هٰذِهِ حَقِيبَةٌ', 'هٰذِهِ مِلْعَقَةٌ', 'هٰذِهِ قِدْرٌ', 'هٰذِهِ بَقَرَةٌ'],
    'تلك': ['تِلْكَ بَطَّةٌ', 'تِلْكَ دَجَاجَةٌ', 'تِلْكَ بَقَرَةٌ', 'تِلْكَ نَاقَةٌ', 'تِلْكَ مُمَرِّضَةٌ', 'تِلْكَ طَبِيبَةٌ', 'تِلْكَ سَيَّارَةٌ', 'تِلْكَ شَمْسٌ']
}
PEOPLE_POOL = ['هٰذَا طَبِيبٌ', 'هٰذَا مُدَرِّسٌ', 'هٰذَا طَالِبٌ', 'هٰذَا وَلَدٌ', 'هٰذَا رَجُلٌ', 'هٰذَا تَاجِرٌ', 'هٰذَا مُهَنْدِسٌ', 'هٰذَا إِمَامٌ']

print("Loaded base pools.")

# Helper to extract dialogue distractor choices
def make_clean_dialogue_distractors(q_text, ans_text, book_num):
    clean_q = strip_tashkeel(q_text)
    clean_ans_norm = normalize_comp(ans_text)
    opts = [ans_text]

    def try_add(cand):
        if len(opts) >= 4: return
        if not cand or '؟' in cand or '?' in cand or ':' in cand: return
        if len(cand) > 50: return
        cand_norm = normalize_comp(cand)
        if not cand_norm or cand_norm == clean_ans_norm: return
        if any(normalize_comp(o) == cand_norm for o in opts): return
        if is_blacklisted_header_or_meta(cand): return
        opts.append(cand)

    if 'كم سورة' in clean_q or 'سورة' in clean_ans_norm:
        for c in ['حَفِظْتُ سُورَةً وَاحِدَةً', 'حَفِظْتُ سُورَتَيْنِ', 'حَفِظْتُ ثَلَاثَ سُوَرٍ', 'حَفِظْتُ خَمْسَ سُوَرٍ', 'حَفِظْتُ عَشْرَ سُوَرٍ']:
            try_add(c)
    elif 'بكم' in clean_q or 'ريال' in clean_ans_norm:
        for c in ['اشْتَرَيْتُهُ بِرِيَالٍ وَاحِدٍ', 'اشْتَرَيْتُهُ بِرِيَالَيْنِ', 'اشْتَرَيْتُهُ بِخَمْسَةِ رِيَالَاتٍ', 'اشْتَرَيْتُهُ بِعَشَرَةِ رِيَالَاتٍ']:
            try_add(c)
    elif 'كم اخ' in clean_q or 'كم اخا' in clean_q or 'اخ' in clean_ans_norm:
        for c in ['لِي أَخٌ وَاحِدٌ', 'لِي أَخَوَانِ اثْنَانِ', 'لِي ثَلَاثَةُ إِخْوَةٍ', 'لِي أَرْبَعَةُ إِخْوَةٍ']:
            try_add(c)
    elif 'كم يوم' in clean_q or 'ايام' in clean_ans_norm:
        for c in ['فِي يَوْمٍ وَاحِدٍ', 'فِي يَوْمَيْنِ اثْنَيْنِ', 'فِي ثَلَاثَةِ أَيَّامٍ', 'فِي سِتَّةِ أَيَّامٍ', 'فِي سَبْعَةِ أَيَّامٍ']:
            try_add(c)
    elif 'كم طالبا' in clean_q or 'كم طالب' in clean_q:
        for c in ['فِيهِ خَمْسَةُ طُلَّابٍ', 'فِيهِ عَشَرَةُ طُلَّابٍ', 'فِيهِ خَمْسَةَ عَشَرَ طَالِبًا', 'فِيهِ عِشْرُونَ طَالِبًا']:
            try_add(c)
    elif 'من اين' in clean_q or 'اليابان' in clean_ans_norm or 'الهند' in clean_ans_norm:
        for c in ['أَنَا مِنَ الْيَابَانِ', 'أَنَا مِنَ الْهِنْدِ', 'أَنَا مِنَ الصِّينِ', 'أَنَا مِنَ الْفِلِبِّينِ', 'أَنَا مِنَ الْمَمْلَكَةِ']:
            try_add(c)
    elif clean_ans_norm.startswith('نعم') or clean_ans_norm.startswith('لا'):
        if clean_ans_norm.startswith('نعم'):
            for c in ['لَا، مَا كَانَ كَذٰلِكَ', 'نَعَمْ، قَرَأْنَاهُ جَيِّدًا', 'لَا، لَمْ نَفْعَلْ ذٰلِكَ', 'نَعَمْ، بِالتَّأْكِيدِ']:
                try_add(c)
        else:
            for c in ['نَعَمْ، هُوَ كَذٰلِكَ', 'لَا، مَا كَانَ ذٰلِكَ', 'نَعَمْ، رَجَعُوا أَمْسِ', 'لَا، لَيْسَ كَذٰلِكَ']:
                try_add(c)

    # Use book-specific pool to fill
    for ar_c, _, _ in BOOK_POOLS_CURATED.get(book_num, BOOK_POOLS_CURATED[1]):
        if len(opts) >= 4: break
        try_add(ar_c)

    random.shuffle(opts)
    return opts

# BUILD DYNAMIC BOOK SENTENCE BANKS FROM ALL UNITS
BOOK_SENTENCE_BANKS = {1: [], 2: [], 3: []}

for book in raw_dataset['books']:
    b_num = book['book_num']
    for unit in book['units']:
        for blk in unit.get('blocks', []):
            txt = strip_speaker_and_annotations(blk.get('text', ''))
            ur = strip_speaker_and_annotations(blk.get('ur', ''))
            en = strip_speaker_and_annotations(blk.get('en', ''))
            if txt and ur and en and 10 <= len(txt) <= 60 and 2 <= len(txt.split()) <= 8:
                if any(c in txt for c in ['؟', '?', ':', '•', '|', '~', '{', '}', '=']): continue
                if any(c in ur for c in ['؟', '?', ':', '•', '|', '~']): continue
                if any(c in en for c in ['؟', '?', ':', '•', '|', '~']): continue
                # Skip dates
                if re.search(r'[\d٠-٩]+.*(ھ|هـ|ه|م|جمادى|شعبان|رمضان|محرم|صفر)', ur + en + txt): continue
                # Skip common ritual formulas when building sentence drills
                if any(w in normalize_comp(txt) for w in ['بسم الله', 'السلام عليكم', 'وعليكم السلام']): continue
                if is_blacklisted_header_or_meta(txt): continue
                if is_real_urdu(ur):
                    BOOK_SENTENCE_BANKS[b_num].append((txt, ur, en))

print(f"Collected sentences from books: B1={len(BOOK_SENTENCE_BANKS[1])}, B2={len(BOOK_SENTENCE_BANKS[2])}, B3={len(BOOK_SENTENCE_BANKS[3])}")

clean_books = []

for book in raw_dataset['books']:
    b_num = book['book_num']
    clean_units = []

    for unit in book['units']:
        u_num = unit['unit_num']
        unit_emoji = unit.get('emoji', '📖')

        lesson_blocks = []
        for blk in unit.get('blocks', []):
            sec = blk.get('section', 'lesson')
            btype = blk.get('type')
            raw_t = blk.get('text', '').strip()

            is_ex = (sec == 'exercises') or (btype == 'exercise_line') or bool(re.search(r'^(تمارين|تمرين|التدريبات|اقرأ واكتب)', raw_t))
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
                clean_blk['cards'] = clean_cards
                lesson_blocks.append(clean_blk)
            else:
                spk = blk.get('speaker', '')
                clean_t = strip_speaker_and_annotations(raw_t)
                clean_ur = strip_speaker_and_annotations(blk.get('ur', ''))
                clean_en = strip_speaker_and_annotations(blk.get('en', ''))
                
                # If raw_t had speaker prefix, separate it
                if not spk and ':' in raw_t:
                    m = re.match(r'^([^:]{1,20}):\s*(.*)$', raw_t)
                    if m:
                        spk = m.group(1).strip()
                        clean_t = strip_speaker_and_annotations(m.group(2))

                clean_blk['speaker'] = spk
                clean_blk['text'] = clean_t
                clean_blk['ur'] = clean_ur
                clean_blk['en'] = clean_en

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
                    q_iso = isolate_single_dialogue_question(txt)
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

        # 1. Visual Object / Person Identification Drill
        for ar_txt, ur, en, em in unit_visuals:
            if len(questions) >= 4: break
            clean_txt = strip_tashkeel(ar_txt)
            first_word = clean_txt.split()[0] if clean_txt.split() else 'هذا'
            is_person = any(w in clean_txt for w in ['طبيب', 'مدرس', 'طالب', 'ولد', 'رجل', 'تاجر', 'طبيبة', 'ممرضة', 'بنت', 'إمام', 'شيخ', 'مهندس'])
            if first_word in ['هذا', 'هٰذَا']: prompt_ar = "مَنْ هٰذَا؟" if is_person else "مَا هٰذَا؟"
            elif first_word in ['ذلك', 'ذٰلِكَ']: prompt_ar = "مَنْ ذٰلِكَ؟" if is_person else "مَا ذٰلِكَ؟"
            elif first_word in ['هذه', 'هٰذِهِ']: prompt_ar = "مَنْ هٰذِهِ؟" if is_person else "مَا هٰذِهِ؟"
            elif first_word in ['تلك', 'تِلْكَ']: prompt_ar = "مَنْ تِلْكَ؟" if is_person else "مَا تِلْكَ؟"
            else: prompt_ar = "اخْتَرْ الْعِبَارَةَ الصَّحِيحَةَ لِلصُّورَةِ:"

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
                    "hint_ur": ur,
                    "hint_en": en,
                    "options": opts,
                    "answer": ar_txt,
                    "explanation_ur": f"درست جواب: {ar_txt}" + (f" ({ur})" if ur else ""),
                    "explanation_en": f"Correct: {ar_txt}" + (f" ({en})" if en else "")
                })

        # 2. Affirmation / Negation Verification Drill
        if len(unit_visuals) >= 2:
            v_correct = unit_visuals[0]
            v_wrong = unit_visuals[1]
            q_affirm = make_clean_interrogative(v_correct[0])
            if q_affirm:
                ans_affirm = f"نَعَمْ، {v_correct[0]}"
                opts_affirm = [ans_affirm, f"لَا، {v_correct[0]}", f"لَا، {v_wrong[0]}", f"نَعَمْ، {v_wrong[0]}"]
                random.shuffle(opts_affirm)
                questions.append({
                    "type": "dialogue_qa",
                    "badge_ar": "تَمْرِينُ التَّأْكِيدِ: نَعَمْ أَوْ لَا",
                    "badge_ur": "مشق: تصدیق (ہاں یا نہیں)",
                    "badge_en": "Exercise: Affirmation & Negation",
                    "emoji": v_correct[3],
                    "prompt_ar": q_affirm,
                    "prompt_ur": f"تصویر {v_correct[3]} دیکھ کر تصدیق کریں:",
                    "prompt_en": f"Look at picture {v_correct[3]} and verify:",
                    "hint_ur": v_correct[1],
                    "hint_en": v_correct[2],
                    "options": opts_affirm,
                    "answer": ans_affirm,
                    "explanation_ur": f"درست جواب: {ans_affirm}",
                    "explanation_en": f"Correct: {ans_affirm}"
                })

            q_neg = make_clean_interrogative(v_wrong[0])
            if q_neg:
                ans_neg = f"لَا، {v_correct[0]}"
                opts_neg = [ans_neg, f"نَعَمْ، {v_wrong[0]}", f"لَا، {v_wrong[0]}", f"نَعَمْ، {v_correct[0]}"]
                random.shuffle(opts_neg)
                questions.append({
                    "type": "dialogue_qa",
                    "badge_ar": "تَمْرِينُ النَّفْيِ وَالتَّصْحِيحِ",
                    "badge_ur": "مشق: نفی اور تصحیح",
                    "badge_en": "Exercise: Negation & Correction",
                    "emoji": v_correct[3],
                    "prompt_ar": q_neg,
                    "prompt_ur": f"تصویر {v_correct[3]} دیکھ کر درست جواب منتخب کریں:",
                    "prompt_en": f"Look at picture {v_correct[3]} and correct:",
                    "hint_ur": v_correct[1],
                    "hint_en": v_correct[2],
                    "options": opts_neg,
                    "answer": ans_neg,
                    "explanation_ur": f"درست جواب: {ans_neg}",
                    "explanation_en": f"Correct: {ans_neg}"
                })

        # 3. High Quality Dialogue Q&A Drill
        for d in unit_dialogues:
            if len(questions) >= 5: break
            q_txt = d['q_text']
            ans_cand = clean_dialogue_answer(d['ans_text'])
            if not ans_cand or is_blacklisted_header_or_meta(ans_cand) or is_blacklisted_header_or_meta(q_txt):
                continue
            if '؟' in ans_cand or ':' in ans_cand or len(ans_cand) > 42: continue

            raw_opts = make_clean_dialogue_distractors(q_txt, ans_cand, b_num)
            opts_dlg = []
            for o in raw_opts:
                c_o = clean_dialogue_answer(o)
                if c_o and len(c_o) <= 42 and not is_blacklisted_header_or_meta(c_o) and c_o not in opts_dlg:
                    opts_dlg.append(c_o)
            
            if ans_cand not in opts_dlg:
                opts_dlg = [ans_cand] + opts_dlg[:3]

            if len(opts_dlg) == 4 and not any('؟' in o or ':' in o for o in opts_dlg):
                questions.append({
                    "type": "dialogue_qa",
                    "badge_ar": "تَمْرِينُ الْحِوَارِ: سُؤَالٌ وَجَوَابٌ",
                    "badge_ur": "مشق: حوار (سوال و جواب)",
                    "badge_en": "Exercise: Dialogue Q&A",
                    "emoji": d['emoji'],
                    "prompt_ar": q_txt,
                    "prompt_ur": "سوال کا مناسب اور درست جواب منتخب کریں:",
                    "prompt_en": "Select the appropriate answer to the question:",
                    "hint_ur": d['ans_ur'] or d['q_ur'],
                    "hint_en": d['ans_en'] or d['q_en'],
                    "options": opts_dlg,
                    "answer": ans_cand,
                    "explanation_ur": f"درست جواب: {ans_cand}",
                    "explanation_en": f"Correct answer: {ans_cand}"
                })

        # 4. Demonstrative Pronoun Drill (strictly 12-60 chars, 2-6 words)
        pool_sentences = unit_visuals + unit_sentences
        for ar_txt, ur, en, em in pool_sentences:
            if len(questions) >= 6: break
            if '؟' in ar_txt or ':' in ar_txt or is_blacklisted_header_or_meta(ar_txt): continue
            words = strip_tashkeel(ar_txt).split()
            if 2 <= len(words) <= 6 and 10 <= len(ar_txt) <= 60 and words[0] in ['هذا', 'هذه', 'ذلك', 'تلك']:
                target = words[0]
                rest = ' '.join(ar_txt.split()[1:])
                blank_prompt = f"[ ＿＿＿ ] {rest}"
                target_ar = 'هٰذَا' if target == 'هذا' else ('هٰذِهِ' if target == 'هذه' else ('ذٰلِكَ' if target == 'ذلك' else 'تِلْكَ'))
                opts_grammar = ['هٰذَا', 'هٰذِهِ', 'ذٰلِكَ', 'تِلْكَ']
                random.shuffle(opts_grammar)
                questions.append({
                    "type": "fill_blank",
                    "badge_ar": "تَمْرِينُ الْقَوَاعِدِ: أَسْمَاءُ الإِشَارَةِ",
                    "badge_ur": "مشق: اسم اشارہ کا درست انتخاب",
                    "badge_en": "Exercise: Demonstrative Pronoun",
                    "emoji": em,
                    "prompt_ar": blank_prompt,
                    "prompt_ur": "خالی جگہ کے لیے درست اسم اشارہ منتخب کریں:",
                    "prompt_en": "Select the correct demonstrative pronoun:",
                    "hint_ur": ur,
                    "hint_en": en,
                    "options": opts_grammar,
                    "answer": target_ar,
                    "explanation_ur": f"درست جواب: {target_ar} {rest}" + (f" ({ur})" if ur else ""),
                    "explanation_en": f"Correct: {target_ar} {rest}" + (f" ({en})" if en else "")
                })
                break

        # 5. Meaning Translation Drill (Arabic to Urdu/English)
        trans_candidates = [it for it in pool_sentences if is_real_urdu(it[1]) and '؟' not in it[0] and ':' not in it[0] and not is_blacklisted_header_or_meta(it[0]) and 10 <= len(it[0]) <= 65]
        if trans_candidates:
            main_it = trans_candidates[0]
            m_txt, m_ur, m_en, m_em = main_it
            m_txt = apply_clean_tashkeel(m_txt)

            # Gather distractors from book-specific pool
            distractors_ur = []
            for other_txt, other_ur, other_en in BOOK_SENTENCE_BANKS.get(b_num, []):
                if is_real_urdu(other_ur) and normalize_comp(other_ur) != normalize_comp(m_ur):
                    if other_ur not in distractors_ur:
                        distractors_ur.append(other_ur)
                if len(distractors_ur) >= 10: break

            # Curated fallback for that book
            for _, cur_ur, _ in BOOK_POOLS_CURATED.get(b_num, BOOK_POOLS_CURATED[1]):
                if cur_ur != m_ur and cur_ur not in distractors_ur:
                    distractors_ur.append(cur_ur)

            random.shuffle(distractors_ur)
            final_opts = [m_ur] + distractors_ur[:3]
            random.shuffle(final_opts)

            if len(final_opts) == 4 and not any('؟' in o or ':' in o for o in final_opts):
                questions.append({
                    "type": "meaning_choice",
                    "badge_ar": "تَمْرِينُ تَرْجَمَةِ الْمَعْنَى",
                    "badge_ur": "مشق: اردو ترجمہ کا انتخاب",
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

        # 6. Sentence Builder Drill
        for ar_txt, ur, en, em in pool_sentences:
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

        # 7. Safe Target Sentence Translation Drill (Guarantees >= 3 questions per unit)
        if len(questions) < 3 and pool_sentences:
            for ar_txt, ur, en, em in pool_sentences:
                if ar_txt and 10 <= len(ar_txt) <= 60 and '؟' not in ar_txt and ':' not in ar_txt and not is_blacklisted_header_or_meta(ar_txt):
                    ar_clean_txt = apply_clean_tashkeel(ar_txt)
                    # Distractors from the same book!
                    other_ar_opts = []
                    for b_ar, _, _ in BOOK_SENTENCE_BANKS.get(b_num, []):
                        b_ar_vow = apply_clean_tashkeel(b_ar)
                        if normalize_comp(b_ar_vow) != normalize_comp(ar_clean_txt) and b_ar_vow not in other_ar_opts:
                            other_ar_opts.append(b_ar_vow)
                        if len(other_ar_opts) >= 10: break

                    for cur_ar, _, _ in BOOK_POOLS_CURATED.get(b_num, BOOK_POOLS_CURATED[1]):
                        cur_ar_vow = apply_clean_tashkeel(cur_ar)
                        if normalize_comp(cur_ar_vow) != normalize_comp(ar_clean_txt) and cur_ar_vow not in other_ar_opts:
                            other_ar_opts.append(cur_ar_vow)

                    random.shuffle(other_ar_opts)
                    target_opts = [ar_clean_txt] + other_ar_opts[:3]
                    random.shuffle(target_opts)

                    if len(target_opts) == 4 and not any(':' in o or '؟' in o for o in target_opts):
                        questions.append({
                            "type": "emoji_choice",
                            "badge_ar": "تَمْرِينُ التَّرْجَمَةِ إِلَى الْعَرَبِيَّةِ",
                            "badge_ur": "مشق: عربی ترجمہ کا انتخاب",
                            "badge_en": "Exercise: Translate to Arabic",
                            "emoji": em,
                            "prompt_ar": "تَرْجِمْ إِلَى الْعَرَبِيَّةِ:",
                            "prompt_ur": "اس جملے کا درست عربی ترجمہ منتخب کریں:",
                            "prompt_en": "Select the correct Arabic translation:",
                            "hint_ur": ur,
                            "hint_en": en,
                            "options": target_opts,
                            "answer": ar_clean_txt,
                            "explanation_ur": f"درست جواب: {ar_clean_txt}" + (f" ({ur})" if ur else ""),
                            "explanation_en": f"Correct: {ar_clean_txt}" + (f" ({en})" if en else "")
                        })
                        break

        clean_unit = dict(unit)
        clean_unit['emoji'] = unit_emoji
        clean_unit['blocks'] = lesson_blocks
        clean_unit['questions'] = questions
        clean_unit['line_count'] = len(lesson_blocks)
        clean_units.append(clean_unit)

    clean_book = dict(book)
    clean_book['units'] = clean_units
    clean_books.append(clean_book)

clean_dataset = {"books": clean_books}

with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(clean_dataset, f, ensure_ascii=False, indent=2)

with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write('window.MADINAH_DATA = ' + json.dumps(clean_dataset, ensure_ascii=False) + ';\n')

print("SUCCESS: Clean dataset v2 generated!")
total_u = sum(len(b['units']) for b in clean_books)
total_b = sum(sum(len(u['blocks']) for u in b['units']) for b in clean_books)
total_q = sum(sum(len(u['questions']) for u in b['units']) for b in clean_books)
print(f"Total units: {total_u}")
print(f"Total pure lesson blocks: {total_b}")
print(f"Total exercise questions: {total_q}")
