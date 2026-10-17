# -*- coding: utf-8 -*-
"""
Full Authentic Curriculum Generator for Madinah Book 3 (Units 10 to 17)
Every unit structured with authentic multi-tamreen exercises matching the textbook.
"""

def get_b3_units_10_to_17_deep():
    data = {}

    # -------------------------------------------------------------
    # UNIT 10: الجملتان الاسمية والفعلية والمصدر المؤول
    # -------------------------------------------------------------
    u10 = []
    # T1: تمييز الجملة الاسمية والفعلية
    t1_u10 = [
        ("الْجُمْلَةُ فِي: (اللَّهُ نُورُ السَّمَاوَاتِ وَالأَرْضِ) هِيَ جُمْلَةٌ: [ ＿＿＿ ]", "اسْمِيَّةٌ (تَبْدَأُ بِاسْمٍ)", ["اسْمِيَّةٌ (تَبْدَأُ بِاسْمٍ)", "فِعْلِيَّةٌ", "شِبْهُ جُمْلَةٍ", "ظَرْفِيَّةٌ"], "جو جملہ اسم سے شروع ہو وہ جملہ اسمیہ کہلاتا ہے۔", "A sentence beginning with a noun is a nominal sentence.", "✨"),
        ("الْجُمْلَةُ فِي: (خَلَقَ اللَّهُ كُلَّ شَيْءٍ) هِيَ جُمْلَةٌ: [ ＿＿＿ ]", "فِعْلِيَّةٌ (تَبْدَأُ بِفِعْلٍ)", ["فِعْلِيَّةٌ (تَبْدَأُ بِفِعْلٍ)", "اسْمِيَّةٌ", "شِبْهُ جُمْلَةٍ", "حَالِيَّةٌ"], "جو جملہ فعل سے شروع ہو وہ جملہ فعلیہ کہلاتا ہے۔", "A sentence beginning with a verb is a verbal sentence.", "🌍"),
        ("تَتَكَوَّنُ الْجُمْلَةُ الاسْمِيَّةُ الأَسَاسِيَّةُ مِنْ: [ ＿＿＿ ]", "مُبْتَدَأٍ وَخَبَرٍ", ["مُبْتَدَأٍ وَخَبَرٍ", "فِعْلٍ وَفَاعِلٍ", "فِعْلٍ وَمَفْعُولٍ", "جَارٍّ وَمَجْرُورٍ"], "جملہ اسمیہ کے بنیادی ارکان مبتدا اور خبر ہیں۔", "The core components of a nominal sentence are subject and predicate.", "⚖️")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u10, 1):
        u10.append({
            "id": f"b3_u10_t1_q{idx}", "book": 3, "unit_num": 10, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): جملہ اسمیہ و فعلیہ", "badge_en": "Exercise (1): Nominal vs Verbal Sentences",
            "tamreen_title_ar": "التَّمْيِيزُ بَيْنَ الْجُمْلَةِ الاسْمِيَّةِ وَالْفِعْلِيَّةِ:",
            "tamreen_title_ur": "جملہ اسمیہ اور فعلیہ کی پہچان اور ارکان کا فہم:",
            "tamreen_title_en": "Distinguishing nominal from verbal sentences and their core components:",
            "grammar_goal_ur": "عربی جملے کی دو بنیادی اقسام کا ادراک۔",
            "grammar_goal_en": "Understanding the two fundamental sentence types in Arabic syntax.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست قسم منتخب کریں:", "prompt_en": "Select the correct sentence type:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: المصدر المؤول
    t2_u10 = [
        ("تَقْدِيرُ الْمَصْدَرِ الْمُؤَوَّلِ فِي: (أُرِيدُ أَنْ أَذْهَبَ) بِالْمَصْدَرِ الصَّرِيحِ هُوَ: [ ＿＿＿ ]", "أُرِيدُ الذَّهَابَ", ["أُرِيدُ الذَّهَابَ", "أُرِيدُ ذَاهِباً", "أُرِيدُ أَنْ يَذْهَبَ", "أُرِيدُ مَذْهَباً"], "'أن' ناصبہ اپنے فعل کے ساتھ مل کر مصدر صریح (الذهاب) کی تاویل میں ہوتا ہے۔", "'An' + present verb is interpreted as the masdar: Ureedu ath-thahaba.", "🚶‍♂️"),
        ("مَحَلُّ الْمَصْدَرِ الْمُؤَوَّلِ فِي: (يَسُرُّنِي أَنْ تَنْجَحَ) مِنَ الإِعْرَابِ: [ ＿＿＿ ]", "فِي مَحَلِّ رَفْعٍ فَاعِلٌ (يَسُرُّنِي نَجَاحُكَ)", ["فِي مَحَلِّ رَفْعٍ فَاعِلٌ (يَسُرُّنِي نَجَاحُكَ)", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "فِي مَحَلِّ جَرٍّ", "خَبَرٌ"], "فاعل مؤول ہے: 'مجھے تمہاری کامیابی خوش کرتی ہے'۔", "The interpreted masdar is in the nominative state as the subject (Fa'il).", "🎉"),
        ("مَحَلُّ الْمَصْدَرِ الْمُؤَوَّلِ فِي: (أَرْجُو أَنْ تَغْفِرَ لِي) هُوَ: [ ＿＿＿ ]", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ (أَرْجُو مَغْفِرَتَكَ)", ["فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ (أَرْجُو مَغْفِرَتَكَ)", "فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "فِي مَحَلِّ جَرٍّ بِحَرْفِ الْجَرِّ", "مُبْتَدَأٌ"], "مفعول به مؤول ہے: أرجو مغفرتك۔", "The interpreted masdar is the object (Maf'ool bihi).", "🤲")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u10, 1):
        u10.append({
            "id": f"b3_u10_t2_q{idx}", "book": 3, "unit_num": 10, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مصدر مؤول", "badge_en": "Exercise (2): The Interpreted Infinitive (Al-Masdar al-Mu'awwal)",
            "tamreen_title_ar": "أَحْكَامُ الْمَصْدَرِ الْمُؤَوَّلِ مِنْ (أَنْ + الْفِعْلِ):",
            "tamreen_title_ur": "مصدر مؤول کو مصدر صریح میں بدلنا اور اس کا اعرابی محل:",
            "tamreen_title_en": "Interpreting Masdar Mu'awwal and determining its syntactic position:",
            "grammar_goal_ur": "أن ناصبہ اور فعل سے مل کر بننے والے مصدر کے نحوی مقام کا فہم۔",
            "grammar_goal_en": "Mastering the syntactic role of Masdar Mu'awwal as subject or object.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست اعرابی محل منتخب کریں:", "prompt_en": "Select the correct syntactic role:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u10'] = u10

    # -------------------------------------------------------------
    # UNIT 11: المبتدأ والخبر وأنواع الخبر • تقديم الخبر
    # -------------------------------------------------------------
    u11 = []
    # T1: أنواع الخبر
    t1_u11 = [
        ("نَوْعُ الْخَبَرِ فِي جُمْلَةِ: (الْقُرْآنُ كِتَابُ اللَّهِ) هُوَ: [ ＿＿＿ ]", "مُفْرَدٌ", ["مُفْرَدٌ", "جُمْلَةٌ اسْمِيَّةٌ", "جُمْلَةٌ فِعْلِيَّةٌ", "شِبْهُ جُمْلَةٍ"], "خبر جملہ یا شبہ جملہ نہیں بلکہ اسم مفرد (مضاف) ہے: كِتَابُ۔", "The predicate is a single term (Mufrad): Kitaab.", "📖"),
        ("نَوْعُ الْخَبَرِ فِي جُمْلَةِ: (الطَّالِبُ يَقْرَأُ الْقُرْآنَ) هُوَ: [ ＿＿＿ ]", "جُمْلَةٌ فِعْلِيَّةٌ (يَقْرَأُ)", ["جُمْلَةٌ فِعْلِيَّةٌ (يَقْرَأُ)", "مُفْرَدٌ", "جُمْلَةٌ اسْمِيَّةٌ", "شِبْهُ جُمْلَةٍ"], "فعل اور فاعل پر مشتمل جملہ فعلیہ خبر بن رہا ہے: يَقْرَأُ۔", "The predicate is a verbal sentence (Yaqra'u).", "👨‍🎓"),
        ("نَوْعُ الْخَبَرِ فِي جُمْلَةِ: (الْمُدَرِّسُ فِي الْفَصْلِ) هُوَ: [ ＿＿＿ ]", "شِبْهُ جُمْلَةٍ (جَارٌّ وَمَجْرُورٌ)", ["شِبْهُ جُمْلَةٍ (جَارٌّ وَمَجْرُورٌ)", "مُفْرَدٌ", "جُمْلَةٌ اسْمِيَّةٌ", "جُمْلَةٌ فِعْلِيَّةٌ"], "جار و مجرور شبہ جملہ بن کر خبر واقع ہوا ہے: فِي الْفَصْلِ۔", "The predicate is a semi-sentence (prepositional phrase): Fi al-fasli.", "🏫")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u11, 1):
        u11.append({
            "id": f"b3_u11_t1_q{idx}", "book": 3, "unit_num": 11, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): خبر کی اقسام", "badge_en": "Exercise (1): Types of Predicates",
            "tamreen_title_ar": "أَنْوَاعُ الْخَبَرِ (مُفْرَدٌ، جُمْلَةٌ، شِبْهُ جُمْلَةٍ):",
            "tamreen_title_ur": "خبر کی تینوں اقسام (مفرد، جملہ، شبہ جملہ) کی پہچان کریں:",
            "tamreen_title_en": "Identify types of predicates (single, sentence, semi-sentence):",
            "grammar_goal_ur": "مبتدا کی خبر کی مختلف ساختوں کا فہم۔",
            "grammar_goal_en": "Mastering the structural varieties of predicates in Arabic.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "خبر کی درست قسم منتخب کریں:", "prompt_en": "Select the correct predicate type:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: تقديم الخبر وجوباً
    t2_u11 = [
        ("فِي جُمْلَةِ: (فِي الدَّارِ رَجُلٌ)، حُكْمُ تَقْدِيمِ الْخَبَرِ (فِي الدَّارِ): [ ＿＿＿ ]", "وَاجِبٌ (لِأَنَّ الْمُبْتَدَأَ نَكِرَةٌ وَالْخَبَرَ شِبْهُ جُمْلَةٍ)", ["وَاجِبٌ (لِأَنَّ الْمُبْتَدَأَ نَكِرَةٌ وَالْخَبَرَ شِبْهُ جُمْلَةٍ)", "جَائِزٌ", "مَمْنُوعٌ", "مَكْرُوهٌ"], "جب مبتدا نکرہ اور خبر شبہ جملہ ہو تو خبر کو پہلے لانا واجب ہے۔", "When subject is indefinite and predicate is a prepositional phrase, advancing the predicate is obligatory.", "🏠"),
        ("فِي جُمْلَةِ: (أَيْنَ الْمُدَرِّسُ؟)، حُكْمُ تَقْدِيمِ (أَيْنَ): [ ＿＿＿ ]", "وَاجِبٌ (لِأَنَّ اسْمَ الِاسْتِفْهَامِ لَهُ صَدَارَةُ الْكَلاَمِ)", ["وَاجِبٌ (لِأَنَّ اسْمَ الِاسْتِفْهَامِ لَهُ صَدَارَةُ الْكَلاَمِ)", "جَائِزٌ", "مَمْنُوعٌ", "تَوْكِيدٌ"], "اسم استفہام کلام کے شروع میں آنا ضروری ہوتا ہے۔", "Interrogative nouns must take the beginning of the sentence.", "❓")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u11, 1):
        u11.append({
            "id": f"b3_u11_t2_q{idx}", "book": 3, "unit_num": 11, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تقدیم الخبر", "badge_en": "Exercise (2): Advancing the Predicate",
            "tamreen_title_ar": "أَحْكَامُ تَقْدِيمِ الْخَبَرِ عَلَى الْمُبْتَدَأِ وُجُوباً:",
            "tamreen_title_ur": "خبر کو مبتدا پر مقدم کرنے کے وجوبی اسباب پہچانیں:",
            "tamreen_title_en": "Identify mandatory reasons for advancing the predicate before the subject:",
            "grammar_goal_ur": "نحوی وجوب اور صدراعظم کلمات کے احکام کا فہم۔",
            "grammar_goal_en": "Understanding obligatory predicate-fronting rules.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست نحوی حکم منتخب کریں:", "prompt_en": "Select the correct ruling:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u11'] = u11

    # -------------------------------------------------------------
    # UNIT 12: المفعول فيه (ظرف الزمان والمكان)
    # -------------------------------------------------------------
    u12 = []
    # T1: تمييز ظرف الزمان وظرف المكان
    t1_u12 = [
        ("كَلِمَةُ (صَبَاحاً) فِي: (سَافَرْتُ صَبَاحاً) هِيَ: [ ＿＿＿ ]", "ظَرْفُ زَمَانٍ (مَفْعُولٌ فِيهِ) مَنْصُوبٌ", ["ظَرْفُ زَمَانٍ (مَفْعُولٌ فِيهِ) مَنْصُوبٌ", "ظَرْفُ مَكَانٍ", "مَفْعُولٌ بِهِ", "حَالٌ"], "صباحاً وقت کو ظاہر کر رہا ہے اس لیے ظرف زمان مفعول فیہ ہے۔", "Sabahan denotes time, so it is an adverb of time (Maf'ool feeh).", "🌅"),
        ("كَلِمَةُ (أَمَامَ) فِي: (جَلَسْتُ أَمَامَ الْمَسْجِدِ) هِيَ: [ ＿＿＿ ]", "ظَرْفُ مَكَانٍ مَنْصُوبٌ", ["ظَرْفُ مَكَانٍ مَنْصُوبٌ", "ظَرْفُ زَمَانٍ", "حَرْفُ جَرٍّ", "مُبْتَدَأٌ"], "أمام جگہ ظاہر کر رہا ہے اس لیے ظرف مکان ہے۔", "Amama denotes place, so it is an adverb of place.", "🕌"),
        ("كَلِمَةُ (حَيْثُ) فِي: (قِفْ حَيْثُ أَمَرْتُكَ) هِيَ: [ ＿＿＿ ]", "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ", ["ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ", "ظَرْفٌ مُعْرَبٌ مَنْصُوبٌ", "حَرْفُ جَزْمٍ", "اسْمٌ مَوْصُولٌ"], "حيثُ ضمہ پر مبنی ظرف مکان ہے۔", "Haythu is an adverb of place Mabni on Dammah.", "📍")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u12, 1):
        u12.append({
            "id": f"b3_u12_t1_q{idx}", "book": 3, "unit_num": 12, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): ظروف زمان و مکان", "badge_en": "Exercise (1): Adverbs of Time and Place",
            "tamreen_title_ar": "تَمْيِيزُ ظُرُوفِ الزَّمَانِ وَالْمَكَانِ (الْمَفْعُولُ فِيهِ):",
            "tamreen_title_ur": "ظرف زمان اور ظرف مکان کی پہچان اور اعراب:",
            "tamreen_title_en": "Distinguish adverbs of time and place (Maf'ool feeh):",
            "grammar_goal_ur": "مفعول فیہ کے معانی اور اعرابی احکام کا فہم۔",
            "grammar_goal_en": "Mastering the syntax and semantics of adverbs in Arabic.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست قسم منتخب کریں:", "prompt_en": "Select the correct category:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: ما ينوب عن الظرف
    t2_u12 = [
        ("فِي جُمْلَةِ: (مَكَثْتُ فِي مَكَّةَ أَرْبَعَةَ أَيَّامٍ)، كَلِمَةُ (أَرْبَعَةَ) هِيَ: [ ＿＿＿ ]", "نَائِبٌ عَنِ الظَّرْفِ مَنْصُوبٌ", ["نَائِبٌ عَنِ الظَّرْفِ مَنْصُوبٌ", "مَفْعُولٌ بِهِ", "تَمْيِيزٌ", "مُضَافٌ إِلَيْهِ"], "عدد جب ظرف کی طرف مضاف ہو تو ظرف کی نیابت کرتا ہے۔", "A number prefixed to a time word acts as deputy adverb.", "📅"),
        ("فِي جُمْلَةِ: (صَبَرْتُ طَوِيلاً)، تَقْدِيرُ الْكَلاَمِ هُوَ: [ ＿＿＿ ]", "صَبَرْتُ وَقْتاً طَوِيلاً (صِفَةُ الظَّرْفِ نَابَتْ عَنْهُ)", ["صَبَرْتُ وَقْتاً طَوِيلاً (صِفَةُ الظَّرْفِ نَابَتْ عَنْهُ)", "صَبَرْتُ صَبْراً طَوِيلاً", "طَالَ صَبْرِي", "صَبَرْتُ مَكَاناً"], "صفت نے ظرف محذوف (وقتاً) کی نیابت کی۔", "The adjective 'Taweelan' stands in for the omitted adverb 'Waqtan'.", "⏳")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u12, 1):
        u12.append({
            "id": f"b3_u12_t2_q{idx}", "book": 3, "unit_num": 12, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): نائب عن الظرف", "badge_en": "Exercise (2): Deputy Adverbs",
            "tamreen_title_ar": "مَا يَنُوبُ عَنِ الظَّرْفِ (الْعَدَدُ وَالصِّفَةُ):",
            "tamreen_title_ur": "ظرف کی جگہ استعمال ہونے والے کلمات (عدد، صفت):",
            "tamreen_title_en": "Words acting as deputy adverbs (numbers and adjectives):",
            "grammar_goal_ur": "ظرف کے حذف اور اس کے نائبین کے قواعد کا فہم۔",
            "grammar_goal_en": "Understanding deputy adverbs in Arabic syntax.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست نحوی حیثیت منتخب کریں:", "prompt_en": "Select the correct syntactic role:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u12'] = u12

    # -------------------------------------------------------------
    # UNIT 13: لام الأمر والجزم بالطلب والندبة
    # -------------------------------------------------------------
    u13 = []
    # T1: لام الأمر
    t1_u13 = [
        ("عَمَلُ (لاَمِ الأَمْرِ) عِنْدَ دُخُولِهَا عَلَى الْفِعْلِ الْمُضَارِعِ هُوَ: [ ＿＿＿ ]", "جَزْمُ الْفِعْلِ الْمُضَارِعِ (لِيَكْتُبْ)", ["جَزْمُ الْفِعْلِ الْمُضَارِعِ (لِيَكْتُبْ)", "نَصْبُ الْفِعْلِ الْمُضَارِعِ", "رَفْعُهُ", "جَرُّهُ"], "لام الامر مضارع کو جزم دیتی ہے: لِيَكْتُبْ۔", "The Lam of command (Lam al-Amr) puts the present tense verb into the jussive (Jazm).", "✍️"),
        ("كَيْفَ تُضْبَطُ (لاَمُ الأَمْرِ) إِذَا سَبَقَتْهَا الْوَاوُ أَوْ الْفَاءُ؟ [ ＿＿＿ ]", "تُسَكَّنُ (وَلْيَكْتُبْ، فَلْيَجْلِسْ)", ["تُسَكَّنُ (وَلْيَكْتُبْ، فَلْيَجْلِسْ)", "تُكْسَرُ دَائِماً", "تُفْتَحُ", "تُضَمُّ"], "واو یا فاء کے بعد لام الامر پر سکون پڑھا جاتا ہے: وَلْيَكْتُبْ۔", "After Waw or Faa, Lam al-Amr takes Sukun: Wal-yaktub, Fal-yajlis.", "📜"),
        ("فِي جُمْلَةِ: (لِيَذْهَبِ الطُّلَّابُ إِلَى الْمُدِيرِ)، تُفِيدُ اللاَّمُ: [ ＿＿＿ ]", "الأَمْرَ لِلْغَائِبِ", ["الأَمْرَ لِلْغَائِبِ", "التَّعْلِيلَ", "التَّوْكِيدَ", "النَّفْيَ"], "غائب کو حکم دینے کے لیے لام الامر استعمال ہوتی ہے۔", "Lam al-Amr issues a command to a 3rd person (absent) subject.", "👥")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u13, 1):
        u13.append({
            "id": f"b3_u13_t1_q{idx}", "book": 3, "unit_num": 13, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): لام الامر", "badge_en": "Exercise (1): The Imperative Lam (Lam al-Amr)",
            "tamreen_title_ar": "أَحْكَامُ لاَمِ الأَمْرِ وَجَزْمُ الْمُضَارِعِ بِهَا:",
            "tamreen_title_ur": "لام الامر کا مضارع پر عمل اور اس کے ضبط کے قواعد:",
            "tamreen_title_en": "Rules of Lam al-Amr and its jussive effect on verbs:",
            "grammar_goal_ur": "لام الامر کے حرکات اور غائب کو حکم دینے کے طریقے کا فہم۔",
            "grammar_goal_en": "Understanding the vocalization and jussive syntax of Lam al-Amr.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست حکم منتخب کریں:", "prompt_en": "Select the correct ruling:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: الجزم في جواب الطلب وأسلوب الندبة
    t2_u13 = [
        ("إِعْرَابُ الْفِعْلِ (تَنْجَحْ) فِي: (اجْتَهِدْ تَنْجَحْ) هُوَ: [ ＿＿＿ ]", "مَجْزُومٌ فِي جَوَابِ الطَّلَبِ", ["مَجْزُومٌ فِي جَوَابِ الطَّلَبِ", "مَرْفُوعٌ بِالضَّمَّةِ", "مَنْصُوبٌ بِالْفَتْحَةِ", "مَبْنِيٌّ"], "امر یا نہی کے جواب میں مضارع جزم لیتا ہے: اجتهد تنجحْ۔", "The verb in response to a command is in the jussive (Jazm fi jawab at-talab).", "🎯"),
        ("أُسْلُوبُ النُّدْبَةِ فِي اللُّغَةِ مِثْلُ: (وَا رَأْسَاهُ!) يُفِيدُ: [ ＿＿＿ ]", "التَّفَجُّعَ وَالتَّوَجُّعَ مِنَ الأَلَمِ", ["التَّفَجُّعَ وَالتَّوَجُّعَ مِنَ الأَلَمِ", "التَّرَجِّيَ", "التَّشْبِيهَ", "الاسْتِفْهَامَ"], "ندبہ درد اور صدمے کے اظہار کے لیے پکارنے کا نام ہے۔", "Nudbah expresses grief or pain using 'Waa...'.", "🤕")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u13, 1):
        u13.append({
            "id": f"b3_u13_t2_q{idx}", "book": 3, "unit_num": 13, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جواب طلب اور ندبہ", "badge_en": "Exercise (2): Jawab at-Talab & Nudbah",
            "tamreen_title_ar": "الْجَزْمُ فِي جَوَابِ الطَّلَبِ وَأُسْلُوبُ النُّدْبَةِ:",
            "tamreen_title_ur": "جواب طلب میں جزم اور اسلوب ندبہ کی پہچان:",
            "tamreen_title_en": "Jussive in response to demands and the style of lamentation (Nudbah):",
            "grammar_goal_ur": "طلب کے بعد نتیجے پر جزم آنے کے شرائط کا فہم۔",
            "grammar_goal_en": "Mastering conditional responses to imperatives and lamentations.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست جواب چنیں:", "prompt_en": "Select the correct answer:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u13'] = u13

    # -------------------------------------------------------------
    # UNIT 14: أدوات الشرط غير الجازمة (إذا، لو، لولا، كلما)
    # -------------------------------------------------------------
    u14 = []
    # T1: أدوات الشرط غير الجازمة
    t1_u14 = [
        ("أَيُّ الأَدَوَاتِ الآتِيَةِ أَدَاةُ شَرْطٍ غَيْرُ جَازِمَةٍ؟ [ ＿＿＿ ]", "إِذَا", ["إِذَا", "إِنْ", "مَنْ", "مَهْمَا"], "إذا شرط کے معنی والا ظرف ہے لیکن جزم نہیں دیتا۔", "Itha is a non-jussive conditional tool denoting future time.", "⏳"),
        ("أَدَاةُ الشَّرْطِ (لَوْ) تُفِيدُ فِي اللُّغَةِ: [ ＿＿＿ ]", "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ (امْتِنَاعُ الْجَوَابِ لِامْتِنَاعِ الشَّرْطِ)", ["حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ (امْتِنَاعُ الْجَوَابِ لِامْتِنَاعِ الشَّرْطِ)", "حَرْفُ امْتِنَاعٍ لِوُجُودٍ", "حَرْفُ جَزْمٍ", "حَرْفُ نَصْبٍ"], "لو: شرط نہ پائے جانے کی وجہ سے جزا بھی نہ پائی گئی: لَوْ جَاءَ لَأَكْرَمْتُهُ۔", "'Law' is a particle of withholding due to withholding (counterfactual condition).", "🛑"),
        ("أَدَاةُ الشَّرْطِ (لَوْلاَ) تُفِيدُ فِي اللُّغَةِ: [ ＿＿＿ ]", "حَرْفُ امْتِنَاعٍ لِوُجُودٍ (امْتِنَاعُ الْجَوَابِ لِوُجُودِ الشَّرْطِ)", ["حَرْفُ امْتِنَاعٍ لِوُجُودٍ (امْتِنَاعُ الْجَوَابِ لِوُجُودِ الشَّرْطِ)", "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ", "حَرْفُ جَزْمٍ", "حَرْفُ اسْتِفْهَامٍ"], "لولا: شرط کی موجودگی کی وجہ سے جزا رک گئی: لَوْلاَ الإِسْلاَمُ لَهَلَكْنَا۔", "'Lawla' denotes prevention of the result due to existence of the condition.", "🛡️")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u14, 1):
        u14.append({
            "id": f"b3_u14_t1_q{idx}", "book": 3, "unit_num": 14, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): ادوات شرط غیر جازمہ", "badge_en": "Exercise (1): Non-Jussive Conditional Particles",
            "tamreen_title_ar": "مَعَانِي أَدَوَاتِ الشَّرْطِ غَيْرِ الْجَازِمَةِ (إِذَا، لَوْ، لَوْلاَ):",
            "tamreen_title_ur": "ادواتِ شرط غیر جازمہ کے معانی اور بلاغی مفاہیم:",
            "tamreen_title_en": "Meanings of non-jussive conditional tools (Itha, Law, Lawla):",
            "grammar_goal_ur": "غیر جازم شرطیہ ادوات کے باہمی معنوی فرق کا فہم۔",
            "grammar_goal_en": "Understanding nuances of non-jussive conditional particles.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست معنی منتخب کریں:", "prompt_en": "Select the correct meaning:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: حذف الخبر بعد لولا
    t2_u14 = [
        ("فِي جُمْلَةِ: (لَوْلاَ الْمَطَرُ لَهَلَكَ الزَّرْعُ)، حُكْمُ حَذْفِ خَبَرِ (الْمَطَرُ): [ ＿＿＿ ]", "وَاجِبٌ (تَقْدِيرُهُ: لَوْلاَ الْمَطَرُ مَوْجُودٌ)", ["وَاجِبٌ (تَقْدِيرُهُ: لَوْلاَ الْمَطَرُ مَوْجُودٌ)", "جَائِزٌ", "مَمْنُوعٌ", "مَكْرُوهٌ"], "لولا کے بعد مبتدا کا عام خبر (موجود) ہمیشہ وجوبی طور پر حذف ہوتا ہے۔", "After 'Lawla', the predicate is obligatorily omitted (implied: mawjood).", "🌧️")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u14, 1):
        u14.append({
            "id": f"b3_u14_t2_q{idx}", "book": 3, "unit_num": 14, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): لولا کے بعد خبر کا حذف", "badge_en": "Exercise (2): Omission of Predicate after Lawla",
            "tamreen_title_ar": "حَذْفُ الْخَبَرِ وُجُوباً بَعْدَ (لَوْلاَ):",
            "tamreen_title_ur": "لولا کے بعد مبتدا کی خبر کے وجوبی حذف کا قاعدہ:",
            "tamreen_title_en": "Obligatory omission of the predicate following Lawla:",
            "grammar_goal_ur": "لولا کے بعد آنے والے جملہ اسمیہ کے نحوی تقاضوں کا فہم۔",
            "grammar_goal_en": "Understanding the syntax of subjects following Lawla.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست حکم چنیں:", "prompt_en": "Select the correct ruling:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u14'] = u14

    # -------------------------------------------------------------
    # UNIT 15: أدوات الشرط الجازمة • حتى • كم الخبرية
    # -------------------------------------------------------------
    u15 = []
    # T1: أدوات الشرط الجازمة لفعلين
    t1_u15 = [
        ("كَمْ فِعْلاً تَجْزِمُ أَدَوَاتُ الشَّرْطِ الْجَازِمَةُ مِثْلُ (إِنْ، مَنْ، مَا)؟ [ ＿＿＿ ]", "تَجْزِمُ فِعْلَيْنِ (فِعْلَ الشَّرْطِ وَجَوَابَ الشَّرْطِ)", ["تَجْزِمُ فِعْلَيْنِ (فِعْلَ الشَّرْطِ وَجَوَابَ الشَّرْطِ)", "تَجْزِمُ فِعْلاً وَاحِداً", "تَنْصِبُ فِعْلَيْنِ", "تَرْفَعُ فِعْلَيْنِ"], "یہ ادوات دو فعلوں کو جزم دیتی ہیں: فعل شرط اور جواب شرط۔", "These conditional particles put two verbs in the jussive: condition and response.", "⚡"),
        ("فِي الآيَةِ: {مَنْ يَعْمَلْ سُوءاً يُجْزَ بِهِ}، عَلَامَةُ جَزْمِ جَوَابِ الشَّرْطِ (يُجْزَ) هِيَ: [ ＿＿＿ ]", "حَذْفُ حَرْفِ الْعِلَّةِ (الأَلِفِ)", ["حَذْفُ حَرْفِ الْعِلَّةِ (الأَلِفِ)", "السُّكُونُ", "الْفَتْحَةُ", "حَذْفُ النُّونِ"], "یجزی ناقص تھا، جزم کی وجہ سے حرف علت الف گر گیا: يُجْزَ۔", "Weak ending dropped due to Jazm: Yujza.", "⚖️"),
        ("فِي جُمْلَةِ: (إِنْ تَجْتَهِدُوا تَنْجَحُوا)، عَلَامَةُ الْجَزْمِ فِي الْفِعْلَيْنِ هِيَ: [ ＿＿＿ ]", "حَذْفُ النُّونِ (لِأَنَّهُمَا مِنَ الأَفْعَالِ الْخَمْسَةِ)", ["حَذْفُ النُّونِ (لِأَنَّهُمَا مِنَ الأَفْعَالِ الْخَمْسَةِ)", "السُّكُونُ", "الْوَاوُ", "حَذْفُ حَرْفِ الْعِلَّةِ"], "افعال خمسہ کا جزم نون گرنے سے ہوتا ہے: تجتهدوا / تنجحوا۔", "Jazm marker in Five Verbs is dropping the Nun: Tajtahidu / Tanjahu.", "👥")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u15, 1):
        u15.append({
            "id": f"b3_u15_t1_q{idx}", "book": 3, "unit_num": 15, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): ادوات شرط جازمہ", "badge_en": "Exercise (1): Jussive Conditional Tools",
            "tamreen_title_ar": "أَدَوَاتُ الشَّرْطِ الْجَازِمَةُ لِفِعْلَيْنِ وَعَلاَمَاتُ الْجَزْمِ:",
            "tamreen_title_ur": "دو فعلوں کو جزم دینے والے ادوات اور جزم کی علامات پہچانیں:",
            "tamreen_title_en": "Conditional tools governing two jussive verbs and their case markers:",
            "grammar_goal_ur": "شرط اور جزا کے اعرابی عمل اور علامات کا فہم۔",
            "grammar_goal_en": "Mastering the double-jussive conditional construction.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست جواب منتخب کریں:", "prompt_en": "Select the correct option:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: كم الخبرية والاستفهامية
    t2_u15 = [
        ("كَمِ الِاسْتِفْهَامِيَّةُ يَكُونُ تَمْيِيزُهَا: [ ＿＿＿ ]", "مُفْرَداً مَنْصُوباً (كَمْ كِتَاباً عِنْدَكَ؟)", ["مُفْرَداً مَنْصُوباً (كَمْ كِتَاباً عِنْدَكَ؟)", "جَمْعاً مَجْرُوراً", "مُفْرَداً مَرْفُوعاً", "جَمْعاً مَرْفُوعاً"], "کم استفہامیہ کا تمییز مفرد منسوب ہوتا ہے۔", "Interrogative 'Kam' takes an accusative singular specification: Kam kitaban.", "❓"),
        ("كَمِ الْخَبَرِيَّةُ (الَّتِي تُفِيدُ التَّكْثِيرَ) يَكُونُ تَمْيِيزُهَا: [ ＿＿＿ ]", "مَجْرُوراً مُفْرَداً أَوْ جَمْعاً (كَمْ كِتَابٍ / كَمْ كُتُبٍ قَرَأْتُ!)", ["مَجْرُوراً مُفْرَداً أَوْ جَمْعاً (كَمْ كِتَابٍ / كَمْ كُتُبٍ قَرَأْتُ!)", "مَنْصُوباً دَائِماً", "مَرْفُوعاً", "سَاكِناً"], "کم خبریہ کثرت بتاتی ہے اور اس کا تمییز مجرور ہوتا ہے۔", "Exclamatory 'Kam' denotes abundance and takes a genitive noun.", "📚")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u15, 1):
        u15.append({
            "id": f"b3_u15_t2_q{idx}", "book": 3, "unit_num": 15, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): کم خبریہ و استفہامیہ", "badge_en": "Exercise (2): Exclamatory vs Interrogative Kam",
            "tamreen_title_ar": "الْفَرْقُ بَيْنَ (كَمِ الاسْتِفْهَامِيَّةِ) وَ(كَمِ الْخَبَرِيَّةِ):",
            "tamreen_title_ur": "کم استفہامیہ اور کم خبریہ کے اعراب اور مفہوم میں فرق:",
            "tamreen_title_en": "Distinguishing between interrogative and exclamatory Kam:",
            "grammar_goal_ur": "کم کی دونوں انواع کے تمییز کے اعراب کی تفریق۔",
            "grammar_goal_en": "Differentiating syntactic cases of nouns governed by Kam.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست ضابطہ منتخب کریں:", "prompt_en": "Select the correct rule:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u15'] = u15

    # -------------------------------------------------------------
    # UNIT 16: المجرد والمزيد • باب فَعَّلَ (تَفْعِيل)
    # -------------------------------------------------------------
    u16 = []
    # T1: المجرد والمزيد
    t1_u16 = [
        ("الْفِعْلُ الْمُجَرَّدُ هُوَ: [ ＿＿＿ ]", "مَا كَانَتْ جَمِيعُ أَحْرُفِهِ أَصْلِيَّةً (مِثْلُ: كَتَبَ)", ["مَا كَانَتْ جَمِيعُ أَحْرُفِهِ أَصْلِيَّةً (مِثْلُ: كَتَبَ)", "مَا زِيدَ فِيهِ حَرْفٌ", "مَا كَانَ مُعْتَلاًّ", "مَا كَانَ مَبْنِيّاً لِلْمَجْهُولِ"], "مجرد وہ فعل ہے جس کے تمام حروف اصلی ہوں۔", "Mujarrad is a verb whose letters are all root radicals.", "🌱"),
        ("الْفِعْلُ الْمَزِيدُ هُوَ: [ ＿＿＿ ]", "مَا زِيدَ عَلَى أَحْرُفِهِ الأَصْلِيَّةِ حَرْفٌ أَوْ أَكْثَرُ (مِثْلُ: عَلَّمَ)", ["مَا زِيدَ عَلَى أَحْرُفِهِ الأَصْلِيَّةِ حَرْفٌ أَوْ أَكْثَرُ (مِثْلُ: عَلَّمَ)", "مَا حُذِفَ مِنْهُ حَرْفٌ", "مَا لَا فَاعِلَ لَهُ", "مَا كَانَ جَامِداً"], "مزید وہ فعل ہے جس میں اصلی حروف پر زیادتی کی گئی ہو۔", "Mazeed is a verb having one or more augmentative letters added to its root.", "🌳")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u16, 1):
        u16.append({
            "id": f"b3_u16_t1_q{idx}", "book": 3, "unit_num": 16, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): مجرد و مزید", "badge_en": "Exercise (1): Bare vs Augmented Verbs",
            "tamreen_title_ar": "التَّفْرِيقُ بَيْنَ الْفِعْلِ الْمُجَرَّدِ وَالْمَزِيدِ:",
            "tamreen_title_ur": "مجرد اور مزید کے بنیادی تصورات اور پہچان:",
            "tamreen_title_en": "Distinguishing bare (Mujarrad) from augmented (Mazeed) verbs:",
            "grammar_goal_ur": "عربی اوزان کی بنیادی صرفی درجہ بندی کا فہم۔",
            "grammar_goal_en": "Foundational understanding of morphological derivation.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست تعریف منتخب کریں:", "prompt_en": "Select the correct definition:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: باب فَعَّلَ يُفَعِّلُ تَفْعِيلاً
    t2_u16 = [
        ("مَصْدَرُ الْفِعْلِ (عَلَّمَ يُعَلِّمُ) عَلَى وَزْنِ (تَفْعِيل) هُوَ: [ ＿＿＿ ]", "تَعْلِيمٌ", ["تَعْلِيمٌ", "عِلْمٌ", "مَعْلُومٌ", "تَعَلُّمٌ"], "باب فعّل کا مصدر تفِعیل کے وزن پر آتا ہے: تَعْلِيمٌ۔", "Masdar of Form II (Fa''ala) is on the pattern Taf'eel: Ta'leem.", "👨‍🏫"),
        ("مَصْدَرُ الْفِعْلِ (سَلَّمَ يُسَلِّمُ) هُوَ: [ ＿＿＿ ]", "تَسْلِيمٌ", ["تَسْلِيمٌ", "سَلاَمٌ", "إِسْلاَمٌ", "سَلاَمَةٌ"], "مصدر: تَسْلِيمٌ۔", "Masdar: Tasleem.", "🤝"),
        ("مَصْدَرُ الْفِعْلِ (كَبَّرَ يُكَبِّرُ) هُوَ: [ ＿＿＿ ]", "تَكْبِيرٌ", ["تَكْبِيرٌ", "كِبَرٌ", "إِكْبَارٌ", "مُتَكَبِّرٌ"], "مصدر: تَكْبِيرٌ (الله أكبر کہنا)۔", "Masdar: Takbeer (proclaiming Allahu Akbar).", "📢")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u16, 1):
        u16.append({
            "id": f"b3_u16_t2_q{idx}", "book": 3, "unit_num": 16, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): باب تَفْعِيل", "badge_en": "Exercise (2): Form II (Fa''ala / Taf'eel)",
            "tamreen_title_ar": "تَصْرِيفُ بَابِ (فَعَّلَ يُفَعِّلُ - تَفْعِيل):",
            "tamreen_title_ur": "باب تفعیل کا ماضی، مضارع اور مصدر صریح بنانا:",
            "tamreen_title_en": "Conjugating Form II verbs and deriving their verbal nouns (Taf'eel):",
            "grammar_goal_ur": "باب فعّل کے وزن اور مصادر کے احکام کا فہم۔",
            "grammar_goal_en": "Mastering Form II conjugation and masdar generation.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست مصدر منتخب کریں:", "prompt_en": "Select the correct verbal noun:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u16'] = u16

    # -------------------------------------------------------------
    # UNIT 17: باب أَفْعَلَ (إِفْعَال) • أصبح • أوشك • المتعدي لمفعولين
    # -------------------------------------------------------------
    u17 = []
    # T1: باب أَفْعَلَ يُفْعِلُ إِفْعَالاً
    t1_u17 = [
        ("مَصْدَرُ الْفِعْلِ (أَرْسَلَ يُرْسِلُ) عَلَى وَزْنِ (إِفْعَال) هُوَ: [ ＿＿＿ ]", "إِرْسَالٌ", ["إِرْسَالٌ", "رِسَالَةٌ", "مُرْسَلٌ", "تَرْسِيلٌ"], "باب أَفْعَل کا مصدر إِفْعَال پر آتا ہے: إِرْسَالٌ۔", "Masdar of Form IV (Af'ala) is on the pattern If'aal: Irsaal.", "✉️"),
        ("مَصْدَرُ الْفِعْلِ (أَسْلَمَ يُسْلِمُ) هُوَ: [ ＿＿＿ ]", "إِسْلاَمٌ", ["إِسْلاَمٌ", "سَلاَمٌ", "تَسْلِيمٌ", "مُسْلِمٌ"], "مصدر: إِسْلاَمٌ۔", "Masdar: Islaam.", "🕌"),
        ("مَصْدَرُ الْفِعْلِ (أَغْلَقَ يُغْلِقُ) هُوَ: [ ＿＿＿ ]", "إِغْلاَقٌ", ["إِغْلاَقٌ", "غَلْقٌ", "مَغْلُوقٌ", "تَغْلِيقٌ"], "مصدر: إِغْلاَقٌ (بند کرنا)۔", "Masdar: Ighlaaq (closing).", "🚪")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u17, 1):
        u17.append({
            "id": f"b3_u17_t1_q{idx}", "book": 3, "unit_num": 17, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): باب إِفْعَال", "badge_en": "Exercise (1): Form IV (Af'ala / If'aal)",
            "tamreen_title_ar": "تَصْرِيفُ بَابِ (أَفْعَلَ يُفْعِلُ - إِفْعَال):",
            "tamreen_title_ur": "باب إفعال کا ماضی، مضارع اور مصدر بنانا:",
            "tamreen_title_en": "Conjugating Form IV verbs and deriving verbal nouns (If'aal):",
            "grammar_goal_ur": "ہمزہ تعدیہ والے باب افعال کے اوزان کا فہم۔",
            "grammar_goal_en": "Mastering Form IV conjugation and causative hamzah rules.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست مصدر چنیں:", "prompt_en": "Select the correct verbal noun:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: أفعال المقاربة والشروع والمتعدي لمفعولين
    t2_u17 = [
        ("الْفِعْلُ (أَوْشَكَ) فِي اللُّغَةِ هُوَ مِنْ: [ ＿＿＿ ]", "أَفْعَالِ الْمُقَارَبَةِ (يَقْتَرِبُ وُقُوعُ الْخَبَرِ)", ["أَفْعَالِ الْمُقَارَبَةِ (يَقْتَرِبُ وُقُوعُ الْخَبَرِ)", "أَفْعَالِ الرَّجَاءِ", "أَفْعَالِ الشُّرُوعِ", "أَفْعَالِ الْمَدْحِ"], "أوشک افعال مقاربۃ میں سے ہے: کام کے قریب الوقوع ہونے کو بتاتا ہے۔", "'Awshaka' is an Af'al al-Muqarabah (verb of proximity).", "⏱️"),
        ("الْفِعْلُ (أَعْطَى) يَتَعَدَّى إِلَى: [ ＿＿＿ ]", "مَفْعُولَيْنِ (أَعْطَيْتُ الْفَقِيرَ مَالاً)", ["مَفْعُولَيْنِ (أَعْطَيْتُ الْفَقِيرَ مَالاً)", "مَفْعُولٍ وَاحِدٍ", "ثَلاَثَةِ مَفَاعِيلَ", "لَا يَتَعَدَّى (لاَزِمٌ)"], "فعل أعطى دو مفعولوں کو نصب دیتا ہے: الفقيرَ مالاً۔", "'A'ta' takes two objects (Maf'oolayn): A'taytu al-faqeera maalan.", "🎁")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u17, 1):
        u17.append({
            "id": f"b3_u17_t2_q{idx}", "book": 3, "unit_num": 17, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): افعال مقاربہ و متعدی بدو مفعول", "badge_en": "Exercise (2): Verbs of Proximity & Double Objects",
            "tamreen_title_ar": "أَفْعَالُ الْمُقَارَبَةِ وَالْمُتَعَدِّي لِمَفْعُولَيْنِ:",
            "tamreen_title_ur": "افعال مقاربۃ (أوشک) اور دو مفعول چاہنے والے افعال کی پہچان:",
            "tamreen_title_en": "Identify verbs of proximity and verbs taking two objects:",
            "grammar_goal_ur": "کاد اور اخواتہا اور افعال القلوب و العطاء کے اعمال کا فہم۔",
            "grammar_goal_en": "Understanding verbs of proximity and ditransitive verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست نحوی ضابطہ منتخب کریں:", "prompt_en": "Select the correct syntax rule:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u17'] = u17

    return data

if __name__ == "__main__":
    d = get_b3_units_10_to_17_deep()
    for u_id in sorted(d.keys()):
        qs = d[u_id]
        tamreens = sorted(list(set(q['tamreen_num'] for q in qs)))
        print(f"{u_id}: {len(qs)} questions across tamreens {tamreens}")
