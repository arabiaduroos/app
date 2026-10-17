# -*- coding: utf-8 -*-
"""
Full Authentic Curriculum Generator for Madinah Book 3 (Units 1 to 17)
Every unit structured with authentic multi-tamreen exercises matching the textbook.
"""
from build_b3_u9_questions import get_b3_u9_complete_questions
from generate_b3_deep_curriculum import build_b3_all_units

def get_b3_complete_dataset():
    data = build_b3_all_units()
    
    # -------------------------------------------------------------
    # UNIT 3: الفعل المبني للمجهول ونائب الفاعل • النسب
    # -------------------------------------------------------------
    u3 = []
    # T1: صوغ المبني للمجهول من الماضي
    t1_u3 = [
        ("الْمَبْنِيُّ لِلْمَجْهُولِ مِنَ الْفِعْلِ الْمَاضِي (كَتَبَ) هُوَ: [ ＿＿＿ ]", "كُتِبَ", ["كُتِبَ", "يَكْتُبُ", "كَاتِبٌ", "مَكْتُوبٌ"], "ماضی مجہول بنانے کا قاعدہ: پہلے حرف کو پیش اور آخری سے پہلے کو زیر دیا جاتا ہے۔", "Rule for passive past: first letter takes dammah, penult takes kasrah: kutiba.", "✍️"),
        ("الْمَبْنِيُّ لِلْمَجْهُولِ مِنَ الْفِعْلِ: (خَلَقَ اللَّهُ الإِنْسَانَ) هُوَ: [ ＿＿＿ ]", "خُلِقَ الإِنْسَانُ", ["خُلِقَ الإِنْسَانُ", "خَلَقَ الإِنْسَانَ", "يُخْلَقُ الإِنْسَانُ", "خَالِقُ الإِنْسَانِ"], "فاعل کو حذف کر کے مفعول بہ کو نائب فاعل مرفوع بنا دیا گیا: خُلِقَ الإِنْسَانُ۔", "Subject is omitted, object becomes nominative deputy subject: Khuliqa al-insanu.", "👤"),
        ("الْمَبْنِيُّ لِلْمَجْهُولِ مِنَ الْفِعْلِ: (سَرَقَ اللِّصُّ السَّيَّارَةَ) هُوَ: [ ＿＿＿ ]", "سُرِقَتِ السَّيَّارَةُ", ["سُرِقَتِ السَّيَّارَةُ", "سُرِقَ السَّيَّارَةُ", "سَرَقَتِ السَّيَّارَةُ", "يُسْرَقُ السَّيَّارَةُ"], "نائب فاعل مؤنث ہونے کی وجہ سے فعل کے ساتھ تائے تانیث آئے گی: سُرِقَتْ۔", "Because deputy subject is feminine, verb takes feminine ta: suriqat.", "🚗"),
        ("الْمَبْنِيُّ لِلْمَجْهُولِ مِنَ الْفِعْلِ: (ضَرَبَ حَامِدٌ هِشَاماً) هُوَ: [ ＿＿＿ ]", "ضُرِبَ هِشَامٌ", ["ضُرِبَ هِشَامٌ", "ضَرَبَ هِشَامٌ", "ضَرَبَ هِشَاماً", "يُضْرَبُ هِشَاماً"], "مفعول به (هشاماً) نائب فاعل بن کر مرفوع (هشامٌ) ہو گیا۔", "The object became nominative deputy subject: duriba Hishamun.", "💥")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u3, 1):
        u3.append({
            "id": f"b3_u3_t1_q{idx}", "book": 3, "unit_num": 3, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): ماضی مجہول", "badge_en": "Exercise (1): Passive Past Verbs",
            "tamreen_title_ar": "صَوْغُ الْفِعْلِ الْمَبْنِيِّ لِلْمَجْهُولِ مِنَ الْمَاضِي:",
            "tamreen_title_ur": "ماضی معروف کو ماضی مجہول میں تبدیل کریں:",
            "tamreen_title_en": "Form the passive voice from past tense verbs:",
            "grammar_goal_ur": "فعل ماضی مجہول بنانے کا وزن (فُعِلَ) سمجھنا۔",
            "grammar_goal_en": "Mastering the passive past pattern (Fu'ila).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست صیغہ مجہول منتخب کریں:", "prompt_en": "Select the correct passive form:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: صوغ المبني للمجهول من المضارع
    t2_u3 = [
        ("الْمَبْنِيُّ لِلْمَجْهُولِ مِنَ الْمُضَارِعِ (يَكْتُبُ) هُوَ: [ ＿＿＿ ]", "يُكْتَبُ", ["يُكْتَبُ", "يَكْتُبُ", "كُتِبَ", "مَكْتُوبٌ"], "مضارع مجہول کا قاعدہ: علامت مضارع پر پیش اور آخری سے پہلے پر زبر: يُفْعَلُ۔", "Passive present rule: dammah on prefix, fathah on penult: yuktabu.", "✍️"),
        ("الْمَبْنِيُّ لِلْمَجْهُولِ مِنَ الْمُضَارِعِ (يَقْتُلُ) هُوَ: [ ＿＿＿ ]", "يُقْتَلُ", ["يُقْتَلُ", "يَقْتُلُ", "قُتِلَ", "مَقْتُولٌ"], "صیغہ مجہول: يُقْتَلُ۔", "Passive form: yuqtalu.", "⚔️"),
        ("الْمَبْنِيُّ لِلْمَجْهُولِ مِنْ: (يَسْمَعُ النَّاسُ الأَذَانَ) هُوَ: [ ＿＿＿ ]", "يُسْمَعُ الأَذَانُ", ["يُسْمَعُ الأَذَانُ", "يَسْمَعُ الأَذَانَ", "سُمِعَ الأَذَانُ", "مَسْمُوعٌ الأَذَانُ"], "مضارع مجہول اور نائب فاعل مرفوع: يُسْمَعُ الأَذَانُ۔", "Passive present with nominative deputy subject: yusma'u al-athanu.", "📢")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u3, 1):
        u3.append({
            "id": f"b3_u3_t2_q{idx}", "book": 3, "unit_num": 3, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مضارع مجہول", "badge_en": "Exercise (2): Passive Present Verbs",
            "tamreen_title_ar": "صَوْغُ الْفِعْلِ الْمَبْنِيِّ لِلْمَجْهُولِ مِنَ الْمُضَارِعِ:",
            "tamreen_title_ur": "مضارع معروف کو مضارع مجہول میں تبدیل کریں:",
            "tamreen_title_en": "Form the passive voice from present tense verbs:",
            "grammar_goal_ur": "فعل مضارع مجہول کا وزن (يُفْعَلُ) سمجھنا۔",
            "grammar_goal_en": "Mastering the passive present pattern (Yuf'alu).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست صیغہ مجہول چنیں:", "prompt_en": "Select the correct passive form:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T3: ياء النسب
    t3_u3 = [
        ("الِاسْمُ الْمَنْسُوبُ إِلَى: (مَكَّةُ) هُوَ: [ ＿＿＿ ]", "مَكِّيٌّ", ["مَكِّيٌّ", "مَكَّةٌ", "مَكَّاوِيٌّ", "مَكِينٌ"], "تائے تانیث کو گرا کر آخر میں یاء مشددہ کا اضافہ کیا جاتا ہے: مَكِّيٌّ۔", "Ta marbutah drops, takes doubled ya of nisbah: Makkiyy.", "🕋"),
        ("الِاسْمُ الْمَنْسُوبُ إِلَى: (مِصْرُ) هُوَ: [ ＿＿＿ ]", "مِصْرِيٌّ", ["مِصْرِيٌّ", "مَصْرِيٌّ", "مِصْرَانِيٌّ", "مُمَصَّرٌ"], "مصر کی طرف نسبت: مِصْرِيٌّ۔", "Attributive noun for Egypt: Misriyy.", "🇪🇬"),
        ("الِاسْمُ الْمَنْسُوبُ إِلَى: (نَحْوٌ) هُوَ: [ ＿＿＿ ]", "نَحْوِيٌّ", ["نَحْوِيٌّ", "نَحَّاوٌ", "نَحْوِيَّةٌ", "نَحْوَانُ"], "نحو کے عالم کی طرف نسبت: نَحْوِيٌّ۔", "Attributive noun for grammar: Nahwiyy.", "📖")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t3_u3, 1):
        u3.append({
            "id": f"b3_u3_t3_q{idx}", "book": 3, "unit_num": 3, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): یاء النسب", "badge_en": "Exercise (3): The Relative Suffix (Yaa an-Nisbah)",
            "tamreen_title_ar": "صَوْغُ الاسْمِ الْمَنْسُوبِ (يَاءُ النَّسَبِ):",
            "tamreen_title_ur": "دیے گئے اسم سے اسم منسوب بنائیں:",
            "tamreen_title_en": "Form the attributive adjective with relative suffix (Yaa an-Nisbah):",
            "grammar_goal_ur": "کسی شہر یا علم کی طرف نسبت ظاہر کرنے کے لیے یاء مشددہ کا استعمال۔",
            "grammar_goal_en": "Forming Nisbah adjectives by appending doubled Yaa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست اسم منسوب منتخب کریں:", "prompt_en": "Select the correct nisbah noun:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u3'] = u3

    # -------------------------------------------------------------
    # UNIT 4: اسم الفاعل واسم المفعول من الثلاثي السالم • ما الحجازية
    # -------------------------------------------------------------
    u4 = []
    # T1: اسم الفاعل من الثلاثي السالم
    t1_u4 = [
        ("اسْمُ الْفَاعِلِ مِنَ الْفِعْلِ الثُّلَاثِيِّ (ذَهَبَ) هُوَ: [ ＿＿＿ ]", "ذَاهِبٌ", ["ذَاهِبٌ", "مَذْهُوبٌ", "ذَهَابٌ", "مُذْهِبٌ"], "ثلاثی مجرد سے اسم فاعل 'فَاعِلٌ' کے وزن پر آتا ہے: ذَاهِبٌ۔", "Active participle of Form I triliteral verb is on pattern Faa'il: Thahib.", "🚶‍♂️"),
        ("اسْمُ الْفَاعِلِ مِنَ الْفِعْلِ (كَتَبَ) هُوَ: [ ＿＿＿ ]", "كَاتِبٌ", ["كَاتِبٌ", "مَكْتُوبٌ", "كِتَابٌ", "مَكْتَبٌ"], "اسم فاعل: كَاتِبٌ۔", "Active participle: Katib.", "✍️"),
        ("اسْمُ الْفَاعِلِ مِنَ الْفِعْلِ (سَمِعَ) هُوَ: [ ＿＿＿ ]", "سَامِعٌ", ["سَامِعٌ", "مَسْمُوعٌ", "سَمَاعٌ", "سَمِيعٌ"], "اسم فاعل: سَامِعٌ۔", "Active participle: Sami'.", "👂")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u4, 1):
        u4.append({
            "id": f"b3_u4_t1_q{idx}", "book": 3, "unit_num": 4, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اسم فاعل", "badge_en": "Exercise (1): Active Participle (Ism al-Fa'il)",
            "tamreen_title_ar": "صَوْغُ اسْمِ الْفَاعِلِ عَلَى وَزْنِ (فَاعِل):",
            "tamreen_title_ur": "ثلاثی سالم سے وزن 'فَاعِل' پر اسم فاعل بنائیں:",
            "tamreen_title_en": "Form the active participle on the pattern (Faa'il):",
            "grammar_goal_ur": "ثلاثی مجرد سے اسم فاعل بنانے کا وزن اور اس کا معنی۔",
            "grammar_goal_en": "Deriving active participles from Form I triliteral verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست اسم فاعل منتخب کریں:", "prompt_en": "Select the correct active participle:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: اسم المفعول من الثلاثي السالم
    t2_u4 = [
        ("اسْمُ الْمَفْعُولِ مِنَ الْفِعْلِ الثُّلَاثِيِّ (فَتَحَ) هُوَ: [ ＿＿＿ ]", "مَفْتُوحٌ", ["مَفْتُوحٌ", "فَاتِحٌ", "مِفْتَاحٌ", "فَتَّاحٌ"], "ثلاثی مجرد سے اسم مفعول 'مَفْعُولٌ' کے وزن پر آتا ہے: مَفْتُوحٌ۔", "Passive participle of Form I is on pattern Maf'ool: Maftooh.", "🔓"),
        ("اسْمُ الْمَفْعُولِ مِنَ الْفِعْلِ (شَرِبَ) هُوَ: [ ＿＿＿ ]", "مَشْرُوبٌ", ["مَشْرُوبٌ", "شَارِبٌ", "شَرَابٌ", "مَشْرَبٌ"], "اسم مفعول: مَشْرُوبٌ۔", "Passive participle: Mashroob.", "🥤"),
        ("اسْمُ الْمَفْعُولِ مِنَ الْفِعْلِ (كَسَرَ) هُوَ: [ ＿＿＿ ]", "مَكْسُورٌ", ["مَكْسُورٌ", "كَاسِرٌ", "كَسَّارٌ", "مِكْسَارٌ"], "اسم مفعول: مَكْسُورٌ۔", "Passive participle: Maksoor.", "🔨")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u4, 1):
        u4.append({
            "id": f"b3_u4_t2_q{idx}", "book": 3, "unit_num": 4, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اسم مفعول", "badge_en": "Exercise (2): Passive Participle (Ism al-Maf'ool)",
            "tamreen_title_ar": "صَوْغُ اسْمِ الْمَفْعُولِ عَلَى وَزْنِ (مَفْعُول):",
            "tamreen_title_ur": "ثلاثی سالم سے وزن 'مَفْعُول' پر اسم مفعول بنائیں:",
            "tamreen_title_en": "Form the passive participle on the pattern (Maf'ool):",
            "grammar_goal_ur": "ثلاثی مجرد سے اسم مفعول کے صیغے اور معنی کو پہچاننا۔",
            "grammar_goal_en": "Deriving passive participles from Form I triliteral verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست اسم مفعول منتخب کریں:", "prompt_en": "Select the correct passive participle:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T3: ما الحجازية
    t3_u4 = [
        ("فِي الآيَةِ الْكَرِيمَةِ: {مَا هٰذَا بَشَراً}، إِعْرَابُ كَلِمَةِ (بَشَراً) هُوَ: [ ＿＿＿ ]", "خَبَرُ (مَا) الْحِجَازِيَّةِ مَنْصُوبٌ", ["خَبَرُ (مَا) الْحِجَازِيَّةِ مَنْصُوبٌ", "حَالٌ مَنْصُوبَةٌ", "مَفْعُولٌ بِهِ", "تَمْيِيزٌ مَنْصُوبٌ"], "ما الحجازیۃ فعل 'لیس' کی طرح عمل کرتی ہے: اسم کو رفع اور خبر کو نصب دیتی ہے۔", "Maa al-Hijaziyyah acts like Laysa: raises the subject and marks the predicate accusative.", "📖"),
        ("مَا عَمَلُ (مَا) النَّافِيَةِ الْحِجَازِيَّةِ فِي الْجُمْلَةِ الاسْمِيَّةِ؟ [ ＿＿＿ ]", "تَرْفَعُ الاسْمَ وَتَنْصِبُ الْخَبَرَ كَـ (لَيْسَ)", ["تَرْفَعُ الاسْمَ وَتَنْصِبُ الْخَبَرَ كَـ (لَيْسَ)", "تَنْصِبُ الاسْمَ وَتَرْفَعُ الْخَبَرَ كَـ (إِنَّ)", "تَجْزِمُ الْفِعْلَيْنِ", "لَا عَمَلَ لَهَا"], "ما الحجازیۃ کا عمل لیس جیسا ہوتا ہے۔", "Hijazi Maa acts like Laysa: raises the subject, makes the predicate accusative.", "⚖️")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t3_u4, 1):
        u4.append({
            "id": f"b3_u4_t3_q{idx}", "book": 3, "unit_num": 4, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): ما الحجازیۃ", "badge_en": "Exercise (3): Maa al-Hijaziyyah",
            "tamreen_title_ar": "عَمَلُ (مَا) الْحِجَازِيَّةِ الشَّبِيهَةِ بِـ (لَيْسَ):",
            "tamreen_title_ur": "ما الحجازیۃ کا جملہ اسمیہ پر نحوی عمل پہچانیں:",
            "tamreen_title_en": "Identify the grammatical operation of Maa al-Hijaziyyah:",
            "grammar_goal_ur": "ما الحجازیۃ کے شرائط اور اسم و خبر کے اعراب کا فہم۔",
            "grammar_goal_en": "Mastering the syntax of Hijazi Maa resembling Laysa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست نحوی جواب منتخب کریں:", "prompt_en": "Select the correct grammatical answer:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u4'] = u4

    # -------------------------------------------------------------
    # UNIT 5: اسم الفاعل والمفعول من المعتل • المبني للمجهول من الأجوف
    # -------------------------------------------------------------
    u5 = []
    # T1: اسم الفاعل من الأجوف
    t1_u5 = [
        ("اسْمُ الْفَاعِلِ مِنَ الْفِعْلِ الأَجْوَفِ (قَالَ) هُوَ: [ ＿＿＿ ]", "قَائِلٌ", ["قَائِلٌ", "قَاوِلٌ", "مَقُولٌ", "قَوَّالٌ"], "اجوف میں حرف علت اسم فاعل کے وزن پر ہمزہ میں بدل جاتا ہے: قَائِلٌ۔", "Weak middle letter converts to hamzah in active participle: Qaa'il.", "🗣️"),
        ("اسْمُ الْفَاعِلِ مِنَ الْفِعْلِ الأَجْوَفِ (بَاعَ) هُوَ: [ ＿＿＿ ]", "بَائِعٌ", ["بَائِعٌ", "بَايِعٌ", "مَبِيعٌ", "بَيَّاعٌ"], "اسم فاعل: بَائِعٌ۔", "Active participle: Baa'i'.", "🏷️"),
        ("اسْمُ الْفَاعِلِ مِنَ الْفِعْلِ (صَامَ) هُوَ: [ ＿＿＿ ]", "صَائِمٌ", ["صَائِمٌ", "صَاوِمٌ", "مَصُومٌ", "صَيَّامٌ"], "اسم فاعل: صَائِمٌ۔", "Active participle: Saa'im.", "🌙")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u5, 1):
        u5.append({
            "id": f"b3_u5_t1_q{idx}", "book": 3, "unit_num": 5, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اسم فاعل از اجوف", "badge_en": "Exercise (1): Active Participle from Hollow Verbs",
            "tamreen_title_ar": "صَوْغُ اسْمِ الْفَاعِلِ مِنَ الْفِعْلِ الأَجْوَفِ:",
            "tamreen_title_ur": "اجوف سے اسم فاعل بنائیں (حرف علت کا ہمزہ میں قلب):",
            "tamreen_title_en": "Form the active participle from hollow verbs:",
            "grammar_goal_ur": "اجوف کے اسم فاعل میں اعلان کے قواعد سمجھنا۔",
            "grammar_goal_en": "Rules of I'lal in active participles of hollow verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست اسم فاعل منتخب کریں:", "prompt_en": "Select the correct active participle:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: اسم المفعول من الأجوف
    t2_u5 = [
        ("اسْمُ الْمَفْعُولِ مِنَ الْفِعْلِ الأَجْوَفِ الْوَاوِيِّ (قَالَ يَقُولُ) هُوَ: [ ＿＿＿ ]", "مَقُولٌ", ["مَقُولٌ", "مَقْوُولٌ", "قَائِلٌ", "مُقَالٌ"], "واوی اجوف میں واو مفعول گر جاتا ہے: مَقُولٌ۔", "Wawi hollow verb forms passive participle as Maqool.", "💬"),
        ("اسْمُ الْمَفْعُولِ مِنَ الْفِعْلِ الأَجْوَفِ الْيَائِيِّ (بَاعَ يَبِيعُ) هُوَ: [ ＿＿＿ ]", "مَبِيعٌ", ["مَبِيعٌ", "مَبْيُوعٌ", "بَائِعٌ", "مُبَاعٌ"], "یائی اجوف میں یاء کے مناسبت سے کسرہ آتا ہے: مَبِيعٌ۔", "Ya'i hollow verb forms passive participle as Mabee'.", "🛒"),
        ("الْمَبْنِيُّ لِلْمَجْهُولِ مِنَ الْفِعْلِ الأَجْوَفِ (قَالَ) هُوَ: [ ＿＿＿ ]", "قِيلَ", ["قِيلَ", "قُولَ", "يُقَالُ", "قُوِلَ"], "اجوف ماضی کا مجہول فاء کلمہ کے کسرہ اور یاء کے ساتھ آتا ہے: قِيلَ۔", "Passive past of hollow verb takes kasrah on first radical: Qeela.", "📖")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u5, 1):
        u5.append({
            "id": f"b3_u5_t2_q{idx}", "book": 3, "unit_num": 5, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اسم مفعول از اجوف", "badge_en": "Exercise (2): Passive Participle from Hollow Verbs",
            "tamreen_title_ar": "صَوْغُ اسْمِ الْمَفْعُولِ وَالْمَجْهُولِ مِنَ الأَجْوَفِ:",
            "tamreen_title_ur": "اجوف سے اسم مفعول اور صیغہ مجہول بنائیں:",
            "tamreen_title_en": "Form the passive participle and passive voice from hollow verbs:",
            "grammar_goal_ur": "اجوف واوی اور یائی کے اسم مفعول کے فرق کو سمجھنا۔",
            "grammar_goal_en": "Distinguishing between Wawi and Ya'i passive participles.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست صیغہ منتخب کریں:", "prompt_en": "Select the correct form:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u5'] = u5

    # -------------------------------------------------------------
    # UNIT 6: اسما المكان والزمان (مَفْعَلٌ وَمَفْعِلٌ)
    # -------------------------------------------------------------
    u6 = []
    # T1: وزن مَفْعَل
    t1_u6 = [
        ("اسْمُ الْمَكَانِ مِنَ الْفِعْلِ (لَعِبَ يَلْعَبُ) هُوَ: [ ＿＿＿ ]", "مَلْعَبٌ", ["مَلْعَبٌ", "مَلْعِبٌ", "لَاعِبٌ", "مَلْعُوبٌ"], "مضارع میں عین کلمہ مفتوح ہو تو اسم مکان 'مَفْعَلٌ' پر آتا ہے: مَلْعَبٌ۔", "If mudari' has fathah on 'ayn, noun of place is on Maf'al: Mal'ab.", "⚽"),
        ("اسْمُ الْمَكَانِ مِنَ الْفِعْلِ (كَتَبَ يَكْتُبُ) هُوَ: [ ＿＿＿ ]", "مَكْتَبٌ", ["مَكْتَبٌ", "مَكْتِبٌ", "كَاتِبٌ", "مَكْتُوبٌ"], "مضارع میں عین کلمہ مضموم ہو تو بھی 'مَفْعَلٌ' آتا ہے: مَكْتَبٌ۔", "If mudari' has dammah on 'ayn, noun of place is on Maf'al: Maktab.", "🏢"),
        ("اسْمُ الْمَكَانِ مِنَ الْفِعْلِ (طَبَخَ يَطْبُخُ) هُوَ: [ ＿＿＿ ]", "مَطْبَخٌ", ["مَطْبَخٌ", "مَطْبِخٌ", "طَابِخٌ", "طَبَّاخٌ"], "اسم مکان: مَطْبَخٌ (باورچی خانہ)۔", "Noun of place: Matbakh (kitchen).", "🍳")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u6, 1):
        u6.append({
            "id": f"b3_u6_t1_q{idx}", "book": 3, "unit_num": 6, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اسم مکان بروزن مَفْعَل", "badge_en": "Exercise (1): Noun of Place/Time on (Maf'al)",
            "tamreen_title_ar": "صَوْغُ اسْمِ الْمَكَانِ عَلَى وَزْنِ (مَفْعَل):",
            "tamreen_title_ur": "عین کلمہ مفتوح یا مضموم ہونے پر وزن 'مَفْعَل' بنائیں:",
            "tamreen_title_en": "Form the noun of place/time on the pattern (Maf'al):",
            "grammar_goal_ur": "مضارع کے اعراب کے مطابق اسم مکان و زمان کا وزن طے کرنا۔",
            "grammar_goal_en": "Deriving nouns of place based on the present tense stem vowel.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست وزن منتخب کریں:", "prompt_en": "Select the correct noun of place:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: وزن مَفْعِل (بكسر العين)
    t2_u6 = [
        ("اسْمُ الْمَكَانِ مِنَ الْفِعْلِ (جَلَسَ يَجْلِسُ) هُوَ: [ ＿＿＿ ]", "مَجْلِسٌ", ["مَجْلِسٌ", "مَجْلَسٌ", "جَالِسٌ", "مَجْلُوسٌ"], "مضارع میں عین کلمہ مکسور ہو تو اسم مکان 'مَفْعِلٌ' پر آتا ہے: مَجْلِسٌ۔", "If mudari' has kasrah on 'ayn, noun of place is on Maf'il: Majlis.", "🪑"),
        ("اسْمُ الْمَكَانِ مِنَ الْفِعْلِ الْمِثَالِ (وَقَفَ يَقِفُ) هُوَ: [ ＿＿＿ ]", "مَوْقِفٌ", ["مَوْقِفٌ", "مَوْقَفٌ", "وَاقِفٌ", "مَوْقُوفٌ"], "مثال واوی سے اسم مکان ہمیشہ 'مَفْعِلٌ' پر آتا ہے: مَوْقِفٌ (سٹینڈ / پارکنگ)۔", "Assimilated verbs form noun of place on Maf'il: Mawqif.", "🅿️"),
        ("اسْمُ الْمَكَانِ مِنَ الْفِعْلِ (نَزَلَ يَنْزِلُ) هُوَ: [ ＿＿＿ ]", "مَنْزِلٌ", ["مَنْزِلٌ", "مَنْزَلٌ", "نَازِلٌ", "مَنْزُولٌ"], "اسم مکان: مَنْزِلٌ (گھر)۔", "Noun of place: Manzil (home/residence).", "🏠")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u6, 1):
        u6.append({
            "id": f"b3_u6_t2_q{idx}", "book": 3, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اسم مکان بروزن مَفْعِل", "badge_en": "Exercise (2): Noun of Place/Time on (Maf'il)",
            "tamreen_title_ar": "صَوْغُ اسْمِ الْمَكَانِ عَلَى وَزْنِ (مَفْعِل):",
            "tamreen_title_ur": "عین کلمہ مکسور یا فعل مثال سے وزن 'مَفْعِل' بنائیں:",
            "tamreen_title_en": "Form the noun of place on the pattern (Maf'il):",
            "grammar_goal_ur": "کسرہ والے مضارع اور مثال واوی کے صیغے پہچاننا۔",
            "grammar_goal_en": "Deriving nouns of place with kasrah on the penult.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست صیغہ منتخب کریں:", "prompt_en": "Select the correct form:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u6'] = u6

    # -------------------------------------------------------------
    # UNIT 7: اسم الآلة وأوزانه (مِفْعَل، مِفْعَال، مِفْعَلَة، فَعَّالَة)
    # -------------------------------------------------------------
    u7 = []
    # T1: أوزان مِفْعَال ومِفْعَل
    t1_u7 = [
        ("اسْمُ الآلَةِ مِنَ الْفِعْلِ (فَتَحَ) عَلَى وَزْنِ (مِفْعَال) هُوَ: [ ＿＿＿ ]", "مِفْتَاحٌ", ["مِفْتَاحٌ", "فَاتِحٌ", "مَفْتُوحٌ", "فَتَّاحَةٌ"], "کھولنے کا آلہ: مِفْتَاحٌ (چابی)۔", "Instrument of opening: Miftaah (key).", "🔑"),
        ("اسْمُ الآلَةِ مِنَ الْفِعْلِ (نَشَرَ) عَلَى وَزْنِ (مِفْعَال) هُوَ: [ ＿＿＿ ]", "مِنْشَارٌ", ["مِنْشَارٌ", "نَاشِرٌ", "مَنْشُورٌ", "نَشَّارَةٌ"], "آری (کاٹنے کا اوزار): مِنْشَارٌ۔", "Instrument for sawing: Minshaar (saw).", "🪚"),
        ("اسْمُ الآلَةِ مِنَ الْفِعْلِ (بَرَدَ) عَلَى وَزْنِ (مِفْعَل) هُوَ: [ ＿＿＿ ]", "مِبْرَدٌ", ["مِبْرَدٌ", "مِبْرَادٌ", "بَارِدٌ", "بَرَّادٌ"], "ریتی (رگڑنے کا اوزار): مِبْرَدٌ۔", "File (tool): Mibrad.", "🔧"),
        ("اسْمُ الآلَةِ مِنَ الْفِعْلِ (قَصَّ) عَلَى وَزْنِ (مِفْعَل) هُوَ: [ ＿＿＿ ]", "مِقَصٌّ", ["مِقَصٌّ", "مِقْصَاصٌ", "قَاصٌّ", "قَصَّاصٌ"], "قینچی: مِقَصٌّ۔", "Scissors: Miqass.", "✂️")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u7, 1):
        u7.append({
            "id": f"b3_u7_t1_q{idx}", "book": 3, "unit_num": 7, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): اسم آلہ (مِفْعَال ومِفْعَل)", "badge_en": "Exercise (1): Nouns of Instrument (Mif'aal & Mif'al)",
            "tamreen_title_ar": "صَوْغُ اسْمِ الآلَةِ عَلَى وَزْنَيْ (مِفْعَال) وَ(مِفْعَل):",
            "tamreen_title_ur": "وزن مِفْعَال اور مِفْعَل پر اسم آلہ بنائیں:",
            "tamreen_title_en": "Form nouns of instrument on patterns (Mif'aal) and (Mif'al):",
            "grammar_goal_ur": "اسم آلہ کے اوزان اور ان کے لغوی استعمالات کا فہم۔",
            "grammar_goal_en": "Mastering the standard morphological patterns of tool nouns.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست اسم آلہ چنیں:", "prompt_en": "Select the correct tool noun:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: أوزان مِفْعَلَة وفَعَّالَة
    t2_u7 = [
        ("اسْمُ الآلَةِ مِنَ الْفِعْلِ (كَنَسَ) عَلَى وَزْنِ (مِفْعَلَة) هُوَ: [ ＿＿＿ ]", "مِكْنَسَةٌ", ["مِكْنَسَةٌ", "مِكْنَاسٌ", "كَانِسٌ", "كَنَّاسَةٌ"], "جھاڑو: مِكْنَسَةٌ۔", "Broom: Miknasah.", "🧹"),
        ("اسْمُ الآلَةِ مِنَ الْفِعْلِ (لَعِقَ) عَلَى وَزْنِ (مِفْعَلَة) هُوَ: [ ＿＿＿ ]", "مِلْعَقَةٌ", ["مِلْعَقَةٌ", "مِلْعَاقٌ", "لَاعِقٌ", "لَعَّاقَةٌ"], "چمچ: مِلْعَقَةٌ۔", "Spoon: Mil'aqah.", "🥄"),
        ("اسْمُ الآلَةِ الْحَدِيثُ مِنَ الْفِعْلِ (غَسَلَ) عَلَى وَزْنِ (فَعَّالَة) هُوَ: [ ＿＿＿ ]", "غَسَّالَةٌ", ["غَسَّالَةٌ", "مِغْسَلَةٌ", "غَاسِلٌ", "مَغْسُولٌ"], "کپڑے دھونے کی مشین: غَسَّالَةٌ۔", "Washing machine: Ghassalah.", "🧺"),
        ("اسْمُ الآلَةِ مِنَ الْفِعْلِ (ثَلَجَ) عَلَى وَزْنِ (فَعَّالَة) هُوَ: [ ＿＿＿ ]", "ثَلَّاجَةٌ", ["ثَلَّاجَةٌ", "مِثْلَجَةٌ", "ثَالِجٌ", "مَثْلُوجٌ"], "ریفریجریٹر / فریج: ثَلَّاجَةٌ۔", "Refrigerator: Thallajah.", "🧊")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u7, 1):
        u7.append({
            "id": f"b3_u7_t2_q{idx}", "book": 3, "unit_num": 7, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اسم آلہ (مِفْعَلَة وفَعَّالَة)", "badge_en": "Exercise (2): Patterns (Mif'alah) & (Fa''aalah)",
            "tamreen_title_ar": "صَوْغُ اسْمِ الآلَةِ عَلَى وَزْنَيْ (مِفْعَلَة) وَ(فَعَّالَة):",
            "tamreen_title_ur": "جدید اور قدیم آلات کے اوزان مِفْعَلَة اور فَعَّالَة کی پہچان کریں:",
            "tamreen_title_en": "Form nouns of instrument on (Mif'alah) and modern (Fa''aalah):",
            "grammar_goal_ur": "جدید مشینوں اور گھریلو آلات کے صوتی اوزان کا فہم۔",
            "grammar_goal_en": "Recognizing classical and modern device nouns in Arabic.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست اسم آلہ منتخب کریں:", "prompt_en": "Select the correct tool noun:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u7'] = u7

    # -------------------------------------------------------------
    # UNIT 8: المعرفة والنكرة وأقسام المعارف السبعة
    # -------------------------------------------------------------
    u8 = []
    # T1: أقسام المعارف السبعة
    t1_u8 = [
        ("كَمْ عَدَدُ أَقْسَامِ الْمَعَارِفِ فِي اللُّغَةِ الْعَرَبِيَّةِ؟ [ ＿＿＿ ]", "سَبْعَةُ أَقْسَامٍ", ["سَبْعَةُ أَقْسَامٍ", "خَمْسَةُ أَقْسَامٍ", "ثَلَاثَةُ أَقْسَامٍ", "عَشَرَةُ أَقْسَامٍ"], "معارف کی سات اقسام ہیں: الضمير، العلم، اسم الإشارة، الاسم الموصول، المعرف بأل، المضاف إلى معرفة، المنادى۔", "There are seven categories of definite nouns.", "🔢"),
        ("كَلِمَةُ (مَكَّةُ) هِيَ اسْمُ مَعْرِفَةٍ لِأَنَّهَا: [ ＿＿＿ ]", "عَلَمٌ", ["عَلَمٌ", "مُعَرَّفٌ بِـ (أَلْ)", "ضَمِيرٌ", "مُضَافٌ إِلَى مَعْرِفَةٍ"], "مکہ ایک شہر کا خاص نام (علم) ہے۔", "Makkah is definite because it is a proper noun ('Alam).", "🕋"),
        ("كَلِمَةُ (هٰذَانِ) فِي اللُّغَةِ هِيَ: [ ＿＿＿ ]", "اسْمُ إِشَارَةٍ (مَعْرِفَةٌ)", ["اسْمُ إِشَارَةٍ (مَعْرِفَةٌ)", "اسْمُ نَكِرَةٍ", "اسْمٌ مَوْصُولٌ", "حَرْفٌ"], "اسماء اشارہ تمام کے تمام معارف میں داخل ہیں۔", "Demonstratives are definite nouns.", "👉")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t1_u8, 1):
        u8.append({
            "id": f"b3_u8_t1_q{idx}", "book": 3, "unit_num": 8, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): معارف کی اقسام", "badge_en": "Exercise (1): The Seven Definite Categories",
            "tamreen_title_ar": "أَقْسَامُ الْمَعَارِفِ السَّبْعَةِ فِي اللُّغَةِ:",
            "tamreen_title_ur": "معارف کی ساتوں اقسام اور ان کی علامات پہچانیں:",
            "tamreen_title_en": "Identify the seven categories of definite nouns:",
            "grammar_goal_ur": "معرفہ کے درجات اور اقسام کا احاطہ۔",
            "grammar_goal_en": "Mastering the seven types of definite nouns in Arabic.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست قسم منتخب کریں:", "prompt_en": "Select the correct category:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })

    # T2: المضاف إلى معرفة
    t2_u8 = [
        ("فِي قَوْلِنَا: (كِتَابُ الطَّالِبِ)، اكْتَسَبَتْ كَلِمَةُ (كِتَابُ) التَّعْرِيفَ بِسَبَبِ: [ ＿＿＿ ]", "الإِضَافَةِ إِلَى الْمُعَرَّفِ بِـ (أَلْ)", ["الإِضَافَةِ إِلَى الْمُعَرَّفِ بِـ (أَلْ)", "دُخُولِ التَّنْوِينِ", "كَوْنِهَا عَلَماً", "كَوْنِهَا نَكِرَةً مَقْصُودَةً"], "نکرہ جب معرفہ کی طرف مضاف ہوتا ہے تو خود بھی معرفہ بن جاتا ہے۔", "An indefinite noun becomes definite upon Idafah to a definite noun.", "📖"),
        ("أَيُّ الْكَلِمَاتِ الآتِيَةِ نَكِرَةٌ؟ [ ＿＿＿ ]", "قَلَمٌ", ["قَلَمٌ", "الْقَلَمُ", "قَلَمِي", "هٰذَا"], "'قلمٌ' تنوین کے ساتھ نکرہ ہے جبکہ باقی سب معرفہ ہیں۔", "'Qalamun' with nunation is indefinite, others are definite.", "✏️")
    ]
    for idx, (p_ar, ans, opts, u_h, e_h, em) in enumerate(t2_u8, 1):
        u8.append({
            "id": f"b3_u8_t2_q{idx}", "book": 3, "unit_num": 8, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): معرفہ بذریعہ اضافت", "badge_en": "Exercise (2): Definiteness through Idafah",
            "tamreen_title_ar": "التَّعْرِيفُ بِالإِضَافَةِ وَالتَّمْيِيزُ بَيْنَ النَّكِرَةِ وَالْمَعْرِفَةِ:",
            "tamreen_title_ur": "اضافت کی وجہ سے معرفہ بننے اور نکرہ و معرفہ میں تمیز کے قواعد:",
            "tamreen_title_en": "Definiteness acquired via Idafah and distinguishing indefinite nouns:",
            "grammar_goal_ur": "مضاف کے معرفہ بننے کے ضوابط کا فہم۔",
            "grammar_goal_en": "Understanding how Idafah conveys definiteness.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": p_ar, "prompt_ur": "درست جواب منتخب کریں:", "prompt_en": "Select the correct option:",
            "answer": ans, "options": opts, "emoji": em, "hint_ur": u_h, "hint_en": e_h,
            "explanation_ur": f"درست جواب: '{ans}'۔ {u_h}", "explanation_en": f"Correct answer: '{ans}'. {e_h}"
        })
    data['b3_u8'] = u8

    return data

if __name__ == "__main__":
    b3 = get_b3_complete_dataset()
    for u_id in sorted(b3.keys()):
        qs = b3[u_id]
        tamreens = sorted(list(set(q['tamreen_num'] for q in qs)))
        print(f"{u_id}: {len(qs)} questions across tamreens {tamreens}")
