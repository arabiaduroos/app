# -*- coding: utf-8 -*-
"""
Deep Authentic Curriculum for Book 2 Units 16 to 31
Faithfully extracted from Madinah Book 2 lessons and exercises.
"""

def get_b2_units_16_to_31():
    units = {}

    # =========================================================================
    # UNIT 16: الفعل يريد وأسماء الألوان وأوزانها
    # =========================================================================
    units[16] = [
        # Tamreen 1: مؤنث الألوان (فعلاء)
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
            "id": "b2_u16_q2", "book": 2, "unit_num": 16, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): رنگ زرد (صفراء)", "badge_en": "Exercise (1): Yellow Color Feminine",
            "tamreen_title_ar": "تَأْنِيثُ اللَّوْنِ الأَصْفَرِ (صَفْرَاءُ):", "tamreen_title_ur": "أصفر کی مؤنث صفراءُ کا استعمال:", "tamreen_title_en": "Feminine form of yellow (Asfar -> Safraa'):",
            "grammar_goal_ur": "بَقَرَةٌ صَفْرَاءُ فاقِعٌ لَوْنُهَا۔", "grammar_goal_en": "Recognizing feminine yellow from Quranic usage.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَالَ تَعَالَى: { إِنَّهَا بَقَرَةٌ [ ＿＿＿ ] فَاقِعٌ لَوْنُهَا } .",
            "prompt_ur": "قرآنی آیت میں گائے کے لیے زرد رنگ کی مؤنث چنیں:", "prompt_en": "Select the feminine yellow adjective in the Quranic verse:",
            "answer": "صَفْرَاءُ",
            "options": ["صَفْرَاءُ", "أَصْفَرُ", "صَفْرَاءٌ", "صَفْرَةٌ"],
            "emoji": "🐄", "hint_ur": "زرد رنگ کی گائے (بَقَرَةٌ صَفْرَاءُ)۔", "hint_en": "Yellow cow (Baqaratun Safraa').",
            "explanation_ur": "بقرۃ مؤنث ہے اس لیے 'صَفْرَاءُ' آئے گا۔", "explanation_en": "Baqarah is feminine, taking Safraa'."
        },
        # Tamreen 2: جمع الألوان (فُعْل)
        {
            "id": "b2_u16_q3", "book": 2, "unit_num": 16, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جمع الألوان (فُعْل)", "badge_en": "Exercise (2): Plural of Colors (Fu'l)",
            "tamreen_title_ar": "جَمْعُ أَسْمَاءِ الأَلْوَانِ عَلَى وَزْنِ (فُعْل):", "tamreen_title_ur": "رنگوں کی جمع کا وزن 'فُعْل' (حُمْر، سُود، صُفْر):", "tamreen_title_en": "Plural pattern for colors (Fu'l):",
            "grammar_goal_ur": "أَحْمَر / حَمْرَاء کی جمع حُمْرٌ ہے اور أَسْوَد / سَوْدَاء کی جمع سُودٌ ہے۔", "grammar_goal_en": "Plural of colors takes pattern Fu'l.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذِهِ أَقْلَامٌ [ ＿＿＿ ] .",
            "prompt_ur": "یہ لال قلم ہیں (أحمر کی جمع منتخب کریں):", "prompt_en": "These are red pens (select plural of Ahmar):",
            "answer": "حُمْرٌ",
            "options": ["حُمْرٌ", "أَحَامِرُ", "حَمْرَاوَاتٌ", "أَحْمَرُونَ"],
            "emoji": "🖍️", "hint_ur": "أحمر کی جمع 'حُمْرٌ' ہے۔", "hint_en": "Plural of Ahmar is Humr.",
            "explanation_ur": "أحمر اور حمراء دونوں کی جمع 'حُمْرٌ' آتی ہے۔", "explanation_en": "Plural of both masculine and feminine color is Humrun."
        },
        # Tamreen 3: تصريف الفعل (يريد)
        {
            "id": "b2_u16_q4", "book": 2, "unit_num": 16, "tamreen_num": 3,
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
        },
        {
            "id": "b2_u16_q5", "book": 2, "unit_num": 16, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): يريد مع نون النسوة", "badge_en": "Exercise (3): Yureedu with Nun an-Niswah",
            "tamreen_title_ar": "إِسْنَادُ (يُرِيدُ) إِلَى نُونِ النِّسْوَةِ (يُرِدْنَ / تُرِدْنَ):", "tamreen_title_ur": "فعل یرید کو نون نسوہ کے ساتھ جوڑنا:", "tamreen_title_en": "Attaching Nun an-Niswah to Yureedu (dropping yaa):",
            "grammar_goal_ur": "الطَّالِبَاتُ يُرِدْنَ الدُّخُولَ کی ساخت۔", "grammar_goal_en": "Dropping yaa when attaching nun an-niswah: Yuridna.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطَّالِبَاتُ [ ＿＿＿ ] أَنْ يَذْهَبْنَ إِلَى الْمَكْتَبَةِ .",
            "prompt_ur": "طالبات لائبریری جانا چاہتی ہیں (طالبات کے لیے درست فعل چنیں):", "prompt_en": "Female students want to go to library (select verb):",
            "answer": "يُرِدْنَ",
            "options": ["يُرِدْنَ", "يُرِيدُونَ", "تُرِدْنَ", "يُرِيدْنَ"],
            "emoji": "📚", "hint_ur": "نون نسوہ کے ساتھ یاء گر جاتی ہے: يُرِدْنَ۔", "hint_en": "Yaa is dropped before nun an-niswah: Yuridna.",
            "explanation_ur": "اجتماع ساکنین کی وجہ سے یاء گر جاتی ہے: يُرِدْنَ۔", "explanation_en": "Yaa drops to prevent two sukoons: Yuridna."
        }
    ]

    # =========================================================================
    # UNIT 17: أن المصدرية ونصب الفعل المضارع ولام التعليل
    # =========================================================================
    units[17] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u17_q1", "book": 2, "unit_num": 17, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "سبق کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "إِلَى أَيْنَ يُرِيدُ الطُّلَّابُ أَنْ يَذْهَبُوا فِي يَوْمِ الْجُمُعَةِ؟ [ ＿＿＿ ]",
            "prompt_ur": "طلبہ جمعہ کے دن کہاں جانا چاہتے ہیں؟", "prompt_en": "Where do students want to go on Friday?",
            "answer": "يُرِيدُونَ أَنْ يَذْهَبُوا إِلَى حَدِيقَةِ الْحَيَوَانَاتِ .",
            "options": ["يُرِيدُونَ أَنْ يَذْهَبُوا إِلَى حَدِيقَةِ الْحَيَوَانَاتِ .", "يُرِيدُونَ أَنْ يَذْهَبُوا إِلَى السُّوقِ .", "يُرِيدُونَ أَنْ يَذْهَبُوا إِلَى الْمَلْعَبِ .", "يُرِيدُونَ أَنْ يَبْقَوْا فِي الْمَهْجَعِ ."],
            "emoji": "🦁", "hint_ur": "وہ چڑیا گھر جانا چاہتے ہیں۔", "hint_en": "They want to go to the zoo.",
            "explanation_ur": "درست جواب: 'يُرِيدُونَ أَنْ يَذْهَبُوا إِلَى حَدِيقَةِ الْحَيَوَانَاتِ .'۔", "explanation_en": "Correct answer: to the zoo."
        },
        # Tamreen 6 & 7: أن المصدرية ونصب المضارع
        {
            "id": "b2_u17_q2", "book": 2, "unit_num": 17, "tamreen_num": 7,
            "badge_ar": "التَّمْرِينُ (7)", "badge_ur": "مشق (7): أَنْ مَصدَرِیَّہ کا نَصب", "badge_en": "Exercise (7): Subjunctive with 'An'",
            "tamreen_title_ar": "نَصْبُ الْمُضَارِعِ بِـ (أَنْ) الْمَصْدَرِيَّةِ:", "tamreen_title_ur": "أن ناصبہ کے بعد فعل مضارع کو زبر دینا:", "tamreen_title_en": "Subjunctive nasb with 'An':",
            "grammar_goal_ur": "أُرِيدُ أَنْ أَذْهَبَ کی ساخت۔", "grammar_goal_en": "Using 'An' followed by accusative present verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أُرِيدُ أَنْ [ ＿＿＿ ] إِلَى مَكَّةَ لِلْعُمْرَةِ .",
            "prompt_ur": "میں عمرے کے لیے مکہ جانا چاہتا ہوں (أن کے بعد منسوب فعل چنیں):", "prompt_en": "I want to go to Makkah (select subjunctive verb):",
            "answer": "أَذْهَبَ",
            "options": ["أَذْهَبَ", "أَذْهَبُ", "أَذْهَبْ", "ذَهَبْتُ"],
            "emoji": "🕋", "hint_ur": "أن کے بعد مضارع پر زبر آتی ہے: أَذْهَبَ۔", "hint_en": "Verb after 'An' takes fathah: Azhaba.",
            "explanation_ur": "أن ناصبہ ہے اس لیے مضارع منسوب ہوگا: أَنْ أَذْهَبَ۔", "explanation_en": "'An' governs the subjunctive case: Azhaba."
        },
        # Tamreen 8: لام التعليل
        {
            "id": "b2_u17_q3", "book": 2, "unit_num": 17, "tamreen_num": 8,
            "badge_ar": "التَّمْرِينُ (8)", "badge_ur": "مشق (8): لَامُ التَّعْلِيلِ", "badge_en": "Exercise (8): Lam of Purpose (Li-)",
            "tamreen_title_ar": "دُخُولُ (لَامِ التَّعْلِيلِ) عَلَى الْمُضَارِعِ وَنَصْبُهُ:", "tamreen_title_ur": "لامِ تعلیل کا داخل ہونا اور مضارع کا منسوب ہونا:", "tamreen_title_en": "Lam of Purpose giving accusative to present verb:",
            "grammar_goal_ur": "ذَهَبْتُ إِلَى الْمَسْجِدِ لِأُصَلِّيَ کا استعمال۔", "grammar_goal_en": "Using Lam of Purpose (Li-) with accusative verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "دَخَلْتُ الْمَطْبَخَ [ ＿＿＿ ] الْمَاءَ .",
            "prompt_ur": "میں کچن میں داخل ہوا تاکہ پانی پیوں:", "prompt_en": "I entered the kitchen to drink water:",
            "answer": "لِأَشْرَبَ",
            "options": ["لِأَشْرَبَ", "لِأَشْرَبُ", "لِأَشْرَبْ", "أَشْرَبَ"],
            "emoji": "💧", "hint_ur": "تاکہ میں پیوں (لِأَشْرَبَ - فتحہ کے ساتھ)۔", "hint_en": "In order to drink (Li-ashraba).",
            "explanation_ur": "لام تعلیل کی وجہ سے مضارع منسوب ہوتا ہے: لِأَشْرَبَ۔", "explanation_en": "Lam of purpose requires accusative: Li-ashraba."
        },
        {
            "id": "b2_u17_q4", "book": 2, "unit_num": 17, "tamreen_num": 7,
            "badge_ar": "التَّمْرِينُ (7)", "badge_ur": "مشق (7): نسیان اور یادداشت", "badge_en": "Exercise (7): Nasiya An Aqula",
            "tamreen_title_ar": "اسْتِعْمَالُ (نَسِيَ أَنْ يَفْعَلَ):", "tamreen_title_ur": "'نَسِيتُ أَنْ أَقُولَ' کا استعمال:", "tamreen_title_en": "Using 'Nasiya An...' with subjunctive verb:",
            "grammar_goal_ur": "نَسِيتُ أَنْ أَقُولَ لَكَ شَيْئاً۔", "grammar_goal_en": "I forgot to say something to you.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَسِيتُ أَنْ [ ＿＿＿ ] لَكَ شَيْئاً يَا أُسْتَاذُ .",
            "prompt_ur": "استاد جی، میں آپ سے ایک بات کہنا بھول گیا:", "prompt_en": "Teacher, I forgot to say something to you:",
            "answer": "أَقُولَ",
            "options": ["أَقُولَ", "أَقُولُ", "أَقُولْ", "قُلْتُ"],
            "emoji": "🗣️", "hint_ur": "أن کے بعد 'أَقُولَ' پر زبر آئے گی۔", "hint_en": "Takes fathah after An: Aqoola.",
            "explanation_ur": "أن ناصبہ کی وجہ سے مضارع منسوب ہوگا: أَنْ أَقُولَ۔", "explanation_en": "Subjunctive after An: An aqoola."
        }
    ]

    # =========================================================================
    # UNIT 18: الأفعال الخمسة وحذف النون في النصب
    # =========================================================================
    units[18] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u18_q1", "book": 2, "unit_num": 18, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "لِمَاذَا جَاءَ الطُّلَّابُ إِلَى الْمُدَرِّسِ؟ [ ＿＿＿ ]",
            "prompt_ur": "طلبہ استاد کے پاس کیوں آئے؟", "prompt_en": "Why did the students come to the teacher?",
            "answer": "لِيَسْأَلُوهُ عَنْ مَسْأَلَةٍ فِي الْقُرْآنِ .",
            "options": ["لِيَسْأَلُوهُ عَنْ مَسْأَلَةٍ فِي الْقُرْآنِ .", "لِيَأْخُذُوا الْكُتُبَ .", "لِيَذْهَبُوا إِلَى الْمَلْعَبِ .", "لِيَشْكُوا إِلَى الْمُدِيرِ ."],
            "emoji": "❓", "hint_ur": "تاکہ وہ ان سے قرآن کا ایک مسئلہ پوچھیں۔", "hint_en": "To ask him about a question in the Quran.",
            "explanation_ur": "درست جواب: 'لِيَسْأَلُوهُ عَنْ مَسْأَلَةٍ فِي الْقُرْآنِ .'۔", "explanation_en": "Correct answer: To ask about a Quranic question."
        },
        # Tamreen 2: حذف النون مع واو الجماعة
        {
            "id": "b2_u18_q2", "book": 2, "unit_num": 18, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): حذفِ نون للنصب", "badge_en": "Exercise (2): Dropping Nun for Nasb",
            "tamreen_title_ar": "نَصْبُ الأَفْعَالِ الْخَمْسَةِ بِحَذْفِ النُّونِ:", "tamreen_title_ur": "افعالِ خمسہ کا نون گر کر منسوب ہونا:", "tamreen_title_en": "Accusative of Five Verbs by dropping the nun:",
            "grammar_goal_ur": "يُرِيدُونَ أَنْ يَذْهَبُوا کی ساخت۔", "grammar_goal_en": "Five verbs drop nun when preceded by 'An'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يُرِيدُ الطُّلَّابُ أَنْ [ ＿＿＿ ] إِلَى الْمَلْعَبِ .",
            "prompt_ur": "أن کے بعد طلبہ کے لیے درست فعلِ منسوب چنیں:", "prompt_en": "Select the accusative verb after 'An':",
            "answer": "يَذْهَبُوا",
            "options": ["يَذْهَبُوا", "يَذْهَبُونَ", "يَذْهَبُ", "تَذْهَبُوا"],
            "emoji": "🏃‍♂️", "hint_ur": "وہ جانا چاہتے ہیں (أَنْ يَذْهَبُوا - نون حذف ہو گیا)۔", "hint_en": "They want to go (An yazhaboo - nun dropped).",
            "explanation_ur": "أن ناصبہ کی وجہ سے افعال خمسہ کا نون گر جاتا ہے: يَذْهَبُوا۔", "explanation_en": "Accusative drops the nun in Five Verbs: Yazhaboo."
        },
        # Tamreen 4: حذف النون مع ياء المخاطبة
        {
            "id": "b2_u18_q3", "book": 2, "unit_num": 18, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): حذف نون لمخاطبہ", "badge_en": "Exercise (4): Dropping Nun for Fem. Addressee",
            "tamreen_title_ar": "نَصْبُ يَاءِ الْمُخَاطَبَةِ بِحَذْفِ النُّونِ (أَنْ تَفْعَلِي):", "tamreen_title_ur": "مؤنث مخاطب کے لیے نون گرانا:", "tamreen_title_en": "Dropping nun with 2nd person feminine singular:",
            "grammar_goal_ur": "أَتُرِيدِينَ أَنْ تَرْجِعِي إِلَى الْبَلَدِ؟", "grammar_goal_en": "Dropping nun from Tarji'eena after An: An Tarji'ee.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَتُرِيدِينَ أَنْ [ ＿＿＿ ] إِلَى بَلَدِكِ فِي الْعُطْلَةِ يَا مَرْيَمُ؟",
            "prompt_ur": "مریم سے پوچھنے کے لیے درست منسوب صیغہ چنیں:", "prompt_en": "Select the verb addressing Maryam after 'An':",
            "answer": "تَرْجِعِي",
            "options": ["تَرْجِعِي", "تَرْجِعِينَ", "تَرْجِعُ", "يَرْجِعْنَ"],
            "emoji": "✈️", "hint_ur": "أن کی وجہ سے نون گر جائے گی: أَنْ تَرْجِعِي۔", "hint_en": "Nun drops after An: An Tarji'ee.",
            "explanation_ur": "افعال خمسہ حالت نصب میں نون حذف کرتے ہیں: أَنْ تَرْجِعِي۔", "explanation_en": "Five verbs drop nun in subjunctive: Tarji'ee."
        },
        # Tamreen 5: لام التعليل مع واو الجماعة
        {
            "id": "b2_u18_q4", "book": 2, "unit_num": 18, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): لامِ تعلیل اور حذفِ نون", "badge_en": "Exercise (5): Lam of Purpose with Plural",
            "tamreen_title_ar": "دُخُولُ لَامِ التَّعْلِيلِ عَلَى الأَفْعَالِ الْخَمْسَةِ:", "tamreen_title_ur": "لامِ تعلیل سے افعال خمسہ کا نون گرنا:", "tamreen_title_en": "Lam of Purpose causing deletion of nun:",
            "grammar_goal_ur": "خَرَجَ الطُّلَّابُ لِيَلْعَبُوا كُرَةَ الْقَدَمِ۔", "grammar_goal_en": "Li-yal'aboo drops nun due to Lam of purpose.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "خَرَجَ الطُّلَّابُ مِنَ الْفَصْلِ [ ＿＿＿ ] كُرَةَ الْقَدَمِ .",
            "prompt_ur": "طلبہ کلاس سے نکلے تاکہ فٹ بال کھیلیں:", "prompt_en": "Students exited class to play football:",
            "answer": "لِيَلْعَبُوا",
            "options": ["لِيَلْعَبُوا", "لِيَلْعَبُونَ", "لِيَلْعَبْ", "يَلْعَبُونَ"],
            "emoji": "⚽", "hint_ur": "تاکہ وہ کھیلیں (لِيَلْعَبُوا - نون گر گیا)۔", "hint_en": "To play (Li-yal'aboo - nun dropped).",
            "explanation_ur": "لام تعلیل کی وجہ سے افعال خمسہ کا نون گر جاتا ہے: لِيَلْعَبُوا۔", "explanation_en": "Lam of purpose drops nun: Li-yal'aboo."
        }
    ]

    # =========================================================================
    # UNIT 19: نفي المستقبل بـ (لن) ونصب المضارع
    # =========================================================================
    units[19] = [
        # Tamreen 1: أسئلة الدرس
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
        # Tamreen 3: نصب المضارع بـ (لن)
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
        },
        # Tamreen 4: مقارنة أدوات النفي (ما، لا، لن)
        {
            "id": "b2_u19_q3", "book": 2, "unit_num": 19, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): أدوات النفی کا فرق", "badge_en": "Exercise (4): Negation Particles (Maa/Laa/Lan)",
            "tamreen_title_ar": "الْمُقَارَنَةُ بَيْنَ (مَا) لِلْمَاضِي، وَ(لَا) لِلْحَالِ، وَ(لَنْ) لِلْمُسْتَقْبَلِ:", "tamreen_title_ur": "ماضی، حال اور مستقبل کے حروفِ نفی کا فرق:", "tamreen_title_en": "Maa for past, Laa for present, Lan for future:",
            "grammar_goal_ur": "مَا ذَهَبْتُ أَمْسِ، لَا أَذْهَبُ الْيَوْمَ، لَنْ أَذْهَبَ غَداً۔", "grammar_goal_en": "Negation across three time frames.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَأَذْهَبُ إِلَى السُّوقِ غَداً ➔ [ ＿＿＿ ] إِلَى السُّوقِ غَداً .",
            "prompt_ur": "کل کی نفی کرنے کے لیے درست جملہ منتخب کریں:", "prompt_en": "Select the correct sentence negating tomorrow's action:",
            "answer": "لَنْ أَذْهَبَ",
            "options": ["لَنْ أَذْهَبَ", "مَا ذَهَبْتُ", "لَا أَذْهَبُ", "لَمْ أَذْهَبْ"],
            "emoji": "🛒", "hint_ur": "مستقبل کی نفی 'لَنْ أَذْهَبَ' سے ہوتی ہے۔", "hint_en": "Future is negated with Lan: Lan Azhaba.",
            "explanation_ur": "مستقبل کی قطعی نفی کے لیے 'لَنْ' اور منسوب فعل آتا ہے: لَنْ أَذْهَبَ۔", "explanation_en": "Lan + subjunctive negates future: Lan Azhaba."
        },
        # Tamreen 6: لن مع الأفعال الخمسة
        {
            "id": "b2_u19_q4", "book": 2, "unit_num": 19, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): لن کے ساتھ حذفِ نون", "badge_en": "Exercise (6): Lan with Five Verbs",
            "tamreen_title_ar": "حَذْفُ النُّونِ بَعْدَ (لَنْ) مَعَ وَاوِ الْجَمَاعَةِ:", "tamreen_title_ur": "لن داخل ہونے پر جمع کے افعال کا نون گرنا:", "tamreen_title_en": "Dropping nun with plural masculine after Lan:",
            "grammar_goal_ur": "لَنْ يَخْرُجُوا مِنَ الْفَصْلِ الْيَوْمَ۔", "grammar_goal_en": "Five verbs drop nun after Lan.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطُّلَّابُ [ ＿＿＿ ] إِلَى الْمَلْعَبِ الْيَوْمَ .",
            "prompt_ur": "طلبہ آج ہرگز میدان نہیں جائیں گے (درست صیغہ چنیں):", "prompt_en": "Students will never go to playground today:",
            "answer": "لَنْ يَذْهَبُوا",
            "options": ["لَنْ يَذْهَبُوا", "لَنْ يَذْهَبُونَ", "لَا يَذْهَبُوا", "لَمْ يَذْهَبُونَ"],
            "emoji": "⚽", "hint_ur": "لن کی وجہ سے نون حذف ہو جائے گا: لَنْ يَذْهَبُوا۔", "hint_en": "Nun is dropped after Lan: Lan Yazhaboo.",
            "explanation_ur": "افعال خمسہ لن کے بعد نون گرا دیتے ہیں: لَنْ يَذْهَبُوا۔", "explanation_en": "Lan drops nun in five verbs: Lan Yazhaboo."
        }
    ]

    # =========================================================================
    # UNIT 20: إعراب المثنى بالألف رفعاً وبالياء نصباً وجراً
    # =========================================================================
    units[20] = [
        # Tamreen 1: أسئلة الدرس
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
        # Tamreen 2: حالات المثنى الإعرابية
        {
            "id": "b2_u20_q2", "book": 2, "unit_num": 20, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تثنیہ کے اعراب (الف و یاء)", "badge_en": "Exercise (2): Dual Inflection",
            "tamreen_title_ar": "إِعْرَابُ الْمُثَنَّى بِالأَلِفِ رَفْعاً وَبِالْيَاءِ نَصْباً وَجَرّاً:", "tamreen_title_ur": "تثنیہ کا اعراب (رفع میں الف، نصب و جر میں یاء):", "tamreen_title_en": "Dual case endings (Alif for Raf', Ya for Nasb/Jarr):",
            "grammar_goal_ur": "اشْتَرَيْتُ كِتَابَيْنِ میں یاء کا فہم۔", "grammar_goal_en": "Accusative dual taking ya.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اشْتَرَيْتُ [ ＿＿＿ ] مِنْ تِلْكَ الْمَكْتَبَةِ .",
            "prompt_ur": "میں نے اس لائبریری سے دو قلم خریدے (مفعول بہ منسوب):", "prompt_en": "I bought two pens (accusative dual):",
            "answer": "قَلَمَيْنِ",
            "options": ["قَلَمَيْنِ", "قَلَمَانِ", "أَقْلَامٌ", "قَلَمٍ"],
            "emoji": "🖊️", "hint_ur": "تثنیہ حالتِ نصب میں یاء کے ساتھ آتا ہے: قَلَمَيْنِ۔", "hint_en": "Dual in accusative case takes ya: Qalamayn.",
            "explanation_ur": "مفعول بہ ہونے کی وجہ سے تثنیہ یاء کے ساتھ آئے گا: قَلَمَيْنِ۔", "explanation_en": "Direct object takes ya in dual form: Qalamayn."
        },
        # Tamreen 3: المجرور بالمثنى
        {
            "id": "b2_u20_q3", "book": 2, "unit_num": 20, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): تثنیہ حالتِ جر میں", "badge_en": "Exercise (5): Dual in Genitive Case",
            "tamreen_title_ar": "جَرُّ الْمُثَنَّى بِالْيَاءِ بَعْدَ حَرْفِ الْجَرِّ:", "tamreen_title_ur": "حرفِ جر کے بعد تثنیہ کو یاء دینا:", "tamreen_title_en": "Genitive case of dual with ya after preposition:",
            "grammar_goal_ur": "اشْتَرَيْتُ هٰذِهِ الْمَجَلَّةَ بِرِيَالَيْنِ اثْنَيْنِ۔", "grammar_goal_en": "Using ya for genitive dual after preposition Bi-.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "بِكَمْ رِيَالاً اشْتَرَيْتَ هٰذَا الْمُشْطَ؟ اشْتَرَيْتُهُ بِـ[ ＿＿＿ ] .",
            "prompt_ur": "میں نے اسے دو ریال میں خریدا (حرف جر باء کے بعد تثنیہ چنیں):", "prompt_en": "I bought it for two riyals (select genitive dual):",
            "answer": "رِيَالَيْنِ اثْنَيْنِ",
            "options": ["رِيَالَيْنِ اثْنَيْنِ", "رِيَالَينِ اثْنَانِ", "رِيَالَـانِ اثْنَانِ", "رِيَالَاتٍ"],
            "emoji": "💵", "hint_ur": "حرف جر کے بعد تثنیہ یاء کے ساتھ مجرور ہوتا ہے: بِرِيَالَيْنِ اثْنَيْنِ۔", "hint_en": "After preposition Bi-, dual takes ya: Bi-riyālayni ithnayn.",
            "explanation_ur": "تثنیہ حالت جر میں یاء کے ساتھ آتا ہے: بِرِيَالَيْنِ اثْنَيْنِ۔", "explanation_en": "Dual takes ya in genitive case: Bi-riyālayni ithnayn."
        },
        # Tamreen 8 & 9: أحدهما والآخر / إحداهما والأخرى
        {
            "id": "b2_u20_q4", "book": 2, "unit_num": 20, "tamreen_num": 8,
            "badge_ar": "التَّمْرِينُ (8)", "badge_ur": "مشق (8): أَحَدُهُمَا وَالآخَرُ", "badge_en": "Exercise (8): One of them and the Other",
            "tamreen_title_ar": "أُسْلُوبُ التَّثْنِيَةِ (أَحَدُهُمَا ... وَالآخَرُ):", "tamreen_title_ur": "دو مذکر چیزوں کے لیے 'أحدهما والآخر' کا استعمال:", "tamreen_title_en": "Using Ahaduhumaa ... wal-Aakhar for masculine dual:",
            "grammar_goal_ur": "لِي أَخَوَانِ، أَحَدُهُمَا طَبِيبٌ وَالآخَرُ مُهَنْدِسٌ۔", "grammar_goal_en": "Distributing two items using Ahaduhuma and Al-Aakhar.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدِي قَلَمَانِ، [ ＿＿＿ ] أَزْرَقُ وَالآخَرُ أَحْمَرُ .",
            "prompt_ur": "میرے پاس دو قلم ہیں، ایک نیلا ہے اور دوسرا لال:", "prompt_en": "I have two pens, one is blue and the other is red:",
            "answer": "أَحَدُهُمَا",
            "options": ["أَحَدُهُمَا", "إِحْدَاهُمَا", "وَاحِدٌ", "الأَوَّلُ"],
            "emoji": "🖊️", "hint_ur": "مذکر تثنیہ کے لیے 'أَحَدُهُمَا' آتا ہے۔", "hint_en": "For masculine dual, use Ahaduhumaa.",
            "explanation_ur": "قلم مذکر ہے اس لیے 'أَحَدُهُمَا' آئے گا۔", "explanation_en": "Qalam is masculine, taking Ahaduhumaa."
        },
        {
            "id": "b2_u20_q5", "book": 2, "unit_num": 20, "tamreen_num": 9,
            "badge_ar": "التَّمْرِينُ (9)", "badge_ur": "مشق (9): إِحْدَاهُمَا وَالأُخْرَى", "badge_en": "Exercise (9): Feminine Dual Pair",
            "tamreen_title_ar": "أُسْلُوبُ التَّثْنِيَةِ لِلْمُؤَنَّثِ (إِحْدَاهُمَا ... وَالأُخْرَى):", "tamreen_title_ur": "دو مؤنث چیزوں کے لیے 'إحداهما والأخرى':", "tamreen_title_en": "Feminine dual distribution (Ihdaahumaa ... wal-Ukhraa):",
            "grammar_goal_ur": "عِنْدِي سَيَّارَتَانِ إِحْدَاهُمَا حَمْرَاءُ وَالأُخْرَى بَيْضَاءُ۔", "grammar_goal_en": "Using feminine Ihdaahumaa and Al-Ukhraa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدِي سَيَّارَتَانِ، [ ＿＿＿ ] حَمْرَاءُ وَالأُخْرَى بَيْضَاءُ .",
            "prompt_ur": "میرے پاس دو گاڑیاں ہیں، ایک لال ہے اور دوسری سفید:", "prompt_en": "I have two cars, one is red and the other is white:",
            "answer": "إِحْدَاهُمَا",
            "options": ["إِحْدَاهُمَا", "أَحَدُهُمَا", "وَاحِدَةٌ", "الأُولَى"],
            "emoji": "🚗", "hint_ur": "مؤنث تثنیہ کے لیے 'إِحْدَاهُمَا' آتا ہے۔", "hint_en": "For feminine dual, use Ihdaahumaa.",
            "explanation_ur": "گاڑی مؤنث ہے اس لیے 'إِحْدَاهُمَا' درست ہے۔", "explanation_en": "Sayyarah is feminine, taking Ihdaahumaa."
        }
    ]

    # =========================================================================
    # UNIT 21: جزم المضارع بـ (لم) وقلب معناه إلى الماضي
    # =========================================================================
    units[21] = [
        # Tamreen 1: أسئلة الدرس
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
        # Tamreen 2: عمل (لم) الجازمة
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
        },
        # Tamreen 3: حذف النون بعد لم مع الأفعال الخمسة
        {
            "id": "b2_u21_q3", "book": 2, "unit_num": 21, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): لم کے ساتھ حذفِ نون", "badge_en": "Exercise (3): Jussive by Dropping Nun",
            "tamreen_title_ar": "جَزْمُ الأَفْعَالِ الْخَمْسَةِ بِحَذْفِ النُّونِ بَعْدَ (لَمْ):", "tamreen_title_ur": "لم داخل ہونے پر افعال خمسہ کا نون گرنا:", "tamreen_title_en": "Jussive case of five verbs by dropping nun after Lam:",
            "grammar_goal_ur": "الطُّلَّابُ لَمْ يَكْتُبُوا الْوَاجِبَ۔", "grammar_goal_en": "Five verbs drop nun when preceded by Lam.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطُّلَّابُ [ ＿＿＿ ] الْوَاجِبَاتِ أَمْسِ .",
            "prompt_ur": "طلبہ نے کل ہوم ورک نہیں لکھا (درست مجزوم صیغہ چنیں):", "prompt_en": "Students didn't write homework yesterday (select jussive):",
            "answer": "لَمْ يَكْتُبُوا",
            "options": ["لَمْ يَكْتُبُوا", "لَمْ يَكْتُبُونَ", "لَا يَكْتُبُوا", "مَا كَتَبُوا"],
            "emoji": "📝", "hint_ur": "لم کے بعد نون گر جائے گا: لَمْ يَكْتُبُوا۔", "hint_en": "Nun drops after Lam: Lam Yak-tuboo.",
            "explanation_ur": "افعال خمسہ حالت جزم میں نون گرا دیتے ہیں: لَمْ يَكْتُبُوا۔", "explanation_en": "Jussive drops nun in five verbs: Lam Yak-tuboo."
        },
        # Tamreen 4: الفرق بين لم ولن
        {
            "id": "b2_u21_q4", "book": 2, "unit_num": 21, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): لَمْ اور لَنْ کا فرق", "badge_en": "Exercise (4): Lam vs Lan",
            "tamreen_title_ar": "الْفَرْقُ بَيْنَ (لَمْ) الْجَازِمَةِ لِلْمَاضِي وَ(لَنْ) النَّاصِبَةِ لِلْمُسْتَقْبَلِ:", "tamreen_title_ur": "لم (ماضی کی جازمہ نفی) اور لن (مستقبل کی ناصبہ نفی) کا فرق:", "tamreen_title_en": "Distinguishing past jussive Lam vs future subjunctive Lan:",
            "grammar_goal_ur": "لَمْ يَذْهَبْ (ماضی) اور لَنْ يَذْهَبَ (مستقبل)۔", "grammar_goal_en": "Contrasting Lam (past jussive) and Lan (future subjunctive).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] أَلْعَبْ أَمْسِ، وَ[ ＿＿＿ ] أَلْعَبَ غَداً .",
            "prompt_ur": "میں کل نہیں کھیلا اور کل ہرگز نہیں کھیلوں گا (درست جوڑا چنیں):", "prompt_en": "I did not play yesterday, and will not play tomorrow:",
            "answer": "لَمْ ... لَنْ",
            "options": ["لَمْ ... لَنْ", "لَنْ ... لَمْ", "مَا ... لَا", "لَا ... لَمْ"],
            "emoji": "⏳", "hint_ur": "کل گزشتہ کے لیے 'لَمْ' اور کل آئندہ کے لیے 'لَنْ' آتا ہے۔", "hint_en": "Yesterday takes Lam, tomorrow takes Lan.",
            "explanation_ur": "ماضی کی جازمہ نفی 'لَمْ' ہے اور مستقبل کی ناصبہ نفی 'لَنْ' ہے۔", "explanation_en": "Lam negates past; Lan negates future."
        }
    ]

    # =========================================================================
    # UNIT 22: الممنوع من الصرف وأسبابه وحالات إعرابه
    # =========================================================================
    units[22] = [
        # Tamreen 1: أعلام على وزن أفعل أو مختومة بألف ونون
        {
            "id": "b2_u22_q1", "book": 2, "unit_num": 22, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): غیر منصرف کے اسباب", "badge_en": "Exercise (1): Diptote Categories",
            "tamreen_title_ar": "أَسْبَابُ مَنْعِ الاسْمِ مِنَ الصَّرْفِ (الأَعْلَامُ):", "tamreen_title_ur": "غیر منصرف اسماء کی وجوہات (علم اور وزن):", "tamreen_title_en": "Reasons for Diptote Status in Proper Nouns:",
            "grammar_goal_ur": "عُثْمَانُ، رَمَضَانُ، أَحْمَدُ پر تنوین نہ آنا۔", "grammar_goal_en": "Names ending in alif-nun or on pattern Af'al are diptotes.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الاسْمُ الْمَمْنُوعُ مِنَ الصَّرْفِ لِانْتِهَائِهِ بِأَلِفٍ وَنُونٍ زَائِدَتَيْنِ هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "الف اور نون زائدتان کی وجہ سے غیر منصرف نام چنیں:", "prompt_en": "Select the diptote noun ending in extra Alif and Nun:",
            "answer": "عُثْمَانُ",
            "options": ["عُثْمَانُ", "مُحَمَّدٌ", "عَلِيٌّ", "خَالِدٌ"],
            "emoji": "📜", "hint_ur": "عثمان کے آخر میں الف اور نون زائد ہے (غیر منصرف)۔", "hint_en": "Uthman ends in extra alif and nun.",
            "explanation_ur": "عثمان علم مؤنث معنوی نہیں بلکہ علم مع زیادۃ الف و نون ہے، اس لیے غیر منصرف ہے۔", "explanation_en": "Uthmanu is diptote due to proper noun + alif-nun."
        },
        # Tamreen 2: جر الممنوع من الصرف بالفتحة
        {
            "id": "b2_u22_q2", "book": 2, "unit_num": 22, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): غیر منصرف کا اعراب بالفتحہ", "badge_en": "Exercise (2): Diptote Genitive with Fathah",
            "tamreen_title_ar": "جَرُّ الْمَمْنُوعِ مِنَ الصَّرْفِ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ:", "tamreen_title_ur": "حالتِ جر میں غیر منصرف کو کسرہ کے بدلے فتحہ (زبر) دینا:", "tamreen_title_en": "Diptotes taking fathah in genitive case:",
            "grammar_goal_ur": "ذَهَبْتُ إِلَى مَكَّةَ اور سَلَّمْتُ عَلَى أَحْمَدَ۔", "grammar_goal_en": "Diptotes never take kasrah or tanween; genitive is marked by fathah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَافَرَ أَبِي إِلَى [ ＿＿＿ ] لِلْعُمْرَةِ .",
            "prompt_ur": "میرے والد عمرے کے لیے مکہ گئے (مکہ کا درست اعراب چنیں):", "prompt_en": "My father traveled to Makkah (select correct case for Makkah):",
            "answer": "مَكَّةَ",
            "options": ["مَكَّةَ", "مَكَّةِ", "مَكَّةٍ", "مَكَّةُ"],
            "emoji": "🕋", "hint_ur": "مکہ غیر منصرف ہے اس لیے حالت جر میں فتحہ (زبر) لے گا: إِلَى مَكَّةَ۔", "hint_en": "Makkah is diptote; takes fathah after Ila: Ila Makkata.",
            "explanation_ur": "مکہ علم مؤنث اور غیر منصرف ہے اس لیے زیر کے بدلے زبر آئے گی: مَكَّةَ۔", "explanation_en": "Diptote takes fathah in genitive case: Makkata."
        },
        # Tamreen 3: صيغ منتهى الجموع (مَفَاعِل / مَفَاعِيل)
        {
            "id": "b2_u22_q3", "book": 2, "unit_num": 22, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): صیغہ منتہی الجموع", "badge_en": "Exercise (3): Ultimate Plural Patterns",
            "tamreen_title_ar": "صِيَغُ مُنْتَهَى الْجُمُوعِ (مَسَاجِدُ / مَفَاتِيحُ):", "tamreen_title_ur": "مساجد اور مفاتیح کے اوزان پر جمع کا غیر منصرف ہونا:", "tamreen_title_en": "Plural patterns Mafa'il and Mafa'eel as diptotes:",
            "grammar_goal_ur": "صَلَّيْتُ فِي مَسَاجِدَ كَثِيرَةٍ کی ساخت۔", "grammar_goal_en": "Masajid is diptote and takes fathah when indefinite genitive.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "صَلَّيْنَا فِي [ ＿＿＿ ] كَثِيرَةٍ .",
            "prompt_ur": "ہم نے بہت سی مساجد میں نماز پڑھی (مساجد کا درست اعراب چنیں):", "prompt_en": "We prayed in many mosques (select correct case):",
            "answer": "مَسَاجِدَ",
            "options": ["مَسَاجِدَ", "مَسَاجِدِ", "مَسَاجِدٍ", "مَسَاجِدُ"],
            "emoji": "🕌", "hint_ur": "مساجد صیغہ منتہی الجموع کی وجہ سے غیر منصرف ہے: مَسَاجِدَ۔", "hint_en": "Masajid is diptote; takes fathah in genitive: Masajida.",
            "explanation_ur": "غیر منصرف تنوین اور کسرہ قبول نہیں کرتا اس لیے 'مَسَاجِدَ' درست ہے۔", "explanation_en": "Diptote plural takes fathah in genitive: Masajida."
        },
        # Tamreen 4: صفات على وزن فَعْلَان ومؤنثها فَعْلَى
        {
            "id": "b2_u22_q4", "book": 2, "unit_num": 22, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): صفات علی وزن فعلان", "badge_en": "Exercise (4): Adjectives on Fa'lan",
            "tamreen_title_ar": "الصِّفَاتُ عَلَى وَزْنِ (فَعْلَان) الَّتِي مُؤَنَّثُهَا (فَعْلَى):", "tamreen_title_ur": "کَسْلَانُ، جَوْعَانُ، غَضْبَانُ کا غیر منصرف ہونا:", "tamreen_title_en": "Adjectives on Fa'lan (Kaslan, Jaw'an, Ghadban) as diptotes:",
            "grammar_goal_ur": "أَنَا جَوْعَانُ (بغیر تنوین)۔", "grammar_goal_en": "Adjectives on Fa'lan never take tanween.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا لَسْتُ كَسْلَانَ، أَنَا [ ＿＿＿ ] جِدّاً .",
            "prompt_ur": "میں بہت بھوکا ہوں (جوعان پر درست اعراب چنیں):", "prompt_en": "I am very hungry (select Jaw'an with correct ending):",
            "answer": "جَوْعَانُ",
            "options": ["جَوْعَانُ", "جَوْعَانٌ", "جَوْعَاناً", "جَوْعَانِ"],
            "emoji": "🍽️", "hint_ur": "جوعان غیر منصرف ہے اس لیے تنوین نہیں آئے گی: جَوْعَانُ۔", "hint_en": "Jaw'an is diptote; takes single dammah: Jaw'aanu.",
            "explanation_ur": "فعلان کے وزن والی صفات غیر منصرف ہوتی ہیں اس لیے صرف ایک پیش آئے گی: جَوْعَانُ۔", "explanation_en": "Diptote adjective takes single dammah: Jaw'aanu."
        }
    ]

    # =========================================================================
    # UNIT 23: جمع المذكر السالم وألفاظ العقود
    # =========================================================================
    units[23] = [
        # Tamreen 1: أسئلة الدرس
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
        # Tamreen 2: إعراب جمع المذكر السالم
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
        },
        # Tamreen 3: جمع مذكر سالم في حالة الرفع
        {
            "id": "b2_u23_q3", "book": 2, "unit_num": 23, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): رفع بالواو", "badge_en": "Exercise (2): Nominative with Waw",
            "tamreen_title_ar": "رَفْعُ جَمْعِ الْمُذَكَّرِ السَّالِمِ بِالْوَاوِ:", "tamreen_title_ur": "فاعل ہونے پر جمع مذکر سالم کو واو دینا:", "tamreen_title_en": "Sound masculine plural subject taking Waw:",
            "grammar_goal_ur": "حَضَرَ الْمُهَنْدِسُونَ الْيَوْمَ۔", "grammar_goal_en": "Subject takes waw in sound masculine plural.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "حَضَرَ [ ＿＿＿ ] إِلَى الْمَوْقِعِ .",
            "prompt_ur": "انجینئرز سائٹ پر حاضر ہوئے (فاعل مرفوع بالواو چنیں):", "prompt_en": "The engineers arrived at the site (select subject with Waw):",
            "answer": "الْمُهَنْدِسُونَ",
            "options": ["الْمُهَنْدِسُونَ", "الْمُهَنْدِسِينَ", "الْمُهَنْدِسَانِ", "مُهَنْدِسِينَ"],
            "emoji": "👷‍♂️", "hint_ur": "فاعل حالت رفع میں واو کے ساتھ آتا ہے: الْمُهَنْدِسُونَ۔", "hint_en": "Subject takes waw: Al-Muhandisoona.",
            "explanation_ur": "فاعل مرفوع بالواو ہوتا ہے اس لیے 'الْمُهَنْدِسُونَ' درست ہے۔", "explanation_en": "Subject is Marfoo' with waw: Al-Muhandisoona."
        },
        # Tamreen 4: ألفاظ العقود (20 إلى 90)
        {
            "id": "b2_u23_q4", "book": 2, "unit_num": 23, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): الفاظِ عقود (20 تا 90)", "badge_en": "Exercise (4): Decade Numbers (20-90)",
            "tamreen_title_ar": "إِعْرَابُ أَلْفَاظِ الْعُقُودِ كَجَمْعِ الْمُذَكَّرِ السَّالِمِ:", "tamreen_title_ur": "الفاظ عقود کا جمع مذکر سالم کی طرح اعراب (عشرون / عشرين):", "tamreen_title_en": "Decade numbers decline like sound masculine plural:",
            "grammar_goal_ur": "فِي الْفَصْلِ عِشْرُونَ طَالِباً، وَرَأَيْتُ ثَلَاثِينَ طَالِباً۔", "grammar_goal_en": "Decade numbers take waw in raf' and ya in nasb/jarr.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي الْمَكْتَبَةِ [ ＿＿＿ ] طَالِباً .",
            "prompt_ur": "لائبریری میں تیس طلبہ ہیں (مبتدأ مؤخر مرفوع چنیں):", "prompt_en": "There are 30 students in the library (select nominative):",
            "answer": "ثَلَاثُونَ",
            "options": ["ثَلَاثُونَ", "ثَلَاثِينَ", "ثَلَاثَةَ", "ثَلَاثُ"],
            "emoji": "3️⃣0️⃣", "hint_ur": "حالت رفع میں واو کے ساتھ 'ثَلَاثُونَ' آئے گا۔", "hint_en": "Nominative takes waw: Thalaathoona.",
            "explanation_ur": "مبتدأ ہونے کی وجہ سے الفاظ عقود واو کے ساتھ مرفوع ہوتے ہیں: ثَلَاثُونَ۔", "explanation_en": "Subject is nominative with waw: Thalaathoona."
        }
    ]

    # =========================================================================
    # UNIT 24: الأسماء الخمسة (أبوك، أخوك، حَمُوكَ، فُوكَ، ذُو مَالٍ)
    # =========================================================================
    units[24] = [
        # Tamreen 1: إعراب الأسماء الخمسة بالواو والألف والياء
        {
            "id": "b2_u24_q1", "book": 2, "unit_num": 24, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اسمائے خمسہ (أَبُو)", "badge_en": "Exercise (1): Five Nouns (Abu)",
            "tamreen_title_ar": "إِعْرَابُ الأَسْمَاءِ الْخَمْسَةِ بِالْوَاوِ رَفْعاً، وَبِالأَلِفِ نَصْباً، وَبِالْيَاءِ جَرّاً:", "tamreen_title_ur": "اسمائے خمسہ کا اعراب (رفع میں واو، نصب میں الف، جر میں یاء):", "tamreen_title_en": "Inflection of Five Nouns (Waw for Raf', Alif for Nasb, Ya for Jarr):",
            "grammar_goal_ur": "جَاءَ أَبُوكَ، رَأَيْتُ أَبَاكَ، سَلَّمْتُ عَلَى أَبِيكَ۔", "grammar_goal_en": "Mastering the three cases of Abu with attached pronoun.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "رَأَيْتُ [ ＿＿＿ ] فِي السُّوقِ أَمْسِ .",
            "prompt_ur": "میں نے کل بازار میں تمہارے والد کو دیکھا (مفعول بہ منسوب چنیں):", "prompt_en": "I saw your father in the market yesterday (select accusative):",
            "answer": "أَبَاكَ",
            "options": ["أَبَاكَ", "أَبُوكَ", "أَبِيكَ", "أَبُوكُمْ"],
            "emoji": "👨", "hint_ur": "اسمائے خمسہ حالتِ نصب میں الف کے ساتھ آتے ہیں: أَبَاكَ۔", "hint_en": "Five nouns take alif in accusative case: Abaaka.",
            "explanation_ur": "مفعول بہ منسوب بالالف ہوتا ہے: أَبَاكَ۔", "explanation_en": "Accusative of Five Nouns takes alif: Abaaka."
        },
        # Tamreen 2: أخوك في حالة الرفع
        {
            "id": "b2_u24_q2", "book": 2, "unit_num": 24, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): رفع أخوك بالواو", "badge_en": "Exercise (2): Akhooke in Nominative",
            "tamreen_title_ar": "رَفْعُ (أَخُوكَ) بِالْوَاوِ عِنْدَمَا يَكُونُ فَاعِلاً أَوْ مُبْتَدَأً:", "tamreen_title_ur": "أخوك کا واو کے ساتھ مرفوع ہونا:", "tamreen_title_en": "Ahooka nominative with waw as subject:",
            "grammar_goal_ur": "أَيْنَ ذَهَبَ أَخُوكَ يَا عَلِيُّ؟", "grammar_goal_en": "Using Akhooka with waw as subject.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ ذَهَبَ [ ＿＿＿ ] الْيَوْمَ يَا حَامِدُ؟",
            "prompt_ur": "اے حامد، تمہارا بھائی آج کہاں گیا؟ (فاعل مرفوع چنیں):", "prompt_en": "Where did your brother go, Hamid? (select subject):",
            "answer": "أَخُوكَ",
            "options": ["أَخُوكَ", "أَخَاكَ", "أَخِيكَ", "أَخٌ لَكَ"],
            "emoji": "👦", "hint_ur": "فاعل حالت رفع میں واو کے ساتھ آتا ہے: أَخُوكَ۔", "hint_en": "Subject takes waw: Akhooka.",
            "explanation_ur": "فاعل مرفوع بالواو ہوتا ہے: ذَهَبَ أَخُوكَ۔", "explanation_en": "Subject takes waw in five nouns: Akhooka."
        },
        # Tamreen 3: ذو بمعنى صاحب
        {
            "id": "b2_u24_q3", "book": 2, "unit_num": 24, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): ذُو (والا)", "badge_en": "Exercise (3): Dhu (Possessor of)",
            "tamreen_title_ar": "اسْتِعْمَالُ (ذُو) بِمَعْنَى صَاحِبٍ وَإِعْرَابُهَا:", "tamreen_title_ur": "ذو کا استعمال اور اس کے بعد مضاف الیہ مجرور ہونا:", "tamreen_title_en": "Using Dhu meaning 'possessor of' + genitive noun:",
            "grammar_goal_ur": "هٰذَا رَجُلٌ ذُو خُلُقٍ حَسَنٍ۔", "grammar_goal_en": "Using Dhu as adjective meaning possessor of.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مُدِيرُنَا رَجُلٌ [ ＿＿＿ ] خُلُقٍ فَاضِلٍ .",
            "prompt_ur": "ہمارے پرنسپل اچھے اخلاق والے آدمی ہیں (ذو، ذا، ذی چنیں):", "prompt_en": "Our principal is a man of noble character (select Dhu):",
            "answer": "ذُو",
            "options": ["ذُو", "ذَا", "ذِي", "ذَوُو"],
            "emoji": "🌟", "hint_ur": "صفت مرفوع ہونے کی وجہ سے واو کے ساتھ آئے گی: ذُو۔", "hint_en": "Adjective agrees with marfoo' noun: Dhu.",
            "explanation_ur": "رجلٌ مرفوع ہے اس لیے اس کی صفت واو کے ساتھ 'ذُو' آئے گی۔", "explanation_en": "Matches nominative rajulun: Dhu."
        },
        # Tamreen 4: فوك وحموك
        {
            "id": "b2_u24_q4", "book": 2, "unit_num": 24, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): فُوكَ اور حَمُوكَ", "badge_en": "Exercise (4): Fooka and Hamooka",
            "tamreen_title_ar": "إِعْرَابُ (فَم) عِنْدَ إِضَافَتِهِ (فُوكَ، فَاكَ، فِيكَ):", "tamreen_title_ur": "منہ (فَم) کا اضافہ ہونے پر اسمائے خمسہ میں شمار ہونا:", "tamreen_title_en": "Mouth (Fam) inflecting as five noun when added to pronoun:",
            "grammar_goal_ur": "اغْسِلْ فَاكَ بِالْمَاءِ وَالصَّابُونِ۔", "grammar_goal_en": "Wash your mouth (Faaka in accusative).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "افْتَحْ [ ＿＿＿ ] عِنْدَ الطَّبِيبِ .",
            "prompt_ur": "ڈاکٹر کے سامنے اپنا منہ کھولو (مفعول بہ منسوب چنیں):", "prompt_en": "Open your mouth in front of doctor (select accusative):",
            "answer": "فَاكَ",
            "options": ["فَاكَ", "فُوكَ", "فِيكَ", "فَمُكَ"],
            "emoji": "👄", "hint_ur": "امر کے بعد مفعول بہ الف کے ساتھ منسوب ہوگا: فَاكَ۔", "hint_en": "Direct object takes alif: Faaka.",
            "explanation_ur": "مفعول بہ منسوب بالالف ہے: فَاكَ۔", "explanation_en": "Accusative of Dhu/Fam takes alif: Faaka."
        }
    ]

    # =========================================================================
    # UNIT 25: كان وأخواتها (لا يَزَالُ) ونفيها
    # =========================================================================
    units[25] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u25_q1", "book": 2, "unit_num": 25, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَيْفَ كَانَ الْجَوُّ فِي الرِّيَاضِ أَمْسِ؟ [ ＿＿＿ ]",
            "prompt_ur": "کل ریاض میں موسم کیسا تھا؟", "prompt_en": "How was the weather in Riyadh yesterday?",
            "answer": "كَانَ الْجَوُّ حَارّاً جِدّاً .",
            "options": ["كَانَ الْجَوُّ حَارّاً جِدّاً .", "كَانَ الْجَوُّ بَارِداً .", "كَانَ الْجَوُّ مُمْطِراً .", "كَانَ الْجَوُّ مُعْتَدِلاً ."],
            "emoji": "☀️", "hint_ur": "موسم بہت گرم تھا۔", "hint_en": "The weather was very hot.",
            "explanation_ur": "درست جواب: 'كَانَ الْجَوُّ حَارّاً جِدّاً .'۔", "explanation_en": "Correct answer: weather was very hot."
        },
        # Tamreen 2: دخول كان ونصب الخبر
        {
            "id": "b2_u25_q2", "book": 2, "unit_num": 25, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): كان کا عمل", "badge_en": "Exercise (2): Syntax of Kaana",
            "tamreen_title_ar": "تَغْيِيرُ إِعْرَابِ الْخَبَرِ بَعْدَ (كَانَ):", "tamreen_title_ur": "کان کے بعد خبر کا مرفوع سے منسوب ہونا:", "tamreen_title_en": "Predicate becoming accusative after Kaana:",
            "grammar_goal_ur": "الْهَاتِفُ مَشْغُولٌ -> كَانَ الْهَاتِفُ مَشْغُولاً۔", "grammar_goal_en": "Transforming predicate from nominative to accusative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْهَاتِفُ مَشْغُولٌ ➔ كَانَ الْهَاتِفُ [ ＿＿＿ ] .",
            "prompt_ur": "کان داخل ہونے پر 'مشغول' کا اعراب چنیں:", "prompt_en": "Select the case of Mashghool after Kaana:",
            "answer": "مَشْغُولاً",
            "options": ["مَشْغُولاً", "مَشْغُولٌ", "مَشْغُولٍ", "الْمَشْغُولُ"],
            "emoji": "📞", "hint_ur": "کان کی خبر منسوب ہوتی ہے: مَشْغُولاً۔", "hint_en": "Predicate of Kaana is Mansub: Mashghoolan.",
            "explanation_ur": "کان اپنے اسم کو رفع اور خبر کو نصب دیتی ہے: مَشْغُولاً۔", "explanation_en": "Kaana makes predicate accusative: Mashghoolan."
        },
        # Tamreen 3: لا يَزَالُ واستمرار الفعل
        {
            "id": "b2_u25_q3", "book": 2, "unit_num": 25, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): لَا يَزَالُ (ابھی تک)", "badge_en": "Exercise (3): Laa Yazaalu (Still)",
            "tamreen_title_ar": "عَمَلُ (لَا يَزَالُ) مِنْ أَخَوَاتِ كَانَ لِاسْتِمْرَارِ الْحَالِ:", "tamreen_title_ur": "کان کی بہن 'لا يَزَالُ' کا عمل (ابھی تک):", "tamreen_title_en": "Syntax of Laa Yazaalu expressing ongoing state:",
            "grammar_goal_ur": "لَا يَزَالُ حَامِدٌ مَرِيضاً (حامد اب بھی بیمار ہے)۔", "grammar_goal_en": "Using Laa Yazaalu + accusative predicate.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَحَامِدٌ مَرِيضٌ؟ نَعَمْ، لَا يَزَالُ [ ＿＿＿ ] .",
            "prompt_ur": "ہاں وہ اب بھی بیمار ہے (لا يزال کی خبر منسوب چنیں):", "prompt_en": "Yes, he is still sick (select accusative predicate):",
            "answer": "مَرِيضاً",
            "options": ["مَرِيضاً", "مَرِيضٌ", "مَرِيضٍ", "الْمَرِيضُ"],
            "emoji": "🤒", "hint_ur": "لا يزال کی خبر منسوب ہوتی ہے: مَرِيضاً۔", "hint_en": "Predicate of La Yazaalu takes fathatan: Maredan.",
            "explanation_ur": "لا يزال کان کی طرح عمل کرتی ہے اس لیے 'مَرِيضاً' منسوب ہے۔", "explanation_en": "La Yazaalu acts like Kaana, governing accusative: Maredan."
        },
        # Tamreen 4: نفي كان بـ ما
        {
            "id": "b2_u25_q4", "book": 2, "unit_num": 25, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): مَا كَانَ (نفی)", "badge_en": "Exercise (4): Negation of Kaana",
            "tamreen_title_ar": "نَفْيُ الْجُمْلَةِ بـ (مَا كَانَ):", "tamreen_title_ur": "ماضی کی نفی کے لیے 'مَا كَانَ' کا استعمال:", "tamreen_title_en": "Negating past nominal sentence with 'Maa Kaana':",
            "grammar_goal_ur": "مَا كَانَ الدَّرْسُ صَعْباً (سبق مشکل نہیں تھا)۔", "grammar_goal_en": "Maa Kaana followed by nominative subject and accusative predicate.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَكَانَ الامْتِحَانُ صَعْباً؟ لَا، مَا كَانَ الامْتِحَانُ [ ＿＿＿ ] .",
            "prompt_ur": "نہیں، امتحان مشکل نہیں تھا:", "prompt_en": "No, the exam was not difficult:",
            "answer": "صَعْباً",
            "options": ["صَعْباً", "صَعْبٌ", "صَعْبٍ", "الصَّعْبُ"],
            "emoji": "📝", "hint_ur": "مَا كَانَ کی خبر بھی منسوب ہوتی ہے: صَعْباً۔", "hint_en": "Predicate of Maa Kaana is Mansub: Sa'ban.",
            "explanation_ur": "نفی کے باوجود کان کی خبر منسوب ہی رہتی ہے: صَعْباً۔", "explanation_en": "Negative Kaana still governs accusative: Sa'ban."
        }
    ]

    # =========================================================================
    # UNIT 26: الفعل المثال الواوي والتصغير
    # =========================================================================
    units[26] = [
        # Tamreen 1 & 2: مضارع الفعل المثال (وقف -> يقف)
        {
            "id": "b2_u26_q1", "book": 2, "unit_num": 26, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مثال واوی کا مضارع", "badge_en": "Exercise (2): Present of Mithal Verbs",
            "tamreen_title_ar": "حَذْفُ الْوَاوِ فِي مُضَارِعِ الْفِعْلِ الْمِثَالِ (وَصَلَ يَصِلُ):", "tamreen_title_ur": "مثال واوی کے مضارع میں واو کا گرنا:", "tamreen_title_en": "Dropping root Waw in present tense of Mithal verbs:",
            "grammar_goal_ur": "وَقَفَ يَقِفُ، وَعَدَ يَعِدُ، وَضَعَ يَضَعُ۔", "grammar_goal_en": "Recognizing dropped waw in Mithal present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مُضَارِعُ الْفِعْلِ (وَقَفَ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "وقف کا مضارع منتخب کریں:", "prompt_en": "Select the present tense of 'Waqafa':",
            "answer": "يَقِفُ (أَصْلُهُ: يَوْقِفُ)",
            "options": ["يَقِفُ (أَصْلُهُ: يَوْقِفُ)", "يَوْقِفُ", "يُوقِفُ", "تَوْقَفُ"],
            "emoji": "🛑", "hint_ur": "مثال واوی کے مضارع میں واو حذف ہو جاتی ہے: يَقِفُ۔", "hint_en": "Waw is dropped in present: Yaqifu.",
            "explanation_ur": "واو علامت مضارعت اور کسرہ کے درمیان گر جاتی ہے: يَقِفُ۔", "explanation_en": "Waw drops between ya and kasrah: Yaqifu."
        },
        # Tamreen 3: أمر الفعل المثال (قِفْ)
        {
            "id": "b2_u26_q2", "book": 2, "unit_num": 26, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): امرِ مثال واوی (قِفْ)", "badge_en": "Exercise (3): Imperative of Mithal Verbs",
            "tamreen_title_ar": "صَوْغُ الأَمْرِ مِنَ الْفِعْلِ الْمِثَالِ (قِفْ، عِدْ، ضَعْ):", "tamreen_title_ur": "مثال واوی سے امر بنانا (قِفْ، ضَعْ):", "tamreen_title_en": "Forming imperative of Mithal verbs:",
            "grammar_goal_ur": "تَقِفُ سے قِفْ اور تَضَعُ سے ضَعْ بنانا۔", "grammar_goal_en": "Deriving imperative by dropping present prefix: Qif.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الأَمْرُ مِنْ (وَضَعَ يَضَعُ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "وَضَعَ يَضَعُ کا امر چنیں (رکھو!):", "prompt_en": "Select the imperative of Wada'a (Put!):",
            "answer": "ضَعْ",
            "options": ["ضَعْ", "اوْضَعْ", "اِضَعْ", "تَضَعْ"],
            "emoji": "📦", "hint_ur": "مثال کا امر بغیر ہمزہ کے بنتا ہے: ضَعْ۔", "hint_en": "Mithal imperative needs no hamzah: Da'.",
            "explanation_ur": "علامت مضارع ہٹانے کے بعد حرف متحرک ہے اس لیے ہمزہ کی ضرورت نہیں: ضَعْ۔", "explanation_en": "First letter is voweled, no hamzatul wasl needed: Da'."
        },
        # Tamreen 5 & 6: اسم التصغير (فُعَيْل)
        {
            "id": "b2_u26_q3", "book": 2, "unit_num": 26, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): اسمِ تصغیر (فُعَيْل)", "badge_en": "Exercise (6): Diminutive Nouns (Fu'ayl)",
            "tamreen_title_ar": "صَوْغُ التَّصْغِيرِ عَلَى وَزْنِ (فُعَيْل):", "tamreen_title_ur": "اسمِ تصغیر کا وزن 'فُعَيْل' (نُهَيْر، جُبَيْل):", "tamreen_title_en": "Forming diminutive on pattern Fu'ayl:",
            "grammar_goal_ur": "نَهْرٌ -> نُهَيْرٌ (چھوٹی نہر) اور جَبَلٌ -> جُبَيْلٌ (چھوٹا پہاڑ)۔", "grammar_goal_en": "Forming diminutive pattern Fu'ayl.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "تَصْغِيرُ كَلِمَةِ (نَهْرٌ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "نہر (دریا) کا اسم تصغیر منتخب کریں:", "prompt_en": "Select the diminutive of 'Nahr' (small stream):",
            "answer": "نُهَيْرٌ",
            "options": ["نُهَيْرٌ", "نَهِيرٌ", "نُهَارٌ", "أَنْهَارٌ"],
            "emoji": "🏞️", "hint_ur": "فُعَيْل کے وزن پر 'نُهَيْرٌ' بنے گا۔", "hint_en": "On pattern Fu'ayl: Nuhayr.",
            "explanation_ur": "ثلاثی اسم کا تصغیر فُعَيْل کے وزن پر آتا ہے: نُهَيْرٌ۔", "explanation_en": "Diminutive of 3-letter noun is Fu'ayl: Nuhayr."
        },
        # Tamreen 10: يجب عليك أن تفعل
        {
            "id": "b2_u26_q4", "book": 2, "unit_num": 26, "tamreen_num": 10,
            "badge_ar": "التَّمْرِينُ (10)", "badge_ur": "مشق (10): يَجِبُ عَلَيْكَ أَنْ", "badge_en": "Exercise (10): Obligation (Yajibu 'Alayka An)",
            "tamreen_title_ar": "اسْتِعْمَالُ التَّعْبِيرِ (يَجِبُ عَلَى ... أَنْ ...):", "tamreen_title_ur": "وجوب کے لیے 'یجب علیک أن' کا استعمال:", "tamreen_title_en": "Expressing obligation with Yajibu 'Ala + An + verb:",
            "grammar_goal_ur": "يَجِبُ عَلَيْكَ أَنْ تَذْهَبَ إِلَى الطَّبِيبِ۔", "grammar_goal_en": "Using Yajibu 'ala to express 'must/ought to'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنْتَ مَرِيضٌ، [ ＿＿＿ ] أَنْ تَذْهَبَ إِلَى الْمُسْتَشْفَى .",
            "prompt_ur": "تم بیمار ہو، تم پر ہسپتال جانا واجب ہے:", "prompt_en": "You are sick, you must go to hospital:",
            "answer": "يَجِبُ عَلَيْكَ",
            "options": ["يَجِبُ عَلَيْكَ", "يَجُوزُ لَكَ", "تُرِيدُ مِنْكَ", "حَرَامٌ عَلَيْكَ"],
            "emoji": "🏥", "hint_ur": "وجوب کے لیے 'يَجِبُ عَلَيْكَ' آتا ہے۔", "hint_en": "Expression of necessity: Yajibu 'alayka.",
            "explanation_ur": "عربی میں فرض یا لازمی کام کے لیے 'يَجِبُ عَلَى' استعمال ہوتا ہے۔", "explanation_en": "Yajibu 'ala indicates necessity/obligation."
        }
    ]

    # =========================================================================
    # UNIT 27: الفعل الأجوف وتصريفه (قال، زار، كان، باع، سار، خاف)
    # =========================================================================
    units[27] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u27_q1", "book": 2, "unit_num": 27, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "فعل اجوف کے مکالمے کا فہم۔", "grammar_goal_en": "Hollow verb dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَتَى قَامَ حَامِدٌ مِنْ نَوْمِهِ؟ [ ＿＿＿ ]",
            "prompt_ur": "حامد اپنی نیند سے کب بیدار ہوا؟", "prompt_en": "When did Hamid wake up from sleep?",
            "answer": "قَامَ قَبْلَ أَذَانِ الْفَجْرِ .",
            "options": ["قَامَ قَبْلَ أَذَانِ الْفَجْرِ .", "قَامَ بَعْدَ شُرُوقِ الشَّمْسِ .", "قَامَ فِي الظُّهْرِ .", "مَا قَامَ حَتَّى الآنَ ."],
            "emoji": "⏰", "hint_ur": "وہ فجر کی اذان سے پہلے بیدار ہوا۔", "hint_en": "He woke up before Fajr adhan.",
            "explanation_ur": "درست جواب: 'قَامَ قَبْلَ أَذَانِ الْفَجْرِ .'۔", "explanation_en": "Correct answer: before Fajr adhan."
        },
        # Tamreen 3 & 4: إسناد الأجوف للضمائر في الماضي (قَالَ -> قُلْتُ)
        {
            "id": "b2_u27_q2", "book": 2, "unit_num": 27, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): إسناد الأجوف للتاء (قُلْتُ)", "badge_en": "Exercise (4): Hollow Past with Taa (Qultu)",
            "tamreen_title_ar": "حَذْفُ عَيْنِ الأَجْوَفِ عِنْدَ اتِّصَالِهِ بِتَاءِ الْفَاعِلِ:", "tamreen_title_ur": "تائے فاعل سے ملنے پر اجوف کے بیچ کا حرف علت گرنا:", "tamreen_title_en": "Dropping middle vowel when attaching subject pronoun:",
            "grammar_goal_ur": "قَالَ -> قُلْتُ، زَارَ -> زُرْتُ، كَانَ -> كُنْتُ۔", "grammar_goal_en": "Dropping middle weak letter to avoid two sukoons.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] الْحَقَّ دَائِماً .",
            "prompt_ur": "میں نے ہمیشہ سچ کہا (فعل قال کو ضمیر أنا کے ساتھ جوڑیں):", "prompt_en": "I always said the truth (conjugate Qaala with Ana):",
            "answer": "قُلْتُ",
            "options": ["قُلْتُ", "قَالْتُ", "قَوْلْتُ", "قِيلْتُ"],
            "emoji": "🗣️", "hint_ur": "اجتماع ساکنین کی وجہ سے الف گر کر 'قُلْتُ' بنتا ہے۔", "hint_en": "Alif drops: Qultu.",
            "explanation_ur": "قال کا عین کلمہ متحرک ضمیر ملنے پر حذف ہو جاتا ہے: قُلْتُ۔", "explanation_en": "Middle vowel drops with consonant suffix: Qultu."
        },
        # Tamreen 6 & 7: مضارع الأجوف (يَقُولُ، يَبِيعُ، يَخَافُ)
        {
            "id": "b2_u27_q3", "book": 2, "unit_num": 27, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): اجوف یائی کا ماضی و مضارع", "badge_en": "Exercise (6): Hollow Yaa'ee (Baa'a / Yabee'u)",
            "tamreen_title_ar": "تَصْرِيفُ الأَجْوَفِ الْيَائِيِّ (بَاعَ يَبِيعُ -> بِعْتُ):", "tamreen_title_ur": "باع یبیع کی تصریف (أنا بِعْتُ):", "tamreen_title_en": "Conjugating hollow ya root (Baa'a / Yabee'u -> Bi'tu):",
            "grammar_goal_ur": "بَاعَ سے بِعْتُ (کسرہ کے ساتھ)۔", "grammar_goal_en": "Taking kasrah in past tense for hollow verbs of ya root.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] سَيَّارَتِي الْقَدِيمَةَ أَمْسِ .",
            "prompt_ur": "میں نے کل اپنی پرانی گاڑی بیچی:", "prompt_en": "I sold my old car yesterday:",
            "answer": "بِعْتُ (بِكَسْرِ الْبَاءِ)",
            "options": ["بِعْتُ (بِكَسْرِ الْبَاءِ)", "بُعْتُ", "بَاعْتُ", "بَيَعْتُ"],
            "emoji": "🚙", "hint_ur": "یائی اجوف میں باء پر زیر آتی ہے: بِعْتُ۔", "hint_en": "Yaa root takes kasrah on first letter: Bi'tu.",
            "explanation_ur": "کیونکہ مضارع یَبِيعُ ہے اس لیے ماضی میں کسرہ آئے گی: بِعْتُ۔", "explanation_en": "Because present has yaa (Yabee'u), past takes kasrah: Bi'tu."
        },
        # Tamreen 10 & 11: جزم الأجوف بـ لم (لَمْ يَقُلْ)
        {
            "id": "b2_u27_q4", "book": 2, "unit_num": 27, "tamreen_num": 10,
            "badge_ar": "التَّمْرِينُ (10)", "badge_ur": "مشق (10): جزمِ اجوف بـ لم", "badge_en": "Exercise (10): Jussive Hollow Verb",
            "tamreen_title_ar": "حَذْفُ حَرْفِ الْعِلَّةِ فِي جَزْمِ الأَجْوَفِ (لَمْ يَقُلْ):", "tamreen_title_ur": "جزم کی حالت میں اجوف کا حرف علت گرنا:", "tamreen_title_en": "Dropping weak letter in jussive hollow verb:",
            "grammar_goal_ur": "يَقُولُ -> لَمْ يَقُلْ، يَبِيعُ -> لَمْ يَبِعْ۔", "grammar_goal_en": "Dropping long vowel when last letter gets sukoon.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عَلِيٌّ [ ＿＿＿ ] شَيْئاً أَمْسِ .",
            "prompt_ur": "علی نے کل کچھ نہیں کہا (فعل مجزوم چنیں):", "prompt_en": "Ali said nothing yesterday (select jussive):",
            "answer": "لَمْ يَقُلْ",
            "options": ["لَمْ يَقُلْ", "لَمْ يَقُولْ", "لَا يَقُولُ", "مَا قَالَ"],
            "emoji": "🤫", "hint_ur": "جزم میں واو گر جائے گی: لَمْ يَقُلْ۔", "hint_en": "Waw drops in jussive: Lam yaqul.",
            "explanation_ur": "لام پر سکون آنے کی وجہ سے واو گر جاتی ہے: لَمْ يَقُلْ۔", "explanation_en": "Long vowel drops before final sukoon: Lam yaqul."
        },
        # Tamreen 13: أمر الأجوف (قُلْ، بِعْ، خَفْ)
        {
            "id": "b2_u27_q5", "book": 2, "unit_num": 27, "tamreen_num": 13,
            "badge_ar": "التَّمْرِينُ (13)", "badge_ur": "مشق (13): امرِ اجوف (قُلْ)", "badge_en": "Exercise (13): Imperative of Hollow Verb",
            "tamreen_title_ar": "صَوْغُ الأَمْرِ مِنَ الأَجْوَفِ (قُلْ، زُرْ، قُمْ):", "tamreen_title_ur": "فعل اجوف سے امر کا صیغہ بنانا:", "tamreen_title_en": "Forming imperative of hollow verbs:",
            "grammar_goal_ur": "تَقُولُ سے قُلْ اور تَقُومُ سے قُمْ بنانا۔", "grammar_goal_en": "Dropping middle vowel in imperative: Qul.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الأَمْرُ مِنْ (قَالَ يَقُولُ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "قال یقول کا امر منتخب کریں (کہو!):", "prompt_en": "Select the imperative of Qaala (Say!):",
            "answer": "قُلْ",
            "options": ["قُلْ", "قُولْ", "اقُولْ", "اقْلْ"],
            "emoji": "🗣️", "hint_ur": "حرف علت گر جائے گا: قُلْ۔", "hint_en": "Weak vowel drops: Qul.",
            "explanation_ur": "امر کے آخر میں سکون کی وجہ سے واو گر جاتی ہے: قُلْ۔", "explanation_en": "Waw drops to avoid two consecutive sukoons: Qul."
        }
    ]

    # =========================================================================
    # UNIT 28: الفعل الناقص وتصريفه (دعا، مشى، قضى، نسي)
    # =========================================================================
    units[28] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u28_q1", "book": 2, "unit_num": 28, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "فعل ناقص کا فہم۔", "grammar_goal_en": "Defective verb facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "إِلَى مَاذَا دَعَا الْمُدَرِّسُ طُلَّابَهُ؟ [ ＿＿＿ ]",
            "prompt_ur": "استاد نے اپنے طلبہ کو کس چیز کی طرف دعوت دی؟", "prompt_en": "To what did the teacher invite his students?",
            "answer": "دَعَاهُمْ إِلَى مَنْزِلِهِ لِتَنَاوُلِ الشَّايِ .",
            "options": ["دَعَاهُمْ إِلَى مَنْزِلِهِ لِتَنَاوُلِ الشَّايِ .", "دَعَاهُمْ إِلَى الْمَطْعَمِ .", "دَعَاهُمْ إِلَى رِحْلَةٍ .", "دَعَاهُمْ لِحِفْظِ الْقُرْآنِ ."],
            "emoji": "☕", "hint_ur": "انہوں نے اپنے گھر چائے کی دعوت دی۔", "hint_en": "He invited them to his home for tea.",
            "explanation_ur": "درست جواب: 'دَعَاهُمْ إِلَى مَنْزِلِهِ لِتَنَاوُلِ الشَّايِ .'۔", "explanation_en": "Correct answer: invited to his house for tea."
        },
        # Tamreen 2 & 3: مضارع الفعل الناقص (دعا يدعو / مشى يمشي)
        {
            "id": "b2_u28_q2", "book": 2, "unit_num": 28, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مضارع ناقص (دَعَا يَدْعُو)", "badge_en": "Exercise (3): Present of Defective Verb",
            "tamreen_title_ar": "تَصْرِيفُ مُضَارِعِ الْفِعْلِ النَّاقِصِ (دَعَا يَدْعُو):", "tamreen_title_ur": "ناقص واوی کا مضارع (دَعَا -> يَدْعُو):", "tamreen_title_en": "Present tense of defective verb (Da'aa -> Yad'oo):",
            "grammar_goal_ur": "دَعَا کا مضارع يَدْعُو اور مَشَى کا مضارع يَمْشِي۔", "grammar_goal_en": "Recognizing weak endings in present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمُؤْمِنُ [ ＿＿＿ ] رَبَّهُ فِي كُلِّ وَقْتٍ .",
            "prompt_ur": "مومن ہر وقت اپنے رب کو پکارتا ہے (دعا کا مضارع چنیں):", "prompt_en": "The believer calls upon his Lord at all times:",
            "answer": "يَدْعُو",
            "options": ["يَدْعُو", "يَدْعَى", "يَدْعِي", "يَدْعُ"],
            "emoji": "🤲", "hint_ur": "دَعَا کا مضارع 'يَدْعُو' ہے۔", "hint_en": "Present of Da'aa is Yad'oo.",
            "explanation_ur": "الف ممدودہ واو میں بدل جاتی ہے: يَدْعُو۔", "explanation_en": "Root waw surfaces in present: Yad'oo."
        },
        # Tamreen 7: ماضي الناقص مع تاء الفاعل (مَشَيْتُ، دَعَوْتُ)
        {
            "id": "b2_u28_q3", "book": 2, "unit_num": 28, "tamreen_num": 7,
            "badge_ar": "التَّمْرِينُ (7)", "badge_ur": "مشق (7): ماضی ناقص مع التاء (مَشَيْتُ)", "badge_en": "Exercise (7): Past Defective with Taa",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ النَّاقِصِ إِلَى تَاءِ الْفَاعِلِ (مَشَيْتُ):", "tamreen_title_ur": "تائے فاعل سے ملنے پر الف مقصورہ کا یاء میں بدلنا:", "tamreen_title_en": "Alif turning to Yaa with subject pronoun (Mashaytu):",
            "grammar_goal_ur": "مَشَى -> مَشَيْتُ، قَضَى -> قَضَيْتُ۔", "grammar_goal_en": "Root letter reappears before consonant suffix.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] كِيلُومِتْرَيْنِ هٰذَا الصَّبَاحَ .",
            "prompt_ur": "میں آج صبح دو کلومیٹر چلا (مَشَى کو أنا کے ساتھ جوڑیں):", "prompt_en": "I walked two kilometers this morning (conjugate Mashaa with Ana):",
            "answer": "مَشَيْتُ",
            "options": ["مَشَيْتُ", "مَشَوْتُ", "مَشَاتُ", "مَشَيْتَ"],
            "emoji": "🚶", "hint_ur": "مَشَى کی اصل یاء ظاہر ہو جائے گی: مَشَيْتُ۔", "hint_en": "Yaa reappears: Mashaytu.",
            "explanation_ur": "الف مقصورہ تاء فاعل ملنے پر یاء میں بدل جاتی ہے: مَشَيْتُ۔", "explanation_en": "Weak ending becomes yaa: Mashaytu."
        },
        # Tamreen 8: جزم الناقص بحذف حرف العلة (لَمْ يَدْعُ / لَمْ يَمْشِ)
        {
            "id": "b2_u28_q4", "book": 2, "unit_num": 28, "tamreen_num": 8,
            "badge_ar": "التَّمْرِينُ (8)", "badge_ur": "مشق (8): جزمِ ناقص بحذف حرف العلہ", "badge_en": "Exercise (8): Jussive by Dropping Weak Letter",
            "tamreen_title_ar": "جَزْمُ الْفِعْلِ النَّاقِصِ بِحَذْفِ حَرْفِ الْعِلَّةِ (لَمْ يَدْعُ / لَمْ يَمْشِ):", "tamreen_title_ur": "ناقص کا حرفِ علت گرا کر مجزوم ہونا:", "tamreen_title_en": "Jussive case of defective verb by dropping final weak letter:",
            "grammar_goal_ur": "يَدْعُو -> لَمْ يَدْعُ، يَمْشِي -> لَمْ يَمْشِ، يَنْسَى -> لَمْ يَنْسَ۔", "grammar_goal_en": "Jussive marker is dropping final vowel letter.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "حَامِدٌ [ ＿＿＿ ] وَاجِبَهُ أَمْسِ .",
            "prompt_ur": "حامد کل اپنا ہوم ورک نہیں بھولا (نَسِيَ يَنسَى کا مجزوم صیغہ چنیں):", "prompt_en": "Hamid did not forget his homework yesterday (select jussive):",
            "answer": "لَمْ يَنْسَ (بِحَذْفِ الأَلِفِ)",
            "options": ["لَمْ يَنْسَ (بِحَذْفِ الأَلِفِ)", "لَمْ يَنْسَى", "لَا يَنْسَى", "مَا نَسِيَ"],
            "emoji": "🧠", "hint_ur": "جزم میں الف گر جائے گی اور صرف فتحہ باقی رہے گا: لَمْ يَنْسَ۔", "hint_en": "Alif drops in jussive: Lam Yansa.",
            "explanation_ur": "ناقص کی علامت جزم حرف علت کا حذف ہونا ہے: لَمْ يَنْسَ۔", "explanation_en": "Jussive drops final weak letter: Lam Yansa."
        },
        # Tamreen 20: أمر الفعل الناقص (ادْعُ، امْشِ، انْسَ)
        {
            "id": "b2_u28_q5", "book": 2, "unit_num": 28, "tamreen_num": 20,
            "badge_ar": "التَّمْرِينُ (20)", "badge_ur": "مشق (20): امرِ ناقص (ادْعُ، امْشِ)", "badge_en": "Exercise (20): Imperative of Defective Verb",
            "tamreen_title_ar": "صَوْغُ الأَمْرِ مِنَ الْفِعْلِ النَّاقِصِ بِحَذْفِ الآخِرِ:", "tamreen_title_ur": "ناقص سے امر بناتے وقت آخری حرفِ علت گرانا:", "tamreen_title_en": "Forming imperative of defective verbs by dropping final vowel:",
            "grammar_goal_ur": "قَالَ تَعَالَى: { ادْعُ إِلَى سَبِيلِ رَبِّكَ بِالْحِكْمَةِ }۔", "grammar_goal_en": "Dropping waw/yaa/alif in imperative: Ud'u, Imshi.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَالَ تَعَالَى: { [ ＿＿＿ ] إِلَى سَبِيلِ رَبِّكَ بِالْحِكْمَةِ } .",
            "prompt_ur": "قرآنی آیت میں دعوت دینے کا امر منتخب کریں:", "prompt_en": "Select the imperative verb in the Quranic verse:",
            "answer": "ادْعُ",
            "options": ["ادْعُ", "ادْعُو", "اِدْعِ", "دْعُو"],
            "emoji": "📖", "hint_ur": "امر میں واو گر کر صرف پیش رہ جاتی ہے: ادْعُ۔", "hint_en": "Waw drops, leaving dammah: Ud'u.",
            "explanation_ur": "فعل ناقص کا امر حرف علت کے گرنے سے بنتا ہے: ادْعُ۔", "explanation_en": "Imperative of defective drops weak ending: Ud'u."
        }
    ]

    # =========================================================================
    # UNIT 29: الفعل المضعف وفك الإدغام (حجّ، مرّ، عدّ، ردّ، ظنّ)
    # =========================================================================
    units[29] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u29_q1", "book": 2, "unit_num": 29, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "فعل مضعف کا فہم۔", "grammar_goal_en": "Doubled verb facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَمْ مَرَّةً حَجَّ الْمُدَرِّسُ؟ [ ＿＿＿ ]",
            "prompt_ur": "استاد نے کتنی بار حج کیا؟", "prompt_en": "How many times did the teacher perform Hajj?",
            "answer": "حَجَّ مَرَّتَيْنِ اثْنَتَيْنِ .",
            "options": ["حَجَّ مَرَّتَيْنِ اثْنَتَيْنِ .", "حَجَّ مَرَّةً وَاحِدَةً .", "حَجَّ ثَلَاثَ مَرَّاتٍ .", "مَا حَجَّ قَطُّ ."],
            "emoji": "🕋", "hint_ur": "انہوں نے دو بار حج کیا۔", "hint_en": "He performed Hajj two times.",
            "explanation_ur": "درست جواب: 'حَجَّ مَرَّتَيْنِ اثْنَتَيْنِ .'۔", "explanation_en": "Correct answer: two times."
        },
        # Tamreen 4: فك الإدغام مع تاء الفاعل (حَجَجْتُ، مَرَرْتُ)
        {
            "id": "b2_u29_q2", "book": 2, "unit_num": 29, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): فکِّ ادغام (حَجَجْتُ)", "badge_en": "Exercise (4): Un-gemination (Hajajtu)",
            "tamreen_title_ar": "فَكُّ الإِدْغَامِ فِي الْمُضَعَّفِ عِنْدَ إِسْنَادِهِ لِتَاءِ الْفَاعِلِ:", "tamreen_title_ur": "تائے فاعل سے ملنے پر تشدید کا کھل جانا (فکِ ادغام):", "tamreen_title_en": "Un-gemination when attaching subject pronoun to doubled verb:",
            "grammar_goal_ur": "حَجَّ -> حَجَجْتُ، مَرَّ -> مَرَرْتُ، عَدَّ -> عَدَدْتُ۔", "grammar_goal_en": "Doubled letters separate when joined to personal pronoun.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] هٰذَا الْعَامَ بِفَضْلِ اللَّهِ .",
            "prompt_ur": "میں نے اس سال اللہ کے فضل سے حج کیا (حَجَّ کو أنا کے ساتھ جوڑیں):", "prompt_en": "I performed Hajj this year (conjugate Hajja with Ana):",
            "answer": "حَجَجْتُ",
            "options": ["حَجَجْتُ", "حَجَّيْتُ", "حَجْتُ", "حَجَّتُ"],
            "emoji": "🕋", "hint_ur": "تشدید کھل جائے گی اور دو جیم ظاہر ہوں گے: حَجَجْتُ۔", "hint_en": "Gemination unbinds: Hajajtu.",
            "explanation_ur": "ضمیر متکلم ملنے پر ادغام کھل جاتا ہے: حَجَجْتُ۔", "explanation_en": "Takes un-geminated form with personal pronoun: Hajajtu."
        },
        # Tamreen 5: أمر الفعل المضعف (حُجَّ / اُحْجُجْ)
        {
            "id": "b2_u29_q3", "book": 2, "unit_num": 29, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): امرِ مضعف (عُدَّ / مُرَّ)", "badge_en": "Exercise (5): Imperative of Doubled Verb",
            "tamreen_title_ar": "صَوْغُ الأَمْرِ مِنَ الْفِعْلِ الْمُضَعَّفِ (عُدَّ، مُرَّ، رُدَّ):", "tamreen_title_ur": "فعل مضعف سے امر بنانا:", "tamreen_title_en": "Forming imperative of doubled verb:",
            "grammar_goal_ur": "عَدَّ يَعُدُّ سے عُدَّ (گنتی کرو!)۔", "grammar_goal_en": "Imperative of doubled verb remains geminated: 'Udda.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا حَامِدُ، [ ＿＿＿ ] هٰذِهِ الْكُتُبَ .",
            "prompt_ur": "حامد، ان کتابوں کو گنو! (عَدَّ يَعُدُّ کا امر چنیں):", "prompt_en": "Hamid, count these books! (select imperative of 'Adda):",
            "answer": "عُدَّ",
            "options": ["عُدَّ", "اعْدُدْ", "عُودَّ", "تَعُدُّ"],
            "emoji": "🔢", "hint_ur": "مضعف کا امر عام طور پر ادغام کے ساتھ 'عُدَّ' آتا ہے۔", "hint_en": "Imperative remains doubled: 'Udda.",
            "explanation_ur": "فعل مضعف کے امر میں ادغام برقرار رہتا ہے: عُدَّ يَا حَامِدُ۔", "explanation_en": "Gemination maintained in singular command: 'Udda."
        },
        # Tamreen 13: الفرق بين قط وأبداً
        {
            "id": "b2_u29_q4", "book": 2, "unit_num": 29, "tamreen_num": 13,
            "badge_ar": "التَّمْرِينُ (13)", "badge_ur": "مشق (13): قَطُّ اور أَبَداً کا فرق", "badge_en": "Exercise (13): Qattu vs Abadan",
            "tamreen_title_ar": "اسْتِعْمَالُ (قَطُّ) لِنَفْيِ الْمَاضِي وَ(أَبَداً) لِنَفْيِ الْمُسْتَقْبَلِ:", "tamreen_title_ur": "قَطُّ (کبھی نہیں - ماضی کے لیے) اور أَبَداً (کبھی نہیں - مستقبل کے لیے):", "tamreen_title_en": "Qattu for past negative vs Abadan for future negative:",
            "grammar_goal_ur": "مَا فَعَلْتُ هٰذَا قَطُّ / لَنْ أَفْعَلَ هٰذَا أَبَداً۔", "grammar_goal_en": "Qattu is strictly past adverb; Abadan is strictly future.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَا رَأَيْتُ هٰذَا الرَّجُلَ [ ＿＿＿ ] .",
            "prompt_ur": "میں نے اس آدمی کو کبھی نہیں دیکھا (ماضی کی نفی کے لیے ظرف چنیں):", "prompt_en": "I have never seen this man (select past negative adverb):",
            "answer": "قَطُّ",
            "options": ["قَطُّ", "أَبَداً", "الآنَ", "دَائِماً"],
            "emoji": "👤", "hint_ur": "ماضی منفی کے بعد ہمیشہ 'قَطُّ' (پیش کے ساتھ) آتا ہے۔", "hint_en": "Past negative strictly takes Qattu with dammah.",
            "explanation_ur": "قَطُّ ماضی مستغرق کی نفی کا ظرف ہے: مَا رَأَيْتُهُ قَطُّ۔", "explanation_en": "Qattu negates past time; Abadan negates future."
        }
    ]

    # =========================================================================
    # UNIT 30: مراجعة شاملة للأفعال وإسنادها لضمائر التثنية
    # =========================================================================
    units[30] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u30_q1", "book": 2, "unit_num": 30, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "تثنیہ فاعل کے مکالمے کا فہم۔", "grammar_goal_en": "Dual dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَا اسْمَا الْفَتَيَيْنِ الْجَدِيدَيْنِ؟ [ ＿＿＿ ]",
            "prompt_ur": "ان دو نئے نوجوانوں کے نام کیا ہیں؟", "prompt_en": "What are the names of the two new young men?",
            "answer": "اسْمَاهُمَا حَسَنٌ وَحُسَيْنٌ .",
            "options": ["اسْمَاهُمَا حَسَنٌ وَحُسَيْنٌ .", "اسْمَاهُمَا عَلِيٌّ وَعُثْمَانُ .", "اسْمَاهُمَا أَحْمَدُ وَمَحْمُودٌ .", "اسْمَاهُمَا خَالِدٌ وَزَيْدٌ ."],
            "emoji": "👬", "hint_ur": "ان کے نام حسن اور حسین ہیں۔", "hint_en": "Their names are Hasan and Husayn.",
            "explanation_ur": "درست جواب: 'اسْمَاهُمَا حَسَنٌ وَحُسَيْنٌ .'۔", "explanation_en": "Correct answer: Hasan and Husayn."
        },
        # Tamreen 2: الفعل الماضي للتثنية (فَعَلَا)
        {
            "id": "b2_u30_q2", "book": 2, "unit_num": 30, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): ماضی تثنیہ (فَعَلَا)", "badge_en": "Exercise (2): Past Tense Dual (Fa'alaa)",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ الْمَاضِي إِلَى أَلِفِ الاِثْنَيْنِ (ذَهَبَا):", "tamreen_title_ur": "ماضی کو الف تثنیہ کے ساتھ جوڑیں:", "tamreen_title_en": "Attaching Alif of Dual to past verb (Zahabaa):",
            "grammar_goal_ur": "أَيْنَ خَالِدٌ وَحَامِدٌ؟ ذَهَبَا إِلَى الْمَكْتَبَةِ۔", "grammar_goal_en": "Dual subject takes dual past verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ خَالِدٌ وَحَامِدٌ؟ هُمَا [ ＿＿＿ ] إِلَى الْمَكْتَبَةِ .",
            "prompt_ur": "خالد اور حامد کہاں ہیں؟ وہ دونوں لائبریری گئے:", "prompt_en": "Where are Khalid and Hamid? They both went to library:",
            "answer": "ذَهَبَا",
            "options": ["ذَهَبَا", "ذَهَبُوا", "ذَهَبَ", "ذَهَبَتَا"],
            "emoji": "📚", "hint_ur": "دو مذکر کے لیے الف تثنیہ آتی ہے: ذَهَبَا۔", "hint_en": "Dual masculine takes Alif: Zahabaa.",
            "explanation_ur": "تثنیہ غائب مذکر کے لیے الف تثنیہ لگتی ہے: ذَهَبَا۔", "explanation_en": "Dual masculine past takes alif: Zahabaa."
        },
        # Tamreen 3: الفعل المضارع للتثنية (يَفْعَلَانِ)
        {
            "id": "b2_u30_q3", "book": 2, "unit_num": 30, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مضارع تثنیہ (يَفْعَلَانِ)", "badge_en": "Exercise (3): Present Tense Dual",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى أَلِفِ الاِثْنَيْنِ (يَفْعَلَانِ):", "tamreen_title_ur": "مضارع کو تثنیہ کے ساتھ جوڑیں (ثبوتِ نون):", "tamreen_title_en": "Present tense dual with affirmative nun:",
            "grammar_goal_ur": "الطَّالِبَانِ الْجَدِيدَانِ يَدْرُسَانِ فِي هٰذِهِ الْكُلِّيَّةِ۔", "grammar_goal_en": "Dual present verb ends in -aani.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَحْمَدُ وَإِبْرَاهِيمُ [ ＿＿＿ ] كُرَةَ السَّلَّةِ كُلَّ مَسَاءٍ .",
            "prompt_ur": "احمد اور ابراہیم ہر شام باسکٹ بال کھیلتے ہیں:", "prompt_en": "Ahmad and Ibrahim play basketball every evening:",
            "answer": "يَلْعَبَانِ",
            "options": ["يَلْعَبَانِ", "يَلْعَبُونَ", "يَلْعَبُ", "تَلْعَبَانِ"],
            "emoji": "🏀", "hint_ur": "تثنیہ مضارع میں الف اور نون آتی ہے: يَلْعَبَانِ۔", "hint_en": "Dual present takes -aani: Yal'abaani.",
            "explanation_ur": "تثنیہ مذکر غائب کے لیے 'يَلْعَبَانِ' آتا ہے۔", "explanation_en": "3rd person masculine dual: Yal'abaani."
        },
        # Tamreen 4: أمر التثنية (افْعَلَا)
        {
            "id": "b2_u30_q4", "book": 2, "unit_num": 30, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): امرِ تثنیہ (اذْهَبَا)", "badge_en": "Exercise (4): Dual Imperative (Idh-habaa)",
            "tamreen_title_ar": "صَوْغُ الأَمْرِ لِلْمُثَنَّى بِحَذْفِ النُّونِ (اذْهَبَا):", "tamreen_title_ur": "تثنیہ کے لیے امر بنانا (نون گرا کر):", "tamreen_title_en": "Forming dual imperative by dropping nun:",
            "grammar_goal_ur": "يَا أَخَوَانِ، اذْهَبَا إِلَى الْمَسْجِدِ الآنَ۔", "grammar_goal_en": "Dropping nun in dual imperative: Idh-habaa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا وَلَدَانِ، [ ＿＿＿ ] إِلَى الْمَسْجِدِ الآنَ .",
            "prompt_ur": "اے دو لڑکو، اب مسجد جاؤ! (تثنیہ کا امر چنیں):", "prompt_en": "O two boys, go to mosque now! (select dual imperative):",
            "answer": "اذْهَبَا",
            "options": ["اذْهَبَا", "اذْهَبُوا", "اذْهَبْ", "تَذْهَبَانِ"],
            "emoji": "🕌", "hint_ur": "تثنیہ کا امر الف کے ساتھ آتا ہے: اذْهَبَا۔", "hint_en": "Dual imperative ends in Alif: Idh-habaa.",
            "explanation_ur": "تثنیہ سے نون گر کر الف رہ جاتی ہے: اذْهَبَا۔", "explanation_en": "Nun drops, leaving alif: Idh-habaa."
        },
        # Tamreen 8: حالات إعراب المضارع للتثنية (رفع، نصب، جزم)
        {
            "id": "b2_u30_q5", "book": 2, "unit_num": 30, "tamreen_num": 8,
            "badge_ar": "التَّمْرِينُ (8)", "badge_ur": "مشق (8): إعراب مضارع التثنیہ", "badge_en": "Exercise (8): Dual Present Inflection",
            "tamreen_title_ar": "إِعْرَابُ الْمُضَارِعِ لِلْمُثَنَّى بِثُبُوتِ النُّونِ رَفْعاً وَحَذْفِهَا نَصْباً وَجَزْماً:", "tamreen_title_ur": "تثنیہ مضارع کا اعراب (رفع میں ثبوت نون، نصب و جزم میں حذف نون):", "tamreen_title_en": "Affirmative nun in Raf', deleted nun in Nasb/Jazm:",
            "grammar_goal_ur": "يَذْهَبَانِ / لَنْ يَذْهَبَا / لَمْ يَذْهَبَا۔", "grammar_goal_en": "Dual present verb drops nun with Lan and Lam.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطَّالِبَانِ [ ＿＿＿ ] أَمْسِ .",
            "prompt_ur": "دونوں طلبہ کل نہیں گئے (لم کے بعد مجزوم تثنیہ چنیں):", "prompt_en": "The two students did not go yesterday (select jussive dual):",
            "answer": "لَمْ يَذْهَبَا",
            "options": ["لَمْ يَذْهَبَا", "لَمْ يَذْهَبَانِ", "لَا يَذْهَبَا", "مَا ذَهَبَا"],
            "emoji": "🚶‍♂️🚶‍♂️", "hint_ur": "لم کی وجہ سے نون گر جائے گا: لَمْ يَذْهَبَا۔", "hint_en": "Nun drops after Lam: Lam Yazhabaa.",
            "explanation_ur": "افعال خمسہ اور تثنیہ حالت جزم میں نون گرا دیتے ہیں: لَمْ يَذْهَبَا۔", "explanation_en": "Jussive dual drops nun: Lam Yazhabaa."
        }
    ]

    # =========================================================================
    # UNIT 31: النعت والمنعوت وأوجه المطابقة والنسبة والأسماء المنقوصة
    # =========================================================================
    units[31] = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b2_u31_q1", "book": 2, "unit_num": 31, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَتَى يَبْدَأُ الطُّلَّابُ الْجُزْءَ الثَّالِثَ؟ [ ＿＿＿ ]",
            "prompt_ur": "طلبہ تیسری کتاب کب شروع کریں گے؟", "prompt_en": "When will the students start the third book?",
            "answer": "يَبْدَؤُونَهُ فِي الأُسْبُوعِ الْقَادِمِ .",
            "options": ["يَبْدَؤُونَهُ فِي الأُسْبُوعِ الْقَادِمِ .", "يَبْدَؤُونَهُ الْيَوْمَ .", "يَبْدَؤُونَهُ بَعْدَ شَهْرٍ .", "يَبْدَؤُونَهُ فِي الْعَامِ الْقَادِمِ ."],
            "emoji": "📖", "hint_ur": "وہ اگلے ہفتے شروع کریں گے۔", "hint_en": "They will start next week.",
            "explanation_ur": "درست جواب: 'يَبْدَؤُونَهُ فِي الأُسْبُوعِ الْقَادِمِ .'۔", "explanation_en": "Correct answer: next week."
        },
        # Tamreen 2: تعيين النعت والمنعوت
        {
            "id": "b2_u31_q2", "book": 2, "unit_num": 31, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): نعت اور منعوت کی پہچان", "badge_en": "Exercise (2): Identifying Adjective & Noun",
            "tamreen_title_ar": "تَعْيِينُ النَّعْتِ وَالْمَنْعُوتِ وَتَطَابُقُهُمَا فِي الإِعْرَابِ:", "tamreen_title_ur": "نعت (صفت) اور منعوت (موصوف) کا باہمی اعرابی مطابقت:", "tamreen_title_en": "Agreement of adjective and modified noun:",
            "grammar_goal_ur": "أُرِيدُ أَنْ أَشْرَبَ مَاءً بَارِداً (بارداً نعت ہے اور ماءً منعوت)۔", "grammar_goal_en": "Adjective agrees in case, gender, and definiteness.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أُرِيدُ أَنْ أَشْرَبَ مَاءً [ ＿＿＿ ] .",
            "prompt_ur": "میں ٹھنڈا پانی پینا چاہتا ہوں (منسوب نعت چنیں):", "prompt_en": "I want to drink cold water (select accusative adjective):",
            "answer": "بَارِداً",
            "options": ["بَارِداً", "بَارِدٌ", "بَارِدٍ", "الْبَارِدَ"],
            "emoji": "🧊", "hint_ur": "ماءً منسوب ہے اس لیے نعت بھی منسوب ہوگی: بَارِداً۔", "hint_en": "Matches mansub maa'an: Baaridan.",
            "explanation_ur": "نعت اپنے منعوت کے اعراب کی پابندی کرتی ہے: مَاءً بَارِداً۔", "explanation_en": "Adjective strictly copies case of noun: Baaridan."
        },
        # Tamreen 3: إكمال الجمل بنعت مناسب
        {
            "id": "b2_u31_q3", "book": 2, "unit_num": 31, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): نعت للمثنى", "badge_en": "Exercise (3): Dual Adjective Matching",
            "tamreen_title_ar": "مُطَابَقَةُ النَّعْتِ لِلْمَنْعُوتِ فِي التَّثْنِيَةِ:", "tamreen_title_ur": "تثنیہ کے لیے نعت کی مطابقت:", "tamreen_title_en": "Adjective agreement with dual noun:",
            "grammar_goal_ur": "لِي أَخَوَانِ كَبِيرَانِ وَأُخْتَانِ صَغِيرَتَانِ۔", "grammar_goal_en": "Dual noun takes dual adjective.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "لِي أَخَوَانِ [ ＿＿＿ ] ، وَأُخْتَانِ [ ＿＿＿ ] .",
            "prompt_ur": "میرے دو بڑے بھائی اور دو چھوٹی بہنیں ہیں (درست صفات چنیں):", "prompt_en": "I have two big brothers and two little sisters:",
            "answer": "كَبِيرَانِ ... صَغِيرَتَانِ",
            "options": ["كَبِيرَانِ ... صَغِيرَتَانِ", "كِبَارٌ ... صِغَارٌ", "كَبِيرَيْنِ ... صَغِيرَتَيْنِ", "كَبِيرٌ ... صَغِيرَةٌ"],
            "emoji": "👨‍👩‍👧‍👦", "hint_ur": "أخوانِ کے لیے كَبِيرَانِ اور أختانِ کے لیے صَغِيرَتَانِ آئے گا۔", "hint_en": "Dual masculine and dual feminine adjectives: Kabeeraani ... Sagheerataani.",
            "explanation_ur": "نعت عدد اور جنس میں منعوت کے مطابق ہوتی ہے: كَبِيرَانِ ... صَغِيرَتَانِ۔", "explanation_en": "Adjectives agree in number and gender."
        },
        # Tamreen 4: الاسم المنقوص (غَالٍ / الْغَالِي / غَالِياً)
        {
            "id": "b2_u31_q4", "book": 2, "unit_num": 21, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): اسمِ منقوص (غَالٍ)", "badge_en": "Exercise (4): Defective Noun (Ghaalin)",
            "tamreen_title_ar": "إِعْرَابُ الاسْمِ الْمَنْقُوصِ (غَالٍ / الْغَالِي / غَالِياً):", "tamreen_title_ur": "اسم منقوص کا اعراب (رفع و جر میں تنوین کسرہ، نصب میں فتحہ ظاہر):", "tamreen_title_en": "Inflection of Mankous noun (Ghaalin / Al-Ghaalee / Ghaaliyan):",
            "grammar_goal_ur": "هٰذَا كِتَابٌ غَالٍ، اشْتَرَيْتُ كِتَاباً غَالِياً۔", "grammar_goal_en": "Recognizing omitted ya in nominative/genitive and explicit ya in accusative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذَا الْمُعْجَمُ [ ＿＿＿ ] جِدّاً .",
            "prompt_ur": "یہ لغت بہت مہنگی ہے (غالی کا مرفوع صیغہ منتخب کریں):", "prompt_en": "This dictionary is very expensive (select nominative):",
            "answer": "غَالٍ",
            "options": ["غَالٍ", "غَالِي", "غَالِياً", "غَالِيٌ"],
            "emoji": "📖", "hint_ur": "اسم منقوص حالت رفع میں بغیر ال کے 'غَالٍ' آتا ہے۔", "hint_en": "Mankous noun drops ya in nominative without Al: Ghaalin.",
            "explanation_ur": "اسم منقوص جب نکرہ ہو تو رفع اور جر میں یاء گر کر دو زیر آتے ہیں: غَالٍ۔", "explanation_en": "Indefinite Mankous noun drops ya in nominative/genitive: Ghaalin."
        },
        # Tamreen 5: اسم النسبة (الياباني، الباكستاني، المصري)
        {
            "id": "b2_u31_q5", "book": 2, "unit_num": 31, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): اسمِ نسبت (يَاءُ النِّسْبَةِ)", "badge_en": "Exercise (5): Relative Adjective (Nisbah)",
            "tamreen_title_ar": "صَوْغُ اسْمِ النِّسْبَةِ بِإِلْحَاقِ يَاءٍ مُشَدَّدَةٍ مَكْسُورٍ مَا قَبْلَهَا:", "tamreen_title_ur": "اسمِ نسبت بنانا (آخر میں یاء مشددہ لگانا):", "tamreen_title_en": "Forming Nisbah adjective with doubled yaa preceded by kasrah:",
            "grammar_goal_ur": "الْيَابَانُ -> يَابَانِيٌّ، مِصْرُ -> مِصْرِيٌّ۔", "grammar_goal_en": "Forming nationality/relative adjectives with -iyy.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطَّالِبُ الَّذِي جَاءَ مِنَ الْيَابَانِ هُوَ طَالِبٌ [ ＿＿＿ ] .",
            "prompt_ur": "جو طالب علم جاپان سے آیا ہے وہ جاپانی طالب علم ہے:", "prompt_en": "The student who came from Japan is a Japanese student:",
            "answer": "يَابَانِيٌّ",
            "options": ["يَابَانِيٌّ", "يَابَانٌ", "يَابَانِيَّةٌ", "يَابَانِيَّانِ"],
            "emoji": "🇯🇵", "hint_ur": "جاپان کی طرف نسبت کے لیے 'يَابَانِيٌّ' آئے گا۔", "hint_en": "Relative adjective for Japan is Yaabaaniyy.",
            "explanation_ur": "یاء نسبت مشددہ کے ذریعے اسم نسبت بنتا ہے: طَالِبٌ يَابَانِيٌّ۔", "explanation_en": "Nisbah suffix -iyy forms nationality adjective: Yaabaaniyy."
        }
    ]

    return units

if __name__ == '__main__':
    u = get_b2_units_16_to_31()
    print("Units 16-31 built successfully!")
    for k in sorted(u.keys()):
        print(f"Unit {k}: {len(u[k])} questions")
