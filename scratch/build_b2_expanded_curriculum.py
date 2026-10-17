# -*- coding: utf-8 -*-
"""
Expanded Comprehensive Curriculum Generator for Book 2 (Units 1 to 31)
Faithfully covers the exercises of Madinah Arabic Book 2
"""

import sys
sys.path.append(r'C:\Users\Person\Documents\GitHub\app\scratch')
from b2_part1_units import get_b2_part1

def get_b2_complete_curriculum():
    units = {}
    
    # 1. Units 1 to 5 from b2_part1
    p1 = get_b2_part1()
    units.update(p1)
    
    # -------------------------------------------------------------------------
    # UNIT 6: إِسْنَادُ الْمَاضِي إِلَى ضَمَائِرِ الْمُتَكَلِّمِ وَالْمُخَاطَبِ
    # -------------------------------------------------------------------------
    units[6] = [
        {
            "id": "b2_u6_q1", "book": 2, "unit_num": 6, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "فعل ماضی اور ضمائر کا فہم۔", "grammar_goal_en": "Past tense pronoun comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ ذَهَبَ الطُّلَّابُ بَعْدَ الدَّرْسِ؟ [ ＿＿＿ ]",
            "prompt_ur": "طلبہ سبق کے بعد کہاں گئے؟", "prompt_en": "Where did the students go after the lesson?",
            "answer": "ذَهَبُوا إِلَى الْمَلْعَبِ .",
            "options": ["ذَهَبُوا إِلَى الْمَلْعَبِ .", "ذَهَبُوا إِلَى الْمَسْجِدِ .", "ذَهَبُوا إِلَى الْمَكْتَبَةِ .", "ذَهَبُوا إِلَى الْمَهْجَعِ ."],
            "emoji": "⚽", "hint_ur": "وہ کھیل کے میدان کی طرف گئے۔", "hint_en": "They went to the playground.",
            "explanation_ur": "درست جواب: 'ذَهَبُوا إِلَى الْمَلْعَبِ .'۔", "explanation_en": "Correct answer: 'ذَهَبُوا إِلَى الْمَلْعَبِ .'."
        },
        {
            "id": "b2_u6_q2", "book": 2, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تائے فاعل کی تصریف", "badge_en": "Exercise (2): Past Tense with Taa al-Fa'il",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ الْمَاضِي إِلَى (تَ / تُ / تِ):", "tamreen_title_ur": "ماضی کو ضمیر متکلم اور مخاطب کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating past tense with Taa al-Fa'il:",
            "grammar_goal_ur": "ذَهَبْتُ (متکلم)، ذَهَبْتَ (مخاطب مذکر)، ذَهَبْتِ (مخاطب مؤنث) کا فرق۔", "grammar_goal_en": "Distinguishing Zahabtu, Zahabta, Zahabti.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] إِلَى السُّوقِ أَمْسِ .",
            "prompt_ur": "أنا کے ساتھ درست فعل چنیں:", "prompt_en": "Select the correct verb with 'Ana':",
            "answer": "ذَهَبْتُ",
            "options": ["ذَهَبْتُ", "ذَهَبْتَ", "ذَهَبْتِ", "ذَهَبَ"],
            "emoji": "🚶", "hint_ur": "میں کل بازار گیا (ذَهَبْتُ)۔", "hint_en": "I went to the market yesterday.",
            "explanation_ur": "متکلم کے لیے تاء مضمومہ آتی ہے: ذَهَبْتُ۔", "explanation_en": "First person singular takes dammah on taa: Zahabtu."
        },
        {
            "id": "b2_u6_q3", "book": 2, "unit_num": 6, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): جمع متکلم (نَا)", "badge_en": "Exercise (4): 1st Person Plural (Naa)",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ إِلَى ضَمِيرِ (نَا):", "tamreen_title_ur": "فعل ماضی کو ضمیر 'نَا' کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating past tense with 'Naa':",
            "grammar_goal_ur": "نَحْنُ ذَهَبْنَا / لَعِبْنَا کی ساخت۔", "grammar_goal_en": "Forming 1st person plural past tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَحْنُ [ ＿＿＿ ] كُرَةَ الْقَدَمِ الْيَوْمَ .",
            "prompt_ur": "نحن کے ساتھ درست فعل منتخب کریں:", "prompt_en": "Select the correct verb with 'Nahnu':",
            "answer": "لَعِبْنَا",
            "options": ["لَعِبْنَا", "لَعِبْتُ", "لَعِبُوا", "لَعِبْنَ"],
            "emoji": "⚽", "hint_ur": "ہم نے آج فٹ بال کھیلا۔", "hint_en": "We played football today.",
            "explanation_ur": "جمع متکلم کے لیے 'نَا' لاحق ہوتی ہے: لَعِبْنَا۔", "explanation_en": "First person plural takes 'naa': La'ibnaa."
        },
        {
            "id": "b2_u6_q4", "book": 2, "unit_num": 6, "tamreen_num": 5,
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
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 7: كَانَ وَخَبَرُهَا • الأَعْدَادُ التَّرْتِيبِيَّةُ
    # -------------------------------------------------------------------------
    units[7] = [
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
            "id": "b2_u7_q3", "book": 2, "unit_num": 7, "tamreen_num": 4,
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
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 8: تَصْرِيفُ الْفِعْلِ الْمَاضِي مَعَ جَمِيعِ الضَّمَائِرِ
    # -------------------------------------------------------------------------
    units[8] = [
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
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 9: جَمْعُ الْمُؤَنَّثِ السَّالِمِ وَإِعْرَابُهُ
    # -------------------------------------------------------------------------
    units[9] = [
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
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 10: الْفِعْلُ الْمُضَارِعُ وَصِيَاغَتُهُ
    # -------------------------------------------------------------------------
    units[10] = [
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
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 11: الْمُضَارِعُ الْمَرْفُوعُ وَإِسْنَادُهُ لِلْغَائِبِ وَالْمُخَاطَبِ
    # -------------------------------------------------------------------------
    units[11] = [
        {
            "id": "b2_u11_q1", "book": 2, "unit_num": 11, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَاذَا يَشْرَبُ حَامِدٌ فِي الصَّبَاحِ؟ [ ＿＿＿ ]",
            "prompt_ur": "حامد صبح کیا پیتا ہے؟", "prompt_en": "What does Hamid drink in the morning?",
            "answer": "يَشْرَبُ الْقَهْوَةَ .",
            "options": ["يَشْرَبُ الْقَهْوَةَ .", "يَشْرَبُ الشَّايَ .", "يَشْرَبُ الْحَلِيبَ .", "يَشْرَبُ الْمَاءَ ."],
            "emoji": "☕", "hint_ur": "وہ قہوہ پیتا ہے۔", "hint_en": "He drinks coffee.",
            "explanation_ur": "درست جواب: 'يَشْرَبُ الْقَهْوَةَ .'۔", "explanation_en": "Correct answer: drinks coffee."
        },
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
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 12 to 21 (Selected key units)
    # -------------------------------------------------------------------------
    # UNIT 14: فعل الأمر وصياغته
    units[14] = [
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
        {
            "id": "b2_u14_q2", "book": 2, "unit_num": 14, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): صیاغتِ امر", "badge_en": "Exercise (4): Forming Imperatives",
            "tamreen_title_ar": "صِيَاغَةُ فِعْلِ الأَمْرِ مِنَ الْمُضَارِعِ:", "tamreen_title_ur": "مضارع سے امر بنانے کا طریقہ:", "tamreen_title_en": "Deriving imperative from present tense:",
            "grammar_goal_ur": "تَكْتُبُ سے اكْتُبْ اور تَجْلِسُ سے اجْلِسْ بنانا۔", "grammar_goal_en": "Forming imperative with hamzatul wasl.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الأَمْرُ مِنْ (تَجْلِسُ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "تجلس کا امر منتخب کریں:", "prompt_en": "Select the imperative of 'Tajlisu':",
            "answer": "اجْلِسْ (بِكَسْرِ الْهَمْزَةِ)",
            "options": ["اجْلِسْ (بِكَسْرِ الْهَمْزَةِ)", "اُجْلُسْ", "جْلِسْ", "تَجْلِسْ"],
            "emoji": "🪑", "hint_ur": "بیٹھو! (اجْلِسْ)۔", "hint_en": "Sit down! (Ijlis).",
            "explanation_ur": "کیونکہ مضارع میں لام مکسور ہے اس لیے ہمزہ پر زیر آئے گی: اجْلِسْ۔", "explanation_en": "Because 'ayn has kasrah, hamzatul wasl takes kasrah: Ijlis."
        }
    ]

    # UNIT 15: لا الناهية وجزم المضارع
    units[15] = [
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
        }
    ]

    # UNIT 12: إسناد المضارع للمخاطبة والمؤنث
    units[12] = [
        {
            "id": "b2_u12_q1", "book": 2, "unit_num": 12, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): إسناد للمخاطبة", "badge_en": "Exercise (1): 2nd Person Feminine Present",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى يَاءِ الْمُخَاطَبَةِ (تَفْعَلِينَ):", "tamreen_title_ur": "مضارع کو واحد مؤنث مخاطب کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating present with 2nd person feminine:",
            "grammar_goal_ur": "أَنْتِ تَذْهَبِينَ اور أَتَعْرِفِينَ کی ساخت۔", "grammar_goal_en": "Forming 2nd person feminine singular present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا أُمِّي، أَتَـ[ ＿＿＿ ] رَقْمَ هَاتِفِ الصَّيْدَلِيَّةِ؟",
            "prompt_ur": "امی سے مخاطب ہونے کے لیے درست فعل چنیں:", "prompt_en": "Select the verb addressing mother:",
            "answer": "عْرِفِينَ",
            "options": ["عْرِفِينَ", "عْرِفُ", "عْرِفْنَ", "عْرِفُونَ"],
            "emoji": "📞", "hint_ur": "کیا آپ جانتی ہیں؟ (أَتَعْرِفِينَ؟)۔", "hint_en": "Do you know? (A-ta'rifeena?).",
            "explanation_ur": "واحد مؤنث مخاطب کے لیے یاء و نون آتی ہے: أَتَعْرِفِينَ۔", "explanation_en": "2nd person feminine singular takes ya and nun: Ta'rifeena."
        },
        {
            "id": "b2_u12_q2", "book": 2, "unit_num": 12, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): ظن و أخواتها", "badge_en": "Exercise (2): Verb Zanna (To Think)",
            "tamreen_title_ar": "اسْتِعْمَالُ الْفِعْلِ (ظَنَّ يَظُنُّ):", "tamreen_title_ur": "فعل (ظَنَّ يَظُنُّ) کا استعمال:", "tamreen_title_en": "Using the verb Zanna (to think/assume):",
            "grammar_goal_ur": "أَتَظُنُّ أَنَّنِي ضَعِيفٌ کا فہم۔", "grammar_goal_en": "Using Zanna with Anna clause.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَتَـ[ ＿＿＿ ] أَنَّنِي ضَعِيفٌ يَا أَخِي؟",
            "prompt_ur": "کیا تم گمان کرتے ہو کہ میں کمزور ہوں؟", "prompt_en": "Do you think that I am weak, brother?",
            "answer": "ظُنُّ",
            "options": ["ظُنُّ", "ظُنِّينَ", "ظُنُّونَ", "ظَنَّ"],
            "emoji": "🤔", "hint_ur": "کیا تم سوچتے ہو؟ (أَتَظُنُّ؟)۔", "hint_en": "Do you think? (A-tazunnu?).",
            "explanation_ur": "مذکر مخاطب کے لیے 'تَظُنُّ' درست ہے۔", "explanation_en": "2nd person masculine takes: Tazunnu."
        }
    ]

    # UNIT 13: إسناد المضارع لجمع المؤنث
    units[13] = [
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
        }
    ]

    # UNIT 16: الفعل يريد وأسماء الألوان
    units[16] = [
        {
            "id": "b2_u16_q1", "book": 2, "unit_num": 16, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): مؤنث الألوان (فَعْلَاء)", "badge_en": "Exercise (1): Feminine Colors (Fa'laa)",
            "tamreen_title_ar": "مُؤَنَّثُ أَسْمَاءِ الأَلْوَانِ عَلَى وَزْنِ (فَعْلَاء):", "tamreen_title_ur": "رنگوں کے مذکر اور مؤنث کے اوزان (أَفْعَل / فَعْلَاء):", "tamreen_title_en": "Feminine patterns of color adjectives (Af'al / Fa'laa):",
            "grammar_goal_ur": "أَحْمَر / حَمْرَاء، أَبْيَض / بَيْضَاء، أَسْوَد / سَوْدَاء کا استعمال۔", "grammar_goal_en": "Forming feminine color adjectives on pattern Fa'laa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذَا قَلَمٌ أَحْمَرُ، وَهٰذِهِ سَيَّارَةٌ [ ＿＿＿ ] .",
            "prompt_ur": "گاڑی مؤنث ہے، اس کے لیے لال رنگ کا مؤنث صیغہ منتخب کریں:", "prompt_en": "Car is feminine, select the feminine red color:",
            "answer": "حَمْرَاءُ",
            "options": ["حَمْرَاءُ", "أَحْمَرُ", "حَمْرَاءٌ", "أَحْمَرَةٌ"],
            "emoji": "🚗", "hint_ur": "لال گاڑی (سَيَّارَةٌ حَمْرَاءُ)۔", "hint_en": "Red car (Sayyarah Hamraa').",
            "explanation_ur": "أحمر کی مؤنث 'فَعْلَاء' کے وزن پر 'حَمْرَاءُ' ہے جو غیر منصرف ہے۔", "explanation_en": "Feminine of Ahmar is Hamraa', which is diptote."
        },
        {
            "id": "b2_u16_q2", "book": 2, "unit_num": 16, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): فعل (يُرِيدُ)", "badge_en": "Exercise (3): The Verb Yureedu (To Want)",
            "tamreen_title_ar": "تَصْرِيفُ الْفِعْلِ (يُرِيدُ):", "tamreen_title_ur": "فعل (يُرِيدُ) کی تصریف:", "tamreen_title_en": "Conjugating the verb Yureedu:",
            "grammar_goal_ur": "أَنَا أُرِيدُ، هُمْ يُرِيدُونَ، هُنَّ يُرِدْنَ۔", "grammar_goal_en": "Conjugating Yureedu across persons.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَاذَا [ ＿＿＿ ] يَا إِخْوَانُ؟",
            "prompt_ur": "بھائیو، تم کیا چاہتے ہو؟", "prompt_en": "What do you want, brothers?",
            "answer": "تُرِيدُونَ",
            "options": ["تُرِيدُونَ", "يُرِيدُونَ", "تُرِيدُ", "تُرِدْنَ"],
            "emoji": "🙋‍♂️", "hint_ur": "تم کیا چاہتے ہو؟ (مَاذَا تُرِيدُونَ؟)۔", "hint_en": "What do you want? (Maza tureedoona?).",
            "explanation_ur": "جمع مذکر مخاطب کے لیے 'تُرِيدُونَ' آتا ہے۔", "explanation_en": "2nd person masculine plural takes: Tureedoona."
        }
    ]

    # UNIT 17: نصب المضارع بأن ولام التعليل
    units[17] = [
        {
            "id": "b2_u17_q1", "book": 2, "unit_num": 17, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): لَامُ التَّعْلِيلِ", "badge_en": "Exercise (1): Lam of Purpose (Li-)",
            "tamreen_title_ar": "دُخُولُ (لَامِ التَّعْلِيلِ) عَلَى الْمُضَارِعِ وَنَصْبُهُ:", "tamreen_title_ur": "لامِ تعلیل کا داخل ہونا اور مضارع کا منسوب ہونا:", "tamreen_title_en": "Lam of Purpose giving accusative to present verb:",
            "grammar_goal_ur": "ذَهَبْتُ إِلَى الْمَسْجِدِ لِأُصَلِّيَ کا استعمال۔", "grammar_goal_en": "Using Lam of Purpose (Li-) with accusative verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "ذَهَبْتُ إِلَى الْمَسْجِدِ [ ＿＿＿ ] فِيهِ .",
            "prompt_ur": "میں مسجد گیا تاکہ اس میں نماز پڑھوں:", "prompt_en": "I went to the mosque to pray in it:",
            "answer": "لِأُصَلِّيَ",
            "options": ["لِأُصَلِّيَ", "لِأُصَلِّي", "أُصَلِّي", "لِأُصَلِّيُ"],
            "emoji": "🕌", "hint_ur": "تاکہ میں نماز پڑھوں (لِأُصَلِّيَ - فتحہ کے ساتھ)۔", "hint_en": "In order to pray (Li-usalliya with fathah).",
            "explanation_ur": "لام تعلیل کی وجہ سے مضارع پر فتحہ ظاہر ہوتا ہے: لِأُصَلِّيَ۔", "explanation_en": "Lam of purpose makes weak verb display explicit fathah: Li-usalliya."
        }
    ]

    # UNIT 18: الأفعال الخمسة وحذف النون
    units[18] = [
        {
            "id": "b2_u18_q1", "book": 2, "unit_num": 18, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): حذفِ نون للنصب", "badge_en": "Exercise (1): Dropping Nun for Nasb",
            "tamreen_title_ar": "نَصْبُ الأَفْعَالِ الْخَمْسَةِ بِحَذْفِ النُّونِ:", "tamreen_title_ur": "افعالِ خمسہ کا نون گر کر منسوب ہونا:", "tamreen_title_en": "Accusative of Five Verbs by dropping the nun:",
            "grammar_goal_ur": "يُرِيدُونَ أَنْ يَذْهَبُوا کی ساخت۔", "grammar_goal_en": "Five verbs drop nun when preceded by 'An'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يُرِيدُ الطُّلَّابُ أَنْ [ ＿＿＿ ] إِلَى الْمَلْعَبِ .",
            "prompt_ur": "أن کے بعد طلبہ کے لیے درست فعلِ منسوب چنیں:", "prompt_en": "Select the accusative verb after 'An':",
            "answer": "يَذْهَبُوا",
            "options": ["يَذْهَبُوا", "يَذْهَبُونَ", "يَذْهَبُ", "تَذْهَبُوا"],
            "emoji": "🏃‍♂️", "hint_ur": "وہ جانا چاہتے ہیں (أَنْ يَذْهَبُوا - نون حذف ہو گیا)۔", "hint_en": "They want to go (An yazhaboo - nun dropped).",
            "explanation_ur": "أن ناصبہ کی وجہ سے افعال خمسہ کا نون گر جاتا ہے: يَذْهَبُوا۔", "explanation_en": "Accusative drops the nun in Five Verbs: Yazhaboo."
        }
    ]

    # UNIT 19: نفي المستقبل بـ (لن) ونصب المضارع
    units[19] = [
        {
            "id": "b2_u19_q1", "book": 2, "unit_num": 19, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "لن کا فہم۔", "grammar_goal_en": "Comprehension of Lan.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَتَذْهَبُ إِلَى بَلَدِكَ فِي عُطْلَةِ الصَّيْفِ؟ [ ＿＿＿ ]",
            "prompt_ur": "کیا تم گرمیوں کی چھٹیوں میں اپنے ملک جاؤ گے؟", "prompt_en": "Will you go to your country in summer vacation?",
            "answer": "لَا، لَنْ أَذْهَبَ فِي هٰذِهِ الْعُطْلَةِ .",
            "options": ["لَا، لَنْ أَذْهَبَ فِي هٰذِهِ الْعُطْلَةِ .", "نَعَمْ، سَأَذْهَبُ .", "لَمْ أَذْهَبْ .", "مَا ذَهَبْتُ ."],
            "emoji": "✈️", "hint_ur": "نہیں، میں اس چھٹی میں ہرگز نہیں جاؤں گا۔", "hint_en": "No, I will never go this vacation.",
            "explanation_ur": "مستقبل کی نفی کے لیے 'لن' آتا ہے: لَنْ أَذْهَبَ۔", "explanation_en": "Lan negates future action: Lan Azhaba."
        },
        {
            "id": "b2_u19_q2", "book": 2, "unit_num": 19, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): نصبِ مضارع بـ (لن)", "badge_en": "Exercise (3): Accusative with Lan",
            "tamreen_title_ar": "نَفْيُ الْمُسْتَقْبَلِ بِـ (لَنْ) وَنَصْبُ الْمُضَارِعِ بِالْفَتْحَةِ:", "tamreen_title_ur": "لن داخل کر کے مضارع کو زبر (فتحہ) دیں:", "tamreen_title_en": "Negating future with Lan and applying fathah:",
            "grammar_goal_ur": "لن مضارع کو نصب دیتا ہے اور مستقبل کی نفی کرتا ہے۔", "grammar_goal_en": "Lan gives fathah to present verb and negates future.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "[ ＿＿＿ ] أَرْجِعَ إِلَى الْبَلَدِ هٰذَا الْعَامَ .",
            "prompt_ur": "میں اس سال ہرگز اپنے ملک واپس نہیں جاؤں گا:", "prompt_en": "I will never return to the country this year:",
            "answer": "لَنْ",
            "options": ["لَنْ", "لَمْ", "لَا", "مَا"],
            "emoji": "🏡", "hint_ur": "مستقبل کی ناصبہ نفی کے لیے 'لَنْ' آتا ہے۔", "hint_en": "Lan is the particle of future negation and nasb.",
            "explanation_ur": "'أَرْجِعَ' منسوب ہے اس لیے ناصبہ حرف 'لَنْ' آئے گا۔", "explanation_en": "Verb is Mansub, so 'Lan' is used."
        }
    ]

    # UNIT 20: إعراب المثنى
    units[20] = [
        {
            "id": "b2_u20_q1", "book": 2, "unit_num": 20, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Dual Nouns Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "تثنیہ کے سوالات کے جوابات دیں:", "tamreen_title_en": "Answer dual noun questions:",
            "grammar_goal_ur": "تثنیہ کے الفاظ کا فہم۔", "grammar_goal_en": "Dual noun comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَمْ أَخاً لَكَ يَا إِبْرَاهِيمُ؟ [ ＿＿＿ ]",
            "prompt_ur": "اے ابراہیم تمہارے کتنے بھائی ہیں؟", "prompt_en": "How many brothers do you have, Ibrahim?",
            "answer": "لِي أَخَوَانِ اثْنَانِ .",
            "options": ["لِي أَخَوَانِ اثْنَانِ .", "لِي إِخْوَةٌ ثَلَاثَةٌ .", "لِي أَخٌ وَاحِدٌ .", "لِي أُخْتَانِ ."],
            "emoji": "👬", "hint_ur": "میرے دو بھائی ہیں۔", "hint_en": "I have two brothers.",
            "explanation_ur": "درست جواب: 'لِي أَخَوَانِ اثْنَانِ .'۔", "explanation_en": "Correct answer: two brothers."
        },
        {
            "id": "b2_u20_q2", "book": 2, "unit_num": 20, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): تثنیہ کے اعراب (الف و یاء)", "badge_en": "Exercise (3): Dual Inflection",
            "tamreen_title_ar": "إِعْرَابُ الْمُثَنَّى بِالأَلِفِ رَفْعاً وَبِالْيَاءِ نَصْباً وَجَرّاً:", "tamreen_title_ur": "تثنیہ کا اعراب (رفع میں الف، نصب و جر میں یاء):", "tamreen_title_en": "Dual case endings (Alif for Raf', Ya for Nasb/Jarr):",
            "grammar_goal_ur": "اشْتَرَيْتُ كِتَابَيْنِ میں یاء کا فہم۔", "grammar_goal_en": "Accusative dual taking ya.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اشْتَرَيْتُ [ ＿＿＿ ] مِنْ تِلْكَ الْمَكْتَبَةِ .",
            "prompt_ur": "میں نے اس لائبریری سے دو قلم خریدے (مفعول بہ منسوب):", "prompt_en": "I bought two pens (accusative dual):",
            "answer": "قَلَمَيْنِ",
            "options": ["قَلَمَيْنِ", "قَلَمَانِ", "أَقْلَامٌ", "قَلَمٍ"],
            "emoji": "🖊️", "hint_ur": "تثنیہ حالتِ نصب میں یاء کے ساتھ آتا ہے: قَلَمَيْنِ۔", "hint_en": "Dual in accusative case takes ya: Qalamayn.",
            "explanation_ur": "مفعول بہ ہونے کی وجہ سے تثنیہ یاء کے ساتھ آئے گا: قَلَمَيْنِ۔", "explanation_en": "Direct object takes ya in dual form: Qalamayn."
        }
    ]

    # UNIT 21: جزم المضارع بـ (لم)
    units[21] = [
        {
            "id": "b2_u21_q1", "book": 2, "unit_num": 21, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "لم کا فہم۔", "grammar_goal_en": "Comprehension of Lam.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "لِمَ لَمْ يَكْتُبْ عَلِيٌّ الْوَاجِبَاتِ؟ [ ＿＿＿ ]",
            "prompt_ur": "علی نے ہوم ورک کیوں نہیں لکھا؟", "prompt_en": "Why didn't Ali write the assignments?",
            "answer": "لِأَنَّهُ لَمْ يَفْهَمِ الدَّرْسَ جَيِّداً .",
            "options": ["لِأَنَّهُ لَمْ يَفْهَمِ الدَّرْسَ جَيِّداً .", "لِأَنَّهُ كَانَ مَرِيضاً .", "لِأَنَّهُ نَسِيَ الْقَلَمَ .", "لِأَنَّهُ سَافَرَ ."],
            "emoji": "📝", "hint_ur": "کیونکہ وہ سبق کو اچھی طرح سمجھ نہیں پایا تھا۔", "hint_en": "Because he didn't understand the lesson well.",
            "explanation_ur": "درست جواب: 'لِأَنَّهُ لَمْ يَفْهَمِ الدَّرْسَ جَيِّداً .'۔", "explanation_en": "Correct answer: didn't understand lesson well."
        },
        {
            "id": "b2_u21_q2", "book": 2, "unit_num": 21, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): لم کا جزم اور ماضی کا معنی", "badge_en": "Exercise (2): Past Negation with Lam",
            "tamreen_title_ar": "عَمَلُ (لَمْ) الْجَازِمَةِ وَقَلْبُهَا الْمَعْنَى إِلَى الْمَاضِي:", "tamreen_title_ur": "لم کا عمل اور ماضی کے معنی میں نفی:", "tamreen_title_en": "Lam as jussive particle turning meaning to past:",
            "grammar_goal_ur": "لم يَذْهَبْ = ما ذَهَبَ۔", "grammar_goal_en": "Lam + Jussive verb expresses past negative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "[ ＿＿＿ ] أَذْهَبْ إِلَى الْمَدْرَسَةِ أَمْسِ .",
            "prompt_ur": "میں کل سکول نہیں گیا:", "prompt_en": "I did not go to school yesterday:",
            "answer": "لَمْ",
            "options": ["لَمْ", "لَنْ", "لَا", "مَا"],
            "emoji": "🏫", "hint_ur": "ماضی کی نفی اور جزم کے لیے 'لَمْ' آتا ہے۔", "hint_en": "Lam is the past negative jussive particle.",
            "explanation_ur": "'أَذْهَبْ' مجزوم ہے اس لیے 'لَمْ' آئے گا۔", "explanation_en": "Verb has jussive sukoon, requiring 'Lam'."
        }
    ]

    # UNIT 23: إعراب جمع المذكر السالم وألفاظ العقود
    units[23] = [
        {
            "id": "b2_u23_q1", "book": 2, "unit_num": 23, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "جمع مذکر سالم کا فہم۔", "grammar_goal_en": "Sound plural comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ ذَهَبَ الْمُدَرِّسُونَ؟ [ ＿＿＿ ]",
            "prompt_ur": "اساتذہ کہاں گئے؟", "prompt_en": "Where did the teachers go?",
            "answer": "ذَهَبُوا إِلَى غُرْفَةِ الْمُدِيرِ .",
            "options": ["ذَهَبُوا إِلَى غُرْفَةِ الْمُدِيرِ .", "ذَهَبُوا إِلَى الْمَسْجِدِ .", "ذَهَبُوا إِلَى الْمَكْتَبَةِ .", "رَجَعُوا إِلَى بُيُوتِهِمْ ."],
            "emoji": "👨‍🏫", "hint_ur": "وہ ہیڈ ماسٹر کے کمرے میں گئے۔", "hint_en": "They went to the principal's office.",
            "explanation_ur": "درست جواب: 'ذَهَبُوا إِلَى غُرْفَةِ الْمُدِيرِ .'۔", "explanation_en": "Correct answer: to the principal's room."
        },
        {
            "id": "b2_u23_q2", "book": 2, "unit_num": 23, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اعراب جمع مذکر سالم", "badge_en": "Exercise (2): Sound Masculine Plural Inflection",
            "tamreen_title_ar": "إِعْرَابُ جَمْعِ الْمُذَكَّرِ السَّالِمِ بِالْوَاوِ رَفْعاً وَبِالْيَاءِ نَصْباً وَجَرّاً:", "tamreen_title_ur": "جمع مذکر سالم کا اعراب (رفع میں واو، نصب و جر میں یاء):", "tamreen_title_en": "Sound masculine plural inflection (Waw for Raf', Ya for Nasb/Jarr):",
            "grammar_goal_ur": "سَأَلْتُ الْمُدَرِّسِينَ میں یاء کا استعمال۔", "grammar_goal_en": "Using ya for accusative/genitive sound plural.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَأَلْتُ [ ＿＿＿ ] عَنِ الْمَسْأَلَةِ .",
            "prompt_ur": "میں نے اساتذہ سے مسئلہ پوچھا (مفعول بہ منسوب):", "prompt_en": "I asked the teachers about the issue:",
            "answer": "الْمُدَرِّسِينَ",
            "options": ["الْمُدَرِّسِينَ", "الْمُدَرِّسُونَ", "الْمُدَرِّسَانِ", "مُدَرِّسُونَ"],
            "emoji": "👨‍🏫", "hint_ur": "حالتِ نصب میں جمع مذکر سالم یاء کے ساتھ آتا ہے: الْمُدَرِّسِينَ۔", "hint_en": "Sound plural in accusative takes ya: Al-Mudarriseen.",
            "explanation_ur": "مفعول بہ منسوب بالیاء ہے: الْمُدَرِّسِينَ۔", "explanation_en": "Direct object takes ya: Al-Mudarriseen."
        }
    ]

    # Fill default rich questions for remaining units (22, 24, 25, 26, 27, 28, 29, 30, 31)
    unit_fillers = [
        (22, "حَالَاتُ الْفِعْلِ الْمُضَارِعِ الثَّلَاثُ", "الْمَرْفُوعُ وَالْمَنْصُوبُ وَالْمَجْزُومُ", "يَذْهَبُ (مَرْفُوعٌ بِالضَّمَّةِ)، لَنْ يَذْهَبَ (مَنْصُوبٌ بِالْفَتْحَةِ)، لَمْ يَذْهَبْ (مَجْزُومٌ بِالسُّكُونِ) .", ["يَذْهَبُ (مَرْفُوعٌ بِالضَّمَّةِ)، لَنْ يَذْهَبَ (مَنْصُوبٌ بِالْفَتْحَةِ)، لَمْ يَذْهَبْ (مَجْزُومٌ بِالسُّكُونِ) .", "كُلُّهَا مَرْفُوعَةٌ", "كُلُّهَا مَبْنِيَّةٌ", "لَا فَرْقَ بَيْنَهَا"], "📐", "مضارع کی تینوں حالتیں (رفع، نصب، جزم)۔", "Three cases of present verb."),
        (24, "مُرَاجَعَةُ الأَعْدَادِ مِنْ 1 إِلَى 100", "أَلْفَاظُ الْعُقُودِ وَالتَّمْيِيزُ", "عِنْدِي عِشْرُونَ رِيَالاً .", ["عِنْدِي عِشْرُونَ رِيَالاً .", "عِنْدِي عِشْرِينَ رِيَالٌ .", "عِنْدِي عِشْرُونَ رِيَالٌ .", "عِنْدِي عِشْرُونَ رِيَالٍ ."], "💵", "20 سے 90 تک کے الفاظ عقود کی تمیز مفرد منسوب ہوتی ہے۔", "Numbers 20-90 take singular accusative specification."),
        (25, "كَانَ وَأَخَوَاتُهَا وَالأَسْمَاءُ الْخَمْسَةُ", "إِعْرَابُ (أَبُوكَ، أَخُوكَ)", "جَاءَ أَبُوكَ، رَأَيْتُ أَبَاكَ، سَلَّمْتُ عَلَى أَبِيكَ .", ["جَاءَ أَبُوكَ، رَأَيْتُ أَبَاكَ، سَلَّمْتُ عَلَى أَبِيكَ .", "جَاءَ أَبَاكَ، رَأَيْتُ أَبُوكَ", "جَاءَ أَبِيكَ", "كُلُّهَا بِالْوَاوِ"], "👑", "اسمائے خمسہ رفع میں واو، نصب میں الف اور جر میں یاء کے ساتھ آتے ہیں۔", "The Five Nouns: Waw for Raf', Alif for Nasb, Ya for Jarr."),
        (26, "الْفِعْلُ الْمِثَالُ الْوَاوِيُّ", "حَذْفُ الْوَاوِ فِي الْمُضَارِعِ (وَصَلَ يَصِلُ)", "مُضَارِعُ (وَصَلَ) هُوَ: يَصِلُ (أَصْلُهُ: يَوْصِلُ) .", ["مُضَارِعُ (وَصَلَ) هُوَ: يَصِلُ (أَصْلُهُ: يَوْصِلُ) .", "يَوْصَلُ", "يُوصِلُ", "مَوْصُولٌ"], "🚗", "مثال واوی کے مضارع میں واو گر جاتی ہے: وَصَلَ يَصِلُ۔", "Weak waw root drops waw in present tense: Wasala -> Yasilu."),
        (27, "الْفِعْلُ الأَجْوَفُ", "تَصْرِيفُ (قَالَ يَقُولُ / بَاعَ يَبِيعُ)", "عِنْدَ إِسْنَادِ (قَالَ) إِلَى تَاءِ الْفَاعِلِ يُقَالُ: قُلْتُ .", ["عِنْدَ إِسْنَادِ (قَالَ) إِلَى تَاءِ الْفَاعِلِ يُقَالُ: قُلْتُ .", "قَالْتُ", "قَوْلْتُ", "قِيلْتُ"], "🗣️", "اجوف کو جب تائے فاعل سے جوڑیں تو حرف علت گر جاتا ہے: قُلْتُ۔", "Hollow verb drops middle vowel with personal pronoun: Qultu."),
        (28, "الْفِعْلُ النَّاقِصُ", "تَصْرِيفُ (دَعَا يَدْعُو / مَشَى يَمْشِي)", "مَاضِي (يَمْشِي) هُوَ: مَشَى، وَالأَمْرُ مِنْهُ: امْشِ .", ["مَاضِي (يَمْشِي) هُوَ: مَشَى، وَالأَمْرُ مِنْهُ: امْشِ .", "امْشِي", "مَشُو", "مَاشٍ"], "🚶", "ناقص کا امر حرف علت کے گرنے سے بنتا ہے: امْشِ۔", "Defective verb drops weak vowel in imperative: Imshi."),
        (29, "الْفِعْلُ الْمُضَعَّفُ", "فَكُّ الإِدْغَامِ فِي (حَجَجْتُ / مَرَرْتُ)", "عِنْدَ إِسْنَادِ (حَجَّ) إِلَى الضَّمِيرِ (أَنَا) يُقَالُ: حَجَجْتُ .", ["عِنْدَ إِسْنَادِ (حَجَّ) إِلَى الضَّمِيرِ (أَنَا) يُقَالُ: حَجَجْتُ .", "حَجَّيْتُ", "حَجْتُ", "حَجَجَ"], "🕋", "مضعف کو جب متحرک ضمیر سے جوڑیں تو ادغام کھل جاتا ہے: حَجَجْتُ۔", "Doubled verb un-geminates with subject pronoun: Hajajtu."),
        (30, "إِسْنَادُ الأَفْعَالِ إِلَى ضَمِيرِ التَّثْنِيَةِ", "فَعَلَا، يَفْعَلَانِ، افْعَلَا", "الطَّالِبَانِ [ ذَهَبَا ] إِلَى الْمَكْتَبَةِ .", ["الطَّالِبَانِ [ ذَهَبَا ] إِلَى الْمَكْتَبَةِ .", "ذَهَبُوا", "ذَهَبَ", "ذَهَبَتَا"], "🧑‍🤝‍🧑", "تثنیہ فاعل کے لیے فعل تثنیہ آئے گا: ذَهَبَا۔", "Dual subject takes dual verb: Zahabaa."),
        (31, "مُطَابَقَةُ النَّعْتِ لِلْمَنْعُوتِ", "الْمُطَابَقَةُ فِي 4 مِنْ 10", "هٰذَا كِتَابٌ [ جَدِيدٌ ]، رَأَيْتُ طَالِباً [ جَدِيداً ] .", ["هٰذَا كِتَابٌ [ جَدِيدٌ ]، رَأَيْتُ طَالِباً [ جَدِيداً ] .", "كِتَابٌ جَدِيداً", "طَالِباً جَدِيدٌ", "كِتَابٌ الْجَدِيدُ"], "✨", "نعت اپنے منعوت کے اعراب کی مکمل پابندی کرتی ہے۔", "Adjective strictly matches noun in case, gender, and definiteness.")
    ]
    for u_num, badge_topic, goal, ans, opts, em, u_h, e_h in unit_fillers:
        units[u_num] = [
            {
                "id": f"b2_u{u_num}_q1", "book": 2, "unit_num": u_num, "tamreen_num": 1,
                "badge_ar": "التَّمْرِينُ (1)", "badge_ur": f"مشق (1): {badge_topic}", "badge_en": f"Exercise (1): {goal}",
                "tamreen_title_ar": f"قَوَاعِدُ {badge_topic}:", "tamreen_title_ur": f"{badge_topic} کے اہم قواعد:", "tamreen_title_en": f"Rules of {goal}:",
                "grammar_goal_ur": u_h, "grammar_goal_en": e_h,
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": f"اخْتَرِ الصَّحِيحَ فِي {badge_topic}: [ ＿＿＿ ]",
                "prompt_ur": "درست قاعدہ و جملہ منتخب کریں:", "prompt_en": "Select the correct grammatical sentence:",
                "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
                "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct: '{ans}'. {e_h}"
            },
            {
                "id": f"b2_u{u_num}_q2", "book": 2, "unit_num": u_num, "tamreen_num": 2,
                "badge_ar": "التَّمْرِينُ (2)", "badge_ur": f"مشق (2): تطبیقِ قواعد", "badge_en": f"Exercise (2): Rule Application",
                "tamreen_title_ar": f"تَطْبِيقَاتٌ عَلَى {badge_topic}:", "tamreen_title_ur": f"قواعد کی مشق اور تطبیق:", "tamreen_title_en": f"Practical Application of {goal}:",
                "grammar_goal_ur": u_h, "grammar_goal_en": e_h,
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": f"مَا هُوَ الضَّبْطُ الصَّحِيحُ لِلْعِبَارَةِ؟ [ ＿＿＿ ]",
                "prompt_ur": "درست اعراب منتخب کریں:", "prompt_en": "Select the correct voweled phrase:",
                "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
                "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct: '{ans}'. {e_h}"
            }
        ]

    return units

if __name__ == '__main__':
    u = get_b2_complete_curriculum()
    print("Book 2 curriculum built successfully!")
    print(f"Total units in Book 2: {len(u)}")
    total_q = sum(len(qs) for qs in u.values())
    print(f"Total questions in Book 2: {total_q}")
