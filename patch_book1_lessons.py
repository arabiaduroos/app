# patch_book1_lessons.py
import json, re

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
b1 = data['books'][0]

# ==========================================
# 1. FIX LESSON 1: Complete "مَنْ هٰذَا؟" section
# ==========================================
u1 = b1['units'][0]

clean_u1_blocks = [
    {
        "type": "text",
        "section": "lesson",
        "text": "هٰـــذَا",
        "ur": "یہ",
        "en": "This",
        "emoji": "👉"
    },
    {
        "type": "emoji_grid",
        "section": "lesson",
        "cards": [
            {"emoji": "🏠", "text": "هٰذَا بَيْتٌ", "ur": "یہ ایک گھر ہے", "en": "This is a house"},
            {"emoji": "🕌", "text": "هٰذَا مَسْجِدٌ", "ur": "یہ ایک مسجد ہے", "en": "This is a mosque"},
            {"emoji": "🚪", "text": "هٰذَا بَابٌ", "ur": "یہ ایک دروازہ ہے", "en": "This is a door"},
            {"emoji": "📖", "text": "هٰذَا كِتَابٌ", "ur": "یہ ایک کتاب ہے", "en": "This is a book"},
            {"emoji": "🖊️", "text": "هٰذَا قَلَمٌ", "ur": "یہ ایک قلم ہے", "en": "This is a pen"},
            {"emoji": "🔑", "text": "هٰذَا مِفْتَاحٌ", "ur": "یہ ایک چابی ہے", "en": "This is a key"},
            {"emoji": "🪑", "text": "هٰذَا مَكْتَبٌ", "ur": "یہ ایک میز ہے", "en": "This is a desk"},
            {"emoji": "🛏️", "text": "هٰذَا سَرِيرٌ", "ur": "یہ ایک بستر ہے", "en": "This is a bed"},
            {"emoji": "🪑", "text": "هٰذَا كُرْسِيٌّ", "ur": "یہ ایک کرسی ہے", "en": "This is a chair"}
        ]
    },
    {
        "type": "section_header",
        "section": "lesson",
        "text": "مَا هٰـــذَا؟",
        "ur": "یہ کیا ہے؟",
        "en": "What is this?",
        "emoji": "❓"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَا هٰذَا؟ هٰذَا بَيْتٌ.",
        "ur": "یہ کیا ہے؟ یہ ایک گھر ہے۔",
        "en": "What is this? This is a house.",
        "emoji": "🏠"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "أَهٰذَا بَيْتٌ؟ نَعَمْ، هٰذَا بَيْتٌ.",
        "ur": "کیا یہ گھر ہے؟ جی ہاں، یہ ایک گھر ہے۔",
        "en": "Is this a house? Yes, this is a house.",
        "emoji": "🏠"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَا هٰذَا؟ هٰذَا قَمِيصٌ.",
        "ur": "یہ کیا ہے؟ یہ ایک قمیض ہے۔",
        "en": "What is this? This is a shirt.",
        "emoji": "👕"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "أَهٰذَا سَرِيرٌ؟ لَا، هٰذَا كُرْسِيٌّ.",
        "ur": "کیا یہ بستر ہے؟ نہیں، یہ کرسی ہے۔",
        "en": "Is this a bed? No, this is a chair.",
        "emoji": "🪑"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "أَهٰذَا مِفْتَاحٌ؟ لَا، هٰذَا قَلَمٌ.",
        "ur": "کیا یہ چابی ہے؟ نہیں، یہ قلم ہے۔",
        "en": "Is this a key? No, this is a pen.",
        "emoji": "🖊️"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَا هٰذَا؟ هٰذَا نَجْمٌ.",
        "ur": "یہ کیا ہے؟ یہ ایک ستارہ ہے۔",
        "en": "What is this? This is a star.",
        "emoji": "⭐"
    },
    # --- PART 2: مَنْ هٰذَا؟ (THE MISSING SECTION!) ---
    {
        "type": "section_header",
        "section": "lesson",
        "text": "مَنْ هٰـــذَا؟",
        "ur": "یہ کون ہے؟",
        "en": "Who is this?",
        "emoji": "👥"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَنْ هٰذَا؟ هٰذَا طَبِيبٌ.",
        "ur": "یہ کون ہے؟ یہ ایک ڈاکٹر ہے۔",
        "en": "Who is this? This is a doctor.",
        "emoji": "👨‍⚕️"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَنْ هٰذَا؟ هٰذَا وَلَدٌ.",
        "ur": "یہ کون ہے؟ یہ ایک لڑکا ہے۔",
        "en": "Who is this? This is a boy.",
        "emoji": "👦"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَنْ هٰذَا؟ هٰذَا طَالِبٌ.",
        "ur": "یہ کون ہے؟ یہ ایک طالب علم ہے۔",
        "en": "Who is this? This is a student.",
        "emoji": "👨‍🎓"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "أَهٰذَا وَلَدٌ؟ لَا، هٰذَا رَجُلٌ.",
        "ur": "کیا یہ لڑکا ہے؟ نہیں، یہ ایک آدمی ہے۔",
        "en": "Is this a boy? No, this is a man.",
        "emoji": "🧔"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَا هٰذَا؟ هٰذَا مَسْجِدٌ.",
        "ur": "یہ کیا ہے؟ یہ ایک مسجد ہے۔",
        "en": "What is this? This is a mosque.",
        "emoji": "🕌"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَنْ هٰذَا؟ هٰذَا تَاجِرٌ.",
        "ur": "یہ کون ہے؟ یہ ایک تاجر ہے۔",
        "en": "Who is this? This is a merchant.",
        "emoji": "👳"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "هٰذَا كَلْبٌ. أَهٰذَا كَلْبٌ؟ لَا، هٰذَا قِطٌّ.",
        "ur": "یہ کتا ہے۔ کیا یہ کتا ہے؟ نہیں، یہ ایک بلی ہے۔",
        "en": "This is a dog. Is this a dog? No, this is a cat.",
        "emoji": "🐈"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "هٰذَا حِمَارٌ. أَهٰذَا حِمَارٌ؟ لَا، هٰذَا حِصَانٌ.",
        "ur": "یہ گدھا ہے۔ کیا یہ گدھا ہے؟ نہیں، یہ ایک گھوڑا ہے۔",
        "en": "This is a donkey. Is this a donkey? No, this is a horse.",
        "emoji": "🐎"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "وَمَا ذٰلِكَ؟ ذٰلِكَ جَمَلٌ.",
        "ur": "اور وہ کیا ہے؟ وہ ایک اونٹ ہے۔",
        "en": "And what is that? That is a camel.",
        "emoji": "🐪"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَا هٰذَا؟ هٰذَا دِيكٌ.",
        "ur": "یہ کیا ہے؟ یہ ایک مرغا ہے۔",
        "en": "What is this? This is a rooster.",
        "emoji": "🐓"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَنْ هٰذَا؟ هٰذَا مُدَرِّسٌ.",
        "ur": "یہ کون ہے؟ یہ ایک استاد ہے۔",
        "en": "Who is this? This is a teacher.",
        "emoji": "🧑‍🏫"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "أَهٰذَا قَمِيصٌ؟ لَا، هٰذَا مِنْدِيلٌ.",
        "ur": "کیا یہ قمیض ہے؟ نہیں، یہ ایک رومال ہے۔",
        "en": "Is this a shirt? No, this is a handkerchief.",
        "emoji": "🧣"
    }
]

