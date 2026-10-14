import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_book3_questions():
    questions = []

    def q(uid, tnum, bar, bur, ben, tar, tur, ten, gur, gen, qtype, par, pur, pen, ans, opts, em, hur, hen):
        if ans not in opts:
            opts[0] = ans
        questions.append({
            "id": f"b3_u{uid}_t{tnum}_q{len(questions)+1}",
            "book": 3,
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
    q(1, 1, "التَّمْرِينُ (1)", "مشق (1): معرب اور مبنی کی تمیز", "Exercise (1): Declinable vs Indeclinable",
      "عَيِّنِ الْمُعْرَبَ مِنَ الْمَبْنِيِّ فِيمَا يَأْتِي:", "معرب اور مبنی الفاظ کی شناخت کریں:", "Distinguish between Mu'rab and Mabnee words:",
      "معرب وہ ہے جس کا آخر عامل سے بدلے اور مبنی کا آخر ایک حالت پر رہے", "Mu'rab inflects; Mabnee remains invariable",
      "fill_blank", "أَيُّ الْكَلِمَاتِ الآتِيَةِ اسْمٌ مَبْنِيٌّ؟", "صحیح مبنی اسم منتخب کریں:", "Select the indeclinable (Mabnee) noun:",
      "هَـٰذَا", ["هَـٰذَا", "كِتَابٌ", "مُدَرِّسٌ", "قَلَمٌ"], "🏷️",
      "اسمائے اشارہ مبنی ہوتے ہیں: هَـٰذَا", "Demonstrative pronouns are mabnee: haadhaa.")
    q(1, 2, "التَّمْرِينُ (2)", "مشق (2): علاماتِ اعراب اصلیہ و فرعیہ", "Exercise (2): Primary and Secondary Case Endings",
      "مَيِّزْ عَلَامَاتِ الإِعْرَابِ الأَصْلِيَّةَ وَالْفَرْعِيَّةَ:", "اعراب بالحروف اور بالحركات کی پہچان:", "Identify primary vowels vs secondary letter markers:",
      "ضمة، فتحة، كسرة اصلی علامات ہیں اور الف، واو، یاء فرعی", "Dammah, Fathah, Kasrah are primary; letters are secondary",
      "fill_blank", "مَا عَلَامَةُ رَفْعِ (الْمُسْلِمُونَ)؟", "صحیح علامت منتخب کریں:", "Select the marker of the nominative:",
      "الْوَاوُ", ["الْوَاوُ", "الضَّمَّةُ", "النُّونُ", "الْأَلِفُ"], "👥",
      "جمع مذكر سالم کی علامتِ رفع واو ہے", "The marker of the nominative in sound masc. plural is Waw.")
    q(1, 3, "التَّمْرِينُ (3)", "مشق (3): اعرابِ تقدیری", "Exercise (3): Estimated Case Endings (Taqdeeree)",
      "عَيِّنِ الإِعْرَابَ التَّقْدِيرِيَّ فِي الْمَقْصُورِ وَالْمَنْقُوصِ:", "اسم مقصور اور منقوص کا اعراب:", "Taqdeeree inflection on Maqsoor (Mustafaa) and Manqoos (Qaadee):",
      "اسم مقصور پر تمام حرکات تقدیری ہوتی ہیں", "Defective nouns take estimated vowels due to impossibility/heaviness",
      "fill_blank", "جَاءَ [ ＿＿＿ ] إِلَى الْمَحْكَمَةِ .", "صحیح لفظ منتخب کریں:", "Select the correct noun:",
      "الْقَاضِي", ["الْقَاضِي", "الْقَاضِيُ", "الْقَاضُ", "قَاضِيًا"], "⚖️",
      "حالتِ رفع میں منقوص پر ضمہ مقدر ہوتا ہے: الْقَاضِي", "In nominative, dammah is estimated: al-Qaadee.")

    # UNIT 2
    q(2, 1, "التَّمْرِينُ (1)", "مشق (1): فہمِ متن", "Exercise (1): Text Comprehension",
      "أجب عن الأسئلة الآتية:", "سبق کی روشنی میں جواب دیں:", "Answer based on the dialogue:",
      "فہمِ عبارت اور عربی جواب", "Comprehension of the dialogue",
      "dialogue_qa", "كَيْفَ أَمَرَ الْمُدَرِّسُ مُعَاوِيَةَ أَنْ يَقْرَأَ؟", "صحیح جواب منتخب کریں:", "Select the correct answer:",
      "أَمَرَهُ أَنْ يَقْرَأَ وَهُوَ جَالِسٌ", ["أَمَرَهُ أَنْ يَقْرَأَ وَهُوَ جَالِسٌ", "أَمَرَهُ أَنْ يَقُومَ", "أَمَرَهُ أَنْ يَسْكُتَ", "أَمَرَهُ أَنْ يَخْرُجَ"], "🪑",
      "استاذ نے فرمایا: بیٹھ کر پڑھو (وَأَنْتَ جَالِسٌ)", "The teacher told him to read while sitting.")
    q(2, 2, "التَّمْرِينُ (2)", "مشق (2): واوِ حال کا استعمال", "Exercise (2): Using Waaw al-Haal",
      "اسْتَعْمِلْ (وَاوَ الْحَالِ) مَعَ الْجُمْلَةِ الاسْمِيَّةِ:", "واو حال کے بعد جملہ اسمیہ جوڑیں:", "Link circumstantial nominal clause with Waaw al-Haal:",
      "واو حال کے بعد مبتدا اور خبر مل کر حال بنتے ہیں", "Waaw al-Haal links a circumstantial state sentence",
      "fill_blank", "دَخَلَ الْمُدَرِّسُ الْفَصْلَ [ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "وَهُوَ يَبْتَسِمُ", ["وَهُوَ يَبْتَسِمُ", "يَبْتَسِمُ هُوَ", "وَابْتَسَمَ", "بِابْتِسَامٍ"], "😊",
      "واو حال کے ساتھ: وَهُوَ يَبْتَسِمُ (مسکراتے ہوئے)", "Circumstantial clause: wa-huwa yabtasimu.")
    q(2, 3, "التَّمْرِينُ (3)", "مشق (3): اعرابِ حال (نصب)", "Exercise (3): Case of Haal (Accusative)",
      "اضْبِطِ الْحَالَ الْمُفْرَدَةَ بِالنَّصْبِ:", "حال مفرد پر ہمیشہ فتحہ (زبر) دیں:", "Inflect singular Haal with accusative fathah:",
      "حال ہمیشہ حالتِ نصب میں ہوتی ہے", "The circumstantial qualifier (Haal) is always mansoob",
      "fill_blank", "رَجَعَ الْوَلَدُ مِنَ الْمَدْرَسَةِ [ ＿＿＿ ] .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "فَرِحًا", ["فَرِحًا", "فَرِحٌ", "فَرِحٍ", "فَرِحْ"], "😄",
      "حال منصوب ہوتی ہے: فَرِحًا (خوشی کی حالت میں)", "Haal is mansoob: farihan.")

    # UNIT 3
    q(3, 1, "التَّمْرِينُ (1)", "مشق (1): ماضی مجہول کی ساخت", "Exercise (1): Passive Voice Past Tense",
      "صُغِ الْفِعْلَ الْمَاضِيَ لِلْمَجْهُولِ:", "پہلے پر پیش اور دوسرے پر زیر کا اصول (فُعِلَ):", "Form the passive past tense on pattern Fu'ila:",
      "ماضی مجہول بنانے کے لیے پہلے حرف کو ضمہ اور ماقبل آخر کو کسرہ دیتے ہیں", "Past passive is formed by dammah on 1st and kasrah on penultimate letter",
      "fill_blank", "كَتَبَ حَامِدٌ الدَّرْسَ ➔ [ ＿＿＿ ] الدَّرْسُ .", "صحیح مجہول منتخب کریں:", "Select the correct passive verb:",
      "كُتِبَ", ["كُتِبَ", "كَتَبَ", "كُتُبَ", "يُكْتَبُ"], "✍️",
      "كَتَبَ سے مجہول: كُتِبَ (لکھا گیا)", "Passive of kataba is kutiba.")
    q(3, 2, "التَّمْرِينُ (2)", "مشق (2): نائب الفاعل کا اعراب (رفع)", "Exercise (2): Case of Naa'ib al-Faa'il (Nominative)",
      "اضْبِطْ نَائِبَ الْفَاعِلِ بِالرَّفْعِ:", "مجہول کے بعد نائب الفاعل کو مرفوع (پیش) کریں:", "Make the deputy agent (Naa'ib al-Faa'il) marfoo' (dammah):",
      "نائب الفاعل فاعل کی جگہ لے کر مرفوع ہو جاتا ہے", "Naa'ib al-Faa'il takes the place of subject and becomes marfoo'",
      "fill_blank", "خُلِقَ [ ＿＿＿ ] مِنْ طِينٍ .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "الإِنْسَانُ", ["الإِنْسَانُ", "الإِنْسَانَ", "الإِنْسَانِ", "الإِنْسَانْ"], "🧍",
      "نائب الفاعل مرفوع ہوتا ہے: خُلِقَ الإِنْسَانُ", "Naa'ib al-faa'il is marfoo': al-Insaanu.")
    q(3, 3, "التَّمْرِينُ (3)", "مشق (3): النَّسَبُ (یائے مشددہ)", "Exercise (3): Nisbah (Attributive Suffix -iyy)",
      "انْسُبْ إِلَى الأَسْمَاءِ الآتِيَةِ:", "یائے مشدد کے ساتھ نسبت بنائیں:", "Form the nisbah adjective by adding -iyy:",
      "اسم کے آخر میں یائے مشددہ لگا کر منسوب بناتے ہیں", "Nisbah adds a doubled Yaa preceded by kasrah",
      "fill_blank", "مَا النِّسْبَةُ إِلَى (مِصْرُ)؟", "صحیح منسوب منتخب کریں:", "Select the correct relative adjective:",
      "مِصْرِيٌّ", ["مِصْرِيٌّ", "مِصْرٌ", "مَصَّارٌ", "مِصْرَانِ"], "🇪🇬",
      "مصر کی نسبت: مِصْرِيٌّ", "Nisbah to Misr is Misriyyun.")

    # UNIT 4
    q(4, 1, "التَّمْرِينُ (1)", "مشق (1): اسمِ فاعل (فَاعِل)", "Exercise (1): Active Participle (Faa'il)",
      "صُغِ اسْمَ الْفَاعِلِ مِنَ الأَفْعَالِ الآتِيَةِ:", "ثلاثی مجرد سے 'فَاعِل' کے وزن پر اسم فاعل بنائیں:", "Form active participle on pattern Faa'il:",
      "کام کرنے والے کے لیے وزن 'فَاعِل' ہے", "Active participle denotes the doer on pattern Faa'il",
      "fill_blank", "سَرَقَ اللِّصُّ الْمَالَ ➔ هُوَ [ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "سَارِقٌ", ["سَارِقٌ", "مَسْرُوقٌ", "سَرِيقٌ", "سَرَّاقٌ"], "🦹",
      "سرق سے اسم فاعل: سَارِقٌ (چور)", "Active participle: saariqun.")
    q(4, 2, "التَّمْرِينُ (2)", "مشق (2): اسمِ مفعول (مَفْعُول)", "Exercise (2): Passive Participle (Maf'ool)",
      "صُغِ اسْمَ الْمَفْعُولِ مِنَ الأَفْعَالِ الآتِيَةِ:", "جس پر کام واقع ہو اس کے لیے 'مَفْعُول' کا وزن:", "Form passive participle on pattern Maf'ool:",
      "مفعول وہ اسم ہے جو مَفْعُول کے وزن پر آئے", "Passive participle denotes what action was done upon on pattern Maf'ool",
      "fill_blank", "سَرَقَ اللِّصُّ الْمَالَ ➔ الْمَالُ [ ＿＿＿ ] .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "مَسْرُوقٌ", ["مَسْرُوقٌ", "سَارِقٌ", "سَرِيقٌ", "سِرْقَةٌ"], "💰",
      "سرق سے اسم مفعول: مَسْرُوقٌ (چوری شدہ)", "Passive participle: masrooqun.")
    q(4, 3, "التَّمْرِينُ (3)", "مشق (3): مَـا الْحِجَازِيَّةُ (الْمُشَبَّهَةُ بِلَيْسَ)", "Exercise (3): Maa al-Hijaaziyyah (Acts like Laysa)",
      "أَعْرِبْ خَبَرَ (مَا) الْحِجَازِيَّةِ:", "ما حجازیہ کی خبر کو منصوب یا باء سے مجرور کریں:", "Inflect predicate of Maa al-Hijaaziyyah (mansoob or with baa):",
      "ما الحجازیۃ لیس کی طرح عمل کرتی ہے", "Maa al-Hijaaziyyah acts like Laysa",
      "fill_blank", "{ وَمَا اللَّهُ [ ＿＿＿ ] عَمَّا تَعْمَلُونَ } .", "صحیح کلمہ منتخب کریں:", "Select the correct word from Quran:",
      "بِغَافِلٍ", ["بِغَافِلٍ", "غَافِلٌ", "غَافِلٍ", "بِغَافِلٌ"], "📖",
      "قرآن مجید میں: وَمَا اللَّهُ بِغَافِلٍ", "In Quran: wa maa Allaahu bi-ghaafilin.")

    # UNIT 5
    q(5, 1, "التَّمْرِينُ (1)", "مشق (1): اسم فاعل اجوف سے (قَائِل، بَائِع)", "Exercise (1): Participles of Hollow Verbs",
      "صُغِ اسْمَ الْفَاعِلِ مِنَ الأَفْعَالِ الْجَوْفَاءِ:", "اجوف میں حرف علت کو ہمزہ میں بدلنے کا اصول:", "Hollow verb active participle converts weak root to hamzah (qa'il, ba'i'):",
      "اجوف کے اسم فاعل میں عین کلمہ ہمزہ بن جاتا ہے", "Middle weak letter becomes hamzah in active participle",
      "fill_blank", "مَا اسْمُ الْفَاعِلِ مِنْ (قَالَ)؟", "صحیح اسم فاعل منتخب کریں:", "Select the correct active participle:",
      "قَائِلٌ", ["قَائِلٌ", "قَاوِلٌ", "مَقُولٌ", "قَوْلٌ"], "🗣️",
      "قال سے اسم فاعل: قَائِلٌ", "Active participle of qaala is qaa'ilun.")
    q(5, 2, "التَّمْرِينُ (2)", "مشق (2): اسم مفعول اجوف سے (مَقُول، مَبِيع)", "Exercise (2): Passive Participles of Hollow Verbs",
      "صُغِ اسْمَ الْمَفْعُولِ مِنَ الأَفْعَالِ الْجَوْفَاءِ:", "مقول اور مبیع کے اوزان:", "Form passive participle of hollow verbs (maqool, mabee'):",
      "اجوف واوی میں مقول اور یائی میں مبیع بنتا ہے", "Waw hollow verbs take maqool; Yaa hollow verbs take mabee'",
      "fill_blank", "مَا اسْمُ الْمَفْعُولِ مِنْ (بَاعَ)؟", "صحیح اسم مفعول منتخب کریں:", "Select the correct passive participle:",
      "مَبِيعٌ", ["مَبِيعٌ", "مَبْيُوعٌ", "بَائِعٌ", "بَيْعٌ"], "🏷️",
      "باع کا اسم مفعول: مَبِيعٌ (نہ کہ مبیوع)", "Passive participle of baa'a is mabee'un.")

    # UNIT 6
    q(6, 1, "التَّمْرِينُ (1)", "مشق (1): اسمائے زمان و مکان (مَفْعَل و مَفْعِل)", "Exercise (1): Nouns of Time and Place (Maf'al and Maf'il)",
      "صُغِ اسْمَ الْمَكَانِ عَلَى وَزْنِ (مَفْعَل) أَوْ (مَفْعِل):", "مقام اور وقت کا اسم بنانے کا اصول:", "Form nouns of place and time on patterns Maf'al and Maf'il:",
      "مقام کے لیے مَفْعَل (جیسے مَكْتَب) اور مَفْعِل (جیسے مَوْعِد) آتا ہے", "Nouns of place/time use Maf'al or Maf'il",
      "fill_blank", "وَضَعَ الْمُدَرِّسُ الْكِتَابَ عَلَى [ ＿＿＿ ] .", "صحیح اسم مکان منتخب کریں:", "Select the correct noun of place:",
      "الْمَكْتَبِ", ["الْمَكْتَبِ", "الْكَاتِبِ", "الْمَكْتُوبِ", "الْكِتَابَةِ"], "🗄️",
      "كَتَبَ کا اسم مکان: مَكْتَبٌ (میز / دفتر)", "Noun of place: maktabun.")
    q(6, 2, "التَّمْرِينُ (2)", "مشق (2): اسمِ مکان معتل سے (مَوْعِد)", "Exercise (2): Noun of Place/Time from Assimilated Verbs",
      "صُغِ اسْمَ الزَّمَانِ أَوْ الْمَكَانِ مِنْ (وَعَدَ):", "مثال واوی سے مَفْعِل کا وزن:", "Assimilated verbs take Maf'il (wa'ada -> maw'id):",
      "مثال واوی سے اسم زمان/مکان 'مَفْعِل' (کسرہ) کے وزن پر آتا ہے", "Assimilated verbs form noun of time/place on pattern Maf'il",
      "fill_blank", "مَا اسْمُ الزَّمَانِ أَوْ الْمَكَانِ مِنْ (وَعَدَ)؟", "صحیح لفظ منتخب کریں:", "Select the correct word:",
      "مَوْعِدٌ", ["مَوْعِدٌ", "مَوْعَدٌ", "وَاعِدٌ", "مَوْعُودٌ"], "📅",
      "وعد کا اسم زمان: مَوْعِدٌ (وقتِ وعدہ)", "Noun of time: maw'idun.")

    # UNIT 7
    q(7, 1, "التَّمْرِينُ (1)", "مشق (1): اسمِ آلہ کے اوزان (مِفْعَال، مِفْعَل، مِفْعَلَة)", "Exercise (1): Nouns of Instrument (Ism al-Aalah)",
      "صُغِ اسْمَ الآلَةِ مِنَ الأَفْعَالِ الآتِيَةِ:", "اوزار اور آلہ کا اسم بنائیں:", "Form noun of instrument on pattern Mif'aal, Mif'al, Mif'alah:",
      "اسم آلہ کے مشہور اوزان: مِفْتَاح، مِبْرَد، مِكْنَسَة", "Ism al-Aalah patterns: Mif'aal (miftaah), Mif'alah (miknasah)",
      "fill_blank", "فَتَحَ الْبَابَ بِـ [ ＿＿＿ ] .", "صحیح اسم آلہ منتخب کریں:", "Select the correct instrument noun:",
      "الْمِفْتَاحِ", ["الْمِفْتَاحِ", "الْفَاتِحِ", "الْمَفْتُوحِ", "الْفَتْحِ"], "🔑",
      "فتح کا اسم آلہ: مِفْتَاحٌ (چابی)", "Instrument of fataha is miftaahun (key).")
    q(7, 2, "التَّمْرِينُ (2)", "مشق (2): اسمِ آلہ بر وزن مِفْعَلَة (مِكْنَسَة)", "Exercise (2): Noun of Instrument (Mif'alah)",
      "صُغِ اسْمَ الآلَةِ عَلَى وَزْنِ (مِفْعَلَة):", "صفائی کے آلے کا نام:", "Form instrument noun on pattern Mif'alah (miknasah):",
      "کنس سے جھاڑو کے لیے: مِكْنَسَة", "Noun of instrument for sweeping: miknasah",
      "fill_blank", "كَنَسْتُ الْغُرْفَةَ بِـ [ ＿＿＿ ] .", "صحیح لفظ منتخب کریں:", "Select the correct word:",
      "الْمِكْنَسَةِ", ["الْمِكْنَسَةِ", "الْكَانِسِ", "الْمَكْنُوسِ", "الْكَنْسِ"], "🧹",
      "کنس کا آلہ: مِكْنَسَةٌ", "Instrument of sweeping: miknasatun.")

    # UNIT 8
    q(8, 1, "التَّمْرِينُ (1)", "مشق (1): تعجب کا صیغہ (مَا أَفْعَلَهُ)", "Exercise (1): Exclamatory Pattern 'Maa Af'alahu!'",
      "صُغْ أُسْلُوبَ التَّعَجُّبِ مِنَ الْجُمَلِ الآتِيَةِ:", "تعجب میں متعجب منہ کو منصوب (زبر) کریں:", "Form exclamatory sentence (Maa Af'ala + accusative noun):",
      "ما أفعلَ کے بعد والا اسم ہمیشہ منصوب (فتحة) ہوتا ہے", "The noun after 'Maa Af'ala' is always accusative (fathah)",
      "fill_blank", "السَّيَّارَةُ جَمِيلَةٌ ➔ مَا [ ＿＿＿ ] السَّيَّارَةَ ! ", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "أَجْمَلَ", ["أَجْمَلَ", "أَجْمَلُ", "جَمِيلَةٌ", "مُجْمَلٌ"], "🚗",
      "تعجب کا صیغہ مبنی بر فتحہ: مَا أَجْمَلَ", "Exclamatory verb takes fathah: Maa ajmala.")
    q(8, 2, "التَّمْرِينُ (2)", "مشق (2): تعجب کا صیغہ ثانی (أَفْعِلْ بِهِ)", "Exercise (2): Second Exclamatory Pattern 'Af'il bihi!'",
      "صُغِ التَّعَجُّبَ عَلَى صِيغَةِ (أَفْعِلْ بِـ):", "تعجب کا دوسرا صیغہ:", "Form exclamation on pattern Af'il bihi:",
      "تعجب کا دوسرا قرآنی صیغہ: أَفْعِلْ بِهِ (جیسے أَسْمِعْ بِهِمْ وَأَبْصِرْ)", "Second pattern of exclamation: Af'il bihi",
      "fill_blank", "{ أَسْمِعْ بِهِمْ [ ＿＿＿ ] } .", "صحیح قرآنی لفظ منتخب کریں:", "Select the correct Quranic word:",
      "وَأَبْصِرْ", ["وَأَبْصِرْ", "وَأَبْصَرَ", "وَبَصِيرٌ", "وَإِبْصَارٌ"], "👁️",
      "قرآن مجید میں: أَسْمِعْ بِهِمْ وَأَبْصِرْ", "In Quran: asmi' bihim wa absir.")

    # UNIT 9
    q(9, 1, "التَّمْرِينُ (1)", "مشق (1): افعالِ مقاربہ (كَادَ يَفْعَلُ)", "Exercise (1): Verbs of Proximity ('Kaada')",
      "اسْتَعْمِلْ (كَادَ) الدَّالَّةَ عَلَى الْمُقَارَبَةِ:", "کاد کا عمل (اسم مرفوع اور خبر جملہ مضارعیہ):", "Using 'Kaada' with present verb predicate:",
      "کاد کان کی طرح عمل کرتی ہے لیکن اس کی خبر فعل مضارع ہوتی ہے", "Kaada governs a marfoo' noun and present verb predicate",
      "fill_blank", "كَادَ الْوَلَدُ [ ＿＿＿ ] عَلَى الأَرْضِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "يَقَعُ", ["يَقَعُ", "وَقَعَ", "أَنْ يَقَعَ", "وَاقِعًا"], "🤸",
      "کاد کی خبر مضارع: كَادَ الْوَلَدُ يَقَعُ", "Predicate is mudari': kaada al-waladu yaqa'u.")
    q(9, 2, "التَّمْرِينُ (2)", "مشق (2): افعالِ رجاء (عَسَى)", "Exercise (2): Verbs of Hope ('Asaa')",
      "اسْتَعْمِلْ (عَسَى) الدَّالَّةَ عَلَى الرَّجَاءِ:", "عسیٰ کے بعد 'أن' اور مضارع کا لانا:", "Using 'Asaa' (governs 'an' + subjunctive verb):",
      "عسیٰ کے بعد اکثر أنْ اور فعل مضارع منصوب آتا ہے", "'Asaa is usually followed by 'an' and subjunctive verb",
      "fill_blank", "{ فَعَسَى اللَّهُ أَنْ [ ＿＿＿ ] بِالْفَتْحِ } .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "يَأْتِيَ", ["يَأْتِيَ", "يَأْتِيُ", "يَأْتِي", "أَتَى"], "📖",
      "أنْ کی وجہ سے فتحة: أَنْ يَأْتِيَ", "Subjunctive with fathah: an ya'tiya.")

    # UNIT 10
    q(10, 1, "التَّمْرِينُ (1)", "مشق (1): لائے نفی جنس کا عمل (مفرد)", "Exercise (1): Absolute Negation (Single Noun)",
      "اضْبِطِ اسْمَ (لَا) النَّافِيَةِ لِلْجِنْسِ:", "اسم لائے نفی جنس کو بغیر تنوین کے مبنی بر فتحہ کریں:", "Ism of Laa an-Naafiyah lil-Jins is built on fathah without tanween:",
      "لائے نفی جنس کا اسم نکرہ مفرد ہو تو مبنی بر فتحہ ہوتا ہے", "The single noun after categorical Laa is built on fathah without tanween",
      "fill_blank", "لَا [ ＿＿＿ ] فِي الْفَصْلِ .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "طَالِبَ", ["طَالِبَ", "طَالِبٌ", "طَالِبًا", "طَالِبٍ"], "🏫",
      "لائے نفی جنس کا اسم: لَا طَالِبَ (بغیر تنوین)", "Built on single fathah: laa taaliba.")
    q(10, 2, "التَّمْرِينُ (2)", "مشق (2): لائے نفی جنس کا اسم مضاف (منصوب)", "Exercise (2): Mudhaf Ism of Laa an-Naafiyah",
      "اضْبِطِ اسْمَ (لَا) إِذَا كَانَ مُضَافًا:", "مضاف اسم کو منصوب بالفتحة کریں:", "When the noun after categorical Laa is mudhaf, it is mansoob:",
      "لائے نفی جنس کا اسم اگر مضاف ہو تو معرب اور منصوب ہوتا ہے", "If mudhaf, the ism of categorical Laa is inflected as mansoob",
      "fill_blank", "لَا طَالِبَ [ ＿＿＿ ] كَسْلَانٌ .", "صحیح لفظ منتخب کریں:", "Select the correct form:",
      "عِلْمٍ", ["عِلْمٍ", "عِلْمٌ", "عِلْمًا", "عِلْمْ"], "📚",
      "مضاف الیہ مجرور: طَالِبَ عِلْمٍ", "Mudaaf ilayh is majroor: taaliba 'ilmin.")

    # UNIT 11
    q(11, 1, "التَّمْرِينُ (1)", "مشق (1): مفعول مطلق مؤکد", "Exercise (1): Absolute Object (Reinforcing)",
      "عَيِّنِ الْمَفْعُولَ الْمُطْلَقَ الْمَنْصُوبَ:", "فعل کے ہم لفظ مصدر کو مفعول مطلق کے طور پر پہچانیں:", "Identify cognate accusative (verbal noun reinforcing action):",
      "مفعول مطلق فعل کے لفظ سے ماخوذ منصوب مصدر ہوتا ہے", "Maf'ool Mutlaq is an accusative verbal noun matching the verb root",
      "fill_blank", "ضَرَبْتُ الْكَلْبَ [ ＿＿＿ ] .", "صحیح مفعول مطلق منتخب کریں:", "Select the correct absolute object:",
      "ضَرْبًا", ["ضَرْبًا", "ضَرْبٌ", "ضَرْبٍ", "ضَارِبًا"], "🐕",
      "تاکید کے لیے مفعول مطلق: ضَرْبًا", "Reinforcing absolute object: darban.")
    q(11, 2, "التَّمْرِينُ (2)", "مشق (2): مفعول مطلق مبین للنوع والعدد", "Exercise (2): Absolute Object (Manner and Number)",
      "عَيِّنِ الْمَفْعُولَ الْمُطْلَقَ الْمُبَيِّنَ لِلْعَدَدِ:", "تعداد ظاہر کرنے والا مفعول مطلق:", "Absolute object indicating number of occurrences:",
      "تعداد کے لیے فعل سے مصدر مرہ لایا جاتا ہے", "Verbal noun of instance shows number of actions",
      "fill_blank", "سَجَدْتُ لِلَّهِ [ ＿＿＿ ] .", "صحیح عدد منتخب کریں:", "Select the correct word:",
      "سَجْدَتَيْنِ", ["سَجْدَتَيْنِ", "سَجْدَتَانِ", "سُجُودًا", "سَاجِدًا"], "🕌",
      "دو سجدوں کے لیے منصوب بالیاء: سَجْدَتَيْنِ", "Two prostrations: sajdatayni.")

    # UNIT 12
    q(12, 1, "التَّمْرِينُ (1)", "مشق (1): مفعول لہ / لأجلہ (سبب و غرض)", "Exercise (1): Object of Reason (al-Maf'ool li-Ajlihi)",
      "عَيِّنِ الْمَفْعُولَ لِأَجْلِهِ فِي الْجُمْلَةِ:", "فعل کا سبب بتانے والے منصوب مصدر کی پہچان:", "Identify accusative noun stating reason/motive of action:",
      "مفعول لہ وہ قلبی مصدر ہے جو فعل کا سبب ظاہر کرے", "Maf'ool li-ajlihi states the motive behind the action",
      "fill_blank", "قُمْتُ [ ＿＿＿ ] لِلْمُعَلِّمِ .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "إِكْرَامًا", ["إِكْرَامًا", "إِكْرَامٌ", "إِكْرَامٍ", "مُكْرِمًا"], "👨‍🏫",
      "سبب بتانے والا مفعول لہ منصوب: إِكْرَامًا (تعظیم کے لیے)", "Object of reason: ikraaman.")
    q(12, 2, "التَّمْرِينُ (2)", "مشق (2): مفعول معہ (واو معیت)", "Exercise (2): Object of Accompaniment (al-Maf'ool Ma'ahu)",
      "عَيِّنِ الْمَفْعُولَ مَعَهُ بَعْدَ وَاوِ الْمَعِيَّةِ:", "واو معیت کے بعد آنے والا اسم منصوب ہوتا ہے:", "The noun following Waw of accompaniment (meaning 'along with') is mansoob:",
      "واو بمعنی ساتھ کے بعد اسم منصوب مفعول معہ کہلاتا ہے", "Noun after Waw of accompaniment is mansoob",
      "fill_blank", "سِرْتُ وَ[ ＿＿＿ ] .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "الشَّاطِئَ", ["الشَّاطِئَ", "الشَّاطِئُ", "الشَّاطِئِ", "الشَّاطِئْ"], "🏖️",
      "واو معیت کے بعد مفعول معہ منصوب: وَالشَّاطِئَ", "Object of accompaniment: wash-shaati'a.")

    # UNIT 13
    q(13, 1, "التَّمْرِينُ (1)", "مشق (1): تمیز المقادیر (پیمانے اور وزن کی تمیز)", "Exercise (1): Specification of Measure (Tamyeez)",
      "عَيِّنِ التَّمْيِيزَ الْمَنْصُوبَ:", "ابہام دور کرنے والے منصوب اسم کی پہچان:", "Identify the accusative noun clarifying ambiguous measure/statement:",
      "تمیز وہ اسم نکرہ منصوب ہے جو ماقبل کے ابہام کو دور کرے", "Tamyeez is an indefinite accusative clarifying prior ambiguity",
      "fill_blank", "اشْتَرَيْتُ كِيلُو غِرَامًا [ ＿＿＿ ] .", "صحیح تمیز منتخب کریں:", "Select the correct Tamyeez:",
      "سُكَّرًا", ["سُكَّرًا", "سُكَّرٌ", "سُكَّرٍ", "السُّكَّرُ"], "🧂",
      "مقدار کی تمیز منصوب: سُكَّرًا", "Tamyeez of weight: sukkaran.")
    q(13, 2, "التَّمْرِينُ (2)", "مشق (2): تمیز النسبة (جملے کی تمیز)", "Exercise (2): Tamyeez of Sentence / Relation",
      "عَيِّنْ تَمْيِيزَ النِّسْبَةِ فِي الآيَةِ الْكَرِيمَةِ:", "جملے کی نسبت سے ابہام دور کرنے والی تمیز:", "Identify Tamyeez clarifying sentence relation:",
      "قرآن مجید میں جملے کی نسبت کی تمیز منصوب آئی ہے", "Tamyeez of relation in Quran",
      "fill_blank", "{ وَاشْتَعَلَ الرَّأْسُ [ ＿＿＿ ] } .", "صحیح قرآنی کلمہ منتخب کریں:", "Select the correct Quranic word:",
      "شَيْبًا", ["شَيْبًا", "شَيْبٌ", "شَيْبٍ", "الشَّيْبُ"], "👴",
      "تمیز نسبت منصوب: شَيْبًا (بڑھاپے سے)", "Tamyeez of relation: shayban.")

    # UNIT 14
    q(14, 1, "التَّمْرِينُ (1)", "مشق (1): مستثنیٰ بـ (إِلَّا)", "Exercise (1): Exception with 'Illaa' (Mustathnaa)",
      "اضْبِطِ الْمُسْتَثْنَى بَعْدَ (إِلَّا) فِي الْكَلَامِ التَّامِّ الْمُوجَبِ:", "کلام تام موجب میں مستثنیٰ کو واجب النصب کریں:", "Inflect noun after 'Illaa' with mandatory accusative in positive speech:",
      "کلام مثبت تام میں الا کے بعد اسم منصوب ہوتا ہے", "In complete positive sentences, the noun after Illaa is strictly mansoob",
      "fill_blank", "حَضَرَ الطُّلَّابُ إِلَّا [ ＿＿＿ ] .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "حَامِدًا", ["حَامِدًا", "حَامِدٌ", "حَامِدٍ", "حَامِدْ"], "👨‍🎓",
      "مستثنیٰ منصوب: إِلَّا حَامِدًا", "Mustathnaa is mansoob: illaa Haamidan.")
    q(14, 2, "التَّمْرِينُ (2)", "مشق (2): الاستثناء بـ (غَيْر) و(سِوَى)", "Exercise (2): Exception with Ghayr and Siwaa",
      "اضْبِطِ الاسْمَ بَعْدَ (غَيْرِ):", "غیر اور سویٰ کے بعد اسم ہمیشہ مجرور ہوتا ہے:", "The noun following 'Ghayr' and 'Siwaa' is always genitive (majroor):",
      "غیر اور سویٰ مضاف بنتے ہیں اس لیے مابعد اسم مجرور ہوتا ہے", "Ghayr and Siwaa act as mudaaf; noun following is majroor",
      "fill_blank", "حَضَرَ الطُّلَّابُ غَيْرَ [ ＿＿＿ ] .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "عَلِيٍّ", ["عَلِيٍّ", "عَلِيًّا", "عَلِيٌّ", "عَلِيّْ"], "👨",
      "غیر کے بعد مضاف الیہ مجرور: غَيْرَ عَلِيٍّ", "Majroor after ghayr: ghayra 'Aliyyin.")

    # UNIT 15
    q(15, 1, "التَّمْرِينُ (1)", "مشق (1): ادواتِ شرط جازمہ (إِنْ، مَنْ)", "Exercise (1): Conditional Particles (Jussive on both verbs)",
      "اضْبِطْ فِعْلَ الشَّرْطِ وَجَوَابَهُ بِالْجَزْمِ:", "ادوات شرط دو فعلوں (شرط اور جزاء) کو جزم دیتی ہیں:", "Conditional particles place both condition and result verbs in jussive:",
      "إنْ اور مَنْ دو فعل مضارع کو مجزوم (ساکن) کرتے ہیں", "In and Man make both conditional verbs majzoom (sukoon)",
      "fill_blank", "مَنْ [ ＿＿＿ ] يَنْجَحْ .", "صحیح فعل شرط منتخب کریں:", "Select the correct conditional verb:",
      "يَجْتَهِدْ", ["يَجْتَهِدْ", "يَجْتَهِدُ", "يَجْتَهِدَ", "اجْتَهَدَ"], "🎯",
      "فعل شرط مجزوم بالسكون: يَجْتَهِدْ", "Condition verb is majzoom: yajtahid.")
    q(15, 2, "التَّمْرِينُ (2)", "مشق (2): اقتران جواب الشرط بالفاء", "Exercise (2): Coupling Condition Result with Faa",
      "أَدْخِلِ الْفَاءَ عَلَى جَوَابِ الشَّرْطِ:", "جب جواب جملہ اسمیہ یا طلبیہ ہو تو فاء لانا واجب ہے:", "The prefix 'Fa-' is mandatory when condition result is nominal or imperative:",
      "اسمية، طلبية، وبجامد، وبما، ولن، وبقد، وبالتنفيس", "Mandatory Fa- on nominal or imperative result clause",
      "fill_blank", "مَنْ غَشَّنَا [ ＿＿＿ ] لَيْسَ مِنَّا .", "خالی جگہ پُر کریں:", "Fill in the blank:",
      "فَـ", ["فَـ", "وَ", "ثُمَّ", "بَلْ"], "📜",
      "جامد فعل سے پہلے فاء واجب ہے: فَلَيْسَ مِنَّا", "Mandatory Fa-: fa-laysa minnaa.")

    # UNIT 16
    q(16, 1, "التَّمْرِينُ (1)", "مشق (1): باب تفعیل کا مصدر (تَفْعِيل)", "Exercise (1): Form II Verbal Noun (Taf'eel)",
      "صُغِ الْمَصْدَرَ مِنْ بَابِ (فَعَّلَ):", "عین کلمے کی تضعیف کے ساتھ مصدر تفْعِيل بنائیں:", "Form verbal noun Taf'eel on Form II:",
      "فَعَّلَ کا مصدر تَفْعِيل آتا ہے", "Fa''ala yields verbal noun Taf'eel",
      "fill_blank", "مَا مَصْدَرُ الْفِعْلِ (عَلَّمَ)؟", "صحیح مصدر منتخب کریں:", "Select the correct verbal noun:",
      "تَعْلِيمٌ", ["تَعْلِيمٌ", "عِلْمٌ", "مُعَلَّمٌ", "إِعْلَامٌ"], "🎓",
      "علّم کا مصدر باب تفعیل میں: تَعْلِيمٌ", "Verbal noun of 'allama is ta'leemun.")
    q(16, 2, "التَّمْرِينُ (2)", "مشق (2): اسم الفاعل من باب فعّل (مُفَعِّل)", "Exercise (2): Form II Active Participle (Mufa''il)",
      "صُغِ اسْمَ الْفَاعِلِ مِنْ (دَرَّسَ):", "مضارع کے شروع میں میم مضموم اور ماقبل آخر زیر:", "Form active participle with initial mu- and kasrah before end:",
      "باب تفعیل کا اسم فاعل مُفَعِّل کے وزن پر آتا ہے", "Form II active participle takes pattern Mufa''il",
      "fill_blank", "مَا اسْمُ الْفَاعِلِ مِنْ (دَرَّسَ)؟", "صحیح اسم فاعل منتخب کریں:", "Select the correct active participle:",
      "مُدَرِّسٌ", ["مُدَرِّسٌ", "دَارِسٌ", "مَدْرُوسٌ", "تَدْرِيسٌ"], "👨‍🏫",
      "درّس کا اسم فاعل: مُدَرِّسٌ (استاذ)", "Active participle is mudarrisun.")

    # UNIT 17
    q(17, 1, "التَّمْرِينُ (1)", "مشق (1): باب افعال کا مصدر (إِفْعَال)", "Exercise (1): Form IV Derived Verb (Af'ala / If'aal)",
      "صُغِ الْمَصْدَرَ مِنْ بَابِ (أَفْعَلَ):", "ہمزۂ قطع کے ساتھ مصدر إِفْعَال بنائیں:", "Form verbal noun on pattern If'aal:",
      "أَفْعَلَ کا مصدر إِفْعَال کے وزن پر آتا ہے", "Pattern Af'ala yields verbal noun If'aal",
      "fill_blank", "مَا مَصْدَرُ الْفِعْلِ (أَسْلَمَ)؟", "صحیح مصدر منتخب کریں:", "Select the correct verbal noun:",
      "إِسْلَامٌ", ["إِسْلَامٌ", "سَلَامٌ", "تَسْلِيمٌ", "مُسْلِمٌ"], "🌙",
      "أسلم کا مصدر: إِسْلَامٌ", "Verbal noun of aslama is Islaamun.")
    q(17, 2, "التَّمْرِينُ (2)", "مشق (2): اسم فاعل باب افعال سے (مُفْعِل)", "Exercise (2): Form IV Active Participle (Muf'il)",
      "صُغِ اسْمَ الْفَاعِلِ مِنْ (أَرْسَلَ):", "شروع میں میم مضموم اور ماقبل آخر زیر:", "Form active participle on pattern Muf'il:",
      "باب افعال کا اسم فاعل مُفْعِل کے وزن پر آتا ہے", "Pattern Af'ala yields active participle Muf'il",
      "fill_blank", "مَا اسْمُ الْفَاعِلِ مِنْ (أَرْسَلَ)؟", "صحیح اسم فاعل منتخب کریں:", "Select the correct active participle:",
      "مُرْسِلٌ", ["مُرْسِلٌ", "رَاسِلٌ", "مُرْسَلٌ", "إِرْسَالٌ"], "✉️",
      "أرسل کا اسم فاعل: مُرْسِلٌ", "Active participle of arsala is mursilun.")
    q(17, 3, "التَّمْرِينُ (3)", "مشق (3): أَخَوَاتُ كَانَ (أَصْبَحَ، أَمْسَى)", "Exercise (3): Sisters of Kaana (Asbaha, Amsaa)",
      "أَدْخِلْ (أَصْبَحَ) عَلَى الْجُمْلَةِ الاسْمِيَّةِ:", "أصبح کا عمل کان کی طرح خبر کو منصوب کرنا ہے:", "'Asbaha' acts like Kaana (raises subject, puts predicate in accusative):",
      "أصبح اور امسیٰ کان کی بہنیں ہیں جو خبر کو نصب دیتی ہیں", "Asbaha is a sister of Kaana and governs an accusative predicate",
      "fill_blank", "الْمَرِيضُ صَحِيحٌ ➔ أَصْبَحَ الْمَرِيضُ [ ＿＿＿ ] .", "صحیح اعراب منتخب کریں:", "Select the correct form:",
      "صَحِيحًا", ["صَحِيحًا", "صَحِيحٌ", "صَحِيحٍ", "صَحِيحْ"], "🏥",
      "أصبح کی خبر منصوب: صَحِيحًا", "Predicate of asbaha is mansoob: saheehan.")

    return questions

if __name__ == '__main__':
    qs = get_book3_questions()
    print(f"Generated {len(qs)} Book 3 questions across units.")
    unit_map = {}
    for q in qs:
        u = q['unit_num']
        t = q['tamreen_num']
        unit_map.setdefault(u, set()).add(t)
    print(f"Units covered: {len(unit_map)}")
    for u in sorted(unit_map.keys()):
        print(f"  Unit {u}: Tamreens {sorted(list(unit_map[u]))}")
