import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_b2_part1():
    units = {}
    
    # -------------------------------------------------------------
    # UNIT 1: إِنَّ وَأَخَوَاتُهَا • لَعَلَّ • ذُو • مِائَةٌ وَأَلْفٌ
    # -------------------------------------------------------------
    units[1] = [
        {
            "id": "b2_u1_q1", "book": 2, "unit_num": 1, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ مکالمہ", "badge_en": "Exercise (1): Dialogue Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the comprehension questions:",
            "grammar_goal_ur": "سوالیہ جملے کا فہم اور درست جواب کی تشکیل۔", "grammar_goal_en": "Comprehending interrogatives and forming accurate answers.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مِنْ أَيْنَ هَاشِمٌ؟ [ ＿＿＿ ]", "prompt_ur": "ہاشم کہاں سے ہے؟ درست جواب منتخب کریں:", "prompt_en": "Where is Hashim from? Select the correct answer:",
            "answer": "هُوَ مِنَ الْهِنْدِ .", "options": ["هُوَ مِنَ الْهِنْدِ .", "هُوَ مِنَ الْيَابَانِ .", "هُوَ مِنَ الصِّينِ .", "هُوَ مِنَ الْبَاكِسْتَانِ ."],
            "emoji": "🇮🇳", "hint_ur": "وہ ہندوستان سے ہے۔", "hint_en": "He is from India.",
            "explanation_ur": "درست جواب: 'هُوَ مِنَ الْهِنْدِ .' (سبق کے مطابق ہاشم ہندوستان سے ہے)",
            "explanation_en": "Correct answer: 'هُوَ مِنَ الْهِنْدِ .' (Hashim is from India)"
        },
        {
            "id": "b2_u1_q2", "book": 2, "unit_num": 1, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): ضمیروں پر (إِنَّ) کا داخل ہونا", "badge_en": "Exercise (4): Attaching Pronouns to Inna",
            "tamreen_title_ar": "أَدْخِلْ (إِنَّ) عَلَى الْجُمَلِ الآتِيَةِ:", "tamreen_title_ur": "ضمیروں پر 'إِنَّ' داخل کریں:", "tamreen_title_en": "Enter Inna onto pronoun sentences:",
            "grammar_goal_ur": "منفصل ضمیروں کا 'إنّ' کے ساتھ متصل منصوب ضمیر میں تبدیل ہونا۔", "grammar_goal_en": "Converting detached pronouns to attached accusative pronouns with Inna.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هُوَ تَاجِرٌ ➔ [ ＿＿＿ ] تَاجِرٌ .", "prompt_ur": "هُوَ تَاجِرٌ پر إِنَّ داخل کریں:", "prompt_en": "Enter Inna onto 'هُوَ تَاجِرٌ':",
            "answer": "إِنَّهُ", "options": ["إِنَّهُ", "إِنَّ هُوَ", "إِنَّكَ", "إِنَّهُمْ"],
            "emoji": "💼", "hint_ur": "بے شک وہ ایک تاجر ہے۔", "hint_en": "Indeed, he is a merchant.",
            "explanation_ur": "درست جواب: 'إِنَّهُ'", "explanation_en": "Correct answer: 'إِنَّهُ'"
        },
        {
            "id": "b2_u1_q3", "book": 2, "unit_num": 1, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): ضمیرِ متکلم کے ساتھ (إِنِّي)", "badge_en": "Exercise (4): 1st Person with Inna",
            "tamreen_title_ar": "أَدْخِلْ (إِنَّ) مَعَ ضَمِيرِ الْمُتَكَلِّمِ:", "tamreen_title_ur": "متکلم کی ضمیر کے ساتھ 'إِنَّ' لگائیں:", "tamreen_title_en": "Attach Inna to 1st person pronoun:",
            "grammar_goal_ur": "'أنا' پر إنّ داخل ہو کر 'إنّي' بنتی ہے۔", "grammar_goal_en": "Forming 'Innee' from Inna + Ana.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا طَالِبٌ ➔ [ ＿＿＿ ] طَالِبٌ .", "prompt_ur": "أَنَا طَالِبٌ پر إِنَّ داخل کریں:", "prompt_en": "Enter Inna onto 'أَنَا طَالِبٌ':",
            "answer": "إِنِّي", "options": ["إِنِّي", "إِنَّ أَنَا", "إِنَّنَا", "إِنَّكَ"],
            "emoji": "👨‍🎓", "hint_ur": "بے شک میں طالب علم ہوں۔", "hint_en": "Indeed, I am a student.",
            "explanation_ur": "درست جواب: 'إِنِّي' (أنا سے إِنِّي یا إِنَّنِي بنتا ہے)", "explanation_en": "Correct answer: 'إِنِّي'"
        },
        {
            "id": "b2_u1_q4", "book": 2, "unit_num": 1, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): اسم پر (إِنَّ) کا داخل ہونا اور اعراب", "badge_en": "Exercise (6): Inna with Nouns",
            "tamreen_title_ar": "أَدْخِلْ (إِنَّ) وَاضْبِطْ أَوَاخِرَ الْكَلِمَاتِ:", "tamreen_title_ur": "اسم پر 'إِنَّ' داخل کر کے درست اعراب لگائیں:", "tamreen_title_en": "Enter Inna and apply accusative fathah to the noun:",
            "grammar_goal_ur": "إنّ کے اسم کا منسوب (زبر) ہونا۔", "grammar_goal_en": "Applying accusative case to Inna's subject.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "السَّيَّارَةُ جَمِيلَةٌ ➔ [ ＿＿＿ ] جَمِيلَةٌ .", "prompt_ur": "السَّيَّارَةُ پر إِنَّ داخل کریں:", "prompt_en": "Enter Inna onto 'السَّيَّارَةُ':",
            "answer": "إِنَّ السَّيَّارَةَ", "options": ["إِنَّ السَّيَّارَةَ", "إِنَّ السَّيَّارَةُ", "إِنَّ السَّيَّارَةِ", "إِنَّ سَيَّارَةً"],
            "emoji": "🚗", "hint_ur": "بے شک گاڑی خوبصورت ہے۔", "hint_en": "Indeed, the car is beautiful.",
            "explanation_ur": "درست جواب: 'إِنَّ السَّيَّارَةَ' (إنّ اپنے اسم کو زبر دیتی ہے)",
            "explanation_en": "Correct answer: 'إِنَّ السَّيَّارَةَ' (Subject of Inna takes accusative fathah)"
        },
        {
            "id": "b2_u1_q5", "book": 2, "unit_num": 1, "tamreen_num": 7,
            "badge_ar": "التَّمْرِينُ (7)", "badge_ur": "مشق (7): اسم تفضیل (أَفْعَلُ مِنْ)", "badge_en": "Exercise (7): Comparative Degree",
            "tamreen_title_ar": "صُغِ اسْمَ التَّفْضِيلِ عَلَى وَزْنِ (أَفْعَلُ):", "tamreen_title_ur": "صفت کو اسم تفضیل 'أَفْعَلُ مِنْ' کے وزن پر لائیں:", "tamreen_title_en": "Form the comparative degree on 'Af'alu min':",
            "grammar_goal_ur": "عربی میں دو چیزوں کا موازنہ کرنے کا قاعدہ۔", "grammar_goal_en": "Comparing two items using 'Af'alu min'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذَا الْكِتَابُ سَهْلٌ وَذٰلِكَ [ ＿＿＿ ] مِنْهُ .", "prompt_ur": "سَهْلٌ کا اسم تفضیل منتخب کریں:", "prompt_en": "Select the comparative form of 'سَهْلٌ':",
            "answer": "أَسْهَلُ", "options": ["أَسْهَلُ", "أَصْعَبُ", "سَهْلٌ", "أَسْهَلِ"],
            "emoji": "📖", "hint_ur": "یہ کتاب آسان ہے اور وہ اس سے زیادہ آسان ہے۔", "hint_en": "This book is easy, and that is easier than it.",
            "explanation_ur": "درست جواب: 'أَسْهَلُ' (سھل کا اسم تفضیل أَسْهَلُ ہے)",
            "explanation_en": "Correct answer: 'أَسْهَلُ' (Comparative of sahl is as-halu)"
        },
        {
            "id": "b2_u1_q6", "book": 2, "unit_num": 1, "tamreen_num": 8,
            "badge_ar": "التَّمْرِينُ (8)", "badge_ur": "مشق (8): کلمہ (ذُو) کا استعمال", "badge_en": "Exercise (8): Using 'Dhu'",
            "tamreen_title_ar": "اسْتَعْمِلْ كَلِمَةَ (ذُو) بِمَعْنَى صَاحِب:", "tamreen_title_ur": "صاحب/والا کے معنی میں 'ذُو' لگائیں:", "tamreen_title_en": "Use 'Dhu' (possessor of):",
            "grammar_goal_ur": "'ذو' ہمیشہ مضاف ہوتا ہے اور اس کے بعد اسم مجرور ہوتا ہے۔", "grammar_goal_en": "Dhu is mudhaf followed by a genitive mudhaf ilayh.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَنْ هٰذَا الرَّجُلُ ذُو [ ＿＿＿ ] ؟", "prompt_ur": "ذُو کے بعد درست مجرور اسم منتخب کریں:", "prompt_en": "Select the correct genitive noun after 'ذُو':",
            "answer": "النَّظَّارَةِ", "options": ["النَّظَّارَةِ", "النَّظَّارَةُ", "النَّظَّارَةَ", "نَظَّارَةٌ"],
            "emoji": "👓", "hint_ur": "چشمے والا یہ آدمی کون ہے؟", "hint_en": "Who is this man with glasses?",
            "explanation_ur": "درست جواب: 'النَّظَّارَةِ' (ذو کے بعد مضاف الیہ مجرور ہوتا ہے)",
            "explanation_en": "Correct answer: 'النَّظَّارَةِ' (Genitive after Dhu)"
        },
        {
            "id": "b2_u1_q7", "book": 2, "unit_num": 1, "tamreen_num": 10,
            "badge_ar": "التَّمْرِينُ (10)", "badge_ur": "مشق (10): (لَعَلَّ) کا استعمال", "badge_en": "Exercise (10): Using 'La'alla'",
            "tamreen_title_ar": "أَدْخِلْ (لَعَلَّ) عَلَى الْجُمَلِ الآتِيَةِ:", "tamreen_title_ur": "امید/اندیشے کے لیے 'لَعَلَّ' داخل کریں:", "tamreen_title_en": "Enter 'La'alla' (perhaps / hopefully):",
            "grammar_goal_ur": "'لعلّ' کے اسم کا منسوب ہونا۔", "grammar_goal_en": "Accusative noun with La'alla.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْجَوُّ بَارِدٌ ➔ [ ＿＿＿ ] بَارِدٌ .", "prompt_ur": "الْجَوُّ پر لَعَلَّ داخل کریں:", "prompt_en": "Enter La'alla onto 'الْجَوُّ':",
            "answer": "لَعَلَّ الْجَوَّ", "options": ["لَعَلَّ الْجَوَّ", "لَعَلَّ الْجَوُّ", "لَعَلَّ الْجَوِّ", "إِنَّ الْجَوُّ"],
            "emoji": "❄️", "hint_ur": "شاید موسم ٹھنڈا ہے۔", "hint_en": "Perhaps the weather is cold.",
            "explanation_ur": "درست جواب: 'لَعَلَّ الْجَوَّ' (لعلّ اپنے اسم کو زبر دیتی ہے)",
            "explanation_en": "Correct answer: 'لَعَلَّ الْجَوَّ' (Noun of La'alla takes fathah)"
        },
        {
            "id": "b2_u1_q8", "book": 2, "unit_num": 1, "tamreen_num": 12,
            "badge_ar": "التَّمْرِينُ (12)", "badge_ur": "مشق (12): (مِائَة) اور (أَلْف) کا معدود", "badge_en": "Exercise (12): Counted Nouns with 100 & 1000",
            "tamreen_title_ar": "اضْبِطْ مَعْدُودَ (مِائَة) وَ (أَلْف):", "tamreen_title_ur": "'مِائَة' اور 'أَلْف' کے بعد معدود کا اعراب لگائیں:", "tamreen_title_en": "Apply correct case to counted nouns after Mi'ah (100) and Alf (1000):",
            "grammar_goal_ur": "سو اور ہزار کا معدود مفرد مجرور ہوتا ہے۔", "grammar_goal_en": "Counted nouns with 100/1000 are singular majroor.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي هٰذِهِ الْكُلِّيَّةِ أَلْفُ [ ＿＿＿ ] .", "prompt_ur": "أَلْفُ کے بعد درست معدود منتخب کریں:", "prompt_en": "Select the correct counted noun after 'أَلْفُ':",
            "answer": "طَالِبٍ", "options": ["طَالِبٍ", "طَالِباً", "طَالِبٌ", "طُلَّابٍ"],
            "emoji": "🏫", "hint_ur": "اس کالج میں ایک ہزار طلبہ ہیں۔", "hint_en": "In this college there are one thousand students.",
            "explanation_ur": "درست جواب: 'طَالِبٍ' (ألف کا معدود مفرد مجرور ہوتا ہے)",
            "explanation_en": "Correct answer: 'طَالِبٍ' (Counted noun with Alf is singular genitive)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 2: لَيْسَ وَخَبَرُهَا الْمَجْرُورُ بِالْبَاءِ
    # -------------------------------------------------------------
    units[2] = [
        {
            "id": "b2_u2_q1", "book": 2, "unit_num": 2, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): نفی بِـ (لَيْسَ) مع الباء", "badge_en": "Exercise (2): Negation with Laysa & Ba",
            "tamreen_title_ar": "انْفِ الْجُمَلَ الآتِيَةَ بِـ (لَيْسَ) وَالْبَاءِ:", "tamreen_title_ur": "'لَيْسَ' داخل کریں اور خبر پر 'بِـ' لگائیں:", "tamreen_title_en": "Negate with Laysa and prefix 'bi-' to predicate:",
            "grammar_goal_ur": "لیس کی خبر پر بائے زائدہ داخل کر کے تاکید کے ساتھ نفی کرنا۔", "grammar_goal_en": "Using prefix 'bi-' on predicate of Laysa for emphasis.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمَاءُ بَارِدٌ ➔ لَيْسَ الْمَاءُ [ ＿＿＿ ] .", "prompt_ur": "درست خبر منتخب کریں:", "prompt_en": "Select the correct predicate with 'bi-':",
            "answer": "بِبَارِدٍ", "options": ["بِبَارِدٍ", "بِبَارِدٌ", "بِبَارِداً", "بَارِدٌ"],
            "emoji": "💧", "hint_ur": "پانی ٹھنڈا نہیں ہے۔", "hint_en": "The water is not cold.",
            "explanation_ur": "درست جواب: 'بِبَارِدٍ' (بِـ حرف جر کی وجہ سے خبر مجرور ہوگی)",
            "explanation_en": "Correct answer: 'بِبَارِدٍ' (Predicate is majroor with bi-)"
        },
        {
            "id": "b2_u2_q2", "book": 2, "unit_num": 2, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مؤنث کے ساتھ (لَيْسَتْ)", "badge_en": "Exercise (2): Feminine Laysat",
            "tamreen_title_ar": "انْفِ الْجُمْلَةَ الْمُؤَنَّثَةَ بِـ (لَيْسَتْ):", "tamreen_title_ur": "مؤنث اسم کی نفی 'لَيْسَتْ' سے کریں:", "tamreen_title_en": "Negate feminine subject with Laysat:",
            "grammar_goal_ur": "مؤنث کے لیے 'لَيْسَتْ' کا استعمال۔", "grammar_goal_en": "Using Laysat with feminine nouns.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْغُرْفَةُ قَرِيبَةٌ ➔ [ ＿＿＿ ] الْغُرْفَةُ بِقَرِيبَةٍ .", "prompt_ur": "مؤنث کے لیے درست منفی فعل منتخب کریں:", "prompt_en": "Select the feminine negative verb:",
            "answer": "لَيْسَتِ", "options": ["لَيْسَتِ", "لَيْسَ", "لَسْتُ", "مَا"],
            "emoji": "🚪", "hint_ur": "کمرہ قریب نہیں ہے۔", "hint_en": "The room is not near.",
            "explanation_ur": "درست جواب: 'لَيْسَتِ'", "explanation_en": "Correct answer: 'لَيْسَتِ'"
        },
        {
            "id": "b2_u2_q3", "book": 2, "unit_num": 2, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): تصریفِ (لَيْسَ) مع المتکلم", "badge_en": "Exercise (3): 1st Person 'Lastu'",
            "tamreen_title_ar": "صَرِّفْ (لَيْسَ) مَعَ (أَنَا):", "tamreen_title_ur": "'أَنَا' کے ساتھ 'لَيْسَ' کی درست گردان منتخب کریں:", "tamreen_title_en": "Conjugate Laysa with 'Ana' (I am not):",
            "grammar_goal_ur": "متکلم کے ساتھ 'لَسْتُ' کی ساخت۔", "grammar_goal_en": "Conjugating Laysa to Lastu.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا مُدَرِّسٌ ➔ [ ＿＿＿ ] بِمُدَرِّسٍ .", "prompt_ur": "أَنَا کے لیے درست صیغہ منتخب کریں:", "prompt_en": "Select the correct form for 'I am not':",
            "answer": "لَسْتُ", "options": ["لَسْتُ", "لَيْسَ", "لَسْتَ", "لَسْنَا"],
            "emoji": "🧑‍🏫", "hint_ur": "میں استاد نہیں ہوں۔", "hint_en": "I am not a teacher.",
            "explanation_ur": "درست جواب: 'لَسْتُ'", "explanation_en": "Correct answer: 'لَسْتُ'"
        },
        {
            "id": "b2_u2_q4", "book": 2, "unit_num": 2, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): تصریفِ (لَيْسَ) مع المخاطب", "badge_en": "Exercise (3): 2nd Person 'Lasta'",
            "tamreen_title_ar": "صَرِّفْ (لَيْسَ) مَعَ (أَنْتَ):", "tamreen_title_ur": "'أَنْتَ' کے ساتھ 'لَيْسَ' کی شکل:", "tamreen_title_en": "Conjugate Laysa with 'Anta':",
            "grammar_goal_ur": "مخاطب مذکر کے ساتھ 'لَسْتَ' کی ساخت۔", "grammar_goal_en": "Conjugating Laysa to Lasta.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنْتَ مُتَزَوِّجٌ ➔ [ ＿＿＿ ] بِمُتَزَوِّجٍ .", "prompt_ur": "أَنْتَ کے لیے درست منفی فعل منتخب کریں:", "prompt_en": "Select the correct form for 'you are not':",
            "answer": "لَسْتَ", "options": ["لَسْتَ", "لَسْتُ", "لَيْسَ", "لَسْتِ"],
            "emoji": "💍", "hint_ur": "تم شادی شدہ نہیں ہو۔", "hint_en": "You are not married.",
            "explanation_ur": "درست جواب: 'لَسْتَ'", "explanation_en": "Correct answer: 'لَسْتَ'"
        },
        {
            "id": "b2_u2_q5", "book": 2, "unit_num": 2, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): جمع کے ساتھ (لَسْنَا)", "badge_en": "Exercise (3): 1st Person Plural 'Lasnaa'",
            "tamreen_title_ar": "صَرِّفْ (لَيْسَ) مَعَ (نَحْنُ):", "tamreen_title_ur": "'نَحْنُ' (ہم) کے ساتھ 'لَيْسَ' کی شکل:", "tamreen_title_en": "Conjugate Laysa with 'Nahnu' (we are not):",
            "grammar_goal_ur": "متکلم مع الغیر کے ساتھ 'لَسْنَا' کی ساخت۔", "grammar_goal_en": "Conjugating Laysa to Lasnaa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَحْنُ طُلَّابٌ ➔ [ ＿＿＿ ] بِطُلَّابٍ .", "prompt_ur": "نَحْنُ کے لیے درست صیغہ منتخب کریں:", "prompt_en": "Select the correct form for 'we are not':",
            "answer": "لَسْنَا", "options": ["لَسْنَا", "لَسْتُمْ", "لَيْسُوا", "لَسْتُ"],
            "emoji": "👥", "hint_ur": "ہم طلبہ نہیں ہیں۔", "hint_en": "We are not students.",
            "explanation_ur": "درست جواب: 'لَسْنَا'", "explanation_en": "Correct answer: 'لَسْنَا'"
        },
        {
            "id": "b2_u2_q6", "book": 2, "unit_num": 2, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): منفی سوال کا جواب (بَلَى)", "badge_en": "Exercise (4): Answering with Balaa",
            "tamreen_title_ar": "أَجِبْ عَنِ السُّؤَالِ الْمَنْفِيِّ بِـ (بَلَى):", "tamreen_title_ur": "منفی سوال کا اثبات میں جواب دیں:", "tamreen_title_en": "Affirm a negative question using Balaa:",
            "grammar_goal_ur": "منفی استفہام کا اثباتی جواب 'بَلَى' سے دینا۔", "grammar_goal_en": "Using Balaa to answer negative questions affirmatively.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَلَيْسَ هٰذَا كِتَابَكَ؟ ➔ [ ＿＿＿ ] ، هٰذَا كِتَابِي .", "prompt_ur": "درست اثباتی کلمہ منتخب کریں:", "prompt_en": "Select the correct affirmative response:",
            "answer": "بَلَى", "options": ["بَلَى", "نَعَمْ", "لَا", "أَجَلْ"],
            "emoji": "📗", "hint_ur": "کیا یہ تمہاری کتاب نہیں ہے؟ کیوں نہیں، یہ میری کتاب ہے۔", "hint_en": "Is this not your book? Yes indeed, this is my book.",
            "explanation_ur": "درست جواب: 'بَلَى' (منفی سوال کے اثبات میں 'بلى' کہا جاتا ہے)",
            "explanation_en": "Correct answer: 'بَلَى' (Balaa affirms negative interrogative questions)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 3: الْأَعْدَادُ الْمُرَكَّبَةُ (١١ - ٢٠)
    # -------------------------------------------------------------
    units[3] = [
        {
            "id": "b2_u3_q1", "book": 2, "unit_num": 3, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ مکالمہ و سوالات", "badge_en": "Exercise (1): Dialogue Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سوال کا درست جواب دیں:", "tamreen_title_en": "Answer the question:",
            "grammar_goal_ur": "مکالمے کی عبارت کا فہم۔", "grammar_goal_en": "Text comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَمْ طَالِباً جَدِيداً جَاءَ الْيَوْمَ؟ [ ＿＿＿ ]", "prompt_ur": "آج کتنے نئے طلبہ آئے؟ درست جواب منتخب کریں:", "prompt_en": "How many new students came today? Select the correct answer:",
            "answer": "جَاءَ خَمْسَةَ عَشَرَ طَالِباً .", "options": ["جَاءَ خَمْسَةَ عَشَرَ طَالِباً .", "جَاءَ عَشَرَةُ طُلَّابٍ .", "جَاءَ أَرْبَعَةُ طُلَّابٍ .", "جَاءَ عِشْرُونَ طَالِباً ."],
            "emoji": "👨‍🎓", "hint_ur": "پندرہ نئے طلبہ آئے۔", "hint_en": "Fifteen new students came.",
            "explanation_ur": "درست جواب: 'جَاءَ خَمْسَةَ عَشَرَ طَالِباً .'", "explanation_en": "Correct answer: 'جَاءَ خَمْسَةَ عَشَرَ طَالِباً .'"
        },
        {
            "id": "b2_u3_q2", "book": 2, "unit_num": 3, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): عدد (١١) مع مذکر معدود", "badge_en": "Exercise (2): Number 11 with Masculine Noun",
            "tamreen_title_ar": "اسْتَعْمِلِ الْعَدَدَ (١١) مَعَ الْمُذَكَّرِ:", "tamreen_title_ur": "مذکر کے لیے عدد ۱۱ کی درست شکل منتخب کریں:", "tamreen_title_en": "Select the correct form of number 11 with masculine noun:",
            "grammar_goal_ur": "گیارہ کے دونوں اجزاء معدود مذکر کے مطابق مذکر آتے ہیں اور مبنی بر فتح ہوتے ہیں۔", "grammar_goal_en": "Both parts of 11 agree with masculine ma'dood and are fixed on fathah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "رَأَيْتُ [ ＿＿＿ ] كَوْكَباً .", "prompt_ur": "كَوْكَباً (مذکر) کے ساتھ عدد ۱۱ لگائیں:", "prompt_en": "Fill in 11 with masculine 'كَوْكَباً':",
            "answer": "أَحَدَ عَشَرَ", "options": ["أَحَدَ عَشَرَ", "إِحْدَى عَشْرَةَ", "أَحَدُ عَشَرَ", "إِحْدَى عَشَرَ"],
            "emoji": "⭐", "hint_ur": "میں نے گیارہ ستارے دیکھے۔", "hint_en": "I saw eleven stars.",
            "explanation_ur": "درست جواب: 'أَحَدَ عَشَرَ' (مذکر کے لیے 'أَحَدَ عَشَرَ' آتا ہے)",
            "explanation_en": "Correct answer: 'أَحَدَ عَشَرَ' (Masculine 11 is Ahada 'ashara)"
        },
        {
            "id": "b2_u3_q3", "book": 2, "unit_num": 3, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): اعداد (١٣ - ١٩) مع مذکر معدود", "badge_en": "Exercise (3): Compound Numbers 13-19",
            "tamreen_title_ar": "تَأَمَّلِ الْعَدَدَ الْمُرَكَّبَ (١٣ - ١٩):", "tamreen_title_ur": "مذکر معدود کے ساتھ ۱۳ تا ۱۹ میں پہلا جزو مؤنث اور دوسرا مذکر ہوتا ہے:", "tamreen_title_en": "For 13-19 with masculine ma'dood, 1st part is feminine and 2nd part masculine:",
            "grammar_goal_ur": "۱۳ سے ۱۹ کے اعداد میں پہلا جزو معدود کے برعکس اور دوسرا موافق ہوتا ہے۔", "grammar_goal_en": "First part opposes gender of noun, second agrees.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي الْفَصْلِ [ ＿＿＿ ] طَالِباً . (15)", "prompt_ur": "طَالِباً (مذکر) کے لیے عدد ۱۵ منتخب کریں:", "prompt_en": "Select 15 for masculine 'طَالِباً':",
            "answer": "خَمْسَةَ عَشَرَ", "options": ["خَمْسَةَ عَشَرَ", "خَمْسَ عَشْرَةَ", "خَمْسَةُ عَشَرَ", "خَمْسَ عَشَرَ"],
            "emoji": "🏫", "hint_ur": "کلاس میں پندرہ طلبہ ہیں۔", "hint_en": "In the classroom there are fifteen students.",
            "explanation_ur": "درست جواب: 'خَمْسَةَ عَشَرَ' (پہلا جزو تاء کے ساتھ مؤنث اور دوسرا مذکر)",
            "explanation_en": "Correct answer: 'خَمْسَةَ عَشَرَ' (First part feminine with ta, second masculine)"
        },
        {
            "id": "b2_u3_q4", "book": 2, "unit_num": 3, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): اعداد (١١ - ٩٩) کا معدود", "badge_en": "Exercise (4): Counted Noun for 11-99",
            "tamreen_title_ar": "اضْبِطْ مَعْدُودَ الْأَعْدَادِ (١١ - ٩٩):", "tamreen_title_ur": "۱۱ سے ۹۹ کے بعد معدود کا اعراب لگائیں:", "tamreen_title_en": "Apply correct case to ma'dood after numbers 11-99:",
            "grammar_goal_ur": "۱۱ تا ۹۹ کا معدود ہمیشہ مفرد منصوب (زبر کے ساتھ) ہوتا ہے۔", "grammar_goal_en": "Counted nouns from 11 to 99 are always singular accusative (mansoob).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدِي أَرْبَعَةَ عَشَرَ [ ＿＿＿ ] .", "prompt_ur": "أَرْبَعَةَ عَشَرَ کے بعد درست معدود منتخب کریں:", "prompt_en": "Select the correct counted noun after 14:",
            "answer": "كِتَاباً", "options": ["كِتَاباً", "كِتَابٍ", "كِتَابٌ", "كُتُباً"],
            "emoji": "📚", "hint_ur": "میرے پاس چودہ کتابیں ہیں۔", "hint_en": "I have fourteen books.",
            "explanation_ur": "درست جواب: 'كِتَاباً' (۱۱ سے ۹۹ کا معدود مفرد منسوب ہوتا ہے)",
            "explanation_en": "Correct answer: 'كِتَاباً' (Counted noun for 11-99 is singular accusative)"
        },
        {
            "id": "b2_u3_q5", "book": 2, "unit_num": 3, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): عدد (١٢) مع مذکر", "badge_en": "Exercise (5): Number 12 with Masculine",
            "tamreen_title_ar": "اسْتَعْمِلِ الْعَدَدَ (١٢):", "tamreen_title_ur": "مذکر کے لیے عدد ۱۲ کی درست حالت:", "tamreen_title_en": "Select number 12 with masculine noun:",
            "grammar_goal_ur": "۱۲ کے دونوں اجزاء معدود کے موافق آتے ہیں اور رفع میں 'اثنا' آتا ہے۔", "grammar_goal_en": "Both parts of 12 agree with noun, nominative takes Ithnaa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "جَاءَ [ ＿＿＿ ] رَجُلاً . (12)", "prompt_ur": "حالتِ رفع میں عدد ۱۲ منتخب کریں:", "prompt_en": "Select 12 in the nominative case:",
            "answer": "اثْنَا عَشَرَ", "options": ["اثْنَا عَشَرَ", "اثْنَتَا عَشْرَةَ", "اثْنَيْ عَشَرَ", "اثْنَتَيْ عَشْرَةَ"],
            "emoji": "🧔", "hint_ur": "بارہ آدمی آئے۔", "hint_en": "Twelve men came.",
            "explanation_ur": "درست جواب: 'اثْنَا عَشَرَ' (مذکر رفعی حالت میں اثنا عشر آتا ہے)",
            "explanation_en": "Correct answer: 'اثْنَا عَشَرَ' (Nominative masculine 12 is Ithnaa 'ashara)"
        },
        {
            "id": "b2_u3_q6", "book": 2, "unit_num": 3, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): عدد (٢٠) الفاظِ عقود", "badge_en": "Exercise (6): Number 20 Decade Word",
            "tamreen_title_ar": "اسْتَعْمِلْ لَفْظَ الْعِقْدِ (٢٠):", "tamreen_title_ur": "۲۰ کے لیے درست کلمہ منتخب کریں:", "tamreen_title_en": "Select the correct word for 20:",
            "grammar_goal_ur": "الفاظِ عقود (۲۰ تا ۹۰) مذکر اور مؤنث دونوں کے لیے یکساں رہتے ہیں۔", "grammar_goal_en": "Decade numbers (20-90) remain identical for both genders.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي الْحَافِلَةِ [ ＿＿＿ ] رَاكِباً . (20)", "prompt_ur": "حالتِ رفع میں ۲۰ منتخب کریں:", "prompt_en": "Select 20 in the nominative case:",
            "answer": "عِشْرُونَ", "options": ["عِشْرُونَ", "عِشْرِينَ", "عَشَرَةُ", "عِشْرُونَاتٌ"],
            "emoji": "🚌", "hint_ur": "بس میں بیس مسافر ہیں۔", "hint_en": "In the bus there are twenty passengers.",
            "explanation_ur": "درست جواب: 'عِشْرُونَ' (رفع کی حالت میں واؤ کے ساتھ عشرون آتا ہے)",
            "explanation_en": "Correct answer: 'عِشْرُونَ' (Nominative form takes waw: 'ishroona)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 4: الْأَعْدَادُ التَّرْتِيبِيَّةُ (الْأَوَّلُ ، الثَّانِي...)
    # -------------------------------------------------------------
    units[4] = [
        {
            "id": "b2_u4_q1", "book": 2, "unit_num": 4, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ مکالمہ", "badge_en": "Exercise (1): Dialogue Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "مکالمے کی روشنی میں جواب دیں:", "tamreen_title_en": "Answer from the dialogue:",
            "grammar_goal_ur": "سوال و جواب کا فہم۔", "grammar_goal_en": "Comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي أَيِّ مَهْجَعٍ أَنْتُمْ؟ [ ＿＿＿ ]", "prompt_ur": "تم سب کس ہاسٹل میں ہو؟ درست جواب منتخب کریں:", "prompt_en": "In which dormitory are you? Select the correct answer:",
            "answer": "نَحْنُ فِي الْمَهْجَعِ الْخَامِسِ .", "options": ["نَحْنُ فِي الْمَهْجَعِ الْخَامِسِ .", "نَحْنُ فِي الْمَهْجَعِ الْأَوَّلِ .", "نَحْنُ فِي الْمَهْجَعِ الثَّانِي .", "نَحْنُ فِي الْفَصْلِ ."],
            "emoji": "🏢", "hint_ur": "ہم پانچویں ہاسٹل میں ہیں۔", "hint_en": "We are in the fifth dormitory.",
            "explanation_ur": "درست جواب: 'نَحْنُ فِي الْمَهْجَعِ الْخَامِسِ .'", "explanation_en": "Correct answer: 'نَحْنُ فِي الْمَهْجَعِ الْخَامِسِ .'"
        },
        {
            "id": "b2_u4_q2", "book": 2, "unit_num": 4, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): عدد ترتیبی مذکر (فَاعِل)", "badge_en": "Exercise (2): Ordinal Numbers Masculine",
            "tamreen_title_ar": "اسْتَعْمِلِ الْعَدَدَ التَّرْتِيبِيَّ:", "tamreen_title_ur": "مذکر اسم کے لیے درست عدد ترتیبی (پہلا، دوسرا، تیسرا...) منتخب کریں:", "tamreen_title_en": "Select the correct masculine ordinal number:",
            "grammar_goal_ur": "عدد ترتیبی وزن 'فَاعِل' پر موصوف کی صفت بن کر تمام اعراب میں موافق ہوتا ہے۔", "grammar_goal_en": "Ordinal numbers match their noun in gender, definiteness, and case as adjectives.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَرَأْتُ الدَّرْسَ [ ＿＿＿ ] . (4)", "prompt_ur": "چوتھے سبق کے لیے درست عدد ترتیبی منتخب کریں:", "prompt_en": "Select the 4th ordinal number for 'الدَّرْسَ':",
            "answer": "الرَّابِعَ", "options": ["الرَّابِعَ", "الْأَرْبَعَةَ", "أَرْبَعَةَ", "الرَّابِعُ"],
            "emoji": "📖", "hint_ur": "میں نے چوتھا سبق پڑھا۔", "hint_en": "I read the fourth lesson.",
            "explanation_ur": "درست جواب: 'الرَّابِعَ' (الدرس منسوب ہے اس لیے صفت بھی زبر کے ساتھ آئے گی)",
            "explanation_en": "Correct answer: 'الرَّابِعَ' (Adjective agrees in accusative case with ar-raabi'a)"
        },
        {
            "id": "b2_u4_q3", "book": 2, "unit_num": 4, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): عدد ترتیبی مؤنث", "badge_en": "Exercise (3): Ordinal Numbers Feminine",
            "tamreen_title_ar": "اسْتَعْمِلِ الْعَدَدَ التَّرْتِيبِيَّ الْمُؤَنَّثَ:", "tamreen_title_ur": "مؤنث اسم کے لیے عدد ترتیبی کی تانیث:", "tamreen_title_en": "Use feminine ordinal number with feminine nouns:",
            "grammar_goal_ur": "مؤنث اسم کے ساتھ عدد ترتیبی میں تائے تانیث آتی ہے۔", "grammar_goal_en": "Feminine nouns take feminine ordinal forms with taa marbootah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَسْكُنُ فِي الْغُرْفَةِ [ ＿＿＿ ] . (3)", "prompt_ur": "الْغُرْفَةِ کے لیے درست عدد ترتیبی منتخب کریں:", "prompt_en": "Select ordinal 3rd for feminine 'الْغُرْفَةِ':",
            "answer": "الثَّالِثَةِ", "options": ["الثَّالِثَةِ", "الثَّالِثِ", "ثَلَاثَةِ", "الثَّالِثَةُ"],
            "emoji": "🚪", "hint_ur": "میں تیسرے کمرے میں رہتا ہوں۔", "hint_en": "I live in the third room.",
            "explanation_ur": "درست جواب: 'الثَّالِثَةِ' (الغرفة مؤنث مجرور ہے)",
            "explanation_en": "Correct answer: 'الثَّالِثَةِ' (Agrees in feminine gender and genitive case)"
        },
        {
            "id": "b2_u4_q4", "book": 2, "unit_num": 4, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): پہلا اور پہلی (الْأَوَّلُ / الْأُولَى)", "badge_en": "Exercise (4): First (Al-Awwal / Al-Oolaa)",
            "tamreen_title_ar": "مَيِّزْ بَيْنَ (الْأَوَّل) وَ (الْأُولَى):", "tamreen_title_ur": "مذکر کے لیے 'الْأَوَّل' اور مؤنث کے لیے 'الْأُولَى' کا انتخاب کریں:", "tamreen_title_en": "Choose masculine 'Al-Awwal' or feminine 'Al-Oolaa':",
            "grammar_goal_ur": "پہلا کے لیے مذکر 'الْأَوَّلُ' اور مؤنث 'الْأُولَى' کا فرق۔", "grammar_goal_en": "Distinguishing masculine al-awwal from feminine al-oolaa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذِهِ هِيَ الْمَرَّةُ [ ＿＿＿ ] . (1)", "prompt_ur": "الْمَرَّةُ (مؤنث) کے لیے 'پہلی' منتخب کریں:", "prompt_en": "Select 'first' for feminine 'الْمَرَّةُ':",
            "answer": "الْأُولَى", "options": ["الْأُولَى", "الْأَوَّلُ", "الْوَاحِدَةُ", "الْأَوَّلَةُ"],
            "emoji": "🥇", "hint_ur": "یہ پہلی مرتبہ ہے۔", "hint_en": "This is the first time.",
            "explanation_ur": "درست جواب: 'الْأُولَى' (المرۃ مؤنث ہے اس لیے پہلی کے لیے الأولیٰ آئے گا)",
            "explanation_en": "Correct answer: 'الْأُولَى' (Feminine of al-awwal is al-oolaa)"
        },
        {
            "id": "b2_u4_q5", "book": 2, "unit_num": 4, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): تمییز عدد مع (كَمْ)", "badge_en": "Exercise (5): Counted Noun with Kam",
            "tamreen_title_ar": "اسْتَعْمِلِ التَّمْيِيزَ مَعَ (كَمْ):", "tamreen_title_ur": "'كَمْ' (کتنے) کے بعد درست تمییز منتخب کریں:", "tamreen_title_en": "Select the correct singular accusative noun after 'Kam':",
            "grammar_goal_ur": "'كم' استفساریہ کے بعد تمییز مفرد منصوب ہوتی ہے۔", "grammar_goal_en": "Noun following interrogative Kam is singular accusative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَمْ [ ＿＿＿ ] فِي غُرْفَتِكَ؟", "prompt_ur": "كَمْ کے بعد درست لفظ منتخب کریں:", "prompt_en": "Select the correct word after 'كَمْ':",
            "answer": "سَرِيراً", "options": ["سَرِيراً", "سَرِيرٌ", "سَرِيرٍ", "أَسِرَّةٍ"],
            "emoji": "🛏️", "hint_ur": "تمہارے کمرے میں کتنے بستر ہیں؟", "hint_en": "How many beds are in your room?",
            "explanation_ur": "درست جواب: 'سَرِيراً' (كم کے بعد اسم زبر کے ساتھ مفرد آتا ہے)",
            "explanation_en": "Correct answer: 'سَرِيراً' (Kam takes singular accusative noun)"
        },
        {
            "id": "b2_u4_q6", "book": 2, "unit_num": 4, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): عدد ترتیبی مرکب (الحادي عشر)", "badge_en": "Exercise (6): Compound Ordinal Numbers",
            "tamreen_title_ar": "اسْتَعْمِلِ الْعَدَدَ التَّرْتِيبِيَّ الْمُرَكَّبَ:", "tamreen_title_ur": "گیارھواں سبق کے لیے درست عدد ترتیبی منتخب کریں:", "tamreen_title_en": "Select the compound ordinal for 'eleventh':",
            "grammar_goal_ur": "گیارھواں کے لیے 'الْحَادِيَ عَشَرَ' کی ساخت۔", "grammar_goal_en": "Compound ordinal structure 'al-haadiya 'ashara'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَحْنُ فِي الدَّرْسِ [ ＿＿＿ ] . (11)", "prompt_ur": "گیارھویں سبق کے لیے درست کلمہ منتخب کریں:", "prompt_en": "Select 'eleventh' for 'الدَّرْسِ':",
            "answer": "الْحَادِيَ عَشَرَ", "options": ["الْحَادِيَ عَشَرَ", "الْأَحَدَ عَشَرَ", "الْحَادِي عَشْرَةَ", "الْإِحْدَى عَشَرَ"],
            "emoji": "1️⃣1️⃣", "hint_ur": "ہم گیارھویں سبق میں ہیں۔", "hint_en": "We are in the eleventh lesson.",
            "explanation_ur": "درست جواب: 'الْحَادِيَ عَشَرَ' (گیارھواں کا عدد ترتیبی)",
            "explanation_en": "Correct answer: 'الْحَادِيَ عَشَرَ' (11th ordinal is al-haadiya 'ashara)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 5: الْفِعْلُ الْمَاضِي (فَعَلَ ، فَعَلُوا ، فَعَلَتْ ، فَعَلْنَ)
    # -------------------------------------------------------------
    units[5] = [
        {
            "id": "b2_u5_q1", "book": 2, "unit_num": 5, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ مکالمہ", "badge_en": "Exercise (1): Dialogue Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے مطابق سوال کا جواب دیں:", "tamreen_title_en": "Answer from the lesson:",
            "grammar_goal_ur": "ماضی کے افعال کا فہم۔", "grammar_goal_en": "Past tense verb comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ ذَهَبَ الطُّلَّابُ بَعْدَ الدَّرْسِ؟ [ ＿＿＿ ]", "prompt_ur": "طلبہ سبق کے بعد کہاں گئے؟ درست جواب منتخب کریں:", "prompt_en": "Where did the students go after the lesson? Select the correct answer:",
            "answer": "ذَهَبُوا إِلَى الْمَلْعَبِ .", "options": ["ذَهَبُوا إِلَى الْمَلْعَبِ .", "ذَهَبُوا إِلَى الْمَطْعَمِ .", "ذَهَبُوا إِلَى السُّوقِ .", "ذَهَبُوا إِلَى بُيُوتِهِمْ ."],
            "emoji": "⚽", "hint_ur": "وہ سب کھیل کے میدان کی طرف گئے۔", "hint_en": "They went to the playground.",
            "explanation_ur": "درست جواب: 'ذَهَبُوا إِلَى الْمَلْعَبِ .'", "explanation_en": "Correct answer: 'ذَهَبُوا إِلَى الْمَلْعَبِ .'"
        },
        {
            "id": "b2_u5_q2", "book": 2, "unit_num": 5, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جمع مذکر غائب (فَعَلُوا)", "badge_en": "Exercise (2): 3rd Person Plural Masculine",
            "tamreen_title_ar": "صَرِّفِ الْفِعْلَ الْمَاضِيَ مَعَ جَمْعِ الْمُذَكَّرِ (هُمْ):", "tamreen_title_ur": "'هُمْ' (وہ سب مذکر) کے ساتھ ماضی کا صیغہ منتخب کریں:", "tamreen_title_en": "Conjugate past tense verb with 'هُمْ' (they masculine):",
            "grammar_goal_ur": "جمع مذکر غائب کے ساتھ واؤ الجماعت اور الف تفریق کا الحاق (`ذَهَبُوا`).", "grammar_goal_en": "Attaching waw al-jama'ah to form 3rd person plural masculine past verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْأَوْلَادُ [ ＿＿＿ ] إِلَى الْمَسْجِدِ . (ذَهَبَ)", "prompt_ur": "الْأَوْلَادُ کے لیے فعل ذَهَبَ کی درست شکل منتخب کریں:", "prompt_en": "Select the correct form of 'ذَهَبَ' for 'الْأَوْلَادُ':",
            "answer": "ذَهَبُوا", "options": ["ذَهَبُوا", "ذَهَبَ", "ذَهَبْنَ", "ذَهَبْتُمْ"],
            "emoji": "🕌", "hint_ur": "لڑکے مسجد کی طرف گئے۔", "hint_en": "The boys went to the mosque.",
            "explanation_ur": "درست جواب: 'ذَهَبُوا' (جمع مذکر غائب کے لیے واؤ کے ساتھ ذَهَبُوا آتا ہے)",
            "explanation_en": "Correct answer: 'ذَهَبُوا' (3rd person plural masculine takes Dhahaboo)"
        },
        {
            "id": "b2_u5_q3", "book": 2, "unit_num": 5, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مفرد مؤنث غائب (فَعَلَتْ)", "badge_en": "Exercise (3): 3rd Person Singular Feminine",
            "tamreen_title_ar": "صَرِّفِ الْفِعْلَ الْمَاضِيَ مَعَ الْمُفْرَدِ الْمُؤَنَّثِ (هِيَ):", "tamreen_title_ur": "مفرد مؤنث غائب کے ساتھ فعل ماضی کی شکل منتخب کریں:", "tamreen_title_en": "Conjugate past tense verb with feminine singular 'هِيَ':",
            "grammar_goal_ur": "ماضی میں مؤنث کے لیے تائے ساکنہ کا الحاق (`ذَهَبَتْ`).", "grammar_goal_en": "Attaching silent taa at-ta'neeth for feminine singular.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "آمِنَةُ [ ＿＿＿ ] إِلَى الْمَطْبَخِ . (دَخَلَ)", "prompt_ur": "آمِنَةُ کے لیے فعل دَخَلَ کی درست شکل منتخب کریں:", "prompt_en": "Select the correct form of 'دَخَلَ' for 'آمِنَةُ':",
            "answer": "دَخَلَتْ", "options": ["دَخَلَتْ", "دَخَلَ", "دَخَلْنَ", "دَخَلْتِ"],
            "emoji": "🍳", "hint_ur": "آمنہ باورچی خانے میں داخل ہوئی۔", "hint_en": "Amina entered the kitchen.",
            "explanation_ur": "درست جواب: 'دَخَلَتْ' (مؤنث کے لیے تائے تانیث کے ساتھ دخلت آتا ہے)",
            "explanation_en": "Correct answer: 'دَخَلَتْ' (Feminine singular takes Dakhalat)"
        },
        {
            "id": "b2_u5_q4", "book": 2, "unit_num": 5, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): جمع مؤنث غائب (فَعَلْنَ)", "badge_en": "Exercise (4): 3rd Person Plural Feminine",
            "tamreen_title_ar": "صَرِّفِ الْفِعْلَ الْمَاضِيَ مَعَ جَمْعِ الْمُؤَنَّثِ (هُنَّ):", "tamreen_title_ur": "جمع مؤنث کے ساتھ نونِ نسوہ کا الحاق کریں:", "tamreen_title_en": "Attach noon an-niswah for 3rd person plural feminine:",
            "grammar_goal_ur": "جمع مؤنث غائب کے ساتھ نون نسوہ اور لام کلمہ پر سکون (`خَرَجْنَ`).", "grammar_goal_en": "Forming 3rd person plural feminine with noon of women (Kharajna).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطَّالِبَاتُ [ ＿＿＿ ] مِنَ الْفَصْلِ . (خَرَجَ)", "prompt_ur": "الطَّالِبَاتُ کے لیے فعل خَرَجَ کی درست شکل منتخب کریں:", "prompt_en": "Select the correct form of 'خَرَجَ' for 'الطَّالِبَاتُ':",
            "answer": "خَرَجْنَ", "options": ["خَرَجْنَ", "خَرَجُوا", "خَرَجَتْ", "خَرَجْتُنَّ"],
            "emoji": "👩‍🎓", "hint_ur": "طالبات کلاس روم سے نکلیں۔", "hint_en": "The female students exited from the classroom.",
            "explanation_ur": "درست جواب: 'خَرَجْنَ' (جمع مؤنث کے لیے نونِ نسوہ کے ساتھ خَرَجْنَ آتا ہے)",
            "explanation_en": "Correct answer: 'خَرَجْنَ' (Plural feminine takes Kharajna)"
        },
        {
            "id": "b2_u5_q5", "book": 2, "unit_num": 5, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): مفعول بہ کا اعراب (نصب بالفتحة)", "badge_en": "Exercise (5): Object Accusative Case",
            "tamreen_title_ar": "اضْبِطِ الْمَفْعُولَ بِهِ بِالْفَتْحَةِ:", "tamreen_title_ur": "مفعول بہ پر درست اعراب (زبر/نصب) لگائیں:", "tamreen_title_en": "Apply accusative fathah to the direct object (Maf'ool bihi):",
            "grammar_goal_ur": "فعل و فاعل کے بعد مفعول بہ ہمیشہ منسوب (زبر والا) ہوتا ہے۔", "grammar_goal_en": "Direct objects in Arabic take the accusative case with fathah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "شَرِبَ الْوَلَدُ [ ＿＿＿ ] .", "prompt_ur": "درست اعراب والا مفعول بہ منتخب کریں:", "prompt_en": "Select the correctly voweled direct object:",
            "answer": "الْمَاءَ", "options": ["الْمَاءَ", "الْمَاءُ", "الْمَاءِ", "مَاءٌ"],
            "emoji": "🥛", "hint_ur": "لڑکے نے پانی پیا۔", "hint_en": "The boy drank water.",
            "explanation_ur": "درست جواب: 'الْمَاءَ' (مفعول بہ منسوب بالفتحۃ ہوتا ہے)",
            "explanation_en": "Correct answer: 'الْمَاءَ' (Direct object takes accusative fathah)"
        },
        {
            "id": "b2_u5_q6", "book": 2, "unit_num": 5, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): ماضی کی نفی (مَا فَعَلَ)", "badge_en": "Exercise (6): Past Tense Negation with Maa",
            "tamreen_title_ar": "انْفِ الْفِعْلَ الْمَاضِيَ بِـ (مَا):", "tamreen_title_ur": "فعل ماضی کی نفی کے لیے 'مَا' کا استعمال کریں:", "tamreen_title_en": "Negate past tense verb using 'Maa':",
            "grammar_goal_ur": "ماضی مطلق کی نفی حرفِ نفی 'مَا' کے ساتھ کی جاتی ہے۔", "grammar_goal_en": "Using negative particle 'Maa' to negate past tense verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَشَرِبْتَ الشَّايَ؟ ➔ لَا ، [ ＿＿＿ ] الشَّايَ .", "prompt_ur": "نفی کے ساتھ درست ماضی جملہ منتخب کریں:", "prompt_en": "Select the correct negative past response:",
            "answer": "مَا شَرِبْتُ", "options": ["مَا شَرِبْتُ", "لَا أَشْرَبُ", "لَمْ أَشْرَبْ", "مَا شَرِبَ"],
            "emoji": "☕", "hint_ur": "کیا تم نے چائے پی؟ نہیں، میں نے چائے نہیں پی۔", "hint_en": "Did you drink tea? No, I did not drink tea.",
            "explanation_ur": "درست جواب: 'مَا شَرِبْتُ' (ماضی کی نفی کے لیے 'ما' آتا ہے)",
            "explanation_en": "Correct answer: 'مَا شَرِبْتُ' (Maa negates past tense: Maa sharibtu)"
        }
    ]

    return units

print("Book 2 Part 1 units module written.")
