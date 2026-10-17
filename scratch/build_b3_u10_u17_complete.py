# -*- coding: utf-8 -*-
"""
Complete Deep Authentic Curriculum for Book 3 Units 10 to 17
Includes textbook dialogue comprehension (Tamreen 1) and all textbook grammar exercises.
"""

def get_b3_units_10_to_17_complete():
    data = {}

    # =========================================================================
    # UNIT 10: الجملة الاسمية والفعلية والمصدر المؤول وأفعال الشروع
    # =========================================================================
    u10 = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b3_u10_t1_q1", "book": 3, "unit_num": 10, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "لِمَ لَمْ يَحْضُرِ الْمُدَرِّسُ إِلَى الْفَصْلِ؟ [ ＿＿＿ ]",
            "prompt_ur": "استاد کلاس میں کیوں حاضر نہیں ہوئے؟", "prompt_en": "Why didn't the teacher attend class?",
            "answer": "لِأَنَّهُ كَانَ مَرِيضاً فَدَخَلَ الْمُسْتَشْفَى .",
            "options": [
                "لِأَنَّهُ كَانَ مَرِيضاً فَدَخَلَ الْمُسْتَشْفَى .",
                "لِأَنَّهُ سَافَرَ إِلَى مَكَّةَ .",
                "لِأَنَّهُ نَسِيَ مَوْعِدَ الدَّرْسِ .",
                "لِأَنَّهُ كَانَ فِي الْمَكْتَبَةِ ."
            ],
            "emoji": "🏥", "hint_ur": "کیونکہ وہ بیمار تھے اور ہسپتال داخل ہو گئے۔", "hint_en": "Because he was sick and entered hospital.",
            "explanation_ur": "درست جواب: 'لِأَنَّهُ كَانَ مَرِيضاً فَدَخَلَ الْمُسْتَشْفَى .'۔", "explanation_en": "Correct answer: He was sick."
        },
        {
            "id": "b3_u10_t1_q2", "book": 3, "unit_num": 10, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے سوالات:", "tamreen_title_en": "Dialogue facts:",
            "grammar_goal_ur": "مکالمے کا فہم۔", "grammar_goal_en": "Dialogue comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَنِ الَّذِي سَمَحَ لِلطُّلَّابِ بِالانْصِرَافِ؟ [ ＿＿＿ ]",
            "prompt_ur": "طلبہ کو جانے کی اجازت کس نے دی؟", "prompt_en": "Who permitted the students to dismiss?",
            "answer": "سَمَحَ لَهُمُ الْمُرَاقِبُ .",
            "options": ["سَمَحَ لَهُمُ الْمُرَاقِبُ .", "سَمَحَ لَهُمُ الْمُدِيرُ .", "سَمَحَ لَهُمُ الْحَارِسُ .", "انْصَرَفُوا بِدُونِ إِذْنٍ ."],
            "emoji": "👨‍💼", "hint_ur": "نگران نے اجازت دی۔", "hint_en": "The supervisor permitted them.",
            "explanation_ur": "درست جواب: 'سَمَحَ لَهُمُ الْمُرَاقِبُ .'۔", "explanation_en": "Correct answer: the supervisor."
        },
        # Tamreen 2: الجملة الاسمية والجملة الفعلية
        {
            "id": "b3_u10_t2_q1", "book": 3, "unit_num": 10, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جملہ اسمیہ و فعلیہ", "badge_en": "Exercise (2): Sentence Types",
            "tamreen_title_ar": "التَّمْيِيزُ بَيْنَ الْجُمْلَةِ الاسْمِيَّةِ وَالْفِعْلِيَّةِ:",
            "tamreen_title_ur": "جملہ اسمیہ اور فعلیہ کی پہچان:",
            "tamreen_title_en": "Distinguishing nominal vs verbal sentences:",
            "grammar_goal_ur": "جملہ اسمیہ اسم سے اور فعلیہ فعل سے شروع ہوتا ہے۔", "grammar_goal_en": "Nominal begins with noun; verbal begins with verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْجُمْلَةُ فِي: (اللَّهُ نُورُ السَّمَاوَاتِ وَالأَرْضِ) هِيَ جُمْلَةٌ: [ ＿＿＿ ]",
            "prompt_ur": "یہ جملہ کون سا جملہ ہے؟", "prompt_en": "What type of sentence is this?",
            "answer": "اسْمِيَّةٌ (تَبْدَأُ بِاسْمٍ)",
            "options": ["اسْمِيَّةٌ (تَبْدَأُ بِاسْمٍ)", "فِعْلِيَّةٌ", "شِبْهُ جُمْلَةٍ", "ظَرْفِيَّةٌ"],
            "emoji": "✨", "hint_ur": "لفظ جلالہ اسم ہے، اس لیے جملہ اسمیہ ہے۔", "hint_en": "Begins with a noun (Allah), so nominal.",
            "explanation_ur": "جو جملہ اسم سے شروع ہو وہ جملہ اسمیہ کہلاتا ہے۔", "explanation_en": "Starts with noun: Ismiyyah."
        },
        # Tamreen 3: المصدر المؤول
        {
            "id": "b3_u10_t3_q1", "book": 3, "unit_num": 10, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مصدر مؤول", "badge_en": "Exercise (3): Masdar Mu'awwal",
            "tamreen_title_ar": "تَقْدِيرُ الْمَصْدَرِ الْمُؤَوَّلِ بِالْمَصْدَرِ الصَّرِيحِ:",
            "tamreen_title_ur": "مصدر مؤول کو مصدر صریح میں بدلنا:",
            "tamreen_title_en": "Interpreting Masdar Mu'awwal as explicit Masdar:",
            "grammar_goal_ur": "أُرِيدُ أَنْ أَذْهَبَ = أُرِيدُ الذَّهَابَ۔", "grammar_goal_en": "An + verb = verbal noun.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "تَقْدِيرُ الْمَصْدَرِ الْمُؤَوَّلِ فِي: (أُرِيدُ أَنْ أَذْهَبَ) بِالْمَصْدَرِ الصَّرِيحِ هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "'أَنْ أَذْهَبَ' کی جگہ مصدر صریح کیا ہوگا؟", "prompt_en": "What is the explicit masdar for 'An adh-haba'?",
            "answer": "أُرِيدُ الذَّهَابَ",
            "options": ["أُرِيدُ الذَّهَابَ", "أُرِيدُ ذَاهِباً", "أُرِيدُ أَنْ يَذْهَبَ", "أُرِيدُ مَذْهَباً"],
            "emoji": "🚶‍♂️", "hint_ur": "أن ناصبہ اور فعل مل کر 'الذَّهَابَ' کی تاویل میں ہیں۔", "hint_en": "Equates to Ath-Thahaba.",
            "explanation_ur": "أن المصدرية اور فعل کا مجموعہ مصدر صریح 'الذَّهَابَ' کا معنی دیتا ہے۔", "explanation_en": "Resolves to: Ureedu ath-thahaba."
        },
        # Tamreen 4: أفعال الشروع (طَفِقَ، جَعَلَ، أَخَذَ)
        {
            "id": "b3_u10_t4_q1", "book": 3, "unit_num": 10, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): افعال الشروع", "badge_en": "Exercise (4): Verbs of Inception",
            "tamreen_title_ar": "أَفْعَالُ الشُّرُوعِ (طَفِقَ / جَعَلَ / أَخَذَ يَفْعَلُ):",
            "tamreen_title_ur": "افعالِ شروع کا عمل (کسی کام کو شروع کرنا):",
            "tamreen_title_en": "Syntax of Verbs of Inception + present verb:",
            "grammar_goal_ur": "طَفِقَ يَفْعَلُ كَذَا أَيْ شَرَعَ وَابْتَدَأَ فِيهِ۔", "grammar_goal_en": "Tafiqa / Ja'ala / Akhadha mean 'began to do'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَعْنَى قَوْلِهِ تَعَالَى: { وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِنْ وَرَقِ الْجَنَّةِ } : [ ＿＿＿ ]",
            "prompt_ur": "قرآنی آیت میں 'طَفِقَا' کا کیا معنی ہے؟", "prompt_en": "What does 'Tafiqa' mean in the Quranic verse?",
            "answer": "أَخَذَا وَشَرَعَا يَفْعَلَانِ",
            "options": ["أَخَذَا وَشَرَعَا يَفْعَلَانِ", "امْتَنَعَا عَنِ الْفِعْلِ", "أَرَادَا أَنْ يَفْعَلَا", "نَسِيَا أَنْ يَفْعَلَا"],
            "emoji": "🍃", "hint_ur": "طفق کا معنی 'شروع کیا' ہے۔", "hint_en": "Tafiqa means began/started to do.",
            "explanation_ur": "طفق افعال شروع میں سے ہے جس کا معنی 'شروع کیا' ہوتا ہے۔", "explanation_en": "Af'al ash-Shuroo' express inception of an action."
        }
    ]
    data['b3_u10'] = u10

    # =========================================================================
    # UNIT 11: المبتدأ والخبر • تقديم الخبر وجوباً • شبه الجملة
    # =========================================================================
    u11 = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b3_u11_t1_q1", "book": 3, "unit_num": 11, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ أَرَادَ حَامِدٌ أَنْ يَذْهَبَ؟ [ ＿＿＿ ]",
            "prompt_ur": "حامد کہاں جانا چاہتا تھا؟", "prompt_en": "Where did Hamid want to go?",
            "answer": "أَرَادَ أَنْ يَذْهَبَ إِلَى الْمُسْتَشْفَى لِعِيَادَةِ الْمُدَرِّسِ .",
            "options": [
                "أَرَادَ أَنْ يَذْهَبَ إِلَى الْمُسْتَشْفَى لِعِيَادَةِ الْمُدَرِّسِ .",
                "أَرَادَ أَنْ يَذْهَبَ إِلَى السُّوقِ .",
                "أَرَادَ أَنْ يَذْهَبَ إِلَى الْمَطَارِ .",
                "أَرَادَ أَنْ يَرْجِعَ إِلَى الْبَيْتِ ."
            ],
            "emoji": "🏥", "hint_ur": "وہ استاد کی عیادت کے لیے ہسپتال جانا چاہتا تھا۔", "hint_en": "To visit the sick teacher in hospital.",
            "explanation_ur": "درست جواب: 'أَرَادَ أَنْ يَذْهَبَ إِلَى الْمُسْتَشْفَى لِعِيَادَةِ الْمُدَرِّسِ .'۔", "explanation_en": "Correct answer: to visit the teacher."
        },
        # Tamreen 2: أنواع الخبر
        {
            "id": "b3_u11_t2_q1", "book": 3, "unit_num": 11, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): خبر کی اقسام", "badge_en": "Exercise (2): Types of Predicate (Khabar)",
            "tamreen_title_ar": "أَنْوَاعُ الْخَبَرِ (مُفْرَدٌ، جُمْلَةٌ، شِبْهُ جُمْلَةٍ):",
            "tamreen_title_ur": "خبر کی تین اقسام (مفرد، جملہ، شبہ جملہ) کی پہچان:",
            "tamreen_title_en": "Types of Predicate: Singular, Sentence, Quasi-sentence:",
            "grammar_goal_ur": "الطَّالِبُ فِي الْفَصْلِ میں خبر شبہ جملہ (جار و مجرور) ہے۔", "grammar_goal_en": "Recognizing quasi-sentence predicate.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَوْعُ الْخَبَرِ فِي جُمْلَةِ: (الْحَمْدُ لِلَّهِ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "'الْحَمْدُ لِلَّهِ' میں خبر کس قسم کی ہے؟", "prompt_en": "What type of Khabar is 'Li-llahi'?",
            "answer": "شِبْهُ جُمْلَةٍ (جَارٌّ وَمَجْرُورٌ)",
            "options": ["شِبْهُ جُمْلَةٍ (جَارٌّ وَمَجْرُورٌ)", "مُفْرَدٌ", "جُمْلَةٌ فِعْلِيَّةٌ", "جُمْلَةٌ اسْمِيَّةٌ"],
            "emoji": "🤲", "hint_ur": "لِلَّهِ جار و مجرور ہے اس لیے شبہ جملہ ہے۔", "hint_en": "Prepositional phrase is Shibh Jumlah.",
            "explanation_ur": "جار و مجرور یا ظرف کو شبہ جملہ کہا جاتا ہے: شِبْهُ جُمْلَةٍ۔", "explanation_en": "Jar wa Majroor constitutes Shibh Jumlah."
        },
        # Tamreen 3: تقديم الخبر وجوباً
        {
            "id": "b3_u11_t3_q1", "book": 3, "unit_num": 11, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): خبر کو پہلے لانا (تقديم الخبر)", "badge_en": "Exercise (3): Obligatory Fronting of Khabar",
            "tamreen_title_ar": "وُجُوبُ تَقْدِيمِ الْخَبَرِ إِذَا كَانَ شِبْهَ جُمْلَةٍ وَالْمُبْتَدَأُ نَكِرَةً:",
            "tamreen_title_ur": "جب مبتدا نکرہ اور خبر شبہ جملہ ہو تو خبر کو پہلے لانا واجب ہے:",
            "tamreen_title_en": "Obligatory fronting when Khabar is quasi-sentence and Mubtada is indefinite:",
            "grammar_goal_ur": "فِي الْفَصْلِ طَالِبٌ (طالبٌ مبتدأ مؤخر ہے)۔", "grammar_goal_en": "Fronted predicate precedes indefinite subject.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي جُمْلَةِ: (فِي الدَّارِ رَجُلٌ)، إِعْرَابُ كَلِمَةِ (رَجُلٌ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "'رَجُلٌ' کا نحوی کردار کیا ہے؟", "prompt_en": "What is the syntactic role of 'Rajulun'?",
            "answer": "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ",
            "options": [
                "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ",
                "خَبَرٌ مَرْفُوعٌ",
                "مَفْعُولٌ بِهِ",
                "مُضَافٌ إِلَيْهِ"
            ],
            "emoji": "🏠", "hint_ur": "یہ مؤخر مبتدا ہے جس کی خبر پہلے آ گئی ہے۔", "hint_en": "Deferred subject: Mubtada Mu'akhkhar.",
            "explanation_ur": "فِي الدَّارِ خبر مقدم ہے اور رَجُلٌ مبتدأ مؤخر ہے۔", "explanation_en": "Rajulun is deferred subject (Mubtada Mu'akhkhar)."
        }
    ]
    data['b3_u11'] = u11

    # =========================================================================
    # UNIT 12: المفعول فيه (ظرفا الزمان والمكان)
    # =========================================================================
    u12 = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b3_u12_t1_q1", "book": 3, "unit_num": 12, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَتَى وَصَلَ الْحُسَيْنُ مِنَ السَّفَرِ؟ [ ＿＿＿ ]",
            "prompt_ur": "حسین سفر سے کب پہنچا؟", "prompt_en": "When did Al-Husayn arrive from travel?",
            "answer": "وَصَلَ أَمْسِ بَعْدَ صَلَاةِ الْمَغْرِبِ .",
            "options": ["وَصَلَ أَمْسِ بَعْدَ صَلَاةِ الْمَغْرِبِ .", "وَصَلَ الْيَوْمَ فِي الصَّبَاحِ .", "وَصَلَ قَبْلَ أُسْبُوعٍ .", "سَيَصِلُ غَداً ."],
            "emoji": "✈️", "hint_ur": "کل نماز مغرب کے بعد پہنچا۔", "hint_en": "Arrived yesterday after Maghrib prayer.",
            "explanation_ur": "درست جواب: 'وَصَلَ أَمْسِ بَعْدَ صَلَاةِ الْمَغْرِبِ .'۔", "explanation_en": "Correct answer: yesterday after Maghrib."
        },
        # Tamreen 2: ظرف الزمان
        {
            "id": "b3_u12_t2_q1", "book": 3, "unit_num": 12, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): ظرفِ زمان", "badge_en": "Exercise (2): Adverb of Time (Zarf Zaman)",
            "tamreen_title_ar": "تَعْيِينُ ظَرْفِ الزَّمَانِ (الْمَفْعُولِ فِيهِ):",
            "tamreen_title_ur": "ظرفِ زمان کی پہچان اور اس کا منسوب ہونا:",
            "tamreen_title_en": "Identifying Adverbs of Time and their accusative case:",
            "grammar_goal_ur": "صُمْتُ يَوْمَ الْخَمِيسِ میں 'يَوْمَ' ظرف زمان منسوب ہے۔", "grammar_goal_en": "Zarf Zaman is Mansub.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَافَرَ أَبِي إِلَى جُدَّةَ [ ＿＿＿ ] .",
            "prompt_ur": "میرے والد جمعرات کے دن جدہ گئے (ظرف زمان منسوب چنیں):", "prompt_en": "My father traveled on Thursday (select accusative adverb):",
            "answer": "يَوْمَ الْخَمِيسِ (مَنْصُوبٌ بِالْفَتْحَةِ)",
            "options": [
                "يَوْمَ الْخَمِيسِ (مَنْصُوبٌ بِالْفَتْحَةِ)",
                "يَوْمُ الْخَمِيسِ",
                "فِي يَوْمُ الْخَمِيسِ",
                "يَوْمٍ"
            ],
            "emoji": "🗓️", "hint_ur": "ظرف زمان ہمیشہ منسوب (زبر والا) ہوتا ہے: يَوْمَ۔", "hint_en": "Zarf Zaman is Mansub with fathah: Yawma.",
            "explanation_ur": "مفعول فیہ (ظرف زمان) منسوب ہوتا ہے: يَوْمَ الْخَمِيسِ۔", "explanation_en": "Adverb of time takes accusative fathah: Yawma."
        },
        # Tamreen 3: ظرف المكان
        {
            "id": "b3_u12_t3_q1", "book": 3, "unit_num": 12, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): ظرفِ مکان", "badge_en": "Exercise (3): Adverb of Place (Zarf Makan)",
            "tamreen_title_ar": "تَعْيِينُ ظَرْفِ الْمَكَانِ (أَمَامَ، خَلْفَ، فَوْقَ، تَحْتَ):",
            "tamreen_title_ur": "ظرفِ مکان کی پہچان اور اس کا نصب:",
            "tamreen_title_en": "Adverbs of Place: Amaama, Khalfa, Fawqa, Tahta:",
            "grammar_goal_ur": "جَلَسَ الطَّالِبُ أَمَامَ الْمُدَرِّسِ۔", "grammar_goal_en": "Using adverbs of place in accusative case.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "وَقَفَ الْخَطِيبُ [ ＿＿＿ ] الْمِنْبَرِ .",
            "prompt_ur": "خطیب منبر کے اوپر کھڑے ہوئے (ظرف مکان چنیں):", "prompt_en": "The preacher stood on/above the pulpit:",
            "answer": "فَوْقَ",
            "options": ["فَوْقَ", "فَوْقُ", "فَوْقِ", "مِنْ فَوْقُ"],
            "emoji": "🕌", "hint_ur": "ظرف مکان منسوب بالفتحہ ہوتا ہے: فَوْقَ۔", "hint_en": "Adverb of place takes fathah: Fawqa.",
            "explanation_ur": "فَوْقَ ظرف مکان ہے اور منسوب بالفتحہ ہوتا ہے۔", "explanation_en": "Fawqa is accusative adverb of place."
        }
    ]
    data['b3_u12'] = u12

    # =========================================================================
    # UNIT 13: لام الأمر وجزم المضارع • جواب الطلب
    # =========================================================================
    u13 = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b3_u13_t1_q1", "book": 3, "unit_num": 13, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مِنْ أَيْنَ يَأْتِي الْوَفْدُ إِلَى الْمَعْهَدِ؟ [ ＿＿＿ ]",
            "prompt_ur": "وفد معہد میں کہاں سے آ رہا ہے؟", "prompt_en": "Where is the delegation coming from?",
            "answer": "يَأْتِي مِنْ نَيْجِيرِيَا .",
            "options": ["يَأْتِي مِنْ نَيْجِيرِيَا .", "يَأْتِي مِنْ إِنْدُونِيسِيَا .", "يَأْتِي مِنْ بَاكِسْتَانَ .", "يَأْتِي مِنْ مِصْرَ ."],
            "emoji": "🌍", "hint_ur": "وہ نائیجیریا سے آ رہا ہے۔", "hint_en": "It is coming from Nigeria.",
            "explanation_ur": "درست جواب: 'يَأْتِي مِنْ نَيْجِيرِيَا .'۔", "explanation_en": "Correct answer: Nigeria."
        },
        # Tamreen 2: لام الأمر
        {
            "id": "b3_u13_t2_q1", "book": 3, "unit_num": 13, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): لَامُ الأَمْرِ", "badge_en": "Exercise (2): Lam of Command (Laam al-Amr)",
            "tamreen_title_ar": "دُخُولُ (لَامِ الأَمْرِ) عَلَى الْمُضَارِعِ وَجَزْمُهُ:",
            "tamreen_title_ur": "لامِ امر کا داخل ہونا اور مضارع کو جزم دینا:",
            "tamreen_title_en": "Laam al-Amr making present verb jussive:",
            "grammar_goal_ur": "لِيَكْتُبْ كُلُّ طَالِبٍ وَاجِبَهُ (چاہیے کہ ہر طالب علم اپنا ہوم ورک لکھے)۔", "grammar_goal_en": "Laam al-Amr conveys 3rd person command with jussive case.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَالَ الْمُدَرِّسُ: [ ＿＿＿ ] كُلُّ طَالِبٍ فِي مَكَانِهِ .",
            "prompt_ur": "استاد نے کہا: چاہیے کہ ہر طالب علم اپنی جگہ پر بیٹھے:", "prompt_en": "The teacher said: Let every student sit in his place:",
            "answer": "لِيَجْلِسْ (بِكَسْرِ اللَّامِ وَجَزْمِ الْفِعْلِ)",
            "options": [
                "لِيَجْلِسْ (بِكَسْرِ اللَّامِ وَجَزْمِ الْفِعْلِ)",
                "لِيَجْلِسُ",
                "لِيَجْلِسَ",
                "يَجْلِسْ"
            ],
            "emoji": "🪑", "hint_ur": "لام امر مکسور ہوتی ہے اور مضارع کو جزم دیتی ہے: لِيَجْلِسْ۔", "hint_en": "Laam al-Amr causes jussive: Li-yajlis.",
            "explanation_ur": "لام امر مضارع کو جزم دیتی ہے: لِيَجْلِسْ۔", "explanation_en": "Laam al-Amr gives jussive sukoon: Li-yajlis."
        },
        # Tamreen 3: جواب الطلب
        {
            "id": "b3_u13_t3_q1", "book": 3, "unit_num": 13, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): جَوَابُ الطَّلَبِ", "badge_en": "Exercise (3): Response to Request (Jawaab at-Talab)",
            "tamreen_title_ar": "جَزْمُ الْمُضَارِعِ الْوَاقِعِ فِي جَوَابِ الطَّلَبِ:",
            "tamreen_title_ur": "امر یا نہی کے جواب میں آنے والے مضارع کا مجزوم ہونا:",
            "tamreen_title_en": "Jussive case of present verb in response to request (Jawaab at-Talab):",
            "grammar_goal_ur": "اجْتَهِدْ تَنْجَحْ (محنت کرو تم کامیاب ہو جاؤ گے)۔", "grammar_goal_en": "Verb following imperative is jussive as conditional response.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَالَ تَعَالَى: { فَاذْكُرُونِي [ ＿＿＿ ] } .",
            "prompt_ur": "قرآنی آیت میں جواب الطلب کا درست مجزوم صیغہ چنیں:", "prompt_en": "Select the jussive response to command in Quranic verse:",
            "answer": "أَذْكُرْكُمْ",
            "options": ["أَذْكُرْكُمْ", "أَذْكُرُكُمْ", "أَذْكُرَكُمْ", "فَأَذْكُرُكُمْ"],
            "emoji": "📖", "hint_ur": "امر (اذْكُرُونِي) کا جواب ہونے کی وجہ سے 'أَذْكُرْكُمْ' مجزوم ہے۔", "hint_en": "Jussive in response to command: Az-kurkum.",
            "explanation_ur": "جواب الطلب میں آنے والا فعل مضارع مجزوم ہوتا ہے: أَذْكُرْكُمْ۔", "explanation_en": "Jawaab at-Talab is in jussive case."
        }
    ]
    data['b3_u13'] = u13

    # =========================================================================
    # UNIT 14: أسلوب الشرط بـ (إذا) واقتران الجواب بالفاء
    # =========================================================================
    u14 = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b3_u14_t1_q1", "book": 3, "unit_num": 14, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَاذَا قَالَ الْمُدَرِّسُ لِمَنْ عَطَسَ فِي الْفَصْلِ؟ [ ＿＿＿ ]",
            "prompt_ur": "کلاس میں چھینکنے والے سے استاد نے کیا کہا؟", "prompt_en": "What did teacher say to the one who sneezed?",
            "answer": "قَالَ لَهُ: يَرْحَمُكَ اللَّهُ (بَعْدَ أَنْ حَمِدَ اللَّهَ) .",
            "options": [
                "قَالَ لَهُ: يَرْحَمُكَ اللَّهُ (بَعْدَ أَنْ حَمِدَ اللَّهَ) .",
                "قَالَ لَهُ: اخْرُجْ مِنَ الْفَصْلِ .",
                "مَا قَالَ لَهُ شَيْئاً .",
                "قَالَ لَهُ: اشْرَبِ الدَّوَاءَ ."
            ],
            "emoji": "🤧", "hint_ur": "اللہ آپ پر رحم فرمائے (یرحمک اللہ)۔", "hint_en": "May Allah have mercy on you.",
            "explanation_ur": "درست جواب: 'يَرْحَمُكَ اللَّهُ'۔", "explanation_en": "Correct answer: Yarhamuka Allah."
        },
        # Tamreen 2: (إذا) الشرطية
        {
            "id": "b3_u14_t2_q1", "book": 3, "unit_num": 14, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): إِذَا الشَّرْطِيَّة", "badge_en": "Exercise (2): Conditional Idhaa",
            "tamreen_title_ar": "دَلَالَةُ (إِذَا) الشَّرْطِيَّةِ غَيْرِ الْجَازِمَةِ عَلَى الْمُسْتَقْبَلِ:",
            "tamreen_title_ur": "إذا شرطیہ کا ماضی کے فعل کو مستقبل کے معنی میں بدلنا:",
            "tamreen_title_en": "Idhaa turning past verb meaning into future:",
            "grammar_goal_ur": "إِذَا جَاءَ نَصْرُ اللهِ (جب اللہ کی مدد آئے گی)۔", "grammar_goal_en": "Idhaa implies future condition with past verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدَ دُخُولِ (إِذَا) عَلَى الْفِعْلِ الْمَاضِي، يُفِيدُ فِي الْمَعْنَى: [ ＿＿＿ ]",
            "prompt_ur": "إذا جب فعل ماضی پر داخل ہو تو وہ معنی میں کیا فائدہ دیتا ہے؟", "prompt_en": "What meaning does Idhaa impart to past verb?",
            "answer": "تَحْوِيلَ الْمَعْنَى إِلَى الْمُسْتَقْبَلِ",
            "options": [
                "تَحْوِيلَ الْمَعْنَى إِلَى الْمُسْتَقْبَلِ",
                "الْمُضِيَّ فَقَطْ",
                "نَفْيَ الْحَدَثِ",
                "التَّعْجِيزَ"
            ],
            "emoji": "⏳", "hint_ur": "اگرچہ فعل ماضی ہو مگر إذا کی وجہ سے معنی مستقبل کا ہوتا ہے۔", "hint_en": "Shifts meaning to the future.",
            "explanation_ur": "إذا ظرف زمان مستقبل ہے جو شرط کا معنی دیتا ہے: تَحْوِيلَ الْمَعْنَى إِلَى الْمُسْتَقْبَلِ۔", "explanation_en": "Idhaa conveys future condition."
        },
        # Tamreen 3: اقتران جواب الشرط بالفاء
        {
            "id": "b3_u14_t3_q1", "book": 3, "unit_num": 14, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): جواب شرط پر فاء کا داخل ہونا", "badge_en": "Exercise (3): Entering Faa on Conditional Response",
            "tamreen_title_ar": "وُجُوبُ اقْتِرَانِ جَوَابِ الشَّرْطِ بِالْفَاءِ:",
            "tamreen_title_ur": "جب جواب شرط جملہ اسمیہ یا طلبیہ ہو تو فاء لگانا واجب ہے:",
            "tamreen_title_en": "Obligatory Faa on response when nominal or imperative:",
            "grammar_goal_ur": "إِذَا رَأَيْتَ حَامِداً فَسَلِّمْ عَلَيْهِ۔", "grammar_goal_en": "Faa is required when answer is an imperative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "إِذَا لَقِيتَ أَخَاكَ الْمُسْلِمَ [ ＿＿＿ ] .",
            "prompt_ur": "جب تم اپنے مسلمان بھائی سے ملو تو اسے سلام کرو (فاء کے ساتھ امر چنیں):", "prompt_en": "When you meet your Muslim brother, greet him:",
            "answer": "فَسَلِّمْ عَلَيْهِ",
            "options": ["فَسَلِّمْ عَلَيْهِ", "سَلِّمْ عَلَيْهِ", "وَسَلِّمْ عَلَيْهِ", "ثُمَّ سَلِّمْ عَلَيْهِ"],
            "emoji": "🤝", "hint_ur": "امر جواب شرط ہو تو فاء لگتی ہے: فَسَلِّمْ عَلَيْهِ۔", "hint_en": "Imperative response takes Faa: Fa-sallim.",
            "explanation_ur": "جب جواب شرط طلبیہ ہو تو فاء کا داخل ہونا واجب ہے: فَسَلِّمْ عَلَيْهِ۔", "explanation_en": "Faa is obligatory with imperative clause."
        }
    ]
    data['b3_u14'] = u14

    # =========================================================================
    # UNIT 15: أدوات الشرط الجازمة • كم الاستفهامية والخبرية • حتى
    # =========================================================================
    u15 = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b3_u15_t1_q1", "book": 3, "unit_num": 15, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَنِ الطَّالِبُ الَّذِي غَابَ أُسْبُوعَيْنِ كَامِلَيْنِ؟ [ ＿＿＿ ]",
            "prompt_ur": "کون سا طالب علم پورے دو ہفتے غیر حاضر رہا؟", "prompt_en": "Which student was absent for two full weeks?",
            "answer": "أُسَامَةُ .",
            "options": ["أُسَامَةُ .", "حَامِدٌ .", "عَلِيٌّ .", "فَيْصَلٌ ."],
            "emoji": "👨‍🎓", "hint_ur": "اسامہ غیر حاضر رہا۔", "hint_en": "Usamah was absent.",
            "explanation_ur": "درست جواب: 'أُسَامَةُ .'۔", "explanation_en": "Correct answer: Usamah."
        },
        # Tamreen 2: أدوات الشرط الجازمة (إِنْ، مَنْ، مَا)
        {
            "id": "b3_u15_t2_q1", "book": 3, "unit_num": 15, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): ادواتِ شرط جازمہ", "badge_en": "Exercise (2): Jussive Conditional Particles",
            "tamreen_title_ar": "جَزْمُ فِعْلَيِ الشَّرْطِ وَالْجَوَابِ بـ (إِنْ، مَنْ):",
            "tamreen_title_ur": "حرف شرط کے ذریعے شرط اور جواب دونوں فعلوں کو جزم دینا:",
            "tamreen_title_en": "Conditional particles making both condition and response jussive:",
            "grammar_goal_ur": "مَنْ يَجْتَهِدْ يَنْجَحْ (دونوں فعل مجزوم ہیں)۔", "grammar_goal_en": "Both verbs take jussive sukoon in conditionals.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَالَ تَعَالَى: { فَمَنْ يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْراً [ ＿＿＿ ] } .",
            "prompt_ur": "قرآنی آیت میں جواب شرط کا درست مجزوم صیغہ چنیں:", "prompt_en": "Select the jussive response verb in Quranic verse:",
            "answer": "يَرَهُ (بِجَزْمِ حَرْفِ الْعِلَّةِ)",
            "options": [
                "يَرَهُ (بِجَزْمِ حَرْفِ الْعِلَّةِ)",
                "يَرَاهُ",
                "يَرَى",
                "يَرَوْهُ"
            ],
            "emoji": "⚖️", "hint_ur": "جواب شرط مجزوم ہے اور اس کا الف گر گیا ہے: يَرَهُ۔", "hint_en": "Drops weak letter in jussive: Yarahu.",
            "explanation_ur": "مَنْ جازمہ کی وجہ سے جواب شرط کا حرف علت گر گیا ہے: يَرَهُ۔", "explanation_en": "Weak ending dropped due to jussive: Yarahu."
        },
        # Tamreen 3: كم الاستفهامية وكم الخبرية
        {
            "id": "b3_u15_t3_q1", "book": 3, "unit_num": 15, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): كَمْ استفہامیہ بمقابلہ كَمْ خبریہ", "badge_en": "Exercise (3): Interrogative vs Exclamatory Kam",
            "tamreen_title_ar": "الْفَرْقُ بَيْنَ (كَمِ) الاسْتِفْهَامِيَّةِ وَ(كَمِ) الْخَبَرِيَّةِ التَّكْثِيرِيَّةِ:",
            "tamreen_title_ur": "کم استفہامیہ (جس کے بعد تمیز مفرد منسوب ہو) اور خبریہ (مجرور) کا فرق:",
            "tamreen_title_en": "Interrogative Kam (singular accusative) vs Exclamatory Kam (genitive):",
            "grammar_goal_ur": "كَمْ طَالِباً فِي الْفَصْلِ؟ (استفہامیہ) بمقابلہ كَمْ كِتَابٍ عِنْدِي! (خبریہ)۔", "grammar_goal_en": "Interrogative takes accusative; exclamatory takes genitive.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي جُمْلَةِ: (كَمْ كِتَابٍ قَرَأْتُهُ فِي الْعُطْلَةِ!)، نَوْعُ (كَمْ) هُنَا: [ ＿＿＿ ]",
            "prompt_ur": "اس جملے میں کم کی قسم کون سی ہے؟ (بہت سی کتابیں میں نے پڑھیں!):", "prompt_en": "What type of Kam is used here (expressing many)?",
            "answer": "خَبَرِيَّةٌ تُفِيدُ التَّكْثِيرَ (تَمْيِيزُهَا مَجْرُورٌ)",
            "options": [
                "خَبَرِيَّةٌ تُفِيدُ التَّكْثِيرَ (تَمْيِيزُهَا مَجْرُورٌ)",
                "اسْتِفْهَامِيَّةٌ تَطْلُبُ عَدَداً",
                "شَرْطِيَّةٌ",
                "نَافِيَةٌ"
            ],
            "emoji": "📚", "hint_ur": "کیونکہ اس کا تمیز مجرور ہے (كِتَابٍ) اس لیے یہ خبریہ تکثیریہ ہے۔", "hint_en": "Followed by genitive, so exclamatory.",
            "explanation_ur": "کم خبریہ کثرت بیان کرتی ہے اور اس کے بعد اسم مجرور آتا ہے: كَمْ كِتَابٍ!۔", "explanation_en": "Exclamatory Kam is followed by genitive noun."
        }
    ]
    data['b3_u15'] = u15

    # =========================================================================
    # UNIT 16: باب فَعَّلَ يُفَعِّلُ تَفْعِيلاً • اسم الفاعل والمفعول • جموع التكسير
    # =========================================================================
    u16 = [
        # Tamreen 1: أسئلة الدرس والحديث الشريف
        {
            "id": "b3_u16_t1_q1", "book": 3, "unit_num": 16, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ حدیثِ نبوی", "badge_en": "Exercise (1): Hadith Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ حَسَبَ الْحَدِيثِ الشَّرِيفِ:",
            "tamreen_title_ur": "حدیث نبوی کے مطابق سوالات کے جوابات دیں:",
            "tamreen_title_en": "Answer questions according to the prophetic Hadith:",
            "grammar_goal_ur": "حدیث شریف کے الفاظ اور معنی کا فہم۔", "grammar_goal_en": "Comprehending Hadith vocabulary.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَاذَا قَالَ النَّبِيُّ ﷺ لِلأَقْرَعِ بْنِ حَابِسٍ عِنْدَمَا قَالَ: مَا قَبَّلْتُ أَحَداً مِنْ وَلَدِي؟ [ ＿＿＿ ]",
            "prompt_ur": "جب اقرع بن حابس نے کہا کہ میں نے اپنے کسی بچے کو نہیں چوما، تو آپ ﷺ نے کیا فرمایا؟", "prompt_en": "What did the Prophet (pbuh) reply to Al-Aqra'?",
            "answer": "\"مَنْ لَا يَرْحَمْ لَا يُرْحَمْ\" .",
            "options": [
                "\"مَنْ لَا يَرْحَمْ لَا يُرْحَمْ\" .",
                "\"الرَّاحِمُونَ يَرْحَمُهُمُ الرَّحْمٰنُ\" .",
                "\"خَيْرُكُمْ خَيْرُكُمْ لِأَهْلِهِ\" .",
                "\"طَلَبُ الْعِلْمِ فَرِيضَةٌ\" ."
            ],
            "emoji": "👦", "hint_ur": "جو رحم نہیں کرتا اس پر رحم نہیں کیا جاتا۔", "hint_en": "Whoever does not show mercy will not receive mercy.",
            "explanation_ur": "درست جواب: حضور ﷺ نے فرمایا: 'مَنْ لَا يَرْحَمْ لَا يُرْحَمْ'۔", "explanation_en": "Prophetic Hadith: Man laa yarham laa yurham."
        },
        # Tamreen 2: باب فَعَّلَ يُفَعِّلُ تَفْعِيلاً
        {
            "id": "b3_u16_t2_q1", "book": 3, "unit_num": 16, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): باب تفعيل", "badge_en": "Exercise (2): Form II (Fa''ala / Taf'eel)",
            "tamreen_title_ar": "صَوْغُ الْمَصْدَرِ مِنْ بَابِ (فَعَّلَ يُفَعِّلُ - تَفْعِيلاً):",
            "tamreen_title_ur": "باب تفعیل کا مصدر صریح بنانا (عَلَّمَ -> تَعْلِيم):",
            "tamreen_title_en": "Deriving verbal noun on pattern Taf'eel from Form II verbs:",
            "grammar_goal_ur": "قَبَّلَ -> تَقْبِيل، عَلَّمَ -> تَعْلِيم، دَرَّسَ -> تَدْرِيس۔", "grammar_goal_en": "Mastering Form II masdar Taf'eel.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَصْدَرُ الْفِعْلِ (قَبَّلَ يُقَبِّلُ) عَلَى وَزْنِ (تَفْعِيل) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "قَبَّلَ يُقَبِّلُ کا مصدر منتخب کریں:", "prompt_en": "Select the verbal noun of Qabbala (Taf'eel):",
            "answer": "تَقْبِيلٌ",
            "options": ["تَقْبِيلٌ", "قُبْلَةٌ", "مُقَبَّلٌ", "قَابِلٌ"],
            "emoji": "😘", "hint_ur": "تَفْعِيل کے وزن پر 'تَقْبِيلٌ' بنے گا۔", "hint_en": "Pattern Taf'eel: Taqbeel.",
            "explanation_ur": "باب فَعَّلَ کا مصدر تَفْعِيل کے وزن پر آتا ہے: تَقْبِيلٌ۔", "explanation_en": "Masdar of Form II is Taf'eel: Taqbeel."
        },
        # Tamreen 3: اسم الفاعل واسم المفعول من باب فَعَّلَ (مُعَلِّم / مُعَلَّم)
        {
            "id": "b3_u16_t3_q1", "book": 3, "unit_num": 16, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): اسم فاعل و مفعول از باب تفعیل", "badge_en": "Exercise (3): Form II Participles",
            "tamreen_title_ar": "صَوْغُ اسْمِ الْفَاعِلِ (مُفَعِّل) وَاسْمِ الْمَفْعُولِ (مُفَعَّل) مِنْ بَابِ (فَعَّلَ):",
            "tamreen_title_ur": "باب تفعیل سے اسم فاعل (مکسور العین) اور اسم مفعول (مفتوح العین) بنانا:",
            "tamreen_title_en": "Active participle with kasrah (Mufa''il) vs passive participle with fathah (Mufa''al):",
            "grammar_goal_ur": "مُدَرِّسٌ (اسم فاعل) اور مُدَرَّسٌ (اسم مفعول) کا فرق۔", "grammar_goal_en": "Distinguishing active vs passive participles in Form II.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اسْمُ الْفَاعِلِ مِنَ الْفِعْلِ (عَلَّمَ يُعَلِّمُ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "عَلَّمَ سے سکھانے والے کا اسم فاعل منتخب کریں:", "prompt_en": "Select the active participle of 'Allama (teacher):",
            "answer": "مُعَلِّمٌ (بِكَسْرِ اللامِ)",
            "options": ["مُعَلِّمٌ (بِكَسْرِ اللامِ)", "مُعَلَّمٌ (بِفَتْحِ اللامِ)", "عَالِمٌ", "عَلِيمٌ"],
            "emoji": "👨‍🏫", "hint_ur": "اسم فاعل میں آخری سے پہلے حرف پر زیر آتی ہے: مُعَلِّمٌ۔", "hint_en": "Active participle has kasrah: Mu'allim.",
            "explanation_ur": "غیر ثلاثی میں اسم فاعل میم مضموم اور کسرہ ما قبل آخر سے بنتا ہے: مُعَلِّمٌ۔", "explanation_en": "Form II active participle takes kasrah: Mu'allim."
        }
    ]
    data['b3_u16'] = u16

    # =========================================================================
    # UNIT 17: باب أَفْعَلَ يُفْعِلُ إِفْعَالاً • أفعال تنصب مفعولين • أصبح
    # =========================================================================
    u17 = [
        # Tamreen 1: أسئلة الدرس وفهم النص
        {
            "id": "b3_u17_t1_q1", "book": 3, "unit_num": 17, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "لِمَ لَمْ يَحْضُرْ عُثْمَانُ إِلَى الْمَعْهَدِ الْيَوْمَ؟ [ ＿＿＿ ]",
            "prompt_ur": "عثمان آج معہد میں کیوں حاضر نہیں ہوا؟", "prompt_en": "Why didn't Uthman attend the institute today?",
            "answer": "لِأَنَّهُ مُصَابٌ بِإِسْهَالٍ شَدِيدٍ .",
            "options": ["لِأَنَّهُ مُصَابٌ بِإِسْهَالٍ شَدِيدٍ .", "لِأَنَّهُ سَافَرَ إِلَى كَنَدَا .", "لِأَنَّهُ نَامَ مُتَأَخِّراً .", "لِأَنَّهُ كَانَ فِي الْمَكْتَبَةِ ."],
            "emoji": "🤒", "hint_ur": "کیونکہ وہ شدید بیماری اور پیٹ کی تکلیف میں مبتلا تھا۔", "hint_en": "Because he had severe diarrhea.",
            "explanation_ur": "درست جواب: 'لِأَنَّهُ مُصَابٌ بِإِسْهَالٍ شَدِيدٍ .'۔", "explanation_en": "Correct answer: severe illness."
        },
        # Tamreen 2: باب أَفْعَلَ ومصدره إِفْعَال
        {
            "id": "b3_u17_t2_q1", "book": 3, "unit_num": 17, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): باب إِفْعَال", "badge_en": "Exercise (2): Form IV (Af'ala / If'aal)",
            "tamreen_title_ar": "صَوْغُ الْمَصْدَرِ مِنْ بَابِ (أَفْعَلَ يُفْعِلُ - إِفْعَالاً):",
            "tamreen_title_ur": "باب افعال کا مصدر صریح بنانا:",
            "tamreen_title_en": "Deriving verbal noun on pattern If'aal from Form IV verbs:",
            "grammar_goal_ur": "أَسْلَمَ -> إِسْلَام، أَرْسَلَ -> إِرْسَال، أَغْلَقَ -> إِغْلَاق۔", "grammar_goal_en": "Form IV masdar on pattern If'aal.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَصْدَرُ الْفِعْلِ (أَسْلَمَ يُسْلِمُ) عَلَى وَزْنِ (إِفْعَال) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "أَسْلَمَ يُسْلِمُ کا مصدر منتخب کریں:", "prompt_en": "Select the verbal noun of Aslama (If'aal):",
            "answer": "إِسْلَامٌ",
            "options": ["إِسْلَامٌ", "سَلَامٌ", "تَسْلِيمٌ", "مُسْلِمٌ"],
            "emoji": "🕌", "hint_ur": "إِفْعَال کے وزن پر 'إِسْلَامٌ' آئے گا۔", "hint_en": "Pattern If'aal: Islaam.",
            "explanation_ur": "باب أَفْعَلَ کا مصدر إِفْعَال کے وزن پر آتا ہے: إِسْلَامٌ۔", "explanation_en": "Masdar of Form IV is If'aal: Islaam."
        },
        # Tamreen 3: أفعال تنصب مفعولين (أَعْطَى)
        {
            "id": "b3_u17_t3_q1", "book": 3, "unit_num": 17, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): أفعال تنصب مفعولين", "badge_en": "Exercise (3): Verbs Taking Two Objects",
            "tamreen_title_ar": "تَعَدِّي الْفِعْلِ (أَعْطَى) إِلَى مَفْعُولَيْنِ اثْنَيْنِ:",
            "tamreen_title_ur": "فعل (أعطى) کا دو مفعولوں کو نصب دینا:",
            "tamreen_title_en": "The verb A'taa governing two accusative objects:",
            "grammar_goal_ur": "أَعْطَيْتُ حَامِداً كِتَاباً (حامداً مفعول اول، کتاباً مفعول ثانی)۔", "grammar_goal_en": "Both objects of A'taa are Mansub.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَعْطَى الْمُدَرِّسُ [ ＿＿＿ ] [ ＿＿＿ ] .",
            "prompt_ur": "استاد نے حامد کو کتاب دی (دونوں مفعولوں کا درست اعراب چنیں):", "prompt_en": "The teacher gave Hamid a book (select two accusative objects):",
            "answer": "حَامِداً ... كِتَاباً",
            "options": [
                "حَامِداً ... كِتَاباً",
                "حَامِدٌ ... كِتَابٌ",
                "حَامِدٍ ... كِتَابٍ",
                "حَامِداً ... كِتَابٌ"
            ],
            "emoji": "📖", "hint_ur": "أعطى کے دونوں مفعول منسوب (دو زبر والے) ہوتے ہیں۔", "hint_en": "Both objects are Mansub: Haamidan ... Kitaaban.",
            "explanation_ur": "أعطى دو مفعولوں کو نصب دیتا ہے: أَعْطَيْتُ حَامِداً كِتَاباً۔", "explanation_en": "A'taa governs two direct objects."
        },
        # Tamreen 4: أصبح من أخوات كان
        {
            "id": "b3_u17_t4_q1", "book": 3, "unit_num": 17, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): أَصْبَحَ (اخوات كان)", "badge_en": "Exercise (4): Asbaha (Sister of Kaana)",
            "tamreen_title_ar": "عَمَلُ (أَصْبَحَ) مِنْ أَخَوَاتِ كَانَ:",
            "tamreen_title_ur": "أصبح کا عمل (اسم کو رفع اور خبر کو نصب دینا):",
            "tamreen_title_en": "Syntax of Asbaha: nominative subject and accusative predicate:",
            "grammar_goal_ur": "أَصْبَحَ حَامِدٌ مَرِيضاً (حامد صبح کے وقت بیمار ہو گیا)۔", "grammar_goal_en": "Asbaha operates like Kaana.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَصْبَحَ الْجَوُّ [ ＿＿＿ ] هٰذَا الصَّبَاحَ .",
            "prompt_ur": "آج صبح موسم ٹھنڈا ہو گیا (أصبح کی خبر منسوب چنیں):", "prompt_en": "The weather became cold this morning (select accusative predicate):",
            "answer": "بَارِداً",
            "options": ["بَارِداً", "بَارِدٌ", "بَارِدٍ", "الْبَارِدُ"],
            "emoji": "❄️", "hint_ur": "أصبح کی خبر منسوب ہوتی ہے: بَارِداً۔", "hint_en": "Predicate of Asbaha is Mansub: Baaridan.",
            "explanation_ur": "أصبح کان کی بہنوں میں سے ہے، اس کی خبر منسوب ہوتی ہے: أَصْبَحَ الْجَوُّ بَارِداً۔", "explanation_en": "Asbaha acts like Kaana, governing accusative: Baaridan."
        }
    ]
    data['b3_u17'] = u17

    return data

if __name__ == '__main__':
    d = get_b3_units_10_to_17_complete()
    for k in sorted(d.keys()):
        print(f"Book 3 {k}: {len(d[k])} questions")
