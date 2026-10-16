import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_b2_part2():
    units = {}
    
    # -------------------------------------------------------------
    # UNIT 6: إِسْنَادُ الْفِعْلِ الْمَاضِي إِلَى الضَّمَائِرِ (الْغَائِبُ وَالْمُخَاطَبُ وَالْمُتَكَلِّمُ)
    # -------------------------------------------------------------
    units[6] = [
        {
            "id": "b2_u6_q1", "book": 2, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): فہمِ متن (صحیح یا غلط)", "badge_en": "Exercise (2): Text Comprehension",
            "tamreen_title_ar": "ضَعْ هٰذِهِ الْعَلَامَةَ (✓) أَمَامَ الصَّحِيحَةِ وَ (✗) أَمَامَ غَيْرِ الصَّحِيحَةِ:",
            "tamreen_title_ur": "صحیح جملے کے آگے (✓) اور غلط کے آگے (✗) لگائیں:",
            "tamreen_title_en": "Mark true (✓) or false (✗) based on the lesson:",
            "grammar_goal_ur": "عربی جملوں کا فہم اور فعل و فاعل کا ربط۔", "grammar_goal_en": "Sentence comprehension and subject-verb agreement.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَرْيَمُ جَوْعَى . [ ＿＿＿ ]", "prompt_ur": "سبق کے مطابق: 'مریم بھوکی ہے' صحیح ہے یا غلط؟", "prompt_en": "According to the lesson: 'Maryam is hungry' - True or False?",
            "answer": "صَحِيحٌ (✓)", "options": ["صَحِيحٌ (✓)", "خَطَأٌ (✗)"],
            "emoji": "👧", "hint_ur": "یہ جملہ درست ہے۔", "hint_en": "This statement is correct.",
            "explanation_ur": "درست جواب: 'صَحِيحٌ (✓)' (سبق میں مریم نے کہا تھا: أنا جوعى)",
            "explanation_en": "Correct: 'صَحِيحٌ (✓)' (Maryam said she was hungry in the lesson)"
        },
        {
            "id": "b2_u6_q2", "book": 2, "unit_num": 6, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): فاعل کی تانیث (تائے تانیث ساکنہ)", "badge_en": "Exercise (4): Feminine Subject Agreement",
            "tamreen_title_ar": "أَنِّثِ الْفَاعِلَ فِي كُلٍّ مِنَ الْجُمَلِ الآتِيَةِ:",
            "tamreen_title_ur": "درج ذیل جملوں میں فاعل کو مؤنث بنائیں:",
            "tamreen_title_en": "Make the subject feminine by attaching taa ta'neeth to the verb:",
            "grammar_goal_ur": "مؤنث فاعل کے ساتھ ماضی کے آخر میں تائے تانیث ساکنہ (تْ) کا اضافہ۔", "grammar_goal_en": "Attaching silent taa (تْ) to past verb for feminine singular subject.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "شَرِبَ مُحَمَّدٌ الْمَاءَ ➔ شَرِبَتْ آمِنَةُ [ ＿＿＿ ] .",
            "prompt_ur": "آمِنَةُ کے لیے درست مفعول منتخب کریں:",
            "prompt_en": "Select the correct object for Aminah:",
            "answer": "الْمَاءَ", "options": ["الْمَاءَ", "الْمَاءُ", "الْمَاءِ", "مَاءٌ"],
            "emoji": "🥛", "hint_ur": "آمنہ نے پانی پیا۔", "hint_en": "Aminah drank the water.",
            "explanation_ur": "درست جواب: 'الْمَاءَ' (شَرِبَتْ میں فاعل مؤنث ہے اور الماء مفعول بہ منسوب ہے)",
            "explanation_en": "Correct: 'الْمَاءَ' (Direct object takes accusative fathah)"
        },
        {
            "id": "b2_u6_q3", "book": 2, "unit_num": 6, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): الْتِقَاءُ السَّاكِنَيْنِ عند تاء التأنيث", "badge_en": "Exercise (5): Resolving Two Saakins on Feminine Taa",
            "tamreen_title_ar": "تَأَمَّلْ مَا يَلِي عِنْدَ الْتِقَاءِ السَّاكِنَيْنِ:",
            "tamreen_title_ur": "دو ساکن ملنے پر تاء تانیث کے کسرہ کی مشق کریں:",
            "tamreen_title_en": "Vowel the feminine taa with kasrah when followed by hamzatul-wasl:",
            "grammar_goal_ur": "ساکن کے بعد الف لام آنے پر تاء تانیث پر زیر دی جاتی ہے (شَرِبَتِ الْبِنْتُ)۔", "grammar_goal_en": "Feminine taa takes kasrah before hamzatul-wasl to avoid two saakins.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "خَرَجَتْ + الْبِنْتُ ➔ [ ＿＿＿ ] الْبِنْتُ .",
            "prompt_ur": "خَرَجَتْ کو الْبِنْتُ سے ملاتے وقت درست شکل منتخب کریں:",
            "prompt_en": "Select the correctly voweled form joining 'خَرَجَتْ' with 'الْبِنْتُ':",
            "answer": "خَرَجَتِ", "options": ["خَرَجَتِ", "خَرَجَتُ", "خَرَجَتَ", "خَرَجَتْ"],
            "emoji": "👧", "hint_ur": "لڑکی نکلی (دو ساکن ملنے پر زیر آتی ہے)۔", "hint_en": "The girl went out.",
            "explanation_ur": "درست جواب: 'خَرَجَتِ' (التقاء ساکنین کی وجہ سے تاء کو زیر دی جاتی ہے)",
            "explanation_en": "Correct: 'خَرَجَتِ' (Takes kasrah to avoid two adjacent sukoons)"
        },
        {
            "id": "b2_u6_q4", "book": 2, "unit_num": 6, "tamreen_num": 7,
            "badge_ar": "التَّمْرِينُ (7)", "badge_ur": "مشق (7): ماضی کے ساتھ نونِ نسوہ (جماعت مؤنث)", "badge_en": "Exercise (7): Past Verb with Noon of Feminine Plural",
            "tamreen_title_ar": "أَسْنِدِ الْفِعْلَ الْمَاضِيَ إِلَى نُونِ النِّسْوَةِ:",
            "tamreen_title_ur": "فعل ماضی کو نونِ نسوہ کے ساتھ جوڑیں:",
            "tamreen_title_en": "Conjugate the past verb with noon of feminine plural:",
            "grammar_goal_ur": "جمع مؤنث غائب میں فعل کے لام کلمہ کو ساکن کر کے نونِ مفتوح ملائی جاتی ہے (ذَهَبْنَ)۔", "grammar_goal_en": "Feminine plural 3rd person past verb takes sukoon on root + na (ذَهَبْنَ).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطَّالِبَاتُ [ ＿＿＿ ] إِلَى الْمَكْتَبَةِ .",
            "prompt_ur": "طالبات (جمع مؤنث) کے لیے درست فعل منتخب کریں:",
            "prompt_en": "Select the correct verb form for 'الطَّالِبَاتُ':",
            "answer": "ذَهَبْنَ", "options": ["ذَهَبْنَ", "ذَهَبُوا", "ذَهَبَتْ", "ذَهَبَتَا"],
            "emoji": "👩‍🎓", "hint_ur": "طالبات لائبریری گئیں۔", "hint_en": "The female students went to the library.",
            "explanation_ur": "درست جواب: 'ذَهَبْنَ' (جمع مؤنث غائب کے لیے ذَهَبْنَ آتا ہے)",
            "explanation_en": "Correct: 'ذَهَبْنَ' (3rd person feminine plural past verb)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 7: إِسْنَادُ الْمَاضِي إِلَى ضَمَائِرِ الْمُخَاطَبِ (أَنْتَ، أَنْتُمْ، أَنْتِ، أَنْتُنَّ)
    # -------------------------------------------------------------
    units[7] = [
        {
            "id": "b2_u7_q1", "book": 2, "unit_num": 7, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تائے خطاب للمفرد المؤنث (تِ)", "badge_en": "Exercise (2): 2nd Person Feminine Singular (تِ)",
            "tamreen_title_ar": "أَسْنِدِ الْفِعْلَ إِلَى ضَمِيرِ الْمُخَاطَبَةِ (أَنْتِ):",
            "tamreen_title_ur": "فعل کو مؤنث مخاطب کی ضمیر (أنتِ) کے ساتھ لائیں:",
            "tamreen_title_en": "Conjugate past verb for 2nd person feminine singular (أَنْتِ):",
            "grammar_goal_ur": "مؤنث مخاطب کے لیے تائے مکسورہ (تِ) کا استعمال (أَكَلْتِ، غَسَلْتِ)۔", "grammar_goal_en": "Using suffix -ti for 2nd person feminine singular past tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا سُعَادُ، أَ [ ＿＿＿ ] الْقَمِيصَ؟",
            "prompt_ur": "سُعاد سے قمیص دھونے کا پوچھنے کے لیے درست صیغہ منتخب کریں:",
            "prompt_en": "Select the correct verb form addressing Su'ad:",
            "answer": "غَسَلْتِ", "options": ["غَسَلْتِ", "غَسَلْتَ", "غَسَلْتُ", "غَسَلَتْ"],
            "emoji": "👕", "hint_ur": "اے سعاد، کیا تم نے قمیص دھوئی؟", "hint_en": "O Su'ad, did you wash the shirt?",
            "explanation_ur": "درست جواب: 'غَسَلْتِ' (مؤنث مخاطب کے لیے تاء کے نیچے زیر آتی ہے)",
            "explanation_en": "Correct: 'غَسَلْتِ' (Addressing feminine singular takes -ti)"
        },
        {
            "id": "b2_u7_q2", "book": 2, "unit_num": 7, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): جمع مؤنث مخاطب (أَنْتُنَّ -> تُنَّ)", "badge_en": "Exercise (4): 2nd Person Feminine Plural (-tunna)",
            "tamreen_title_ar": "أَسْنِدِ الْفِعْلَ إِلَى ضَمِيرِ جَمْعِ الْمُؤَنَّثِ الْمُخَاطَبِ (أَنْتُنَّ):",
            "tamreen_title_ur": "فعل کو جمع مؤنث مخاطب کے صیغے میں لائیں:",
            "tamreen_title_en": "Conjugate past verb for 2nd person feminine plural (أَنْتُنَّ):",
            "grammar_goal_ur": "جمع مؤنث مخاطب کے لیے ضمیر 'تُنَّ' کا لاحقہ لگتا ہے۔", "grammar_goal_en": "Using suffix -tunna for 2nd person feminine plural past verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ [ ＿＿＿ ] يَا أَخَوَاتُ بَعْدَ الدَّرْسِ؟",
            "prompt_ur": "بہنوں (جمع مؤنث) سے پوچھنے کے لیے درست فعل منتخب کریں:",
            "prompt_en": "Select the correct verb form addressing sisters (plural):",
            "answer": "ذَهَبْتُنَّ", "options": ["ذَهَبْتُنَّ", "ذَهَبْتُمْ", "ذَهَبْنَ", "ذَهَبْتِ"],
            "emoji": "🧕", "hint_ur": "اے بہنو، تم سب سبق کے بعد کہاں گئیں؟", "hint_en": "Where did you (all females) go after class, sisters?",
            "explanation_ur": "درست جواب: 'ذَهَبْتُنَّ' (أنتن کے ساتھ ذَهَبْتُنَّ آتا ہے)",
            "explanation_en": "Correct: 'ذَهَبْتُنَّ' (2nd person feminine plural suffix is -tunna)"
        },
        {
            "id": "b2_u7_q3", "book": 2, "unit_num": 7, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): ضمیرِ متکلم مع الغیر (نَحْنُ -> نَا)", "badge_en": "Exercise (6): 1st Person Plural (-naa)",
            "tamreen_title_ar": "أَسْنِدِ الْفِعْلَ إِلَى ضَمِيرِ الْمُتَكَلِّمِينَ (نَحْنُ):",
            "tamreen_title_ur": "فعل کو ضمیر 'نحن' کے ساتھ جوڑیں:",
            "tamreen_title_en": "Conjugate past verb with 1st person plural (نَحْنُ):",
            "grammar_goal_ur": "ماضی میں متکلم مع الغیر کے لیے 'نَا' لگتا ہے اور لام کلمہ ساکن ہوتا ہے (لَعِبْنَا)۔", "grammar_goal_en": "1st person plural past verb takes suffix -naa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَحْنُ [ ＿＿＿ ] كُرَةَ الْقَدَمِ الْيَوْمَ .",
            "prompt_ur": "نَحْنُ کے ساتھ درست فعل منتخب کریں:",
            "prompt_en": "Select the correct verb form for 'نَحْنُ':",
            "answer": "لَعِبْنَا", "options": ["لَعِبْنَا", "لَعِبْتُمْ", "لَعِبُوا", "لَعِبْتُ"],
            "emoji": "⚽", "hint_ur": "ہم نے آج فٹ بال کھیلا۔", "hint_en": "We played soccer today.",
            "explanation_ur": "درست جواب: 'لَعِبْنَا' (نحن کے ساتھ لَعِبْنَا آتا ہے)",
            "explanation_en": "Correct: 'لَعِبْنَا' (1st person plural past suffix is -naa)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 8: ضَمَائِرُ النَّصْبِ الْمُتَّصِلَةُ بِالْفِعْلِ (ـهُ، ـهَا، ـهُمْ، ـكَ، ـكِ، ـنِي، ـنَا)
    # -------------------------------------------------------------
    units[8] = [
        {
            "id": "b2_u8_q1", "book": 2, "unit_num": 8, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مفعول بہ کی ضمیر (ـهُ / ـهَا)", "badge_en": "Exercise (2): Attached Object Pronouns (-hu / -haa)",
            "tamreen_title_ar": "عَيِّنِ الْمَفْعُولَ بِهِ الْمُتَّصِلَ بِالْفِعْلِ:",
            "tamreen_title_ur": "فعل کے ساتھ متصل مفعول بہ کی درست ضمیر لگائیں:",
            "tamreen_title_en": "Attach the correct accusative pronoun to the verb:",
            "grammar_goal_ur": "مذکر غائب مفعول بہ کے لیے ضمیر 'ـهُ' اور مؤنث کے لیے 'ـهَا' آتی ہے۔", "grammar_goal_en": "Using -hu for masculine and -haa for feminine singular direct object pronoun.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ الْكِتَابُ؟ أَ [ ＿＿＿ ] يَا عَلِيُّ؟",
            "prompt_ur": "کتاب (مذکر) کے بارے میں پوچھنے کے لیے درست فعل و ضمیر منتخب کریں:",
            "prompt_en": "Select the correct verb with attached pronoun referring to the book:",
            "answer": "رَأَيْتَهُ", "options": ["رَأَيْتَهُ", "رَأَيْتَهَا", "رَأَيْتَهُمْ", "رَأَيْتَكَ"],
            "emoji": "📖", "hint_ur": "کتاب کہاں ہے؟ کیا تم نے اسے دیکھا ہے اے علی؟", "hint_en": "Where is the book? Did you see it, O Ali?",
            "explanation_ur": "درست جواب: 'رَأَيْتَهُ' (الکتاب چونکہ مذکر ہے اس لیے ضمیر ـهُ آئے گی)",
            "explanation_en": "Correct: 'رَأَيْتَهُ' (Masculine singular object pronoun is -hu)"
        },
        {
            "id": "b2_u8_q2", "book": 2, "unit_num": 8, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مفعول بہ مؤنث کی ضمیر (ـهَا)", "badge_en": "Exercise (3): Feminine Attached Object Pronoun (-haa)",
            "tamreen_title_ar": "صِلِ الْفِعْلَ بِضَمِيرِ الْمَفْعُولِ بِهِ الْمُؤَنَّثِ:",
            "tamreen_title_ur": "مؤنث اسم کے لیے فعل کو درست مفعولی ضمیر سے جوڑیں:",
            "tamreen_title_en": "Attach feminine object pronoun to the verb:",
            "grammar_goal_ur": "مؤنث غیر عاقل یا عاقل کے لیے مفعول کی ضمیر 'ـهَا' آتی ہے۔", "grammar_goal_en": "Attaching -haa for feminine object.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ السَّيَّارَةُ؟ [ ＿＿＿ ] أَمَامَ الْمَسْجِدِ .",
            "prompt_ur": "گاڑی (مؤنث) کو دیکھنے کے جواب میں درست جملہ منتخب کریں:",
            "prompt_en": "Select the correct answer referring to the car (feminine):",
            "answer": "رَأَيْتُهَا", "options": ["رَأَيْتُهَا", "رَأَيْتُهُ", "رَأَيْتُهُمْ", "رَأَيْتُكِ"],
            "emoji": "🚗", "hint_ur": "میں نے اسے مسجد کے سامنے دیکھا۔", "hint_en": "I saw it in front of the mosque.",
            "explanation_ur": "درست جواب: 'رَأَيْتُهَا' (السیارة مؤنث ہے اس لیے ضمیر ـهَا استعمال ہوگی)",
            "explanation_en": "Correct: 'رَأَيْتُهَا' (Car is feminine, takes object pronoun -haa)"
        },
        {
            "id": "b2_u8_q3", "book": 2, "unit_num": 8, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): نونِ وقایہ ضمیرِ متکلم کے ساتھ (ـنِي)", "badge_en": "Exercise (5): Noon of Protection with 1st Person (ـنِي)",
            "tamreen_title_ar": "أَسْنِدِ الْفِعْلَ إِلَى يَاءِ الْمُتَكَلِّمِ مَعَ نُونِ الْوِقَايَةِ:",
            "tamreen_title_ur": "فعل کو یائے متکلم سے ملاتے وقت نونِ وقایہ کی مشق کریں:",
            "tamreen_title_en": "Add noon al-wiqaayah when attaching 1st person object pronoun to verb:",
            "grammar_goal_ur": "فعل کو کسرہ سے بچانے کے لیے یائے متکلم سے پہلے نونِ وقایہ لانا واجب ہے (سَأَلَنِي)۔", "grammar_goal_en": "Noon of protection (noon al-wiqaayah) protects verb from taking kasrah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَأَلَ الْمُدَرِّسُ مُحَمَّداً وَ [ ＿＿＿ ] أَيْضاً .",
            "prompt_ur": "استاد نے مجھ سے بھی پوچھا، کے لیے درست لفظ منتخب کریں:",
            "prompt_en": "Select the correct verb form for 'and he asked me too':",
            "answer": "سَأَلَنِي", "options": ["سَأَلَنِي", "سَأَلِي", "سَأَلَنَا", "سَأَلْتُنِي"],
            "emoji": "👨‍🏫", "hint_ur": "استاد نے مجھ سے بھی پوچھا۔", "hint_en": "The teacher asked me too.",
            "explanation_ur": "درست جواب: 'سَأَلَنِي' (فعل کے ساتھ یائے متکلم ملاتے وقت نونِ وقایہ لائی جاتی ہے)",
            "explanation_en": "Correct: 'سَأَلَنِي' (Noon al-wiqaayah is required before yaa al-mutakallim)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 9: الْفَاعِلُ وَالْمَفْعُولُ بِهِ (الظَّاهِرُ وَالْمُضْمَرُ)
    # -------------------------------------------------------------
    units[9] = [
        {
            "id": "b2_u9_q1", "book": 2, "unit_num": 9, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): فاعل کا مرفوع اور مفعول بہ کا منصوب ہونا", "badge_en": "Exercise (2): Nominative Subject and Accusative Object",
            "tamreen_title_ar": "عَيِّنِ الْفَاعِلَ وَالْمَفْعُولَ بِهِ وَاضْبِطْ أَوَاخِرَهُمَا:",
            "tamreen_title_ur": "فاعل اور مفعول بہ کے آخری اعراب کو پہچانیں:",
            "tamreen_title_en": "Identify subject (marfoo') and object (mansoob):",
            "grammar_goal_ur": "فاعل ہمیشہ مرفوع (پیش) اور مفعول بہ ہمیشہ منصوب (زبر) ہوتا ہے۔", "grammar_goal_en": "Subject takes dammah; direct object takes fathah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَتَلَ الرَّجُلُ [ ＿＿＿ ] .",
            "prompt_ur": "درست مفعول بہ (منصوب) منتخب کریں:",
            "prompt_en": "Select the correct accusative direct object:",
            "answer": "الْحَيَّةَ", "options": ["الْحَيَّةَ", "الْحَيَّةُ", "الْحَيَّةِ", "حَيَّةٌ"],
            "emoji": "🐍", "hint_ur": "آدمی نے سانپ کو مار ڈالا۔", "hint_en": "The man killed the snake.",
            "explanation_ur": "درست جواب: 'الْحَيَّةَ' (مفعول بہ پر زبر آتی ہے)",
            "explanation_en": "Correct: 'الْحَيَّةَ' (Direct object takes fathah)"
        },
        {
            "id": "b2_u9_q2", "book": 2, "unit_num": 9, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): فاعل ضمیر مستتر", "badge_en": "Exercise (4): Hidden Pronoun Subject",
            "tamreen_title_ar": "حَدِّدْ نَوْعَ الْفَاعِلِ فِي الْجُمْلَةِ:",
            "tamreen_title_ur": "جملے میں فاعل کی قسم (ظاہر یا ضمیر مستتر) پہچانیں:",
            "tamreen_title_en": "Identify subject type (explicit noun or latent pronoun):",
            "grammar_goal_ur": "جب فاعل لفظوں میں مذکور نہ ہو تو وہ ضمیر مستتر ہوتا ہے۔", "grammar_goal_en": "When subject noun is absent, it is an implied/hidden pronoun.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ بِلَالٌ؟ - خَرَجَ قَبْلَ قَلِيلٍ . الْفَاعِلُ فِي (خَرَجَ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "فعل (خَرَجَ) میں فاعل کیا ہے؟",
            "prompt_en": "What is the subject of 'خَرَجَ' in this sentence?",
            "answer": "ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ (هُوَ)", "options": ["ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ (هُوَ)", "اسْمٌ ظَاهِرٌ", "قَبْلَ", "قَلِيلٍ"],
            "emoji": "🚶", "hint_ur": "بلال کہاں ہے؟ وہ کچھ دیر پہلے نکلا۔", "hint_en": "Where is Bilal? He left a short while ago.",
            "explanation_ur": "درست جواب: 'ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ (هُوَ)' (فاعل چھپی ہوئی ضمیر ہے جو بلال کی طرف لوٹتی ہے)",
            "explanation_en": "Correct: 'ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ (هُوَ)' (Hidden pronoun huwwa)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 10: كَانَ وَأَخَوَاتُهَا (اسْمُ كَانَ وَخَبَرُهَا)
    # -------------------------------------------------------------
    units[10] = [
        {
            "id": "b2_u10_q1", "book": 2, "unit_num": 10, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): (كَانَ) کا اسم اور خبر", "badge_en": "Exercise (2): Ism and Khabar of Kaana",
            "tamreen_title_ar": "أَدْخِلْ (كَانَ) عَلَى الْجُمَلِ الآتِيَةِ وَاضْبِطْ أَوَاخِرَهَا:",
            "tamreen_title_ur": "جملے پر 'كَانَ' داخل کریں اور اعراب درست کریں:",
            "tamreen_title_en": "Enter Kaana and apply correct endings (nominative ism, accusative khabar):",
            "grammar_goal_ur": "کان اپنے اسم کو پیش (رفع) اور اپنی خبر کو زبر (نصب) دیتا ہے۔", "grammar_goal_en": "Kaana makes its ism nominative and its khabar accusative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْمُدِيرُ فِي غُرْفَتِهِ ➔ كَانَ الْمُدِيرُ [ ＿＿＿ ] فِي غُرْفَتِهِ .",
            "prompt_ur": "كَانَ حَامِدٌ مَرِيضٌ کی صحیح شکل کیا ہے؟",
            "prompt_en": "What is the correct form when entering Kaana onto 'حَامِدٌ مَرِيضٌ'?",
            "answer": "كَانَ حَامِدٌ مَرِيضاً", "options": ["كَانَ حَامِدٌ مَرِيضاً", "كَانَ حَامِداً مَرِيضٌ", "كَانَ حَامِدٍ مَرِيضٍ", "كَانَ حَامِدٌ مَرِيضٌ"],
            "emoji": "🤒", "hint_ur": "حامد بیمار تھا۔", "hint_en": "Hamid was sick.",
            "explanation_ur": "درست جواب: 'كَانَ حَامِدٌ مَرِيضاً' (کان کا اسم مرفوع اور خبر منصوب ہوتی ہے)",
            "explanation_en": "Correct: 'كَانَ حَامِدٌ مَرِيضاً' (Kaana takes nominative subject + accusative predicate)"
        },
        {
            "id": "b2_u10_q2", "book": 2, "unit_num": 10, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): كَانَتْ للمؤنث", "badge_en": "Exercise (3): Kaana with Feminine Subject (كَانَتْ)",
            "tamreen_title_ar": "أَدْخِلْ (كَانَتْ) مَعَ الْفَاعِلِ الْمُؤَنَّثِ:",
            "tamreen_title_ur": "مؤنث اسم کے لیے 'كَانَتْ' داخل کریں:",
            "tamreen_title_en": "Enter Kaana with feminine subject (Kaanat):",
            "grammar_goal_ur": "مؤنث اسم کے ساتھ 'كَانَتْ' آتی ہے اور خبر منسوب رہتی ہے۔", "grammar_goal_en": "Feminine subject takes Kaanat with accusative predicate.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "آمِنَةُ طَالِبَةٌ ➔ [ ＿＿＿ ] آمِنَةُ طَالِبَةً .",
            "prompt_ur": "آمِنَةُ کے لیے درست فعلِ ناقص منتخب کریں:",
            "prompt_en": "Select the correct form of Kaana for Aminah:",
            "answer": "كَانَتْ", "options": ["كَانَتْ", "كَانَ", "كُنْتُ", "كَانُوا"],
            "emoji": "👩‍🎓", "hint_ur": "آمنہ طالبہ تھی۔", "hint_en": "Aminah was a student.",
            "explanation_ur": "درست جواب: 'كَانَتْ' (مؤنث اسم کے ساتھ كَانَتْ آتا ہے)",
            "explanation_en": "Correct: 'كَانَتْ' (Feminine form of Kaana)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 11: كَسْرُ هَمْزَةِ إِنَّ وَفَتْحُهَا (إِنَّ وَأَنَّ)
    # -------------------------------------------------------------
    units[11] = [
        {
            "id": "b2_u11_q1", "book": 2, "unit_num": 11, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): كسر ہمزہ 'إِنَّ' بعد القول", "badge_en": "Exercise (2): Kasrah of Inna after Qawl",
            "tamreen_title_ar": "اخْتَرْ بَيْنَ (إِنَّ) وَ (أَنَّ) حَسَبَ الْقَاعِدَةِ:",
            "tamreen_title_ur": "قاعدے کے مطابق 'إِنَّ' اور 'أَنَّ' میں سے درست کا انتخاب کریں:",
            "tamreen_title_en": "Choose between Inna and Anna according to grammar rules:",
            "grammar_goal_ur": "کلام کے شروع میں اور مادۂ قول (قَالَ، يَقُولُ) کے فوراً بعد ہمزہ مکسور (إِنَّ) آتا ہے۔", "grammar_goal_en": "Hamzah of Inna takes kasrah at sentence beginning and after qaala.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَالَ الْمُدَرِّسُ: [ ＿＿＿ ] الِامْتِحَانَ سَهْلٌ .",
            "prompt_ur": "قَالَ کے بعد درست کلمہ منتخب کریں:",
            "prompt_en": "Select the correct word after 'قَالَ':",
            "answer": "إِنَّ", "options": ["إِنَّ", "أَنَّ", "إِنْ", "أَنْ"],
            "emoji": "👨‍🏫", "hint_ur": "استاد نے کہا: بے شک امتحان آسان ہے۔", "hint_en": "The teacher said: Indeed, the exam is easy.",
            "explanation_ur": "درست جواب: 'إِنَّ' (قَالَ کے بعد ہمیشہ إِنَّ کا ہمزہ مکسور آتا ہے)",
            "explanation_en": "Correct: 'إِنَّ' (Always takes kasrah after qaala)"
        },
        {
            "id": "b2_u11_q2", "book": 2, "unit_num": 11, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): فتح ہمزہ 'أَنَّ' بعد الظن والعلم", "badge_en": "Exercise (3): Fathah of Anna after Dhann and 'Ilm",
            "tamreen_title_ar": "اسْتَعْمِلْ (أَنَّ) فِي وَسَطِ الْكَلَامِ:",
            "tamreen_title_ur": "کلام کے درمیان (أَظُنُّ، عَلِمْتُ) کے بعد 'أَنَّ' کا استعمال:",
            "tamreen_title_en": "Use Anna in mid-sentence after dhann and 'ilm:",
            "grammar_goal_ur": "جب جملہ مفعول بن رہا ہو (جیسے أَظُنُّ کے بعد) تو ہمزہ مفتوح (أَنَّ) آتا ہے۔", "grammar_goal_en": "Hamzah takes fathah (Anna) when acting as object clause.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَظُنُّ [ ＿＿＿ ] طَالِبٌ جَدِيدٌ .",
            "prompt_ur": "أَظُنُّ کے بعد درست ضمیر والی شکل منتخب کریں:",
            "prompt_en": "Select the correct form after 'أَظُنُّ':",
            "answer": "أَنَّهُ", "options": ["أَنَّهُ", "إِنَّهُ", "أَنْ هُوَ", "إِنَّ هُوَ"],
            "emoji": "🤔", "hint_ur": "میرا گمان ہے کہ وہ ایک نیا طالب علم ہے۔", "hint_en": "I think that he is a new student.",
            "explanation_ur": "درست جواب: 'أَنَّهُ' (أظن کے بعد ہمزہ مفتوح 'أَنَّ' آتا ہے)",
            "explanation_en": "Correct: 'أَنَّهُ' (Takes fathah after verbs of perception like adhinnu)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 12: الْفِعْلُ الْمُضَارِعُ (حُرُوفُ الْمُضَارَعَةِ: أ، ن، ي، ت)
    # -------------------------------------------------------------
    units[12] = [
        {
            "id": "b2_u12_q1", "book": 2, "unit_num": 12, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): صیاغتِ مضارع از ماضی", "badge_en": "Exercise (2): Forming Present Tense from Past",
            "tamreen_title_ar": "حَوِّلِ الْفِعْلَ الْمَاضِيَ إِلَى الْمُضَارِعِ:",
            "tamreen_title_ur": "ماضی کو مضارع میں تبدیل کریں:",
            "tamreen_title_en": "Convert past tense verb to present tense:",
            "grammar_goal_ur": "مضارع کے شروع میں حرفِ مضارع اور آخر میں ضمہ (پیش) آتا ہے (ذَهَبَ -> يَذْهَبُ)۔", "grammar_goal_en": "Present tense takes mudara'ah prefix and ending dammah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "خَرَجَ حَامِدٌ ➔ حَامِدٌ [ ＿＿＿ ] مِنَ الْفَصْلِ .",
            "prompt_ur": "خَرَجَ کا مضارع منتخب کریں:",
            "prompt_en": "Select the present tense form of 'خَرَجَ':",
            "answer": "يَخْرُجُ", "options": ["يَخْرُجُ", "يَخْرُجَ", "خَرَجَ", "اُخْرُجْ"],
            "emoji": "🚪", "hint_ur": "حامد کلاس سے نکل رہا ہے۔", "hint_en": "Hamid is leaving the classroom.",
            "explanation_ur": "درست جواب: 'يَخْرُجُ' (خَرَجَ کا مضارع يَخْرُجُ ہے)",
            "explanation_en": "Correct: 'يَخْرُجُ' (Present tense of kharaja)"
        },
        {
            "id": "b2_u12_q2", "book": 2, "unit_num": 12, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): مضارع مع ضمیر متکلم (أَنَا -> أَفْعَلُ)", "badge_en": "Exercise (4): Present Tense 1st Person (أَنَا)",
            "tamreen_title_ar": "صُغِ الْمُضَارِعَ مَعَ ضَمِيرِ الْمُتَكَلِّمِ (أَنَا):",
            "tamreen_title_ur": "ضمیر 'أنا' کے ساتھ فعل مضارع کا صیغہ بنائیں:",
            "tamreen_title_en": "Form present tense with 1st person prefix (hamzah):",
            "grammar_goal_ur": "متکلم کے لیے حرفِ مضارع ہمزہ 'أَ' آتا ہے (أَذْهَبُ، أَشْرَبُ)۔", "grammar_goal_en": "1st person singular takes prefix hamzah (أَ-).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] الْقُرْآنَ الْكَرِيمَ كُلَّ صَبَاحٍ .",
            "prompt_ur": "أَنَا کے لیے درست فعل مضارع منتخب کریں:",
            "prompt_en": "Select the correct present tense verb for 'أَنَا':",
            "answer": "أَقْرَأُ", "options": ["أَقْرَأُ", "يَقْرَأُ", "تَقْرَأُ", "نَقْرَأُ"],
            "emoji": "📖", "hint_ur": "میں ہر صبح قرآن کریم پڑھتا ہوں۔", "hint_en": "I read the Holy Quran every morning.",
            "explanation_ur": "درست جواب: 'أَقْرَأُ' (أنا کے ساتھ ہمزہ سے أَقْرَأُ بنتا ہے)",
            "explanation_en": "Correct: 'أَقْرَأُ' (1st person prefix is hamzah)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 13: تَصْرِيفُ الْمُضَارِعِ مَعَ جَمِيعِ الضَّمَائِرِ (الْأَفْعَالُ الْخَمْسَةُ)
    # -------------------------------------------------------------
    units[13] = [
        {
            "id": "b2_u13_q1", "book": 2, "unit_num": 13, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جمع مذکر غائب فی المضارع (يَفْعَلُونَ)", "badge_en": "Exercise (2): 3rd Person Masculine Plural (يَفْعَلُونَ)",
            "tamreen_title_ar": "أَسْنِدِ الْمُضَارِعَ إِلَى وَاوِ الْجَمَاعَةِ:",
            "tamreen_title_ur": "فعل مضارع کو واؤ جماعت کے ساتھ جوڑیں:",
            "tamreen_title_en": "Conjugate present tense with waw al-jamaa'ah:",
            "grammar_goal_ur": "جمع مذکر غائب میں واؤ جماعت اور نونِ اعرابی آتا ہے (يَذْهَبُونَ)۔", "grammar_goal_en": "Masculine plural takes suffix -oona (noon of inflection).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطُّلَّابُ [ ＿＿＿ ] إِلَى مَلْعَبِ الْمَدْرَسَةِ .",
            "prompt_ur": "الطلاب (جمع مذکر) کے لیے درست مضارع منتخب کریں:",
            "prompt_en": "Select the correct present verb for 'الطُّلَّابُ':",
            "answer": "يَذْهَبُونَ", "options": ["يَذْهَبُونَ", "يَذْهَبُ", "تَذْهَبُونَ", "يَذْهَبْنَ"],
            "emoji": "⚽", "hint_ur": "طلبہ اسکول کے کھیل کے میدان میں جا رہے ہیں۔", "hint_en": "The students are going to the school playground.",
            "explanation_ur": "درست جواب: 'يَذْهَبُونَ' (جمع مذکر کے لیے يَذْهَبُونَ آتا ہے)",
            "explanation_en": "Correct: 'يَذْهَبُونَ' (3rd person masculine plural ending is -oona)"
        },
        {
            "id": "b2_u13_q2", "book": 2, "unit_num": 13, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مفرد مؤنث مخاطب فی المضارع (تَفْعَلِينَ)", "badge_en": "Exercise (3): 2nd Person Feminine Singular (تَفْعَلِينَ)",
            "tamreen_title_ar": "أَسْنِدِ الْمُضَارِعَ إِلَى يَاءِ الْمُخَاطَبَةِ:",
            "tamreen_title_ur": "فعل مضارع کو یائے مخاطبہ کے ساتھ لائیں:",
            "tamreen_title_en": "Conjugate present tense with yaa al-mukhaatabah (-eena):",
            "grammar_goal_ur": "مؤنث مخاطب کے لیے مضارع میں تاء کے ساتھ 'ـِينَ' کا لاحقہ لگتا ہے (تَغْسِلِينَ)۔", "grammar_goal_en": "Feminine singular takes prefix taa- and suffix -eena.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ [ ＿＿＿ ] يَا مَرْيَمُ؟",
            "prompt_ur": "مریم سے پوچھنے کے لیے درست مضارع منتخب کریں:",
            "prompt_en": "Select the correct present verb addressing Maryam:",
            "answer": "تَذْهَبِينَ", "options": ["تَذْهَبِينَ", "تَذْهَبُ", "تَذْهَبُونَ", "يَذْهَبْنَ"],
            "emoji": "👧", "hint_ur": "تم کہاں جا رہی ہو اے مریم؟", "hint_en": "Where are you going, O Maryam?",
            "explanation_ur": "درست جواب: 'تَذْهَبِينَ' (مؤنث مخاطب کے لیے تَذْهَبِينَ آتا ہے)",
            "explanation_en": "Correct: 'تَذْهَبِينَ' (Takes prefix ta- and suffix -eena)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 14: نَفْيُ الْمُضَارِعِ (لَا) وَنَفْيُ الْمَاضِي (مَا) وَالسُّؤَالُ بـ (أَلَمْ)
    # -------------------------------------------------------------
    units[14] = [
        {
            "id": "b2_u14_q1", "book": 2, "unit_num": 14, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): نفیِ مضارع بـ (لَا) النافية", "badge_en": "Exercise (2): Negating Present Tense with 'Laa'",
            "tamreen_title_ar": "انْفِ الْفِعْلَ الْمُضَارِعَ بِـ (لَا) النَّافِيَةِ:",
            "tamreen_title_ur": "فعل مضارع کی نفی کے لیے حرف منتخب کریں:",
            "tamreen_title_en": "Negate the present tense verb with Laa an-naafiyah:",
            "grammar_goal_ur": "مضارع کی نفی 'لَا' سے کی جاتی ہے اور فعل کے اعراب پر کوئی اثر نہیں پڑتا۔", "grammar_goal_en": "Laa an-naafiyah negates present tense without changing its mood.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا [ ＿＿＿ ] أَشْرَبُ الْقَهْوَةَ .",
            "prompt_ur": "مضارع کی نفی کے لیے درست کلمہ منتخب کریں:",
            "prompt_en": "Select the correct negative particle for present tense:",
            "answer": "لَا", "options": ["لَا", "مَا", "لَمْ", "لَنْ"],
            "emoji": "☕", "hint_ur": "میں کافی نہیں پیتا ہوں۔", "hint_en": "I do not drink coffee.",
            "explanation_ur": "درست جواب: 'لَا' (مضارع کی نفی عموماً لَا سے کی جاتی ہے)",
            "explanation_en": "Correct: 'لَا' (Laa negates the present tense without apocopation)"
        },
        {
            "id": "b2_u14_q2", "book": 2, "unit_num": 14, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): جوابِ استفہامِ منفی (بَلَى / نَعَمْ)", "badge_en": "Exercise (4): Answering Negative Questions (Balaa / Na'am)",
            "tamreen_title_ar": "أَجِبْ عَنِ السُّؤَالِ الْمَنْفِيِّ بِـ (بَلَى) لِلْإِثْبَاتِ:",
            "tamreen_title_ur": "منفی سوال کا اثباتی جواب دینے کا قاعدہ:",
            "tamreen_title_en": "Answer the negative question in the affirmative using 'Balaa':",
            "grammar_goal_ur": "منفی سوال (أَلَمْ، أَلَيْسَ) کے اثبات کے لیے 'بَلَى' اور نفی برقرار رکھنے کے لیے 'نَعَمْ' کہا جاتا ہے۔", "grammar_goal_en": "Affirmative answer to negative interrogative uses Balaa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَلَمْ تَذْهَبْ إِلَى الْمَسْجِدِ؟ ➔ [ ＿＿＿ ] ذَهَبْتُ .",
            "prompt_ur": "اثباتی جواب ('کیوں نہیں، میں گیا تھا') کے لیے درست کلمہ منتخب کریں:",
            "prompt_en": "Select the affirmative particle answering the negative question:",
            "answer": "بَلَى", "options": ["بَلَى", "نَعَمْ", "لَا", "إِنَّ"],
            "emoji": "🕌", "hint_ur": "کیوں نہیں، میں مسجد گیا تھا۔", "hint_en": "Yes indeed, I did go to the mosque.",
            "explanation_ur": "درست جواب: 'بَلَى' (منفی سوال کے جواب میں اثبات کے لیے بَلَى بولا جاتا ہے)",
            "explanation_en": "Correct: 'بَلَى' (Affirmative response to a negative question)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 15: فِعْلُ الْأَمْرِ (صَوْغُهُ وَإِعْرَابُهُ)
    # -------------------------------------------------------------
    units[15] = [
        {
            "id": "b2_u15_q1", "book": 2, "unit_num": 15, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): صیاغتِ امر با ہمزۃ الوصل مکسورۃ (اِفْعَلْ)", "badge_en": "Exercise (2): Imperative with Kasrah Hamzah (اِفْعَلْ)",
            "tamreen_title_ar": "صُغْ فِعْلَ الْأَمْرِ مِنَ الْفِعْلِ الْمُضَارِعِ:",
            "tamreen_title_ur": "مضارع (تَجْلِسُ) سے فعل امر بنائیں:",
            "tamreen_title_en": "Form imperative from present tense 'تَجْلِسُ':",
            "grammar_goal_ur": "اگر مضارع کا عین کلمہ مکسور ہو تو امر میں ہمزہ وصلیہ کو زیر دی جاتی ہے اور آخر ساکن ہوتا ہے (اِجْلِسْ)۔", "grammar_goal_en": "Imperative takes kasrah on hamzatul-wasl when middle root vowel is kasrah/fathah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنْتَ تَجْلِسُ ➔ يَا عَلِيُّ، [ ＿＿＿ ] هُنَا ! ",
            "prompt_ur": "تَجْلِسُ کا فعل امر منتخب کریں:",
            "prompt_en": "Select the imperative form of 'تَجْلِسُ':",
            "answer": "اِجْلِسْ", "options": ["اِجْلِسْ", "أُجْلُسْ", "تَجْلِسْ", "جَلَسَ"],
            "emoji": "🪑", "hint_ur": "اے علی، یہاں بیٹھو!", "hint_en": "O Ali, sit here!",
            "explanation_ur": "درست جواب: 'اِجْلِسْ' (تجلس سے فعل امر اِجْلِسْ بنتا ہے)",
            "explanation_en": "Correct: 'اِجْلِسْ' (Imperative of tajlisu is ijlis)"
        },
        {
            "id": "b2_u15_q2", "book": 2, "unit_num": 15, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): صیاغتِ امر با ہمزۃ الوصل مضمومۃ (اُفْعُلْ)", "badge_en": "Exercise (3): Imperative with Dammah Hamzah (اُفْعُلْ)",
            "tamreen_title_ar": "صُغِ الْأَمْرَ إِذَا كَانَتْ عَيْنُ الْمُضَارِعِ مَضْمُومَةً:",
            "tamreen_title_ur": "جب مضارع کا عین کلمہ مضموم ہو تو امر کا صیغہ بنائیں:",
            "tamreen_title_en": "Form imperative when middle root vowel has dammah:",
            "grammar_goal_ur": "اگر مضارع کے عین کلمہ پر پیش ہو تو ہمزہ وصلیہ پر پیش دی جاتی ہے (تَكْتُبُ -> اُكْتُبْ)۔", "grammar_goal_en": "Imperative hamzah takes dammah when middle root has dammah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنْتَ تَكْتُبُ ➔ يَا حَامِدُ، [ ＿＿＿ ] الدَّرْسَ ! ",
            "prompt_ur": "تَكْتُبُ کا فعل امر منتخب کریں:",
            "prompt_en": "Select the imperative form of 'تَكْتُبُ':",
            "answer": "اُكْتُبْ", "options": ["اُكْتُبْ", "اِكْتِبْ", "أَكْتَبْ", "تَكْتُبْ"],
            "emoji": "✍️", "hint_ur": "اے حامد، سبق لکھو!", "hint_en": "O Hamid, write the lesson!",
            "explanation_ur": "درست جواب: 'اُكْتُبْ' (تَكْتُبُ میں تاء پر پیش ہونے کی وجہ سے ہمزہ پر پیش آتی ہے)",
            "explanation_en": "Correct: 'اُكْتُبْ' (Middle root has dammah, so prefix is u-)"
        },
        {
            "id": "b2_u15_q3", "book": 2, "unit_num": 15, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): امرِ حاضر مؤنث (اِفْعَلِي)", "badge_en": "Exercise (4): Feminine Imperative (اِفْعَلِي)",
            "tamreen_title_ar": "صُغِ الْأَمْرَ لِلْمُخَاطَبَةِ الْمُؤَنَّثَةِ:",
            "tamreen_title_ur": "مؤنث مخاطب کے لیے فعل امر بنائیں:",
            "tamreen_title_en": "Form feminine singular imperative by dropping noon:",
            "grammar_goal_ur": "مؤنث مخاطب کے امر میں نونِ اعرابی گر جاتی ہے اور یائے تخاطب باقی رہتی ہے (اِذْهَبِي)۔", "grammar_goal_en": "Feminine singular imperative ends in yaa without noon.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا آمِنَةُ، [ ＿＿＿ ] إِلَى الْفَصْلِ ! ",
            "prompt_ur": "آمنہ کو حکم دینے کے لیے درست امر منتخب کریں:",
            "prompt_en": "Select the correct imperative addressing Aminah:",
            "answer": "اِذْهَبِي", "options": ["اِذْهَبِي", "اِذْهَبْ", "تَذْهَبِينَ", "اِذْهَبُوا"],
            "emoji": "👧", "hint_ur": "اے آمنہ، کلاس میں جاؤ!", "hint_en": "O Aminah, go to the classroom!",
            "explanation_ur": "درست جواب: 'اِذْهَبِي' (مؤنث مخاطب کے لیے اِذْهَبِي آتا ہے)",
            "explanation_en": "Correct: 'اِذْهَبِي' (Feminine imperative suffix is -ee)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 16: النَّهْيُ بِـ (لَا) النَّاهِيَةِ الْجَازِمَةِ
    # -------------------------------------------------------------
    units[16] = [
        {
            "id": "b2_u16_q1", "book": 2, "unit_num": 16, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): نہی کا جزم (لَا تَفْعَلْ)", "badge_en": "Exercise (2): Jussive Prohibition (Laa Taf'al)",
            "tamreen_title_ar": "أَدْخِلْ (لَا النَّاهِيَةَ) عَلَى الْفِعْلِ الْمُضَارِعِ:",
            "tamreen_title_ur": "فعل مضارع پر 'لَا الناہیہ' داخل کر کے جزم دیں:",
            "tamreen_title_en": "Enter Laa an-naahiyah and apply jussive sukoon:",
            "grammar_goal_ur": "لا الناہیہ مضارع کو جزم (سکون) دیتی ہے (لَا تَخْرُجْ)۔", "grammar_goal_en": "Laa an-naahiyah gives jussive sukoon to present tense.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا أَخِي، [ ＿＿＿ ] مِنَ الْفَصْلِ الْآنَ ! ",
            "prompt_ur": "کلاس سے نہ نکلنے سے روکنے کے لیے درست صیغہ منتخب کریں:",
            "prompt_en": "Select the correct negative command form:",
            "answer": "لَا تَخْرُجْ", "options": ["لَا تَخْرُجْ", "لَا تَخْرُجُ", "لَا تَخْرُجَ", "مَا تَخْرُجْ"],
            "emoji": "🛑", "hint_ur": "اے میرے بھائی، ابھی کلاس سے مت نکلو!", "hint_en": "O my brother, do not leave the classroom now!",
            "explanation_ur": "درست جواب: 'لَا تَخْرُجْ' (لا الناہیہ کے بعد مضارع پر جزم آتی ہے)",
            "explanation_en": "Correct: 'لَا تَخْرُجْ' (Takes jussive sukoon after prohibitive laa)"
        },
        {
            "id": "b2_u16_q2", "book": 2, "unit_num": 16, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): نہی للمؤنث بحذف النون (لَا تَفْعَلِي)", "badge_en": "Exercise (4): Prohibitive for Feminine (-ee)",
            "tamreen_title_ar": "صُغِ النَّهْيَ لِلْمُؤَنَّثَةِ الْمُخَاطَبَةِ:",
            "tamreen_title_ur": "مؤنث مخاطب کے لیے نہی کا صیغہ بنائیں:",
            "tamreen_title_en": "Form feminine prohibitive by dropping noon:",
            "grammar_goal_ur": "مؤنث مخاطب میں لا الناہیہ سے نون اعرابی حذف ہو جاتی ہے (لَا تَذْهَبِي)۔", "grammar_goal_en": "Feminine singular drops noon after prohibitive laa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا فَاطِمَةُ، [ ＿＿＿ ] النَّافِذَةَ ! ",
            "prompt_ur": "فاطمہ کو کھڑکی نہ کھولنے سے منع کرنے کے لیے درست فعل منتخب کریں:",
            "prompt_en": "Select the correct prohibitive verb addressing Fatimah:",
            "answer": "لَا تَفْتَحِي", "options": ["لَا تَفْتَحِي", "لَا تَفْتَحِينَ", "لَا تَفْتَحْ", "لَا تَفْتَحُ"],
            "emoji": "🪟", "hint_ur": "اے فاطمہ، کھڑکی مت کھولو!", "hint_en": "O Fatimah, do not open the window!",
            "explanation_ur": "درست جواب: 'لَا تَفْتَحِي' (مؤنث مخاطب کے لیے نون حذف ہو کر لَا تَفْتَحِي بنتا ہے)",
            "explanation_en": "Correct: 'لَا تَفْتَحِي' (Drops noon in jussive feminine singular)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 17: نَصْبُ الْمُضَارِعِ بِـ (أَنْ) الْمَصْدَرِيَّةِ وَ (لَامِ التَّعْلِيلِ)
    # -------------------------------------------------------------
    units[17] = [
        {
            "id": "b2_u17_q1", "book": 2, "unit_num": 17, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): ناصبہ 'أَنْ' کا عمل (نصب)", "badge_en": "Exercise (6): Subjunctive with 'An'",
            "tamreen_title_ar": "أَدْخِلْ (أَنْ) عَلَى الْفِعْلِ الْمُضَارِعِ:",
            "tamreen_title_ur": "فعل مضارع پر 'أَنْ' داخل کر کے زبر (نصب) دیں:",
            "tamreen_title_en": "Enter 'An' and apply subjunctive fathah:",
            "grammar_goal_ur": "حرفِ ناصب 'أَنْ' مضارع کو نصب (زبر) دیتا ہے (أَنْ أَذْهَبَ)۔", "grammar_goal_en": "The particle 'An' puts present verb into subjunctive (mansoob with fathah).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أُرِيدُ أَنْ [ ＿＿＿ ] إِلَى الْمُسْتَوْصَفِ .",
            "prompt_ur": "أَنْ کے بعد درست اعراب والا فعل منتخب کریں:",
            "prompt_en": "Select the correctly voweled verb after 'أَنْ':",
            "answer": "أَذْهَبَ", "options": ["أَذْهَبَ", "أَذْهَبُ", "أَذْهَبْ", "أَذْهَبِ"],
            "emoji": "🏥", "hint_ur": "میں ڈسپنسری جانا چاہتا ہوں۔", "hint_en": "I want to go to the clinic.",
            "explanation_ur": "درست جواب: 'أَذْهَبَ' (أَنْ ناصبہ کے بعد مضارع پر زبر آتی ہے)",
            "explanation_en": "Correct: 'أَذْهَبَ' (Takes subjunctive fathah after 'An')"
        },
        {
            "id": "b2_u17_q2", "book": 2, "unit_num": 17, "tamreen_num": 8,
            "badge_ar": "التَّمْرِينُ (8)", "badge_ur": "مشق (8): لَامُ التَّعْلِيلِ النَّاصِبَة", "badge_en": "Exercise (8): Laam of Reason (Subjunctive)",
            "tamreen_title_ar": "اسْتَعْمِلْ (لَامَ التَّعْلِيلِ) مَعَ الْمُضَارِعِ:",
            "tamreen_title_ur": "سبب بیان کرنے کے لیے 'لامِ تعلیل' لگائیں:",
            "tamreen_title_en": "Use Laam of reason with present tense verb:",
            "grammar_goal_ur": "لامِ تعلیل مضارع کو نصب دیتی ہے (لِنَفْهَمَ)۔", "grammar_goal_en": "Laam of causation (li-) governs present tense in subjunctive fathah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "نَدْرُسُ اللُّغَةَ الْعَرَبِيَّةَ [ ＿＿＿ ] الْقُرْآنَ الْكَرِيمَ .",
            "prompt_ur": "قرآن سمجھنے کے سبب کے لیے درست فعل منتخب کریں:",
            "prompt_en": "Select the correct verb indicating purpose:",
            "answer": "لِنَفْهَمَ", "options": ["لِنَفْهَمَ", "لِنَفْهَمُ", "لِنَفْهَمْ", "نَفْهَمُ"],
            "emoji": "📖", "hint_ur": "ہم عربی زبان پڑھتے ہیں تاکہ قرآن کریم سمجھیں۔", "hint_en": "We study Arabic in order to understand the Holy Quran.",
            "explanation_ur": "درست جواب: 'لِنَفْهَمَ' (لامِ تعلیل کے بعد مضارع منصوب ہوتا ہے)",
            "explanation_en": "Correct: 'لِنَفْهَمَ' (Subjunctive after laam of reason)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 18: نَصْبُ الْأَفْعَالِ الْخَمْسَةِ بِحَذْفِ النُّونِ (أَنْ / لَنْ)
    # -------------------------------------------------------------
    units[18] = [
        {
            "id": "b2_u18_q1", "book": 2, "unit_num": 18, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): حذف النون فی الأفعال الخمسة مَعَ (أَنْ)", "badge_en": "Exercise (4): Elision of Noon with 'An'",
            "tamreen_title_ar": "أَسْنِدِ الْمُضَارِعَ الْمَنْصُوبَ إِلَى وَاوِ الْجَمَاعَةِ:",
            "tamreen_title_ur": "جمع مذکر میں 'أَنْ' کے بعد نون گرانے کی مشق کریں:",
            "tamreen_title_en": "Omit noon in 5 verbs after subjunctive 'An':",
            "grammar_goal_ur": "افعالِ خمسہ جب منصوب ہوں تو ان کی نون گر جاتی ہے (أَنْ يَذْهَبُوا)۔", "grammar_goal_en": "The Five Verbs lose the ending noon in subjunctive case.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يُرِيدُ الطُّلَّابُ أَنْ [ ＿＿＿ ] إِلَى الْمُتْحَفِ غَداً .",
            "prompt_ur": "طلبہ کے لیے 'أَنْ' کے بعد درست فعل منتخب کریں:",
            "prompt_en": "Select the correct subjunctive form for students after 'أَنْ':",
            "answer": "يَذْهَبُوا", "options": ["يَذْهَبُوا", "يَذْهَبُونَ", "يَذْهَبُ", "يَذْهَبْنَ"],
            "emoji": "🏛️", "hint_ur": "طلبہ کل عجائب گھر جانا چاہتے ہیں۔", "hint_en": "The students want to go to the museum tomorrow.",
            "explanation_ur": "درست جواب: 'يَذْهَبُوا' (أَنْ کی وجہ سے نون گر گئی اور الف لکھی جاتی ہے)",
            "explanation_en": "Correct: 'يَذْهَبُوا' (Noon is dropped in subjunctive plural)"
        },
        {
            "id": "b2_u18_q2", "book": 2, "unit_num": 18, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): نفیِ مستقبل بـ (لَنْ) الناصبة", "badge_en": "Exercise (5): Future Negative Subjunctive with 'Lan'",
            "tamreen_title_ar": "انْفِ الْمُسْتَقْبَلَ بِـ (لَنْ) النَّاصِبَةِ:",
            "tamreen_title_ur": "مستقبل کی تاکیدی نفی کے لیے 'لَنْ' لگائیں:",
            "tamreen_title_en": "Negate future with emphatic particle 'Lan':",
            "grammar_goal_ur": "'لَنْ' مستقبل کی نفی کرتی ہے اور مضارع کو زبر (نصب) دیتی ہے (لَنْ أَذْهَبَ)۔", "grammar_goal_en": "Lan negates future action and governs present verb in subjunctive.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا تَعْبَانُ الْيَوْمَ ، [ ＿＿＿ ] أَخْرُجَ مِنَ الْبَيْتِ .",
            "prompt_ur": "مستقبل کی نفی کے لیے درست ناصب حرف منتخب کریں:",
            "prompt_en": "Select the correct future negative particle:",
            "answer": "لَنْ", "options": ["لَنْ", "لَمْ", "لَا", "مَا"],
            "emoji": "🏠", "hint_ur": "میں آج تھکا ہوا ہوں، میں ہرگز گھر سے نہیں نکلوں گا۔", "hint_en": "I am tired today; I will never go out of the house.",
            "explanation_ur": "درست جواب: 'لَنْ' (لَنْ مستقبل کی تاکیدی نفی کے لیے آتا ہے اور نصب دیتا ہے)",
            "explanation_en": "Correct: 'لَنْ' (Particle of future negative with subjunctive)"
        }
    ]

    return units

if __name__ == "__main__":
    u = get_b2_part2()
    print("Units in part 2:", sorted(u.keys()))
    print("Total Qs in part 2:", sum(len(v) for v in u.values()))
