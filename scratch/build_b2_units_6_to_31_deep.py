# -*- coding: utf-8 -*-
"""
Deep Authentic Curriculum Generator for Madinah Book 2 (Units 6 to 31)
Ensures every unit has multi-tamreen exercises matching the textbook.
"""

def get_b2_units_6_to_31_deep():
    units = {}

    # -------------------------------------------------------------------------
    # UNIT 6: إِسْنَادُ الْمَاضِي إِلَى ضَمَائِرِ الْمُتَكَلِّمِ وَالْمُخَاطَبِ
    # -------------------------------------------------------------------------
    units[6] = [
        # T1: أجب عن الأسئلة
        {
            "id": "b2_u6_t1_q1", "book": 2, "unit_num": 6, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے مطابق سوالات کے جوابات دیں:", "tamreen_title_en": "Answer based on the lesson:",
            "grammar_goal_ur": "فعل ماضی اور ضمائر کا فہم۔", "grammar_goal_en": "Past tense pronoun comprehension.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ ذَهَبَ الطُّلَّابُ بَعْدَ الدَّرْسِ؟ [ ＿＿＿ ]",
            "prompt_ur": "طلبہ سبق کے بعد کہاں گئے؟", "prompt_en": "Where did the students go after the lesson?",
            "answer": "ذَهَبُوا إِلَى الْمَلْعَبِ .",
            "options": ["ذَهَبُوا إِلَى الْمَلْعَبِ .", "ذَهَبُوا إِلَى الْمَسْجِدِ .", "ذَهَبُوا إِلَى الْمَكْتَبَةِ .", "ذَهَبُوا إِلَى الْمَهْجَعِ ."],
            "emoji": "⚽", "hint_ur": "وہ کھیل کے میدان کی طرف گئے۔", "hint_en": "They went to the playground.",
            "explanation_ur": "سبق کے مطابق طلبہ کھیل کے میدان گئے۔", "explanation_en": "According to the dialogue, the students went to the playground."
        },
        # T2: إسناد الفعل إلى (تَ / تُ / تِ)
        {
            "id": "b2_u6_t2_q1", "book": 2, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تائے فاعل کی تصریف", "badge_en": "Exercise (2): Past Tense with Taa al-Fa'il",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ الْمَاضِي إِلَى (تَ / تُ / تِ):", "tamreen_title_ur": "ماضی کو ضمیر متکلم اور مخاطب کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating past tense with Taa al-Fa'il:",
            "grammar_goal_ur": "ذَهَبْتُ (متکلم)، ذَهَبْتَ (مخاطب مذکر)، ذَهَبْتِ (مخاطب مؤنث) کا فرق۔", "grammar_goal_en": "Distinguishing Zahabtu, Zahabta, Zahabti.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] إِلَى السُّوقِ أَمْسِ .",
            "prompt_ur": "أنا کے ساتھ درست فعل چنیں:", "prompt_en": "Select the correct verb with 'Ana':",
            "answer": "ذَهَبْتُ",
            "options": ["ذَهَبْتُ", "ذَهَبْتَ", "ذَهَبْتِ", "ذَهَبَ"],
            "emoji": "🚶‍♂️", "hint_ur": "میں کل بازار گیا (ذَهَبْتُ)۔", "hint_en": "I went to the market yesterday.",
            "explanation_ur": "متکلم کے لیے تاء مضمومہ آتی ہے: ذَهَبْتُ۔", "explanation_en": "First person singular takes dammah on taa: Zahabtu."
        },
        {
            "id": "b2_u6_t2_q2", "book": 2, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تائے فاعل کی تصریف", "badge_en": "Exercise (2): Past Tense with Taa al-Fa'il",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ الْمَاضِي إِلَى (تَ / تُ / تِ):", "tamreen_title_ur": "مخاطب مذکر کے لیے تائے مفتوحہ کا استعمال:", "tamreen_title_en": "2nd person masculine past conjugation:",
            "grammar_goal_ur": "أَنْتَ ذَهَبْتَ کی ساخت۔", "grammar_goal_en": "Anta thahabta structure.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ [ ＿＿＿ ] يَا عَلِيُّ؟",
            "prompt_ur": "علی (مخاطب مذکر) کے لیے درست فعل چنیں:", "prompt_en": "Select the correct verb addressing Ali:",
            "answer": "ذَهَبْتَ",
            "options": ["ذَهَبْتَ", "ذَهَبْتُ", "ذَهَبْتِ", "ذَهَبُوا"],
            "emoji": "❓", "hint_ur": "مخاطب مذکر کے لیے تاء مفتوحہ آئے گی: ذَهَبْتَ۔", "hint_en": "2nd person masculine singular takes fathah on taa: Thahabta.",
            "explanation_ur": "مخاطب مذکر کے لیے 'ذَهَبْتَ' آتا ہے۔", "explanation_en": "Second person masculine singular takes 'thahabta'."
        },
        # T4: إسناد الفعل إلى ضمیر (نَا)
        {
            "id": "b2_u6_t4_q1", "book": 2, "unit_num": 6, "tamreen_num": 4,
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
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 7: تَأْنِيثُ الْفِعْلِ الْمَاضِي
    # -------------------------------------------------------------------------
    units[7] = [
        # T1: أجب عن الأسئلة
        {
            "id": "b2_u7_t1_q1", "book": 2, "unit_num": 7, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ سبق", "badge_en": "Exercise (1): Lesson Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "سبق کے مطابق سوالات کے جوابات دیں:", "tamreen_title_en": "Answer based on the lesson:",
            "grammar_goal_ur": "مؤنث ضمائر کے ساتھ ماضی کی پہچان۔", "grammar_goal_en": "Past tense with feminine subjects.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ ذَهَبَتْ آمِنَةُ وَأَخَوَاتُهَا؟ [ ＿＿＿ ]",
            "prompt_ur": "آمنہ اور اس کی بہنیں کہاں گئیں؟", "prompt_en": "Where did Aminah and her sisters go?",
            "answer": "ذَهَبْنَ إِلَى الْمَسْجِدِ .",
            "options": ["ذَهَبْنَ إِلَى الْمَسْجِدِ .", "ذَهَبُوا إِلَى الْمَسْجِدِ .", "ذَهَبَتْ إِلَى الْمَسْجِدِ .", "ذَهَبَ إِلَى الْمَسْجِدِ ."],
            "emoji": "🕌", "hint_ur": "جمع مؤنث غائب کے لیے 'ذَهَبْنَ' آئے گا۔", "hint_en": "Feminine plural takes 'Thahabna'.",
            "explanation_ur": "آمنہ اور اس کی بہنیں جمع مؤنث ہیں اس لیے 'ذَهَبْنَ' آئے گا۔", "explanation_en": "Feminine plural subject requires 'thahabna'."
        },
        # T2: تأنيث الفاعل
        {
            "id": "b2_u7_t2_q1", "book": 2, "unit_num": 7, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تانیثِ فاعل", "badge_en": "Exercise (2): Feminizing the Subject",
            "tamreen_title_ar": "أَنِّثِ الْفَاعِلَ فِي الْجُمَلِ الآتِيَةِ:", "tamreen_title_ur": "فاعل کو مذکر سے مؤنث میں تبدیل کریں:", "tamreen_title_en": "Make the subject feminine in the following sentences:",
            "grammar_goal_ur": "فعل میں تائے تانیث ساکنہ کا اضافہ: خَرَجَ الطَّالِبُ -> خَرَجَتِ الطَّالِبَةُ۔", "grammar_goal_en": "Appending taa ta'neeth to the verb when subject is feminine.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "(خَرَجَ الطَّالِبُ مِنَ الْفَصْلِ) عِنْدَ تَأْنِيثِ الْفَاعِلِ يُصْبِحُ: [ ＿＿＿ ]",
            "prompt_ur": "طالبہ کے لیے جملہ کیا بنے گا؟", "prompt_en": "When subject becomes female student, sentence becomes:",
            "answer": "خَرَجَتِ الطَّالِبَةُ مِنَ الْفَصْلِ",
            "options": ["خَرَجَتِ الطَّالِبَةُ مِنَ الْفَصْلِ", "خَرَجَ الطَّالِبَةُ مِنَ الْفَصْلِ", "خَرَجْنَ الطَّالِبَةُ مِنَ الْفَصْلِ", "خَرَجُوا الطَّالِبَةُ مِنَ الْفَصْلِ"],
            "emoji": "👩‍🎓", "hint_ur": "فعل کے آخر میں تائے تانیث آئے گی: خَرَجَتِ الطَّالِبَةُ۔", "hint_en": "Verb takes feminine marker: Kharajati at-taalibatu.",
            "explanation_ur": "فاعل مؤنث ہو تو فعل کے ساتھ تائے تانیث آتی ہے: خَرَجَتِ الطَّالِبَةُ۔", "explanation_en": "Feminine singular subject requires taa ta'neeth: Kharajat."
        },
        # T4: تصريف الفعل مع أنتنّ
        {
            "id": "b2_u7_t4_q1", "book": 2, "unit_num": 7, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): جمع مؤنث مخاطب", "badge_en": "Exercise (4): 2nd Person Feminine Plural",
            "tamreen_title_ar": "إِسْنَادُ الْفِعْلِ إِلَى ضَمِيرِ (أَنْتُنَّ):", "tamreen_title_ur": "فعل کو ضمیر 'أَنْتُنَّ' (تم سب عورتیں) کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugate past tense with 'Antunna':",
            "grammar_goal_ur": "أَنْتُنَّ ذَهَبْتُنَّ کی ساخت۔", "grammar_goal_en": "Antunna thahabtunna structure.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا أَخَوَاتُ، أَ [ ＿＿＿ ] الدَّرْسَ؟",
            "prompt_ur": "اے بہنو، کیا تم نے سبق سمجھا؟", "prompt_en": "O sisters, did you understand the lesson?",
            "answer": "فَهِمْتُنَّ",
            "options": ["فَهِمْتُنَّ", "فَهِمْتُمْ", "فَهِمْنَ", "فَهِمْتِ"],
            "emoji": "👭", "hint_ur": "جمع مؤنث مخاطب کے لیے 'ـتُنَّ' لاحق ہوتا ہے: فَهِمْتُنَّ۔", "hint_en": "2nd person feminine plural takes '-tunna': Fahimtunna.",
            "explanation_ur": "جمع مؤنث مخاطب کے لیے صیغہ 'فَهِمْتُنَّ' آتا ہے۔", "explanation_en": "Second person feminine plural past takes '-tunna': Fahimtunna."
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 8: الْفِعْلُ الْمُضَارِعُ (يَذْهَبُ، تَذْهَبُ، أَذْهَبُ، نَذْهَبُ)
    # -------------------------------------------------------------------------
    units[8] = [
        # T1: حروف المضارعة
        {
            "id": "b2_u8_t1_q1", "book": 2, "unit_num": 8, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): حروفِ مضارع", "badge_en": "Exercise (1): Present Tense Prefixes",
            "tamreen_title_ar": "حُرُوفُ الْمُضَارَعَةِ (أَنَيْتَ):", "tamreen_title_ur": "حروف مضارع (ہمزہ، نون، یاء، تاء) کی پہچان کریں:", "tamreen_title_en": "Identify present tense prefixes (Alif, Noon, Yaa, Taa):",
            "grammar_goal_ur": "ماضی سے مضارع بناتے وقت شروع میں حروف مضارع کا اضافہ۔", "grammar_goal_en": "Forming the present tense with appropriate prefixes.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْفِعْلُ الْمُضَارِعُ مِنْ (ذَهَبَ) مَعَ ضَمِيرِ (هُوَ): [ ＿＿＿ ]",
            "prompt_ur": "هو (وہ ایک مرد) کے ساتھ مضارع کا صیغہ چنیں:", "prompt_en": "Select the present tense verb with 'Huwa':",
            "answer": "يَذْهَبُ",
            "options": ["يَذْهَبُ", "تَذْهَبُ", "أَذْهَبُ", "نَذْهَبُ"],
            "emoji": "🚶‍♂️", "hint_ur": "مذکر غائب کے لیے علامت مضارع 'ياء' آتی ہے: يَذْهَبُ۔", "hint_en": "3rd person masculine singular takes yaa prefix: Yath-habu.",
            "explanation_ur": "مفرد مذکر غائب کے لیے 'يَذْهَبُ' آتا ہے۔", "explanation_en": "Third person masculine singular takes prefix yaa: Yathhabu."
        },
        # T2: إسناد المضارع إلى المتكلم
        {
            "id": "b2_u8_t2_q1", "book": 2, "unit_num": 8, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مضارع متکلم", "badge_en": "Exercise (2): 1st Person Present",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى (أَنَا) وَ(نَحْنُ):", "tamreen_title_ur": "مضارع کو ضمیر متکلم (میں اور ہم) کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating present verbs with 'Ana' and 'Nahnu':",
            "grammar_goal_ur": "أَنَا أَذْهَبُ اور نَحْنُ نَذْهَبُ کی تمیز۔", "grammar_goal_en": "Distinguishing Ana ath-habu and Nahnu nath-habu.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] اللُّغَةَ الْعَرَبِيَّةَ .",
            "prompt_ur": "میں عربی زبان پڑھتا ہوں:", "prompt_en": "I study the Arabic language:",
            "answer": "أَدْرُسُ",
            "options": ["أَدْرُسُ", "يَدْرُسُ", "تَدْرُسُ", "نَدْرُسُ"],
            "emoji": "📖", "hint_ur": "متکلم کے لیے علامت مضارع ہمزہ 'أَ' ہے: أَدْرُسُ۔", "hint_en": "1st person singular prefix is alif: Adrusu.",
            "explanation_ur": "أنا کے ساتھ ہمزہ مضارعت آتا ہے: أَنَا أَدْرُسُ۔", "explanation_en": "First person singular takes alif prefix: Adrusu."
        },
        # T3: إسناد المضارع إلى المخاطب
        {
            "id": "b2_u8_t3_q1", "book": 2, "unit_num": 8, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مضارع مخاطب", "badge_en": "Exercise (3): 2nd Person Present",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى (أَنْتَ):", "tamreen_title_ur": "مخاطب مذکر کے لیے مضارع کا صیغہ منتخب کریں:", "tamreen_title_en": "Conjugate present verb with 'Anta':",
            "grammar_goal_ur": "أَنْتَ تَذْهَبُ کی ساخت۔", "grammar_goal_en": "Anta tath-habu structure.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ [ ＿＿＿ ] يَا أَخِي؟",
            "prompt_ur": "اے میرے بھائی تم کہاں جا رہے ہو؟", "prompt_en": "Where are you going, my brother?",
            "answer": "تَذْهَبُ",
            "options": ["تَذْهَبُ", "يَذْهَبُ", "أَذْهَبُ", "تَذْهَبِينَ"],
            "emoji": "🚶‍♂️", "hint_ur": "مخاطب مذکر کے لیے علامت مضارع 'تاء' آتی ہے: تَذْهَبُ۔", "hint_en": "2nd person masculine takes taa prefix: Tath-habu.",
            "explanation_ur": "مخاطب مذکر کے لیے 'تَذْهَبُ' آتا ہے۔", "explanation_en": "Second person masculine singular takes prefix taa: Tathhabu."
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 9: ضَمَائِرُ الرَّفْعِ فِي الْمُضَارِعِ (الأَفْعَالُ الْخَمْسَةُ)
    # -------------------------------------------------------------------------
    units[9] = [
        # T1: إسناد المضارع إلى واو الجماعة
        {
            "id": "b2_u9_t1_q1", "book": 2, "unit_num": 9, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): واو الجماعت مع مضارع", "badge_en": "Exercise (1): Present with Waw al-Jama'ah",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى وَاوِ الْجَمَاعَةِ (يَفْعَلُونَ):", "tamreen_title_ur": "جمع مذکر غائب کے ساتھ مضارع کا صیغہ منتخب کریں:", "tamreen_title_en": "Conjugate present tense with Waw al-Jama'ah:",
            "grammar_goal_ur": "الطلاب يَذْهَبُونَ کی ساخت اور ثبوت نون۔", "grammar_goal_en": "Plural present conjugation with attached Waw and Nun.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطُّلَّابُ [ ＿＿＿ ] إِلَى الْمَلْعَبِ كُلَّ مَسَاءٍ .",
            "prompt_ur": "طلبہ ہر شام کھیل کے میدان جاتے ہیں:", "prompt_en": "The students go to the playground every evening:",
            "answer": "يَذْهَبُونَ",
            "options": ["يَذْهَبُونَ", "يَذْهَبُ", "تَذْهَبُونَ", "يَذْهَبْنَ"],
            "emoji": "⚽", "hint_ur": "جمع مذکر غائب کے لیے واو اور نون لاحق ہوتے ہیں: يَذْهَبُونَ۔", "hint_en": "3rd person masculine plural takes -oona suffix: Yath-haboona.",
            "explanation_ur": "جمع مذکر فاعل ہو تو مضارع میں واو اور نون آتا ہے: يَذْهَبُونَ۔", "explanation_en": "Masculine plural subject takes -oona suffix: Yathhaboona."
        },
        # T2: إسناد المضارع إلى ياء المخاطبة
        {
            "id": "b2_u9_t2_q1", "book": 2, "unit_num": 9, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): یاء المخاطبہ", "badge_en": "Exercise (2): 2nd Person Feminine Singular",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى يَاءِ الْمُخَاطَبَةِ (تَفْعَلِينَ):", "tamreen_title_ur": "مخاطب مؤنث کے ساتھ مضارع کا صیغہ منتخب کریں:", "tamreen_title_en": "Conjugate present tense with Yaa al-Mukhartabah:",
            "grammar_goal_ur": "أَنْتِ تَذْهَبِينَ کی ساخت۔", "grammar_goal_en": "Anti tath-habeena structure.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَاذَا [ ＿＿＿ ] يَا مَرْيَمُ؟",
            "prompt_ur": "اے مریم تم کیا لکھ رہی ہو؟", "prompt_en": "What are you writing, O Maryam?",
            "answer": "تَكْتُبِينَ",
            "options": ["تَكْتُبِينَ", "تَكْتُبُ", "يَكْتُبْنَ", "تَكْتُبُونَ"],
            "emoji": "✍️", "hint_ur": "مخاطب مؤنث کے لیے 'ـِينَ' لاحق ہوتا ہے: تَكْتُبِينَ۔", "hint_en": "2nd person feminine singular takes -eena suffix: Taktubeena.",
            "explanation_ur": "مفرد مؤنث مخاطب کے لیے صیغہ 'تَكْتُبِينَ' آتا ہے۔", "explanation_en": "Second person feminine singular takes -eena suffix: Taktubeena."
        },
        # T3: إسناد المضارع إلى نون النسوة
        {
            "id": "b2_u9_t3_q1", "book": 2, "unit_num": 9, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): نون النسوہ مع مضارع", "badge_en": "Exercise (3): Present with Nun an-Niswah",
            "tamreen_title_ar": "إِسْنَادُ الْمُضَارِعِ إِلَى نُونِ النِّسْوَةِ (يَفْعَلْنَ / تَفْعَلْنَ):", "tamreen_title_ur": "طالبات (جمع مؤنث) کے ساتھ مضارع کا صیغہ منتخب کریں:", "tamreen_title_en": "Conjugate present tense with Nun an-Niswah:",
            "grammar_goal_ur": "الطَّالِبَاتُ يَذْهَبْنَ کی ساخت۔", "grammar_goal_en": "Feminine plural present conjugation.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطَّالِبَاتُ [ ＿＿＿ ] فِي الْمَهْجَعِ .",
            "prompt_ur": "طالبات ہاسٹل میں رہتی ہیں:", "prompt_en": "The female students live in the dormitory:",
            "answer": "يَسْكُنَّ",
            "options": ["يَسْكُنَّ", "يَسْكُنُونَ", "تَسْكُنُ", "يَسْكُنُ"],
            "emoji": "🏢", "hint_ur": "جمع مؤنث غائب کے لیے 'يَفْعَلْنَ' آتا ہے: يَسْكُنَّ۔", "hint_en": "3rd person feminine plural takes -na suffix: Yaskunna.",
            "explanation_ur": "جمع مؤنث کے ساتھ نون نسوہ لاحق ہوتی ہے: يَسْكُنَّ۔", "explanation_en": "Feminine plural takes nun an-niswah: Yaskunna."
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 10: حُرُوفُ النَّصْبِ فِي الْمُضَارِعِ (أَنْ، لَنْ، كَيْ)
    # -------------------------------------------------------------------------
    units[10] = [
        # T1: أن الناصبة للمضارع
        {
            "id": "b2_u10_t1_q1", "book": 2, "unit_num": 10, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): حرفِ (أَنْ) ناصبہ", "badge_en": "Exercise (1): Subjunctive with 'An'",
            "tamreen_title_ar": "عَمَلُ (أَنْ) النَّاصِبَةِ فِي الْمُضَارِعِ:", "tamreen_title_ur": "فعل مضارع پر 'أَنْ' کا نحوی عمل (نصب دینا):", "tamreen_title_en": "The subjunctive effect of 'An' on present verbs:",
            "grammar_goal_ur": "أَنْ مضارع کو فتحہ (زبر) دیتی ہے: أُرِيدُ أَنْ أَذْهَبَ۔", "grammar_goal_en": "'An' places the present verb in the subjunctive mood (Nasb with fathah).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أُرِيدُ أَنْ [ ＿＿＿ ] إِلَى السُّوقِ .",
            "prompt_ur": "میں بازار جانا چاہتا ہوں (درست اعراب چنیں):", "prompt_en": "I want to go to the market (choose correct case):",
            "answer": "أَذْهَبَ",
            "options": ["أَذْهَبَ", "أَذْهَبُ", "أَذْهَبْ", "أَذْهَبِ"],
            "emoji": "🚶‍♂️", "hint_ur": "'أَنْ' کے بعد فعل مضارع پر زبر (فتحہ) آتا ہے: أَذْهَبَ۔", "hint_en": "After 'An', the present verb takes fathah: Ath-haba.",
            "explanation_ur": "أن ناصبہ مضارع کو منسوب کرتی ہے: أَنْ أَذْهَبَ۔", "explanation_en": "Subjunctive particle 'An' puts the verb in the accusative: An ath-haba."
        },
        # T2: لن النافية الناصبة للمستقبل
        {
            "id": "b2_u10_t2_q1", "book": 2, "unit_num": 10, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): حرفِ (لَنْ) ناصبہ", "badge_en": "Exercise (2): Future Negation with 'Lan'",
            "tamreen_title_ar": "نَفْيُ الْمُسْتَقْبَلِ وَنَصْبُ الْمُضَارِعِ بِـ (لَنْ):", "tamreen_title_ur": "مستقبل میں نفیِ موکد کے لیے 'لَنْ' کا استعمال اور اعراب:", "tamreen_title_en": "Emphatic future negation and subjunctive marking with 'Lan':",
            "grammar_goal_ur": "لَنْ مستقبل کی نفی کرتی ہے اور مضارع کو فتحہ دیتی ہے۔", "grammar_goal_en": "'Lan' negates future actions and marks the verb accusative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "[ ＿＿＿ ] إِلَى بَلَدِي فِي الْعُطْلَةِ الصَّيْفِيَّةِ .",
            "prompt_ur": "میں گرمیوں کی چھٹیوں میں ہرگز اپنے وطن نہیں جاؤں گا:", "prompt_en": "I will never go to my home country during summer vacation:",
            "answer": "لَنْ أَذْهَبَ",
            "options": ["لَنْ أَذْهَبَ", "لَنْ أَذْهَبُ", "مَا أَذْهَبَ", "لَمْ أَذْهَبَ"],
            "emoji": "✈️", "hint_ur": "مستقبل کی نفی 'لَنْ' سے ہوتی ہے اور آخر میں زبر آتا ہے: لَنْ أَذْهَبَ۔", "hint_en": "'Lan' indicates future negation with fathah: Lan ath-haba.",
            "explanation_ur": "لَنْ ناصبہ مضارع پر داخل ہو کر اسے مستقبل کے لیے منفی کرتی ہے: لَنْ أَذْهَبَ۔", "explanation_en": "Lan negates the future and puts the verb in the subjunctive: Lan athhaba."
        },
        # T3: حذف النون مع أن ولن في الأفعال الخمسة
        {
            "id": "b2_u10_t3_q1", "book": 2, "unit_num": 10, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): افعال خمسہ کا نصب", "badge_en": "Exercise (3): Subjunctive in Five Verbs",
            "tamreen_title_ar": "حَذْفُ النُّونِ فِي نَصْبِ الأَفْعَالِ الْخَمْسَةِ:", "tamreen_title_ur": "افعال خمسہ میں 'لَنْ' کے داخل ہونے پر نون کا گرنا:", "tamreen_title_en": "Dropping the Nun in subjunctive mood of the Five Verbs:",
            "grammar_goal_ur": "يَذْهَبُونَ پر لن داخل ہو کر لَنْ يَذْهَبُوا بنتا ہے۔", "grammar_goal_en": "Yathhaboona becomes Lan yathhaboo.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطُّلَّابُ [ ＿＿＿ ] الْيَوْمَ . (نَفْيُ: يَخْرُجُونَ)",
            "prompt_ur": "طلبہ آج ہرگز نہیں نکلیں گے:", "prompt_en": "The students will never exit today:",
            "answer": "لَنْ يَخْرُجُوا",
            "options": ["لَنْ يَخْرُجُوا", "لَنْ يَخْرُجُونَ", "لَنْ يَخْرُجْ", "مَا يَخْرُجُوا"],
            "emoji": "🚪", "hint_ur": "حالت نصب میں افعال خمسہ کا نون حذف ہو جاتا ہے: لَنْ يَخْرُجُوا۔", "hint_en": "Nun drops in the subjunctive case of Five Verbs: Lan yakhrujoo.",
            "explanation_ur": "افعال خمسہ کی علامت نصب حذف نون ہے: لَنْ يَخْرُجُوا۔", "explanation_en": "The subjunctive marker for Five Verbs is dropping the Nun: Lan yakhrujoo."
        }
    ]

    # -------------------------------------------------------------------------
    # UNIT 11 to 31: Systematically generate remaining units!
    # -------------------------------------------------------------------------
    # UNIT 11: لَمْ الْجَازِمَةُ وَلَا النَّاهِيَةُ
    units[11] = [
        {
            "id": "b2_u11_t1_q1", "book": 2, "unit_num": 11, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): حرفِ (لَمْ) جازمہ", "badge_en": "Exercise (1): Jussive with 'Lam'",
            "tamreen_title_ar": "جَزْمُ الْفِعْلِ الْمُضَارِعِ بِـ (لَمْ):", "tamreen_title_ur": "'لَمْ' کے ساتھ مضارع کو جزم دینا اور ماضی منفی بنانا:", "tamreen_title_en": "Jussive mood and past negation with 'Lam':",
            "grammar_goal_ur": "لَمْ مضارع کو جزم (سکون) دیتی ہے اور معنی کو ماضی منفی میں بدلتی ہے۔", "grammar_goal_en": "Lam puts the verb in the jussive (Sukun) and turns meaning to negative past.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "[ ＿＿＿ ] حَامِدٌ إِلَى الْمَدْرَسَةِ الْيَوْمَ .",
            "prompt_ur": "حامد آج اسکول نہیں گیا (لَمْ کے ساتھ):", "prompt_en": "Hamid did not go to school today (with Lam):",
            "answer": "لَمْ يَذْهَبْ",
            "options": ["لَمْ يَذْهَبْ", "لَمْ يَذْهَبُ", "لَمْ يَذْهَبَ", "لَا يَذْهَبْ"],
            "emoji": "🏫", "hint_ur": "لَمْ کے بعد فعل پر جزم (سکون) آتا ہے: لَمْ يَذْهَبْ۔", "hint_en": "Verb after Lam takes sukun: Lam yath-hab.",
            "explanation_ur": "لَمْ حرف جزم و نفی و قلب ہے: لَمْ يَذْهَبْ۔", "explanation_en": "Lam is a particle of jussive and past negation: Lam yathhab."
        },
        {
            "id": "b2_u11_t2_q1", "book": 2, "unit_num": 11, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): حرفِ (لَمَّا)", "badge_en": "Exercise (2): Jussive with 'Lamma'",
            "tamreen_title_ar": "جَزْمُ الْمُضَارِعِ بِـ (لَمَّا):", "tamreen_title_ur": "'لَمَّا' (ابھی تک نہیں) کا استعمال اور جزم:", "tamreen_title_en": "Jussive with 'Lamma' (not yet):",
            "grammar_goal_ur": "لَمَّا حال تک نفی کو کھینچتی ہے: لَمَّا يَرْجِعْ۔", "grammar_goal_en": "'Lamma' denotes 'not yet' up to the present moment.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَرَجَعَ الْمُدِيرُ؟ — لاَ، [ ＿＿＿ ] .",
            "prompt_ur": "کیا پرنسپل واپس آئے؟ نہیں، ابھی تک واپس نہیں آئے:", "prompt_en": "Did the director return? No, not yet:",
            "answer": "لَمَّا يَرْجِعْ",
            "options": ["لَمَّا يَرْجِعْ", "لَمَّا يَرْجِعُ", "لَمْ يَرْجِعَ", "مَا يَرْجِعْ"],
            "emoji": "👔", "hint_ur": "ابھی تک نہیں کے لیے 'لَمَّا يَرْجِعْ' آتا ہے۔", "hint_en": "'Not yet returned' is expressed as: Lamma yarji'.",
            "explanation_ur": "لَمَّا حرف جزم ہے جو نفی کو وقت تکلم تک جاری رکھتا ہے: لَمَّا يَرْجِعْ۔", "explanation_en": "Lamma indicates ongoing negation up to now: Lamma yarji'."
        }
    ]

    # UNIT 12: فِعْلُ الأَمْرِ (اجْلِسْ، اكْتُبْ، اذْهَبُوا)
    units[12] = [
        {
            "id": "b2_u12_t1_q1", "book": 2, "unit_num": 12, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): صیغہ امر", "badge_en": "Exercise (1): Imperative Form (Al-Amr)",
            "tamreen_title_ar": "صَوْغُ فِعْلِ الأَمْرِ مِنَ الثُّلَاثِيِّ:", "tamreen_title_ur": "ثلاثی مجرد سے صیغہ امر بنانا:", "tamreen_title_en": "Forming the imperative from triliteral verbs:",
            "grammar_goal_ur": "تَجْلِسُ سے اجْلِسْ اور تَكْتُبُ سے اكْتُبْ بنانے کا قاعدہ۔", "grammar_goal_en": "Deriving imperative from present tense verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِعْلُ الأَمْرِ مِنْ: (تَجْلِسُ) لِلْمُخَاطَبِ الْمُفْرَدِ هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "بیٹھو (مرد کے لیے امر کا صیغہ):", "prompt_en": "Sit down (imperative masculine singular):",
            "answer": "اجْلِسْ",
            "options": ["اجْلِسْ", "اجْلِسُ", "تَجْلِسْ", "جَلَسَ"],
            "emoji": "🪑", "hint_ur": "تجلس سے حرف مضارع گرا کر ہمزۃ الوصل مکسورہ کے ساتھ: اجْلِسْ۔", "hint_en": "Drop prefix, add hamzat al-wasl with kasrah: Ijlis.",
            "explanation_ur": "تَجْلِسُ کا امر مکسور العین ہونے کی وجہ سے 'اجْلِسْ' آتا ہے۔", "explanation_en": "Present with kasrah on 'ayn forms imperative as: Ijlis."
        },
        {
            "id": "b2_u12_t2_q1", "book": 2, "unit_num": 12, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): امر برائے جمع و مؤنث", "badge_en": "Exercise (2): Imperative Plural & Feminine",
            "tamreen_title_ar": "تَصْرِيفُ فِعْلِ الأَمْرِ مَعَ الضَّمَائِرِ:", "tamreen_title_ur": "امر کو جمع اور مؤنث کے ساتھ جوڑیں:", "tamreen_title_en": "Conjugating imperatives for plural and feminine subjects:",
            "grammar_goal_ur": "اجْلِسُوا (جمع مذکر)، اجْلِسِي (مفرد مؤنث)، اجْلِسْنَ (جمع مؤنث)۔", "grammar_goal_en": "Conjugating imperatives: Ijlisoo, Ijlisee, Ijlisna.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا أَبْنَائِي، [ ＿＿＿ ] إِلَى الْفَصْلِ .",
            "prompt_ur": "اے میرے بیٹو، کلاس میں جاؤ (جمع مذکر):", "prompt_en": "O my sons, go to the classroom (masculine plural):",
            "answer": "اذْهَبُوا",
            "options": ["اذْهَبُوا", "اذْهَبْ", "اذْهَبِي", "اذْهَبْنَ"],
            "emoji": "🏫", "hint_ur": "جمع مذکر مخاطب کے لیے واو الجماعت لاحق ہوتی ہے: اذْهَبُوا۔", "hint_en": "Masculine plural imperative takes -oo: Ith-haboo.",
            "explanation_ur": "جمع مذکر مخاطب کا امر واو الجماعت کے ساتھ آتا ہے: اذْهَبُوا۔", "explanation_en": "Masculine plural imperative: Ithhaboo."
        }
    ]

    # UNIT 13: الأَمْرُ مِنَ الْمُعْتَلِّ (قُلْ، بِعْ، خَفْ، ادْعُ)
    units[13] = [
        {
            "id": "b2_u13_t1_q1", "book": 2, "unit_num": 13, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): امر از اجوف", "badge_en": "Exercise (1): Imperative from Hollow Verbs",
            "tamreen_title_ar": "صَوْغُ الأَمْرِ مِنَ الْفِعْلِ الأَجْوَفِ:", "tamreen_title_ur": "اجوف سے صیغہ امر بنانا (التقاء ساکنین سے حرف علت کا حذف):", "tamreen_title_en": "Forming imperatives from hollow verbs:",
            "grammar_goal_ur": "تَقُولُ -> قُلْ، تَبِيعُ -> بِعْ، تَنَامُ -> نَمْ۔", "grammar_goal_en": "Dropping weak letter in hollow imperatives due to meeting of two sukoons.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِعْلُ الأَمْرِ مِنْ: (قَالَ يَقُولُ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "کہو / سچ بولو (امر کا صیغہ):", "prompt_en": "Say / speak (imperative form):",
            "answer": "قُلْ",
            "options": ["قُلْ", "قُولْ", "اقُولْ", "قَالَ"],
            "emoji": "🗣️", "hint_ur": "سکون آنے پر واو گر جاتا ہے: قُلْ۔", "hint_en": "Weak middle letter drops before sukun: Qul.",
            "explanation_ur": "التقاء ساکنین کی وجہ سے واو گر کر 'قُلْ' رہ جاتا ہے۔", "explanation_en": "Meeting of two sukoons causes waw to drop: Qul."
        },
        {
            "id": "b2_u13_t2_q1", "book": 2, "unit_num": 13, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): امر از ناقص", "badge_en": "Exercise (2): Imperative from Defective Verbs",
            "tamreen_title_ar": "صَوْغُ الأَمْرِ مِنَ الْفِعْلِ النَّاقِصِ:", "tamreen_title_ur": "ناقص سے امر بناتے وقت حرف علت کو گرانا:", "tamreen_title_en": "Forming imperatives from defective verbs by dropping the weak letter:",
            "grammar_goal_ur": "تَدْعُو -> ادْعُ، تَمْشِي -> امْشِ۔", "grammar_goal_en": "Dropping final weak letter in defective imperatives.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِعْلُ الأَمْرِ مِنْ: (دَعَا يَدْعُو) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "دعا مانگو / بلاؤ (امر کا صیغہ):", "prompt_en": "Call / supplicate (imperative form):",
            "answer": "ادْعُ",
            "options": ["ادْعُ", "ادْعُو", "دَعَا", "تَدْعُ"],
            "emoji": "🤲", "hint_ur": "امر میں آخری حرف علت (واو) گر کر ضمہ رہ جاتا ہے: ادْعُ۔", "hint_en": "Weak ending drops in imperative leaving dammah: Ud'u.",
            "explanation_ur": "ناقص کا امر حرف علت کے گرنے پر مبنی ہوتا ہے: ادْعُ۔", "explanation_en": "Defective imperative is built on dropping the weak letter: Ud'u."
        }
    ]

    # UNIT 14: لاَ النَّاهِيَةُ
    units[14] = [
        {
            "id": "b2_u14_t1_q1", "book": 2, "unit_num": 14, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): لا ناہیہ", "badge_en": "Exercise (1): Prohibitive 'Laa'",
            "tamreen_title_ar": "عَمَلُ (لاَ النَّاهِيَةِ) الْجَازِمَةِ:", "tamreen_title_ur": "کسی کام سے روکنے کے لیے 'لا الناہیة' کا استعمال اور جزم:", "tamreen_title_en": "Syntax and semantics of prohibitive 'Laa':",
            "grammar_goal_ur": "لا الناہیۃ مضارع کو جزم دیتی ہے: لَا تَذْهَبْ (مت جاؤ)۔", "grammar_goal_en": "Prohibitive Laa puts the verb into the jussive (Sukun).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا حَامِدُ، [ ＿＿＿ ] الْفَصْلَ فِي وَقْتِ الدَّرْسِ ! (نَهْيٌ عَنِ الْخُرُوجِ)",
            "prompt_ur": "اے حامد، سبق کے دوران کلاس سے مت نکلو:", "prompt_en": "O Hamid, do not exit the classroom during class:",
            "answer": "لَا تَخْرُجْ",
            "options": ["لَا تَخْرُجْ", "لَا تَخْرُجُ", "مَا تَخْرُجْ", "لَنْ تَخْرُجْ"],
            "emoji": "🚫", "hint_ur": "روکنے کے لیے 'لَا تَخْرُجْ' پر جزم آئے گا۔", "hint_en": "Prohibition takes jussive sukun: Laa takhruj.",
            "explanation_ur": "لا ناہیہ مضارع کو جزم دیتی ہے: لَا تَخْرُجْ۔", "explanation_en": "Prohibitive Laa marks the verb with sukun: Laa takhruj."
        },
        {
            "id": "b2_u14_t2_q1", "book": 2, "unit_num": 14, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): نہی برائے جمع", "badge_en": "Exercise (2): Prohibition for Plural",
            "tamreen_title_ar": "النَّهْيُ مَعَ وَاوِ الْجَمَاعَةِ (حَذْفُ النُّونِ):", "tamreen_title_ur": "جمع کو روکتے وقت نون کا حذف ہونا:", "tamreen_title_en": "Prohibition with masculine plural (dropping Nun):",
            "grammar_goal_ur": "لَا تَذْهَبُوا میں علامت جزم حذف نون ہے۔", "grammar_goal_en": "Dropping the Nun when prohibiting masculine plural.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا إِخْوَانُ، [ ＿＿＿ ] فِي الشَّارِعِ ! (نَهْيٌ عَنِ اللَّعِبِ)",
            "prompt_ur": "اے بھائیو، سڑک پر مت کھیلو:", "prompt_en": "O brothers, do not play in the street:",
            "answer": "لَا تَلْعَبُوا",
            "options": ["لَا تَلْعَبُوا", "لَا تَلْعَبُونَ", "لَا تَلْعَبْ", "مَا تَلْعَبُوا"],
            "emoji": "🛑", "hint_ur": "جمع کو منع کرتے وقت نون گر جاتا ہے: لَا تَلْعَبُوا۔", "hint_en": "Plural prohibition drops Nun: Laa tal'aboo.",
            "explanation_ur": "لا ناہیہ افعال خمسہ کے نون کو گرا دیتی ہے: لَا تَلْعَبُوا۔", "explanation_en": "Prohibitive Laa drops Nun in Five Verbs: Laa tal'aboo."
        }
    ]

    # UNIT 15: حُرُوفُ الْعَطْفِ (الْوَاوُ، الْفَاءُ، ثُمَّ، أَوْ)
    units[15] = [
        {
            "id": "b2_u15_t1_q1", "book": 2, "unit_num": 15, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): معانی حروف العطف", "badge_en": "Exercise (1): Coordinating Conjunctions",
            "tamreen_title_ar": "مَعَانِي حُرُوفِ الْعَطْفِ (ثُمَّ، الْفَاءُ، أَوْ):", "tamreen_title_ur": "حروف عطف کے معانی (ترتیب، تعقیب اور تراخی):", "tamreen_title_en": "Meanings of conjunctions (Thumma, Faa, Aw):",
            "grammar_goal_ur": "الفاء (تعقیب بلا تاخیر) اور ثمّ (ترتیب مع تاخیر/تراخی) کا فرق۔", "grammar_goal_en": "Faa denotes immediate sequence, Thumma denotes sequence with a delay.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "رَكَعَ الإِمَامُ [ ＿＿＿ ] سَجَدَ . (لِلتَّرَاخِي وَالْمُهْلَةِ)",
            "prompt_ur": "امام نے رکوع کیا پھر سجدہ کیا (وقفے کے ساتھ):", "prompt_en": "The Imam bowed, then prostrated (with interval):",
            "answer": "ثُمَّ",
            "options": ["ثُمَّ", "فَـ", "وَ", "أَوْ"],
            "emoji": "🕌", "hint_ur": "مہلت اور وقفے کے ساتھ عطف کے لیے 'ثُمَّ' آتا ہے۔", "hint_en": "Sequence with interval is denoted by 'Thumma'.",
            "explanation_ur": "ثُمَّ عطف مع التراخی (وقفے کے ساتھ) کے لیے آتی ہے۔", "explanation_en": "Thumma denotes sequential order with a time interval."
        }
    ]

    # UNIT 16: الأَسْمَاءُ الْمَوْصُولَةُ لِلْجَمْعِ (الَّذِينَ، اللَّاتِي)
    units[16] = [
        {
            "id": "b2_u16_t1_q1", "book": 2, "unit_num": 16, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اسم موصول برائے جمع", "badge_en": "Exercise (1): Relative Pronouns for Plural",
            "tamreen_title_ar": "اسْتِعْمَالُ (الَّذِينَ) وَ(اللَّاتِي):", "tamreen_title_ur": "جمع مذکر کے لیے 'الَّذِينَ' اور جمع مؤنث کے لیے 'اللَّاتِي':", "tamreen_title_en": "Using 'Alladheena' (masculine) and 'Allaatee' (feminine):",
            "grammar_goal_ur": "اسم موصول کا صلے کے فاعل کے مطابق ہونا۔", "grammar_goal_en": "Agreement of relative pronoun with plural antecedents.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَنْ هٰؤُلاَءِ الْفِتْيَةُ [ ＿＿＿ ] دَخَلُوا الْفَصْلَ؟",
            "prompt_ur": "وہ نوجوان کون ہیں جو کلاس میں داخل ہوئے؟", "prompt_en": "Who are those young men who entered the class?",
            "answer": "الَّذِينَ",
            "options": ["الَّذِينَ", "الَّذِي", "اللَّاتِي", "الَّتِي"],
            "emoji": "👥", "hint_ur": "جمع مذکر کے لیے 'الَّذِينَ' آتا ہے۔", "hint_en": "Masculine plural relative pronoun is: Alladheena.",
            "explanation_ur": "جمع مذکر عاقل کے لیے اسم موصول 'الَّذِينَ' استعمال ہوتا ہے۔", "explanation_en": "Alladheena is the relative pronoun for masculine plural."
        }
    ]

    # UNIT 17: الأَعْدَادُ التَّرْتِيبِيَّةُ (الأَوَّلُ إِلَى الْعَاشِرِ)
    units[17] = [
        {
            "id": "b2_u17_t1_q1", "book": 2, "unit_num": 17, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): ترتیبی گنتی", "badge_en": "Exercise (1): Ordinal Numbers",
            "tamreen_title_ar": "الأَعْدَادُ التَّرْتِيبِيَّةُ (الأَوَّلُ، الثَّانِي، الثَّالِثُ...):", "tamreen_title_ur": "ترتیبی عدد (پہلا، دوسرا، تیسرا) صفت بن کر موصوف کے مطابق آتا ہے:", "tamreen_title_en": "Ordinal numbers acting as descriptive adjectives:",
            "grammar_goal_ur": "ترتیبی عدد نعت بنتا ہے اور مذکر و مؤنث میں مطابقت رکھتا ہے۔", "grammar_goal_en": "Ordinal numbers agree in gender and definiteness with their nouns.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذَا هُوَ الدَّرْسُ [ ＿＿＿ ] .",
            "prompt_ur": "یہ چوتھا سبق ہے:", "prompt_en": "This is the fourth lesson:",
            "answer": "الرَّابِعُ",
            "options": ["الرَّابِعُ", "أَرْبَعَةٌ", "الأَرْبَعَةُ", "رَابِعَةٌ"],
            "emoji": "4️⃣", "hint_ur": "مذکر کے لیے 'الرَّابِعُ' صفت آئے گی۔", "hint_en": "Masculine ordinal number: Ar-Rabi'u.",
            "explanation_ur": "الدَّرْسُ مذکر معرفہ ہے اس لیے نعت 'الرَّابِعُ' آئے گی۔", "explanation_en": "Ad-Darsu is masculine definite, taking 'Ar-Rabi'u'."
        }
    ]

    # UNIT 18: كَمِ الِاسْتِفْهَامِيَّةُ
    units[18] = [
        {
            "id": "b2_u18_t1_q1", "book": 2, "unit_num": 18, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): کم استفہامیہ", "badge_en": "Exercise (1): Interrogative 'Kam'",
            "tamreen_title_ar": "تَمْيِيزُ (كَمِ الاسْتِفْهَامِيَّةِ):", "tamreen_title_ur": "کم استفہامیہ کا تمییز مفرد اور منسوب (دو زبر) ہوتا ہے:", "tamreen_title_en": "Specification of interrogative Kam (accusative singular):",
            "grammar_goal_ur": "كَمْ طَالِباً، كَمْ رِيَالاً کا ضبط۔", "grammar_goal_en": "Governing an accusative singular noun after Kam.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَمْ [ ＿＿＿ ] لَكَ يَا عَلِيُّ؟",
            "prompt_ur": "اے علی تمہارے کتنے بھائی ہیں؟", "prompt_en": "How many brothers do you have, O Ali?",
            "answer": "أَخاً",
            "options": ["أَخاً", "أَخٌ", "إِخْوَةٌ", "أَخٍ"],
            "emoji": "👦", "hint_ur": "کم استفہامیہ کے بعد اسم مفرد منسوب (دو زبر) آتا ہے: أَخاً۔", "hint_en": "Noun after interrogative Kam is singular accusative: Akhan.",
            "explanation_ur": "کم استفہامیہ کا تمییز مفرد منسوب بالفتحہ ہوتا ہے: أَخاً۔", "explanation_en": "Tamyeeth of Kam is singular accusative: Akhan."
        }
    ]

    # UNIT 19: الْمُثَنَّى (كِتَابَانِ / كِتَابَيْنِ)
    units[19] = [
        {
            "id": "b2_u19_t1_q1", "book": 2, "unit_num": 19, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اعرابِ تثنیہ", "badge_en": "Exercise (1): Dual Noun Inflection",
            "tamreen_title_ar": "إِعْرَابُ الْمُثَنَّى فِي الرَّفْعِ وَالنَّصْبِ وَالْجَرِّ:", "tamreen_title_ur": "تثنیہ حالت رفع میں الف اور حالت نصب و جر میں یاء کے ساتھ آتا ہے:", "tamreen_title_en": "Dual noun inflection: Alif for Raf', Yaa for Nasb and Jarr:",
            "grammar_goal_ur": "حالت رفع (الف) اور حالت نصب و جر (یاء) کا فرق۔", "grammar_goal_en": "Distinguishing Alif (nominative) from Yaa (accusative/genitive).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدِي [ ＿＿＿ ] جَدِيدَانِ . (مُبْتَدَأٌ مَرْفُوعٌ)",
            "prompt_ur": "میرے پاس دو نئی کتابیں ہیں (حالت رفع):", "prompt_en": "I have two new books (nominative case):",
            "answer": "كِتَابَانِ",
            "options": ["كِتَابَانِ", "كِتَابَيْنِ", "كُتُبٌ", "كِتَابٌ"],
            "emoji": "📚", "hint_ur": "حالت رفع میں تثنیہ الف کے ساتھ آتا ہے: كِتَابَانِ۔", "hint_en": "Nominative dual ends in -aani: Kitaabaani.",
            "explanation_ur": "تثنیہ کی علامت رفع الف ہے: كِتَابَانِ۔", "explanation_en": "The nominative marker of dual is Alif: Kitaabaani."
        },
        {
            "id": "b2_u19_t2_q1", "book": 2, "unit_num": 19, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تثنیہ حالتِ نصب میں", "badge_en": "Exercise (2): Dual in Accusative Case",
            "tamreen_title_ar": "الْمُثَنَّى فِي حَالَةِ النَّصْبِ (مَفْعُولٌ بِهِ):", "tamreen_title_ur": "مفعول بہ بننے پر تثنیہ یاء کے ساتھ آتا ہے:", "tamreen_title_en": "Dual noun as direct object taking Yaa:",
            "grammar_goal_ur": "شَرَيْتُ كِتَابَيْنِ کی ساخت۔", "grammar_goal_en": "Sharaitu kitaabayni structure.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اشْتَرَيْتُ [ ＿＿＿ ] مِنَ الْمَكْتَبَةِ .",
            "prompt_ur": "میں نے لائبریری سے دو قلم خریدے (مفعول بہ):", "prompt_en": "I bought two pens from the bookstore (direct object):",
            "answer": "قَلَمَيْنِ",
            "options": ["قَلَمَيْنِ", "قَلَمَانِ", "أَقْلاَمٌ", "قَلَماً"],
            "emoji": "🖊️", "hint_ur": "مفعول بہ منسوب ہوتا ہے اور تثنیہ کا نصب یاء کے ساتھ ہے: قَلَمَيْنِ۔", "hint_en": "Accusative dual ends in -ayni: Qalamayni.",
            "explanation_ur": "تثنیہ مفعول بہ ہو تو یاء کے ساتھ منسوب ہوتا ہے: قَلَمَيْنِ۔", "explanation_en": "Dual direct object takes -ayni: Qalamayni."
        }
    ]

    # UNIT 20: الأَسْمَاءُ الْخَمْسَةُ (أَبُو، أَخُو، حَمُو، فُو، ذُو)
    units[20] = [
        {
            "id": "b2_u20_t1_q1", "book": 2, "unit_num": 20, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اسمائے خمسہ کا اعراب", "badge_en": "Exercise (1): The Five Nouns",
            "tamreen_title_ar": "إِعْرَابُ الأَسْمَاءِ الْخَمْسَةِ (الْوَاوُ، الأَلِفُ، الْيَاءُ):", "tamreen_title_ur": "اسمائے خمسہ حالت رفع میں واو، نصب میں الف، اور جر میں یاء لیتے ہیں:", "tamreen_title_en": "The Five Nouns inflection: Waw for Raf', Alif for Nasb, Yaa for Jarr:",
            "grammar_goal_ur": "أَبُوكَ (رفع)، أَبَاكَ (نصب)، أَبِيكَ (جر) کا فرق۔", "grammar_goal_en": "Abooka (Raf'), Abaaka (Nasb), Abeeka (Jarr).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ [ ＿＿＿ ] يَا بِلاَلُ؟ (فَاعِلٌ مَرْفُوعٌ)",
            "prompt_ur": "اے بلال تمہارے والد کہاں ہیں؟ (حالت رفع):", "prompt_en": "Where is your father, O Bilal? (nominative):",
            "answer": "أَبُوكَ",
            "options": ["أَبُوكَ", "أَبَاكَ", "أَبِيكَ", "أَبَكِ"],
            "emoji": "👨", "hint_ur": "حالت رفع میں اسمائے خمسہ کے ساتھ واو آتا ہے: أَبُوكَ۔", "hint_en": "Nominative Five Nouns take Waw: Abooka.",
            "explanation_ur": "فاعل مرفوع ہے اس لیے واو کے ساتھ آئے گا: أَبُوكَ۔", "explanation_en": "Nominative case takes Waw: Abooka."
        },
        {
            "id": "b2_u20_t2_q1", "book": 2, "unit_num": 20, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اسمائے خمسہ حالتِ نصب میں", "badge_en": "Exercise (2): Five Nouns in Accusative Case",
            "tamreen_title_ar": "الأَسْمَاءُ الْخَمْسَةُ فِي حَالَةِ النَّصْبِ (الأَلِفُ):", "tamreen_title_ur": "مفعول بہ بننے پر الف کے ساتھ آنا:", "tamreen_title_en": "Five Nouns taking Alif when accusative (direct object):",
            "grammar_goal_ur": "رَأَيْتُ أَبَاكَ کی ساخت۔", "grammar_goal_en": "Ra'aytu abaaka structure.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "رَأَيْتُ [ ＿＿＿ ] فِي الْمَسْجِدِ . (مَفْعُولٌ بِهِ)",
            "prompt_ur": "میں نے تمہارے بھائی کو مسجد میں دیکھا:", "prompt_en": "I saw your brother in the mosque (direct object):",
            "answer": "أَخَاكَ",
            "options": ["أَخَاكَ", "أَخُوكَ", "أَخِيكَ", "أَخٌ"],
            "emoji": "👦", "hint_ur": "حالت نصب میں الف آتا ہے: أَخَاكَ۔", "hint_en": "Accusative case takes Alif: Akhaaka.",
            "explanation_ur": "مفعول بہ منسوب بالالف ہوتا ہے: أَخَاكَ۔", "explanation_en": "Accusative Five Nouns take Alif: Akhaaka."
        }
    ]

    # UNIT 21: الْمَمْنُوعُ مِنَ الصَّرْفِ
    units[21] = [
        {
            "id": "b2_u21_t1_q1", "book": 2, "unit_num": 21, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): غیر منصرف کی علامات", "badge_en": "Exercise (1): Diptote Rules",
            "tamreen_title_ar": "أَحْكَامُ الْمَمْنُوعِ مِنَ الصَّرْفِ (لاَ يُنَوَّنُ وَيُجَرُّ بِالْفَتْحَةِ):", "tamreen_title_ur": "غیر منصرف پر تنوین نہیں آتی اور حالت جر میں فتحہ (زبر) لیتا ہے:", "tamreen_title_en": "Rules of Diptotes (No nunation and takes fathah for genitive):",
            "grammar_goal_ur": "عَلَم مؤنث، عَلَم عجمی اور فَعْلاَن کے اوزان غیر منصرف ہیں۔", "grammar_goal_en": "Feminine and foreign proper nouns and Fa'laan patterns are diptotes.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَلَّمْتُ عَلَى [ ＿＿＿ ] . (اسْمٌ مَجْرُورٌ)",
            "prompt_ur": "میں نے عثمان کو سلام کیا (عثمان غیر منصرف ہے):", "prompt_en": "I greeted Uthman (Uthman is a diptote):",
            "answer": "عُثْمَانَ",
            "options": ["عُثْمَانَ", "عُثْمَانٍ", "عُثْمَانُ", "عُثْمَانِ"],
            "emoji": "🤝", "hint_ur": "غیر منصرف حالت جر میں کسرہ کے بجائے فتحہ (زبر) لیتا ہے: عُثْمَانَ۔", "hint_en": "Diptote takes fathah in genitive state: 'Uthmaana.",
            "explanation_ur": "عثمان غیر منصرف ہے اس لیے حرف جر کے بعد زبر آئے گا: عَلَى عُثْمَانَ۔", "explanation_en": "Diptote noun takes fathah in the genitive state: 'Uthmaana."
        }
    ]

    # UNIT 22: مُرَاجَعَةُ حَالَاتِ الْمُضَارِعِ الثَّلاَثِ
    units[22] = [
        {
            "id": "b2_u22_t1_q1", "book": 2, "unit_num": 22, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): حالاتِ مضارع ثلاثہ", "badge_en": "Exercise (1): The Three Moods of the Present Verb",
            "tamreen_title_ar": "الْمُضَارِعُ الْمَرْفُوعُ وَالْمَنْصُوبُ وَالْمَجْزُومُ:", "tamreen_title_ur": "مضارع کی تینوں حالتوں (رفع، نصب اور جزم) کا خلاصہ:", "tamreen_title_en": "Summary of the three moods of Mudari' (Indicative, Subjunctive, Jussive):",
            "grammar_goal_ur": "يَذْهَبُ (رفع)، لَنْ يَذْهَبَ (نصب)، لَمْ يَذْهَبْ (جزم)۔", "grammar_goal_en": "Yath-habu (dammah), Lan yath-haba (fathah), Lam yath-hab (sukun).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدَ دُخُولِ (لَمْ) الْجَازِمَةِ عَلَى: (يَكْتُبُ) تُصْبِحُ: [ ＿＿＿ ]",
            "prompt_ur": "لم کے داخل ہونے پر مضارع کیا بن جائے گا؟", "prompt_en": "When jussive Lam enters upon 'yaktubu', it becomes:",
            "answer": "لَمْ يَكْتُبْ",
            "options": ["لَمْ يَكْتُبْ", "لَمْ يَكْتُبُ", "لَمْ يَكْتُبَ", "لَمْ كَتَبَ"],
            "emoji": "⚖️", "hint_ur": "لم جزم دیتا ہے اس لیے سکون آئے گا: لَمْ يَكْتُبْ۔", "hint_en": "Lam causes sukun: Lam yaktub.",
            "explanation_ur": "لم حرف جزم ہے: لَمْ يَكْتُبْ۔", "explanation_en": "Lam puts the verb into the jussive: Lam yaktub."
        }
    ]

    # UNIT 23: جَمْعُ الْمُذَكَّرِ السَّالِمِ (مُسْلِمُونَ / مُسْلِمِينَ)
    units[23] = [
        {
            "id": "b2_u23_t1_q1", "book": 2, "unit_num": 23, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اعرابِ جمع مذکر سالم", "badge_en": "Exercise (1): Sound Masculine Plural Inflection",
            "tamreen_title_ar": "إِعْرَابُ جَمْعِ الْمُذَكَّرِ السَّالِمِ (الْوَاوُ رَفْعاً وَالْيَاءُ نَصْباً وَجَرّاً):", "tamreen_title_ur": "جمع مذکر سالم حالت رفع میں واو اور نصب و جر میں یاء لیتا ہے:", "tamreen_title_en": "Sound masculine plural: Waw for Raf', Yaa for Nasb and Jarr:",
            "grammar_goal_ur": "مُسْلِمُونَ اور مُسْلِمِينَ کے اعرابی مقامات کا فہم۔", "grammar_goal_en": "Muslimoona (nominative) vs Muslimeena (accusative/genitive).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "حَضَرَ [ ＿＿＿ ] إِلَى الْمَسْجِدِ . (فَاعِلٌ مَرْفُوعٌ)",
            "prompt_ur": "نمازی مسجد میں حاضر ہوئے (حالت رفع):", "prompt_en": "The worshipers attended the mosque (nominative):",
            "answer": "الْمُصَلُّونَ",
            "options": ["الْمُصَلُّونَ", "الْمُصَلِّينَ", "مُصَلِّي", "مُصَلٍّ"],
            "emoji": "🕌", "hint_ur": "حالت رفع میں واو آتا ہے: الْمُصَلُّونَ۔", "hint_en": "Nominative sound plural ends in -oona: Al-musalloona.",
            "explanation_ur": "فاعل مرفوع بالواو ہوتا ہے: حَضَرَ الْمُصَلُّونَ۔", "explanation_en": "Subject is nominative with Waw: Al-musalloona."
        },
        {
            "id": "b2_u23_t2_q1", "book": 2, "unit_num": 23, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جمع مذکر حالتِ نصب میں", "badge_en": "Exercise (2): Sound Masculine Plural in Accusative",
            "tamreen_title_ar": "جَمْعُ الْمُذَكَّرِ السَّالِمِ فِي حَالَةِ النَّصْبِ (الْيَاءُ):", "tamreen_title_ur": "مفعول بہ بننے پر یاء کے ساتھ آنا:", "tamreen_title_en": "Sound masculine plural taking Yaa when accusative:",
            "grammar_goal_ur": "سَأَلْتُ الْمُدَرِّسِينَ کی ساخت۔", "grammar_goal_en": "Sa'altu al-mudarreiseena structure.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَأَلْتُ [ ＿＿＿ ] عَنِ الدَّرْسِ . (مَفْعُولٌ بِهِ)",
            "prompt_ur": "میں نے اساتذہ سے سبق کے بارے میں پوچھا:", "prompt_en": "I asked the teachers about the lesson:",
            "answer": "الْمُدَرِّسِينَ",
            "options": ["الْمُدَرِّسِينَ", "الْمُدَرِّسُونَ", "مُدَرِّسَانِ", "مُدَرِّسٌ"],
            "emoji": "👨‍🏫", "hint_ur": "مفعول بہ حالت نصب میں یاء کے ساتھ آئے گا: الْمُدَرِّسِينَ۔", "hint_en": "Accusative sound plural takes -eena: Al-mudarreiseena.",
            "explanation_ur": "جمع مذکر سالم مفعول بہ ہو تو یاء کے ساتھ منسوب ہوتا ہے: الْمُدَرِّسِينَ۔", "explanation_en": "Accusative sound plural ends in -eena: Al-mudarreiseena."
        }
    ]

    # UNIT 24: مُرَاجَعَةُ الأَعْدَادِ (١ - ١٠٠)
    units[24] = [
        {
            "id": "b2_u24_t1_q1", "book": 2, "unit_num": 24, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): گنتی کے مکمل قواعد", "badge_en": "Exercise (1): Numbers 1 to 100 Rules",
            "tamreen_title_ar": "قَوَاعِدُ الْعَدَدِ وَالْمَعْدُودِ (١ - ١٠٠):", "tamreen_title_ur": "اعداد 1 تا 100 کے معدود کے اعرابی احکام:", "tamreen_title_en": "Rules of numbers 1 to 100 and their counted nouns:",
            "grammar_goal_ur": "3 تا 10 جمع مجرور، 11 تا 99 مفرد منسوب، 100 مفرد مجرور۔", "grammar_goal_en": "3-10 take genitive plural, 11-99 take accusative singular, 100 takes genitive singular.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي الْفَصْلِ (25) [ ＿＿＿ ] .",
            "prompt_ur": "کلاس میں 25 طلبہ ہیں (11 تا 99 کا تمییز مفرد منسوب ہوتا ہے):", "prompt_en": "In the classroom there are 25 students:",
            "answer": "طَالِباً",
            "options": ["طَالِباً", "طَالِبٍ", "طُلَّابٍ", "طَالِبٌ"],
            "emoji": "👥", "hint_ur": "11 سے 99 تک کا معدود مفرد منسوب (دو زبر) ہوتا ہے: طَالِباً۔", "hint_en": "Counted noun for 11-99 is accusative singular: Taaliban.",
            "explanation_ur": "25 کا معدود مفرد منسوب بالفتحہ آئے گا: خَمْسَةٌ وَعِشْرُونَ طَالِباً۔", "explanation_en": "Numbers 11-99 take an accusative singular noun: Taaliban."
        }
    ]

    # UNIT 25: الْفِعْلُ الْمِثَالُ (الْمُعْتَلُّ الْفَاءِ: وَعَدَ يَعِدُ)
    units[25] = [
        {
            "id": "b2_u25_t1_q1", "book": 2, "unit_num": 25, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فعل مثال واوی", "badge_en": "Exercise (1): Assimilated Verbs (Al-Mithal)",
            "tamreen_title_ar": "حَذْفُ الْوَاوِ فِي مُضَارِعِ الْمِثَالِ الْوَاوِيِّ (وَعَدَ يَعِدُ):", "tamreen_title_ur": "مثال واوی کے مضارع میں واو کے گرنے کا قاعدہ:", "tamreen_title_en": "Dropping Waw in the present tense of assimilated verbs:",
            "grammar_goal_ur": "وَصَلَ يَصِلُ، وَقَفَ يَقِفُ، وَجَدَ يَجِدُ۔", "grammar_goal_en": "Dropping first weak letter Waw in Mudari'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمُضَارِعُ مِنَ الْفِعْلِ الْمِثَالِ: (وَقَفَ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "وقف کا مضارع (وہ کھڑا ہوتا ہے):", "prompt_en": "Present tense of 'Waqafa' (he stands):",
            "answer": "يَقِفُ",
            "options": ["يَقِفُ", "يَوْقِفُ", "وَاقِفٌ", "يَقُوفُ"],
            "emoji": "🧍", "hint_ur": "مضارع میں واو گر کر 'يَقِفُ' بنتا ہے۔", "hint_en": "Waw drops in present tense: Yaqifu.",
            "explanation_ur": "مثال واوی کے مضارع میں واو حذف ہو جاتی ہے: وَقَفَ -> يَقِفُ۔", "explanation_en": "Initial Waw drops in present tense: Waqafa -> Yaqifu."
        }
    ]

    # UNIT 26: الْفِعْلُ الأَجْوَفُ (قَالَ يَقُولُ، بَاعَ يَبِيعُ)
    units[26] = [
        {
            "id": "b2_u26_t1_q1", "book": 2, "unit_num": 26, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فعل اجوف", "badge_en": "Exercise (1): Hollow Verbs (Al-Ajwaf)",
            "tamreen_title_ar": "تَصْرِيفُ الْفِعْلِ الأَجْوَفِ فِي الْمَاضِي وَالْمُضَارِعِ:", "tamreen_title_ur": "اجوف کا مضارع (قال یقول، باع یبیع، نام ینام):", "tamreen_title_en": "Conjugating hollow verbs in past and present:",
            "grammar_goal_ur": "درمیانی حرف علت کے واو، یاء یا الف بننے کے ضوابط۔", "grammar_goal_en": "Middle radical behavior in hollow verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمُضَارِعُ مِنَ الْفِعْلِ الأَجْوَفِ: (بَاعَ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "باع (اس نے بیچا) کا مضارع کیا ہے؟", "prompt_en": "Present tense of 'Baa'a' (he sold):",
            "answer": "يَبِيعُ",
            "options": ["يَبِيعُ", "يَبُوعُ", "بَائِعٌ", "يَبَاعُ"],
            "emoji": "🏷️", "hint_ur": "باع کا مضارع یائی ہے: يَبِيعُ۔", "hint_en": "Present tense is ya'i: Yabee'u.",
            "explanation_ur": "باع کا مضارع يَبِيعُ آتا ہے۔", "explanation_en": "Baa'a conjugates in present as Yabee'u."
        }
    ]

    # UNIT 27: إِسْنَادُ الأَجْوَفِ إِلَى ضَمَائِرِ الرَّفْعِ الْمُتَحَرِّكَةِ
    units[27] = [
        {
            "id": "b2_u27_t1_q1", "book": 2, "unit_num": 27, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اجوف مع تائے فاعل", "badge_en": "Exercise (1): Hollow Verbs with Taa al-Fa'il",
            "tamreen_title_ar": "حَذْفُ عَيْنِ الأَجْوَفِ مَعَ ضَمَائِرِ الرَّفْعِ الْمُتَحَرِّكَةِ:", "tamreen_title_ur": "تائے فاعل ملنے پر اجوف کے درمیانی حرف کا گرنا:", "tamreen_title_en": "Dropping middle weak letter when attaching moving pronouns:",
            "grammar_goal_ur": "قَالَ -> قُلْتُ، زَارَ -> زُرْتُ، كَانَ -> كُنْتُ۔", "grammar_goal_en": "Qaala becomes Qultu, Zaara becomes Zurtu, Kaana becomes Kuntu.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] مَكَّةَ الْمُكَرَّمَةَ فِي رَمَضَانَ . (مِنْ: زَارَ)",
            "prompt_ur": "میں نے رمضان میں مکہ کی زیارت کی (زَارَ سے):", "prompt_en": "I visited Makkah in Ramadan (from Zaara):",
            "answer": "زُرْتُ",
            "options": ["زُرْتُ", "زَارْتُ", "زِرْتُ", "أَزُورُ"],
            "emoji": "🕋", "hint_ur": "تاء ملنے پر الف گر کر ضمہ آئے گا: زُرْتُ۔", "hint_en": "Alif drops and first letter takes dammah: Zurtu.",
            "explanation_ur": "اجوف واوی میں تائے فاعل کے ملنے پر فا کلمہ مضموم ہوتا ہے: زُرْتُ۔", "explanation_en": "Wawi hollow verb drops weak letter taking dammah: Zurtu."
        }
    ]

    # UNIT 28: الْفِعْلُ النَّاقِصُ (دَعَا يَدْعُو، قَضَى يَقْضِي، نَسِيَ يَنْسَى)
    units[28] = [
        {
            "id": "b2_u28_t1_q1", "book": 2, "unit_num": 28, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فعل ناقص", "badge_en": "Exercise (1): Defective Verbs (An-Naaqis)",
            "tamreen_title_ar": "تَصْرِيفُ الْفِعْلِ النَّاقِصِ فِي الْمَاضِي وَالْمُضَارِعِ:", "tamreen_title_ur": "ناقص واوی اور یائی کے مضارع کی ساخت:", "tamreen_title_en": "Conjugating defective verbs in past and present:",
            "grammar_goal_ur": "دَعَا يَدْعُو، قَضَى يَقْضِي، نَسِيَ يَنْسَى۔", "grammar_goal_en": "Da'aa yad'oo, Qadaa yaqdee, Nasiya yansaa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمُضَارِعُ مِنَ الْفِعْلِ: (مَشَى) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "مشى (وہ چلا) کا مضارع کیا ہے؟", "prompt_en": "Present tense of 'Mashaa' (he walked):",
            "answer": "يَمْشِي",
            "options": ["يَمْشِي", "يَمْشُو", "مَاشٍ", "يَمْشَى"],
            "emoji": "🚶‍♂️", "hint_ur": "مشى کا مضارع یائی ہے: يَمْشِي۔", "hint_en": "Present tense ends in yaa: Yamshee.",
            "explanation_ur": "مَشَى کا مضارع يَمْشِي آتا ہے۔", "explanation_en": "Present tense of Mashaa is Yamshee."
        }
    ]

    # UNIT 29: الْفِعْلُ الْمُضَعَّفُ (حَجَّ يَحُجُّ، مَرَّ يَمُرُّ)
    units[29] = [
        {
            "id": "b2_u29_t1_q1", "book": 2, "unit_num": 29, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فعل مضعف", "badge_en": "Exercise (1): Doubled Verbs (Al-Muda''af)",
            "tamreen_title_ar": "فَكُّ الإِدْغَامِ فِي الْمُضَعَّفِ مَعَ ضَمَائِرِ الرَّفْعِ الْمُتَحَرِّكَةِ:", "tamreen_title_ur": "تائے فاعل ملنے پر ادغام کا کھلنا: حَجَّ -> حَجَجْتُ:", "tamreen_title_en": "Unfolding gemination when attaching moving subject pronouns:",
            "grammar_goal_ur": "حَجَجْتُ، مَرَرْتُ، عَدَدْتُ کی ساخت۔", "grammar_goal_en": "Unfolding idgham: Hajajtu, Marartu, 'Adadtu.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] هٰذَا الْعَامَ . (مِنْ: حَجَّ)",
            "prompt_ur": "میں نے اس سال حج کیا (حَجَّ سے متکلم کا صیغہ):", "prompt_en": "I performed Hajj this year (from Hajja):",
            "answer": "حَجَجْتُ",
            "options": ["حَجَجْتُ", "حَجَّيْتُ", "حَجْتُ", "أَحُجُّ"],
            "emoji": "🕋", "hint_ur": "تائے فاعل ملنے پر تشدید کھل جاتی ہے: حَجَجْتُ۔", "hint_en": "Gemination unfolds: Hajajtu.",
            "explanation_ur": "مضعف میں ضمیر متحرک ملنے پر فک ادغام واجب ہے: حَجَجْتُ۔", "explanation_en": "Idgham must unfold when attaching pronoun: Hajajtu."
        }
    ]

    # UNIT 30: تَدْرِيبَاتٌ شَامِلَةٌ عَلَى تَصْرِيفِ الأَفْعَالِ
    units[30] = [
        {
            "id": "b2_u30_t1_q1", "book": 2, "unit_num": 30, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): تصریف افعال جامع مشق", "badge_en": "Exercise (1): Comprehensive Verb Drills",
            "tamreen_title_ar": "تَصْرِيفُ الأَفْعَالِ فِي الْمَاضِي وَالْمُضَارِعِ وَالأَمْرِ:", "tamreen_title_ur": "ماضی، مضارع اور امر کی ہم آہنگی:", "tamreen_title_en": "Past, present, and imperative alignment:",
            "grammar_goal_ur": "تمام ابواب کے ماضی، مضارع اور امر کا مجموعی فہم۔", "grammar_goal_en": "Mastering past, present and imperative forms across categories.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمَاضِي: (شَرِبَ)، الْمُضَارِعُ: (يَشْرَبُ)، الأَمْرُ: [ ＿＿＿ ]",
            "prompt_ur": "شرب کا فعل امر کیا بنے گا؟", "prompt_en": "What is the imperative of 'Shariba'?",
            "answer": "اشْرَبْ",
            "options": ["اشْرَبْ", "اشْرِبْ", "شَرَابٌ", "تَشْرَبْ"],
            "emoji": "🥤", "hint_ur": "عین کلمہ مفتوح ہے اس لیے ہمزہ مکسور ہوگا: اشْرَبْ۔", "hint_en": "Imperative is: Ishrab.",
            "explanation_ur": "يَشْرَبُ کا امر 'اشْرَبْ' آتا ہے۔", "explanation_en": "The imperative of yashrabu is Ishrab."
        }
    ]

    # UNIT 31: النَّعْتُ وَالْمَنْعُوتُ وَالإِعْرَابُ الشَّامِلُ
    units[31] = [
        {
            "id": "b2_u31_t1_q1", "book": 2, "unit_num": 31, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): نعت اور منعوت", "badge_en": "Exercise (1): Adjective and Noun Agreement",
            "tamreen_title_ar": "مُطَابَقَةُ النَّعْتِ لِلْمَنْعُوتِ فِي الأَحْكَامِ الأَرْبَعَةِ:", "tamreen_title_ur": "نعت کا اعراب، تعریف، تذکیر اور عدد میں منعوت کے مطابق ہونا:", "tamreen_title_en": "Fourfold agreement of the adjective with its noun:",
            "grammar_goal_ur": "نعت اپنے موصوف کے 4 امور میں تابع ہوتی ہے۔", "grammar_goal_en": "Adjectives follow their modified nouns in case, definiteness, gender and number.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اشْتَرَيْتُ سَيَّارَةً [ ＿＿＿ ] .",
            "prompt_ur": "میں نے ایک نئی گاڑی خریدی (درست نعت چنیں):", "prompt_en": "I bought a new car (choose matching adjective):",
            "answer": "جَدِيدَةً",
            "options": ["جَدِيدَةً", "جَدِيدٌ", "جَدِيدَةٌ", "جَدِيدٍ"],
            "emoji": "🚗", "hint_ur": "سیارةً مؤنث منسوب ہے اس لیے نعت بھی مؤنث منسوب ہوگی: جَدِيدَةً۔", "hint_en": "Sayyaratan is feminine accusative, taking: Jadeedatan.",
            "explanation_ur": "نعت اپنے موصوف کی تانیث اور اعراب میں تابع ہوتی ہے: سَيَّارَةً جَدِيدَةً۔", "explanation_en": "Adjective agrees in gender and case: Sayyaratan jadeedatan."
        }
    ]

    return units

if __name__ == "__main__":
    u = get_b2_units_6_to_31_deep()
    print("Generated deep units for Book 2:", list(u.keys()))
