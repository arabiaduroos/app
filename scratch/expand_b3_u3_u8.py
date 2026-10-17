# -*- coding: utf-8 -*-
"""
Expanded authentic questions for Book 3 Units 3 to 8
Adding dialogue comprehension and deep grammar exercises directly from Madinah Book 3.
"""

def get_b3_u3_u8_expanded():
    data = {}

    # =========================================================================
    # UNIT 5: المبني للمجهول ونائب الفاعل • تصريف الأجوف والناقص للمجهول
    # =========================================================================
    u5 = [
        # Tamreen 1: أسئلة الدرس وفهم النص
        {
            "id": "b3_u5_t1_q1", "book": 3, "unit_num": 5, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے اور مجہول جملوں کا فہم۔", "grammar_goal_en": "Comprehending passive sentences in dialogue.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَتُبَاعُ كُتُبُ الْمَعْهَدِ فِي الْمَكْتَبَاتِ التِّجَارِيَّةِ؟ [ ＿＿＿ ]",
            "prompt_ur": "کیا معہد کی کتابیں کمرشل بک اسٹورز پر فروخت ہوتی ہیں؟", "prompt_en": "Are the institute's books sold in commercial bookstores?",
            "answer": "لَا، لَا تُبَاعُ فِي الْمَكْتَبَاتِ التِّجَارِيَّةِ، بَلْ تُوَزَّعُ مَجَّاناً .",
            "options": [
                "لَا، لَا تُبَاعُ فِي الْمَكْتَبَاتِ التِّجَارِيَّةِ، بَلْ تُوَزَّعُ مَجَّاناً .",
                "نَعَمْ، تُبَاعُ فِي كُلِّ مَكَانٍ .",
                "تُبَاعُ بِثَمَنٍ غَالٍ جِدّاً .",
                "لَا يُمْكِنُ الْحُصُولُ عَلَيْهَا أَبَداً ."
            ],
            "emoji": "📚", "hint_ur": "وہ بازار میں فروخت نہیں ہوتیں بلکہ مفت تقسیم کی جاتی ہیں۔", "hint_en": "They are not sold; distributed for free.",
            "explanation_ur": "درست جواب: معہد کی کتابیں مفت تقسیم ہوتی ہیں: 'لَا، لَا تُبَاعُ فِي الْمَكْتَبَاتِ التِّجَارِيَّةِ، بَلْ تُوَزَّعُ مَجَّاناً .'۔",
            "explanation_en": "Correct answer: They are distributed for free."
        },
        {
            "id": "b3_u5_t1_q2", "book": 3, "unit_num": 5, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے سوالات:", "tamreen_title_en": "Dialogue facts:",
            "grammar_goal_ur": "مجہول فعل کے مفعول کا فہم۔", "grammar_goal_en": "Understanding passive verbs in context.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مِنْ أَيْنَ يُمْكِنُ الْحُصُولُ عَلَى كُتُبِ الْمَعْهَدِ؟ [ ＿＿＿ ]",
            "prompt_ur": "معہد کی کتابیں کہاں سے حاصل کی جا سکتی ہیں؟", "prompt_en": "Where can the institute's books be obtained from?",
            "answer": "مِنْ إِدَارَةِ الْمَعْهَدِ .",
            "options": ["مِنْ إِدَارَةِ الْمَعْهَدِ .", "مِنَ السُّوقِ .", "مِنَ الْمَطْبَعَةِ .", "مِنَ الْمَسْجِدِ ."],
            "emoji": "🏢", "hint_ur": "معہد کے دفتر اور انتظامیہ سے۔", "hint_en": "From the institute administration.",
            "explanation_ur": "درست جواب: 'مِنْ إِدَارَةِ الْمَعْهَدِ .'۔", "explanation_en": "From the institute's administration."
        },
        # Tamreen 2: المبني للمجهول من الماضي الثلاثي
        {
            "id": "b3_u5_t2_q1", "book": 3, "unit_num": 5, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): ماضی مجہول (فُعِلَ)", "badge_en": "Exercise (2): Passive Past (Fu'ila)",
            "tamreen_title_ar": "صَوْغُ الْمَبْنِيِّ لِلْمَجْهُولِ مِنَ الْفِعْلِ الْمَاضِي الثُّلَاثِيِّ:",
            "tamreen_title_ur": "ثلاثی ماضی سے مجہول کا صیغہ بنائیں:",
            "tamreen_title_en": "Form the passive past from triliteral verbs:",
            "grammar_goal_ur": "فُعِلَ کے وزن پر کُتِبَ، فُتِحَ، ضُرِبَ کی صیاغت۔", "grammar_goal_en": "Mastering the Fu'ila pattern for past passive.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمَبْنِيُّ لِلْمَجْهُولِ مِنْ (قَتَلَ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "قَتَلَ کا ماضی مجہول منتخب کریں:", "prompt_en": "Select the passive past of 'Qatala':",
            "answer": "قُتِلَ",
            "options": ["قُتِلَ", "يُقْتَلُ", "قَاتَلَ", "مَقْتُولٌ"],
            "emoji": "⚔️", "hint_ur": "پہلے پر پیش اور دوسرے پر زیر: قُتِلَ۔", "hint_en": "First letter dammah, second kasrah: Qutila.",
            "explanation_ur": "ماضی مجہول فُعِلَ کے وزن پر آتا ہے: قُتِلَ۔", "explanation_en": "Passive past takes pattern Fu'ila: Qutila."
        },
        # Tamreen 2: المبني للمجهول من الأجوف (قَالَ -> قِيلَ، بَاعَ -> بِيعَ)
        {
            "id": "b3_u5_t2_q2", "book": 3, "unit_num": 5, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اجوف کا مجہول (قِيلَ / بِيعَ)", "badge_en": "Exercise (2): Passive of Hollow Verbs",
            "tamreen_title_ar": "صَوْغُ الْمَبْنِيِّ لِلْمَجْهُولِ مِنَ الْفِعْلِ الأَجْوَفِ (قَالَ -> قِيلَ):",
            "tamreen_title_ur": "اجوف سے مجہول بناتے وقت فاء کلمہ کو کسرہ اور یاء دینا:",
            "tamreen_title_en": "Passive of hollow verbs with kasrah and yaa (Qeela, Bee'a):",
            "grammar_goal_ur": "قَالَ -> قِيلَ، بَاعَ -> بِيعَ، صَامَ -> صِيمَ۔", "grammar_goal_en": "Passive of hollow past verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمَبْنِيُّ لِلْمَجْهُولِ مِنَ الْفِعْلِ الأَجْوَفِ (بَاعَ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "باع (بیچا) کا مجہول منتخب کریں (بیچا گیا):", "prompt_en": "Select the passive of 'Baa'a' (was sold):",
            "answer": "بِيعَ",
            "options": ["بِيعَ", "بُوعَ", "يُبَاعُ", "مَبِيعٌ"],
            "emoji": "🏷️", "hint_ur": "اجوف کا ماضی مجہول 'بِيعَ' آتا ہے۔", "hint_en": "Passive of Baa'a is Bee'a.",
            "explanation_ur": "اجوف ماضی کا مجہول فاء کلمہ کے کسرہ اور یاء کے ساتھ آتا ہے: بِيعَ۔", "explanation_en": "Takes kasrah and yaa: Bee'a."
        },
        # Tamreen 3: مضارع الأجوف المبني للمجهول (يَقُولُ -> يُقَالُ، يَبِيعُ -> يُبَاعُ)
        {
            "id": "b3_u5_t3_q1", "book": 3, "unit_num": 5, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مضارع اجوف مجہول (يُقَالُ)", "badge_en": "Exercise (3): Present Passive of Hollow",
            "tamreen_title_ar": "صَوْغُ الْمُضَارِعِ الْمَجْهُولِ مِنَ الأَجْوَفِ (يُقَالُ / يُبَاعُ):",
            "tamreen_title_ur": "اجوف کے مضارع مجہول میں الف کا ظاہر ہونا:",
            "tamreen_title_en": "Present passive of hollow verbs taking alif (Yuqaalu, Yubaa'u):",
            "grammar_goal_ur": "يَقُولُ سے يُقَالُ اور يَبِيعُ سے يُبَاعُ بنانا۔", "grammar_goal_en": "Alif appears in present passive of hollow verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمُضَارِعُ الْمَبْنِيُّ لِلْمَجْهُولِ مِنْ (يَبِيعُ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "یَبِیعُ کا مضارع مجہول منتخب کریں (بیچا جاتا ہے):", "prompt_en": "Select present passive of Yabee'u (is sold):",
            "answer": "يُبَاعُ",
            "options": ["يُبَاعُ", "يَبِيعُ", "بِيعَ", "مَبِيعٌ"],
            "emoji": "🛒", "hint_ur": "مضارع مجہول میں حرف علت الف میں بدلتا ہے: يُبَاعُ۔", "hint_en": "Weak vowel turns to alif: Yubaa'u.",
            "explanation_ur": "مضارع مجہول میں ماقبل مفتوح ہونے سے یاء الف میں بدل جاتی ہے: يُبَاعُ۔", "explanation_en": "Becomes alif due to preceding fathah: Yubaa'u."
        },
        # Tamreen 4: إعراب نائب الفاعل
        {
            "id": "b3_u5_t4_q1", "book": 3, "unit_num": 5, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): اعراب نائب الفاعل", "badge_en": "Exercise (4): Case of Deputy Subject",
            "tamreen_title_ar": "رَفْعُ نَائِبِ الْفَاعِلِ فِي الْجُمْلَةِ الْمَبْنِيَّةِ لِلْمَجْهُولِ:",
            "tamreen_title_ur": "مجہول فعل کے بعد نائب فاعل کو رفع (پیش) دینا:",
            "tamreen_title_en": "Nominative case for deputy subject (Naa'ib al-Fa'il):",
            "grammar_goal_ur": "خُلِقَ الإِنْسَانُ ضَعِيفاً میں الإنسانُ نائب فاعل مرفوع ہے۔", "grammar_goal_en": "Deputy subject is always in nominative (Marfoo') case.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَالَ تَعَالَى: { وَخُلِقَ [ ＿＿＿ ] ضَعِيفاً } .",
            "prompt_ur": "قرآنی آیت میں نائب فاعل کا درست اعراب چنیں:", "prompt_en": "Select the correct case for deputy subject in Quranic verse:",
            "answer": "الإِنْسَانُ (مَرْفُوعٌ بِالضَّمَّةِ)",
            "options": [
                "الإِنْسَانُ (مَرْفُوعٌ بِالضَّمَّةِ)",
                "الإِنْسَانَ (مَنْصُوبٌ بِالْفَتْحَةِ)",
                "الإِنْسَانِ (مَجْرُورٌ بِالْكَسْرَةِ)",
                "إِنْسَاناً"
            ],
            "emoji": "📖", "hint_ur": "نائب فاعل فاعل کی طرح ہمیشہ مرفوع ہوتا ہے: الإِنْسَانُ۔", "hint_en": "Deputy subject takes dammah: Al-Insaanu.",
            "explanation_ur": "نائب فاعل ہمیشہ مرفوع ہوتا ہے اس لیے 'الإِنْسَانُ' پر پیش آئے گی۔", "explanation_en": "Naa'ib al-Fa'il is strictly nominative."
        }
    ]
    data['b3_u5'] = u5

    # =========================================================================
    # UNIT 6: الحال وأحكامه • رحلة الحج
    # =========================================================================
    u6 = [
        # Tamreen 1: أسئلة الدرس وفهم النص
        {
            "id": "b3_u6_t1_q1", "book": 3, "unit_num": 6, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "حج کے سفر کے مکالمے کا فہم۔", "grammar_goal_en": "Comprehending pilgrimage dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَا عَدَدُ الْمُشْتَرِكِينَ فِي رِحْلَةِ الْحَجِّ؟ [ ＿＿＿ ]",
            "prompt_ur": "حج کے سفر میں شریک ہونے والوں کی تعداد کتنی تھی؟", "prompt_en": "How many participants were in the Hajj trip?",
            "answer": "عَدَدُهُمْ ثَلَاثُونَ طَالِباً .",
            "options": ["عَدَدُهُمْ ثَلَاثُونَ طَالِباً .", "عَدَدُهُمْ عِشْرُونَ طَالِباً .", "عَدَدُهُمْ خَمْسُونَ طَالِباً .", "عَدَدُهُمْ عَشَرَةُ طُلَّابٍ ."],
            "emoji": "🕋", "hint_ur": "تیس طلبہ شریک تھے۔", "hint_en": "There were 30 students.",
            "explanation_ur": "درست جواب: 'عَدَدُهُمْ ثَلَاثُونَ طَالِباً .'۔", "explanation_en": "Correct answer: 30 students."
        },
        {
            "id": "b3_u6_t1_q2", "book": 3, "unit_num": 6, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے سوالات:", "tamreen_title_en": "Dialogue facts:",
            "grammar_goal_ur": "مکالمے کا فہم۔", "grammar_goal_en": "Dialogue comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ يَلْتَقِي الطُّلَّابُ لِلسَّفَرِ؟ [ ＿＿＿ ]",
            "prompt_ur": "سفر کے لیے طلبہ کہاں جمع ہوں گے؟", "prompt_en": "Where do the students meet for travel?",
            "answer": "أَمَامَ مَسْجِدِ الْجَامِعَةِ .",
            "options": ["أَمَامَ مَسْجِدِ الْجَامِعَةِ .", "فِي الْمَطَارِ .", "فِي السُّوقِ .", "فِي الْمَحَطَّةِ ."],
            "emoji": "🕌", "hint_ur": "یونیورسٹی کی مسجد کے سامنے۔", "hint_en": "In front of the university mosque.",
            "explanation_ur": "درست جواب: 'أَمَامَ مَسْجِدِ الْجَامِعَةِ .'۔", "explanation_en": "In front of the university mosque."
        },
        # Tamreen 2: تعريف الحال وإعرابه
        {
            "id": "b3_u6_t2_q1", "book": 3, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): حَال کا اعراب (نصب)", "badge_en": "Exercise (2): Accusative Case of Haal",
            "tamreen_title_ar": "تَعْرِيفُ الْحَالِ وَحُكْمُهُ الإِعْرَابِيُّ (مَنْصُوبٌ دَائِماً):",
            "tamreen_title_ur": "حال کی پہچان اور اس کا ہمیشہ منسوب ہونا:",
            "tamreen_title_en": "Definition of Haal (circumstantial state) and its accusative case:",
            "grammar_goal_ur": "دَخَلَ الْمُدَرِّسُ الْفَصْلَ بَاسِماً (حال نکرہ منسوب ہے)۔", "grammar_goal_en": "Haal describes condition of subject/object and is always Mansub.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "دَخَلَ الْمُدَرِّسُ الْفَصْلَ [ ＿＿＿ ] .",
            "prompt_ur": "استاد مسکراتے ہوئے کلاس میں داخل ہوئے (حال منسوب چنیں):", "prompt_en": "The teacher entered the class smiling (select accusative Haal):",
            "answer": "بَاسِماً",
            "options": ["بَاسِماً", "بَاسِمٌ", "بَاسِمٍ", "الْبَاسِمُ"],
            "emoji": "😊", "hint_ur": "حال نکرہ اور منسوب ہوتی ہے: بَاسِماً۔", "hint_en": "Haal takes fathatan: Baasiman.",
            "explanation_ur": "حال منسوب ہوتی ہے اس لیے 'بَاسِماً' پر دو زبر آئیں گے۔", "explanation_en": "Haal is always accusative (Mansub): Baasiman."
        },
        # Tamreen 3: حال لجمع المذكر السالم (مسرورين)
        {
            "id": "b3_u6_t3_q1", "book": 3, "unit_num": 6, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): حال جمع مذکر (مَسْرُورِينَ)", "badge_en": "Exercise (3): Plural Haal with Yaa",
            "tamreen_title_ar": "نَصْبُ الْحَالِ بِالْيَاءِ إِذَا كَانَ جَمْعَ مُذَكَّرٍ سَالِماً:",
            "tamreen_title_ur": "جمع مذکر سالم حالتِ حال میں یاء کے ساتھ منسوب ہونا:",
            "tamreen_title_en": "Plural masculine Haal taking yaa in accusative:",
            "grammar_goal_ur": "رَجَعَ الطُّلَّابُ مِنَ الرِّحْلَةِ مَسْرُورِينَ۔", "grammar_goal_en": "Plural Haal takes yaa: Masrooreena.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "رَجَعَ الطُّلَّابُ مِنَ الرِّحْلَةِ [ ＿＿＿ ] .",
            "prompt_ur": "طلبہ سفر سے خوش و خرم واپس آئے (حال جمع چنیں):", "prompt_en": "Students returned from the trip joyful (select plural Haal):",
            "answer": "مَسْرُورِينَ",
            "options": ["مَسْرُورِينَ", "مَسْرُورُونَ", "مَسْرُورَانِ", "مَسْرُوراً"],
            "emoji": "😃", "hint_ur": "جمع مذکر سالم حالت نصب میں یاء لیتا ہے: مَسْرُورِينَ۔", "hint_en": "Sound plural takes yaa in accusative: Masrooreena.",
            "explanation_ur": "حال منسوب بالیاء ہے کیونکہ جمع مذکر سالم ہے: مَسْرُورِينَ۔", "explanation_en": "Plural Haal takes yaa: Masrooreena."
        },
        # Tamreen 4: صاحب الحال
        {
            "id": "b3_u6_t4_q1", "book": 3, "unit_num": 6, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): صَاحِبُ الْحَال", "badge_en": "Exercise (4): Owner of the State (Saahib al-Haal)",
            "tamreen_title_ar": "تَعْيِينُ صَاحِبِ الْحَالِ (الْفَاعِلِ أَوِ الْمَفْعُولِ):",
            "tamreen_title_ur": "صاحبِ حال کی پہچان (جس کی حالت بیان ہو رہی ہو، جو معرفہ ہوتا ہے):",
            "tamreen_title_en": "Identifying Saahib al-Haal (always definite):",
            "grammar_goal_ur": "شَرِبْتُ الْمَاءَ بَارِداً میں صاحب الحال 'الْمَاءَ' ہے۔", "grammar_goal_en": "Saahib al-Haal is definite, while Haal is indefinite.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي جُمْلَةِ: (شَرِبْتُ الْمَاءَ بَارِداً)، صَاحِبُ الْحَالِ هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "اس جملے میں صاحب الحال (جس کی حالت بتائی گئی) کون سا لفظ ہے؟", "prompt_en": "In this sentence, which word is Saahib al-Haal?",
            "answer": "الْمَاءَ (مَفْعُولٌ بِهِ مَعْرِفَةٌ)",
            "options": ["الْمَاءَ (مَفْعُولٌ بِهِ مَعْرِفَةٌ)", "التَّاءُ فِي شَرِبْتُ", "بَارِداً", "فِعْلُ شَرِبَ"],
            "emoji": "💧", "hint_ur": "پانی کی حالت بیان کی گئی ہے کہ وہ ٹھنڈا تھا۔", "hint_en": "The water's state was cold: Al-Maa'a.",
            "explanation_ur": "ٹھنڈا ہونا پانی کی صفت/حالت ہے اس لیے صاحب الحال 'الْمَاءَ' ہے۔", "explanation_en": "Al-Maa'a is the object described by the Haal."
        }
    ]
    data['b3_u6'] = u6

    # =========================================================================
    # UNIT 7: اسم الآلة وأوزانه الثلاثة المشهورة
    # =========================================================================
    u7 = [
        # Tamreen 1: أسئلة الدرس
        {
            "id": "b3_u7_t1_q1", "book": 3, "unit_num": 7, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے مکالمے کا فہم۔", "grammar_goal_en": "Dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَاذَا طَلَبَتْ أُمُّ أَحْمَدَ مِنَ السُّوقِ؟ [ ＿＿＿ ]",
            "prompt_ur": "احمد کی والدہ نے بازار سے کیا چیز منگوائی؟", "prompt_en": "What did Ahmad's mother ask to bring from market?",
            "answer": "طَلَبَتْ مِكْنَسَةً جَدِيدَةً وَمِقَصّاً .",
            "options": ["طَلَبَتْ مِكْنَسَةً جَدِيدَةً وَمِقَصّاً .", "طَلَبَتْ سَيَّارَةً .", "طَلَبَتْ كُتُباً .", "طَلَبَتْ طَعَاماً ."],
            "emoji": "🧹", "hint_ur": "ایک نیا جھاڑو اور قینچی۔", "hint_en": "A new broom and scissors.",
            "explanation_ur": "درست جواب: 'طَلَبَتْ مِكْنَسَةً جَدِيدَةً وَمِقَصّاً .'۔", "explanation_en": "Correct answer: broom and scissors."
        },
        # Tamreen 2: وزن مِفْعَال (مِفْتَاح، مِيزَان)
        {
            "id": "b3_u7_t2_q1", "book": 3, "unit_num": 7, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): وزن مِفْعَال", "badge_en": "Exercise (2): Pattern Mif'aal",
            "tamreen_title_ar": "صَوْغُ اسْمِ الآلَةِ عَلَى وَزْنِ (مِفْعَال):",
            "tamreen_title_ur": "وزن مِفْعَال پر اسم آلہ بنانا (مِفْتَاح، مِيزَان، مِقْرَاض):",
            "tamreen_title_en": "Forming Noun of Instrument on pattern Mif'aal:",
            "grammar_goal_ur": "فَتَحَ سے مِفْتَاحٌ اور وَزَنَ سے مِيزَانٌ۔", "grammar_goal_en": "Deriving tool noun on pattern Mif'aal.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اسْمُ الآلَةِ مِنَ الْفِعْلِ (فَتَحَ يَفْتَحُ) عَلَى وَزْنِ مِفْعَال هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "فَتَحَ سے کھولنے کا آلہ (چابی) منتخب کریں:", "prompt_en": "Select tool noun of Fataha (Key):",
            "answer": "مِفْتَاحٌ",
            "options": ["مِفْتَاحٌ", "فَاتِحٌ", "مَفْتُوحٌ", "فَتَّاحٌ"],
            "emoji": "🔑", "hint_ur": "کھولنے کا آلہ: مِفْتَاحٌ۔", "hint_en": "Tool for opening: Miftaah.",
            "explanation_ur": "فَتَحَ سے اسم آلہ مِفْعَال کے وزن پر 'مِفْتَاحٌ' آتا ہے۔", "explanation_en": "Noun of instrument on Mif'aal: Miftaah."
        },
        # Tamreen 3: وزن مِفْعَلَة (مِكْنَسَة، مِلْعَقَة)
        {
            "id": "b3_u7_t3_q1", "book": 3, "unit_num": 7, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): وزن مِفْعَلَة", "badge_en": "Exercise (3): Pattern Mif'alah",
            "tamreen_title_ar": "صَوْغُ اسْمِ الآلَةِ عَلَى وَزْنِ (مِفْعَلَة):",
            "tamreen_title_ur": "وزن مِفْعَلَة پر اسم آلہ بنانا (مِكْنَسَة، مِلْعَقَة، مِرْوَحَة):",
            "tamreen_title_en": "Forming Noun of Instrument on pattern Mif'alah:",
            "grammar_goal_ur": "كَنَسَ سے مِكْنَسَةٌ اور لَعِقَ سے مِلْعَقَةٌ۔", "grammar_goal_en": "Deriving tool noun on pattern Mif'alah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اسْمُ الآلَةِ مِنَ الْفِعْلِ (كَنَسَ يَكْنُسُ) لِتَنْظِيفِ الأَرْضِ هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "صفائی کا آلہ (جھاڑو) منتخب کریں:", "prompt_en": "Select the tool for sweeping (Broom):",
            "answer": "مِكْنَسَةٌ",
            "options": ["مِكْنَسَةٌ", "كَانِسٌ", "مَكْنُوسٌ", "كَنَّاسٌ"],
            "emoji": "🧹", "hint_ur": "جھاڑو: مِكْنَسَةٌ۔", "hint_en": "Broom: Miknasah.",
            "explanation_ur": "کَنَسَ سے اسم آلہ مِفْعَلَة کے وزن پر 'مِكْنَسَةٌ' بنتا ہے۔", "explanation_en": "Tool for sweeping is Miknasah."
        },
        # Tamreen 4: وزن مِفْعَل (مِبْرَد، مِشْرَط، مِصْعَد)
        {
            "id": "b3_u7_t4_q1", "book": 3, "unit_num": 7, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): وزن مِفْعَل", "badge_en": "Exercise (4): Pattern Mif'al",
            "tamreen_title_ar": "صَوْغُ اسْمِ الآلَةِ عَلَى وَزْنِ (مِفْعَل):",
            "tamreen_title_ur": "وزن مِفْعَل پر اسم آلہ بنانا (مِبْرَد، مِشْرَط، مِصْعَد):",
            "tamreen_title_en": "Forming Noun of Instrument on pattern Mif'al:",
            "grammar_goal_ur": "صَعِدَ سے مِصْعَدٌ (لفٹ) اور شَرَطَ سے مِشْرَطٌ۔", "grammar_goal_en": "Deriving tool noun on pattern Mif'al.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اسْمُ الآلَةِ الَّتِي نَصْعَدُ بِهَا فِي الْعِمَارَاتِ الْعَالِيَةِ (الْمِصْعَدُ) عَلَى وَزْنِ: [ ＿＿＿ ]",
            "prompt_ur": "لفٹ (مِصْعَدٌ) کس وزن پر ہے؟", "prompt_en": "What is the grammatical pattern of 'Mis'ad' (Elevator)?",
            "answer": "مِفْعَل",
            "options": ["مِفْعَل", "مِفْعَال", "مِفْعَلَة", "فَاعُول"],
            "emoji": "🛗", "hint_ur": "مِصْعَد مِفْعَل کے وزن پر ہے۔", "hint_en": "Mis'ad is on pattern Mif'al.",
            "explanation_ur": "مِصْعَد کا وزن مِفْعَل ہے: مِصْعَدٌ / مِفْعَلٌ۔", "explanation_en": "Pattern is Mif'al: Mis'ad."
        }
    ]
    data['b3_u7'] = u7

    # =========================================================================
    # UNIT 8: المعرفة والنكرة وأقسام المعارف الستة • البدل
    # =========================================================================
    u8 = [
        # Tamreen 1: أسئلة الدرس وفهم النص
        {
            "id": "b3_u8_t1_q1", "book": 3, "unit_num": 8, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Facts",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سبق کے حقائق کا فہم۔", "grammar_goal_en": "Comprehending lesson dialogue facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَا الأَشْيَاءُ الَّتِي اشْتَرَاهَا مَالِكٌ؟ [ ＿＿＿ ]",
            "prompt_ur": "مالک نے بازار سے کیا چیزیں خریدیں؟", "prompt_en": "What items did Malik buy?",
            "answer": "اشْتَرَى لَوْحَةً جَمِيلَةً وَمُعْجَماً .",
            "options": ["اشْتَرَى لَوْحَةً جَمِيلَةً وَمُعْجَماً .", "اشْتَرَى سَيَّارَةً وَقَلَماً .", "اشْتَرَى ثَوْباً وَحِذَاءً .", "مَا اشْتَرَى شَيْئاً ."],
            "emoji": "🖼️", "hint_ur": "ایک خوبصورت پینٹنگ اور ایک لغت خریدی۔", "hint_en": "He bought a beautiful painting and a dictionary.",
            "explanation_ur": "درست جواب: 'اشْتَرَى لَوْحَةً جَمِيلَةً وَمُعْجَماً .'۔", "explanation_en": "Correct answer: a painting and a dictionary."
        },
        # Tamreen 2: أقسام المعارف الستة
        {
            "id": "b3_u8_t2_q1", "book": 3, "unit_num": 8, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): معرفہ کی چھ اقسام", "badge_en": "Exercise (2): Six Classes of Definite Nouns",
            "tamreen_title_ar": "أَقْسَامُ الْمَعَارِفِ السِّتَّةُ فِي اللُّغَةِ الْعَرَبِيَّةِ:",
            "tamreen_title_ur": "عربی میں معرفہ کی چھ اقسام کی پہچان:",
            "tamreen_title_en": "Recognizing the six classes of definite nouns:",
            "grammar_goal_ur": "الضمير، العَلَم، اسم الإشارة، الاسم الموصول، المحلى بأل، المضاف إلى معرفة۔", "grammar_goal_en": "Six classes: Pronoun, Proper noun, Demonstrative, Relative pronoun, Definite by Al, Added to definite.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيُّ الْكَلِمَاتِ الآتِيَةِ نَكِرَةٌ وَلَيْسَتْ مَعْرِفَةً؟ [ ＿＿＿ ]",
            "prompt_ur": "مندرجہ ذیل میں سے کون سا لفظ نکرہ ہے (معرفہ نہیں ہے)؟", "prompt_en": "Which of the following words is indefinite (Nakirah)?",
            "answer": "كِتَابٌ (مُجَرَّدٌ مِنْ أَلْ وَالإِضَافَةِ)",
            "options": [
                "كِتَابٌ (مُجَرَّدٌ مِنْ أَلْ وَالإِضَافَةِ)",
                "مُحَمَّدٌ (عَلَمٌ)",
                "هٰذَا (اسْمُ إِشَارَةٍ)",
                "أَنْتَ (ضَمِيرٌ)"
            ],
            "emoji": "📖", "hint_ur": "کتابٌ عام ہے، نہ اس پر ال ہے اور نہ یہ مضاف ہے۔", "hint_en": "Kitaabun has no Al and is not annexed.",
            "explanation_ur": "محمد علم ہے، هذا اسم اشارہ ہے، أنت ضمیر ہے، صرف 'كِتَابٌ' نکرہ ہے۔", "explanation_en": "Kitaabun is indefinite (Nakirah)."
        },
        # Tamreen 3: البدل وأنواعه
        {
            "id": "b3_u8_t3_q1", "book": 3, "unit_num": 8, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): الْبَدَلُ وَالْمُبْدَلُ مِنْهُ", "badge_en": "Exercise (3): Badal (Apposition)",
            "tamreen_title_ar": "تَعْيِينُ الْبَدَلِ وَإِعْرَابِهِ:",
            "tamreen_title_ur": "بدل کی پہچان اور اعراب میں مبدل منہ کی پیروی:",
            "tamreen_title_en": "Identifying Badal and its case agreement with Mubdal Minhu:",
            "grammar_goal_ur": "خَلِيفَةُ رَسُولِ اللهِ أَبُو بَكْرٍ میں 'أَبُو بَكْرٍ' بدل ہے۔", "grammar_goal_en": "Badal agrees in case with the noun it clarifies.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي جُمْلَةِ: (قَالَ الْفَارُوقُ عُمَرُ)، كَلِمَةُ (عُمَرُ) إِعْرَابُهَا: [ ＿＿＿ ]",
            "prompt_ur": "اس جملے میں لفظ 'عمر' کا اعرابی کردار کیا ہے؟", "prompt_en": "In this sentence, what is the syntactic role of 'Umar'?",
            "answer": "بَدَلٌ مَرْفُوعٌ بِالضَّمَّةِ",
            "options": ["بَدَلٌ مَرْفُوعٌ بِالضَّمَّةِ", "نَعْتٌ مَجْرُورٌ", "مَفْعُولٌ بِهِ", "مُضَافٌ إِلَيْهِ"],
            "emoji": "👑", "hint_ur": "عمر، الفاروق کا بدل ہے۔", "hint_en": "Umar is Badal for Al-Farooq.",
            "explanation_ur": "عمر لقب کے بعد آیا ہے اس لیے بدل مرفوع ہے: قَالَ الْفَارُوقُ عُمَرُ۔", "explanation_en": "Umar is Badal (apposition) following the title."
        }
    ]
    data['b3_u8'] = u8

    return data

if __name__ == '__main__':
    d = get_b3_u3_u8_expanded()
    for k in sorted(d.keys()):
        print(f"Book 3 {k}: {len(d[k])} questions")