u1['blocks'] = clean_u1_blocks

# ==========================================
# 2. FIX LESSON 2: Near/Far Visuals & Kalimat Jadida
# ==========================================
u2 = b1['units'][1]
clean_u2_blocks = [
    {
        "type": "text",
        "section": "lesson",
        "text": "ذٰلِـــكَ",
        "ur": "وہ (دور کے لیے)",
        "en": "That (for distant objects)",
        "emoji": "👉"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَا ذٰلِكَ؟ ذٰلِكَ نَجْمٌ .",
        "ur": "وہ کیا ہے؟ وہ ایک ستارہ ہے۔",
        "en": "What is that? That is a star.",
        "emoji": "⭐"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "هٰذَا مَسْجِدٌ وَذٰلِكَ بَيْتٌ .",
        "ur": "یہ مسجد ہے اور وہ گھر ہے۔",
        "en": "This is a mosque and that is a house.",
        "emoji": "🕌",
        "near_emoji": "🕌",
        "far_emoji": "🏠"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "هٰذَا حِصَانٌ وَذٰلِكَ حِمَارٌ .",
        "ur": "یہ گھوڑا ہے اور وہ گدھا ہے۔",
        "en": "This is a horse and that is a donkey.",
        "emoji": "🐎",
        "near_emoji": "🐎",
        "far_emoji": "🐴"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "أَذٰلِكَ كَلْبٌ؟ لَا، ذٰلِكَ قِطٌّ .",
        "ur": "کیا وہ کتا ہے؟ نہیں، وہ ایک بلی ہے۔",
        "en": "Is that a dog? No, that is a cat.",
        "emoji": "🐈"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَا ذٰلِكَ؟ ذٰلِكَ سَرِيرٌ .",
        "ur": "وہ کیا ہے؟ وہ ایک بستر ہے۔",
        "en": "What is that? That is a bed.",
        "emoji": "🛏️"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَنْ هٰذَا وَمَنْ ذٰلِكَ؟ هٰذَا مُدَرِّسٌ وَذٰلِكَ إِمَامٌ .",
        "ur": "یہ کون ہے اور وہ کون ہے؟ یہ استاد ہے اور وہ امام ہے۔",
        "en": "Who is this and who is that? This is a teacher and that is an Imam.",
        "emoji": "🧑‍🏫",
        "near_emoji": "🧑‍🏫",
        "far_emoji": "👳"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "مَا ذٰلِكَ؟ ذٰلِكَ حَجَرٌ .",
        "ur": "وہ کیا ہے؟ وہ ایک پتھر ہے۔",
        "en": "What is that? That is a stone.",
        "emoji": "🪨"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "هٰذَا سُكَّرٌ وَذٰلِكَ لَبَنٌ .",
        "ur": "یہ چینی ہے اور وہ دودھ ہے۔",
        "en": "This is sugar and that is milk.",
        "emoji": "🍬",
        "near_emoji": "🍬",
        "far_emoji": "🥛"
    },
    {
        "type": "vocab_table",
        "section": "lesson",
        "title_ar": "الْكَلِمَاتُ الْجَدِيدَةُ",
        "title_ur": "نئے الفاظ",
        "title_en": "New Vocabulary",
        "words": [
            {"ar": "إِمَامٌ", "ur": "امام", "en": "Imam"},
            {"ar": "حَجَرٌ", "ur": "پتھر", "en": "Stone"},
            {"ar": "سُكَّرٌ", "ur": "چینی", "en": "Sugar"},
            {"ar": "لَبَنٌ", "ur": "دودھ", "en": "Milk"}
        ]
    }
]
u2['blocks'] = clean_u2_blocks

