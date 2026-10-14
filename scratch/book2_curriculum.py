import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_book2_questions():
    questions = []

    def q(uid, tnum, bar, bur, ben, tar, tur, ten, gur, gen, qtype, par, pur, pen, ans, opts, em, hur, hen):
        if ans not in opts:
            opts[0] = ans
        questions.append({
            "id": f"b2_u{uid}_t{tnum}_q{len(questions)+1}",
            "book": 2,
            "unit_num": uid,
            "tamreen_num": tnum,
            "badge_ar": bar,
            "badge_ur": bur,
            "badge_en": ben,
            "tamreen_title_ar": tar,
            "tamreen_title_ur": tur,
            "tamreen_title_en": ten,
            "grammar_goal_ur": gur,
            "grammar_goal_en": gen,
            "type": qtype,
            "strict_tashkeel": True,
            "prompt_ar": par,
            "prompt_ur": pur,
            "prompt_en": pen,
            "answer": ans,
            "options": opts,
            "emoji": em,
            "hint_ur": hur,
            "hint_en": hen,
            "explanation_ur": f"درست جواب: '{ans}' ({gur})",
            "explanation_en": f"Correct answer: '{ans}' ({gen})"
        })

    # UNIT 1
    q(1, 1, "التَّمْرِينُ (1)", "مشق (1): فہمِ متن", "Exercise (1): Reading Comprehension",
      "أجب عن الأسئلة الآتية:", "سوالات کے درست جوابات دیں:", "Answer the following questions:",
      "فہمِ عبارت اور عربی میں جواب دینا", "Answering based on lesson dialogue",
      "dialogue_qa", "مِنْ أَيْنَ هَاشِمٌ؟", "صحیح جواب منتخب کریں:", "Select the correct answer:",
      "هُوَ مِنَ الْهِنْدِ", ["هُوَ مِنَ الْهِنْدِ", "هُوَ مِنَ الْيَابَانِ", "هُوَ مِنَ الصِّينِ", "هُوَ مِنَ الْكُوَيْتِ"], "🇮🇳",
      "ہاشم ہندوستان سے ہے", "Hashim is from India.")
    q(1, 1, "التَّمْرِينُ (1)", "مشق (1): فہمِ متن", "Exercise (1): Reading Comprehension",
      "أجب عن الأسئلة الآتية:", "سوالات کے درست جوابات دیں:", "Answer the following questions:",
      "فہمِ عبارت اور عربی میں جواب دینا", "Answering based on lesson dialogue",
      "dialogue_qa", "بِكَمْ سَاعَةُ هَاشِمٍ؟", "صحیح جواب منتخب کریں:", "Select the correct answer:",
      "هِيَ بِمِائَةِ رِيَالٍ", ["هِيَ بِمِائَةِ رِيَالٍ", "هِيَ بِعَشَرَةِ رِيَالَاتٍ", "هِيَ بِأَلْفِ رِيَالٍ", "هِيَ مَجَّانًا"], "⌚",
      "اس کی گھڑی سو ریال کی ہے", "His watch cost 100 Riyals.")
    q(1, 1, "التَّمْرِينُ (1)", "مشق (1): فہمِ متن", "Exercise (1): Reading Comprehension",
      "أجب عن الأسئلة الآتية:", "سوالات کے درست جوابات دیں:", "Answer the following questions:",
      "فہمِ عبارت اور عربی میں جواب دینا", "Answering based on lesson dialogue",
      "dialogue_qa", "كَمْ أَخًا لِهَاشِمٍ؟", "صحیح جواب منتخب کریں:", "Select the correct answer:",
      "لَهُ ثَلَاثَةُ إِخْوَةٍ", ["لَهُ ثَلَاثَةُ إِخْوَةٍ", "لَهُ أَرْبَعَةُ إِخْوَةٍ", "لَهُ أَخٌ وَاحِدٌ", "لَيْسَ لَهُ إِخْوَةٌ"], "👨‍👦‍👦",
      "ہاشم کے تین بھائی ہیں", "Hashim has three brothers.")
    q(1, 2, "التَّمْرِينُ (2)", "مشق (2): إنّ کے ساتھ ضمائر", "Exercise (2): Pronouns with Inna",
      "أَدْخِلْ (إِنَّ) عَلَى الْجُمَلِ الآتِيَةِ:", "(إِنَّ) کے ساتھ درست ضمیر متصل لگائیں:", "Attach Inna to the sentences:",
      "ضمیر منفصل کو ضمیر متصل میں بدلنا", "Attaching pronouns to Inna",
      "fill_blank", "هُوَ تَاجِرٌ ➔ [ ＿＿＿ ] تَاجِرٌ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "إِنَّهُ", ["إِنَّهُ", "إِنَّهُمْ", "إِنَّكَ", "إِنَّنِي"], "💼",
      "هُوَ سے بنتا ہے: إِنَّهُ", "With 'huwa' it becomes 'innahu'.")
    q(1, 2, "التَّمْرِينُ (2)", "مشق (2): إنّ کے ساتھ ضمائر", "Exercise (2): Pronouns with Inna",
      "أَدْخِلْ (إِنَّ) عَلَى الْجُمَلِ الآتِيَةِ:", "(إِنَّ) کے ساتھ درست ضمیر متصل لگائیں:", "Attach Inna to the sentences:",
      "ضمیر منفصل کو ضمیر متصل میں بدلنا", "Attaching pronouns to Inna",
      "fill_blank", "أَنَا طَالِبٌ ➔ [ ＿＿＿ ] طَالِبٌ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "إِنَّنِي", ["إِنَّنِي", "إِنَّهُ", "إِنَّكَ", "إِنَّكُمْ"], "👨‍🎓",
      "أَنَا سے بنتا ہے: إِنَّنِي یا إِنِّي", "With 'ana' it becomes 'innanee'.")
    q(1, 3, "التَّمْرِينُ (3)", "مشق (3): اسمِ إنّ کا اعراب", "Exercise (3): Case of Ism Inna",
      "أَدْخِلْ (إِنَّ) وَاضْبِطْ أَوَاخِرَ الْكَلِمَاتِ:", "اسمِ إنّ کا درست اعراب (نصب) منتخب کریں:", "Case ending of Ism Inna (Accusative):",
      "اسمِ إنّ ہمیشہ منصوب (فتحة) ہوتا ہے", "Ism Inna is always mansoob (takes fathah)",
      "fill_blank", "الدَّرْسُ صَعْبٌ ➔ إِنَّ [ ＿＿＿ ] صَعْبٌ .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "الدَّرْسَ", ["الدَّرْسَ", "الدَّرْسُ", "الدَّرْسِ", "الدَّرْسْ"], "📖",
      "اسمِ إنّ پر زبر (فتحة) آتا ہے", "Ism Inna takes fathah: ad-darsa.")
    q(1, 4, "التَّمْرِينُ (4)", "مشق (4): اسم التفضیل (أَفْعَلُ مِنْ)", "Exercise (4): Comparative (Af'alu min)",
      "تَأَمَّلِ الْمِثَالَيْنِ، ثُمَّ كَوِّنْ جُمَلًا مِثْلَهُمَا:", "اسمِ تفضیل کا درست صیغہ منتخب کریں:", "Form the comparative degree (Af'alu min):",
      "صفت سے اسمِ تفضیل بنانا", "Forming comparatives on pattern Af'alu",
      "fill_blank", "حَامِدٌ طَوِيلٌ وَعَلِيٌّ قَصِيرٌ ➔ حَامِدٌ [ ＿＿＿ ] مِنْ عَلِيٍّ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "أَطْوَلُ", ["أَطْوَلُ", "طَوِيلٌ", "أَقْصَرُ", "طَوِيلَةٌ"], "📏",
      "طويل کا اسم تفضیل أَطْوَلُ ہے", "Comparative of taweel is atwalu.")
    q(1, 5, "التَّمْرِينُ (5)", "مشق (5): (ذُو) کا استعمال", "Exercise (5): Using 'Dhu' (Possessor of)",
      "تَأَمَّلِ الأَمْثِلَةَ الآتِيَةَ لِـ (ذُو):", "(ذُو) کے بعد والے اسم کا اعراب منتخب کریں:", "Select the case of the noun following Dhu:",
      "ذو کے بعد اسم مضاف الیہ (مجرور) ہوتا ہے", "The noun after Dhu is always majroor",
      "fill_blank", "هَذَا الرَّجُلُ ذُو [ ＿＿＿ ] كَثِيرٍ .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "مَالٍ", ["مَالٍ", "مَالٌ", "مَالًا", "مَالْ"], "💰",
      "ذو کے بعد مضاف الیہ مجرور (زیر): مَالٍ", "Majroor after Dhu: maalin.")
    q(1, 6, "التَّمْرِينُ (6)", "مشق (6): (غَالٍ) اور (غَالِيَةٌ)", "Exercise (6): Using Ghaalin / Ghaaliyah",
      "أَكْمِلِ الْجُمَلَ بِوَضْعِ (غَالٍ) أَوْ (غَالِيَةٌ):", "مذکر یا مؤنث کے مطابق درست صفت لگائیں:", "Select Ghaalin (masc.) or Ghaaliyah (fem.):",
      "مذکر کے لیے غالٍ اور مؤنث کے لیے غالية", "Ghaalin for masc, Ghaaliyah for fem",
      "fill_blank", "هَذَا الْقَلَمُ [ ＿＿＿ ] جِدًّا .", "صحیح لفظ منتخب کریں:", "Select the correct word:",
      "غَالٍ", ["غَالٍ", "غَالِيَةٌ", "غَالِي", "غَالِيًا"], "🖊️",
      "قلم مذکر ہے اس لیے: غَالٍ", "Al-Qalam is masculine: ghaalin.")

    # UNIT 2
    q(2, 1, "التَّمْرِينُ (1)", "مشق (1): فہمِ عبارت", "Exercise (1): Reading Comprehension",
      "أجب عن الأسئلة الآتية:", "سبق کی روشنی میں جواب دیں:", "Answer based on the dialogue:",
      "عربی فہم اور جواب", "Comprehension of dialogue",
      "dialogue_qa", "مِنْ أَيْنَ هِشَامٌ؟", "صحیح جواب منتخب کریں:", "Select the correct answer:",
      "هُوَ مِنْ وَاشِنْطُنَ", ["هُوَ مِنْ وَاشِنْطُنَ", "هُوَ مِنَ الْهِنْدِ", "هُوَ مِنْ لَنْدَنَ", "هُوَ مِنَ الْيَابَانِ"], "🏛️",
      "ہشام واشنگٹن سے ہے", "Hisham is from Washington.")
    q(2, 2, "التَّمْرِينُ (2)", "مشق (2): تصریفِ ليس", "Exercise (2): Conjugation of Laysa",
      "أَدْخِلْ (لَيْسَ) عَلَى الْجُمَلِ الآتِيَةِ:", "فاعل کے مطابق (ليس) کا درست صیغہ لگائیں:", "Conjugate Laysa with the appropriate pronoun:",
      "مختلف فاعل کے ساتھ ليس کا تصریف", "Conjugating Laysa correctly",
      "fill_blank", "الطُّلَّابُ [ ＿＿＿ ] فِي الْفَصْلِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لَيْسُوا", ["لَيْسُوا", "لَيْسَ", "لَيْسَتْ", "لَسْنَ"], "👨‍🎓",
      "جمع مذکر غائب کے لیے: لَيْسُوا", "Masculine plural: laysoo.")
    q(2, 3, "التَّمْرِينُ (3)", "مشق (3): خبرِ ليس پر باء زائدہ", "Exercise (3): Khabar Laysa with Baa",
      "أَدْخِلْ (لَيْسَ) مَعَ الْبَاءِ الزَّائِدَةِ:", "خبرِ ليس پر باء کا درست اعراب:", "Predicate of Laysa with preposition 'bi-':",
      "باء زائدہ کے بعد خبر مجرور لفظاً ہوتی ہے", "Khabar is majroor with reinforcing baa",
      "fill_blank", "الْمَاءُ بَارِدٌ ➔ لَيْسَ الْمَاءُ [ ＿＿＿ ] .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "بِبَارِدٍ", ["بِبَارِدٍ", "بِبَارِدٌ", "بِبَارِدًا", "بَارِدٌ"], "💧",
      "باء کے ساتھ مجرور: بِبَارِدٍ", "Majroor with baa: bi-baaredin.")

    # UNIT 3
    q(3, 1, "التَّمْرِينُ (1)", "مشق (1): (لَكِنَّ) کا استعمال", "Exercise (1): Using 'Lakinna' (But)",
      "اِرْبِطْ بَيْنَ الْجُمْلَتَيْنِ بِـ (لَكِنَّ):", "(لَكِنَّ) کے بعد اسم کا اعراب (نصب):", "Join sentences with Lakinna and inflect its noun:",
      "لكنّ کے بعد اسم منصوب (فتحة) ہوتا ہے", "Noun after lakinna is mansoob",
      "fill_blank", "الطُّلَّابُ كَثِيرُونَ [ ＿＿＿ ] الْفَصْلَ صَغِيرٌ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "وَلَكِنَّ", ["وَلَكِنَّ", "وَإِنَّ", "وَكَأَنَّ", "وَلَيْتَ"], "🏫",
      "استدراک کے لیے: وَلَكِنَّ", "For contrast: walakinna.")
    q(3, 2, "التَّمْرِينُ (2)", "مشق (2): (كَأَنَّ) برائے تشبیہ", "Exercise (2): Using 'Ka-anna' (As if)",
      "أَدْخِلْ (كَأَنَّ) عَلَى الْجُمَلِ الآتِيَةِ:", "(كَأَنَّ) کا درست استعمال:", "Use Ka-anna (similarity / assumption):",
      "تشبیہ کے لیے كأنّ کا استعمال", "Using ka-anna for similitude",
      "fill_blank", "هُوَ مَرِيضٌ ➔ [ ＿＿＿ ] مَرِيضٌ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "كَأَنَّهُ", ["كَأَنَّهُ", "إِنَّهُ", "لَكِنَّهُ", "لَعَلَّهُ"], "🤒",
      "گویا کہ وہ بیمار ہے: كَأَنَّهُ مَرِيضٌ", "As if he is sick: ka-annahu mareedun.")
    q(3, 3, "التَّمْرِينُ (3)", "مشق (3): ترتیبی اعداد", "Exercise (3): Ordinal Numbers",
      "اِنْعَتِ الأَسْمَاءَ بِالْعَدَدِ التَّرْتِيبِيِّ:", "صحیح ترتیبی عدد منتخب کریں:", "Select the correct ordinal number:",
      "ترتیبی عدد صفت بن کر موصوف کے مطابق ہوتا ہے", "Ordinal number matches noun in gender and case",
      "fill_blank", "قَرَأْتُ الدَّرْسَ [ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "الثَّالِثَ", ["الثَّالِثَ", "الثَّالِثُ", "الثَّلَاثَةَ", "ثَلَاثَةَ"], "📗",
      "الدرس کی صفت منصوب: الدَّرْسَ الثَّالِثَ", "Matching accusative: ad-darsa ath-thaalitha.")

    # UNIT 4
    q(4, 1, "التَّمْرِينُ (1)", "مشق (1): فعل ماضی کی گردان", "Exercise (1): Past Tense Conjugation",
      "ضَعِ الْفِعْلَ (ذَهَبَ) مَعَ الضَّمِيرِ الْمُنَاسِبِ:", "فاعل کے مطابق فعل ماضی کا درست صیغہ لگائیں:", "Conjugate past verb with the subject:",
      "ماضی کے صیغے اور ضمائرِ رفع متصلہ", "Conjugating past verbs with attached pronouns",
      "fill_blank", "الطُّلَّابُ [ ＿＿＿ ] إِلَى الْمَلْعَبِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "ذَهَبُوا", ["ذَهَبُوا", "ذَهَبَ", "ذَهَبَتْ", "ذَهَبْنَ"], "⚽",
      "جمع مذکر کے لیے: ذَهَبُوا", "Masculine plural: dhahaboo.")
    q(4, 2, "التَّمْرِينُ (2)", "مشق (2): ماضی کی نفی (مَا)", "Exercise (2): Negation of Past with 'Maa'",
      "أَجِبْ عَنِ الأَسْئِلَةِ بِالنَّفْيِ مُسْتَعْمِلًا (مَا):", "ماضی کی نفی کے لیے (مَا) کا استعمال:", "Negate past tense using 'Maa':",
      "ماضی کی نفی حرفِ 'ما' سے کی جاتی ہے", "Past tense is negated with 'Maa'",
      "fill_blank", "أَذَهَبْتَ إِلَى السُّوقِ؟ ➔ لَا، [ ＿＿＿ ] إِلَى السُّوقِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "مَا ذَهَبْتُ", ["مَا ذَهَبْتُ", "لَا أَذْهَبُ", "لَمْ أَذْهَبْ", "لَسْتُ ذَاهِبًا"], "🛒",
      "ماضی کی نفی: مَا ذَهَبْتُ (میں نہیں گیا)", "Negated past: maa dhahabtu.")

    # UNIT 5
    q(5, 1, "التَّمْرِينُ (1)", "مشق (1): فاعل اور مفعول بہ کا اعراب", "Exercise (1): Subject and Object Case Endings",
      "عَيِّنِ الْفَاعِلَ وَالْمَفْعُولَ بِهِ وَاضْبِطْهُمَا:", "فاعل پر پیش اور مفعول پر زبر کا تعین کریں:", "Identify Faa'il (nominative) and Maf'ool (accusative):",
      "فاعل مرفوع (ضمة) اور مفعول به منصوب (فتحة) ہوتا ہے", "Faa'il takes dammah, Maf'ool takes fathah",
      "fill_blank", "قَرَأَ [ ＿＿＿ ] الْقُرْآنَ .", "صحیح فاعل منتخب کریں:", "Select the correct subject (Faa'il):",
      "الْوَلَدُ", ["الْوَلَدُ", "الْوَلَدَ", "الْوَلَدِ", "الْوَلَدْ"], "📖",
      "فاعل ہمیشہ مرفوع (پیش) ہوتا ہے: الْوَلَدُ", "Faa'il is marfoo': al-waladu.")
    q(5, 2, "التَّمْرِينُ (2)", "مشق (2): جملہ فعلیہ میں مفعول بہ", "Exercise (2): Object in Verbal Sentence",
      "اِجْعَلِ الْكَلِمَةَ مَفْعُولًا بِهِ مَضْبُوطًا:", "لفظ کو مفعول بہ بنا کر درست اعراب لگائیں:", "Make the word a direct object with correct diacritics:",
      "مفعول بہ پر فتحة (زبر) دینا", "Applying fathah to direct objects",
      "fill_blank", "كَتَبَ حَامِدٌ [ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "الدَّرْسَ", ["الدَّرْسَ", "الدَّرْسُ", "الدَّرْسِ", "الدَّرْسْ"], "✍️",
      "مفعول بہ منصوب: الدَّرْسَ", "Accusative object: ad-darsa.")

    # UNIT 6
    q(6, 1, "التَّمْرِينُ (1)", "مشق (1): فعل کے ساتھ مفعول بہ ضمیر", "Exercise (1): Object Pronouns with Verbs",
      "صِلِ الضَّمِيرَ بِالْفِعْلِ الْمَاضِي:", "فعل کے ساتھ ضمیر نصب متصل لگائیں:", "Attach the object pronoun to the verb:",
      "ضمیر متصل مفعول بہ بن کر فعل سے جڑتی ہے", "Pronouns attached to verbs serve as objects",
      "fill_blank", "رَأَيْتُ حَامِدًا ➔ رَأَيْتُـ[ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "ـهُ", ["ـهُ", "ـهَا", "ـهُمْ", "ـكَ"], "👁️",
      "حامد مذکر کے لیے: رَأَيْتُهُ", "For singular masc: ra'aytuhu.")
    q(6, 2, "التَّمْرِينُ (2)", "مشق (2): مؤنث ضمیر مفعول", "Exercise (2): Feminine Object Pronoun",
      "صِلِ الضَّمِيرَ بِالْفِعْلِ الْمَاضِي:", "مؤنث اسم کی جگہ درست ضمیر لگائیں:", "Attach the feminine object pronoun:",
      "مؤنث مفعول کے لیے 'ها' کا استعمال", "Using '-ha' for feminine object",
      "fill_blank", "غَسَلَتْ آمِنَةُ السَّيَّارَةَ ➔ غَسَلَتْـ[ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "ـهَا", ["ـهَا", "ـهُ", "ـهُمْ", "ـكِ"], "🚗",
      "گاڑی مؤنث ہے اس لیے: غَسَلَتْهَا", "Car is feminine: ghasalat-haa.")

    # UNIT 7
    q(7, 1, "التَّمْرِينُ (1)", "مشق (1): نون النسوۃ کا استعمال", "Exercise (1): Using Noon an-Niswa",
      "أَسْنِدِ الْفِعْلَ إِلَى نُونِ النِّسْوَةِ:", "جمع مؤنث کے ساتھ فعل ماضی کو جوڑیں:", "Attach the verb to Noon an-Niswa (fem. plural):",
      "جمع مؤنث کے فاعل کے ساتھ فعل پر نون النسوۃ لانا", "Noon an-niswa marks feminine plural subject",
      "fill_blank", "الطَّالِبَاتُ [ ＿＿＿ ] الْفَصْلَ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "دَخَلْنَ", ["دَخَلْنَ", "دَخَلُوا", "دَخَلَتْ", "دَخَلْتُمْ"], "🚪",
      "جمع مؤنث کے لیے: دَخَلْنَ", "Feminine plural: dakhalna.")
    q(7, 2, "التَّمْرِينُ (2)", "مشق (2): ضمیر مفعول جمع مؤنث (ـهُنَّ)", "Exercise (2): Plural Fem. Object Pronoun (-hunna)",
      "صِلِ الضَّمِيرَ (ـهُنَّ) بِالْفِعْلِ:", "جمع مؤنث غائب کے لیے ضمیر مفعول لگائیں:", "Attach object pronoun -hunna to the verb:",
      "جمع مؤنث کے لیے ضمیر متصل 'ـهنّ' آتی ہے", "Object pronoun for feminine plural is -hunna",
      "fill_blank", "رَأَيْتُ الطَّالِبَاتِ ➔ رَأَيْتُـ[ ＿＿＿ ] فِي الْمَكْتَبَةِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "ـهُنَّ", ["ـهُنَّ", "ـهُمْ", "ـهَا", "ـكُنَّ"], "👩‍🎓",
      "جمع مؤنث کے لیے: رَأَيْتُهُنَّ", "For female plural: ra'aytuhunna.")

    # UNIT 8
    q(8, 1, "التَّمْرِينُ (1)", "مشق (1): فاعل جمع اور فعل کا صیغہ", "Exercise (1): Verbs with Plural Subjects",
      "طَابِقْ بَيْنَ الْفِعْلِ وَالْفَاعِلِ:", "جملے کے آغاز میں فعل کے صیغے کا تعین:", "Verb agreement at the start of sentence:",
      "فعل جملے کے شروع میں ہو تو ہمیشہ مفرد رہتا ہے", "Verb at sentence start remains singular",
      "fill_blank", "[ ＿＿＿ ] الطُّلَّابُ إِلَى الْمَسْجِدِ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "ذَهَبَ", ["ذَهَبَ", "ذَهَبُوا", "يَذْهَبُونَ", "ذَهَبْتُمْ"], "🕌",
      "فاعل ظاہر ہو تو فعل مفرد رہے گا: ذَهَبَ الطُّلَّابُ", "Verb stays singular before overt subject: dhahaba at-tullaabu.")
    q(8, 2, "التَّمْرِينُ (2)", "مشق (2): جملہ اسمیہ میں مطابقت", "Exercise (2): Subject-Verb Agreement in Nominal Sentences",
      "طَابِقْ بَيْنَ الْمُبْتَدَإِ وَالْخَبَرِ الْفِعْلِيِّ:", "مبتدا جمع ہو تو فعل بھی جمع لائیں:", "When plural subject precedes, verb must be plural:",
      "فاعل پہلے آ جائے تو فعل میں ضمیر جمع لانا لازم ہے", "Post-subject verb matches in number and gender",
      "fill_blank", "الطُّلَّابُ [ ＿＿＿ ] إِلَى الْمَسْجِدِ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "ذَهَبُوا", ["ذَهَبُوا", "ذَهَبَ", "يَذْهَبُ", "ذَهَبَتْ"], "🕌",
      "مبتدا کے بعد فعل جمع ہوگا: الطُّلَّابُ ذَهَبُوا", "Matches plural subject: at-tullaabu dhahaboo.")

    # UNIT 9
    q(9, 1, "التَّمْرِينُ (1)", "مشق (1): ادواتِ استفہام (مَتَى)", "Exercise (1): Interrogative 'Mataa' (When)",
      "اخْتَرِ اسْمَ الِاسْتِفْهَامِ الْمُنَاسِبَ:", "وقت کے لیے درست سوالیہ لفظ لگائیں:", "Select the correct interrogative for time:",
      "وقت پوچھنے کے لیے 'مَتَى' کا استعمال", "'Mataa' is used to ask about time",
      "fill_blank", "[ ＿＿＿ ] رَجَعْتَ مِنَ الْمَدْرَسَةِ؟ ➔ رَجَعْتُ فِي السَّاعَةِ الثَّانِيَةِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "مَتَى", ["مَتَى", "أَيْنَ", "كَيْفَ", "مَاذَا"], "⏰",
      "وقت کے سوال کے لیے: مَتَى (کب)", "To ask when: mataa.")
    q(9, 2, "التَّمْرِينُ (2)", "مشق (2): ادواتِ استفہام (لِمَاذَا)", "Exercise (2): Interrogative 'Limaadhaa' (Why)",
      "اخْتَرِ اسْمَ الِاسْتِفْهَامِ لِلسَّبَبِ:", "وجہ اور سبب پوچھنے کے لیے سوالیہ لفظ:", "Select interrogative for asking reasons:",
      "سبب پوچھنے کے لیے 'لِمَاذَا' (کیوں) کا استعمال", "'Limaadhaa' asks for causes/reasons",
      "fill_blank", "[ ＿＿＿ ] غِبْتَ أَمْسِ يَا عَمَّارُ؟ ➔ لِأَنِّي كُنْتُ مَرِيضًا .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لِمَاذَا", ["لِمَاذَا", "مَتَى", "أَيْنَ", "مَنْ"], "❓",
      "وجہ پوچھنے کے لیے: لِمَاذَا (کیوں)", "To ask why: limaadhaa.")

    # UNIT 10
    q(10, 1, "التَّمْرِينُ (1)", "مشق (1): مضارع کی گردان (مفرد)", "Exercise (1): Present Tense Singular Conjugation",
      "صَرِّفِ الْفِعْلَ الْمُضَارِعَ مَعَ الضَّمِيرِ:", "فاعل کے مطابق مضارع کا درست صیغہ لگائیں:", "Conjugate present tense verb for the subject:",
      "مضارع میں حروف اتین (أ، ن، ي، ت) کا استعمال", "Present tense prefixes (a-, na-, ya-, ta-)",
      "fill_blank", "حَامِدٌ [ ＿＿＿ ] إِلَى الْمَسْجِدِ كُلَّ يَوْمٍ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "يَذْهَبُ", ["يَذْهَبُ", "تَذْهَبُ", "أَذْهَبُ", "نَذْهَبُ"], "🕌",
      "مذکر غائب کے لیے یاء: يَذْهَبُ", "3rd person masc singular: yadhhabu.")
    q(10, 2, "التَّمْرِينُ (2)", "مشق (2): متکلم کا مضارع (أَفْعَلُ)", "Exercise (2): 1st Person Present Verb",
      "صَرِّفِ الْمُضَارِعَ لِلْمُتَكَلِّمِ:", "واحد متکلم (أَنَا) کے لیے مضارع کا صیغہ:", "Conjugate present verb for 'Ana' (1st person singular):",
      "واحد متکلم میں ہمزہ آتا ہے: أَفْعَلُ", "1st person singular takes prefix Alif: af'alu",
      "fill_blank", "أَنَا [ ＿＿＿ ] كِتَابَ اللَّهِ كُلَّ صَبَاحٍ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "أَقْرَأُ", ["أَقْرَأُ", "يَقْرَأُ", "تَقْرَأُ", "نَقْرَأُ"], "📖",
      "متکلم کے لیے ہمزہ: أَقْرَأُ (میں پڑھتا ہوں)", "1st person: aqra'u.")

    # UNIT 11
    q(11, 1, "التَّمْرِينُ (1)", "مشق (1): مضارع برائے جمع مذکر", "Exercise (1): Present Tense Masc. Plural",
      "صَرِّفِ الْمُضَارِعَ لِلْجَمْعِ:", "جمع مذکر کے لیے مضارع کا صیغہ:", "Conjugate present verb for plural subject:",
      "جمع مذکر غائب میں واو اور نون (يَفْعَلُونَ) کا اضافہ", "Masculine plural ending in -oona",
      "fill_blank", "الطُّلَّابُ [ ＿＿＿ ] كُرَةَ الْقَدَمِ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "يَلْعَبُونَ", ["يَلْعَبُونَ", "يَلْعَبُ", "تَلْعَبُونَ", "لَعِبُوا"], "⚽",
      "جمع مذکر غائب: يَلْعَبُونَ", "Masculine plural: yal'aboona.")
    q(11, 2, "التَّمْرِينُ (2)", "مشق (2): مضارع کی نفی (لَا)", "Exercise (2): Negation of Present with 'Laa'",
      "انْفِ الْفِعْلَ الْمُضَارِعَ بِـ (لَا):", "مضارع کی نفی کے لیے حرف منتخب کریں:", "Negate present tense with 'Laa':",
      "مضارع کی عام نفی حرفِ 'لَا' سے ہوتی ہے", "Present tense is negated with 'Laa'",
      "fill_blank", "أَنَا [ ＿＿＿ ] أَشْرَبُ الْقَهْوَةَ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لَا", ["لَا", "مَا", "لَمْ", "لَنْ"], "☕",
      "مضارع کی نفی: لَا أَشْرَبُ", "Negating present: laa ashrabu.")

    # UNIT 12
    q(12, 1, "التَّمْرِينُ (1)", "مشق (1): مضارع برائے واحد مؤنث مخاطب", "Exercise (1): Present Tense Fem. 2nd Person (Taf'aleena)",
      "خَاطِبِ الْمُؤَنَّثَ بِالْفِعْلِ الْمُضَارِعِ:", "واحد مؤنث مخاطب کے لیے مضارع کا صیغہ لگائیں:", "Conjugate present verb for female addressee:",
      "واحد مؤنث مخاطب پر یائے مخاطبہ اور نون: تَفْعَلِينَ", "Feminine singular addressee: taf'aleena",
      "fill_blank", "مَاذَا [ ＿＿＿ ] يَا سُعَادُ؟", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "تَكْتُبِينَ", ["تَكْتُبِينَ", "تَكْتُبُ", "يَكْتُبْنَ", "كَتَبْتِ"], "✍️",
      "مؤنث مخاطب کے لیے: تَكْتُبِينَ", "For female addressee: taktubeena.")
    q(12, 2, "التَّمْرِينُ (2)", "مشق (2): مضارع برائے جمع مؤنث مخاطب", "Exercise (2): Present Tense Fem. Plural (Taf'alna)",
      "صَرِّفِ الْمُضَارِعَ لِجَمْعِ الإِنَاثِ الْمُخَاطَبَاتِ:", "جمع مؤنث مخاطب کے لیے نون النسوۃ کا صیغہ:", "Conjugate present verb for female plural addressees:",
      "جمع مؤنث مخاطب میں تاء اور نون النسوۃ: تَفْعَلْنَ", "Feminine plural addressees: taf'alna",
      "fill_blank", "أَيْنَ [ ＿＿＿ ] يَا بَنَاتُ؟", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "تَذْهَبْنَ", ["تَذْهَبْنَ", "تَذْهَبُونَ", "يَذْهَبْنَ", "تَذْهَبِينَ"], "👧",
      "جمع مؤنث مخاطب: تَذْهَبْنَ", "Female plural addressees: tadhhabna.")

    # UNIT 13
    q(13, 1, "التَّمْرِينُ (1)", "مشق (1): سین استقبال (سَـ)", "Exercise (1): Future Particle 'Sa-'",
      "اسْتَعْمِلِ السِّينَ لِلْمُسْتَقْبَلِ:", "مستقبل قریب کے لیے سین کا استعمال:", "Using prefix Sa- for near future:",
      "مضارع پر سین داخل ہو کر مستقبل کا معنی دیتا ہے", "Prefix 'sa-' designates future tense",
      "fill_blank", "[ ＿＿＿ ] أَذْهَبُ إِلَى مَكَّةَ غَدًا إِنْ شَاءَ اللَّهُ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "سَـ", ["سَـ", "قَدْ", "لَمْ", "مَا"], "🕋",
      "مستقبل کے لیے: سَأَذْهَبُ (میں جاؤں گا)", "Future prefix: sa-adhhabu.")
    q(13, 2, "التَّمْرِينُ (2)", "مشق (2): سَوْفَ لِلْمُسْتَقْبَلِ الْبَعِيدِ", "Exercise (2): Future Particle 'Sawfa'",
      "اسْتَعْمِلْ (سَوْفَ) لِلْمُسْتَقْبَلِ:", "مستقبل کے لیے سوف کا استعمال:", "Using 'Sawfa' for future action:",
      "سوف مضارع سے پہلے الگ کلمہ بن کر مستقبل کا معنی دیتا ہے", "'Sawfa' precedes the verb as a standalone particle",
      "fill_blank", "{ كَلَّا [ ＿＿＿ ] تَعْلَمُونَ } .", "صحیح قرآنی کلمہ منتخب کریں:", "Select the correct Quranic word:",
      "سَوْفَ", ["سَوْفَ", "سَـ", "قَدْ", "لَنْ"], "📖",
      "قرآن مجید میں: كَلَّا سَوْفَ تَعْلَمُونَ", "In Quran: kallaa sawfa ta'lamoona.")

    # UNIT 14
    q(14, 1, "التَّمْرِينُ (1)", "مشق (1): ثلاثی مجرد کے ابواب (نَظَرَ، جَلَسَ)", "Exercise (1): Triliteral Verb Patterns",
      "هَاتِ مُضَارِعَ الأَفْعَالِ الآتِيَةِ:", "ماضی سے صحیح مضارع منتخب کریں:", "Select correct present tense according to verb bab:",
      "ماضی اور مضارع میں عین کلمے کی حرکت کی پہچان", "Recognizing middle root vowel changes in Mudari'",
      "fill_blank", "نَظَرَ ➔ هُوَ [ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "يَنْظُرُ", ["يَنْظُرُ", "يَنْظِرُ", "يَنْظَرُ", "نَاظِرٌ"], "👁️",
      "نظر ینظُر (باب نصر ینصُر)", "Nazara yanzuru (Bab Nasara).")
    q(14, 2, "التَّمْرِينُ (2)", "مشق (2): باب فَعَلَ يَفْعَلُ (فَتَحَ، ذَهَبَ)", "Exercise (2): Verb Pattern Fa'ala Yaf'alu",
      "هَاتِ مُضَارِعَ (فَتَحَ) وَ(ذَهَبَ):", "عین کلمے پر فتحہ والے مضارع کی پہچان:", "Verbs with fathah on middle radical in past and present:",
      "فتح اور ذہب باب فتح یفتح سے ہیں (دونوں میں زبر)", "Fataha and dhahaba have fathah on middle letter in both tenses",
      "fill_blank", "فَتَحَ الْوَلَدُ الْبَابَ ➔ هُوَ [ ＿＿＿ ] الْبَابَ .", "صحیح مضارع منتخب کریں:", "Select the correct present verb:",
      "يَفْتَحُ", ["يَفْتَحُ", "يَفْتِحُ", "يَفْتُحُ", "فَاتِحٌ"], "🚪",
      "فتح کا مضارع: يَفْتَحُ (زبر کے ساتھ)", "Mudari' of fataha is yaftahu.")

    # UNIT 15
    q(15, 1, "التَّمْرِينُ (1)", "مشق (1): فعل امر کی ساخت (اكْتُبْ)", "Exercise (1): Imperative Verb Formation",
      "صُغْ فِعْلَ الأَمْرِ مِنَ الْمُضَارِعِ:", "مضارع سے فعل امر کا درست صیغہ بنائیں:", "Form the imperative verb from the present tense:",
      "حرف مضارع گرا کر آخر کو ساکن اور شروع میں ہمزہ وصل لانا", "Forming imperative with hamzat al-wasl and sukoon",
      "fill_blank", "تَكْتُبُ ➔ يَا عَلِيُّ [ ＿＿＿ ] الدَّرْسَ ! ", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "اكْتُبْ", ["اكْتُبْ", "تَكْتُبْ", "كَتَبَ", "اكْتُبُ"], "✍️",
      "تکتُب سے امر: اكْتُبْ (پیش کے ساتھ)", "Imperative of taktubu is uktub.")
    q(15, 2, "التَّمْرِينُ (2)", "مشق (2): امر میں ہمزہ وصل کا کسرہ (اجْلِسْ)", "Exercise (2): Imperative with Kasrah on Wasl",
      "صُغِ الأَمْرَ مَعَ كَسْرِ هَمْزَةِ الْوَصْلِ:", "مکسور العین مضارع سے امر بنائیں:", "When middle vowel is kasrah or fathah, hamzat al-wasl takes kasrah:",
      "جب مضارع کا عین کلمہ مکسور ہو تو امر کا ہمزہ مکسور (زیر) ہوتا ہے", "Hamzat al-wasl takes kasrah if middle radical is not dammah",
      "fill_blank", "تَجْلِسُ ➔ يَا حَامِدُ [ ＿＿＿ ] هُنَا ! ", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "اجْلِسْ", ["اجْلِسْ", "اجْلُسْ", "تَجْلِسْ", "جَلَسَ"], "🪑",
      "تجلِس سے امر: اجْلِسْ (زیر کے ساتھ)", "Imperative of yajlisu is ijlis.")

    # UNIT 16
    q(16, 1, "التَّمْرِينُ (1)", "مشق (1): امر برائے مؤنث (افْعَلِي)", "Exercise (1): Feminine Imperative (If'alee)",
      "صُغِ الأَمْرَ لِلْمُؤَنَّثِ الْمُخَاطَبَةِ:", "مؤنث کے لیے یائے مخاطبہ کا اضافہ:", "Add suffix -ee for female singular imperative:",
      "مؤنث مخاطب کے امر میں یائے مخاطبہ آتی ہے", "Feminine singular imperative ends in -ee",
      "fill_blank", "يَا مَرْيَمُ [ ＿＿＿ ] الْقُرْآنَ ! ", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "اقْرَئِي", ["اقْرَئِي", "اقْرَأْ", "اقْرَؤُوا", "تَقْرَئِينَ"], "📖",
      "مؤنث کے لیے یائے مخاطبہ: اقْرَئِي", "Feminine imperative: iqra'ee.")
    q(16, 2, "التَّمْرِينُ (2)", "مشق (2): امر برائے جمع مذکر (افْعَلُوا)", "Exercise (2): Masc. Plural Imperative (If'aloo)",
      "صُغِ الأَمْرَ لِجَمْعِ الذُّكُورِ:", "جمع مذکر کے لیے واو الجماعة کا اضافہ:", "Add suffix -oo for masculine plural imperative:",
      "جمع مذکر مخاطب کے امر میں واو الجماعة لگائی جاتی ہے", "Plural imperative ends in -oo",
      "fill_blank", "يَا أَبْنَائِي [ ＿＿＿ ] إِلَى الْمَسْجِدِ ! ", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "اذْهَبُوا", ["اذْهَبُوا", "اذْهَبْ", "اذْهَبْنَ", "تَذْهَبُونَ"], "🕌",
      "جمع مذکر کے لیے: اذْهَبُوا", "Plural imperative: idhhaboo.")

    # UNIT 17
    q(17, 1, "التَّمْرِينُ (1)", "مشق (1): نہی برائے ممانعت مفرد (لَا تَفْعَلْ)", "Exercise (1): Singular Prohibition (Laa Taf'al)",
      "انْهَ بِاسْتِعْمَالِ (لَا النَّاهِيَةِ):", "مضارع کو مجزوم (ساکن) کر کے ممانعت بنائیں:", "Form prohibition with Laa an-Naahiyah and sukoon:",
      "لا الناہیہ مضارع کو جزم (ساکن) دیتی ہے", "Laa an-naahiyah places the verb in jussive (sukoon)",
      "fill_blank", "يَا وَلَدُ [ ＿＿＿ ] فِي الشَّارِعِ ! ", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لَا تَلْعَبْ", ["لَا تَلْعَبْ", "لَا تَلْعَبُ", "لَا تَلْعَبِ", "مَا لَعِبْتَ"], "🚸",
      "نہی کے ساتھ جزم: لَا تَلْعَبْ", "Prohibitive with sukoon: laa tal'ab.")
    q(17, 2, "التَّمْرِينُ (2)", "مشق (2): نہی برائے جمع (حذفِ نون)", "Exercise (2): Plural Prohibition (Dropping Noon)",
      "انْهَ جَمْعَ الذُّكُورِ بِـ (لَا النَّاهِيَةِ):", "جمع میں نون گرانے کا اصول:", "Form plural prohibition by dropping final noon:",
      "لا الناہیہ داخل ہونے پر افعال خمسہ کی نون گر جاتی ہے", "Laa an-naahiyah drops the final noon in plural verbs",
      "fill_blank", "يَا إِخْوَانُ [ ＿＿＿ ] مِنَ الْفَصْلِ الآنَ ! ", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لَا تَخْرُجُوا", ["لَا تَخْرُجُوا", "لَا تَخْرُجُونَ", "لَا تَخْرُجْ", "مَا خَرَجْتُمْ"], "🚪",
      "جمع مذکر میں نون گر جائے گی: لَا تَخْرُجُوا", "Jussive drops the noon: laa takhrujoo.")

    # UNIT 18
    q(18, 1, "التَّمْرِينُ (1)", "مشق (1): (أَنْ) ناصبہ کا عمل", "Exercise (1): The Subjunctive Particle 'An'",
      "أَدْخِلْ (أَنْ) وَاضْبِطِ الْفِعْلَ الْمُضَارِعَ:", "(أَنْ) کے بعد مضارع پر زبر (فتحة) لگائیں:", "Apply fathah to the present verb after 'An':",
      "أنْ مصدریہ مضارع کو نصب (زبر) دیتی ہے", "The particle 'an' puts the present verb in subjunctive (fathah)",
      "fill_blank", "أُرِيدُ أَنْ [ ＿＿＿ ] إِلَى السُّوقِ .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "أَذْهَبَ", ["أَذْهَبَ", "أَذْهَبُ", "أَذْهَبِ", "أَذْهَبْ"], "🛒",
      "أنْ کے بعد زبر: أَنْ أَذْهَبَ", "Takes fathah after 'an': an adhhaba.")
    q(18, 2, "التَّمْرِينُ (2)", "مشق (2): (أَنْ) کے ساتھ مصدری معنی", "Exercise (2): Masdariyyah Meaning with 'An'",
      "عَيِّنِ الْفِعْلَ الْمَنْصُوبَ بَعْدَ (أَنْ):", "(أَنْ) کے بعد فعل مضارع کا اعراب:", "Subjunctive inflection of present verb after 'an':",
      "أنْ کے بعد مضارع ہمیشہ منصوب ہوتا ہے", "Verbs following 'an' must be mansoob",
      "fill_blank", "يَجِبُ عَلَيْكَ أَنْ [ ＿＿＿ ] الْوَاجِبَ .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "تَكْتُبَ", ["تَكْتُبَ", "تَكْتُبُ", "تَكْتُبِ", "تَكْتُبْ"], "📝",
      "أنْ کے بعد منصوب: أَنْ تَكْتُبَ", "Subjunctive: an taktuba.")

    # UNIT 19
    q(19, 1, "التَّمْرِينُ (1)", "مشق (1): (لَنْ) ناصبہ برائے نفی مستقبل", "Exercise (1): Negating Future with 'Lan'",
      "انْفِ الْمُسْتَقْبَلَ بِـ (لَنْ):", "(لَنْ) کے بعد مضارع پر نصب لگائیں:", "Negate future with 'Lan' (takes fathah):",
      "لن مستقبل کی تاکیدی نفی کرتی ہے اور مضارع کو فتحة دیتی ہے", "'Lan' emphatically negates future and gives fathah",
      "fill_blank", "[ ＿＿＿ ] الْكَسْلَانُ فِي الِامْتِحَانِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لَنْ يَنْجَحَ", ["لَنْ يَنْجَحَ", "لَنْ يَنْجَحُ", "لَا يَنْجَحُ", "مَا يَنْجَحْ"], "📝",
      "لن کے بعد زبر: لَنْ يَنْجَحَ (ہرگز کامیاب نہیں ہوگا)", "Accusative after lan: lan yanjaha.")
    q(19, 2, "التَّمْرِينُ (2)", "مشق (2): (لَنْ) کے ساتھ حذفِ نون", "Exercise (2): Dropping Noon after 'Lan'",
      "أَدْخِلْ (لَنْ) عَلَى جَمْعِ الْمُذَكَّرِ:", "لن کے داخل ہونے پر جمع کے مضارع سے نون گرائیں:", "Drop noon in masculine plural after 'Lan':",
      "افعال خمسہ پر لن داخل ہو تو نون حذف ہو جاتی ہے", "Verbs of the five forms drop noon after lan",
      "fill_blank", "الْكُسَالَى [ ＿＿＿ ] الْيَوْمَ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "لَنْ يَحْضُرُوا", ["لَنْ يَحْضُرُوا", "لَنْ يَحْضُرُونَ", "لَا يَحْضُرُونَ", "مَا حَضَرُوا"], "😴",
      "لن کے ساتھ نون گر گئی: لَنْ يَحْضُرُوا", "Drops noon: lan yahduroo.")

    # UNIT 20
    q(20, 1, "التَّمْرِينُ (1)", "مشق (1): لامِ تعلیل (لِـ)", "Exercise (1): Laam of Purpose (Laam at-Ta'leel)",
      "بَيِّنِ السَّبَبَ بِـ (لَامِ التَّعْلِيلِ):", "لام تعلیل کے بعد مضارع پر زبر لگائیں:", "Express purpose with Laam at-Ta'leel (takes fathah):",
      "لام تعلیل کے بعد فعل مضارع منصوب ہوتا ہے", "The verb after Laam at-Ta'leel is in subjunctive",
      "fill_blank", "دَخَلْتُ الْمَسْجِدَ [ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لِأُصَلِّيَ", ["لِأُصَلِّيَ", "لِأُصَلِّي", "لِأُصَلِّيُ", "أُصَلِّي"], "🕌",
      "لام تعلیل کے بعد فتحة: لِأُصَلِّيَ (تاکہ میں نماز پڑھوں)", "Subjunctive with fathah: li-usalliya.")
    q(20, 2, "التَّمْرِينُ (2)", "مشق (2): سوال بـ (لِمَاذَا) اور جواب بـ (لِـ)", "Exercise (2): Answering 'Why' with Laam at-Ta'leel",
      "أَجِبْ عَنْ (لِمَاذَا) بِاسْتِعْمَالِ لَامِ التَّعْلِيلِ:", "وجہ بتانے کے لیے لام تعلیل لگائیں:", "Answer 'Limaadhaa' using Laam at-Ta'leel:",
      "لماذا کے جواب میں لام تعلیل کے ساتھ فعل منصوب لاتے ہیں", "Answering 'why' with purpose clause",
      "fill_blank", "لِمَاذَا خَرَجْتَ مِنَ الْفَصْلِ؟ ➔ خَرَجْتُ [ ＿＿＿ ] الْمَاءَ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لِأَشْرَبَ", ["لِأَشْرَبَ", "لِأَشْرَبُ", "أَشْرَبُ", "لِشُرْبِ"], "💧",
      "لام تعلیل کے بعد زبر: لِأَشْرَبَ", "Subjunctive with fathah: li-ashraba.")

    # UNIT 21
    q(21, 1, "التَّمْرِينُ (1)", "مشق (1): (لَمْ) جازمہ اور نفی ماضی", "Exercise (1): The Jussive Particle 'Lam'",
      "انْفِ الْمَاضِيَ بِـ (لَمْ) مَعَ الْمُضَارِعِ:", "(لَمْ) کے بعد مضارع کو ساکن کریں:", "Negate past meaning using 'Lam' with jussive verb:",
      "لمْ مضارع کو جزم (ساکن) دیتی ہے اور معنی ماضی کا کر دیتی ہے", "'Lam' gives sukoon and flips meaning to past negative",
      "fill_blank", "[ ＿＿＿ ] حَامِدٌ الدَّرْسَ أَمْسِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "لَمْ يَكْتُبْ", ["لَمْ يَكْتُبْ", "لَمْ يَكْتُبُ", "لَمْ يَكْتُبَ", "لَا يَكْتُبُ"], "✍️",
      "لم کے بعد جزم: لَمْ يَكْتُبْ (اس نے نہیں لکھا)", "Jussive with sukoon: lam yaktub.")
    q(21, 2, "التَّمْرِينُ (2)", "مشق (2): (لَمْ) کے ساتھ حذفِ نون", "Exercise (2): Dropping Noon after 'Lam'",
      "أَدْخِلْ (لَمْ) عَلَى جَمْعِ الْمُذَكَّرِ:", "لم داخل ہونے پر نون گرائیں:", "Drop noon in masculine plural after 'Lam':",
      "افعال خمسہ پر لم داخل ہو تو علامت جزم حذفِ نون ہے", "Jussive marker for five verbs is dropping noon",
      "fill_blank", "الطُّلَّابُ [ ＿＿＿ ] إِلَى الْمَلْعَبِ أَمْسِ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "لَمْ يَذْهَبُوا", ["لَمْ يَذْهَبُوا", "لَمْ يَذْهَبُونَ", "لَا يَذْهَبُونَ", "مَا ذَهَبَ"], "⚽",
      "لم کے بعد نون گر گئی: لَمْ يَذْهَبُوا", "Drops noon after lam: lam yadhhaboo.")

    # UNIT 22
    q(22, 1, "التَّمْرِينُ (1)", "مشق (1): افعال خمسہ کی رفع (ثبوتِ نون)", "Exercise (1): The Five Verbs Nominative (Thuboot an-Noon)",
      "اضْبِطِ الأَفْعَالَ الْخَمْسَةَ فِي حَالَةِ الرَّفْعِ:", "حالتِ رفع میں نون برقرار رکھیں:", "In nominative, the Five Verbs retain final noon:",
      "افعال خمسہ کی علامتِ رفع ثبوتِ نون ہے", "The nominative marker of the Five Verbs is retention of noon",
      "fill_blank", "أَنْتُمْ [ ＿＿＿ ] الْقُرْآنَ بِخُشُوعٍ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "تَقْرَؤُونَ", ["تَقْرَؤُونَ", "تَقْرَؤُوا", "تَقْرَأْ", "قَرَأْتُمْ"], "📖",
      "حالتِ رفع میں نون موجود رہے گی: تَقْرَؤُونَ", "Retains noon in nominative: taqra'oona.")
    q(22, 2, "التَّمْرِينُ (2)", "مشق (2): افعال خمسہ کی نصب و جزم (حذفِ نون)", "Exercise (2): Subjunctive/Jussive of Five Verbs",
      "اضْبِطِ الأَفْعَالَ الْخَمْسَةَ فِي حَالَتَيِ النَّصْبِ وَالْجَزْمِ:", "نواصب و جوازم کے بعد نون گرائیں:", "Subjunctive/Jussive markers are dropping final noon:",
      "افعال خمسہ کی علامتِ نصب و جزم حذفِ نون ہے", "The subjunctive/jussive marker is dropping final noon",
      "fill_blank", "أَرَادَ الطُّلَّابُ أَنْ [ ＿＿＿ ] إِلَى الْمَلْعَبِ .", "صحیح فعل منتخب کریں:", "Select the correct form:",
      "يَذْهَبُوا", ["يَذْهَبُوا", "يَذْهَبُونَ", "يَذْهَبْ", "ذَهَبُوا"], "⚽",
      "أنْ کی وجہ سے نون گر گیا: أَنْ يَذْهَبُوا", "Dropping noon after 'an': an yadhhaboo.")

    # UNIT 23
    q(23, 1, "التَّمْرِينُ (1)", "مشق (1): تمیز الأعداد 3-10 (جمع مجرور)", "Exercise (1): Numbers 3-10 Rules (Plural Genitive)",
      "اخْتَرِ التَّمْيِيزَ الصَّحِيحَ لِلْعَدَدِ:", "3 سے 10 تک کے لیے جمع مجرور معدود لگائیں:", "Select the correct counted noun (plural genitive):",
      "3 سے 10 تک معدود جمع مجرور ہوتا ہے اور عدد جنس میں الٹ ہوتا ہے", "Numbers 3-10 take a plural genitive counted noun",
      "fill_blank", "عِنْدِي ثَلَاثَةُ [ ＿＿＿ ] .", "صحیح معدود منتخب کریں:", "Select the correct counted noun:",
      "أَقْلَامٍ", ["أَقْلَامٍ", "قَلَمٍ", "أَقْلَامًا", "قَلَمًا"], "🖊️",
      "3 کے بعد جمع مجرور: ثَلَاثَةُ أَقْلَامٍ", "Plural genitive: thalaathatu aqlaamin.")
    q(23, 2, "التَّمْرِينُ (2)", "مشق (2): تمیز الأعداد 11-19 (مفرد منصوب)", "Exercise (2): Numbers 11-19 Rules (Singular Accusative)",
      "اخْتَرِ التَّمْيِيزَ لِلأَعْدَادِ الْمُرَكَّبَةِ:", "11 سے 19 تک کے لیے مفرد منصوب معدود لگائیں:", "Select the counted noun for compound numbers (singular accusative):",
      "11 سے 19 تک معدود ہمیشہ مفرد منصوب ہوتا ہے", "Numbers 11-19 take a singular accusative counted noun",
      "fill_blank", "فِي الْفَصْلِ خَمْسَةَ عَشَرَ [ ＿＿＿ ] .", "صحیح معدود منتخب کریں:", "Select the correct counted noun:",
      "طَالِبًا", ["طَالِبًا", "طَالِبٍ", "طُلَّابٍ", "طَالِبٌ"], "👨‍🎓",
      "15 کے بعد مفرد منصوب: طَالِبًا", "Singular accusative: taaliban.")

    # UNIT 24
    q(24, 1, "التَّمْرِينُ (1)", "مشق (1): ممنوع من الصرف کا اعراب (حالتِ جر میں زبر)", "Exercise (1): Diptotes Genitive Case (Fathah)",
      "اضْبِطِ الاسْمَ الْمَمْنُوعَ مِنَ الصَّرْفِ:", "حالتِ جر میں فتحہ (زبر) کا اصول:", "Case ending of diptotes (fathah in genitive):",
      "ممنوع من الصرف پر تنوین نہیں آتی اور حالت جر میں فتحہ آتا ہے", "Diptotes do not take tanween and take fathah in genitive",
      "fill_blank", "ذَهَبْتُ إِلَى [ ＿＿＿ ] .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "مَكَّةَ", ["مَكَّةَ", "مَكَّةِ", "مَكَّةٍ", "مَكَّةُ"], "🕋",
      "ممنوع من الصرف پر زیر کی جگہ زبر: إِلَى مَكَّةَ", "Fathah in genitive: ilaa Makkata.")
    q(24, 2, "التَّمْرِينُ (2)", "مشق (2): صیغہ منتہی الجموع (مَفَاعِل، مَفَاعِيل)", "Exercise (2): Ultimate Plural Patterns (Masaajid, Manaadeel)",
      "عَيِّنِ الاسْمَ الْمَمْنُوعَ مِنَ الصَّرْفِ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ:", "منتہی الجموع پر تنوین نہ آنے کا اصول:", "Ultimate plural patterns take single vowel and no tanween:",
      "مساجد، مفاتیح جیسے اوزان غیر منصرف ہوتے ہیں", "Patterns Masaajid and Mafaateeh are diptotes",
      "fill_blank", "صَلَّيْتُ فِي [ ＿＿＿ ] كَثِيرَةٍ .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "مَسَاجِدَ", ["مَسَاجِدَ", "مَسَاجِدِ", "مَسَاجِدٍ", "مَسَاجِدٌ"], "🕌",
      "منتہی الجموع پر زیر کی جگہ زبر: مَسَاجِدَ", "Takes fathah without tanween: masaajida.")

    # UNIT 25
    q(25, 1, "التَّمْرِينُ (1)", "مشق (1): فہمِ متن", "Exercise (1): Reading Comprehension",
      "أجب عن الأسئلة الآتية:", "سبق کے مطابق جواب دیں:", "Answer based on the dialogue:",
      "فہمِ عبارت اور عربی جواب", "Comprehension of dialogue",
      "dialogue_qa", "أَيْنَ كَانَ أَنْوَرُ وَاقِفًا؟", "صحیح جواب منتخب کریں:", "Select the correct answer:",
      "كَانَ وَاقِفًا أَمَامَ الْمَحَطَّةِ", ["كَانَ وَاقِفًا أَمَامَ الْمَحَطَّةِ", "كَانَ فِي الْفَصْلِ", "كَانَ فِي الْمَسْجِدِ", "كَانَ فِي السُّوقِ"], "🚉",
      "انور اسٹیشن کے سامنے کھڑا تھا", "Anwar was standing in front of the station.")
    q(25, 2, "التَّمْرِينُ (2)", "مشق (2): (كَانَ) کا عمل", "Exercise (2): Action of 'Kaana' on Predicate",
      "أَدْخِلْ (كَانَ) عَلَى الْجُمَلِ الآتِيَةِ:", "(كَانَ) کے بعد خبر کو منصوب (زبر) کریں:", "Make the predicate accusative (mansoob) after Kaana:",
      "کان کا اسم مرفوع اور خبر منصوب ہوتی ہے", "Ism of Kaana is marfoo' and Khabar is mansoob",
      "fill_blank", "حَامِدٌ مَرِيضٌ الآنَ ➔ كَانَ حَامِدٌ [ ＿＿＿ ] أَمْسِ .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "مَرِيضًا", ["مَرِيضًا", "مَرِيضٌ", "مَرِيضٍ", "مَرِيضْ"], "🤒",
      "کان کی خبر منصوب ہوتی ہے: مَرِيضًا", "Khabar of Kaana is mansoob: mareedan.")
    q(25, 3, "التَّمْرِينُ (3)", "مشق (3): (لَا يَزَالُ) کا عمل", "Exercise (3): Action of 'Laa Yazaalu'",
      "أَدْخِلْ (لَا يَزَالُ) عَلَى الْجُمَلِ الآتِيَةِ:", "(لَا يَزَالُ) کا عمل کان کی طرح خبر کو منصوب کرنا ہے:", "'Laa yazaalu' acts like Kaana (raises noun, puts predicate in accusative):",
      "لا یزال استمرار کے لیے آتا ہے اور اس کی خبر منصوب ہوتی ہے", "'Laa yazaalu' indicates continuity and governs an accusative predicate",
      "fill_blank", "إِبْرَاهِيمُ نَائِمٌ ➔ لَا يَزَالُ إِبْرَاهِيمُ [ ＿＿＿ ] .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "نَائِمًا", ["نَائِمًا", "نَائِمٌ", "نَائِمٍ", "نَائِمْ"], "😴",
      "لا یزال کی خبر منصوب: نَائِمًا", "Predicate takes fathah: naa'iman.")
    q(25, 4, "التَّمْرِينُ (4)", "مشق (4): اسمائے خمسہ (أَبُونَا، أَبَانَا، أَبِينَا)", "Exercise (4): Asmaa al-Khamsah (Aboo, Abaa, Abee)",
      "امْلَأِ الْفَرَاغَ بِـ (أَب) مُعْرَبًا بِالْحُرُوفِ:", "حالتِ رفع (واو)، نصب (الف)، جر (یاء) کا اصول:", "Inflecting Asmaa' al-Khamsah (Waw in Nom., Alif in Acc., Yaa in Gen.):",
      "اسمائے خمسہ کا اعراب حروف سے ہوتا ہے", "Asmaa' al-Khamsah are inflected with letters (Waw, Alif, Yaa)",
      "fill_blank", "[ ＿＿＿ ] تَاجِرٌ كَبِيرٌ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "أَبُونَا", ["أَبُونَا", "أَبَانَا", "أَبِينَا", "أَبُنَا"], "🧔",
      "مبتدا مرفوع بالواو: أَبُونَا", "Nominative with Waw: Aboonaa.")

    # UNIT 26
    q(26, 1, "التَّمْرِينُ (1)", "مشق (1): مثال واوی کا مضارع (واؤ کا حذف)", "Exercise (1): Present of Assimilated Verbs (Dropping Waw)",
      "هَاتِ مُضَارِعَ الأَفْعَالِ الْمُعْتَلَّةِ الْفَاءِ:", "مضارع میں واؤ گرانے کا اصول:", "Drop root Waw in present tense (waqafa -> yaqifu):",
      "مثال واوی کے مضارع میں فائے کلمہ (واؤ) حذف ہو جاتی ہے", "Root Waw is elided in Mudari' when middle vowel is kasrah",
      "fill_blank", "وَقَفَ السَّائِقُ ➔ هُوَ [ ＿＿＿ ] أَمَامَ الْمَحَطَّةِ .", "صحیح مضارع منتخب کریں:", "Select the correct present verb:",
      "يَقِفُ", ["يَقِفُ", "يَوْقِفُ", "يَقُفُ", "وَقَفَ"], "🚏",
      "وقف کا مضارع واؤ گرا کر: يَقِفُ", "Waqafa becomes yaqifu (dropping waw).")
    q(26, 2, "التَّمْرِينُ (2)", "مشق (2): مثال واوی کا فعلِ امر", "Exercise (2): Imperative of Assimilated Verbs",
      "صُغِ الأَمْرَ مِنَ الأَفْعَالِ الآتِيَةِ:", "ہمزہ وصل کے بغیر امر بنانے کا اصول:", "Forming imperative without hamzat al-wasl (qif, zin, da'):",
      "مثال واوی کے امر میں ہمزہ وصل کی ضرورت نہیں ہوتی کیونکہ پہلا حرف متحرک ہے", "No hamzat al-wasl is needed because first letter has a harakah",
      "fill_blank", "تَقِفُ فِي الطَّرِيقِ ➔ يَا سَائِقُ [ ＿＿＿ ] هُنَا ! ", "صحیح امر منتخب کریں:", "Select the correct imperative:",
      "قِفْ", ["قِفْ", "اقِفْ", "تَقِفُ", "وَقَفَ"], "✋",
      "تَقِفُ سے امر: قِفْ (بغیر ہمزہ)", "Imperative of yaqifu is qif.")
    q(26, 3, "التَّمْرِينُ (3)", "مشق (3): اسمِ مصغر (فُعَيْل)", "Exercise (3): Diminutive Pattern (Fu'ayl)",
      "صَغِّرِ الأَسْمَاءَ الآتِيَةَ عَلَى وَزْنِ (فُعَيْل):", "اسم کو تصغیر کے وزن پر لائیں:", "Form the diminutive on the pattern Fu'ayl (walad -> wulayyid):",
      "ثلاثی اسم کی تصغیر کا وزن 'فُعَيْل' ہے", "Trilateral diminutive pattern is Fu'ayl",
      "fill_blank", "مَا تَصْغِيرُ كَلِمَةِ (وَلَدٌ)؟", "صحیح مصغر منتخب کریں:", "Select the correct diminutive:",
      "وُلَيْدٌ", ["وُلَيْدٌ", "وَلِيدٌ", "أَوْلَادٌ", "وَلَدٌ"], "👦",
      "ولد کا مصغر: وُلَيْدٌ (چھوٹا لڑکا)", "Diminutive of walad is wulayyid.")
    q(26, 4, "التَّمْرِينُ (4)", "مشق (4): اسم التفضیل مضعف سے", "Exercise (4): Superlative of Doubled Verbs (Aqallu, Ahabbu)",
      "صُغِ اسْمَ التَّفْضِيلِ مِنَ الْفِعْلِ الْمُضَعَّفِ:", "مضعف حروف میں ادغام کے ساتھ اسم تفضیل:", "Form comparative of geminate roots with idghaam:",
      "مضعف میں اسم تفضیل کا وزن 'أَفَلُّ' (ادغام کے ساتھ) بنتا ہے", "Geminate roots assimilate in comparative (aqallu, ahabbu)",
      "fill_blank", "مَا اسْمُ التَّفْضِيلِ مِنْ (قَلِيلٌ)؟", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "أَقَلُّ", ["أَقَلُّ", "أَقْلَلُ", "قَلِيلٌ", "مَقْلُولٌ"], "📉",
      "قلیل سے اسم تفضیل: أَقَلُّ", "Comparative of qaleel is aqallu.")
    q(26, 5, "التَّمْرِينُ (5)", "مشق (5): (يَجِبُ عَلَى) کا استعمال", "Exercise (5): Using 'Yajibu 'alaa' (Must/Ought to)",
      "اسْتَعْمِلْ (يَجِبُ عَلَى) مَعَ الْمَصْدَرِ الْمُؤَوَّلِ:", "(يَجِبُ عَلَى) کے بعد 'أَنْ' اور منصوب فعل لگائیں:", "Use 'Yajibu 'alaa' followed by 'an' and subjunctive verb:",
      "يجب على کے بعد أنْ اور فعل مضارع منصوب آتا ہے", "'Yajibu 'alaa' is followed by 'an' and a subjunctive verb",
      "fill_blank", "يَجِبُ عَلَيْنَا أَنْ [ ＿＿＿ ] الْقُرْآنَ الْكَرِيمَ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "نَفْهَمَ", ["نَفْهَمَ", "نَفْهَمُ", "نَفْهَمِ", "نَفْهَمْ"], "📖",
      "أنْ کی وجہ سے فتحة: أَنْ نَفْهَمَ", "Subjunctive with fathah: an naf-hama.")

    # UNIT 27
    q(27, 1, "التَّمْرِينُ (1)", "مشق (1): اجوف کا مضارع (واوی اور یائی)", "Exercise (1): Hollow Verbs Present Tense",
      "هَاتِ مُضَارِعَ الأَفْعَالِ الْجَوْفَاءِ الآتِيَةِ:", "اجوف کے مضارع میں حرفِ علت کی تبدیلی:", "Present tense of hollow verbs (qaala -> yaqoolu, baa'a -> yabee'u):",
      "اجوف واوی میں الف واؤ سے اور یائی میں یاء سے بدلتا ہے", "Hollow verbs convert root to Waw or Yaa in present tense",
      "fill_blank", "قَالَ الْمُدَرِّسُ ➔ هُوَ [ ＿＿＿ ] الْحَقَّ .", "صحیح مضارع منتخب کریں:", "Select the correct present verb:",
      "يَقُولُ", ["يَقُولُ", "يَقْوُلُ", "يَقَالُ", "قَائِلٌ"], "🗣️",
      "قال کا مضارع: يَقُولُ", "Qaala becomes yaqoolu.")
    q(27, 2, "التَّمْرِينُ (2)", "مشق (2): اجوف کا فعلِ امر", "Exercise (2): Imperative of Hollow Verbs",
      "صُغِ الأَمْرَ مِنَ الأَفْعَالِ الْجَوْفَاءِ:", "اجتماعِ ساکنین کے سبب حرفِ علت گرانے کا اصول:", "Hollow verb imperative drops root vowel due to sukoon (qul, bi', nam):",
      "امر میں آخری حرف ساکن ہونے سے حرفِ علت حذف ہو جاتا ہے", "The root vowel is dropped before sukoon: qul, bi'",
      "fill_blank", "تَقُولُ الْحَقَّ ➔ يَا أَخِي [ ＿＿＿ ] الْحَقَّ ! ", "صحیح امر منتخب کریں:", "Select the correct imperative:",
      "قُلْ", ["قُلْ", "قُولْ", "اقُولْ", "تَقُولْ"], "🗣️",
      "تقول سے امر: قُلْ (واؤ گر گئی)", "Imperative of yaqoolu is qul.")

    # UNIT 28
    q(28, 1, "التَّمْرِينُ (1)", "مشق (1): فعل ناقص کا مضارع", "Exercise (1): Present of Defective Verbs",
      "هَاتِ مُضَارِعَ الأَفْعَالِ النَّاقِصَةِ الآتِيَةِ:", "ناقص واوی اور یائی کا مضارع:", "Present of defective verbs (da'aa -> yad'oo, mashaa -> yamshee):",
      "لام کلمہ حرفِ علت ہو تو مضارع میں واؤ یا یاء بنتا ہے", "Defective verbs end in Waw or Yaa in Mudari'",
      "fill_blank", "دَعَا الْمُؤَذِّنُ ➔ هُوَ [ ＿＿＿ ] النَّاسَ إِلَى الصَّلَاةِ .", "صحیح مضارع منتخب کریں:", "Select the correct present verb:",
      "يَدْعُو", ["يَدْعُو", "يَدْعِي", "يَدْعَى", "دَاعٍ"], "🕌",
      "دعا کا مضارع: يَدْعُو", "Da'aa becomes yad'oo.")
    q(28, 2, "التَّمْرِينُ (2)", "مشق (2): فعل ناقص کا امر (حذفِ حرفِ علت)", "Exercise (2): Imperative of Defective Verbs",
      "صُغِ الأَمْرَ مِنَ الأَفْعَالِ النَّاقِصَةِ:", "امر میں حرفِ علت گرانے کا اصول:", "Defective verb imperative drops final weak letter (ud'u, imshi):",
      "ناقص کا فعل امر حرف علت کے حذف پر مبنی ہوتا ہے", "Imperative of defective verbs drops the final vowel letter",
      "fill_blank", "تَدْعُو اللَّهَ ➔ يَا أَخِي [ ＿＿＿ ] اللَّهَ ! ", "صحیح امر منتخب کریں:", "Select the correct imperative:",
      "ادْعُ", ["ادْعُ", "ادْعُو", "تَدْعُ", "دَعَا"], "🤲",
      "امر میں واؤ گر گئی: ادْعُ (پیش کے ساتھ)", "Imperative drops waw: ud'u.")

    # UNIT 29
    q(29, 1, "التَّمْرِينُ (1)", "مشق (1): لفیف مفروق (وقى يقي قِ)", "Exercise (1): Doubly Weak Separated Verbs (Lafeef Mafrooq)",
      "صُغِ الأَمْرَ مِنْ (وَقَى يَقِي):", "لفیف مفروق کا ایک حرفی امر:", "Single-letter imperative of Lafeef Mafrooq (Waqaa -> Yaqee -> Qi):",
      "لفیف مفروق کے امر میں فاء اور لام دونوں گر جاتے ہیں", "Both first and last weak root letters drop in imperative",
      "fill_blank", "يَقِي نَفْسَهُ ➔ يَا مُسْلِمُ [ ＿＿＿ ] نَفْسَكَ مِنَ النَّارِ ! ", "صحیح امر منتخب کریں:", "Select the correct imperative:",
      "قِ", ["قِ", "قِي", "اقِ", "وَقِ"], "🛡️",
      "وقى کا امر صرف ایک حرف ہے: قِ (بچاؤ)", "Imperative of waqaa is qi.")
    q(29, 2, "التَّمْرِينُ (2)", "مشق (2): لفیف مقرون (روى يروي اروِ)", "Exercise (2): Doubly Weak Adjacent Verbs (Lafeef Maqroon)",
      "صُغِ الأَمْرَ مِنْ (رَوَى يَرْوِي):", "لفیف مقرون کا فعل امر:", "Form imperative of Lafeef Maqroon (drop final weak letter):",
      "لفیف مقرون کے امر میں صرف آخری حرف علت گرتا ہے", "Only the final weak letter drops in Lafeef Maqroon",
      "fill_blank", "يَرْوِي الْحَدِيثَ ➔ يَا طَالِبُ [ ＿＿＿ ] الْحَدِيثَ بِسَنَدِهِ ! ", "صحیح امر منتخب کریں:", "Select the correct imperative:",
      "ارْوِ", ["ارْوِ", "ارْوِي", "رَوِ", "تَرْوِ"], "📜",
      "روى کا امر: ارْوِ (زیر کے ساتھ)", "Imperative of rawaa is irwi.")

    # UNIT 30
    q(30, 1, "التَّمْرِينُ (1)", "مشق (1): مضعف کا ادغام اور فکِ ادغام", "Exercise (1): Doubled Verbs (Mudha''af)",
      "صَرِّفِ الْفِعْلَ الْمُضَعَّفَ مَعَ الضَّمِيرِ:", "ضمیر متحرک کے ساتھ فکِ ادغام کا اصول:", "Unraveling assimilation with subject pronouns (marartu, zanan-tu):",
      "جب مضعف فعل متحرک ضمیر سے ملے تو ادغام کھل جاتا ہے", "Assimilation dissolves when attached to agent pronouns",
      "fill_blank", "أَنَا [ ＿＿＿ ] بِالْمَسْجِدِ أَمْسِ .", "صحیح فعل منتخب کریں:", "Select the correct verb:",
      "مَرَرْتُ", ["مَرَرْتُ", "مَرَّيْتُ", "مَرْتُ", "مَرَرْتَ"], "🕌",
      "متکلم کے ساتھ ادغام کھل گیا: مَرَرْتُ", "Assimilation dissolves: marartu.")
    q(30, 2, "التَّمْرِينُ (2)", "مشق (2): مضعف کا مضارع (يَمُرُّ، يَظُنُّ)", "Exercise (2): Present of Doubled Verbs",
      "هَاتِ مُضَارِعَ الأَفْعَالِ الْمُضَعَّفَةِ:", "مضارع میں تضعیف برقرار رکھنے کا اصول:", "Retaining gemination in present tense of doubled verbs:",
      "مضارع میں مضعف ادغام کے ساتھ رہتا ہے", "Gemination remains intact in mudari'",
      "fill_blank", "مَرَّ الرَّجُلُ ➔ هُوَ [ ＿＿＿ ] أَمَامَ الْبَيْتِ .", "صحیح مضارع منتخب کریں:", "Select the correct present verb:",
      "يَمُرُّ", ["يَمُرُّ", "يَمْرُرُ", "يَمُرَّ", "مَارٌّ"], "🚶",
      "مرّ کا مضارع ادغام کے ساتھ: يَمُرُّ", "Present of marra is yamurru.")

    # UNIT 31
    q(31, 1, "التَّمْرِينُ (1)", "مشق (1): معتل کی اقسام کی تمیز", "Exercise (1): Classifying Weak Verbs",
      "مَيِّزْ نَوْعَ الْفِعْلِ الْمُعْتَلِّ:", "معتل کے مقام کی بنیاد پر قسم بتائیں:", "Identify category of weak verb (Mithaal, Ajwaf, Naaqis):",
      "فاء پر علت = مثال، عین پر = اجوف، لام پر = ناقص", "1st weak = Mithaal, 2nd weak = Ajwaf, 3rd weak = Naaqis",
      "fill_blank", "مَا نَوْعُ الْفِعْلِ (وَجَدَ)؟", "صحیح قسم منتخب کریں:", "Select the correct category:",
      "مِثَالٌ (مُعْتَلُّ الْفَاءِ)", ["مِثَالٌ (مُعْتَلُّ الْفَاءِ)", "أَجْوَفُ (مُعْتَلُّ الْعَيْنِ)", "نَاقِصٌ (مُعْتَلُّ اللَّامِ)", "مُضَعَّفٌ"], "🔍",
      "وجد کے شروع میں واؤ ہے اس لیے: مثال", "Wajada has weak 1st root: Mithaal.")
    q(31, 2, "التَّمْرِينُ (2)", "مشق (2): اجوف اور ناقص کی تمیز", "Exercise (2): Distinguishing Ajwaf and Naaqis",
      "مَيِّزْ بَيْنَ الأَجْوَفِ وَالنَّاقِصِ:", "درمیان یا آخر میں حرفِ علت کی پہچان:", "Distinguish between middle-weak (Ajwaf) and final-weak (Naaqis):",
      "درمیان میں علت ہو تو اجوف اور آخر میں ہو تو ناقص", "Middle weak radical is Ajwaf; final weak radical is Naaqis",
      "fill_blank", "مَا نَوْعُ الْفِعْلِ (قَضَى)؟", "صحیح قسم منتخب کریں:", "Select the correct category:",
      "نَاقِصٌ (مُعْتَلُّ اللَّامِ)", ["نَاقِصٌ (مُعْتَلُّ اللَّامِ)", "أَجْوَفُ (مُعْتَلُّ الْعَيْنِ)", "مِثَالٌ (مُعْتَلُّ الْفَاءِ)", "مَهْمُوزٌ"], "⚖️",
      "قضى کے آخر میں حرف علت ہے اس لیے: ناقص", "Qadaa has final weak letter: Naaqis.")

    return questions

if __name__ == '__main__':
    qs = get_book2_questions()
    print(f"Generated {len(qs)} Book 2 questions across units.")
    unit_map = {}
    for q in qs:
        u = q['unit_num']
        t = q['tamreen_num']
        unit_map.setdefault(u, set()).add(t)
    print(f"Units covered: {len(unit_map)}")
    for u in sorted(unit_map.keys()):
        print(f"  Unit {u}: Tamreens {sorted(list(unit_map[u]))}")
