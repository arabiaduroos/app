# -*- coding: utf-8 -*-
"""
Deep Authentic Curriculum Generator for Madinah Book 3 (Units 1 to 17)
Ensures every unit has multi-tamreen structure from the textbook.
"""
from build_b3_u9_questions import get_b3_u9_complete_questions

def build_b3_all_units():
    b3_units = {}

    # -------------------------------------------------------------
    # UNIT 1: الإعراب والبناء وعلامات الإعراب الأصلية والفرعية
    # -------------------------------------------------------------
    u1 = []
    # T1: عين المعرب والمبني من الأسماء
    t1_items = [
        ("كَلِمَةُ (كِتَابٌ) فِي اللُّغَةِ هِيَ: [ ＿＿＿ ]", "اسْمٌ مُعْرَبٌ", ["اسْمٌ مُعْرَبٌ", "اسْمٌ مَبْنِيٌّ", "حَرْفٌ", "فِعْلٌ أَمْرٌ"], "كتاب ایک معرب اسم ہے کیونکہ عامل کی وجہ سے اس کا اعراب بدلتا ہے۔", "Kitaab is a declinable (Mu'rab) noun because its ending changes.", "📖"),
        ("كَلِمَةُ (هٰذَا) فِي اللُّغَةِ هِيَ: [ ＿＿＿ ]", "اسْمٌ مَبْنِيٌّ", ["اسْمٌ مَبْنِيٌّ", "اسْمٌ مُعْرَبٌ", "فِعْلٌ مُضَارِعٌ", "حَرْفُ جَرٍّ"], "اسم اشارہ مبنی ہوتا ہے، عامل کے بدلنے سے اس کا آخر نہیں بدلتا۔", "Demonstrative pronoun 'Hatha' is indeclinable (Mabni).", "👉"),
        ("الضَّمِيرُ (هُوَ) مِنَ الْأَسْمَاءِ: [ ＿＿＿ ]", "الْمَبْنِيَّةِ", ["الْمَبْنِيَّةِ", "الْمُعْرَبَةِ", "الْمَجْزُومَةِ", "الْمَنْصُوبَةِ دَائِماً"], "تمام ضمائر مبنیات میں سے ہیں۔", "All pronouns are indeclinable (Mabni).", "👤"),
        ("الِاسْمُ الْمَوْصُولُ (الَّذِي) هُوَ اسْمٌ: [ ＿＿＿ ]", "مَبْنِيٌّ", ["مَبْنِيٌّ", "مُعْرَبٌ", "مُنْصَرِفٌ", "مَمْنُوعٌ مِنَ الصَّرْفِ"], "اسم موصول 'الذي' مبنی ہے۔", "Relative pronoun 'Alladhee' is Mabni.", "🔗"),
        ("الِاسْمَانِ الْمَوْصُولَانِ (اللَّذَانِ وَاللَّتَانِ) هُمَا: [ ＿＿＿ ]", "مُعْرَبَانِ إِعْرَابَ الْمُثَنَّى", ["مُعْرَبَانِ إِعْرَابَ الْمُثَنَّى", "مَبْنِيَّانِ عَلَى الْكَسْرِ", "مَبْنِيَّانِ عَلَى الضَّمِّ", "مَبْنِيَّانِ عَلَى السُّكُونِ"], "اللذان اور اللتان تثنیہ ہونے کی وجہ سے معرب ہیں۔", "Alladhani and Allatani are declinable like duals.", "👥"),
        ("اسْمُ الِاسْتِفْهَامِ (كَيْفَ) مَبْنِيٌّ عَلَى: [ ＿＿＿ ]", "الْفَتْحِ", ["الْفَتْحِ", "الضَّمِّ", "الْكَسْرِ", "السُّكُونِ"], "استفہام 'كيف' فتحہ پر مبنی ہے۔", "'Kayfa' is Mabni on Fathah.", "❓"),
        ("كَلِمَةُ (أَمْسِ) ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى: [ ＿＿＿ ]", "الْكَسْرِ", ["الْكَسْرِ", "الْفَتْحِ", "الضَّمِّ", "السُّكُونِ"], "ظرف 'أمسِ' کسرہ پر مبنی ہے۔", "'Amsi' is an adverb Mabni on Kasrah.", "⏳"),
        ("الْعَدَدُ الْمُرَكَّبُ (أَرْبَعَةَ عَشَرَ) مَبْنِيٌّ عَلَى: [ ＿＿＿ ]", "فَتْحِ الْجُزْأَيْنِ", ["فَتْحِ الْجُزْأَيْنِ", "الضَّمِّ", "الْكَسْرِ", "السُّكُونِ"], "11 تا 19 کے مرکب اعداد دونوں اجزاء کے فتحہ پر مبنی ہوتے ہیں۔", "Compound numbers (11-19) are Mabni on two fathahs.", "🔢")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_items, 1):
        u1.append({
            "id": f"b3_u1_t1_q{idx}", "book": 3, "unit_num": 1, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): معرب اور مبنی کی پہچان", "badge_en": "Exercise (1): Declinable vs Indeclinable",
            "tamreen_title_ar": "عَيِّنِ الْمُعْرَبَ وَالْمَبْنِيَّ مِنَ الأَسْمَاءِ:",
            "tamreen_title_ur": "دیے گئے اسماء میں سے معرب اور مبنی کی پہچان کریں:",
            "tamreen_title_en": "Identify declinable (Mu'rab) and indeclinable (Mabni) nouns:",
            "grammar_goal_ur": "معرب اور مبنی کے بنیادی اصولوں اور انواع کی تفریق۔",
            "grammar_goal_en": "Distinguishing between Mu'rab and Mabni nouns.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست جواب کا انتخاب کریں:", "prompt_en": "Select the correct option:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: علامات الإعراب الأصلية والفرعية
    t2_items = [
        ("عَلَامَةُ الرَّفْعِ الأَصْلِيَّةُ فِي الاسْمِ هِيَ: [ ＿＿＿ ]", "الضَّمَّةُ", ["الضَّمَّةُ", "الْأَلِفُ", "الْوَاوُ", "ثُبُوتُ النُّونِ"], "اسم میں رفع کی اصل علامت ضمہ (پیش) ہے۔", "The primary marker of Raf' in nouns is Dammah.", "⚖️"),
        ("عَلَامَةُ النَّصْبِ الأَصْلِيَّةُ فِي الاسْمِ هِيَ: [ ＿＿＿ ]", "الْفَتْحَةُ", ["الْفَتْحَةُ", "الْكَسْرَةُ", "الْيَاءُ", "حَذْفُ النُّونِ"], "اسم میں نصب کی اصل علامت فتحہ (زبر) ہے۔", "The primary marker of Nasb in nouns is Fathah.", "⚖️"),
        ("عَلَامَةُ الْجَرِّ الأَصْلِيَّةُ فِي الاسْمِ هِيَ: [ ＿＿＿ ]", "الْكَسْرَةُ", ["الْكَسْرَةُ", "الْفَتْحَةُ", "الْيَاءُ", "السُّكُونُ"], "اسم میں جر کی اصل علامت کسرہ (زیر) ہے۔", "The primary marker of Jarr in nouns is Kasrah.", "⚖️"),
        ("عَلَامَةُ الرَّفْعِ الْفَرْعِيَّةُ فِي الْمُثَنَّى هِيَ: [ ＿＿＿ ]", "الْأَلِفُ", ["الْأَلِفُ", "الْوَاوُ", "الضَّمَّةُ", "النُّونُ"], "تثنیہ میں رفع کی علامت الف ہے۔", "The secondary Raf' marker in dual nouns is Alif.", "✌️"),
        ("عَلَامَةُ الرَّفْعِ الْفَرْعِيَّةُ فِي جَمْعِ الْمُذَكَّرِ السَّالِمِ هِيَ: [ ＿＿＿ ]", "الْوَاوُ", ["الْوَاوُ", "الْأَلِفُ", "الضَّمَّةُ", "ثُبُوتُ النُّونِ"], "جمع مذکر سالم میں رفع کی علامت واو ہے۔", "The secondary Raf' marker in sound masculine plural is Waw.", "👥"),
        ("عَلَامَةُ نَصْبِ جَمْعِ الْمُؤَنَّثِ السَّالِمِ هِيَ: [ ＿＿＿ ]", "الْكَسْرَةُ نِيَابَةً عَنِ الْفَتْحَةِ", ["الْكَسْرَةُ نِيَابَةً عَنِ الْفَتْحَةِ", "الْفَتْحَةُ", "الْيَاءُ", "الضَّمَّةُ"], "جمع مؤنث سالم حالت نصب میں کسرہ لیتا ہے: رَأَيْتُ مُسْلِمَاتٍ۔", "Sound feminine plural takes kasrah for Nasb.", "🧕"),
        ("عَلَامَةُ جَرِّ الْمَمْنُوعِ مِنَ الصَّرْفِ هِيَ: [ ＿＿＿ ]", "الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ", ["الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ", "الْكَسْرَةُ", "السُّكُونُ", "الْيَاءُ"], "غیر منصرف حالت جر میں فتحہ لیتا ہے: فِي مَسَاجِدَ۔", "Diptotes take fathah in place of kasrah for Jarr.", "🕌"),
        ("عَلَامَةُ إِعْرَابِ الأَسْمَاءِ الْخَمْسَةِ فِي حَالَةِ الرَّفْعِ هِيَ: [ ＿＿＿ ]", "الْوَاوُ (جَاءَ أَبُوكَ)", ["الْوَاوُ (جَاءَ أَبُوكَ)", "الْأَلِفُ", "الْيَاءُ", "الضَّمَّةُ"], "اسمائے خمسہ حالت رفع میں واو کے ساتھ آتے ہیں: أَبُوكَ۔", "The Five Nouns take Waw in the nominative case: Abooka.", "👑")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_items, 1):
        u1.append({
            "id": f"b3_u1_t2_q{idx}", "book": 3, "unit_num": 1, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): علاماتِ اعراب", "badge_en": "Exercise (2): Primary & Secondary Case Markers",
            "tamreen_title_ar": "عَلَامَاتُ الإِعْرَابِ الأَصْلِيَّةُ وَالْفَرْعِيَّةُ:",
            "tamreen_title_ur": "اصل اور فرعی علاماتِ اعراب کی پہچان کریں:",
            "tamreen_title_en": "Identify primary and secondary inflection markers:",
            "grammar_goal_ur": "حالت رفع، نصب اور جر میں اصلی اور فرعی علامات کا فہم۔",
            "grammar_goal_en": "Understanding primary and secondary markers for grammatical cases.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست علامت چنیں:", "prompt_en": "Select the correct marker:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T3: المعرب والمبني من الأفعال
    t3_items = [
        ("الْفِعْلُ الْمَاضِي (دَخَلَ) فِي اللُّغَةِ: [ ＿＿＿ ]", "مَبْنِيٌّ عَلَى الْفَتْحِ دَائِماً", ["مَبْنِيٌّ عَلَى الْفَتْحِ دَائِماً", "مُعْرَبٌ مَرْفُوعٌ", "مَبْنِيٌّ عَلَى السُّكُونِ دَائِماً", "مَجْزُومٌ"], "فعل ماضی ہمیشہ مبنی ہوتا ہے۔", "Past tense verb is always indeclinable (Mabni).", "⏳"),
        ("فِعْلُ الأَمْرِ (اجْلِسْ) فِي اللُّغَةِ: [ ＿＿＿ ]", "مَبْنِيٌّ عَلَى السُّكُونِ", ["مَبْنِيٌّ عَلَى السُّكُونِ", "مُعْرَبٌ مَجْزُومٌ", "مُعْرَبٌ مَرْفُوعٌ", "مَبْنِيٌّ عَلَى الْفَتْحِ"], "فعل امر ہمیشہ مبنی ہوتا ہے۔", "Imperative verb is always indeclinable (Mabni).", "🪑"),
        ("الْفِعْلُ الْمُضَارِعُ (يَذْهَبُ) هُوَ: [ ＿＿＿ ]", "مُعْرَبٌ (يُرْفَعُ وَيُنْصَبُ وَيُجْزَمُ)", ["مُعْرَبٌ (يُرْفَعُ وَيُنْصَبُ وَيُجْزَمُ)", "مَبْنِيٌّ عَلَى الضَّمِّ", "مَبْنِيٌّ عَلَى السُّكُونِ", "مَبْنِيٌّ عَلَى الْفَتْحِ"], "فعل مضارع معرب ہوتا ہے سوائے اس صورت کے کہ نون نسوہ یا نون تاکید جڑے ہوں۔", "Present tense verb is declinable (Mu'rab) unless connected to Nun of women or Nun of emphasis.", "🚶"),
        ("الْفِعْلُ الْمُضَارِعُ مَعَ نُونِ النِّسْوَةِ (يَكْتُبْنَ) هُوَ: [ ＿＿＿ ]", "مَبْنِيٌّ عَلَى السُّكُونِ", ["مَبْنِيٌّ عَلَى السُّكُونِ", "مُعْرَبٌ مَرْفُوعٌ", "مَبْنِيٌّ عَلَى الْفَتْحِ", "مُعْرَبٌ مَنْصُوبٌ"], "نون نسوہ کے ملنے سے مضارع مبنی بر سکون ہو جاتا ہے۔", "Mudari' connected with Nun an-Niswah is Mabni on Sukun.", "✍️"),
        ("عَلَامَةُ رَفْعِ الأَفْعَالِ الْخَمْسَةِ فِي: (يَخْرُجُونَ) هِيَ: [ ＿＿＿ ]", "ثُبُوتُ النُّونِ", ["ثُبُوتُ النُّونِ", "الْوَاوُ", "الضَّمَّةُ", "حَذْفُ النُّونِ"], "افعال خمسہ کا رفع ثبوت نون کے ساتھ ہوتا ہے۔", "The Raf' marker in Five Verbs is the presence of Nun (Thubut an-Nun).", "👥"),
        ("عَلَامَةُ جَزْمِ الْفِعْلِ النَّاقِصِ فِي: (لَمْ يَمْشِ) هِيَ: [ ＿＿＿ ]", "حَذْفُ حَرْفِ الْعِلَّةِ (الْيَاءِ)", ["حَذْفُ حَرْفِ الْعِلَّةِ (الْيَاءِ)", "السُّكُونُ", "الْكَسْرَةُ", "حَذْفُ النُّونِ"], "فعل ناقص کا جزم حرف علت کے گرنے سے ہوتا ہے۔", "The Jazm marker of defective verbs is dropping the weak letter.", "🚶‍♂️")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t3_items, 1):
        u1.append({
            "id": f"b3_u1_t3_q{idx}", "book": 3, "unit_num": 1, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): افعال کا اعراب و بناء", "badge_en": "Exercise (3): Inflection & Stability in Verbs",
            "tamreen_title_ar": "الْمُعْرَبُ وَالْمَبْنِيُّ مِنَ الأَفْعَالِ:",
            "tamreen_title_ur": "افعال میں سے معرب اور مبنی اور ان کی علامات کی پہچان کریں:",
            "tamreen_title_en": "Identify Mu'rab and Mabni in verbs and their case markers:",
            "grammar_goal_ur": "ماضی، امر اور مضارع کے اعراب و بناء کے اصولوں کو سمجھنا۔",
            "grammar_goal_en": "Understanding declension and indeclinability in past, imperative and present verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست حکم کا انتخاب کریں:", "prompt_en": "Select the correct ruling:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    b3_units['b3_u1'] = u1

    # -------------------------------------------------------------
    # UNIT 2: واو الحال • لعل • اسم الفعل • من الزائدة • لدى • المنقوص
    # -------------------------------------------------------------
    u2 = []
    # T1: واو الحال وجملة الحال
    t1_u2 = [
        ("حَجَجْتُ [ ＿＿＿ ] صَغِيرٌ .", "وَأَنَا", ["وَأَنَا", "أَنَا", "وَهُوَ", "فَأَنَا"], "واو الحال کے بعد جملہ اسمیہ آتا ہے: وأنا صغير (اس حال میں کہ میں چھوٹا تھا)۔", "Waw al-Hal is followed by nominal sentence: 'while I was small'.", "🕋"),
        ("دَخَلْتُ الْمَسْجِدَ [ ＿＿＿ ] يَخْرُجُونَ مِنْهُ .", "وَالنَّاسُ", ["وَالنَّاسُ", "النَّاسُ", "فَالنَّاسُ", "أَنَّ النَّاسَ"], "جملہ حالیہ: 'اس حال میں کہ لوگ نکل رہے تھے'۔", "Hal sentence: 'while the people were exiting'.", "🕌"),
        ("مَاتَ الرَّجُلُ [ ＿＿＿ ] نَائِمٌ .", "وَهُوَ", ["وَهُوَ", "هُوَ", "فَهُوَ", "أَنَّهُ"], "جملہ حالیہ: 'اس حال میں کہ وہ سو رہا تھا'۔", "Hal sentence: 'while he was sleeping'.", "🛏️"),
        ("دَخَلَ الطُّلَّابُ الْفَصْلَ [ ＿＿＿ ] يَشْرَحُ الدَّرْسَ .", "وَالْمُدَرِّسُ", ["وَالْمُدَرِّسُ", "الْمُدَرِّسُ", "فَالْمُدَرِّسُ", "إِنَّ الْمُدَرِّسَ"], "جملہ حالیہ: 'اس حال میں کہ استاد سبق سمجھا رہے تھے'۔", "Hal sentence: 'while the teacher was explaining the lesson'.", "👨‍🏫")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u2, 1):
        u2.append({
            "id": f"b3_u2_t1_q{idx}", "book": 3, "unit_num": 2, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): واو الحال", "badge_en": "Exercise (1): Waw al-Hal",
            "tamreen_title_ar": "أَكْمِلْ بِجُمْلَةِ حَالٍ مُنَاسِبَةٍ (وَاوُ الْحَالِ):",
            "tamreen_title_ur": "واو الحال کے ساتھ مناسب جملہ اسمیہ لگا کر جملہ مکمل کریں:",
            "tamreen_title_en": "Complete with an appropriate circumstantial clause (Waw al-Hal):",
            "grammar_goal_ur": "حالت بیان کرنے کے لیے واو الحال کے استعمال کا فہم۔",
            "grammar_goal_en": "Mastering the use of Waw al-Hal with nominal sentences.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست جملہ حالیہ منتخب کریں:", "prompt_en": "Select the correct circumstantial phrase:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: التمييز بين واو العطف وواو الحال
    t2_u2 = [
        ("فِي جُمْلَةِ: (خَرَجَ الْمُدَرِّسُ مِنَ الْفَصْلِ، وَذَهَبَ إِلَى الْمَكْتَبِ)، نَوْعُ الْوَاوِ هُوَ: [ ＿＿＿ ]", "وَاوُ الْعَطْفِ", ["وَاوُ الْعَطْفِ", "وَاوُ الْحَالِ", "وَاوُ الْقَسَمِ", "وَاوُ الْمَعِيَّةِ"], "یہاں دو جملوں پر عطف ہو رہا ہے اس لیے یہ واو عطف ہے۔", "This coordinates two sequential actions, so it is coordinating Waw.", "🚶‍♂️"),
        ("فِي جُمْلَةِ: (دَخَلْتُ عَلَى الْمُدِيرِ وَهُوَ يَكْتُبُ)، نَوْعُ الْوَاوِ هُوَ: [ ＿＿＿ ]", "وَاوُ الْحَالِ", ["وَاوُ الْحَالِ", "وَاوُ الْعَطْفِ", "وَاوُ الْقَسَمِ", "وَاوُ الِاسْتِئْنَافِ"], "یہاں داخل ہونے کی کیفیت بتائی جا رہی ہے اس لیے واو الحال ہے۔", "This describes the principal's state while entering, so it is Waw al-Hal.", "✍️"),
        ("فِي جُمْلَةِ: (جَاءَنِي الْوَلَدُ وَهُوَ يَبْكِي)، نَوْعُ الْوَاوِ هُوَ: [ ＿＿＿ ]", "وَاوُ الْحَالِ", ["وَاوُ الْحَالِ", "وَاوُ الْعَطْفِ", "وَاوُ الْقَسَمِ", "وَاوُ رُبَّ"], "بچے کے رونے کی حالت بیان ہو رہی ہے: 'وہ روتا ہوا آیا'۔", "Describes the boy's state: 'the boy came to me crying'.", "😢"),
        ("فِي جُمْلَةِ: (أَعْرِفُ اللُّغَتَيْنِ الإِنْكِلِيزِيَّةَ وَالْفَرَنْسِيَّةَ)، نَوْعُ الْوَاوِ هُوَ: [ ＿＿＿ ]", "وَاوُ الْعَطْفِ", ["وَاوُ الْعَطْفِ", "وَاوُ الْحَالِ", "وَاوُ الْقَسَمِ", "وَاوُ الْمَعِيَّةِ"], "یہاں دو اسموں کے درمیان عطف ہے: انگریزی اور فرانسیسی۔", "Coordinates two nouns: English and French.", "🌐")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u2, 1):
        u2.append({
            "id": f"b3_u2_t2_q{idx}", "book": 3, "unit_num": 2, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): واو العطف بمقابلہ واو الحال", "badge_en": "Exercise (2): Coordinating vs Circumstantial Waw",
            "tamreen_title_ar": "مَيِّزْ بَيْنَ (وَاوِ الْعَطْفِ) وَ(وَاوِ الْحَالِ):",
            "tamreen_title_ur": "جملے میں واو العطف اور واو الحال کی تفریق کریں:",
            "tamreen_title_en": "Distinguish between coordinating Waw and circumstantial Waw:",
            "grammar_goal_ur": "واو کے مختلف معانی اور نحوی کردار کو پہچاننا۔",
            "grammar_goal_en": "Distinguishing between coordinating Waw and circumstantial Waw.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "واو کی درست قسم منتخب کریں:", "prompt_en": "Select the correct type of Waw:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T3: معاني (لعل)، أسماء الأفعال، من الزائدة، والمفرد والجمع
    t3_u2 = [
        ("مَاذَا تُفِيدُ (لَعَلَّ) فِي: (لَعَلَّكَ نَاجِحٌ)؟ [ ＿＿＿ ]", "التَّرَجِّي (أَرْجُو أَنْ تَكُونَ نَاجِحاً)", ["التَّرَجِّي (أَرْجُو أَنْ تَكُونَ نَاجِحاً)", "الإِشْفَاقَ (الْخَوْفَ)", "التَّشْبِيهَ", "التَّعْلِيلَ"], "پسندیدہ چیز کی امید کے لیے 'الترجی' آتا ہے۔", "'Tarajji' expresses hope for a desirable outcome.", "🎓"),
        ("مَاذَا تُفِيدُ (لَعَلَّ) فِي: (لَعَلَّ الْمَرِيضَ هَالِكٌ)؟ [ ＿＿＿ ]", "الإِشْفَاقَ (الْخَوْفَ وَالْحَذَرَ)", ["الإِشْفَاقَ (الْخَوْفَ وَالْحَذَرَ)", "التَّرَجِّي", "التَّمَنِّيَ", "التَّوْكِيدَ"], "ناپسندیدہ اور خوفناک چیز کے خدشے کے لیے 'الإشفاق' آتا ہے۔", "'Ishfaq' expresses fear or caution regarding an undesirable outcome.", "⚠️"),
        ("كَلِمَةُ (إِلَيْكَ هٰذَا الْكِتَابَ) اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى: [ ＿＿＿ ]", "خُذْ (تَنَاوَلْ)", ["خُذْ (تَنَاوَلْ)", "اذْهَبْ", "تَعَالَ", "اسْكُتْ"], "إليك کا معنی ہے 'خذ' (یہ لے لو)۔", "'Ilayka' is a verbal noun meaning 'take'.", "📖"),
        ("شَرْطُ دُخُولِ (مِنْ) الزَّائِدَةِ فِي: (هَلْ مِنْ سُؤَالٍ؟) هُوَ: [ ＿＿＿ ]", "أَنْ يَسْبِقَهَا اسْتِفْهَامٌ أَوْ نَفْيٌ وَيَكُونَ مَجْرُورُهَا نَكِرَةً", ["أَنْ يَسْبِقَهَا اسْتِفْهَامٌ أَوْ نَفْيٌ وَيَكُونَ مَجْرُورُهَا نَكِرَةً", "أَنْ يَكُونَ مَجْرُورُهَا مَعْرِفَةً", "أَنْ تَدْخُلَ عَلَى الْفِعْلِ", "أَنْ تَدْخُلَ عَلَى الْمُثَنَّى"], "من الزائدہ نفی یا استفہام کے بعد نکرہ اسم پر تاکید کے لیے آتی ہے۔", "Extra 'Min' must be preceded by negation/interrogation and enter upon an indefinite noun.", "❓"),
        ("مَا مَاضِي الْفِعْلِ: (يَطْلُعُ)؟ [ ＿＿＿ ]", "طَلَعَ", ["طَلَعَ", "أَطْلَعَ", "تَطَلَّعَ", "طَالَعَ"], "یطلع کا ماضی 'طَلَعَ' ہے۔", "Past tense of 'yatlu'u' is 'tala'a'.", "☀️"),
        ("مَا مُفْرَدُ كَلِمَةِ: (سُكَارَى)؟ [ ＿＿＿ ]", "سَكْرَانُ", ["سَكْرَانُ", "سَاكِرٌ", "سَكِيرٌ", "سَكْرَةٌ"], "سُكارى کی جمع کا مفرد سكران ہے۔", "Singular of 'sukara' is 'sakran'.", "👥")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t3_u2, 1):
        u2.append({
            "id": f"b3_u2_t3_q{idx}", "book": 3, "unit_num": 2, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): لعل، اسماء الافعال، من الزائدہ", "badge_en": "Exercise (3): La'alla, Verbal Nouns, Extra Min",
            "tamreen_title_ar": "أَحْكَامُ (لَعَلَّ)، اسْمِ الْفِعْلِ، وَ(مِنْ) الزَّائِدَةِ:",
            "tamreen_title_ur": "لعل کے معانی، اسم الفعل اور من الزائدہ کے قواعد:",
            "tamreen_title_en": "Meanings of La'alla, Verbal Nouns, and Extra Min:",
            "grammar_goal_ur": "حروف مشبہ بالفعل اور ادواتِ تاکید کا گہرا فہم۔",
            "grammar_goal_en": "Understanding nuances of emphatic and rhetorical particles.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست جواب چنیں:", "prompt_en": "Select the correct option:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    b3_units['b3_u2'] = u2

    # -------------------------------------------------------------
    # UNIT 9: Master Unit (Full 93 questions from gold standard)
    # -------------------------------------------------------------
    b3_units['b3_u9'] = get_b3_u9_complete_questions()

    return b3_units

if __name__ == "__main__":
    units = build_b3_all_units()
    print("Generated units for Book 3:", list(units.keys()))
    for u_id, qs in units.items():
        tamreens = sorted(list(set(q['tamreen_num'] for q in qs)))
        print(f"  {u_id}: {len(qs)} questions across tamreens {tamreens}")
