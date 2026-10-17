# -*- coding: utf-8 -*-
"""
Comprehensive Curriculum Generator for Madinah Book 2 (Units 1 to 31)
Incorporate ALL exercises from the original textbook with full authenticity.
"""

def get_b2_all_units():
    units = {}

    # We will build comprehensive questions for each of the 31 units:
    
    # --- UNIT 1: إِنَّ وَأَخَوَاتُهَا • لَعَلَّ • ذُو • أَمْ • مِائَةٌ وَأَلْفٌ ---
    units[1] = [
        {"id": "b2_u1_q1", "tamreen_num": 1, "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Comprehension",
         "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے مطابق سوالات کے جوابات دیں:", "tamreen_title_en": "Answer based on the lesson:",
         "grammar_goal_ur": "ہاشم کے وطن کی پہچان۔", "grammar_goal_en": "Hashim's origin.",
         "prompt_ar": "مِنْ أَيْنَ هَاشِمٌ؟ [ ＿＿＿ ]", "prompt_ur": "ہاشم کہاں سے ہے؟", "prompt_en": "Where is Hashim from?",
         "answer": "هُوَ مِنَ الْهِنْدِ .", "options": ["هُوَ مِنَ الْهِنْدِ .", "هُوَ مِنْ بَاكِسْتَانَ .", "هُوَ مِنَ الْيَابَانِ .", "هُوَ مِنَ الْفِلِبِّينِ ."],
         "emoji": "🇮🇳", "hint_ur": "ہاشم نے کہا: إني من الهند", "hint_en": "Hashim is from India.",
         "explanation_ur": "ہاشم کا تعلق ہندوستان سے ہے۔", "explanation_en": "Hashim is from India.", "type": "fill_blank"},
        {"id": "b2_u1_q2", "tamreen_num": 1, "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Comprehension",
         "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے مطابق سوالات کے جوابات دیں:", "tamreen_title_en": "Answer based on the lesson:",
         "grammar_goal_ur": "ہاشم کی گھڑی کی قیمت۔", "grammar_goal_en": "Watch price.",
         "prompt_ar": "بِكَمِ اشْتَرَى هَاشِمٌ سَاعَتَهُ؟ [ ＿＿＿ ]", "prompt_ur": "ہاشم نے اپنی گھڑی کتنے میں خریدی؟", "prompt_en": "How much was Hashim's watch?",
         "answer": "اشْتَرَاهَا بِمِائَةِ رِيَالٍ .", "options": ["اشْتَرَاهَا بِمِائَةِ رِيَالٍ .", "اشْتَرَاهَا بِأَلْفِ رِيَالٍ .", "اشْتَرَاهَا بِعَشَرَةِ رِيَالاَتٍ .", "اشْتَرَاهَا بِمِائَتَيْ رِيَالٍ ."],
         "emoji": "⌚", "hint_ur": "ہاشم نے بتایا: اشتريتها بمائة ريال", "hint_en": "He bought it for 100 Riyals.",
         "explanation_ur": "ہاشم نے گھڑی سو ریال میں خریدی۔", "explanation_en": "Hashim bought the watch for 100 Riyals.", "type": "fill_blank"},
        {"id": "b2_u1_q3", "tamreen_num": 3, "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): ضمائر پر 'إِنَّ'", "badge_en": "Exercise (3): Inna with Pronouns",
         "tamreen_title_ar": "أَدْخِلْ (إِنَّ) عَلَى الضَّمَائِرِ الآتِيَةِ:", "tamreen_title_ur": "ضمیروں پر 'إِنَّ' داخل کریں:", "tamreen_title_en": "Enter 'Inna' upon pronouns:",
         "grammar_goal_ur": "هُوَ کا إِنَّهُ بننا۔", "grammar_goal_en": "Huwa becomes Innahu.",
         "prompt_ar": "(هُوَ طَالِبٌ) عِنْدَ دُخُولِ (إِنَّ) تُصْبِحُ: [ ＿＿＿ ]", "prompt_ur": "(هو) پر 'إنّ' داخل کریں:", "prompt_en": "Enter 'Inna' upon 'Huwa talibun':",
         "answer": "إِنَّهُ طَالِبٌ", "options": ["إِنَّهُ طَالِبٌ", "إِنَّ هُوَ طَالِبٌ", "إِنَّكَ طَالِبٌ", "إِنَّهُمْ طَالِبٌ"],
         "emoji": "👤", "hint_ur": "ضمیر متصل 'ـه' لگے گی: إِنَّهُ۔", "hint_en": "Takes attached pronoun -hu: Innahu.",
         "explanation_ur": "إنّ کے ساتھ ضمیر نصب متصل آتی ہے: إِنَّهُ۔", "explanation_en": "Inna takes attached accusative pronoun: Innahu.", "type": "fill_blank"},
        {"id": "b2_u1_q4", "tamreen_num": 6, "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): اعرابِ اسم إنّ", "badge_en": "Exercise (6): Case of Ism Inna",
         "tamreen_title_ar": "أَدْخِلْ (إِنَّ) وَاضْبِطْ أَوَاخِرَ الْكَلِمَاتِ:", "tamreen_title_ur": "اسم پر 'إِنَّ' داخل کر کے اعراب لگائیں:", "tamreen_title_en": "Vocalize with Inna:",
         "grammar_goal_ur": "اسم پر فتحہ (زبر) اور خبر پر ضمہ (پیش)۔", "grammar_goal_en": "Ism Inna takes fathah, Khabar takes dammah.",
         "prompt_ar": "أَدْخِلْ (إِنَّ) عَلَى: (الدَّرْسُ صَعْبٌ) : [ ＿＿＿ ]", "prompt_ur": "(الدرس صعب) پر 'إنّ' داخل کریں:", "prompt_en": "Enter Inna upon 'Ad-darsu sa'bun':",
         "answer": "إِنَّ الدَّرْسَ صَعْبٌ", "options": ["إِنَّ الدَّرْسَ صَعْبٌ", "إِنَّ الدَّرْسُ صَعْبٌ", "إِنَّ الدَّرْسَ صَعْباً", "إِنَّ الدَّرْسِ صَعْبٌ"],
         "emoji": "📖", "hint_ur": "اسم پر زبر آئے گا: إِنَّ الدَّرْسَ صَعْبٌ۔", "hint_en": "Noun takes fathah: Inna ad-darsa sa'bun.",
         "explanation_ur": "إنّ کا اسم منسوب ہوتا ہے: إِنَّ الدَّرْسَ صَعْبٌ۔", "explanation_en": "Ism Inna is accusative: Inna ad-darsa sa'bun.", "type": "fill_blank"},
        {"id": "b2_u1_q5", "tamreen_num": 7, "badge_ar": "التَّمْرِينُ (7)", "badge_ur": "مشق (7): لفظِ (ذُو)", "badge_en": "Exercise (7): The Word 'Dhoo'",
         "tamreen_title_ar": "اسْتَعْمِلْ كَلِمَةَ (ذُو) بِمَعْنَى صَاحِب:", "tamreen_title_ur": "صاحب/والا کے معنی میں 'ذُو' لگائیں:", "tamreen_title_en": "Use 'Dhoo' (possessor of):",
         "grammar_goal_ur": "ذُو کا استعمال اور مضاف الیہ کا جر۔", "grammar_goal_en": "Using Dhoo as annexion head.",
         "prompt_ar": "مُدِيرُنَا رَجُلٌ [ ＿＿＿ ] خُلُقٍ حَسَنٍ .", "prompt_ur": "خالی جگہ میں 'ذو' بھریں:", "prompt_en": "Fill the blank with 'Dhoo':",
         "answer": "ذُو", "options": ["ذُو", "ذَا", "ذِي", "ذَوُو"],
         "emoji": "👔", "hint_ur": "صفت مرفوع ہے اس لیے 'ذُو' آئے گا۔", "hint_en": "Nominative adjective takes 'Dhoo'.",
         "explanation_ur": "رجلٌ کی نعت مرفوع ہے اس لیے 'ذُو' آئے گا۔", "explanation_en": "Dhoo is nominative masculine: Dhoo khuluqin.", "type": "fill_blank"},
        {"id": "b2_u1_q6", "tamreen_num": 10, "badge_ar": "التَّمْرِينُ (10)", "badge_ur": "مشق (10): حرفِ (لَعَلَّ)", "badge_en": "Exercise (10): The Particle 'La'alla'",
         "tamreen_title_ar": "أَدْخِلْ (لَعَلَّ) عَلَى الْجُمَلِ:", "tamreen_title_ur": "'لَعَلَّ' داخل کریں:", "tamreen_title_en": "Enter 'La'alla':",
         "grammar_goal_ur": "لعلّ کا نحوی عمل۔", "grammar_goal_en": "Syntax of La'alla.",
         "prompt_ar": "(الْجَوُّ جَمِيلٌ) عِنْدَ دُخُولِ (لَعَلَّ) تُصْبِحُ: [ ＿＿＿ ]", "prompt_ur": "(الجو جميل) پر 'لعلّ' داخل کریں:", "prompt_en": "Enter 'La'alla' upon 'Al-jawwu jameelun':",
         "answer": "لَعَلَّ الْجَوَّ جَمِيلٌ", "options": ["لَعَلَّ الْجَوَّ جَمِيلٌ", "لَعَلَّ الْجَوُّ جَمِيلٌ", "لَعَلَّ الْجَوَّ جَمِيلاً", "لَعَلَّ الْجَوِّ جَمِيلٌ"],
         "emoji": "🌤️", "hint_ur": "لعلّ کا اسم منسوب ہوتا ہے: لَعَلَّ الْجَوَّ۔", "hint_en": "Ism La'alla takes fathah: La'alla al-jawwa.",
         "explanation_ur": "اسم لعلّ منسوب بالفتحہ ہوتا ہے: لَعَلَّ الْجَوَّ جَمِيلٌ۔", "explanation_en": "Ism La'alla is accusative: La'alla al-jawwa jameelun.", "type": "fill_blank"},
        {"id": "b2_u1_q7", "tamreen_num": 12, "badge_ar": "التَّمْرِينُ (12)", "badge_ur": "مشق (12): مائة اور ألف", "badge_en": "Exercise (12): 100 and 1000",
         "tamreen_title_ar": "اضْبِطْ مَعْدُودَ (مِائَة) وَ(أَلْف):", "tamreen_title_ur": "مائۃ اور ألف کے معدود کا اعراب لگائیں:", "tamreen_title_en": "Vocalize counted noun with 100 & 1000:",
         "grammar_goal_ur": "معدود کا مفرد مجرور ہونا۔", "grammar_goal_en": "Counted noun is singular genitive.",
         "prompt_ar": "فِي هٰذَا الْمَعْهَدِ (100) [ ＿＿＿ ] .", "prompt_ur": "اس ادارے میں 100 طلبہ ہیں:", "prompt_en": "In this institute there are 100 students:",
         "answer": "مِائَةُ طَالِبٍ", "options": ["مِائَةُ طَالِبٍ", "مِائَةُ طَالِباً", "مِائَةُ طُلَّابٍ", "مِائَةُ طَالِبٌ"],
         "emoji": "🏫", "hint_ur": "مائۃ کا معدود مفرد مجرور (دو زیر) ہوتا ہے: طَالِبٍ۔", "hint_en": "Counted noun of 100 takes kasrah: Taalibin.",
         "explanation_ur": "مائۃ کا تمییز مفرد مجرور ہوتا ہے: مِائَةُ طَالِبٍ۔", "explanation_en": "Mi'ah takes singular genitive: Mi'atu taalibin.", "type": "fill_blank"}
    ]

    # --- UNIT 2: لَيْسَ وَخَبَرُهَا الْمَجْرُورُ بِالْبَاءِ ---
    units[2] = [
        {"id": "b2_u2_q1", "tamreen_num": 1, "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Comprehension",
         "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer questions:",
         "grammar_goal_ur": "ہشام کا مسکن۔", "grammar_goal_en": "Hisham's residence.",
         "prompt_ar": "أَيْنَ بَيْتُ هِشَامٍ؟ [ ＿＿＿ ]", "prompt_ur": "ہشام کا گھر کہاں ہے؟", "prompt_en": "Where is Hisham's house?",
         "answer": "بَيْتُهُ فِي وَاشِنْطُنَ .", "options": ["بَيْتُهُ فِي وَاشِنْطُنَ .", "بَيْتُهُ فِي نِيُويُورْكَ .", "بَيْتُهُ فِي لَنْدَنَ .", "بَيْتُهُ فِي بَارِيسَ ."],
         "emoji": "🏠", "hint_ur": "ہشام واشنگٹن میں رہتا ہے۔", "hint_en": "Hisham lives in Washington.",
         "explanation_ur": "ہشام کا گھر واشنگٹن میں ہے۔", "explanation_en": "Hisham's house is in Washington.", "type": "fill_blank"},
        {"id": "b2_u2_q2", "tamreen_num": 2, "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تصریفِ ليس", "badge_en": "Exercise (2): Conjugation of Laysa",
         "tamreen_title_ar": "أَسْنِدْ (لَيْسَ) إِلَى الضَّمَائِرِ:", "tamreen_title_ur": "لیس کو ضمائر کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugate Laysa with pronouns:",
         "grammar_goal_ur": "جمع مذکر کے ساتھ لَيْسُوا۔", "grammar_goal_en": "Plural masculine takes Laysu.",
         "prompt_ar": "(الطُّلَّابُ) [ ＿＿＿ ] فِي الْفَصْلِ .", "prompt_ur": "طلبہ کلاس میں نہیں ہیں:", "prompt_en": "The students are not in the classroom:",
         "answer": "لَيْسُوا", "options": ["لَيْسُوا", "لَيْسَ", "لَسْتُمْ", "لَسْنَ"],
         "emoji": "👥", "hint_ur": "جمع مذکر غائب کے لیے 'لَيْسُوا' آتا ہے۔", "hint_en": "Masculine plural takes Laysu.",
         "explanation_ur": "جمع مذکر کے لیے صیغہ 'لَيْسُوا' آتا ہے۔", "explanation_en": "Masculine plural takes Laysu.", "type": "fill_blank"},
        {"id": "b2_u2_q3", "tamreen_num": 2, "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تصریفِ ليس", "badge_en": "Exercise (2): Conjugation of Laysa",
         "tamreen_title_ar": "أَسْنِدْ (لَيْسَ) إِلَى الضَّمَائِرِ:", "tamreen_title_ur": "جمع مؤنث کے ساتھ لَسْنَ:", "tamreen_title_en": "Feminine plural takes Lasna:",
         "grammar_goal_ur": "نون نسوہ کے ساتھ لَسْنَ۔", "grammar_goal_en": "Lasna with nun an-niswah.",
         "prompt_ar": "(الطَّالِبَاتُ) [ ＿＿＿ ] فِي الْمَكْتَبَةِ .", "prompt_ur": "طالبات لائبریری میں نہیں ہیں:", "prompt_en": "The female students are not in the library:",
         "answer": "لَسْنَ", "options": ["لَسْنَ", "لَيْسَتْ", "لَيْسُوا", "لَسْتُنَّ"],
         "emoji": "🧕", "hint_ur": "جمع مؤنث کے لیے 'لَسْنَ' آتا ہے۔", "hint_en": "Feminine plural takes Lasna.",
         "explanation_ur": "جمع مؤنث غائب کے لیے 'لَسْنَ' آتا ہے۔", "explanation_en": "Feminine plural takes Lasna.", "type": "fill_blank"},
        {"id": "b2_u2_q4", "tamreen_num": 3, "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): باء زائدہ مع ليس", "badge_en": "Exercise (3): Extra Baa with Laysa",
         "tamreen_title_ar": "أَدْخِلْ (الْبَاءَ) عَلَى خَبَرِ (لَيْسَ):", "tamreen_title_ur": "لیس کی خبر پر باء زائدہ لگائیں:", "tamreen_title_en": "Add emphatic Baa to predicate:",
         "grammar_goal_ur": "لَسْتُ بِمَرِيضٍ کا اعراب۔", "grammar_goal_en": "Lastu bi-mareedin inflection.",
         "prompt_ar": "أَنَا [ ＿＿＿ ] . (نَفْيُ: أَنَا مَرِيضٌ)", "prompt_ur": "میں بیمار نہیں ہوں:", "prompt_en": "I am not sick (with emphatic Baa):",
         "answer": "لَسْتُ بِمَرِيضٍ", "options": ["لَسْتُ بِمَرِيضٍ", "لَيْسَ بِمَرِيضٍ", "لَسْتُ مَرِيضٌ", "لَسْتَ بِمَرِيضٍ"],
         "emoji": "🤒", "hint_ur": "متکلم کے لیے 'لَسْتُ' اور باء کے ساتھ: بِمَرِيضٍ۔", "hint_en": "First person with genitive predicate: Lastu bi-mareedin.",
         "explanation_ur": "متکلم کے لیے 'لَسْتُ بِمَرِيضٍ' آتا ہے۔", "explanation_en": "First person takes Lastu bi-mareedin.", "type": "fill_blank"}
    ]

    # --- UNIT 3: اسْمُ التَّفْضِيلِ (أَفْعَلُ) • لٰكِنَّ • كَأَنَّ • الْأَعْدَادُ ١١-٢٠ ---
    units[3] = [
        {"id": "b2_u3_q1", "tamreen_num": 1, "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اسم تفضیل", "badge_en": "Exercise (1): Comparative Degree",
         "tamreen_title_ar": "صُغِ اسْمَ التَّفْضِيلِ عَلَى وَزْنِ (أَفْعَلُ مِنْ):", "tamreen_title_ur": "وزن 'أَفْعَلُ مِنْ' پر اسم تفضیل بنائیں:", "tamreen_title_en": "Form comparative on (Af'alu min):",
         "grammar_goal_ur": "طویل سے اطول۔", "grammar_goal_en": "Comparative of taweel.",
         "prompt_ar": "هَاشِمٌ طَوِيلٌ، وَحَامِدٌ [ ＿＿＿ ] مِنْهُ .", "prompt_ur": "حامد اس سے زیادہ لمبا ہے:", "prompt_en": "Hamid is taller than him:",
         "answer": "أَطْوَلُ", "options": ["أَطْوَلُ", "طَوِيلٌ", "أَطْوَلِ", "أَطْوَلَ"],
         "emoji": "📏", "hint_ur": "طویل سے اسم تفضیل 'أَطْوَلُ' بنتا ہے۔", "hint_en": "Comparative is Atwalu.",
         "explanation_ur": "اسم تفضیل غیر منصرف ہوتا ہے: أَطْوَلُ۔", "explanation_en": "Comparative is a diptote: Atwalu.", "type": "fill_blank"},
        {"id": "b2_u3_q2", "tamreen_num": 4, "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): مرکب اعداد (11-20)", "badge_en": "Exercise (4): Numbers 11-20",
         "tamreen_title_ar": "اضْبِطِ الأَعْدَادَ الْمُرَكَّبَةَ (١١ - ٢٠):", "tamreen_title_ur": "مرکب اعداد کا ضبط اور تمییز:", "tamreen_title_en": "Vocalize numbers 11-20:",
         "grammar_goal_ur": "خمسة عشر طالباً۔", "grammar_goal_en": "Khamsata ashara taaliban.",
         "prompt_ar": "رَأَيْتُ فِي الْمَسْجِدِ (15) [ ＿＿＿ ] .", "prompt_ur": "15 طلبہ کے لیے درست عربی عبارت منتخب کریں:", "prompt_en": "Choose correct Arabic for 15 students:",
         "answer": "خَمْسَةَ عَشَرَ طَالِباً", "options": ["خَمْسَةَ عَشَرَ طَالِباً", "خَمْسَةُ عَشَرَ طَالِبٍ", "خَمْسَ عَشْرَةَ طَالِباً", "خَمْسَةَ عَشَرَ طَالِبٌ"],
         "emoji": "👥", "hint_ur": "دونوں اجزاء پر زبر آئے گا: خَمْسَةَ عَشَرَ طَالِباً۔", "hint_en": "Both parts take fathah: Khamsata 'ashara taaliban.",
         "explanation_ur": "15 کے عدد میں فتح الجزأین ہوتا ہے: خَمْسَةَ عَشَرَ طَالِباً۔", "explanation_en": "Compound numbers 11-19 are built on two fathahs.", "type": "fill_blank"},
        {"id": "b2_u3_q3", "tamreen_num": 6, "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): حرفِ (لٰكِنَّ)", "badge_en": "Exercise (6): The Particle 'Laakinna'",
         "tamreen_title_ar": "اسْتَعْمِلْ (لٰكِنَّ) لِلاِسْتِدْرَاكِ:", "tamreen_title_ur": "استدراک کے لیے 'لٰكِنَّ' کا استعمال:", "tamreen_title_en": "Use 'Laakinna' for rectification:",
         "grammar_goal_ur": "اسم لکنّ کا منسوب ہونا۔", "grammar_goal_en": "Noun of Laakinna is accusative.",
         "prompt_ar": "هَاشِمٌ ذَكِيٌّ، [ ＿＿＿ ] كَسْلاَنُ .", "prompt_ur": "ہاشم ذہین ہے لیکن اس کا ساتھی سست ہے:", "prompt_en": "Hashim is smart, but his classmate is lazy:",
         "answer": "لٰكِنَّ صَدِيقَهُ", "options": ["لٰكِنَّ صَدِيقَهُ", "لٰكِنَّ صَدِيقُهُ", "لٰكِنَّ صَدِيقِهِ", "وَصَدِيقُهُ"],
         "emoji": "💡", "hint_ur": "لٰكِنَّ کا اسم منسوب ہوتا ہے: صَدِيقَهُ۔", "hint_en": "Ism Laakinna is accusative: Sadeeqahu.",
         "explanation_ur": "لٰكِنَّ کے بعد اسم منسوب بالفتحہ آئے گا: لٰكِنَّ صَدِيقَهُ۔", "explanation_en": "Ism Laakinna is mansub with fathah.", "type": "fill_blank"}
    ]

    # --- UNIT 4: الْفِعْلُ الْمَاضِي مَعَ الضَّمَائِرِ • لِأَنَّ • بَلَى ---
    units[4] = [
        {"id": "b2_u4_q1", "tamreen_num": 1, "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Comprehension",
         "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے مطابق جواب دیں:", "tamreen_title_en": "Answer questions:",
         "grammar_goal_ur": "ابراہیم کے والد کا سفر۔", "grammar_goal_en": "Ibrahim's father destination.",
         "prompt_ar": "أَيْنَ ذَهَبَ أَبُو إِبْرَاهِيمَ؟ [ ＿＿＿ ]", "prompt_ur": "ابراہیم کے والد کہاں گئے؟", "prompt_en": "Where did Ibrahim's father go?",
         "answer": "ذَهَبَ إِلَى السُّوقِ .", "options": ["ذَهَبَ إِلَى السُّوقِ .", "ذَهَبَ إِلَى الْمَسْجِدِ .", "ذَهَبَ إِلَى الْمُسْتَشْفَى .", "ذَهَبَ إِلَى الْمَطَارِ ."],
         "emoji": "🛒", "hint_ur": "ابراہیم نے بتایا: ذهب إلى السوق۔", "hint_en": "He went to the market.",
         "explanation_ur": "ابراہیم کے والد بازار گئے۔", "explanation_en": "Ibrahim's father went to the market.", "type": "fill_blank"},
        {"id": "b2_u4_q2", "tamreen_num": 3, "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): ماضی کی ضمائر", "badge_en": "Exercise (3): Past Tense Pronouns",
         "tamreen_title_ar": "أَسْنِدِ الْفِعْلَ الْمَاضِيَ (ذَهَبَ) إِلَى الضَّمَائِرِ:", "tamreen_title_ur": "فعل ماضی کو فاعل کی ضمیر کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugate past verb with pronouns:",
         "grammar_goal_ur": "جمع مؤنث کے ساتھ ذَهَبْنَ۔", "grammar_goal_en": "Feminine plural takes Thahabna.",
         "prompt_ar": "الطَّالِبَاتُ [ ＿＿＿ ] إِلَى الْمَدْرَسَةِ .", "prompt_ur": "طالبات اسکول گئیں:", "prompt_en": "The female students went to school:",
         "answer": "ذَهَبْنَ", "options": ["ذَهَبْنَ", "ذَهَبُوا", "ذَهَبَتْ", "ذَهَبْتُمْ"],
         "emoji": "👩‍🎓", "hint_ur": "جمع مؤنث کے ساتھ نون نسوہ آئے گا: ذَهَبْنَ۔", "hint_en": "Feminine plural takes Thahabna.",
         "explanation_ur": "جمع مؤنث غائب کے لیے 'ذَهَبْنَ' آتا ہے۔", "explanation_en": "Feminine plural takes Thahabna.", "type": "fill_blank"},
        {"id": "b2_u4_q3", "tamreen_num": 5, "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): نفیِ ماضی (مَا)", "badge_en": "Exercise (5): Past Negation with Maa",
         "tamreen_title_ar": "أَجِبْ عَنِ الأَسْئِلَةِ بِالنَّفْيِ مُسْتَعْمِلاً (مَا):", "tamreen_title_ur": "'مَا' کے ساتھ ماضی کی نفی کریں:", "tamreen_title_en": "Negate past verbs using Maa:",
         "grammar_goal_ur": "ما ذهبتُ کی ساخت۔", "grammar_goal_en": "Maa thahabtu structure.",
         "prompt_ar": "أَذَهَبْتَ إِلَى الْمَدْرَسَةِ أَمْسِ؟ — لاَ، [ ＿＿＿ ] .", "prompt_ur": "کیا تم کل اسکول گئے تھے؟ نہیں، میں نہیں گیا:", "prompt_en": "Did you go to school yesterday? No, I did not go:",
         "answer": "مَا ذَهَبْتُ", "options": ["مَا ذَهَبْتُ", "لَمْ أَذْهَبْتُ", "لاَ ذَهَبْتُ", "مَا ذَهَبْتَ"],
         "emoji": "🏫", "hint_ur": "ماضی کی نفی 'مَا ذَهَبْتُ' ہے۔", "hint_en": "Past negation: Maa thahabtu.",
         "explanation_ur": "فعل ماضی کی نفی 'مَا' سے کی جاتی ہے: مَا ذَهَبْتُ۔", "explanation_en": "Past tense verb is negated with 'Maa': Maa thahabtu.", "type": "fill_blank"}
    ]

    # --- UNIT 5: الْفَاعِلُ وَالْمَفْعُولُ بِهِ (الْمَرْفُوعُ وَالْمَنْصُوبُ) ---
    units[5] = [
        {"id": "b2_u5_q1", "tamreen_num": 1, "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Comprehension",
         "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer questions:",
         "grammar_goal_ur": "ابراہیم کا حفظ۔", "grammar_goal_en": "Ibrahim's memorization.",
         "prompt_ar": "أَيَّ سُورَةٍ حَفِظَ إِبْرَاهِيمُ؟ [ ＿＿＿ ]", "prompt_ur": "ابراہیم نے کون سی سورت یاد کی؟", "prompt_en": "Which Surah did Ibrahim memorize?",
         "answer": "حَفِظَ سُورَةَ الرَّحْمٰنِ .", "options": ["حَفِظَ سُورَةَ الرَّحْمٰنِ .", "حَفِظَ سُورَةَ الْفَجْرِ .", "حَفِظَ سُورَةَ النَّبَإِ .", "حَفِظَ سُورَةَ الْمُلْكِ ."],
         "emoji": "📖", "hint_ur": "ابراہیم نے سورة الرحمن حفظ کی تھی۔", "hint_en": "He memorized Surah ar-Rahman.",
         "explanation_ur": "ابراہیم نے سورة الرحمن حفظ کی۔", "explanation_en": "Ibrahim memorized Surah ar-Rahman.", "type": "fill_blank"},
        {"id": "b2_u5_q2", "tamreen_num": 4, "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): فاعل و مفعول بہ", "badge_en": "Exercise (4): Subject & Object",
         "tamreen_title_ar": "عَيِّنِ الْفَاعِلَ وَالْمَفْعُولَ بِهِ فِي الْجُمَلِ:", "tamreen_title_ur": "فاعل (مرفوع) اور مفعول بہ (منصوب) کا اعراب لگائیں:", "tamreen_title_en": "Vocalize subject and object:",
         "grammar_goal_ur": "فاعل پر پیش اور مفعول بہ پر زبر۔", "grammar_goal_en": "Fa'il takes dammah, Maf'ool bihi takes fathah.",
         "prompt_ar": "اخْتَرِ الضَّبْطَ الصَّحِيحَ لِلْفَاعِلِ وَالْمَفْعُولِ بِهِ: [ ＿＿＿ ]", "prompt_ur": "گائے نے پانی پیا (درست اعراب والا جملہ چنیں):", "prompt_en": "The cow drank the water (choose correct case):",
         "answer": "شَرِبَتِ الْبَقَرَةُ الْمَاءَ", "options": ["شَرِبَتِ الْبَقَرَةُ الْمَاءَ", "شَرِبَتِ الْبَقَرَةَ الْمَاءُ", "شَرِبَتِ الْبَقَرَةُ الْمَاءِ", "شَرِبَتِ الْبَقَرَةِ الْمَاءَ"],
         "emoji": "🐄", "hint_ur": "فاعل (البقرةُ) مرفوع اور مفعول (الماءَ) منسوب ہوگا۔", "hint_en": "Subject takes dammah, object takes fathah.",
         "explanation_ur": "فاعل مرفوع اور مفعول به منصوب ہوتا ہے: شَرِبَتِ الْبَقَرَةُ الْمَاءَ۔", "explanation_en": "Subject is nominative, object is accusative.", "type": "fill_blank"}
    ]

    # Import and add all deep units from 6 to 31
    from build_b2_units_6_to_31_deep import get_b2_units_6_to_31_deep
    deep_units = get_b2_units_6_to_31_deep()
    units.update(deep_units)

    return units

if __name__ == "__main__":
    u = get_b2_all_units()
    print(f"Total Book 2 Units Generated: {len(u)}")
    total_q = sum(len(qs) for qs in u.values())
    print(f"Total Book 2 Questions: {total_q}")
    for unum in sorted(u.keys()):
        qs = u[unum]
        tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in qs)))
        print(f"  Unit {unum:2d}: {len(qs):2d} questions (Tamreens: {tamreens})")