# ==========================================
# 3. FIX LESSON 3: Proper Grammatical Pairs, Separated Numbered Sentences, and Vocab Tables
# ==========================================
u3 = b1['units'][2]

clean_u3_blocks = [
    {
        "type": "grammar_pairs",
        "section": "lesson",
        "text": "بَيْتٌ ➔ الْبَيْتُ • قَلَمٌ ➔ الْقَلَمُ • كِتَابٌ ➔ الْكِتَابُ • جَمَلٌ ➔ الْجَمَلُ",
        "ur": "بَيْتٌ (کوئی گھر) ➔ الْبَيْتُ (خاص گھر) • قَلَمٌ (کوئی قلم) ➔ الْقَلَمُ (خاص قلم) • كِتَابٌ (کوئی کتاب) ➔ الْكِتَابُ (خاص کتاب) • جَمَلٌ (کوئی اونٹ) ➔ الْجَمَلُ (خاص اونٹ)",
        "en": "A house ➔ The house • A pen ➔ The pen • A book ➔ The book • A camel ➔ The camel",
        "emoji": "⚖️",
        "pairs": [
            {"indef": "بَيْتٌ", "def": "الْبَيْتُ", "ur_indef": "ایک گھر", "ur_def": "خاص گھر", "en_indef": "A house", "en_def": "The house"},
            {"indef": "قَلَمٌ", "def": "الْقَلَمُ", "ur_indef": "ایک قلم", "ur_def": "خاص قلم", "en_indef": "A pen", "en_def": "The pen"},
            {"indef": "كِتَابٌ", "def": "الْكِتَابُ", "ur_indef": "ایک کتاب", "ur_def": "خاص کتاب", "en_indef": "A book", "en_def": "The book"},
            {"indef": "جَمَلٌ", "def": "الْجَمَلُ", "ur_indef": "ایک اونٹ", "ur_def": "خاص اونٹ", "en_indef": "A camel", "en_def": "The camel"}
        ]
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "الْقَلَمُ مَكْسُورٌ .",
        "ur": "قلم ٹوٹا ہوا ہے۔",
        "en": "The pen is broken.",
        "emoji": "🖊️"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "الْبَابُ مَفْتُوحٌ .",
        "ur": "دروازہ کھلا ہے۔",
        "en": "The door is open.",
        "emoji": "🚪"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "الْوَلَدُ جَالِسٌ وَالْمُدَرِّسُ وَاقِفٌ .",
        "ur": "لڑکا بیٹھا ہے اور استاد کھڑے ہیں۔",
        "en": "The boy is sitting and the teacher is standing.",
        "emoji": "👦",
        "near_emoji": "👦",
        "far_emoji": "🧑‍🏫"
    },
    # SEPARATED NUMBERED SENTENCES (EACH ON ITS OWN CARD!)
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(1) الْكِتَابُ جَدِيدٌ وَالْقَلَمُ قَدِيمٌ .",
        "ur": "(۱) کتاب نئی ہے اور قلم پرانا ہے۔",
        "en": "(1) The book is new and the pen is old.",
        "emoji": "📚"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(2) الْحِمَارُ صَغِيرٌ وَالْحِصَانُ كَبِيرٌ .",
        "ur": "(۲) گدھا چھوٹا ہے اور گھوڑا بڑا ہے۔",
        "en": "(2) The donkey is small and the horse is big.",
        "emoji": "🐴",
        "near_emoji": "🐴",
        "far_emoji": "🐎"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(3) الْكُرْسِيُّ مَكْسُورٌ .",
        "ur": "(۳) کرسی ٹوٹی ہوئی ہے۔",
        "en": "(3) The chair is broken.",
        "emoji": "🪑"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(4) الْمِنْدِيلُ وَسِخٌ .",
        "ur": "(۴) رومال میلا ہے۔",
        "en": "(4) The handkerchief is dirty.",
        "emoji": "🧣"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(5) الْمَاءُ بَارِدٌ .",
        "ur": "(۵) پانی ٹھنڈا ہے۔",
        "en": "(5) The water is cold.",
        "emoji": "💧"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(6) الْقَمَرُ جَمِيلٌ .",
        "ur": "(۶) چاند خوبصورت ہے۔",
        "en": "(6) The moon is beautiful.",
        "emoji": "🌙"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(7) الْبَيْتُ قَرِيبٌ وَالْمَسْجِدُ بَعِيدٌ .",
        "ur": "(۷) گھر قریب ہے اور مسجد دور ہے۔",
        "en": "(7) The house is near and the mosque is far.",
        "emoji": "🏠",
        "near_emoji": "🏠",
        "far_emoji": "🕌"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(8) الْحَجَرُ ثَقِيلٌ وَالْوَرَقُ خَفِيفٌ .",
        "ur": "(۸) پتھر بھاری ہے اور کاغذ ہلکا ہے۔",
        "en": "(8) The stone is heavy and the paper is light.",
        "emoji": "🪨"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(9) اللَّبَنُ حَارٌّ .",
        "ur": "(۹) دودھ گرم ہے۔",
        "en": "(9) The milk is hot.",
        "emoji": "🥛"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(10) الْقَمِيصُ نَظِيفٌ .",
        "ur": "(۱۰) قمیض صاف ہے۔",
        "en": "(10) The shirt is clean.",
        "emoji": "👕"
    },
    # KALIMATUL JADIDA TABLE 1 (MAX 16 WORDS PER CARD!)
    {
        "type": "vocab_table",
        "section": "lesson",
        "title_ar": "الْكَلِمَاتُ الْجَدِيدَةُ",
        "title_ur": "نئے الفاظ (۱ سے ۱۶)",
        "title_en": "New Vocabulary (1 to 16)",
        "words": [
            {"ar": "الْقَمَرُ", "ur": "چاند", "en": "The moon"},
            {"ar": "جَدِيدٌ", "ur": "نیا", "en": "New"},
            {"ar": "قَدِيمٌ", "ur": "پرانا", "en": "Old"},
            {"ar": "وَسِخٌ", "ur": "میلا / گندا", "en": "Dirty"},
            {"ar": "نَظِيفٌ", "ur": "صاف", "en": "Clean"},
            {"ar": "حَارٌّ", "ur": "گرم", "en": "Hot"},
            {"ar": "بَارِدٌ", "ur": "ٹھنڈا", "en": "Cold"},
            {"ar": "صَغِيرٌ", "ur": "چھوٹا", "en": "Small"},
            {"ar": "كَبِيرٌ", "ur": "بڑا", "en": "Big"},
            {"ar": "مَفْتُوحٌ", "ur": "کھلا", "en": "Open"},
            {"ar": "مَكْسُورٌ", "ur": "ٹوٹا ہوا", "en": "Broken"},
            {"ar": "ثَقِيلٌ", "ur": "بھاری", "en": "Heavy"},
            {"ar": "خَفِيفٌ", "ur": "ہلکا", "en": "Light"},
            {"ar": "جَمِيلٌ", "ur": "خوبصورت", "en": "Beautiful"},
            {"ar": "وَاقِفٌ", "ur": "کھڑا", "en": "Standing"},
            {"ar": "جَالِسٌ", "ur": "بیٹھا", "en": "Sitting"}
        ]
    },
    # PART 2: النَّجْمُ ... (الحروف الشمسية والقمرية)
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(1) النَّجْمُ بَعِيدٌ .",
        "ur": "(۱) ستارہ دور ہے۔",
        "en": "(1) The star is far.",
        "emoji": "⭐"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(2) الرَّجُلُ وَاقِفٌ .",
        "ur": "(۲) آدمی کھڑا ہے۔",
        "en": "(2) The man is standing.",
        "emoji": "🧍"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(3) السُّكَّرُ حُلْوٌ .",
        "ur": "(۳) چینی میٹھی ہے۔",
        "en": "(3) The sugar is sweet.",
        "emoji": "🍬"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(4) الطَّالِبُ مَرِيضٌ .",
        "ur": "(۴) طالب علم بیمار ہے۔",
        "en": "(4) The student is sick.",
        "emoji": "🤒"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(5) الدِّيكُ جَمِيلٌ .",
        "ur": "(۵) مرغا خوبصورت ہے۔",
        "en": "(5) The rooster is beautiful.",
        "emoji": "🐓"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(6) الدَّفْتَرُ جَدِيدٌ .",
        "ur": "(۶) کاپی نئی ہے۔",
        "en": "(6) The notebook is new.",
        "emoji": "📓"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(7) التَّاجِرُ غَنِيٌّ .",
        "ur": "(۷) تاجر مالدار ہے۔",
        "en": "(7) The merchant is rich.",
        "emoji": "💰"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(8) الدُّكَّانُ مَفْتُوحٌ .",
        "ur": "(۸) دکان کھلی ہے۔",
        "en": "(8) The shop is open.",
        "emoji": "🏪"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(9) الْوَلَدُ فَقِيرٌ .",
        "ur": "(۹) لڑکا غریب ہے۔",
        "en": "(9) The boy is poor.",
        "emoji": "👦"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(10) التُّفَّاحُ لَذِيذٌ .",
        "ur": "(۱۰) سیب لذیذ ہے۔",
        "en": "(10) The apple is delicious.",
        "emoji": "🍎"
    },
    {
        "type": "illustrated_line",
        "section": "lesson",
        "text": "(11) الطَّبِيبُ طَوِيلٌ وَالْمَرِيضُ قَصِيرٌ .",
        "ur": "(۱۱) ڈاکٹر لمبا ہے اور مریض چھوٹے قد کا ہے۔",
        "en": "(11) The doctor is tall and the patient is short.",
        "emoji": "👨‍⚕️"
    },
    # KALIMATUL JADIDA TABLE 2 (MAX 16 WORDS PER CARD!)
    {
        "type": "vocab_table",
        "section": "lesson",
        "title_ar": "الْكَلِمَاتُ الْجَدِيدَةُ",
        "title_ur": "نئے الفاظ (۱۷ سے ۲۴)",
        "title_en": "New Vocabulary (17 to 24)",
        "words": [
            {"ar": "حُلْوٌ", "ur": "میٹھا", "en": "Sweet"},
            {"ar": "مَرِيضٌ", "ur": "بیمار", "en": "Sick"},
            {"ar": "الدُّكَّانُ", "ur": "دکان", "en": "The shop"},
            {"ar": "غَنِيٌّ", "ur": "مالدار / امیر", "en": "Rich"},
            {"ar": "طَوِيلٌ", "ur": "لمبا", "en": "Tall"},
            {"ar": "فَقِيرٌ", "ur": "غریب", "en": "Poor"},
            {"ar": "قَصِيرٌ", "ur": "چھوٹے قد کا / پستہ قد", "en": "Short"},
            {"ar": "التُّفَّاحُ", "ur": "سیب", "en": "The apple"}
        ]
    }
]
u3['blocks'] = clean_u3_blocks

with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Book 1 Units 1, 2, and 3 patched with complete lessons, separate numbered cards, and vocab tables!")
