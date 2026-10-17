# -*- coding: utf-8 -*-
"""
Deep Authentic Curriculum for Book 2 Units 6 to 15
Faithfully extracted from Madinah Book 2 lessons and exercises.
"""

def get_b2_units_6_to_15():
    units = {}

    # =========================================================================
    # UNIT 6: إسناد الماضي إلى ضمائر المتكلم والمخاطب والمفعول به
    # =========================================================================
    units[6] = [
        # Tamreen 1: أجب عن الأسئلة الآتية
        {
            "id": "b2_u6_q1", "book": 2, "unit_num": 6, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the following questions:",
            "grammar_goal_ur": "سبق کے مکالمے اور فعل ماضی کا فہم۔", "grammar_goal_en": "Dialogue facts and past tense comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ ذَهَبَ الطُّلَّابُ بَعْدَ الدَّرْسِ؟ [ ＿＿＿ ]",
            "prompt_ur": "طلبہ سبق کے بعد کہاں گئے؟", "prompt_en": "Where did the students go after the lesson?",
            "answer": "ذَهَبُوا إِلَى الْمَلْعَبِ .",
            "options": ["ذَهَبُوا إِلَى الْمَلْعَبِ .", "ذَهَبُوا إِلَى الْمَسْجِدِ .", "ذَهَبُوا إِلَى الْمَكْتَبَةِ .", "ذَهَبُوا إِلَى الْمَهْجَعِ ."],
            "emoji": "⚽", "hint_ur": "وہ کھیل کے میدان کی طرف گئے۔", "hint_en": "They went to the playground.",
            "explanation_ur": "سبق کے مطابق طلبہ کھیل کے میدان کی طرف گئے: 'ذَهَبُوا إِلَى الْمَلْعَبِ .'۔", "explanation_en": "According to the lesson, they went to the playground."
        },
        {
            "id": "b2_u6_q2", "book": 2, "unit_num": 6, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the following questions:",
            "grammar_goal_ur": "مفعول بہ کے جواب کا فہم۔", "grammar_goal_en": "Object comprehension in dialogue.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيَّ سُورَةٍ حَفِظَ فَيْصَلٌ؟ [ ＿＿＿ ]",
            "prompt_ur": "فیصل نے کون سی سورت یاد کی؟", "prompt_en": "Which surah did Faysal memorize?",
            "answer": "حَفِظَ سُورَةَ النَّبَإِ .",
            "options": ["حَفِظَ سُورَةَ النَّبَإِ .", "حَفِظَ سُورَةَ الرَّحْمٰنِ .", "حَفِظَ سُورَةَ الْمُلْكِ .", "حَفِظَ سُورَةَ الْفَجْرِ ."],
            "emoji": "📖", "hint_ur": "اس نے سورۃ النبأ یاد کی۔", "hint_en": "He memorized Surah An-Naba.",
            "explanation_ur": "مکالمے کے مطابق فیصل نے سورۃ النبأ یاد کی: 'حَفِظَ سُورَةَ النَّبَإِ .'۔", "explanation_en": "Correct answer: He memorized Surah An-Naba."
        },
        # Tamreen 2: إسناد الفعل إلى تاء الفاعل
        {
            "id": "b2_u6_q3", "book": 2, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تائے فاعل (تُ / تَ / تِ)", "badge_en": "Exercise (2): Taa al-Fa'il Conjugation",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ الْمَاضِي إِلَى ضَمَائِرِ الْمُتَكَلِّمِ وَالْمُخَاطَبِ:", "tamreen_title_ur": "فعل ماضی کو متکلم اور مخاطب کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating past verb with subject pronouns:",
            "grammar_goal_ur": "ذَهَبْتُ (متکلم) اور ذَهَبْتَ (مخاطب) کا فرق۔", "grammar_goal_en": "Distinguishing Zahabtu (1st person) and Zahabta (2nd person).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] إِلَى السُّوقِ أَمْسِ .",
            "prompt_ur": "ضمیر 'أنا' کے لیے درست فعل ماضی منتخب کریں:", "prompt_en": "Select the correct past verb for pronoun 'Ana':",
            "answer": "ذَهَبْتُ",
            "options": ["ذَهَبْتُ", "ذَهَبْتَ", "ذَهَبَتْ", "ذَهَبُوا"],
            "emoji": "🚶", "hint_ur": "میں کل بازار گیا (ذَهَبْتُ)۔", "hint_en": "I went to the market yesterday (Zahabtu).",
            "explanation_ur": "متکلم مفرد کے لیے تاء پر پیش آتی ہے: ذَهَبْتُ۔", "explanation_en": "First person singular takes dammah on taa: Zahabtu."
        },
        {
            "id": "b2_u6_q4", "book": 2, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مخاطب مذکر (تَ)", "badge_en": "Exercise (2): 2nd Person Masc. Singular",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ الْمَاضِي إِلَى تَاءِ الْمُخَاطَبِ (فَعَلْتَ):", "tamreen_title_ur": "مخاطب مذکر کے لیے تاء مفتوحہ کا استعمال:", "tamreen_title_en": "Using Taa with fathah for masculine addressee:",
            "grammar_goal_ur": "مخاطب کے لیے ذَهَبْتَ کا استعمال۔", "grammar_goal_en": "Using Zahabta for 2nd person singular masculine.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَ[ ＿＿＿ ] الدَّرْسَ الْجَدِيدَ يَا حَامِدُ؟",
            "prompt_ur": "حامد سے پوچھنے کے لیے درست فعل چنیں (کیا تم نے سمجھا؟):", "prompt_en": "Select the verb addressing Hamid (Did you understand?):",
            "answer": "فَهِمْتَ",
            "options": ["فَهِمْتَ", "فَهِمْتُ", "فَهِمْتِ", "فَهِمُوا"],
            "emoji": "💡", "hint_ur": "کیا تم نے نیا سبق سمجھا؟ (أَفَهِمْتَ؟)۔", "hint_en": "Did you understand the new lesson? (A-fahimta?).",
            "explanation_ur": "مذکر مخاطب کے لیے تاء پر زبر آتی ہے: فَهِمْتَ۔", "explanation_en": "Masculine 2nd person takes fathah on taa: Fahimta."
        },
        # Tamreen 4: إسناد الفعل إلى ضمير (نا)
        {
            "id": "b2_u6_q5", "book": 2, "unit_num": 6, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): جمع متکلم (نَا)", "badge_en": "Exercise (4): 1st Person Plural (Naa)",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ إِلَى ضَمِيرِ (نَا):", "tamreen_title_ur": "فعل ماضی کو ضمیر 'نَا' کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating past tense with 'Naa':",
            "grammar_goal_ur": "نَحْنُ لَعِبْنَا / خَرَجْنَا کی ساخت۔", "grammar_goal_en": "Forming 1st person plural past tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَحْنُ [ ＿＿＿ ] كُرَةَ الْقَدَمِ الْيَوْمَ .",
            "prompt_ur": "نحن کے لیے درست فعل منتخب کریں:", "prompt_en": "Select the correct verb for 'Nahnu':",
            "answer": "لَعِبْنَا",
            "options": ["لَعِبْنَا", "لَعِبْتُ", "لَعِبُوا", "لَعِبْنَ"],
            "emoji": "⚽", "hint_ur": "ہم نے آج فٹ بال کھیلا۔", "hint_en": "We played football today.",
            "explanation_ur": "جمع متکلم کے لیے 'نَا' لاحق ہوتی ہے: لَعِبْنَا۔", "explanation_en": "First person plural takes 'naa': La'ibnaa."
        },
        # Tamreen 5: تعيين المفعول به وضبطه
        {
            "id": "b2_u6_q6", "book": 2, "unit_num": 6, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): مفعول بہ کا اعراب", "badge_en": "Exercise (5): Direct Object (Maf'ool Bihi)",
            "tamreen_title_ar": "تَعْيِينُ الْمَفْعُولِ بِهِ وَضَبْطُهُ بِالْفَتْحَةِ:", "tamreen_title_ur": "مفعول بہ کو پہچانیں اور زبر (نصب) دیں:", "tamreen_title_en": "Identifying direct object with accusative fathah:",
            "grammar_goal_ur": "مفعول بہ کا منسوب ہونا۔", "grammar_goal_en": "Accusative case for direct object.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَرَأَ الْوَلَدُ [ ＿＿＿ ] .",
            "prompt_ur": "درست اعراب والا مفعول بہ چنیں:", "prompt_en": "Select the direct object with correct case:",
            "answer": "الْقُرْآنَ",
            "options": ["الْقُرْآنَ", "الْقُرْآنُ", "الْقُرْآنِ", "قُرْآنٌ"],
            "emoji": "📖", "hint_ur": "لڑکے نے قرآن پڑھا (مفعول بہ منسوب بالفتحہ)۔", "hint_en": "The boy read the Quran (Maf'ool Bihi with fathah).",
            "explanation_ur": "مفعول بہ منسوب ہوتا ہے اس لیے 'الْقُرْآنَ' پر فتحہ آئے گی۔", "explanation_en": "Direct object is Mansub with fathah."
        },
        {
            "id": "b2_u6_q7", "book": 2, "unit_num": 6, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): مفعول بہ کی تطبیق", "badge_en": "Exercise (5): Direct Object Application",
            "tamreen_title_ar": "ضَبْطُ الْمَفْعُولِ بِهِ فِي الْجُمْلَةِ الْفِعْلِيَّةِ:", "tamreen_title_ur": "جملہ فعلیہ میں مفعول بہ پر زبر لگانا:", "tamreen_title_en": "Applying fathah to direct object in verbal sentence:",
            "grammar_goal_ur": "شَرِبَ الْوَلَدُ الْمَاءَ کی ساخت۔", "grammar_goal_en": "Recognizing subject vs object case endings.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "شَرِبَ يُوسُفُ [ ＿＿＿ ] .",
            "prompt_ur": "یوسف نے پانی پیا (مفعول بہ منسوب منتخب کریں):", "prompt_en": "Yusuf drank water (select accusative object):",
            "answer": "الْمَاءَ",
            "options": ["الْمَاءَ", "الْمَاءُ", "الْمَاءِ", "مَاءٌ"],
            "emoji": "🥤", "hint_ur": "پانی پیا (الْمَاءَ پر زبر آئے گی)۔", "hint_en": "Drank water (Al-Maa'a takes fathah).",
            "explanation_ur": "مفعول بہ پر فتحہ آتی ہے: شَرِبَ يُوسُفُ الْمَاءَ۔", "explanation_en": "Direct object takes fathah: Al-Maa'a."
        }
    ]

    # =========================================================================
    # UNIT 7: كَانَ وَخَبَرُهَا • الأَعْدَادُ التَّرْتِيبِيَّةُ
    # =========================================================================
    units[7] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u7_q1", "book": 2, "unit_num": 7, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَتَى رَجَعَ أَبُوكَ مِنْ مَكَّةَ يَا عَلِيُّ؟ [ ＿＿＿ ]",
            "prompt_ur": "علی کے والد مکہ سے کب واپس آئے؟", "prompt_en": "When did your father return from Makkah, Ali?",
            "answer": "رَجَعَ قَبْلَ أُسْبُوعٍ .",
            "options": ["رَجَعَ قَبْلَ أُسْبُوعٍ .", "رَجَعَ أَمْسِ .", "رَجَعَ الْيَوْمَ .", "رَجَعَ قَبْلَ شَهْرٍ ."],
            "emoji": "🕋", "hint_ur": "وہ ایک ہفتہ پہلے واپس آئے۔", "hint_en": "He returned a week ago.",
            "explanation_ur": "درست جواب: 'رَجَعَ قَبْلَ أُسْبُوعٍ .'۔", "explanation_en": "Correct answer: 'رَجَعَ قَبْلَ أُسْبُوعٍ .'."
        },
        # Tamreen 2: عمل كان
        {
            "id": "b2_u7_q2", "book": 2, "unit_num": 7, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): عَمَلُ كَانَ", "badge_en": "Exercise (2): Syntax of Kaana",
            "tamreen_title_ar": "أَدْخِلْ (كَانَ) عَلَى الْجُمْلَةِ الاسْمِيَّةِ:", "tamreen_title_ur": "جملہ اسمیہ پر 'كَانَ' داخل کریں:", "tamreen_title_en": "Enter 'Kaana' onto nominal sentence:",
            "grammar_goal_ur": "کان اپنے اسم کو رفع اور خبر کو نصب دیتی ہے۔", "grammar_goal_en": "Kaana keeps subject nominative and makes predicate accusative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمَاءُ بَارِدٌ ➔ كَانَ الْمَاءُ [ ＿＿＿ ] .",
            "prompt_ur": "کان کی خبر کا اعراب منتخب کریں:", "prompt_en": "Select the predicate of Kaana:",
            "answer": "بَارِداً",
            "options": ["بَارِداً", "بَارِدٌ", "بَارِدٍ", "الْبَارِدُ"],
            "emoji": "💧", "hint_ur": "پانی ٹھنڈا تھا (کان کی خبر منسوب ہوتی ہے)۔", "hint_en": "The water was cold (predicate of Kaana is Mansub).",
            "explanation_ur": "کان کی خبر منسوب ہوتی ہے اس لیے 'بَارِداً' درست ہے۔", "explanation_en": "Predicate of Kaana takes fathatan: Baaridan."
        },
        {
            "id": "b2_u7_q3", "book": 2, "unit_num": 7, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): كان مريضاً", "badge_en": "Exercise (2): Kaana with Adjective",
            "tamreen_title_ar": "نَصْبُ خَبَرِ (كَانَ):", "tamreen_title_ur": "کان کی خبر کو فتحہ (زبر) دیں:", "tamreen_title_en": "Applying accusative case to predicate of Kaana:",
            "grammar_goal_ur": "حَامِدٌ مَرِيضٌ -> كَانَ حَامِدٌ مَرِيضاً۔", "grammar_goal_en": "Transforming nominal sentence with Kaana.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "حَامِدٌ مَرِيضٌ ➔ كَانَ حَامِدٌ [ ＿＿＿ ] أَمْسِ .",
            "prompt_ur": "کان داخل ہونے کے بعد 'مريض' کا درست اعراب چنیں:", "prompt_en": "Select the correct form of 'Mared' after Kaana:",
            "answer": "مَرِيضاً",
            "options": ["مَرِيضاً", "مَرِيضٌ", "مَرِيضٍ", "الْمَرِيضَ"],
            "emoji": "🤒", "hint_ur": "حامد کل بیمار تھا (مَرِيضاً)۔", "hint_en": "Hamid was sick yesterday (Maredan).",
            "explanation_ur": "کان کی خبر پر دو زبر آتے ہیں: مَرِيضاً۔", "explanation_en": "Predicate of Kaana is Mansub: Maredan."
        },
        # Tamreen 4: الأعداد الترتيبية
        {
            "id": "b2_u7_q4", "book": 2, "unit_num": 7, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): اعدادِ ترتیبیہ", "badge_en": "Exercise (4): Ordinal Numbers",
            "tamreen_title_ar": "الأَعْدَادُ التَّرْتِيبِيَّةُ (الأَوَّلُ، الثَّانِي، الثَّالِثُ):", "tamreen_title_ur": "ترتیبی گنتی کے الفاظ چنیں:", "tamreen_title_en": "Using Ordinal Numbers:",
            "grammar_goal_ur": "پہلا، دوسرا، تیسرا وغیرہ کے لیے اعداد ترتیبیہ کا استعمال۔", "grammar_goal_en": "Forming ordinal numbers as adjectives.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَرَأْتُ الدَّرْسَ [ ＿＿＿ ] .",
            "prompt_ur": "میں نے پہلا سبق پڑھا:", "prompt_en": "I read the first lesson:",
            "answer": "الْأَوَّلَ",
            "options": ["الْأَوَّلَ", "وَاحِداً", "الْأُولَى", "الأَوَّلُ"],
            "emoji": "🥇", "hint_ur": "پہلا سبق (الدرس الأول)۔", "hint_en": "The first lesson.",
            "explanation_ur": "نعت منسوب ہونے کی وجہ سے 'الْأَوَّلَ' منسوب ہوگا۔", "explanation_en": "Adjective agrees with Mansub object: Al-Awwala."
        },
        {
            "id": "b2_u7_q5", "book": 2, "unit_num": 7, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): عدد ترتیبی للمؤنث", "badge_en": "Exercise (4): Feminine Ordinal Numbers",
            "tamreen_title_ar": "الأَعْدَادُ التَّرْتِيبِيَّةُ لِلْمُؤَنَّثِ (الأُولَى، الثَّانِيَةُ):", "tamreen_title_ur": "مؤنث کے لیے ترتیبی عدد کا استعمال:", "tamreen_title_en": "Feminine ordinal numbers:",
            "grammar_goal_ur": "السَّنَةُ الأُولَى / السَّاعَةُ الثَّانِيَةُ کی ساخت۔", "grammar_goal_en": "Feminine forms of ordinal numbers.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذِهِ هِيَ الْغُرْفَةُ [ ＿＿＿ ] .",
            "prompt_ur": "یہ دوسرا کمرہ ہے (مؤنث عدد ترتیبی چنیں):", "prompt_en": "This is the second room (select feminine ordinal):",
            "answer": "الثَّانِيَةُ",
            "options": ["الثَّانِيَةُ", "الثَّانِي", "اثْنَتَانِ", "اثْنَيْنِ"],
            "emoji": "🚪", "hint_ur": "دوسرا کمرہ (الْغُرْفَةُ الثَّانِيَةُ)۔", "hint_en": "The second room (Al-Ghurfatu ath-Thaaniyah).",
            "explanation_ur": "غرفة مؤنث ہے اس لیے عدد ترتیبی مؤنث آئے گا: الثَّانِيَةُ۔", "explanation_en": "Feminine noun matches feminine ordinal: Ath-Thaaniyah."
        }
    ]

    # =========================================================================
    # UNIT 8: تصريف الماضي مع نون النسوة وضَمائر النصب المتصلة
    # =========================================================================
    units[8] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u8_q1", "book": 2, "unit_num": 8, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "سبق کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَنْ فَتَحَ النَّوَافِذَ يَا فَيْصَلُ؟ [ ＿＿＿ ]",
            "prompt_ur": "کھڑکیاں کس نے کھولیں؟", "prompt_en": "Who opened the windows, Faysal?",
            "answer": "أَنَا فَتَحْتُهَا .",
            "options": ["أَنَا فَتَحْتُهَا .", "عَلِيٌّ فَتَحَهَا .", "الْمُدَرِّسُ فَتَحَهَا .", "مَا فَتَحَهَا أَحَدٌ ."],
            "emoji": "🪟", "hint_ur": "میں نے انہیں کھولا (أنا فتحتُها)۔", "hint_en": "I opened them.",
            "explanation_ur": "درست جواب: 'أَنَا فَتَحْتُهَا .'۔", "explanation_en": "Correct answer: 'أَنَا فَتَحْتُهَا .'."
        },
        # Tamreen 2: إسناد الماضي إلى نون النسوة
        {
            "id": "b2_u8_q2", "book": 2, "unit_num": 8, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جمع مؤنث غائب (نَ)", "badge_en": "Exercise (2): 3rd Person Fem. Plural",
            "tamreen_title_ar": "إِسْنَادُ الْمَاضِي إِلَى نُونِ النِّسْوَةِ (فَعَلْنَ):", "tamreen_title_ur": "ماضی کو نون نسوہ کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating past with Nun an-Niswah:",
            "grammar_goal_ur": "الطَّالِبَاتُ خَرَجْنَ کی ساخت۔", "grammar_goal_en": "Past tense with feminine plural.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْبَنَاتُ [ ＿＿＿ ] مِنَ الْفَصْلِ .",
            "prompt_ur": "بچیوں کے لیے درست فعل منتخب کریں:", "prompt_en": "Select the correct verb for girls:",
            "answer": "خَرَجْنَ",
            "options": ["خَرَجْنَ", "خَرَجُوا", "خَرَجَتْ", "خَرَجْتُنَّ"],
            "emoji": "👧", "hint_ur": "لڑکیاں کلاس سے نکل گئیں (خَرَجْنَ)۔", "hint_en": "The girls left the classroom.",
            "explanation_ur": "جمع مؤنث غائب کے لیے 'نَ' آتی ہے: خَرَجْنَ۔", "explanation_en": "Feminine plural third person takes nun: Kharajna."
        },
        # Tamreen 3: ضمائر النصب المتصلة
        {
            "id": "b2_u8_q3", "book": 2, "unit_num": 8, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): ضمیر مفعول متصل", "badge_en": "Exercise (3): Attached Object Pronouns",
            "tamreen_title_ar": "اتِّصَالُ ضَمَائِرِ النَّصْبِ بِالْفِعْلِ الْمَاضِي:", "tamreen_title_ur": "فعل کے ساتھ ضمیر مفعول جوڑیں:", "tamreen_title_en": "Attaching object pronouns to past verb:",
            "grammar_goal_ur": "رَأَيْتُهُ، رَأَيْتُهَا، رَأَيْتُهُمْ کا استعمال۔", "grammar_goal_en": "Using direct object attached pronouns.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ الْحَيَّةُ؟ أَقَتَلْتَـ[ ＿＿＿ ]؟",
            "prompt_ur": "سانپ مؤنث ہے، اس کے لیے درست ضمیر منتخب کریں:", "prompt_en": "Snake (Hayyah) is feminine, select the pronoun:",
            "answer": "هَا",
            "options": ["هَا", "هُ", "هُمْ", "كَ"],
            "emoji": "🐍", "hint_ur": "کیا تم نے اسے مار ڈالا؟ (أَقَتَلْتَهَا؟)۔", "hint_en": "Did you kill it? (Aqatal-tahaa?).",
            "explanation_ur": "حيّة مؤنث مجازی ہے اس لیے ضمیر 'هَا' آئے گی۔", "explanation_en": "Hayyah is feminine, taking the pronoun -haa."
        },
        {
            "id": "b2_u8_q4", "book": 2, "unit_num": 8, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): ضمیر مفعول للمذكر", "badge_en": "Exercise (3): Masculine Object Pronoun",
            "tamreen_title_ar": "ضَمِيرُ الْغَائِبِ الْمُذَكَّرِ (ـهُ):", "tamreen_title_ur": "مذکر مفرد کے لیے ضمیر مفعول 'ـهُ' کا استعمال:", "tamreen_title_en": "Using masculine singular object pronoun (-hu):",
            "grammar_goal_ur": "رَأَيْتُ حَامِداً -> رَأَيْتُهُ۔", "grammar_goal_en": "Replacing masculine noun with object pronoun -hu.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ كِتَابُكَ الْجَدِيدُ؟ أَرَأَيْتَـ[ ＿＿＿ ]؟",
            "prompt_ur": "کتاب مذکر ہے، اس کے لیے درست ضمیر منتخب کریں:", "prompt_en": "Book is masculine, select the pronoun:",
            "answer": "هُ",
            "options": ["هُ", "هَا", "هُمْ", "كُمَا"],
            "emoji": "📗", "hint_ur": "کیا تم نے اسے دیکھا؟ (أَرَأَيْتَهُ؟)۔", "hint_en": "Did you see it? (A-ra'aytahu?).",
            "explanation_ur": "کتاب مذکر ہے اس لیے ضمیر 'ـهُ' آئے گی: أَرَأَيْتَهُ؟۔", "explanation_en": "Kitaab is masculine, taking pronoun -hu."
        },
        {
            "id": "b2_u8_q5", "book": 2, "unit_num": 8, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): اسمائے اشارہ للبعید", "badge_en": "Exercise (5): Demonstrative Pronouns",
            "tamreen_title_ar": "أَسْمَاءُ الإِشَارَةِ (ذٰلِكَ / تِلْكَ / أُولٰئِكَ):", "tamreen_title_ur": "دور کے اشارے (ذٰلِكَ، تِلْكَ، أُولٰئِكَ):", "tamreen_title_en": "Distant Demonstrative Pronouns:",
            "grammar_goal_ur": "جمع عقلاء کے لیے أُولٰئِكَ کا استعمال۔", "grammar_goal_en": "Using Ulaa'ika for rational plural.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "[ ＿＿＿ ] الطُّلَّابُ إِخْوَتِي .",
            "prompt_ur": "طلبہ جمع ہیں، دور کا درست اسم اشارہ چنیں:", "prompt_en": "Students is plural, select distant demonstrative:",
            "answer": "أُولٰئِكَ",
            "options": ["أُولٰئِكَ", "ذٰلِكَ", "تِلْكَ", "هٰذَا"],
            "emoji": "👥", "hint_ur": "وہ طلبہ میرے بھائی ہیں (أُولٰئِكَ)۔", "hint_en": "Those students are my brothers (Ulaa'ika).",
            "explanation_ur": "جمع عاقل کے لیے 'أُولٰئِكَ' استعمال ہوتا ہے۔", "explanation_en": "Ulaa'ika is used for plural rational beings."
        }
    ]

    # =========================================================================
    # UNIT 9: جمع المؤنث السالم وإعرابه والأعداد من 11 إلى 20
    # =========================================================================
    units[9] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u9_q1", "book": 2, "unit_num": 9, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "سبق کے سوالات۔", "grammar_goal_en": "Lesson comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَمْ طَالِبَةً جَدِيدَةً جَاءَتْ إِلَى الْفَصْلِ؟ [ ＿＿＿ ]",
            "prompt_ur": "کلاس میں کتنی نئی طالبات آئیں؟", "prompt_en": "How many new female students came to the class?",
            "answer": "جَاءَتْ خَمْسُ طَالِبَاتٍ جُدُدٍ .",
            "options": ["جَاءَتْ خَمْسُ طَالِبَاتٍ جُدُدٍ .", "جَاءَتْ ثَلَاثُ طَالِبَاتٍ .", "جَاءَتْ عَشْرُ طَالِبَاتٍ .", "مَا جَاءَتْ أَحَدٌ ."],
            "emoji": "👩‍🎓", "hint_ur": "پانچ نئی طالبات آئیں۔", "hint_en": "Five new students came.",
            "explanation_ur": "درست جواب: 'جَاءَتْ خَمْسُ طَالِبَاتٍ جُدُدٍ .'۔", "explanation_en": "Correct answer: five new students."
        },
        # Tamreen 2: نصب جمع المؤنث السالم بالكسرة
        {
            "id": "b2_u9_q2", "book": 2, "unit_num": 9, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جمع مؤنث کا اعراب بالکسرہ", "badge_en": "Exercise (2): Feminine Plural in Accusative",
            "tamreen_title_ar": "نَصْبُ جَمْعِ الْمُؤَنَّثِ السَّالِمِ بِالْكَسْرَةِ:", "tamreen_title_ur": "حالتِ نصب میں جمع مؤنث سالم کو کسرہ دیں:", "tamreen_title_en": "Sound feminine plural taking kasrah in accusative:",
            "grammar_goal_ur": "جمع مؤنث سالم پر زبر (فتحہ) کبھی نہیں آتی، نصب میں بھی کسرہ آتی ہے۔", "grammar_goal_en": "Sound feminine plural never takes fathah; it takes kasrah in accusative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "رَأَيْتُ [ ＿＿＿ ] فِي الْمَسْجِدِ .",
            "prompt_ur": "درست اعراب والا مفعول بہ منتخب کریں:", "prompt_en": "Select the direct object with correct case:",
            "answer": "الْمُسْلِمَاتِ",
            "options": ["الْمُسْلِمَاتِ", "الْمُسْلِمَاتَ", "الْمُسْلِمَاتُ", "مُسْلِمَاتٌ"],
            "emoji": "🧕", "hint_ur": "میں نے مسلمان عورتوں کو دیکھا (جمع مؤنث سالم منسوب بالکسرہ)۔", "hint_en": "I saw Muslim women (sound feminine plural with kasrah).",
            "explanation_ur": "جمع مؤنث سالم حالت نصب میں کسرہ لیتا ہے: الْمُسْلِمَاتِ۔", "explanation_en": "Takes kasrah in accusative case: Al-Muslimaati."
        },
        {
            "id": "b2_u9_q3", "book": 2, "unit_num": 9, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): خلق الله السماوات", "badge_en": "Exercise (2): Quranic Accusative Kasrah",
            "tamreen_title_ar": "إِعْرَابُ (السَّمَاوَاتِ) فِي الْقُرْآنِ الْكَرِيمِ:", "tamreen_title_ur": "قرآن کریم میں جمع مؤنث سالم کا اعراب:", "tamreen_title_en": "Grammar of As-Samawati in the Quran:",
            "grammar_goal_ur": "خَلَقَ اللهُ السَّمَاوَاتِ میں کسرہ کا فہم۔", "grammar_goal_en": "Recognizing kasrah as accusative marker for feminine sound plural.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "{ خَلَقَ اللَّهُ [ ＿＿＿ ] وَالأَرْضَ } .",
            "prompt_ur": "درست قرآنی اعراب منتخب کریں:", "prompt_en": "Select the correct Quranic vocalization:",
            "answer": "السَّمَاوَاتِ",
            "options": ["السَّمَاوَاتِ", "السَّمَاوَاتَ", "السَّمَاوَاتُ", "سَمَاوَاتٌ"],
            "emoji": "🌌", "hint_ur": "اللہ نے آسمانوں کو پیدا فرمایا (مفعول بہ منسوب بالکسرہ)۔", "hint_en": "Allah created the heavens (Maf'ool Bihi with kasrah).",
            "explanation_ur": "جمع مؤنث سالم حالت نصب میں کسرہ لیتا ہے: السَّمَاوَاتِ۔", "explanation_en": "Sound feminine plural takes kasrah in accusative: As-Samaawaati."
        },
        # Tamreen 4: الأعداد من 11 إلى 20 مع المعدود المؤنث
        {
            "id": "b2_u9_q4", "book": 2, "unit_num": 9, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): اعدادِ مرکبہ (11 تا 19)", "badge_en": "Exercise (4): Compound Numbers (11-19)",
            "tamreen_title_ar": "عَدَدُ الْمَعْدُودِ الْمُؤَنَّثِ مِنَ (11 إِلَى 19):", "tamreen_title_ur": "مؤنث چیزوں کے لیے 11 تا 19 گنتی:", "tamreen_title_en": "Counting feminine nouns from 11 to 19:",
            "grammar_goal_ur": "إِحْدَى عَشْرَةَ طَالِبَةً اور ثَلَاثَ عَشْرَةَ طَالِبَةً کی ساخت۔", "grammar_goal_en": "Forming compound numbers with feminine counted nouns.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي الْفَصْلِ [ ＿＿＿ ] طَالِبَةً .",
            "prompt_ur": "کلاس میں گیارہ طالبات ہیں (درست عدد چنیں):", "prompt_en": "In the class there are 11 female students:",
            "answer": "إِحْدَى عَشْرَةَ",
            "options": ["إِحْدَى عَشْرَةَ", "أَحَدَ عَشَرَ", "وَاحِدَةَ عَشْرَةَ", "إِحْدَى عَشَرَ"],
            "emoji": "1️⃣1️⃣", "hint_ur": "گیارہ طالبات (إِحْدَى عَشْرَةَ طَالِبَةً)۔", "hint_en": "Eleven female students (Ihda 'ashrata).",
            "explanation_ur": "مؤنث معدود کے لیے دونوں جز مؤنث اور مبنی بر فتحہ ہوتے ہیں: إِحْدَى عَشْرَةَ۔", "explanation_en": "Both parts agree with feminine noun: Ihdaa 'ashrata."
        },
        {
            "id": "b2_u9_q5", "book": 2, "unit_num": 9, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): عدد (15) للمؤنث", "badge_en": "Exercise (4): Number 15 Feminine",
            "tamreen_title_ar": "مُخَالَفَةُ الْجُزْءِ الأَوَّلِ فِي الأَعْدَادِ (13-19):", "tamreen_title_ur": "13 تا 19 میں پہلے جز کی مخالفت:", "tamreen_title_en": "Opposition of first digit in numbers 13-19:",
            "grammar_goal_ur": "خَمْسَ عَشْرَةَ طَالِبَةً میں خَمْسَ مذکر اور عَشْرَةَ مؤنث۔", "grammar_goal_en": "First part opposes gender, second part matches.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدِي [ ＿＿＿ ] مَجَلَّةً .",
            "prompt_ur": "میرے پاس پندرہ رسائل ہیں (درست عدد منتخب کریں):", "prompt_en": "I have 15 magazines (select correct number):",
            "answer": "خَمْسَ عَشْرَةَ",
            "options": ["خَمْسَ عَشْرَةَ", "خَمْسَةَ عَشَرَ", "خَمْسَةَ عَشْرَةَ", "خَمْسُ عَشْرٍ"],
            "emoji": "📰", "hint_ur": "مجلة مؤنث ہے اس لیے پہلا حصہ مذکر اور دوسرا مؤنث ہوگا: خَمْسَ عَشْرَةَ۔", "hint_en": "Majallah is feminine, so first part is masculine: Khamsa 'Ashrata.",
            "explanation_ur": "درست ترکیب: خَمْسَ عَشْرَةَ مَجَلَّةً۔", "explanation_en": "Correct form: Khamsa 'ashrata majallatan."
        }
    ]

    # =========================================================================
    # UNIT 10: الفعل المضارع وصياغته وحروف المضارعة
    # =========================================================================
    units[10] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u10_q1", "book": 2, "unit_num": 10, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "فعل مضارع کے ابتدائی جملوں کا فہم۔", "grammar_goal_en": "Present tense comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "إِلَى أَيْنَ يَذْهَبُ عَمَّارٌ كُلَّ يَوْمٍ؟ [ ＿＿＿ ]",
            "prompt_ur": "عمار روزانہ کہاں جاتا ہے؟", "prompt_en": "Where does Ammar go every day?",
            "answer": "يَذْهَبُ إِلَى الْمَصْنَعِ .",
            "options": ["يَذْهَبُ إِلَى الْمَصْنَعِ .", "يَذْهَبُ إِلَى الْمَسْجِدِ .", "يَذْهَبُ إِلَى الْجَامِعَةِ .", "يَذْهَبُ إِلَى السُّوقِ ."],
            "emoji": "🏭", "hint_ur": "وہ فیکٹری جاتا ہے۔", "hint_en": "He goes to the factory.",
            "explanation_ur": "درست جواب: 'يَذْهَبُ إِلَى الْمَصْنَعِ .'۔", "explanation_en": "Correct answer: goes to the factory."
        },
        # Tamreen 2: حروف المضارعة
        {
            "id": "b2_u10_q2", "book": 2, "unit_num": 10, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مضارع کے حروف (أَنَيْتُ)", "badge_en": "Exercise (2): Present Tense Prefixes",
            "tamreen_title_ar": "حُرُوفُ الْمُضَارَعَةِ (الْهَمْزَةُ، النُّونُ، الْيَاءُ، التَّاءُ):", "tamreen_title_ur": "مضارع کے شروع کے حروف کی پہچان:", "tamreen_title_en": "Prefixes of Present Tense:",
            "grammar_goal_ur": "أَذْهَبُ، نَذْهَبُ، يَذْهَبُ، تَذْهَبُ کی پہچان۔", "grammar_goal_en": "Recognizing present tense prefixes.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] الدَّرْسَ الآنَ .",
            "prompt_ur": "أنا کے لیے درست فعلِ مضارع منتخب کریں:", "prompt_en": "Select the correct present verb for 'Ana':",
            "answer": "أَفْهَمُ",
            "options": ["أَفْهَمُ", "يَفْهَمُ", "تَفْهَمُ", "نَفْهَمُ"],
            "emoji": "💡", "hint_ur": "میں اب سبق سمجھ رہا ہوں (أَفْهَمُ)۔", "hint_en": "I understand the lesson now.",
            "explanation_ur": "متکلم مفرد کے لیے ہمزہ آتی ہے: أَفْهَمُ۔", "explanation_en": "First person singular takes hamzah prefix: Afhamu."
        },
        {
            "id": "b2_u10_q3", "book": 2, "unit_num": 10, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): نون مضارعت (نَ)", "badge_en": "Exercise (2): Present Prefix 'Nun' for We",
            "tamreen_title_ar": "حَرْفُ النُّونِ لِلْجَمْعِ الْمُتَكَلِّمِ (نَفْعَلُ):", "tamreen_title_ur": "جمع متکلم کے لیے مضارع کا صیغہ:", "tamreen_title_en": "Present tense prefix Nun for 'We':",
            "grammar_goal_ur": "نَحْنُ نَلْعَبُ / نَذْهَبُ کی پہچان۔", "grammar_goal_en": "Forming 1st person plural present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَحْنُ [ ＿＿＿ ] الْقُرْآنَ كُلَّ صَبَاحٍ .",
            "prompt_ur": "ہم ہر صبح قرآن پڑھتے ہیں (نحن کے ساتھ درست فعل چنیں):", "prompt_en": "We read the Quran every morning (select verb for Nahnu):",
            "answer": "نَقْرَأُ",
            "options": ["نَقْرَأُ", "يَقْرَأُ", "أَقْرَأُ", "تَقْرَأُ"],
            "emoji": "📖", "hint_ur": "ہم پڑھتے ہیں (نَقْرَأُ)۔", "hint_en": "We read (Naqra'u).",
            "explanation_ur": "جمع متکلم کے لیے نون کا لاحقہ آتا ہے: نَقْرَأُ۔", "explanation_en": "1st person plural takes nun: Naqra'u."
        },
        # Tamreen 3: تصريف المضارع مع هو وهي
        {
            "id": "b2_u10_q4", "book": 2, "unit_num": 10, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): غائب مؤنث (تَفْعَلُ)", "badge_en": "Exercise (3): 3rd Person Fem. Present",
            "tamreen_title_ar": "الْفِعْلُ الْمُضَارِعُ لِلْمُؤَنَّثِ الْغَائِبِ (تَفْعَلُ):", "tamreen_title_ur": "مؤنث غائب کے لیے تاء مضارعت:", "tamreen_title_en": "Present tense with Taa for 3rd person fem singular:",
            "grammar_goal_ur": "آمِنَةُ تَغْسِلُ الثِّيَابَ کی ساخت۔", "grammar_goal_en": "Subject-verb agreement for feminine present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أُمِّي [ ＿＿＿ ] الطَّعَامَ فِي الْمَطْبَخِ .",
            "prompt_ur": "امی کھانا پکا رہی ہیں (امی کے لیے درست فعل چنیں):", "prompt_en": "Mother is cooking food in kitchen (select verb):",
            "answer": "تَطْبُخُ",
            "options": ["تَطْبُخُ", "يَطْبُخُ", "أَطْبُخُ", "نَطْبُخُ"],
            "emoji": "🍳", "hint_ur": "مؤنث غائب کے لیے 'تَطْبُخُ' آئے گا۔", "hint_en": "Feminine takes taa: Tatbukhu.",
            "explanation_ur": "امی مؤنث ہیں اس لیے مضارع تاء کے ساتھ آئے گا: تَطْبُخُ۔", "explanation_en": "Mother is feminine, verb takes taa: Tatbukhu."
        },
        {
            "id": "b2_u10_q5", "book": 2, "unit_num": 10, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): مضارع مرفوع بالضمة", "badge_en": "Exercise (4): Present Verb Nominative",
            "tamreen_title_ar": "إِعْرَابُ الْفِعْلِ الْمُضَارِعِ الْمَرْفُوعِ بِالضَّمَّةِ:", "tamreen_title_ur": "مضارع کا ضمہ (پیش) کے ساتھ مرفوع ہونا:", "tamreen_title_en": "Present verb is nominative with dammah:",
            "grammar_goal_ur": "مضارع پر جب ناصب یا جازم نہ ہو تو وہ مرفوع بالضمہ ہوتا ہے۔", "grammar_goal_en": "Default present tense is Marfoo' with dammah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَشْرَبُ حَامِدٌ [ ＿＿＿ ] .",
            "prompt_ur": "حامد چائے پیتا ہے (مفعول بہ منسوب چنیں):", "prompt_en": "Hamid drinks tea (select accusative object):",
            "answer": "الشَّايَ",
            "options": ["الشَّايَ", "الشَّايُ", "الشَّايِ", "شَايٌ"],
            "emoji": "🍵", "hint_ur": "چائے پیتا ہے (مفعول بہ منسوب بالفتحہ)۔", "hint_en": "Drinks tea (Ash-Shaaya with fathah).",
            "explanation_ur": "مفعول بہ منسوب ہوتا ہے اس لیے 'الشَّايَ' درست ہے۔", "explanation_en": "Direct object is Mansub: Ash-Shaaya."
        }
    ]

    # =========================================================================
    # UNIT 11: إسناد المضارع للغائب وواو الجماعة وسين الاستقبال
    # =========================================================================
    units[11] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u11_q1", "book": 2, "unit_num": 11, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "بِأَيِّ جَامِعَةٍ يَدْرُسُ عَبْدُ اللَّهِ؟ [ ＿＿＿ ]",
            "prompt_ur": "عبد اللہ کس یونیورسٹی میں پڑھتا ہے؟", "prompt_en": "In which university does Abdullah study?",
            "answer": "يَدْرُسُ بِجَامِعَةِ الرِّيَاضِ .",
            "options": ["يَدْرُسُ بِجَامِعَةِ الرِّيَاضِ .", "يَدْرُسُ بِالْجَامِعَةِ الإِسْلَامِيَّةِ .", "يَدْرُسُ بِجَامِعَةِ الْقَاهِرَةِ .", "يَدْرُسُ بِجَامِعَةِ أُمِّ الْقُرَى ."],
            "emoji": "🎓", "hint_ur": "وہ ریاض یونیورسٹی میں پڑھتا ہے۔", "hint_en": "He studies at Riyadh University.",
            "explanation_ur": "درست جواب: 'يَدْرُسُ بِجَامِعَةِ الرِّيَاضِ .'۔", "explanation_en": "Correct answer: Riyadh University."
        },
        # Tamreen 4: إسناد المضارع إلى واو الجماعة
        {
            "id": "b2_u11_q2", "book": 2, "unit_num": 11, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): جمع مذکر میں ثبوتِ نون", "badge_en": "Exercise (4): Plural Present Tense with Nun",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى وَاوِ الْجَمَاعَةِ (يَفْعَلُونَ):", "tamreen_title_ur": "مضارع کو جمع مذکر کے ساتھ جوڑیں (ثبوت نون):", "tamreen_title_en": "Present tense with plural masculine (Yaf'aloona):",
            "grammar_goal_ur": "الطلاب يكتبون میں ثبوتِ نون کا فہم۔", "grammar_goal_en": "Recognizing affirmative nun in plural present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطُّلَّابُ [ ＿＿＿ ] إِلَى الْمَسْجِدِ كُلَّ يَوْمٍ .",
            "prompt_ur": "طلبہ کے لیے درست فعل چنیں:", "prompt_en": "Select the correct verb for students:",
            "answer": "يَذْهَبُونَ",
            "options": ["يَذْهَبُونَ", "يَذْهَبُ", "تَذْهَبُونَ", "يَذْهَبُوا"],
            "emoji": "🕌", "hint_ur": "طلبہ روزانہ مسجد جاتے ہیں (يَذْهَبُونَ)۔", "hint_en": "The students go to the mosque every day.",
            "explanation_ur": "جمع مذکر غائب کے لیے واو و نون کے ساتھ 'يَذْهَبُونَ' آتا ہے۔", "explanation_en": "Plural masculine takes waw and nun: Yazhaboona."
        },
        # Tamreen 8: أنت تذهب وهي تذهب
        {
            "id": "b2_u11_q3", "book": 2, "unit_num": 11, "tamreen_num": 8,
            "badge_ar": "التَّمْرِينُ (8)", "badge_ur": "مشق (8): تَذْهَبُ کے دو معنی", "badge_en": "Exercise (8): Two Meanings of Tazhabu",
            "tamreen_title_ar": "اشْتِرَاكُ صِيغَةِ (تَفْعَلُ) بَيْنَ الْمُخَاطَبِ وَالْغَائِبَةِ:", "tamreen_title_ur": "'تَذْهَبُ' کا أنتَ اور هِيَ دونوں کے لیے آنا:", "tamreen_title_en": "Tazhabu shared by 2nd person masc. and 3rd person fem.:",
            "grammar_goal_ur": "أَنْتَ تَذْهَبُ اور هِيَ تَذْهَبُ کی پہچان۔", "grammar_goal_en": "Understanding shared form of Tazhabu based on context.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ [ ＿＿＿ ] يَا حَامِدُ الآنَ؟",
            "prompt_ur": "حامد سے مخاطب ہو کر پوچھنے کے لیے درست صیغہ چنیں:", "prompt_en": "Select the verb addressing Hamid (Where are you going?):",
            "answer": "تَذْهَبُ",
            "options": ["تَذْهَبُ", "يَذْهَبُ", "أَذْهَبُ", "تَذْهَبِينَ"],
            "emoji": "🚶‍♂️", "hint_ur": "اے حامد، تم اب کہاں جا رہے ہو؟ (تَذْهَبُ)۔", "hint_en": "Where are you going, Hamid? (Tazhabu).",
            "explanation_ur": "مذکر مخاطب کے لیے 'تَذْهَبُ' آتا ہے۔", "explanation_en": "2nd person masculine takes: Tazhabu."
        },
        # Tamreen 11: سين الاستقبال
        {
            "id": "b2_u11_q4", "book": 2, "unit_num": 11, "tamreen_num": 11,
            "badge_ar": "التَّمْرِينُ (11)", "badge_ur": "مشق (11): سِينُ الاسْتِقْبَالِ", "badge_en": "Exercise (11): Future Prefix Seen",
            "tamreen_title_ar": "دُخُولُ (السِّينِ) عَلَى الْمُضَارِعِ لِتَخْصِيصِهِ بِالْمُسْتَقْبَلِ:", "tamreen_title_ur": "مضارع پر 'سین' داخل کر کے مستقبل کے لیے خاص کرنا:", "tamreen_title_en": "Prefixing Seen onto present tense for near future:",
            "grammar_goal_ur": "سَيَرْجِعُ الْمُدِيرُ غَداً کا فہم۔", "grammar_goal_en": "Using Seen prefix for future actions.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "[ ＿＿＿ ] الْمُدِيرُ غَداً إِنْ شَاءَ اللَّهُ .",
            "prompt_ur": "پرنسپل کل واپس آئیں گے (مستقبل کے لیے درست فعل چنیں):", "prompt_en": "The principal will return tomorrow (select future verb):",
            "answer": "سَيَرْجِعُ",
            "options": ["سَيَرْجِعُ", "رَجَعَ", "يَرْجِعُ أَمْسِ", "ارْجِعْ"],
            "emoji": "📅", "hint_ur": "کل واپس آئیں گے (سَيَرْجِعُ)۔", "hint_en": "Will return tomorrow (Sa-yarji'u).",
            "explanation_ur": "مستقبل کے لیے مضارع کے شروع میں سین آتی ہے: سَيَرْجِعُ۔", "explanation_en": "Seen indicates future tense: Sa-yarji'u."
        },
        # Tamreen 14: أَمَّا ... فَـ
        {
            "id": "b2_u11_q5", "book": 2, "unit_num": 11, "tamreen_num": 14,
            "badge_ar": "التَّمْرِينُ (14)", "badge_ur": "مشق (14): أَمَّا ... فَـ", "badge_en": "Exercise (14): Ammaa ... Fa Construction",
            "tamreen_title_ar": "اسْتِعْمَالُ أُسْلُوبِ الشَّرْطِ وَالتَّفْصِيلِ (أَمَّا ... فَـ):", "tamreen_title_ur": "تفصیل اور وضاحت کے لیے 'أَمَّا ... فَـ' کا استعمال:", "tamreen_title_en": "Using Ammaa ... Fa for contrast/detail:",
            "grammar_goal_ur": "أَمَّا الْكِتَابُ فَهُوَ بِعَشَرَةِ رِيَالَاتٍ۔", "grammar_goal_en": "Mastering Ammaa ... Fa conditional structure.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَمَّا الْكِتَابُ [ ＿＿＿ ] بِعَشَرَةِ رِيَالَاتٍ .",
            "prompt_ur": "اما کے بعد جواب میں کون سا حرف آتا ہے؟", "prompt_en": "Which letter introduces the clause after Amma?",
            "answer": "فَهُوَ",
            "options": ["فَهُوَ", "وَهُوَ", "ثُمَّ هُوَ", "بَلْ هُوَ"],
            "emoji": "📖", "hint_ur": "جہاں بھی 'أَمَّا' آئے وہاں جواب میں 'فَـ' لازمی آتی ہے: فَهُوَ۔", "hint_en": "Ammaa requires 'Faa' in its following clause: Fa-huwa.",
            "explanation_ur": "أما کے جواب میں ہمیشہ فاء کا داخل ہونا واجب ہے: فَهُوَ۔", "explanation_en": "Faa is obligatory after Ammaa: Fa-huwa."
        }
    ]

    # =========================================================================
    # UNIT 12: إسناد المضارع لياء المخاطبة وتأكيد إن وأَن
    # =========================================================================
    units[12] = [
        # Tamreen 1: تصحيح أخطاء الدرس
        {
            "id": "b2_u12_q1", "book": 2, "unit_num": 12, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "صَحِّحْ مَا يَلِي حَسَبَ نَصِّ الدَّرْسِ:", "tamreen_title_ur": "سبق کے مطابق جملوں کی تصحیح کریں:", "tamreen_title_en": "Correct statements according to lesson:",
            "grammar_goal_ur": "سبق کے مکالمے کے حقائق۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عَنْ مَاذَا تَبْحَثُ أُمُّ أَحْمَدَ؟ [ ＿＿＿ ]",
            "prompt_ur": "ام احمد کس چیز کی تلاش کر رہی ہیں؟", "prompt_en": "What is Umm Ahmad searching for?",
            "answer": "تَبْحَثُ عَنِ الدَّوَاءِ .",
            "options": ["تَبْحَثُ عَنِ الدَّوَاءِ .", "تَبْحَثُ عَنِ الْمِفْتَاحِ .", "تَبْحَثُ عَنِ الْقَلَمِ .", "تَبْحَثُ عَنِ النَّظَّارَةِ ."],
            "emoji": "💊", "hint_ur": "وہ دوائی تلاش کر رہی ہیں۔", "hint_en": "She is searching for the medicine.",
            "explanation_ur": "درست جواب: 'تَبْحَثُ عَنِ الدَّوَاءِ .'۔", "explanation_en": "Correct answer: searching for medicine."
        },
        # Tamreen 2 & 5: إسناد المضارع لياء المخاطبة (تَفْعَلِينَ)
        {
            "id": "b2_u12_q2", "book": 2, "unit_num": 12, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): إسناد للمخاطبة", "badge_en": "Exercise (5): 2nd Person Feminine Present",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى يَاءِ الْمُخَاطَبَةِ (تَفْعَلِينَ):", "tamreen_title_ur": "مضارع کو واحد مؤنث مخاطب کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating present with 2nd person feminine:",
            "grammar_goal_ur": "أَنْتِ تَذْهَبِينَ اور أَتَعْرِفِينَ کی ساخت۔", "grammar_goal_en": "Forming 2nd person feminine singular present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي أَيِّ سَنَةٍ [ ＿＿＿ ] يَا فَتَاةُ؟",
            "prompt_ur": "لڑکی سے پوچھنے کے لیے درست فعل منتخب کریں:", "prompt_en": "Select the verb addressing a young woman:",
            "answer": "تَدْرُسِينَ",
            "options": ["تَدْرُسِينَ", "تَدْرُسُ", "يَدْرُسُونَ", "تَدْرُسْنَ"],
            "emoji": "👩‍🎓", "hint_ur": "اے لڑکی، تم کس سال میں پڑھتی ہو؟ (تَدْرُسِينَ)۔", "hint_en": "In which year do you study? (Tadruseena).",
            "explanation_ur": "واحد مؤنث مخاطب کے لیے یاء اور نون آتی ہے: تَدْرُسِينَ۔", "explanation_en": "2nd person feminine takes ya and nun: Tadruseena."
        },
        {
            "id": "b2_u12_q3", "book": 2, "unit_num": 12, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): كتابت بالاحمر", "badge_en": "Exercise (5): Fem. Plural Addressing",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ لِجَمْعِ الإِنَاثِ الْمُخَاطَبَاتِ (تَفْعَلْنَ):", "tamreen_title_ur": "بیٹیوں سے مخاطب ہونے کے لیے فعل چنیں:", "tamreen_title_en": "Addressing daughters with feminine plural present verb:",
            "grammar_goal_ur": "لِمَاذَا تَكْتُبْنَ الْوَاجِبَاتِ بِالْقَلَمِ الأَحْمَرِ يَا بَنَاتِي؟", "grammar_goal_en": "Using Tak-tubna for 2nd person feminine plural.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "لِمَاذَا [ ＿＿＿ ] الْوَاجِبَاتِ بِالْقَلَمِ الأَحْمَرِ يَا بَنَاتِي؟",
            "prompt_ur": "اے میری بیٹیو! تم لال قلم سے کیوں لکھتی ہو؟", "prompt_en": "Why do you write homework in red pen, daughters?",
            "answer": "تَكْتُبْنَ",
            "options": ["تَكْتُبْنَ", "تَكْتُبُونَ", "يَكْتُبْنَ", "تَكْتُبِينَ"],
            "emoji": "🖊️", "hint_ur": "جمع مؤنث مخاطب کے لیے 'تَكْتُبْنَ' آتا ہے۔", "hint_en": "Feminine plural takes Tak-tubna.",
            "explanation_ur": "بیٹیوں سے خطاب ہے اس لیے نون نسوہ کے ساتھ 'تَكْتُبْنَ' آئے گا۔", "explanation_en": "2nd person feminine plural takes: Tak-tubna."
        },
        # Tamreen 6: الفرق بين إِنَّ وَأَنَّ
        {
            "id": "b2_u12_q4", "book": 2, "unit_num": 12, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): إِنَّ اور أَنَّ کا فرق", "badge_en": "Exercise (6): Inna vs Anna",
            "tamreen_title_ar": "كَسْرُ هَمْزَةِ (إِنَّ) فِي ابْتِدَاءِ الْكَلاَمِ وَفَتْحُهَا بَعْدَ سَمِعْتُ:", "tamreen_title_ur": "جملے کے شروع میں إِنَّ اور سمعت کے بعد أَنَّ کا استعمال:", "tamreen_title_en": "Kasrah on Inna at sentence start vs fathah after Sami'tu:",
            "grammar_goal_ur": "إِنَّ الْقُرْآنَ كِتَابُ اللهِ / سَمِعْتُ أَنَّهَا أَحْسَنُ طَبِيبَةٍ۔", "grammar_goal_en": "Distinguishing Inna (beginning/after Qaala) and Anna (after verbs of perception).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَمِعْتُ [ ＿＿＿ ] أَحْسَنُ طَبِيبَةٍ فِي الْمُسْتَشْفَى .",
            "prompt_ur": "میں نے سنا ہے کہ وہ بہترین ڈاکٹر ہیں (ان یا أن چنیں):", "prompt_en": "I heard that she is the best doctor (select Inna/Anna):",
            "answer": "أَنَّهَا",
            "options": ["أَنَّهَا", "إِنَّهَا", "أَنْ هَا", "كَأَنَّهَا"],
            "emoji": "👩‍⚕️", "hint_ur": "سَمِعْتُ کے بعد ہمزہ پر زبر آتی ہے: أَنَّهَا۔", "hint_en": "After verbs of knowledge/perception, use Anna: Anna-haa.",
            "explanation_ur": "فعل سمعت کے بعد مفتوحہ 'أَنَّ' آتی ہے: سَمِعْتُ أَنَّهَا۔", "explanation_en": "Anna with fathah is used after Sami'tu."
        },
        # Tamreen 7: أيام الأسبوع
        {
            "id": "b2_u12_q5", "book": 2, "unit_num": 12, "tamreen_num": 7,
            "badge_ar": "التَّمْرِينُ (7)", "badge_ur": "مشق (7): ہفتے کے دنوں کے نام", "badge_en": "Exercise (7): Days of the Week",
            "tamreen_title_ar": "أَسْمَاءُ أَيَّامِ الأُسْبُوعِ فِي اللُّغَةِ الْعَرَبِيَّةِ:", "tamreen_title_ur": "عربی میں ہفتے کے دنوں کے نام:", "tamreen_title_en": "Days of the week in Arabic:",
            "grammar_goal_ur": "السبت، الأحد، الإثنين، الثلاثاء، الأربعاء، الخميس، الجمعة۔", "grammar_goal_en": "Recognizing days of the week in Arabic.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَوَّلُ أَيَّامِ الأُسْبُوعِ فِي الْجَدْوَلِ هُوَ يَوْمُ [ ＿＿＿ ] .",
            "prompt_ur": "سبق کے جدول کے مطابق ہفتے کا پہلا دن کون سا ہے؟", "prompt_en": "According to the lesson schedule, what is Saturday in Arabic?",
            "answer": "السَّبْتِ",
            "options": ["السَّبْتِ", "الأَحَدِ", "الْجُمُعَةِ", "الثُّلَاثَاءِ"],
            "emoji": "🗓️", "hint_ur": "ہفتے کا دن (يَوْمُ السَّبْتِ)۔", "hint_en": "Saturday (Yawm as-Sabt).",
            "explanation_ur": "ہفتے کے دن کو عربی میں 'يَوْمُ السَّبْتِ' کہتے ہیں۔", "explanation_en": "Saturday is Yawm as-Sabt."
        }
    ]

    # =========================================================================
    # UNIT 13: إسناد المضارع لجمع المؤنث المخاطب (أَنْتُنَّ تَفْعَلْنَ)
    # =========================================================================
    units[13] = [
        # Tamreen 1: إسناد المضارع لأنتن
        {
            "id": "b2_u13_q1", "book": 2, "unit_num": 13, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): جمع مؤنث مخاطب (تَفْعَلْنَ)", "badge_en": "Exercise (1): 2nd Person Fem. Plural Present",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى نُونِ النِّسْوَةِ لِلْمُخَاطَبَاتِ (تَفْعَلْنَ):", "tamreen_title_ur": "مضارع کو جمع مؤنث مخاطب کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating present with feminine plural (Taf'alna):",
            "grammar_goal_ur": "أَنْتُنَّ تَذْهَبْنَ کی ساخت۔", "grammar_goal_en": "Forming 2nd person feminine plural present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ [ ＿＿＿ ] يَا أَخَوَاتِي فِي الْمَسَاءِ؟",
            "prompt_ur": "بہنوں سے مخاطب ہونے کے لیے درست فعل چنیں:", "prompt_en": "Select the verb addressing sisters:",
            "answer": "تَذْهَبْنَ",
            "options": ["تَذْهَبْنَ", "تَذْهَبُونَ", "يَذْهَبْنَ", "تَذْهَبِينَ"],
            "emoji": "👭", "hint_ur": "اے میری بہنو، تم شام کو کہاں جاتی ہو؟", "hint_en": "Where do you go in the evening, sisters?",
            "explanation_ur": "جمع مؤنث مخاطب کے لیے تاء اور نون نسوہ آتی ہے: تَذْهَبْنَ۔", "explanation_en": "2nd person feminine plural takes taa and nun: Tazhabna."
        },
        # Tamreen 2: إكمال الجمل بفعل مضارع
        {
            "id": "b2_u13_q2", "book": 2, "unit_num": 13, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): سکن اور رہائش", "badge_en": "Exercise (2): Verb Sakana (To Live)",
            "tamreen_title_ar": "اسْتِعْمَالُ الْفِعْلِ (يَسْكُنُ) مَعَ جَمْعِ الإِنَاثِ:", "tamreen_title_ur": "جمع مؤنث کے ساتھ 'تسکنّ' کا استعمال:", "tamreen_title_en": "Using the verb 'to reside' with fem. plural:",
            "grammar_goal_ur": "فِي أَيِّ مَهْجَعٍ تَسْكُنَّ يَا أَخَوَاتُ؟", "grammar_goal_en": "Using Taskunna for feminine plural living.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي أَيِّ مَهْجَعٍ [ ＿＿＿ ] يَا طَالِبَاتُ؟",
            "prompt_ur": "طالبات سے پوچھنے کے لیے درست فعل منتخب کریں:", "prompt_en": "Select the verb asking female students where they live:",
            "answer": "تَسْكُنَّ",
            "options": ["تَسْكُنَّ", "تَسْكُنُونَ", "يَسْكُنَّ", "تَسْكُنِينَ"],
            "emoji": "🏢", "hint_ur": "اے طالبات، تم کس ہاسٹل میں رہتی ہو؟ (تَسْكُنَّ)۔", "hint_en": "In which hostel do you live? (Taskunna).",
            "explanation_ur": "جمع مؤنث مخاطب کے لیے 'تَسْكُنَّ' آتا ہے۔", "explanation_en": "2nd person feminine plural takes: Taskunna."
        },
        # Tamreen 3: تصحيح الجمل
        {
            "id": "b2_u13_q3", "book": 2, "unit_num": 13, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): تصحیح جملے", "badge_en": "Exercise (3): Sentence Correction",
            "tamreen_title_ar": "تَصْحِيحُ إِسْنَادِ الْفِعْلِ إِلَى الْفَاعِلِ الْمُؤَنَّثِ:", "tamreen_title_ur": "مؤنث فاعل کے ساتھ فعل کی درستی:", "tamreen_title_en": "Correcting verb agreement with feminine subjects:",
            "grammar_goal_ur": "الْبَنَاتُ يَذْهَبْنَ نہ کہ يَذْهَبُونَ۔", "grammar_goal_en": "Feminine subjects require feminine verb agreement.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْبَنَاتُ [ ＿＿＿ ] إِلَى الْمَدْرَسَةِ بِالْحَافِلَةِ .",
            "prompt_ur": "لڑکیاں بس کے ذریعے سکول جاتی ہیں (درست فعل چنیں):", "prompt_en": "The girls go to school by bus (select correct verb):",
            "answer": "يَذْهَبْنَ",
            "options": ["يَذْهَبْنَ", "يَذْهَبُونَ", "تَذْهَبُونَ", "يَذْهَبُ"],
            "emoji": "🚌", "hint_ur": "لڑکیاں غائب جمع ہیں اس لیے 'يَذْهَبْنَ' آئے گا۔", "hint_en": "3rd person feminine plural takes Yazhabna.",
            "explanation_ur": "جمع مؤنث غائب کے لیے یاء اور نون نسوہ آتی ہے: يَذْهَبْنَ۔", "explanation_en": "Takes ya and nun an-niswah: Yazhabna."
        },
        # Tamreen 4: زيارة المريض
        {
            "id": "b2_u13_q4", "book": 2, "unit_num": 13, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): عیادت اور زیارت", "badge_en": "Exercise (4): Visiting the Sick",
            "tamreen_title_ar": "صِيَاغَةُ الْفِعْلِ (يَزُورُ) مَعَ الْمُخَاطَبَاتِ:", "tamreen_title_ur": "مؤنث مخاطب کے لیے 'تَزُرْنَ' کا صیغہ:", "tamreen_title_en": "Conjugating 'to visit' with feminine plural:",
            "grammar_goal_ur": "مَتَى تَزُرْنَ مُدِيرَتَكُنَّ يَا أَخَوَاتُ؟", "grammar_goal_en": "Using Tazurna for visiting.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَتَى [ ＿＿＿ ] أُمَّكُنَّ فِي الْمُسْتَشْفَى يَا بَنَاتُ؟",
            "prompt_ur": "بیٹیو، تم اپنی امی کی عیادت کب کرو گی؟", "prompt_en": "When will you visit your mother, daughters?",
            "answer": "تَزُرْنَ",
            "options": ["تَزُرْنَ", "تَزُورُونَ", "يَزُرْنَ", "تَزُورِينَ"],
            "emoji": "🏥", "hint_ur": "تم کب عیادت کرو گی؟ (تَزُرْنَ)۔", "hint_en": "When will you visit? (Tazurna).",
            "explanation_ur": "فعل اجوف نون نسوہ سے ملنے پر واو گرا دیتا ہے: تَزُرْنَ۔", "explanation_en": "Hollow verb drops long vowel with nun an-niswah: Tazurna."
        }
    ]

    # =========================================================================
    # UNIT 14: فعل الأمر وصياغته من المضارع
    # =========================================================================
    units[14] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u14_q1", "book": 2, "unit_num": 14, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "امر کے جملوں کا فہم۔", "grammar_goal_en": "Imperative comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَاذَا قَالَ الْمُدَرِّسُ لِعَلِيٍّ؟ [ ＿＿＿ ]",
            "prompt_ur": "استاد نے علی سے کیا کہا؟", "prompt_en": "What did the teacher say to Ali?",
            "answer": "اقْرَأِ الدَّرْسَ يَا عَلِيُّ .",
            "options": ["اقْرَأِ الدَّرْسَ يَا عَلِيُّ .", "اكْتُبِ الدَّرْسَ .", "اخْرُجْ مِنَ الْفَصْلِ .", "افْتَحِ الْبَابَ ."],
            "emoji": "📖", "hint_ur": "علی، سبق پڑھو (اقْرَأْ)۔", "hint_en": "Read the lesson, Ali.",
            "explanation_ur": "درست جواب: 'اقْرَأِ الدَّرْسَ يَا عَلِيُّ .'۔", "explanation_en": "Correct answer: Read the lesson."
        },
        # Tamreen 4: صياغة فعل الأمر
        {
            "id": "b2_u14_q2", "book": 2, "unit_num": 14, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): صیاغتِ امر مکسور العین", "badge_en": "Exercise (4): Imperative with Kasrah",
            "tamreen_title_ar": "صِيَاغَةُ فِعْلِ الأَمْرِ مِنَ الْمُضَارِعِ:", "tamreen_title_ur": "مضارع سے امر بنانے کا طریقہ:", "tamreen_title_en": "Deriving imperative from present tense:",
            "grammar_goal_ur": "تَجْلِسُ سے اجْلِسْ بنانا۔", "grammar_goal_en": "Forming imperative with hamzatul wasl.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الأَمْرُ مِنْ (تَجْلِسُ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "تجلس کا امر منتخب کریں:", "prompt_en": "Select the imperative of 'Tajlisu':",
            "answer": "اجْلِسْ (بِكَسْرِ الْهَمْزَةِ)",
            "options": ["اجْلِسْ (بِكَسْرِ الْهَمْزَةِ)", "اُجْلُسْ", "جْلِسْ", "تَجْلِسْ"],
            "emoji": "🪑", "hint_ur": "بیٹھو! (اجْلِسْ)۔", "hint_en": "Sit down! (Ijlis).",
            "explanation_ur": "کیونکہ مضارع میں لام مکسور ہے اس لیے ہمزہ پر زیر آئے گی: اجْلِسْ۔", "explanation_en": "Because 'ayn has kasrah, hamzatul wasl takes kasrah: Ijlis."
        },
        {
            "id": "b2_u14_q3", "book": 2, "unit_num": 14, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): امر مضموم العین (اُفْعُلْ)", "badge_en": "Exercise (4): Imperative with Dammah",
            "tamreen_title_ar": "هَمْزَةُ الْوَصْلِ الْمَضْمُومَةُ فِي الأَمْرِ (اكْتُبْ):", "tamreen_title_ur": "امر میں ہمزہ پر پیش (تَكْتُبُ -> اكْتُبْ):", "tamreen_title_en": "Hamzah with dammah in imperative (Tak-tubu -> Uktub):",
            "grammar_goal_ur": "تَدْخُلُ سے ادْخُلْ اور تَكْتُبُ سے اكْتُبْ کی صیاغت۔", "grammar_goal_en": "Forming imperative with dammah on hamzah when middle radical has dammah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الأَمْرُ مِنْ (تَدْخُلُ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "تَدْخُلُ سے امر کا درست صیغہ منتخب کریں:", "prompt_en": "Select the imperative of 'Tad-khulu':",
            "answer": "ادْخُلْ (بِضَمِّ الْهَمْزَةِ)",
            "options": ["ادْخُلْ (بِضَمِّ الْهَمْزَةِ)", "اِدْخَلْ", "دْخُلْ", "تَدْخُلْ"],
            "emoji": "🚪", "hint_ur": "داخل ہو جاؤ! (ادْخُلْ)۔", "hint_en": "Enter! (Ud-khul).",
            "explanation_ur": "کیونکہ مضارع کا عین کلمہ مضموم ہے (تَدْخُلُ) اس لیے ہمزہ مضموم ہوگا: ادْخُلْ۔", "explanation_en": "Middle letter has dammah, so hamzatul wasl takes dammah: Ud-khul."
        },
        # Tamreen 5: فعل الأمر للجمع (افْعَلُوا)
        {
            "id": "b2_u14_q4", "book": 2, "unit_num": 14, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): امر جمع مذکر (افْعَلُوا)", "badge_en": "Exercise (5): Plural Imperative (If'aloo)",
            "tamreen_title_ar": "صِيَاغَةُ الأَمْرِ لِجَمَاعَةِ الذُّكُورِ (احْذِفِ النُّونَ):", "tamreen_title_ur": "جمع مذکر کے لیے امر بنانا (نون گرا کر):", "tamreen_title_en": "Plural imperative formed by dropping nun:",
            "grammar_goal_ur": "تَكْتُبُونَ سے اكْتُبُوا بنانا۔", "grammar_goal_en": "Forming masculine plural imperative by dropping nun.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا أَبْنَائِي، [ ＿＿＿ ] الْوَاجِبَاتِ الآنَ .",
            "prompt_ur": "بیٹو، اب ہوم ورک لکھو (جمع کا امر منتخب کریں):", "prompt_en": "My sons, write homework now (select plural imperative):",
            "answer": "اكْتُبُوا",
            "options": ["اكْتُبُوا", "اكْتُبْ", "تَكْتُبُونَ", "يَكْتُبُوا"],
            "emoji": "📝", "hint_ur": "تم سب لکھو (اكْتُبُوا)۔", "hint_en": "Write (all of you)! (Uk-tuboo).",
            "explanation_ur": "جمع مذکر کے لیے نون گر کر واو الف آتی ہے: اكْتُبُوا۔", "explanation_en": "Plural imperative drops nun and adds alif: Uk-tuboo."
        },
        # Tamreen 6: فعل الأمر للمفردة المؤنثة (افْعَلِي)
        {
            "id": "b2_u14_q5", "book": 2, "unit_num": 14, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): امر مؤنث مخاطب (افْعَلِي)", "badge_en": "Exercise (6): Feminine Imperative (If'alee)",
            "tamreen_title_ar": "صِيَاغَةُ الأَمْرِ لِلْمُفْرَدَةِ الْمُؤَنَّثَةِ (احْذِفِ النُّونَ):", "tamreen_title_ur": "واحد مؤنث کے لیے امر بنانا:", "tamreen_title_en": "Forming feminine singular imperative:",
            "grammar_goal_ur": "تَجْلِسِينَ سے اجْلِسِي اور تَشْرَبِينَ سے اشْرَبِي۔", "grammar_goal_en": "Dropping nun to form feminine singular imperative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا مَرْيَمُ، [ ＿＿＿ ] الْبَابَ .",
            "prompt_ur": "مریم، دروازہ کھولو (مؤنث کے لیے امر چنیں):", "prompt_en": "Maryam, open the door (select fem. imperative):",
            "answer": "افْتَحِي",
            "options": ["افْتَحِي", "افْتَحْ", "تَفْتَحِينَ", "افْتَحُوا"],
            "emoji": "🚪", "hint_ur": "کھولو! (افْتَحِي)۔", "hint_en": "Open! (If-tahee).",
            "explanation_ur": "مؤنث کے لیے یاء کے ساتھ نون حذف ہو جاتی ہے: افْتَحِي۔", "explanation_en": "Feminine takes ya and drops nun: If-tahee."
        }
    ]

    # =========================================================================
    # UNIT 15: لا الناهية وجزم المضارع
    # =========================================================================
    units[15] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u15_q1", "book": 2, "unit_num": 15, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "نہی کا فہم۔", "grammar_goal_en": "Prohibition comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَاذَا قَالَ الْمُدَرِّسُ لِأَحْمَدَ؟ [ ＿＿＿ ]",
            "prompt_ur": "استاد نے احمد سے کیا کہا؟", "prompt_en": "What did the teacher say to Ahmad?",
            "answer": "لَا تَخْرُجْ مِنَ الْفَصْلِ .",
            "options": ["لَا تَخْرُجْ مِنَ الْفَصْلِ .", "اخْرُجْ مِنَ الْفَصْلِ .", "لَا تَكْتُبْ .", "لَا تَشْرَبْ ."],
            "emoji": "🛑", "hint_ur": "کلاس سے باہر مت نکلو۔", "hint_en": "Do not leave the classroom.",
            "explanation_ur": "درست جواب: 'لَا تَخْرُجْ مِنَ الْفَصْلِ .'۔", "explanation_en": "Correct answer: Do not exit."
        },
        # Tamreen 3: دخول لا الناهية وجزم المضارع
        {
            "id": "b2_u15_q2", "book": 2, "unit_num": 15, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): لا ناہیہ کا جزم", "badge_en": "Exercise (3): Jussive with La an-Nahiyah",
            "tamreen_title_ar": "دُخُولُ (لَا النَّاهِيَةِ) وَجَزْمُ الْمُضَارِعِ بِالسُّكُونِ:", "tamreen_title_ur": "لا ناہیہ داخل کریں اور مضارع کو جزم (سکون) دیں:", "tamreen_title_en": "Entering La an-Nahiyah and making verb jussive:",
            "grammar_goal_ur": "لا ناہیہ مضارع کو جزم دیتی ہے (لَا تَشْرَبْ)۔", "grammar_goal_en": "Prohibitive La gives jussive sukoon to verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا حَامِدُ، [ ＿＿＿ ] الْمَاءَ الْبَارِدَ .",
            "prompt_ur": "ٹھنڈا پانی مت پیو:", "prompt_en": "Do not drink cold water:",
            "answer": "لَا تَشْرَبْ",
            "options": ["لَا تَشْرَبْ", "لَا تَشْرَبُ", "لَا تَشْرَبِ", "مَا تَشْرَبُ"],
            "emoji": "🧊", "hint_ur": "نہ پیو (لَا تَشْرَبْ - سکون کے ساتھ)۔", "hint_en": "Do not drink (La Tashrab with sukoon).",
            "explanation_ur": "لا ناہیہ کی وجہ سے مضارع مجزوم ہوگا: لَا تَشْرَبْ۔", "explanation_en": "Jussive with sukoon: La tashrab."
        },
        # Tamreen 4: لا الناهية للجمع
        {
            "id": "b2_u15_q3", "book": 2, "unit_num": 15, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): نہی جمع مذکر (لَا تَفْعَلُوا)", "badge_en": "Exercise (4): Prohibitive for Plural",
            "tamreen_title_ar": "جَزْمُ الأَفْعَالِ الْخَمْسَةِ بِحَذْفِ النُّونِ بَعْدَ لَا النَّاهِيَةِ:", "tamreen_title_ur": "جمع مذکر کے لیے نون گرا کر نہی بنانا:", "tamreen_title_en": "Dropping nun after prohibitive La with plural:",
            "grammar_goal_ur": "لَا تَخْرُجُوا مِنَ الْفَصْلِ فِي وَقْتِ الدَّرْسِ۔", "grammar_goal_en": "Dropping nun with plural masculine prohibitive.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا إِخْوَانُ، [ ＿＿＿ ] فِي الْفَصْلِ .",
            "prompt_ur": "بھائیو، کلاس میں مت ہنسو (جمع کی نہی منتخب کریں):", "prompt_en": "Brothers, do not laugh in class (select plural):",
            "answer": "لَا تَضْحَكُوا",
            "options": ["لَا تَضْحَكُوا", "لَا تَضْحَكُونَ", "لَا تَضْحَكْ", "مَا تَضْحَكُوا"],
            "emoji": "🤫", "hint_ur": "مت ہنسو (لَا تَضْحَكُوا - نون گر گیا)۔", "hint_en": "Do not laugh (La Tadhakoo).",
            "explanation_ur": "لا ناہیہ کی وجہ سے جمع کا نون گر جاتا ہے: لَا تَضْحَكُوا۔", "explanation_en": "Prohibitive drops nun in plural: La Tadhakoo."
        },
        # Tamreen 5: الفرق بين لا الناهية ولا النافية
        {
            "id": "b2_u15_q4", "book": 2, "unit_num": 15, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): لا ناہیہ اور لا نافیہ کا فرق", "badge_en": "Exercise (5): Prohibitive vs Negative La",
            "tamreen_title_ar": "الْفَرْقُ بَيْنَ (لَا النَّاهِيَةِ الْجَازِمَةِ) وَ(لَا النَّافِيَةِ غَيْرِ الْعَامِلَةِ):", "tamreen_title_ur": "لا ناہیہ (جزم دینے والی) اور لا نافیہ (بے عمل) کا فرق:", "tamreen_title_en": "Distinguishing Jussive Prohibitive La vs Ineffective Negative La:",
            "grammar_goal_ur": "لَا تَكْتُبْ (نہی، جزم) بمقابلہ أَنَا لَا أَكْتُبُ (نفی، مرفوع)۔", "grammar_goal_en": "Understanding jussive meaning of nahy vs simple negation.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] الشَّايَ فِي اللَّيْلِ .",
            "prompt_ur": "میں رات کو چائے نہیں پیتا (یہ صرف خبر/نفی ہے):", "prompt_en": "I do not drink tea at night (pure negation):",
            "answer": "لَا أَشْرَبُ",
            "options": ["لَا أَشْرَبُ", "لَا أَشْرَبْ", "لَمْ أَشْرَبُ", "لَنْ أَشْرَبْ"],
            "emoji": "☕", "hint_ur": "لا نافیہ فعل کو جزم نہیں دیتی، وہ مرفوع رہتا ہے: لَا أَشْرَبُ۔", "hint_en": "Negative La leaves verb nominative: La Ashrabu.",
            "explanation_ur": "یہاں لا نافیہ ہے اس لیے مضارع مرفوع رہے گا: لَا أَشْرَبُ۔", "explanation_en": "Negative La does not cause jussive: La Ashrabu."
        }
    ]

    return units

if __name__ == '__main__':
    u = get_b2_units_6_to_15()
    print("Units 6-15 built successfully!")
    for k in sorted(u.keys()):
        print(f"Unit {k}: {len(u[k])} questions")
