import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

# Build Book 1 complete questions
def get_b1_unit_questions(unit_num):
    # Returns a list of authentic questions for Book 1 Unit unit_num
    qs = []
    
    if unit_num == 1:
        # Unit 1: هذا (اسم الإشارة للقريب) ومَنْ هذا
        # Tamreen 1: ما هذا؟ (غير العاقل)
        t1_items = [
            ("مَا هٰذَا؟ (صورة بيت)", "هٰذَا بَيْتٌ", ["هٰذَا بَيْتٌ", "هٰذَا مَسْجِدٌ", "هٰذَا بَابٌ", "هٰذَا قَلَمٌ"], "🏠", "یہ کیا ہے؟ یہ ایک گھر ہے۔", "What is this? This is a house."),
            ("مَا هٰذَا؟ (صورة مسجد)", "هٰذَا مَسْجِدٌ", ["هٰذَا مَسْجِدٌ", "هٰذَا بَيْتٌ", "هٰذَا مَكْتَبٌ", "هٰذَا كُرْسِيٌّ"], "🕌", "یہ کیا ہے؟ یہ مسجد ہے۔", "What is this? This is a mosque."),
            ("مَا هٰذَا؟ (صورة باب)", "هٰذَا بَابٌ", ["هٰذَا بَابٌ", "هٰذَا كِتَابٌ", "هٰذَا قَلَمٌ", "هٰذَا مِفْتَاحٌ"], "🚪", "یہ کیا ہے؟ یہ دروازہ ہے۔", "What is this? This is a door."),
            ("مَا هٰذَا؟ (صورة كتاب)", "هٰذَا كِتَابٌ", ["هٰذَا كِتَابٌ", "هٰذَا دَفْتَرٌ", "هٰذَا قَلَمٌ", "هٰذَا مَكْتَبٌ"], "📖", "یہ کیا ہے؟ یہ ایک کتاب ہے۔", "What is this? This is a book."),
            ("مَا هٰذَا؟ (صورة قلم)", "هٰذَا قَلَمٌ", ["هٰذَا قَلَمٌ", "هٰذَا مِفْتَاحٌ", "هٰذَا كِتَابٌ", "هٰذَا قَمِيصٌ"], "🖊️", "یہ کیا ہے؟ یہ قلم ہے۔", "What is this? This is a pen."),
            ("مَا هٰذَا؟ (صورة مفتاح)", "هٰذَا مِفْتَاحٌ", ["هٰذَا مِفْتَاحٌ", "هٰذَا قَلَمٌ", "هٰذَا بَابٌ", "هٰذَا سَرِيرٌ"], "🔑", "یہ کیا ہے؟ یہ چابی ہے۔", "What is this? This is a key."),
            ("مَا هٰذَا؟ (صورة مكتب)", "هٰذَا مَكْتَبٌ", ["هٰذَا مَكْتَبٌ", "هٰذَا كُرْسِيٌّ", "هٰذَا سَرِيرٌ", "هٰذَا بَيْتٌ"], "🗄️", "یہ کیا ہے؟ یہ میز ہے۔", "What is this? This is a desk."),
            ("مَا هٰذَا؟ (صورة سرير)", "هٰذَا سَرِيرٌ", ["هٰذَا سَرِيرٌ", "هٰذَا كُرْسِيٌّ", "هٰذَا بَابٌ", "هٰذَا مَكْتَبٌ"], "🛏️", "یہ کیا ہے؟ یہ بستر ہے۔", "What is this? This is a bed."),
            ("مَا هٰذَا؟ (صورة كرسي)", "هٰذَا كُرْسِيٌّ", ["هٰذَا كُرْسِيٌّ", "هٰذَا سَرِيرٌ", "هٰذَا مَكْتَبٌ", "هٰذَا بَابٌ"], "🪑", "یہ کیا ہے؟ یہ کرسی ہے۔", "What is this? This is a chair."),
            ("مَا هٰذَا؟ (صورة نجم)", "هٰذَا نَجْمٌ", ["هٰذَا نَجْمٌ", "هٰذَا قَمَرٌ", "هٰذَا بَيْتٌ", "هٰذَا حَجَرٌ"], "⭐", "یہ کیا ہے؟ یہ ستارہ ہے۔", "What is this? This is a star.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t1_items, 1):
            qs.append({
                "id": f"b1_u1_q{len(qs)+1}",
                "book": 1, "unit_num": 1, "tamreen_num": 1,
                "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): مَا هٰذَا؟", "badge_en": "Exercise (1): What is this?",
                "tamreen_title_ar": "التَّمْرِينُ (1): مَا هٰذَا؟ (التَّعَرُّفُ عَلَى الْأَشْيَاءِ)",
                "tamreen_title_ur": "مشق (1): یہ کیا ہے؟ (اشیاء کی پہچان)",
                "tamreen_title_en": "Exercise (1): What is this? (Object Identification)",
                "grammar_goal_ur": "اسم اشارہ قریب 'هٰذَا' اور غیر عاقل کے لیے سوالیہ کلمہ 'مَا' کا درست استعمال۔",
                "grammar_goal_en": "Using demonstrative 'Hatha' and question particle 'Maa' for non-rational objects.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": f"مَا هٰذَا؟ [ ＿＿＿ ]", "prompt_ur": "تصویر دیکھ کر درست جملہ منتخب کریں:", "prompt_en": "Select the correct sentence for the object:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست جواب: '{ans}' (اشیاء کے لیے 'ما هذا' استعمال ہوتا ہے)",
                "explanation_en": f"Correct answer: '{ans}' ('Maa hatha' is used for non-living objects)"
            })
            
        # Tamreen 2: أهذا...؟ نعم / لا
        t2_items = [
            ("أَهٰذَا بَيْتٌ؟ (والصورة بيت)", "نَعَمْ ، هٰذَا بَيْتٌ .", ["نَعَمْ ، هٰذَا بَيْتٌ .", "لَا ، هٰذَا مَسْجِدٌ .", "نَعَمْ ، هٰذَا قَمِيصٌ .", "لَا ، هٰذَا كُرْسِيٌّ ."], "🏠", "کیا یہ گھر ہے؟ جی ہاں، یہ ایک گھر ہے۔", "Is this a house? Yes, this is a house."),
            ("أَهٰذَا قَمِيصٌ؟ (والصورة قميص)", "نَعَمْ ، هٰذَا قَمِيصٌ .", ["نَعَمْ ، هٰذَا قَمِيصٌ .", "لَا ، هٰذَا مِنْدِيلٌ .", "نَعَمْ ، هٰذَا سَرِيرٌ .", "لَا ، هٰذَا بَيْتٌ ."], "👕", "کیا یہ قمیض ہے؟ جی ہاں، یہ قمیض ہے۔", "Is this a shirt? Yes, this is a shirt."),
            ("أَهٰذَا سَرِيرٌ؟ (والصورة كرسي)", "لَا ، هٰذَا كُرْسِيٌّ .", ["لَا ، هٰذَا كُرْسِيٌّ .", "نَعَمْ ، هٰذَا سَرِيرٌ .", "لَا ، هٰذَا مَكْتَبٌ .", "نَعَمْ ، هٰذَا كُرْسِيٌّ ."], "🪑", "کیا یہ بستر ہے؟ نہیں، یہ کرسی ہے۔", "Is this a bed? No, this is a chair."),
            ("أَهٰذَا مِفْتَاحٌ؟ (والصورة قلم)", "لَا ، هٰذَا قَلَمٌ .", ["لَا ، هٰذَا قَلَمٌ .", "نَعَمْ ، هٰذَا مِفْتَاحٌ .", "لَا ، هٰذَا كِتَابٌ .", "نَعَمْ ، هٰذَا قَلَمٌ ."], "🖊️", "کیا یہ چابی ہے؟ نہیں، یہ قلم ہے۔", "Is this a key? No, this is a pen."),
            ("أَهٰذَا نَجْمٌ؟ (والصورة نجم)", "نَعَمْ ، هٰذَا نَجْمٌ .", ["نَعَمْ ، هٰذَا نَجْمٌ .", "لَا ، هٰذَا قَمَرٌ .", "نَعَمْ ، هٰذَا مَسْجِدٌ .", "لَا ، هٰذَا نَجْمٌ ."], "⭐", "کیا یہ ستارہ ہے؟ جی ہاں، یہ ستارہ ہے۔", "Is this a star? Yes, this is a star.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t2_items, 1):
            qs.append({
                "id": f"b1_u1_q{len(qs)+1}",
                "book": 1, "unit_num": 1, "tamreen_num": 2,
                "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): أَهٰذَا...؟", "badge_en": "Exercise (2): Is this...?",
                "tamreen_title_ar": "التَّمْرِينُ (2): أَهٰذَا...؟ (الْإِثْبَاتُ وَالنَّفْيُ بِـ نَعَمْ / لَا)",
                "tamreen_title_ur": "مشق (2): کیا یہ...؟ (نعم / لا کے ساتھ جواب)",
                "tamreen_title_en": "Exercise (2): Is this...? (Yes / No Answers)",
                "grammar_goal_ur": "ہمزہ استفہام 'أ' کے سوال کا جواب 'نعم' یا 'لا' سے دینا۔",
                "grammar_goal_en": "Answering interrogative hamzah with 'Na'am' (yes) or 'Laa' (no).",
                "type": "dialogue_qa", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "درست جواب منتخب کریں:", "prompt_en": "Select the correct answer:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست جواب: '{ans}'", "explanation_en": f"Correct answer: '{ans}'"
            })
            
        # Tamreen 3: مَنْ هٰذَا؟ (العاقل)
        t3_items = [
            ("مَنْ هٰذَا؟ (صورة طبيب)", "هٰذَا طَبِيبٌ .", ["هٰذَا طَبِيبٌ .", "هٰذَا مُدَرِّسٌ .", "هٰذَا طَالِبٌ .", "هٰذَا تَاجِرٌ ."], "👨‍⚕️", "یہ کون ہیں؟ یہ ڈاکٹر ہیں۔", "Who is this? This is a doctor."),
            ("مَنْ هٰذَا؟ (صورة ولد)", "هٰذَا وَلَدٌ .", ["هٰذَا وَلَدٌ .", "هٰذَا رَجُلٌ .", "هٰذَا طَالِبٌ .", "هٰذَا طَبِيبٌ ."], "👦", "یہ کون ہے؟ یہ ایک لڑکا ہے۔", "Who is this? This is a boy."),
            ("مَنْ هٰذَا؟ (صورة طالب)", "هٰذَا طَالِبٌ .", ["هٰذَا طَالِبٌ .", "هٰذَا مُدَرِّسٌ .", "هٰذَا وَلَدٌ .", "هٰذَا تَاجِرٌ ."], "👨‍🎓", "یہ کون ہے؟ یہ طالب علم ہے۔", "Who is this? This is a student."),
            ("أَهٰذَا وَلَدٌ؟ (والصورة رجل)", "لَا ، هٰذَا رَجُلٌ .", ["لَا ، هٰذَا رَجُلٌ .", "نَعَمْ ، هٰذَا وَلَدٌ .", "لَا ، هٰذَا طَالِبٌ .", "نَعَمْ ، هٰذَا رَجُلٌ ."], "🧔", "کیا یہ لڑکا ہے؟ نہیں، یہ آدمی ہے۔", "Is this a boy? No, this is a man."),
            ("مَنْ هٰذَا؟ (صورة تاجر)", "هٰذَا تَاجِرٌ .", ["هٰذَا تَاجِرٌ .", "هٰذَا طَبِيبٌ .", "هٰذَا مُدَرِّسٌ .", "هٰذَا إِمَامٌ ."], "👳", "یہ کون ہیں؟ یہ تاجر ہیں۔", "Who is this? This is a merchant."),
            ("مَنْ هٰذَا؟ (صورة مدرس)", "هٰذَا مُدَرِّسٌ .", ["هٰذَا مُدَرِّسٌ .", "هٰذَا طَالِبٌ .", "هٰذَا طَبِيبٌ .", "هٰذَا رَجُلٌ ."], "🧑‍🏫", "یہ کون ہیں؟ یہ استاد ہیں۔", "Who is this? This is a teacher.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t3_items, 1):
            qs.append({
                "id": f"b1_u1_q{len(qs)+1}",
                "book": 1, "unit_num": 1, "tamreen_num": 3,
                "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مَنْ هٰذَا؟", "badge_en": "Exercise (3): Who is this?",
                "tamreen_title_ar": "التَّمْرِينُ (3): مَنْ هٰذَا؟ (السُّؤَالُ عَنِ الْعَاقِلِ)",
                "tamreen_title_ur": "مشق (3): یہ کون ہے؟ (انسانوں/عاقل کے بارے میں سوال)",
                "tamreen_title_en": "Exercise (3): Who is this? (Asking about Persons)",
                "grammar_goal_ur": "عاقل (انسانوں) کے لیے 'مَنْ' کا استعمال سمجھنا۔",
                "grammar_goal_en": "Using question particle 'Man' (who) exclusively for rational beings.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": f"[ ＿＿＿ ] هٰذَا؟ {ans}", "prompt_ur": "درست سوالیہ کلمہ یا جواب منتخب کریں:", "prompt_en": "Select the correct particle or answer:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"عاقل یعنی انسانوں کے لیے 'مَنْ' آتا ہے۔ درست جواب: '{ans}'",
                "explanation_en": f"'Man' is used for humans. Correct answer: '{ans}'"
            })
            
        # Tamreen 4: التمييز بين ما ومن
        t4_items = [
            ("طَبِيبٌ ➔ نَسْأَلُ عَنْهُ بِـ:", "مَنْ هٰذَا؟", ["مَنْ هٰذَا؟", "مَا هٰذَا؟", "أَيْنَ هٰذَا؟", "كَيْفَ هٰذَا؟"], "👨‍⚕️", "ڈاکٹر کے متعلق پوچھیں گے: یہ کون ہیں؟", "For a doctor we ask: Who is this?"),
            ("مَسْجِدٌ ➔ نَسْأَلُ عَنْهُ بِـ:", "مَا هٰذَا؟", ["مَا هٰذَا؟", "مَنْ هٰذَا؟", "كَمْ هٰذَا؟", "مَتَى هٰذَا؟"], "🕌", "مسجد کے متعلق پوچھیں گے: یہ کیا ہے؟", "For a mosque we ask: What is this?"),
            ("طَالِبٌ ➔ نَسْأَلُ عَنْهُ بِـ:", "مَنْ هٰذَا؟", ["مَنْ هٰذَا؟", "مَا هٰذَا؟", "مَا ذٰلِكَ؟", "كَيْفَ هٰذَا؟"], "👨‍🎓", "طالب علم کے متعلق پوچھیں گے: یہ کون ہے؟", "For a student we ask: Who is this?"),
            ("قَلَمٌ ➔ نَسْأَلُ عَنْهُ بِـ:", "مَا هٰذَا؟", ["مَا هٰذَا؟", "مَنْ هٰذَا؟", "مَنْ ذٰلِكَ؟", "أَيْنَ هٰذَا؟"], "🖊️", "قلم کے متعلق پوچھیں گے: یہ کیا ہے؟", "For a pen we ask: What is this?")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t4_items, 1):
            qs.append({
                "id": f"b1_u1_q{len(qs)+1}",
                "book": 1, "unit_num": 1, "tamreen_num": 4,
                "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): مَا بمقابلہ مَنْ", "badge_en": "Exercise (4): 'Maa' vs 'Man'",
                "tamreen_title_ar": "التَّمْرِينُ (4): التَّمْيِيزُ بَيْنَ (مَا) وَ (مَنْ)",
                "tamreen_title_ur": "مشق (4): 'ما' اور 'من' کے درمیان فرق",
                "tamreen_title_en": "Exercise (4): Distinguishing 'Maa' vs 'Man'",
                "grammar_goal_ur": "عاقل کے لیے 'مَنْ' اور غیر عاقل کے لیے 'مَا' کا امتیاز۔",
                "grammar_goal_en": "Distinguishing 'Maa' (what) for non-rational vs 'Man' (who) for rational beings.",
                "type": "meaning_choice", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "درست سوالیہ جملہ منتخب کریں:", "prompt_en": "Select the correct interrogative question:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست سوال: '{ans}'", "explanation_en": f"Correct question: '{ans}'"
            })
            
    elif unit_num == 2:
        # Unit 2: ذٰلِكَ
        # Tamreen 1: ما ذلك؟
        t1_items = [
            ("مَا ذٰلِكَ؟ (صورة نجم بعيد)", "ذٰلِكَ نَجْمٌ .", ["ذٰلِكَ نَجْمٌ .", "هٰذَا نَجْمٌ .", "ذٰلِكَ قَمَرٌ .", "تِلْكَ نَجْمٌ ."], "⭐", "وہ ایک ستارہ ہے۔", "That is a star."),
            ("مَا ذٰلِكَ؟ (صورة بيت بعيد)", "ذٰلِكَ بَيْتٌ .", ["ذٰلِكَ بَيْتٌ .", "هٰذَا بَيْتٌ .", "ذٰلِكَ مَسْجِدٌ .", "ذٰلِكَ حَجَرٌ ."], "🏠", "وہ ایک گھر ہے۔", "That is a house."),
            ("مَا ذٰلِكَ؟ (صورة سرير بعيد)", "ذٰلِكَ سَرِيرٌ .", ["ذٰلِكَ سَرِيرٌ .", "هٰذَا سَرِيرٌ .", "ذٰلِكَ كُرْسِيٌّ .", "ذٰلِكَ مَكْتَبٌ ."], "🛏️", "وہ ایک بستر ہے۔", "That is a bed."),
            ("مَا ذٰلِكَ؟ (صورة حجر)", "ذٰلِكَ حَجَرٌ .", ["ذٰلِكَ حَجَرٌ .", "هٰذَا حَجَرٌ .", "ذٰلِكَ جَبَلٌ .", "ذٰلِكَ بَيْتٌ ."], "⛰️", "وہ ایک پتھر ہے۔", "That is a stone.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t1_items, 1):
            qs.append({
                "id": f"b1_u2_q{len(qs)+1}",
                "book": 1, "unit_num": 2, "tamreen_num": 1,
                "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): مَا ذٰلِكَ؟", "badge_en": "Exercise (1): What is that?",
                "tamreen_title_ar": "التَّمْرِينُ (1): مَا ذٰلِكَ؟ (اسْمُ الْإِشَارَةِ لِلْبَعِيدِ)",
                "tamreen_title_ur": "مشق (1): وہ کیا ہے؟ (اسم اشارہ برائے بعید)",
                "tamreen_title_en": "Exercise (1): What is that? (Distant Demonstrative)",
                "grammar_goal_ur": "دور کی مذکر اشیاء کے لیے 'ذٰلِكَ' کا درست استعمال۔",
                "grammar_goal_en": "Using distant masculine demonstrative 'Dhaalika' for distant objects.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": f"مَا ذٰلِكَ؟ [ ＿＿＿ ]", "prompt_ur": "درست جملہ منتخب کریں:", "prompt_en": "Select the correct sentence:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست جواب: '{ans}'", "explanation_en": f"Correct answer: '{ans}'"
            })
            
        # Tamreen 2: من ذلك؟
        t2_items = [
            ("مَنْ ذٰلِكَ؟ (صورة إمام)", "ذٰلِكَ إِمَامٌ .", ["ذٰلِكَ إِمَامٌ .", "هٰذَا إِمَامٌ .", "ذٰلِكَ مُدَرِّسٌ .", "ذٰلِكَ طَالِبٌ ."], "👳", "وہ ایک امام ہیں۔", "That is an Imam."),
            ("مَنْ هٰذَا وَمَنْ ذٰلِكَ؟", "هٰذَا مُدَرِّسٌ وَذٰلِكَ إِمَامٌ .", ["هٰذَا مُدَرِّسٌ وَذٰلِكَ إِمَامٌ .", "ذٰلِكَ مُدَرِّسٌ وَهٰذَا إِمَامٌ .", "هٰذَا طَالِبٌ وَذٰلِكَ تَاجِرٌ .", "هٰذَا إِمَامٌ وَذٰلِكَ مُدَرِّسٌ ."], "🧑‍🏫", "یہ استاد ہیں اور وہ امام ہیں۔", "This is a teacher and that is an Imam.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t2_items, 1):
            qs.append({
                "id": f"b1_u2_q{len(qs)+1}",
                "book": 1, "unit_num": 2, "tamreen_num": 2,
                "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مَنْ ذٰلِكَ؟", "badge_en": "Exercise (2): Who is that?",
                "tamreen_title_ar": "التَّمْرِينُ (2): مَنْ ذٰلِكَ؟ (الْعَاقِلُ لِلْبَعِيدِ)",
                "tamreen_title_ur": "مشق (2): وہ کون ہے؟ (دور کے انسانوں کا تعارف)",
                "tamreen_title_en": "Exercise (2): Who is that? (Distant Persons)",
                "grammar_goal_ur": "دور کے عاقل (انسانوں) کے لیے 'مَنْ ذٰلِكَ' کا استعمال۔",
                "grammar_goal_en": "Using 'Man dhaalika' for distant rational beings.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "درست جواب منتخب کریں:", "prompt_en": "Select the correct answer:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست جواب: '{ans}'", "explanation_en": f"Correct answer: '{ans}'"
            })
            
        # Tamreen 3: هذا للقريب وذلك للبعيد
        t3_items = [
            ("هٰذَا مَسْجِدٌ وَ [ ＿＿＿ ] بَيْتٌ .", "ذٰلِكَ", ["ذٰلِكَ", "هٰذَا", "هٰذِهِ", "تِلْكَ"], "🕌", "یہ مسجد ہے اور وہ گھر ہے۔", "This is a mosque and that is a house."),
            ("هٰذَا سُكَّرٌ وَ [ ＿＿＿ ] لَبَنٌ .", "ذٰلِكَ", ["ذٰلِكَ", "هٰذَا", "هِيَ", "هُوَ"], "🍬", "یہ چینی ہے اور وہ دودھ ہے۔", "This is sugar and that is milk."),
            ("أَذٰلِكَ كَلْبٌ؟ (والصورة قط)", "لَا ، ذٰلِكَ قِطٌّ .", ["لَا ، ذٰلِكَ قِطٌّ .", "نَعَمْ ، ذٰلِكَ كَلْبٌ .", "لَا ، هٰذَا كَلْبٌ .", "نَعَمْ ، هٰذَا قِطٌّ ."], "🐈", "کیا وہ کتا ہے؟ نہیں، وہ بلی ہے۔", "Is that a dog? No, that is a cat.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t3_items, 1):
            qs.append({
                "id": f"b1_u2_q{len(qs)+1}",
                "book": 1, "unit_num": 2, "tamreen_num": 3,
                "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): هٰذَا بمقابلہ ذٰلِكَ", "badge_en": "Exercise (3): Near vs Far",
                "tamreen_title_ar": "التَّمْرِينُ (3): الْمُقَارَنَةُ بَيْنَ (هٰذَا) لِلْقَرِيبِ وَ (ذٰلِكَ) لِلْبَعِيدِ",
                "tamreen_title_ur": "مشق (3): قریب (هذا) اور دور (ذلك) کا موازنہ",
                "tamreen_title_en": "Exercise (3): Comparing Near (Hatha) vs Far (Dhalika)",
                "grammar_goal_ur": "قریب اور بعید کے اشاروں میں امتیاز کرنا۔",
                "grammar_goal_en": "Distinguishing near demonstrative 'Hatha' from distant 'Dhalika'.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "خالی جگہ پر کریں:", "prompt_en": "Fill in the blank:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست جواب: '{ans}'", "explanation_en": f"Correct answer: '{ans}'"
            })
            
    elif unit_num == 3:
        # Unit 3: المعرفة والنكرة (أل والتنوين) وحروف الشمس والقمر
        # Tamreen 1 (User requested Tamreen 6): تنوين بمقابلہ ضمة واحدة مع أل
        t6_items = [
            ("اخْتَرْ الصَّحِيحَ عِنْدَ دُخُولِ (أَلْ) عَلَى (بَيْتٌ):", "الْبَيْتُ", ["الْبَيْتُ", "الْبَيْتٌ", "بَيْتُ", "بَيْتٌ"], "🏠", "ال بیت (ایک پیش کے ساتھ)", "The house (single damma)"),
            ("اخْتَرْ الصَّحِيحَ لِلِاسْمِ النَّكِرَةِ (بِدُونِ أَلْ):", "كِتَابٌ", ["كِتَابٌ", "كِتَابُ", "الْكِتَابٌ", "الْكِتَابُ"], "📖", "کتاب (دو پیش / تنوین کے ساتھ)", "A book (tanween)"),
            ("اخْتَرْ الضَّبْطَ الصَّحِيحَ:", "الْقَلَمُ مَكْسُورٌ", ["الْقَلَمُ مَكْسُورٌ", "الْقَلَمٌ مَكْسُورٌ", "الْقَلَمُ مَكْسُورُ", "قَلَمُ مَكْسُورٌ"], "🖊️", "قلم ٹوٹا ہوا ہے", "The pen is broken"),
            ("اخْتَرْ الضَّبْطَ الصَّحِيحَ:", "الْمَسْجِدُ قَرِيبٌ", ["الْمَسْجِدُ قَرِيبٌ", "الْمَسْجِدٌ قَرِيبٌ", "مَسْجِدُ قَرِيبٌ", "الْمَسْجِدُ قَرِيبُ"], "🕌", "مسجد قریب ہے", "The mosque is near")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t6_items, 1):
            qs.append({
                "id": f"b1_u3_q{len(qs)+1}",
                "book": 1, "unit_num": 3, "tamreen_num": 1,
                "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): أَلْ اور تنوین کا فرق", "badge_en": "Exercise (1): Al- vs Tanween",
                "tamreen_title_ar": "التَّمْرِينُ (1): اخْتِيَارُ الْكَلِمَاتِ مَعَ (أَلْ) وَبِدُونِهَا (ضَمَّةٌ وَاحِدَةٌ أَمْ تَنْوِينٌ)",
                "tamreen_title_ur": "مشق (1): الف لام اور بغیر الف لام میں ایک پیش اور دو پیش کی پہچان",
                "tamreen_title_en": "Exercise (1): Words with and without 'Al-' (Single Damma vs Tanween)",
                "grammar_goal_ur": "الف لام داخل ہونے پر تنوین ختم ہو کر صرف ایک پیش (ضمة) رہ جاتی ہے۔ 'ال' اور تنوین کبھی اکٹھے نہیں آتے۔",
                "grammar_goal_en": "A noun with 'Al-' takes a single damma, never tanween. 'Al-' and tanween are mutually exclusive.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "اعراب کے اصول کے مطابق درست کلمہ چنیں:", "prompt_en": "Select the word with correct voweling:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": "جب لفظ پر 'ال' آتا ہے تو تنوین ہٹ جاتی ہے اور صرف ایک پیش آتی ہے، جیسے: 'الْبَيْتُ'۔",
                "explanation_en": "When 'Al-' is prefixed, tanween drops and only a single damma remains: 'al-Baytu'."
            })

        # Tamreen 2 (User requested Tamreen 7): ترجمہ کے مطابق درست آپشن منتخب کرنا
        t7_items = [
            ("وہ ستارہ دور ہے۔ (اختر الترجمة الصحيحة):", "النَّجْمُ بَعِيدٌ .", ["النَّجْمُ بَعِيدٌ .", "نَجْمٌ بَعِيدٌ .", "النَّجْمٌ بَعِيدُ .", "نَجْمُ بَعِيدٌ ."], "⭐", "ستارہ دور ہے۔", "The star is far away."),
            ("پانی ٹھنڈا ہے۔ (The water is cold):", "الْمَاءُ بَارِدٌ .", ["الْمَاءُ بَارِدٌ .", "مَاءٌ بَارِدٌ .", "الْمَاءٌ بَارِدٌ .", "الْمَاءُ بَارِدُ ."], "💧", "پانی ٹھنڈا ہے۔", "The water is cold."),
            ("دودھ گرم ہے۔ (The milk is hot):", "اللَّبَنُ حَارٌّ .", ["اللَّبَنُ حَارٌّ .", "لَبَنٌ حَارٌّ .", "اللَّبَنٌ حَارٌّ .", "اللَّبَنُ حَارُّ ."], "🥛", "دودھ گرم ہے۔", "The milk is hot.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t7_items, 1):
            qs.append({
                "id": f"b1_u3_q{len(qs)+1}",
                "book": 1, "unit_num": 3, "tamreen_num": 2,
                "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): معرفہ جملے کا ترجمہ", "badge_en": "Exercise (2): Definite Sentence Translation",
                "tamreen_title_ar": "التَّمْرِينُ (2): اخْتِيَارُ الْجُمْلَةِ الصَّحِيحَةِ لِلتَّرْجَمَةِ (مَعْرِفَةٌ أَمْ نَكِرَةٌ)",
                "tamreen_title_ur": "مشق (2): اردو/انگریزی ترجمہ کے مطابق درست عربی جملہ چننا",
                "tamreen_title_en": "Exercise (2): Matching Translation with Correct Arabic Options",
                "grammar_goal_ur": "مبتدا معرفہ (ال کے ساتھ) اور خبر نکرہ (تنوین کے ساتھ) ہوتی ہے۔",
                "grammar_goal_en": "Subject is definite (with Al-) and predicate is indefinite (with tanween).",
                "type": "meaning_choice", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "درست عربی جملہ منتخب کریں:", "prompt_en": "Select the correct Arabic sentence:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست جواب: '{ans}' (مبتدا پر ال اور ایک پیش، خبر پر تنوین)",
                "explanation_en": f"Correct answer: '{ans}' (Subject has 'Al-', predicate has tanween)"
            })

        # Tamreen 3 (User requested Tamreen 8): امْلَأ الفراغ بوضع الكلمة المناسبة
        t8_items = [
            ("الْحَجَرُ [ ＿＿＿ ] .", "ثَقِيلٌ", ["ثَقِيلٌ", "خَفِيفٌ", "مَفْتُوحٌ", "وَسِخٌ"], "⛰️", "پتھر بھاری ہے۔", "The stone is heavy."),
            ("الْبَابُ [ ＿＿＿ ] .", "مَفْتُوحٌ", ["مَفْتوحٌ", "مَكْسُورٌ", "حَارٌّ", "ثَقِيلٌ"], "🚪", "دروازہ کھلا ہے۔", "The door is open."),
            ("الْقَمَرُ [ ＿＿＿ ] .", "جَمِيلٌ", ["جَمِيلٌ", "وَسِخٌ", "حَارٌّ", "مَكْسُورٌ"], "🌙", "چاند خوبصورت ہے۔", "The moon is beautiful."),
            ("الْوَرَقُ [ ＿＿＿ ] .", "خَفِيفٌ", ["خَفِيفٌ", "ثَقِيلٌ", "حَارٌّ", "وَسِخٌ"], "📄", "ورق ہلکا ہے۔", "The paper is light."),
            ("الْمِنْدِيلُ [ ＿＿＿ ] .", "وَسِخٌ", ["وَسِخٌ", "نَظِيفٌ", "حَارٌّ", "ثَقِيلٌ"], "🧣", "رومال میلا ہے۔", "The handkerchief is dirty."),
            ("اللَّبَنُ [ ＿＿＿ ] .", "حَارٌّ", ["حَارٌّ", "مَفْتُوحٌ", "مَكْسُورٌ", "خَفِيفٌ"], "🥛", "دودھ گرم ہے۔", "The milk is hot.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t8_items, 1):
            qs.append({
                "id": f"b1_u3_q{len(qs)+1}",
                "book": 1, "unit_num": 3, "tamreen_num": 3,
                "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مناسب خبر سے خالی جگہ", "badge_en": "Exercise (3): Fill Blank with Predicate",
                "tamreen_title_ar": "التَّمْرِينُ (3): امْلَأِ الْفَرَاغَ بِوَضْعِ الْكَلِمَةِ الْمُنَاسِبَةِ مِنَ الْقَائِمَةِ",
                "tamreen_title_ur": "مشق (3): دیے گئے الفاظ میں سے مناسب خبر چن کر خالی جگہ پر کریں",
                "tamreen_title_en": "Exercise (3): Fill Blanks with Suitable Predicate from List",
                "grammar_goal_ur": "مبتدا کے مفہوم کے مطابق درست صفت/خبر کا انتخاب۔",
                "grammar_goal_en": "Selecting contextually and grammatically appropriate predicate for the subject.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "دیے گئے الفاظ میں سے مناسب کلمہ چنیں:", "prompt_en": "Select the fitting word for the blank:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست جواب: '{ans}'", "explanation_en": f"Correct answer: '{ans}'"
            })

        # Tamreen 4 (User requested Tamreen 9): امْلَأ الفراغ بوضع مبتدأ مناسب
        t9_items = [
            ("[ ＿＿＿ ] نَظِيفٌ .", "الْمِنْدِيلُ", ["الْمِنْدِيلُ", "الْقَمَرُ", "الْحَجَرُ", "الْمَاءُ"], "🧣", "رومال صاف ہے۔", "The handkerchief is clean."),
            ("[ ＿＿＿ ] مَكْسُورٌ .", "الْقَلَمُ", ["الْقَلَمُ", "الْمَاءُ", "اللَّبَنُ", "الشَّمْسُ"], "🖊️", "قلم ٹوٹا ہوا ہے۔", "The pen is broken."),
            ("[ ＿＿＿ ] بَارِدٌ .", "الْمَاءُ", ["الْمَاءُ", "النَّارُ", "الشَّمْسُ", "الْقَلَمُ"], "💧", "پانی ٹھنڈا ہے۔", "The water is cold."),
            ("[ ＿＿＿ ] قَرِيبٌ .", "الْمَسْجِدُ", ["الْمَسْجِدُ", "النَّجْمُ", "الْقَمَرُ", "السَّمَاءُ"], "🕌", "مسجد قریب ہے۔", "The mosque is near."),
            ("[ ＿＿＿ ] بَعِيدٌ .", "الْقَمَرُ", ["الْقَمَرُ", "الْبَابُ", "الْمَكْتَبُ", "الْكُرْسِيُّ"], "🌙", "چاند دور ہے۔", "The moon is far.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t9_items, 1):
            qs.append({
                "id": f"b1_u3_q{len(qs)+1}",
                "book": 1, "unit_num": 3, "tamreen_num": 4,
                "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): مناسب مبتدا سے خالی جگہ", "badge_en": "Exercise (4): Fill Blank with Subject",
                "tamreen_title_ar": "التَّمْرِينُ (4): امْلَأِ الْفَرَاغَ بِوَضْعِ كَلِمَةٍ مُنَاسِبَةٍ (مُبْتَدَأٌ)",
                "tamreen_title_ur": "مشق (4): مناسب مبتدا لگا کر جملہ مکمل کریں",
                "tamreen_title_en": "Exercise (4): Fill Blanks by Choosing Suitable Subject",
                "grammar_goal_ur": "خبر کے مطابق صحیح مبتدا لگانا جو ال کے ساتھ معرفہ ہو۔",
                "grammar_goal_en": "Choosing a definite subject that agrees with the predicate.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "مناسب مبتدا منتخب کریں:", "prompt_en": "Select the appropriate subject:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست مبتدا: '{ans}'", "explanation_en": f"Correct subject: '{ans}'"
            })

        # Tamreen 5 (User requested Tamreen 11): امْلَأ الفراغ بوضع كلمة مناسبة
        t11_items = [
            ("التَّاجِرُ [ ＿＿＿ ] .", "غَنِيٌّ", ["غَنِيٌّ", "حُلْوٌ", "مَكْسُورٌ", "بَارِدٌ"], "👳", "تاجر مالدار ہے۔", "The merchant is rich."),
            ("السُّكَّرُ [ ＿＿＿ ] .", "حُلْوٌ", ["حُلْوٌ", "مَرِيضٌ", "طَوِيلٌ", "قَصِيرٌ"], "🍬", "چینی میٹھی ہے۔", "The sugar is sweet."),
            ("الطَّالِبُ [ ＿＿＿ ] .", "مَرِيضٌ", ["مَرِيضٌ", "حُلْوٌ", "لَذِيذٌ", "مَفْتُوحٌ"], "👨‍🎓", "طالب علم بیمار ہے۔", "The student is sick."),
            ("التُّفَّاحُ [ ＿＿＿ ] .", "لَذِيذٌ", ["لَذِيذٌ", "غَنِيٌّ", "طَوِيلٌ", "مَكْسُورٌ"], "🍎", "سیب لذیذ ہے۔", "The apple is delicious."),
            ("الطَّبِيبُ طَوِيلٌ وَالْمَرِيضُ [ ＿＿＿ ] .", "قَصِيرٌ", ["قَصِيرٌ", "حُلْوٌ", "لَذِيذٌ", "غَنِيٌّ"], "👨‍⚕️", "ڈاکٹر لمبا ہے اور مریض پستہ قد ہے۔", "The doctor is tall and patient is short.")
        ]
        for idx, (p, ans, opts, em, ur, en) in enumerate(t11_items, 1):
            qs.append({
                "id": f"b1_u3_q{len(qs)+1}",
                "book": 1, "unit_num": 3, "tamreen_num": 5,
                "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): مناسب صفت سے خالی جگہ", "badge_en": "Exercise (5): Fill Blank with Predicate",
                "tamreen_title_ar": "التَّمْرِينُ (5): امْلَأِ الْفَرَاغَ بِوَضْعِ كَلِمَةٍ مُنَاسِبَةٍ (الصِّفَاتُ)",
                "tamreen_title_ur": "مشق (5): مناسب صفت لگا کر خالی جگہ پر کریں",
                "tamreen_title_en": "Exercise (5): Fill Blanks with Fitting Adjectival Predicates",
                "grammar_goal_ur": "الفاظ: غني، حلو، مريض، لذيذ، طويل، قصير کا بامعنی استعمال۔",
                "grammar_goal_en": "Meaningful usage of descriptive predicates.",
                "type": "fill_blank", "strict_tashkeel": True,
                "prompt_ar": p, "prompt_ur": "خالی جگہ کے لیے درست کلمہ چنیں:", "prompt_en": "Select the fitting word for the blank:",
                "answer": ans, "options": opts, "emoji": em,
                "hint_ur": ur, "hint_en": en,
                "explanation_ur": f"درست جواب: '{ans}'", "explanation_en": f"Correct answer: '{ans}'"
            })

        # Tamreen 6 (User requested Tamreen 12): التوصيل بين القائمة أ والقائمة ب
        qs.append({
            "id": f"b1_u3_q{len(qs)+1}",
            "book": 1, "unit_num": 3, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): کالم ملائیں", "badge_en": "Exercise (6): Match Columns",
            "tamreen_title_ar": "التَّمْرِينُ (6): صِلْ بَيْنَ الْقَائِمَةِ (أ) وَالْقَائِمَةِ (ب)",
            "tamreen_title_ur": "مشق (6): کتاب کے مطابق کالم (أ) اور کالم (ب) کو باہم ملائیں",
            "tamreen_title_en": "Exercise (6): Match Column (A) with Column (B) as in Book",
            "grammar_goal_ur": "مبتدا اور اس کے مناسب خبر کو باہم جوڑ کر مکمل جملہ اسمیہ بنانا۔",
            "grammar_goal_en": "Connecting each subject with its corresponding predicate to form complete sentences.",
            "type": "pair_match", "strict_tashkeel": True,
            "prompt_ar": "اخْتَرْ كَلِمَةً مِنَ الْقَائِمَةِ (ب) تُنَاسِبُ الْكَلِمَةَ الَّتِي فِي الْقَائِمَةِ (أ):",
            "prompt_ur": "کالم (أ) کے لفظ پر کلک کریں پھر کالم (ب) کے مناسب لفظ پر کلک کریں:",
            "prompt_en": "Click a word in Column A, then click its matching predicate in Column B:",
            "answer": "matched",
            "pairs": [
                {"left": "الطَّالِبُ", "right": "مَرِيضٌ"},
                {"left": "الدُّكَّانُ", "right": "مَفْتُوحٌ"},
                {"left": "التُّفَّاحُ", "right": "لَذِيذٌ"},
                {"left": "الْمَاءُ", "right": "حَارٌّ"},
                {"left": "الْحَجَرُ", "right": "ثَقِيلٌ"},
                {"left": "الْقَلَمُ", "right": "مَكْسُورٌ"}
            ],
            "options": [], "emoji": "📋",
            "hint_ur": "کالم الف اور ب کے درست جوڑے بنائیں", "hint_en": "Match Column A with Column B",
            "explanation_ur": "الطلب مريض، الدكان مفتوح، التفاح لذيذ، الماء حار، الحجر ثقيل، القلم مكسور",
            "explanation_en": "Matched pairs forming meaningful nominative sentences."
        })

    return qs

print("Book 1 Unit 1-3 test generator defined successfully!")
for u in [1, 2, 3]:
    q_list = get_b1_unit_questions(u)
    print(f"Unit {u}: {len(q_list)} questions generated")
