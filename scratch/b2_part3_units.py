import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_b2_part3():
    units = {}

    # -------------------------------------------------------------
    # UNIT 19: جَزْمُ الْمُضَارِعِ بِـ (لَمْ) وَحَذْفُ النُّونِ
    # -------------------------------------------------------------
    units[19] = [
        {
            "id": "b2_u19_q1", "book": 2, "unit_num": 19, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جزم بـ (لَمْ) وقلب المعنى للماضي", "badge_en": "Exercise (2): Jussive Negative with 'Lam'",
            "tamreen_title_ar": "أَدْخِلْ (لَمْ) عَلَى الْفِعْلِ الْمُضَارِعِ:",
            "tamreen_title_ur": "مضارع پر 'لَمْ' داخل کر کے جزم دیں:",
            "tamreen_title_en": "Enter 'Lam' and apply jussive sukoon:",
            "grammar_goal_ur": "'لَمْ' مضارع کو جزم دیتی ہے اور اس کے معنی کو ماضی منفی میں بدل دیتی ہے (لَمْ يَذْهَبْ)۔", "grammar_goal_en": "Lam gives jussive sukoon and flips meaning to past negative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَكْتُبُ الطَّالِبُ ➔ الطَّالِبُ [ ＿＿＿ ] الدَّرْسَ .",
            "prompt_ur": "طلبہ کے سبق نہ لکھنے کے لیے درست صیغہ منتخب کریں:",
            "prompt_en": "Select the correct jussive verb form after 'لَمْ':",
            "answer": "لَمْ يَكْتُبْ", "options": ["لَمْ يَكْتُبْ", "لَمْ يَكْتُبُ", "لَمْ يَكْتُبَ", "مَا يَكْتُبْ"],
            "emoji": "✍️", "hint_ur": "طالب علم نے سبق نہیں لکھا۔", "hint_en": "The student did not write the lesson.",
            "explanation_ur": "درست جواب: 'لَمْ يَكْتُبْ' (لَمْ کے بعد مضارع پر جزم آتی ہے)",
            "explanation_en": "Correct: 'لَمْ يَكْتُبْ' (Takes jussive sukoon after Lam)"
        },
        {
            "id": "b2_u19_q2", "book": 2, "unit_num": 19, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): حذف النون فی الأفعال الخمسة مَعَ (لَمْ)", "badge_en": "Exercise (4): Dropping Noon with 'Lam' in Plural",
            "tamreen_title_ar": "انْفِ الْجَمْعَ بِـ (لَمْ) مَعَ حَذْفِ النُّونِ:",
            "tamreen_title_ur": "جمع مذکر کی 'لَمْ' کے ساتھ نفی میں نون گرانے کی مشق کریں:",
            "tamreen_title_en": "Negate plural present verb with 'Lam' dropping noon:",
            "grammar_goal_ur": "افعالِ خمسہ پر جب 'لَمْ' داخل ہو تو نون اعرابی حذف ہو جاتی ہے (لَمْ يَذْهَبُوا)۔", "grammar_goal_en": "The Five Verbs lose the ending noon in jussive case.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الطُّلَّابُ [ ＿＿＿ ] إِلَى الْمَلْعَبِ الْيَوْمَ .",
            "prompt_ur": "طلبہ کے نہ جانے کے لیے درست صیغہ منتخب کریں:",
            "prompt_en": "Select the correct negated plural verb:",
            "answer": "لَمْ يَذْهَبُوا", "options": ["لَمْ يَذْهَبُوا", "لَمْ يَذْهَبُونَ", "لَمْ يَذْهَبْ", "مَا ذَهَبُوا"],
            "emoji": "🏃‍♂️", "hint_ur": "طلبہ آج کھیل کے میدان میں نہیں گئے۔", "hint_en": "The students did not go to the playground today.",
            "explanation_ur": "درست جواب: 'لَمْ يَذْهَبُوا' (جزم کی علامت نون کا گرنا ہے)",
            "explanation_en": "Correct: 'لَمْ يَذْهَبُوا' (Jussive marker in the five verbs is omission of noon)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 20: الْمُثَنَّى (إِعْرَابُهُ بِالْأَلِفِ وَالْيَاءِ)
    # -------------------------------------------------------------
    units[20] = [
        {
            "id": "b2_u20_q1", "book": 2, "unit_num": 20, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): رفعِ مثنیٰ بالالف (انِ)", "badge_en": "Exercise (2): Nominative Dual Ending (-aani)",
            "tamreen_title_ar": "ثَنِّ الِاسْمَ فِي حَالَةِ الرَّفْعِ:",
            "tamreen_title_ur": "حالتِ رفع (مبتدا یا فاعل) میں اسم کو تثنیہ بنائیں:",
            "tamreen_title_en": "Make the noun dual in the nominative case:",
            "grammar_goal_ur": "مثنیٰ حالتِ رفع میں الف اور نونِ مکسورہ (انِ) کے ساتھ آتا ہے (كِتَابَانِ)۔", "grammar_goal_en": "Dual noun in nominative case takes suffix -aani.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدِي [ ＿＿＿ ] جَدِيدَانِ .",
            "prompt_ur": "میرے پاس دو نئی کتابیں ہیں، کے لیے درست لفظ منتخب کریں:",
            "prompt_en": "Select the correct nominative dual noun for 'two books':",
            "answer": "كِتَابَانِ", "options": ["كِتَابَانِ", "كِتَابَيْنِ", "كُتُبٌ", "كِتَابٌ"],
            "emoji": "📚", "hint_ur": "میرے پاس دو نئی کتابیں ہیں۔", "hint_en": "I have two new books.",
            "explanation_ur": "درست جواب: 'كِتَابَانِ' (مبتدائے مؤخر مرفوع ہے، تثنیہ کی علامت الف ہے)",
            "explanation_en": "Correct: 'كِتَابَانِ' (Dual takes -aani in nominative)"
        },
        {
            "id": "b2_u20_q2", "book": 2, "unit_num": 20, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): نصب و جرِ مثنیٰ بالیاء (يْنِ)", "badge_en": "Exercise (4): Accusative/Genitive Dual Ending (-ayni)",
            "tamreen_title_ar": "ثَنِّ الِاسْمَ فِي حَالَتَيِ النَّصْبِ وَالْجَرِّ:",
            "tamreen_title_ur": "حالتِ نصب (مفعول بہ) میں تثنیہ کا اعراب لگائیں:",
            "tamreen_title_en": "Apply accusative/genitive dual ending (-ayni):",
            "grammar_goal_ur": "حالتِ نصب اور جر میں مثنیٰ یائے ماقبل مفتوح اور نونِ مکسورہ (يْنِ) کے ساتھ آتا ہے (قَلَمَيْنِ)۔", "grammar_goal_en": "Dual takes -ayni in accusative and genitive cases.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "اشْتَرَيْتُ [ ＿＿＿ ] مِنَ الْمَكْتَبَةِ .",
            "prompt_ur": "میں نے لائبریری سے دو قلم خریدے، کے لیے درست لفظ منتخب کریں:",
            "prompt_en": "Select the correct accusative dual noun for 'two pens':",
            "answer": "قَلَمَيْنِ", "options": ["قَلَمَيْنِ", "قَلَمَانِ", "أَقْلَامٌ", "قَلَمٍ"],
            "emoji": "🖊️", "hint_ur": "میں نے دو قلم خریدے۔", "hint_en": "I bought two pens.",
            "explanation_ur": "درست جواب: 'قَلَمَيْنِ' (مفعول بہ منصوب ہے، تثنیہ کی حالتِ نصب میں یاء آتی ہے)",
            "explanation_en": "Correct: 'قَلَمَيْنِ' (Accusative dual ending is -ayni)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 21: كِلَا وَكِلْتَا وَأَسْمَاءُ الْإِشَارَةِ لِلْمُثَنَّى
    # -------------------------------------------------------------
    units[21] = [
        {
            "id": "b2_u21_q1", "book": 2, "unit_num": 21, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اسم اشارہ للمثنیٰ المذکر (هٰذَانِ / هٰذَيْنِ)", "badge_en": "Exercise (2): Dual Demonstrative Pronoun (هٰذَانِ)",
            "tamreen_title_ar": "اخْتَرْ اسْمَ الْإِشَارَةِ الْمُنَاسِبَ لِلْمُثَنَّى:",
            "tamreen_title_ur": "تثنیہ مذکر کے لیے درست اسمِ اشارہ منتخب کریں:",
            "tamreen_title_en": "Select the appropriate demonstrative pronoun for masculine dual:",
            "grammar_goal_ur": "حالتِ رفع میں تثنیہ مذکر کے لیے 'هٰذَانِ' اور مؤنث کے لیے 'هَاتَانِ' آتا ہے۔", "grammar_goal_en": "Masculine nominative dual demonstrative is Haadhaani.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "[ ＿＿＿ ] طَالِبَانِ جَدِيدَانِ مِنَ الْيَابَانِ .",
            "prompt_ur": "طالبان جدیدان کے لیے درست اسمِ اشارہ کیا ہے؟",
            "prompt_en": "What is the correct demonstrative pronoun for 'طَالِبَانِ'?",
            "answer": "هٰذَانِ", "options": ["هٰذَانِ", "هٰذَيْنِ", "هٰؤُلَاءِ", "هٰذَا"],
            "emoji": "👨‍🎓", "hint_ur": "یہ دونوں جاپان سے آئے ہوئے نئے طالب علم ہیں۔", "hint_en": "These two are new students from Japan.",
            "explanation_ur": "درست جواب: 'هٰذَانِ' (تثنیہ مذکر مرفوع کے لیے هٰذَانِ آتا ہے)",
            "explanation_en": "Correct: 'هٰذَانِ' (Nominative masculine dual demonstrative)"
        },
        {
            "id": "b2_u21_q2", "book": 2, "unit_num": 21, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): توکید بـ (كِلَاهُمَا / كِلْتَاهُمَا)", "badge_en": "Exercise (4): Corroboration with Kilaahumaa",
            "tamreen_title_ar": "أَكِّدِ الْمُثَنَّى بِـ (كِلَاهُمَا) أَوْ (كِلْتَاهُمَا):",
            "tamreen_title_ur": "تثنیہ کی تاکید کے لیے درست لفظ منتخب کریں:",
            "tamreen_title_en": "Use Kilaahumaa (masc) or Kiltaahumaa (fem) for dual emphasis:",
            "grammar_goal_ur": "مذکر کے لیے 'كِلَاهُمَا' اور مؤنث کے لیے 'كِلْتَاهُمَا' استعمال ہوتا ہے۔", "grammar_goal_en": "Kilaahumaa for masculine dual, Kiltaahumaa for feminine dual.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَحْمَدُ وَعَلِيٌّ [ ＿＿＿ ] طَالِبَانِ مُجْتَهِدَانِ .",
            "prompt_ur": "احمد اور علی (مذکر تثنیہ) کی تاکید کے لیے درست کلمہ منتخب کریں:",
            "prompt_en": "Select the correct dual corroboration for Ahmad and Ali:",
            "answer": "كِلَاهُمَا", "options": ["كِلَاهُمَا", "كِلْتَاهُمَا", "كُلُّهُمْ", "كِلَيْهِمَا"],
            "emoji": "👬", "hint_ur": "احمد اور علی دونوں محنتی طالب علم ہیں۔", "hint_en": "Ahmad and Ali, both of them are diligent students.",
            "explanation_ur": "درست جواب: 'كِلَاهُمَا' (مذکر تثنیہ مرفوع کے لیے كِلَاهُمَا آتا ہے)",
            "explanation_en": "Correct: 'كِلَاهُمَا' (Masculine nominative dual emphasis)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 22: أَوْجُهُ إِعْرَابِ الْمُضَارِعِ الثَّلَاثَةِ (مَرْفُوع، مَنْصُوب، مَجْزُوم)
    # -------------------------------------------------------------
    units[22] = [
        {
            "id": "b2_u22_q1", "book": 2, "unit_num": 22, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): موازنہ اعرابِ مضارع (رفع، نصب، جزم)", "badge_en": "Exercise (1): The 3 Moods of the Imperfect Verb",
            "tamreen_title_ar": "حَدِّدْ حَالَةَ إِعْرَابِ الْفِعْلِ الْمُضَارِعِ:",
            "tamreen_title_ur": "مضارع کی اعرابی حالت (مرفوع، منصوب، مجزوم) پہچانیں:",
            "tamreen_title_en": "Identify the grammatical mood of the imperfect verb:",
            "grammar_goal_ur": "مضارع پر جب ناصب یا جازم نہ ہو تو وہ مرفوع ہوتا ہے، ناصب سے منصوب اور جازم سے مجزوم۔", "grammar_goal_en": "Imperfect verb is marfoo' by default, mansoob after naasib, majzoom after jaazim.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْفِعْلُ فِي جُمْلَةِ (لَمْ يَذْهَبْ) هُوَ: [ ＿＿＿ ]",
            "prompt_ur": "(لَمْ يَذْهَبْ) میں فعل کا اعراب کیا ہے؟",
            "prompt_en": "What is the mood of the verb in 'لَمْ يَذْهَبْ'?",
            "answer": "مَجْزُومٌ بِالسُّكُونِ", "options": ["مَجْزُومٌ بِالسُّكُونِ", "مَنْصُوبٌ بِالْفَتْحَةِ", "مَرْفُوعٌ بِالضَّمَّةِ", "مَبْنِيٌّ عَلَى الْفَتْحِ"],
            "emoji": "⚖️", "hint_ur": "یہ فعل جزم والا ہے (سکون کے ساتھ)۔", "hint_en": "The verb is apocopated (jussive with sukoon).",
            "explanation_ur": "درست جواب: 'مَجْزُومٌ بِالسُّكُونِ' (لَمْ جازمہ کی وجہ سے فعل مجزوم ہے)",
            "explanation_en": "Correct: 'مَجْزُومٌ بِالسُّكُونِ' (Majzoom with sukoon governed by Lam)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 23: جَمْعُ الْمُذَكَّرِ السَّالِمُ (إِعْرَابُهُ بِالْوَاوِ وَالْيَاءِ)
    # -------------------------------------------------------------
    units[23] = [
        {
            "id": "b2_u23_q1", "book": 2, "unit_num": 23, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): رفعِ جمع مذکر سالم بالواو (ـُونَ)", "badge_en": "Exercise (2): Nominative Sound Plural Ending (-oona)",
            "tamreen_title_ar": "اجْمَعِ الِاسْمَ جَمْعَ مُذَكَّرٍ سَالِماً فِي حَالَةِ الرَّفْعِ:",
            "tamreen_title_ur": "حالتِ رفع (فاعل/مبتدا) میں جمع مذکر سالم کا صیغہ بنائیں:",
            "tamreen_title_en": "Form nominative sound masculine plural ending in -oona:",
            "grammar_goal_ur": "جمع مذکر سالم حالتِ رفع میں واؤ اور نونِ مفتوحہ (ـُونَ) کے ساتھ آتا ہے (مُدَرِّسُونَ)۔", "grammar_goal_en": "Sound masculine plural takes -oona in nominative.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "خَرَجَ [ ＿＿＿ ] مِنَ الْفُصُولِ .",
            "prompt_ur": "فاعل (مدرسین) کے لیے درست لفظ منتخب کریں:",
            "prompt_en": "Select the correct nominative plural subject for 'teachers':",
            "answer": "الْمُدَرِّسُونَ", "options": ["الْمُدَرِّسُونَ", "الْمُدَرِّسِينَ", "الْمُدَرِّسَاتُ", "مُدَرِّسٍ"],
            "emoji": "👨‍🏫", "hint_ur": "اساتذہ کلاسوں سے نکلے۔", "hint_en": "The teachers went out of the classrooms.",
            "explanation_ur": "درست جواب: 'الْمُدَرِّسُونَ' (فاعل مرفوع ہے اور جمع مذکر سالم میں رفع کی علامت واؤ ہے)",
            "explanation_en": "Correct: 'الْمُدَرِّسُونَ' (Nominative plural marker is waw)"
        },
        {
            "id": "b2_u23_q2", "book": 2, "unit_num": 23, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): نصب و جرِ جمع مذکر سالم بالیاء (ـِينَ)", "badge_en": "Exercise (4): Accusative/Genitive Plural Ending (-eena)",
            "tamreen_title_ar": "أَعْرِبْ جَمْعَ الْمُذَكَّرِ السَّالِمِ فِي حَالَةِ النَّصْبِ:",
            "tamreen_title_ur": "حالتِ نصب (مفعول بہ) میں جمع مذکر سالم کا اعراب لگائیں:",
            "tamreen_title_en": "Apply accusative plural ending (-eena) to direct object:",
            "grammar_goal_ur": "جمع مذکر سالم حالتِ نصب اور جر میں یائے ماقبل مکسور اور نونِ مفتوحہ (ـِينَ) سے آتا ہے (الْمُهَنْدِسِينَ)۔", "grammar_goal_en": "Sound masculine plural takes -eena in accusative and genitive.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "رَأَيْتُ [ ＿＿＿ ] فِي الْمَصْنَعِ .",
            "prompt_ur": "مفعول بہ (انجینئرز) کے لیے درست لفظ منتخب کریں:",
            "prompt_en": "Select the correct accusative plural object for 'engineers':",
            "answer": "الْمُهَنْدِسِينَ", "options": ["الْمُهَنْدِسِينَ", "الْمُهَنْدِسُونَ", "الْمُهَنْدِسَاتِ", "مُهَنْدِسٍ"],
            "emoji": "👷‍♂️", "hint_ur": "میں نے کارخانے میں انجینئرز کو دیکھا۔", "hint_en": "I saw the engineers in the factory.",
            "explanation_ur": "درست جواب: 'الْمُهَنْدِسِينَ' (مفعول بہ منسوب ہے، جمع مذکر سالم میں نصب کی علامت یاء ہے)",
            "explanation_en": "Correct: 'الْمُهَنْدِسِينَ' (Accusative plural marker is yaa)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 24: مَرْجِعُ الْأَعْدَادِ وَالْعُقُودِ (11 - 100)
    # -------------------------------------------------------------
    units[24] = [
        {
            "id": "b2_u24_q1", "book": 2, "unit_num": 24, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): معدود العقود (20 إلى 90)", "badge_en": "Exercise (1): Decades Numbers (20 to 90)",
            "tamreen_title_ar": "اضْبِطْ تَمْيِيزَ أَلْفَاظِ الْعُقُودِ (20 - 90):",
            "tamreen_title_ur": "عقود (بیس سے نوے) کے بعد معدود کا اعراب لگائیں:",
            "tamreen_title_en": "Vowel the counted noun after decades (20-90) as singular accusative:",
            "grammar_goal_ur": "11 سے 99 تک کے اعداد کا معدود ہمیشہ مفرد اور منصوب (زبر والا) ہوتا ہے (طَالِباً)۔", "grammar_goal_en": "Tamyeez of numbers 11-99 is always singular accusative (mansoob).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فِي الْفَصْلِ عِشْرُونَ [ ＿＿＿ ] .",
            "prompt_ur": "عِشْرُونَ کے بعد درست معدود منتخب کریں:",
            "prompt_en": "Select the correct counted noun after 'عِشْرُونَ':",
            "answer": "طَالِباً", "options": ["طَالِباً", "طَالِبٍ", "طَالِبٌ", "طُلَّابٍ"],
            "emoji": "👨‍🎓", "hint_ur": "کلاس میں بیس طالب علم ہیں۔", "hint_en": "In the classroom there are twenty students.",
            "explanation_ur": "درست جواب: 'طَالِباً' (عقود کا تمیز مفرد منصوب ہوتا ہے)",
            "explanation_en": "Correct: 'طَالِباً' (Tamyeez of decades is singular accusative)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 25: الْأَسْمَاءُ الْخَمْسَةُ (أَبٌ، أَخٌ، حَمٌ، فُو، ذُو)
    # -------------------------------------------------------------
    units[25] = [
        {
            "id": "b2_u25_q1", "book": 2, "unit_num": 25, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): رفع الأسماء الخمسة بالواو (أَبُوكَ)", "badge_en": "Exercise (2): Nominative Five Nouns with Waw",
            "tamreen_title_ar": "أَعْرِبِ الْأَسْمَاءَ الْخَمْسَةَ فِي حَالَةِ الرَّفْعِ:",
            "tamreen_title_ur": "حالتِ رفع (مبتدا یا فاعل) میں اسمائے خمسہ کا صیغہ لگائیں:",
            "tamreen_title_en": "Use the Five Nouns in nominative with waw:",
            "grammar_goal_ur": "اسمائے خمسہ جب مضاف ہوں تو حالتِ رفع میں واؤ سے اعراب پاتے ہیں (أَبُوكَ)۔", "grammar_goal_en": "The Five Nouns take waw in nominative case when annexed.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ [ ＿＿＿ ] يَا بِلَالُ؟",
            "prompt_ur": "بلال سے ان کے والد کے بارے میں پوچھنے کے لیے درست لفظ منتخب کریں:",
            "prompt_en": "Select the correct nominative form of 'your father':",
            "answer": "أَبُوكَ", "options": ["أَبُوكَ", "أَبَاكَ", "أَبِيكَ", "أَبُوكِ"],
            "emoji": "🧔", "hint_ur": "اے بلال، تمہارے والد کہاں ہیں؟", "hint_en": "Where is your father, O Bilal?",
            "explanation_ur": "درست جواب: 'أَبُوكَ' (مبتدائے مؤخر مرفوع ہے، اسمائے خمسہ میں رفع کی علامت واؤ ہے)",
            "explanation_en": "Correct: 'أَبُوكَ' (Takes waw in nominative)"
        },
        {
            "id": "b2_u25_q2", "book": 2, "unit_num": 25, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): نصب الأسماء الخمسة بالألف (أَخَاكَ)", "badge_en": "Exercise (3): Accusative Five Nouns with Alif",
            "tamreen_title_ar": "أَعْرِبِ الْأَسْمَاءَ الْخَمْسَةَ فِي حَالَةِ النَّصْبِ:",
            "tamreen_title_ur": "حالتِ نصب (مفعول بہ) میں اسمائے خمسہ کا صیغہ لگائیں:",
            "tamreen_title_en": "Use the Five Nouns in accusative with alif:",
            "grammar_goal_ur": "اسمائے خمسہ حالتِ نصب میں الف سے آتے ہیں (رَأَيْتُ أَخَاكَ)۔", "grammar_goal_en": "The Five Nouns take alif in accusative case when annexed.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَرَأَيْتَ [ ＿＿＿ ] فِي السُّوقِ يَا عَلِيُّ؟",
            "prompt_ur": "علی کے بھائی کو دیکھنے کے لیے درست مفعول منتخب کریں:",
            "prompt_en": "Select the correct accusative form of 'your brother':",
            "answer": "أَخَاكَ", "options": ["أَخَاكَ", "أَخُوكَ", "أَخِيكَ", "أَخٌ"],
            "emoji": "👨", "hint_ur": "کیا تم نے بازار میں اپنے بھائی کو دیکھا اے علی؟", "hint_en": "Did you see your brother in the market, O Ali?",
            "explanation_ur": "درست جواب: 'أَخَاكَ' (مفعول بہ منسوب ہے، اسمائے خمسہ میں نصب کی علامت الف ہے)",
            "explanation_en": "Correct: 'أَخَاكَ' (Takes alif in accusative)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 26: الْفِعْلُ الْمِثَالُ (الْمُعْتَلُّ الْفَاءِ: وَعَدَ، وَصَلَ، وَقَفَ، وَجَدَ)
    # -------------------------------------------------------------
    units[26] = [
        {
            "id": "b2_u26_q1", "book": 2, "unit_num": 26, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): حذف الواو فی مضارع المثال الواوی (يَعِدُ)", "badge_en": "Exercise (2): Dropping Waw in Present Mithal Verb",
            "tamreen_title_ar": "حَوِّلِ الْمِثَالَ الْوَاوِيَّ إِلَى الْمُضَارِعِ:",
            "tamreen_title_ur": "معتل الفاء واوی (وَصَلَ) کا فعل مضارع بنائیں:",
            "tamreen_title_en": "Convert past Mithal verb (with initial waw) to present tense:",
            "grammar_goal_ur": "مثال واوی کے مضارع میں حرفِ علت واؤ حذف ہو جاتی ہے (وَصَلَ -> يَصِلُ)۔", "grammar_goal_en": "In mithal verbs, root waw is omitted in present tense (يَصِلُ).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "وَصَلَ الْقِطَارُ ➔ الْقِطَارُ [ ＿＿＿ ] الْآنَ .",
            "prompt_ur": "وَصَلَ کا درست مضارع منتخب کریں:",
            "prompt_en": "Select the correct present tense form of 'وَصَلَ':",
            "answer": "يَصِلُ", "options": ["يَصِلُ", "يَوْصِلُ", "وَصَلَ", "صِلْ"],
            "emoji": "🚆", "hint_ur": "ٹرین ابھی پہنچ رہی ہے۔", "hint_en": "The train is arriving now.",
            "explanation_ur": "درست جواب: 'يَصِلُ' (مثال واوی کے مضارع میں واؤ گر جاتی ہے)",
            "explanation_en": "Correct: 'يَصِلُ' (Root waw drops in present tense)"
        },
        {
            "id": "b2_u26_q2", "book": 2, "unit_num": 26, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): صیاغتِ امر از فعلِ مثال (قِفْ، ضَعْ)", "badge_en": "Exercise (4): Imperative of Mithal Verb",
            "tamreen_title_ar": "صُغِ الْأَمْرَ مِنْ فِعْلِ الْمِثَالِ الْوَاوِيِّ:",
            "tamreen_title_ur": "وَقَفَ سے فعل امر بنائیں:",
            "tamreen_title_en": "Form imperative from past mithal verb 'وَقَفَ':",
            "grammar_goal_ur": "مثال واوی کے امر میں واؤ اور ہمزہ دونوں نہیں ہوتے، صرف فاء و لام رہتے ہیں (قِفْ)۔", "grammar_goal_en": "Imperative of mithal drops initial waw without hamzah (قِفْ).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "وَقَفَ الرَّجُلُ ➔ يَا أَخِي، [ ＿＿＿ ] هُنَا ! ",
            "prompt_ur": "رکنے کا حکم دینے کے لیے درست امر منتخب کریں:",
            "prompt_en": "Select the correct imperative form of 'وَقَفَ':",
            "answer": "قِفْ", "options": ["قِفْ", "اِيقَفْ", "تَقِفُ", "وَقَفَ"],
            "emoji": "🛑", "hint_ur": "اے میرے بھائی، یہاں رکو!", "hint_en": "O my brother, stop here!",
            "explanation_ur": "درست جواب: 'قِفْ' (وَقَفَ / يَقِفُ سے فعل امر قِفْ بنتا ہے)",
            "explanation_en": "Correct: 'قِفْ' (Imperative of waqafa is qif)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 27: الْفِعْلُ الْأَجْوَفُ (قَالَ/يَقُولُ، بَاعَ/يَبِيعُ، نَامَ/يَنَامُ)
    # -------------------------------------------------------------
    units[27] = [
        {
            "id": "b2_u27_q1", "book": 2, "unit_num": 27, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مضارع الاجوف (يَقُولُ)", "badge_en": "Exercise (2): Present Tense of Ajwaf Verb",
            "tamreen_title_ar": "حَوِّلِ الْفِعْلَ الْأَجْوَفَ إِلَى الْمُضَارِعِ:",
            "tamreen_title_ur": "فعلِ اجوف (قَالَ) کا مضارع بنائیں:",
            "tamreen_title_en": "Convert past ajwaf verb 'قَالَ' to present tense:",
            "grammar_goal_ur": "اجوف واوی میں عین کلمہ کی الف مضارع میں واؤ بن جاتی ہے (قَالَ -> يَقُولُ)۔", "grammar_goal_en": "Middle alif converts to waw in present tense of ajwaf waawi.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "قَالَ الْمُدَرِّسُ ➔ الْمُدَرِّسُ [ ＿＿＿ ] الْحَقَّ .",
            "prompt_ur": "قَالَ کا درست مضارع منتخب کریں:",
            "prompt_en": "Select the present tense form of 'قَالَ':",
            "answer": "يَقُولُ", "options": ["يَقُولُ", "يَقَالُ", "يَقْوُلُ", "قُلْ"],
            "emoji": "🗣️", "hint_ur": "استاد سچ کہتے ہیں۔", "hint_en": "The teacher speaks the truth.",
            "explanation_ur": "درست جواب: 'يَقُولُ' (قَالَ کا مضارع يَقُولُ ہے)",
            "explanation_en": "Correct: 'يَقُولُ' (Present of qaala is yaqoolu)"
        },
        {
            "id": "b2_u27_q2", "book": 2, "unit_num": 27, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): امر از فعل اجوف بحذف حرف العلة (قُلْ، بِعْ)", "badge_en": "Exercise (6): Imperative of Ajwaf Verb (Qul, Bi')",
            "tamreen_title_ar": "صُغِ الْأَمْرَ مِنَ الْفِعْلِ الْأَجْوَفِ عِنْدَ الْتِقَاءِ السَّاكِنَيْنِ:",
            "tamreen_title_ur": "اجوف سے امر بناتے وقت حرفِ علت حذف کرنے کا قاعدہ:",
            "tamreen_title_en": "Form imperative of ajwaf dropping weak vowel to avoid two saakins:",
            "grammar_goal_ur": "اجوف کے امر میں ساکن ملنے کی وجہ سے حرفِ علت گر جاتا ہے (يَقُولُ -> قُلْ)۔", "grammar_goal_en": "Middle weak letter drops in imperative to resolve two saakins (قُلْ).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنْتَ تَقُولُ ➔ يَا عَلِيُّ، [ ＿＿＿ ] الْحَقَّ دَائِماً ! ",
            "prompt_ur": "سچ بولنے کا حکم دینے کے لیے درست امر منتخب کریں:",
            "prompt_en": "Select the correct imperative form of 'تَقُولُ':",
            "answer": "قُلْ", "options": ["قُلْ", "قُولْ", "اُقُولْ", "تَقُلْ"],
            "emoji": "🗣️", "hint_ur": "اے علی، ہمیشہ سچ بولو!", "hint_en": "O Ali, always speak the truth!",
            "explanation_ur": "درست جواب: 'قُلْ' (واؤ اور لام کے التقاء ساکنین کی وجہ سے واؤ گر جاتی ہے)",
            "explanation_en": "Correct: 'قُلْ' (Waw drops due to two saakins)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 28: الْفِعْلُ النَّاقِصُ (دَعَا/يَدْعُو، بَنَى/يَبْنِي، نَسِيَ/يَنْسَى)
    # -------------------------------------------------------------
    units[28] = [
        {
            "id": "b2_u28_q1", "book": 2, "unit_num": 28, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): جزمِ ناقص بحذف حرف العلة (لَمْ يَبْنِ)", "badge_en": "Exercise (3): Jussive of Naaqis Verb by Dropping Weak Letter",
            "tamreen_title_ar": "اجْزِمِ الْفِعْلَ النَّاقِصَ بِـ (لَمْ) مَعَ حَذْفِ حَرْفِ الْعِلَّةِ:",
            "tamreen_title_ur": "ناقص (يَبْنِي) پر 'لَمْ' داخل کر کے حرفِ علت گرائیں:",
            "tamreen_title_en": "Apply jussive to defective verb by dropping final weak letter:",
            "grammar_goal_ur": "فعلِ ناقص میں جزم کی علامت آخری حرفِ علت کا گرنا ہے (لَمْ يَبْنِ)۔", "grammar_goal_en": "Jussive marker in defective verb is omission of final weak letter.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الرَّجُلُ [ ＿＿＿ ] الْبَيْتَ بَعْدُ .",
            "prompt_ur": "گھر نہ بنانے کے لیے درست مجزوم فعل منتخب کریں:",
            "prompt_en": "Select the correct jussive defective verb form:",
            "answer": "لَمْ يَبْنِ", "options": ["لَمْ يَبْنِ", "لَمْ يَبْنِي", "لَمْ يَبْنَ", "مَا بَنَى"],
            "emoji": "🏠", "hint_ur": "آدمی نے ابھی تک گھر نہیں بنایا۔", "hint_en": "The man has not built the house yet.",
            "explanation_ur": "درست جواب: 'لَمْ يَبْنِ' (جزم کی وجہ سے آخری یاء گر جاتی ہے اور کسرہ باقی رہتی ہے)",
            "explanation_en": "Correct: 'لَمْ يَبْنِ' (Weak ending yaa drops in jussive)"
        },
        {
            "id": "b2_u28_q2", "book": 2, "unit_num": 28, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): امر از فعل ناقص بحذف حرف العلة (اُدْعُ)", "badge_en": "Exercise (5): Imperative of Naaqis Verb (Ud'u)",
            "tamreen_title_ar": "صُغِ الْأَمْرَ مِنَ الْفِعْلِ النَّاقِصِ:",
            "tamreen_title_ur": "دَعَا / يَدْعُو سے فعلِ امر بنائیں:",
            "tamreen_title_en": "Form imperative from defective verb 'دَعَا / يَدْعُو':",
            "grammar_goal_ur": "ناقص کے امر میں آخری حرفِ علت گر جاتا ہے (اُدْعُ، اِرْمِ، اِمْشِ)۔", "grammar_goal_en": "Imperative of defective verb drops final weak letter (اُدْعُ).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنْتَ تَدْعُو ➔ [ ＿＿＿ ] رَبَّكَ دَائِماً ! ",
            "prompt_ur": "رب کو پکارنے کا حکم دینے کے لیے درست امر منتخب کریں:",
            "prompt_en": "Select the correct imperative of 'تَدْعُو':",
            "answer": "اُدْعُ", "options": ["اُدْعُ", "اُدْعُو", "اِدْعِ", "تَدْعُ"],
            "emoji": "🤲", "hint_ur": "اپنے رب کو ہمیشہ پکارو!", "hint_en": "Call upon your Lord always!",
            "explanation_ur": "درست جواب: 'اُدْعُ' (امر میں حرفِ علت واؤ گر جاتا ہے)",
            "explanation_en": "Correct: 'اُدْعُ' (Final weak letter waw drops in imperative)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 29: الْفِعْلُ الْمُضَاعَفُ (حَجَّ/يَحُجُّ، عَدَّ/يَعُدُّ، رَدَّ/يَرُدُّ)
    # -------------------------------------------------------------
    units[29] = [
        {
            "id": "b2_u29_q1", "book": 2, "unit_num": 29, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): فکِ ادغام فی الماضی مع ضمائر الرفع المتحركة", "badge_en": "Exercise (3): Unfolding Geminate Verb in Past Tense",
            "tamreen_title_ar": "فُكَّ إِدْغَامَ الْمُضَاعَفِ مَعَ ضَمِيرِ الْمُتَكَلِّمِ (أَنَا):",
            "tamreen_title_ur": "مضاعف (حَجَّ) کو ضمیر 'أنا' سے جوڑتے وقت ادغام کھولیں:",
            "tamreen_title_en": "Unfold geminate verb 'حَجَّ' with 1st person pronoun:",
            "grammar_goal_ur": "مضاعف کے ماضی میں جب تائے فاعل ملائی جائے تو ادغام کھل جاتا ہے (حَجَّ -> حَجَجْتُ)۔", "grammar_goal_en": "Geminate verb splits into two distinct letters before vocalic subject pronouns (حَجَجْتُ).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "حَجَّ أَخِي الْعَامَ الْمَاضِيَ ، وَأَنَا [ ＿＿＿ ] هٰذَا الْعَامَ .",
            "prompt_ur": "أَنَا کے لیے درست فعل منتخب کریں:",
            "prompt_en": "Select the correct verb form for 'أَنَا':",
            "answer": "حَجَجْتُ", "options": ["حَجَجْتُ", "حَجَّيْتُ", "حَجْتُ", "حَجَّتُ"],
            "emoji": "🕋", "hint_ur": "میرے بھائی نے پچھلے سال حج کیا اور میں نے اس سال حج کیا۔", "hint_en": "My brother performed Hajj last year, and I performed Hajj this year.",
            "explanation_ur": "درست جواب: 'حَجَجْتُ' (تائے متکلم ملنے سے ادغام کھل جاتا ہے)",
            "explanation_en": "Correct: 'حَجَجْتُ' (Gemination splits before vocalic suffix)"
        },
        {
            "id": "b2_u29_q2", "book": 2, "unit_num": 29, "tamreen_num": 5,
            "badge_ar": "التَّمْرِينُ (5)", "badge_ur": "مشق (5): امر از مضاعف (جُرَّ، صُبَّ)", "badge_en": "Exercise (5): Imperative of Geminate Verb",
            "tamreen_title_ar": "صُغِ الْأَمْرَ مِنَ الْفِعْلِ الْمُضَاعَفِ:",
            "tamreen_title_ur": "مضاعف (جَرَّ / يَجُرُّ) سے فعل امر بنائیں:",
            "tamreen_title_en": "Form imperative from geminate verb 'جَرَّ / يَجُرُّ':",
            "grammar_goal_ur": "مضاعف کے امر میں فتحہ دے کر تشدید برقرار رکھی جاتی ہے (جُرَّ، عُدَّ)۔", "grammar_goal_en": "Imperative of geminate keeps shaddah with fathah ending (جُرَّ).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا وَلَدُ، [ ＿＿＿ ] هٰذَا الْمَكْتَبَ ! ",
            "prompt_ur": "میز گھسیٹنے کا حکم دینے کے لیے درست امر منتخب کریں:",
            "prompt_en": "Select the correct imperative form of 'يَجُرُّ':",
            "answer": "جُرَّ", "options": ["جُرَّ", "اُجْرُرْ", "جِرَّ", "تَجُرَّ"],
            "emoji": "🗄️", "hint_ur": "اے لڑکے، یہ میز کھینچو / گھسیٹو!", "hint_en": "O boy, pull this desk!",
            "explanation_ur": "درست جواب: 'جُرَّ' (مضاعف کا امر جُرَّ آتا ہے)",
            "explanation_en": "Correct: 'جُرَّ' (Geminate imperative retains doubled consonant with fathah)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 30: إِسْنَادُ الْأَفْعَالِ إِلَى أَلِفِ الِاثْنَيْنِ
    # -------------------------------------------------------------
    units[30] = [
        {
            "id": "b2_u30_q1", "book": 2, "unit_num": 30, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): ماضی مع الف الاثنین (ذَهَبَا)", "badge_en": "Exercise (2): Past Verb with Dual Alif",
            "tamreen_title_ar": "أَسْنِدِ الْفِعْلَ الْمَاضِيَ إِلَى أَلِفِ الِاثْنَيْنِ:",
            "tamreen_title_ur": "ماضی کو الفِ تثنیہ کے ساتھ جوڑیں:",
            "tamreen_title_en": "Conjugate past verb with dual subject pronoun alif:",
            "grammar_goal_ur": "تثنیہ مذکر غائب میں ماضی کے آخر میں الف کا اضافہ ہوتا ہے (ذَهَبَا)۔", "grammar_goal_en": "Past verb takes alif for dual 3rd person masculine subject.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ خَالِدٌ وَحَامِدٌ؟ - [ ＿＿＿ ] إِلَى الْمَكْتَبَةِ .",
            "prompt_ur": "خالد اور حامد کے لیے درست ماضی منتخب کریں:",
            "prompt_en": "Select the correct past dual verb form for Khalid and Hamid:",
            "answer": "ذَهَبَا", "options": ["ذَهَبَا", "ذَهَبُوا", "ذَهَبَ", "ذَهَبَتَا"],
            "emoji": "👬", "hint_ur": "خالد اور حامد کہاں ہیں؟ وہ دونوں لائبریری گئے۔", "hint_en": "Where are Khalid and Hamid? They both went to the library.",
            "explanation_ur": "درست جواب: 'ذَهَبَا' (تثنیہ مذکر غائب کے لیے ذَهَبَا آتا ہے)",
            "explanation_en": "Correct: 'ذَهَبَا' (Dual masculine past ending is -aa)"
        },
        {
            "id": "b2_u30_q2", "book": 2, "unit_num": 30, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مضارع مع الف الاثنین (يَذْهَبَانِ)", "badge_en": "Exercise (3): Present Verb with Dual Alif",
            "tamreen_title_ar": "أَسْنِدِ الْفِعْلَ الْمُضَارِعَ إِلَى أَلِفِ الِاثْنَيْنِ:",
            "tamreen_title_ur": "مضارع کو الفِ تثنیہ اور نونِ اعرابی کے ساتھ جوڑیں:",
            "tamreen_title_en": "Conjugate present verb with dual pronoun and noon:",
            "grammar_goal_ur": "تثنیہ مذکر غائب میں مضارع کے آخر میں الف اور نونِ مکسورہ آتا ہے (يَذْهَبَانِ)۔", "grammar_goal_en": "Present tense dual ending is -aani.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَحْمَدُ وَإِبْرَاهِيمُ [ ＿＿＿ ] إِلَى الْمَسْجِدِ مَعاً .",
            "prompt_ur": "احمد اور ابراہیم کے لیے درست مضارع منتخب کریں:",
            "prompt_en": "Select the correct present dual verb form:",
            "answer": "يَذْهَبَانِ", "options": ["يَذْهَبَانِ", "يَذْهَبُونَ", "يَذْهَبُ", "تَذْهَبَانِ"],
            "emoji": "🕌", "hint_ur": "احمد اور ابراہیم اکٹھے مسجد جاتے ہیں۔", "hint_en": "Ahmad and Ibrahim go to the mosque together.",
            "explanation_ur": "درست جواب: 'يَذْهَبَانِ' (مضارع تثنیہ مذکر غائب کے لیے يَذْهَبَانِ آتا ہے)",
            "explanation_en": "Correct: 'يَذْهَبَانِ' (Dual masculine present ending is -aani)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 31: النَّعْتُ وَالْمَنْعُوتُ (أَوْجُهُ التَّطَابُقِ الْأَرْبَعَةُ)
    # -------------------------------------------------------------
    units[31] = [
        {
            "id": "b2_u31_q1", "book": 2, "unit_num": 31, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تطابق النعت والمنعوت فی الإعراب والتنکیر", "badge_en": "Exercise (2): Concord of Adjective in Case and Indefiniteness",
            "tamreen_title_ar": "عَيِّنِ النَّعْتَ الْمُطَابِقَ لِلْمَنْعُوتِ فِي الْإِعْرَابِ:",
            "tamreen_title_ur": "اعراب اور تنکیر میں منعوت کے مطابق درست نعت لگائیں:",
            "tamreen_title_en": "Match the adjective with noun in case and state:",
            "grammar_goal_ur": "نعت اعراب (زبر/پیش/زیر) اور نکرہ/معرفہ ہونے میں ہمیشہ اپنے منعوت کے تابع ہوتی ہے۔", "grammar_goal_en": "Adjective agrees with qualified noun in case, gender, and definiteness.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أُرِيدُ أَنْ أَشْرَبَ مَاءً [ ＿＿＿ ] .",
            "prompt_ur": "مَاءً (مفعول بہ منصوب، نکرہ) کے لیے درست نعت منتخب کریں:",
            "prompt_en": "Select the correct matching adjective for 'مَاءً':",
            "answer": "بَارِداً", "options": ["بَارِداً", "بَارِدٌ", "بَارِدٍ", "الْبَارِدَ"],
            "emoji": "🥤", "hint_ur": "میں ٹھنڈا پانی پینا چاہتا ہوں۔", "hint_en": "I want to drink cold water.",
            "explanation_ur": "درست جواب: 'بَارِداً' (مَاءً چونکہ منسوب اور نکرہ ہے اس لیے نعت بھی منسوب اور نکرہ ہوگی)",
            "explanation_en": "Correct: 'بَارِداً' (Matches accusative indefinite noun)"
        },
        {
            "id": "b2_u31_q2", "book": 2, "unit_num": 31, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): تطابق النعت فی الجمع والتعریف", "badge_en": "Exercise (3): Concord of Adjective in Plural and Definiteness",
            "tamreen_title_ar": "طَابِقِ النَّعْتَ فِي التَّعْرِيفِ وَالْجَمْعِ:",
            "tamreen_title_ur": "معرفہ اور جمع میں درست نعت کا انتخاب کریں:",
            "tamreen_title_en": "Match adjective with definite plural noun:",
            "grammar_goal_ur": "جمع مذکر عاقل کے لیے نعت جمع مذکر معرفہ آتی ہے (الطُّلَّابُ الْجُدُدُ)۔", "grammar_goal_en": "Adjective for rational masculine plural agrees in plural and definiteness.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَيْنَ الطُّلَّابُ [ ＿＿＿ ] الَّذِينَ جَاءُوا أَمْسِ؟",
            "prompt_ur": "الطُّلَّابُ کے لیے درست صفت منتخب کریں:",
            "prompt_en": "Select the correct adjective matching 'الطُّلَّابُ':",
            "answer": "الْجُدُدُ", "options": ["الْجُدُدُ", "جَدِيدٌ", "الْجَدِيدَةُ", "جُدُداً"],
            "emoji": "👨‍🎓", "hint_ur": "وہ نئے طلبہ کہاں ہیں جو کل آئے تھے؟", "hint_en": "Where are the new students who came yesterday?",
            "explanation_ur": "درست جواب: 'الْجُدُدُ' (الطلاب کے مطابق نعت پر ال بھی آئے گا اور جمع مرفوع ہوگی)",
            "explanation_en": "Correct: 'الْجُدُدُ' (Matches definite rational plural)"
        }
    ]

    return units

if __name__ == "__main__":
    u = get_b2_part3()
    print("Units in part 3:", sorted(u.keys()))
    print("Total Qs in part 3:", sum(len(v) for v in u.values()))
