import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_b3_curriculum():
    units = {}

    # -------------------------------------------------------------
    # UNIT 1: الْمُعْرَبُ وَالْمَبْنِيُّ
    # -------------------------------------------------------------
    units[1] = [
        {
            "id": "b3_u1_q1", "book": 3, "unit_num": 1, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ متن (أجب عن الأسئلة)", "badge_en": "Exercise (1): Text Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ بِنَاءً عَلَى حِوَارِ الدَّرْسِ:",
            "tamreen_title_ur": "سبق کے مکالمے کی روشنی میں جواب دیں:",
            "tamreen_title_en": "Answer the comprehension questions based on the dialogue:",
            "grammar_goal_ur": "سوال کا فہم اور جملے کی درست تشکیل۔", "grammar_goal_en": "Comprehending interrogatives and forming accurate answers.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَا هُوَ الِاسْمُ الْمَبْنِيُّ؟ هُوَ الَّذِي [ ＿＿＿ ] آخِرُهُ .",
            "prompt_ur": "اسم مبنی کی تعریف مکمل کریں:",
            "prompt_en": "Complete the definition of Mabnee noun:",
            "answer": "لَا يَتَغَيَّرُ", "options": ["لَا يَتَغَيَّرُ", "يَتَغَيَّرُ", "يُرْفَعُ", "يُنْصَبُ"],
            "emoji": "🏛️", "hint_ur": "مبنی وہ اسم ہے جس کا آخر عامل بدلنے سے تبدیل نہ ہو۔", "hint_en": "A mabnee noun is one whose ending does not change.",
            "explanation_ur": "درست جواب: 'لَا يَتَغَيَّرُ' (مبنی کا آخر ہمیشہ ایک ہی حالت پر قائم رہتا ہے)",
            "explanation_en": "Correct: 'لَا يَتَغَيَّرُ' (A mabnee word has an unchangeable ending)"
        },
        {
            "id": "b3_u1_q2", "book": 3, "unit_num": 1, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): تمیزِ معرب از مبنی", "badge_en": "Exercise (3): Distinguishing Mu'rab from Mabnee",
            "tamreen_title_ar": "مَيِّزِ الِاسْمَ الْمُعْرَبَ مِنَ الِاسْمِ الْمَبْنِيِّ:",
            "tamreen_title_ur": "معرب اور مبنی اسم کے درمیان فرق پہچانیں:",
            "tamreen_title_en": "Distinguish between declinable (Mu'rab) and indeclinable (Mabnee):",
            "grammar_goal_ur": "ضمائر، اسمائے اشارہ اور موصولہ مبنی ہوتے ہیں، جبکہ اکثر اسماء معرب ہوتے ہیں۔", "grammar_goal_en": "Pronouns, demonstratives, and relatives are mabnee, whereas standard nouns are mu'rab.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَلِمَةُ (هٰذَا) فِي اللُّغَةِ الْعَرَبِيَّةِ هِيَ: [ ＿＿＿ ]",
            "prompt_ur": "(هٰذَا) اسم معرب ہے یا مبنی؟",
            "prompt_en": "Is 'هٰذَا' Mu'rab or Mabnee?",
            "answer": "اسْمٌ مَبْنِيٌّ", "options": ["اسْمٌ مَبْنِيٌّ", "اسْمٌ مُعْرَبٌ", "فِعْلٌ مَاضٍ", "حَرْفُ جَرٍّ"],
            "emoji": "👉", "hint_ur": "اسم اشارہ ہمیشہ مبنی ہوتا ہے۔", "hint_en": "Demonstrative pronouns are always mabnee.",
            "explanation_ur": "درست جواب: 'اسْمٌ مَبْنِيٌّ' (اسمائے اشارہ مبنیات میں سے ہیں)",
            "explanation_en": "Correct: 'اسْمٌ مَبْنِيٌّ' (Demonstratives are indeclinable)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 2: عَلَامَاتُ الْإِعْرَابِ الْأَصْلِيَّةُ وَالْفَرْعِيَّةُ
    # -------------------------------------------------------------
    units[2] = [
        {
            "id": "b3_u2_q1", "book": 3, "unit_num": 2, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): علاماتِ اعراب اصلیہ (حرکات)", "badge_en": "Exercise (2): Primary Inflection Markers",
            "tamreen_title_ar": "حَدِّدْ عَلَامَاتِ الْإِعْرَابِ الْأَصْلِيَّةَ:",
            "tamreen_title_ur": "اعراب کی اصلی علامات (ضمہ، فتحہ، کسرہ) پہچانیں:",
            "tamreen_title_en": "Identify primary inflection marks (vowels):",
            "grammar_goal_ur": "اصلی اعراب حرکات (ضمہ للرفع، فتحہ للنصب، کسرہ للجر) سے ہوتا ہے۔", "grammar_goal_en": "Primary case markers are short vowels: dammah, fathah, kasrah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عَلَامَةُ الرَّفْعِ الْأَصْلِيَّةُ فِي الِاسْمِ الْمُفْرَدِ هِيَ: [ ＿＿＿ ]",
            "prompt_ur": "مفرد اسم میں رفع کی اصلی علامت کیا ہے؟",
            "prompt_en": "What is the primary marker of nominative case in a singular noun?",
            "answer": "الضَّمَّةُ", "options": ["الضَّمَّةُ", "الْفَتْحَةُ", "الْكَسْرَةُ", "الْوَاوُ"],
            "emoji": "🎯", "hint_ur": "رفع کی اصل علامت پیش (ضمہ) ہے۔", "hint_en": "The primary nominative marker is dammah.",
            "explanation_ur": "درست جواب: 'الضَّمَّةُ' (مفرد اسم میں رفع ضمہ سے آتا ہے)",
            "explanation_en": "Correct: 'الضَّمَّةُ' (Dammah is the primary marker for raf')"
        },
        {
            "id": "b3_u2_q2", "book": 3, "unit_num": 2, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): علاماتِ اعراب فرعیہ (حروف)", "badge_en": "Exercise (4): Secondary Inflection Markers",
            "tamreen_title_ar": "عَيِّنِ الْعَلَامَةَ الْفَرْعِيَّةَ فِي جَمْعِ الْمُذَكَّرِ السَّالِمِ:",
            "tamreen_title_ur": "جمع مذکر سالم میں فرعی علامتِ رفع پہچانیں:",
            "tamreen_title_en": "Identify the secondary nominative marker in sound masculine plural:",
            "grammar_goal_ur": "جمع مذکر سالم میں رفع کی فرعی علامت 'الواو' ہے۔", "grammar_goal_en": "Secondary nominative marker in sound masculine plural is waw.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عَلَامَةُ الرَّفْعِ فِي (الْمُسْلِمُونَ) هِيَ: [ ＿＿＿ ]",
            "prompt_ur": "الْمُسْلِمُونَ میں علامتِ رفع کیا ہے؟",
            "prompt_en": "What is the marker of raf' in 'الْمُسْلِمُونَ'?",
            "answer": "الْوَاوُ نِيَابَةً عَنِ الضَّمَّةِ", "options": ["الْوَاوُ نِيَابَةً عَنِ الضَّمَّةِ", "الضَّمَّةُ", "النُّونُ", "الْفَتْحَةُ"],
            "emoji": "🕌", "hint_ur": "یہاں واؤ پیش کا نائب ہے۔", "hint_en": "Waw acts as the substitute for dammah.",
            "explanation_ur": "درست جواب: 'الْوَاوُ نِيَابَةً عَنِ الضَّمَّةِ' (جمع مذکر سالم میں رفع کی علامت واؤ ہے)",
            "explanation_en": "Correct: 'الْوَاوُ نِيَابَةً عَنِ الضَّمَّةِ' (Waw replaces dammah in sound plural)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 3: حَالُ الْجُمْلَةِ وَوَاوُ الْحَالِ
    # -------------------------------------------------------------
    units[3] = [
        {
            "id": "b3_u3_q1", "book": 3, "unit_num": 3, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): واوِ حال کے ساتھ جملہ اسمیہ", "badge_en": "Exercise (2): Nominal Hal Clause with Waaw al-Haal",
            "tamreen_title_ar": "أَدْخِلْ (وَاوَ الْحَالِ) مَعَ الْجُمْلَةِ الِاسْمِيَّةِ:",
            "tamreen_title_ur": "حالت بیان کرنے کے لیے 'واوِ حال' داخل کریں:",
            "tamreen_title_en": "Use Waaw al-Haal to introduce nominal circumstantial clause:",
            "grammar_goal_ur": "جب حال جملہ اسمیہ ہو تو اس کے شروع میں واوِ حال اور ضمیر آتی ہے (وَهُوَ يَبْتَسِمُ)۔", "grammar_goal_en": "Nominal circumstantial clause requires Waaw al-Haal and pronoun.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "دَخَلَ الْمُدَرِّسُ الْفَصْلَ [ ＿＿＿ ] .",
            "prompt_ur": "استاد کے مسکراتے ہوئے داخل ہونے کی حالت کے لیے درست جملہ منتخب کریں:",
            "prompt_en": "Select the correct Hal clause for 'while smiling':",
            "answer": "وَهُوَ يَبْتَسِمُ", "options": ["وَهُوَ يَبْتَسِمُ", "يَبْتَسِمُ هُوَ", "وَهُوَ مُبْتَسِمٌ", "وَابْتَسَمَ"],
            "emoji": "😊", "hint_ur": "استاد مسکراتے ہوئے کلاس میں داخل ہوئے۔", "hint_en": "The teacher entered the classroom while smiling.",
            "explanation_ur": "درست جواب: 'وَهُوَ يَبْتَسِمُ' (واوِ حال کے بعد جملہ اسمیہ حال بن کر آتا ہے)",
            "explanation_en": "Correct: 'وَهُوَ يَبْتَسِمُ' (Circumstantial state introduced by waaw al-haal)"
        },
        {
            "id": "b3_u3_q2", "book": 3, "unit_num": 3, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): حال مفرد منصوب", "badge_en": "Exercise (4): Singular Accusative Hal",
            "tamreen_title_ar": "اضْبِطِ الْحَالَ الْمُفْرَدَ فِي الْجُمْلَةِ:",
            "tamreen_title_ur": "مفرد حال پر درست اعراب (نصب) لگائیں:",
            "tamreen_title_en": "Apply accusative case to singular Hal:",
            "grammar_goal_ur": "مفرد حال ہمیشہ نکرہ اور منصوب ہوتا ہے (رَاكِباً)۔", "grammar_goal_en": "Singular Hal is always indefinite and accusative (mansoob).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "رَجَعَ أَبِي مِنَ السَّفَرِ [ ＿＿＿ ] .",
            "prompt_ur": "والد کے خوشی سے لوٹنے کی حالت کے لیے درست لفظ منتخب کریں:",
            "prompt_en": "Select the correct accusative Hal for 'happy':",
            "answer": "مَسْرُوراً", "options": ["مَسْرُوراً", "مَسْرُورٌ", "مَسْرُورٍ", "الْمَسْرُورَ"],
            "emoji": "😃", "hint_ur": "میرے والد سفر سے خوشی خوشی لوٹے۔", "hint_en": "My father returned from travel happily.",
            "explanation_ur": "درست جواب: 'مَسْرُوراً' (حال ہمیشہ منصوب ہوتا ہے)",
            "explanation_en": "Correct: 'مَسْرُوراً' (Hal takes accusative tanween)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 4: الْفِعْلُ الْمَبْنِيُّ لِلْمَجْهُولِ وَنَائِبُ الْفَاعِلِ
    # -------------------------------------------------------------
    units[4] = [
        {
            "id": "b3_u4_q1", "book": 3, "unit_num": 4, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): صیاغتِ مجہول فی الماضی (فُعِلَ)", "badge_en": "Exercise (2): Passive Voice in Past Tense (Fu'ila)",
            "tamreen_title_ar": "حَوِّلِ الْفِعْلَ الْمَاضِيَ إِلَى الْمَبْنِيِّ لِلْمَجْهُولِ:",
            "tamreen_title_ur": "فعل ماضی معروف کو مجہول میں تبدیل کریں:",
            "tamreen_title_en": "Convert active past verb to passive voice:",
            "grammar_goal_ur": "ماضی مجہول میں پہلے حرف پر پیش اور آخری سے پہلے زیر دی جاتی ہے (كَتَبَ -> كُتِبَ)۔", "grammar_goal_en": "Past passive is formed by dammah on first letter and kasrah on penultimate letter.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَتَبَ التِّلْمِيذُ الدَّرْسَ ➔ [ ＿＿＿ ] الدَّرْسُ .",
            "prompt_ur": "كَتَبَ کا مجہول منتخب کریں:",
            "prompt_en": "Select the passive form of 'كَتَبَ':",
            "answer": "كُتِبَ", "options": ["كُتِبَ", "كَتَبَ", "يُكْتَبُ", "كُتِبَتْ"],
            "emoji": "✍️", "hint_ur": "سبق لکھا گیا۔", "hint_en": "The lesson was written.",
            "explanation_ur": "درست جواب: 'كُتِبَ' (ماضی مجہول فُعِلَ کے وزن پر آتا ہے)",
            "explanation_en": "Correct: 'كُتِبَ' (Formed on pattern Fu'ila)"
        },
        {
            "id": "b3_u4_q2", "book": 3, "unit_num": 4, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): نائب الفاعل کا مرفوع ہونا", "badge_en": "Exercise (3): Nominative Case of Naa'ib al-Faa'il",
            "tamreen_title_ar": "اضْبِطْ نَائِبَ الْفَاعِلِ فِي الْجُمْلَةِ:",
            "tamreen_title_ur": "نائب الفاعل پر درست اعراب (پیش) لگائیں:",
            "tamreen_title_en": "Apply nominative case to Naa'ib al-Faa'il:",
            "grammar_goal_ur": "فعل مجہول کے بعد مفعول بہ نائب فاعل بن کر مرفوع (پیش والا) ہو جاتا ہے۔", "grammar_goal_en": "Direct object becomes nominative Naa'ib al-Faa'il after passive verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "فُتِحَ [ ＿＿＿ ] فِي الصَّبَاحِ .",
            "prompt_ur": "فُتِحَ کے بعد درست نائب فاعل منتخب کریں:",
            "prompt_en": "Select the correct nominative Naa'ib al-Faa'il after 'فُتِحَ':",
            "answer": "الْبَابُ", "options": ["الْبَابُ", "الْبَابَ", "الْبَابِ", "بَاباً"],
            "emoji": "🚪", "hint_ur": "صبح کے وقت دروازہ کھولا گیا۔", "hint_en": "The door was opened in the morning.",
            "explanation_ur": "درست جواب: 'الْبَابُ' (نائب فاعل ہمیشہ مرفوع ہوتا ہے)",
            "explanation_en": "Correct: 'الْبَابُ' (Naa'ib al-Faa'il takes nominative dammah)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 5: اسْمُ الْفَاعِلِ (صَوْغُهُ مِنَ الثُّلَاثِيِّ وَغَيْرِ الثُّلَاثِيِّ)
    # -------------------------------------------------------------
    units[5] = [
        {
            "id": "b3_u5_q1", "book": 3, "unit_num": 5, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): صیاغتِ اسم فاعل از ثلاثی مجرد (فَاعِل)", "badge_en": "Exercise (2): Active Participle from Trilateral Verb (Faa'il)",
            "tamreen_title_ar": "صُغِ اسْمَ الْفَاعِلِ عَلَى وَزْنِ (فَاعِل):",
            "tamreen_title_ur": "ثلاثی مجرد (كَتَبَ) سے اسمِ فاعل بنائیں:",
            "tamreen_title_en": "Form active participle on pattern Faa'il from 'كَتَبَ':",
            "grammar_goal_ur": "ثلاثی مجرد سے اسمِ فاعل 'فَاعِلٌ' کے وزن پر بنتا ہے (كَاتِبٌ)۔", "grammar_goal_en": "Active participle of Form I is formed on pattern Faa'il.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَنْ كَتَبَ هٰذِهِ الرِّسَالَةَ هُوَ [ ＿＿＿ ] لَهَا .",
            "prompt_ur": "كَتَبَ کا اسم فاعل منتخب کریں:",
            "prompt_en": "Select the active participle of 'كَتَبَ':",
            "answer": "كَاتِبٌ", "options": ["كَاتِبٌ", "مَكْتُوبٌ", "كِتَابٌ", "مَكْتَبٌ"],
            "emoji": "✍️", "hint_ur": "جس نے یہ خط لکھا وہ اس کا لکھنے والا (کاتب) ہے۔", "hint_en": "He who wrote this letter is its writer (Kaatib).",
            "explanation_ur": "درست جواب: 'كَاتِبٌ' (كَتَبَ سے اسم فاعل كَاتِبٌ بنتا ہے)",
            "explanation_en": "Correct: 'كَاتِبٌ' (Form I active participle is Kaatib)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 6: اسْمُ الْمَفْعُولِ (صَوْغُهُ عَلَى وَزْنِ مَفْعُول)
    # -------------------------------------------------------------
    units[6] = [
        {
            "id": "b3_u6_q1", "book": 3, "unit_num": 6, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): صیاغتِ اسم مفعول از ثلاثی مجرد (مَفْعُول)", "badge_en": "Exercise (2): Passive Participle on Pattern Maf'ool",
            "tamreen_title_ar": "صُغِ اسْمَ الْمَفْعُولِ عَلَى وَزْنِ (مَفْعُول):",
            "tamreen_title_ur": "ثلاثی مجرد (فَتَحَ) سے اسمِ مفعول بنائیں:",
            "tamreen_title_en": "Form passive participle on pattern Maf'ool from 'فَتَحَ':",
            "grammar_goal_ur": "ثلاثی مجرد سے اسمِ مفعول 'مَفْعُولٌ' کے وزن پر بنتا ہے (مَفْتُوحٌ)۔", "grammar_goal_en": "Passive participle of Form I is formed on pattern Maf'ool.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْبَابُ الَّذِي فُتِحَ هُوَ [ ＿＿＿ ] .",
            "prompt_ur": "فَتَحَ کا اسم مفعول منتخب کریں:",
            "prompt_en": "Select the passive participle of 'فَتَحَ':",
            "answer": "مَفْتُوحٌ", "options": ["مَفْتُوحٌ", "فَاتِحٌ", "مِفْتَاحٌ", "فَتْحٌ"],
            "emoji": "🚪", "hint_ur": "جو دروازہ کھولا گیا وہ کھلا ہوا (مفتوح) ہے۔", "hint_en": "The door that was opened is open (Maftooh).",
            "explanation_ur": "درست جواب: 'مَفْتُوحٌ' (فَتَحَ سے اسم مفعول مَفْتُوحٌ بنتا ہے)",
            "explanation_en": "Correct: 'مَفْتُوحٌ' (Form I passive participle is Maftooh)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 7: اسْمُ الزَّمَانِ وَاسْمُ الْمَكَانِ (مَفْعَل / مَفْعِل)
    # -------------------------------------------------------------
    units[7] = [
        {
            "id": "b3_u7_q1", "book": 3, "unit_num": 7, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): صیاغتِ اسم مکان بر وزن (مَفْعَل)", "badge_en": "Exercise (2): Noun of Place on Pattern Maf'al",
            "tamreen_title_ar": "صُغِ اسْمَ الْمَكَانِ عَلَى وَزْنِ (مَفْعَل):",
            "tamreen_title_ur": "لَعِبَ سے کھیلنے کی جگہ (اسمِ مکان) بنائیں:",
            "tamreen_title_en": "Form noun of place from 'لَعِبَ' on pattern Maf'al:",
            "grammar_goal_ur": "کھیلنے کی جگہ کے لیے وزن 'مَفْعَلٌ' آتا ہے (مَلْعَبٌ)۔", "grammar_goal_en": "Noun of place is formed on pattern Maf'al (Mal'ab).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَكَانُ لَعِبِ الطُّلَّابِ يُسَمَّى: [ ＿＿＿ ]",
            "prompt_ur": "کھیل کے میدان کے لیے درست اسمِ مکان منتخب کریں:",
            "prompt_en": "Select the correct noun of place for 'playground':",
            "answer": "مَلْعَبٌ", "options": ["مَلْعَبٌ", "لَاعِبٌ", "مَلْعُوبٌ", "لِعْبَةٌ"],
            "emoji": "🏟️", "hint_ur": "طلبہ کے کھیلنے کی جگہ کو ملعب (کھیل کا میدان) کہتے ہیں۔", "hint_en": "The place where students play is called a Mal'ab.",
            "explanation_ur": "درست جواب: 'مَلْعَبٌ' (لَعِبَ سے اسم مکان مَلْعَبٌ بنتا ہے)",
            "explanation_en": "Correct: 'مَلْعَبٌ' (Pattern Maf'al for place of action)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 8: اسْمُ الْآلَةِ (مِفْعَال، مِفْعَل، مِفْعَلَة)
    # -------------------------------------------------------------
    units[8] = [
        {
            "id": "b3_u8_q1", "book": 3, "unit_num": 8, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): صیاغتِ اسم آلہ بر وزن (مِفْعَال)", "badge_en": "Exercise (2): Noun of Instrument on Pattern Mif'aal",
            "tamreen_title_ar": "صُغِ اسْمَ الْآلَةِ عَلَى وَزْنِ (مِفْعَال):",
            "tamreen_title_ur": "فَتَحَ سے کھولنے کے آلے کا نام (اسمِ آلہ) بنائیں:",
            "tamreen_title_en": "Form noun of instrument from 'فَتَحَ' on pattern Mif'aal:",
            "grammar_goal_ur": "کھولنے کے آلے کو 'مِفْعَالٌ' کے وزن پر 'مِفْتَاحٌ' کہتے ہیں۔", "grammar_goal_en": "Noun of instrument is formed on pattern Mif'aal (Miftaah).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْآلَةُ الَّتِي نَفْتَحُ بِهَا الْبَابَ هِيَ: [ ＿＿＿ ]",
            "prompt_ur": "دروازہ کھولنے کے آلے (چابی) کے لیے درست کلمہ منتخب کریں:",
            "prompt_en": "Select the noun of instrument for 'key':",
            "answer": "مِفْتَاحٌ", "options": ["مِفْتَاحٌ", "فَاتِحٌ", "مَفْتُوحٌ", "فَتْحٌ"],
            "emoji": "🔑", "hint_ur": "وہ آلہ جس سے ہم دروازہ کھولتے ہیں وہ چابی (مفتاح) ہے۔", "hint_en": "The instrument with which we open the door is a key (Miftaah).",
            "explanation_ur": "درست جواب: 'مِفْتَاحٌ' (اسم آلہ مِفْعَال کے وزن پر مِفْتَاحٌ آتا ہے)",
            "explanation_en": "Correct: 'مِفْتَاحٌ' (Noun of instrument on pattern Mif'aal)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 9: أَقْسَامُ الْمَعَارِفِ السَّبْعَةُ
    # -------------------------------------------------------------
    units[9] = [
        {
            "id": "b3_u9_q1", "book": 3, "unit_num": 9, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): اقسامِ معرفہ کی پہچان", "badge_en": "Exercise (2): Identifying Categories of Definite Nouns",
            "tamreen_title_ar": "حَدِّدْ نَوْعَ الْمَعْرِفَةِ فِي الْكَلِمَةِ الْمُعَيَّنَةِ:",
            "tamreen_title_ur": "لفظ میں معرفہ کی قسم (علم، ضمیر، اسم اشارہ وغیرہ) پہچانیں:",
            "tamreen_title_en": "Identify the type of definite noun:",
            "grammar_goal_ur": "معارف کی سات اقسام ہیں جن میں سب سے زیادہ معرفہ ضمیر اور علم ہیں۔", "grammar_goal_en": "There are seven categories of definite nouns including proper nouns and pronouns.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَلِمَةُ (مَكَّةُ) فِي اللُّغَةِ هِيَ: [ ＿＿＿ ]",
            "prompt_ur": "(مَكَّةُ) معرفہ کی کون سی قسم ہے؟",
            "prompt_en": "What type of definite noun is 'مَكَّةُ'?",
            "answer": "عَلَمٌ", "options": ["عَلَمٌ", "ضَمِيرٌ", "اسْمُ إِشَارَةٍ", "اسْمٌ مَوْصُولٌ"],
            "emoji": "🕋", "hint_ur": "یہ ایک مخصوص شہر کا نام (علم) ہے۔", "hint_en": "This is a proper noun (name of a specific city).",
            "explanation_ur": "درست جواب: 'عَلَمٌ' (شہر یا شخص کے نام کو علم کہتے ہیں)",
            "explanation_en": "Correct: 'عَلَمٌ' (Proper noun / name of a place)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 10: الْجُمْلَةُ الِاسْمِيَّةُ وَالْجُمْلَةُ الْفِعْلِيَّةُ
    # -------------------------------------------------------------
    units[10] = [
        {
            "id": "b3_u10_q1", "book": 3, "unit_num": 10, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): تمیزِ جملہ اسمیہ از جملہ فعلیہ", "badge_en": "Exercise (2): Distinguishing Nominal from Verbal Sentences",
            "tamreen_title_ar": "مَيِّزِ الْجُمْلَةَ الِاسْمِيَّةَ مِنَ الْجُمْلَةِ الْفِعْلِيَّةِ:",
            "tamreen_title_ur": "جملہ اسمیہ اور فعلیہ کے درمیان تمیز کریں:",
            "tamreen_title_en": "Distinguish between nominal and verbal sentences based on initial element:",
            "grammar_goal_ur": "جس جملے کے شروع میں اسم ہو وہ جملہ اسمیہ ہے اور جس کے شروع میں فعل ہو وہ جملہ فعلیہ ہے۔", "grammar_goal_en": "A nominal sentence begins with a noun; a verbal sentence begins with a verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "جُمْلَةُ (قَرَأَ الطَّالِبُ الْكِتَابَ) هِيَ: [ ＿＿＿ ]",
            "prompt_ur": "اس جملے کی قسم بتائیں:",
            "prompt_en": "Identify the sentence type:",
            "answer": "جُمْلَةٌ فِعْلِيَّةٌ", "options": ["جُمْلَةٌ فِعْلِيَّةٌ", "جُمْلَةٌ اسْمِيَّةٌ", "شِبْهُ جُمْلَةٍ", "جُمْلَةٌ شَرْطِيَّةٌ"],
            "emoji": "📖", "hint_ur": "یہ جملہ فعل (قَرَأَ) سے شروع ہو رہا ہے۔", "hint_en": "This sentence begins with a verb (Qara'a).",
            "explanation_ur": "درست جواب: 'جُمْلَةٌ فِعْلِيَّةٌ' (کیونکہ اس کا صدر فعل ہے)",
            "explanation_en": "Correct: 'جُمْلَةٌ فِعْلِيَّةٌ' (Begins with a finite verb)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 11: أَنْوَاعُ الْخَبَرِ (مُفْرَد، جُمْلَة، شِبْهُ جُمْلَة)
    # -------------------------------------------------------------
    units[11] = [
        {
            "id": "b3_u11_q1", "book": 3, "unit_num": 11, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): خبر کا جملہ اسمیہ ہونا", "badge_en": "Exercise (6): Predicate as a Nominal Clause",
            "tamreen_title_ar": "اجْعَلِ الْخَبَرَ جُمْلَةً اسْمِيَّةً مُشْتَمِلَةً عَلَى ضَمِيرٍ:",
            "tamreen_title_ur": "خبر کو ایسا جملہ اسمیہ بنائیں جس میں مبتدا کی طرف لوٹنے والی ضمیر ہو:",
            "tamreen_title_en": "Form a nominal clause predicate with a returning pronoun:",
            "grammar_goal_ur": "جب خبر جملہ اسمیہ ہو تو اس میں مبتدا کی طرف لوٹنے والی ضمیر (رابط) ہونی چاہیے۔", "grammar_goal_en": "A nominal clause predicate requires a pronoun referencing the subject.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "حَامِدٌ [ ＿＿＿ ] طَبِيبٌ .",
            "prompt_ur": "حامد کے لیے جملہ اسمیہ خبر مکمل کریں:",
            "prompt_en": "Complete the nominal predicate clause for Hamid:",
            "answer": "أَبُوهُ", "options": ["أَبُوهُ", "أَبُوهَا", "أَبُوهُمْ", "أَبُوكَ"],
            "emoji": "👨‍⚕️", "hint_ur": "حامد، اس کے والد ڈاکٹر ہیں۔", "hint_en": "Hamid, his father is a doctor.",
            "explanation_ur": "درست جواب: 'أَبُوهُ' (حامد چونکہ مذکر ہے اس لیے ضمیر ـهُ آئے گی)",
            "explanation_en": "Correct: 'أَبُوهُ' (Masculine pronoun returning to Hamid)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 12: ظُرُوفُ الزَّمَانِ وَالْمَكَانِ (الْمَفْعُولُ فِيهِ)
    # -------------------------------------------------------------
    units[12] = [
        {
            "id": "b3_u12_q1", "book": 3, "unit_num": 12, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): مفعول فیہ (ظرف) کا منصوب ہونا", "badge_en": "Exercise (3): Accusative Case of Adverb of Time/Place",
            "tamreen_title_ar": "اضْبِطْ ظَرْفَ الزَّمَانِ أَوِ الْمَكَانِ بِالْفَتْحَةِ:",
            "tamreen_title_ur": "ظرفِ زمان یا مکان پر درست اعراب (نصب) لگائیں:",
            "tamreen_title_en": "Vowel the adverb of time/place in accusative case:",
            "grammar_goal_ur": "مفعول فیہ (ظرف) ہمیشہ منصوب (زبر والا) ہوتا ہے (صَبَاحاً، أَمَامَ)۔", "grammar_goal_en": "Adverbs of time and place are mansoob with fathah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "سَافَرْتُ إِلَى الْمَدِينَةِ الْمُنَوَّرَةِ [ ＿＿＿ ] .",
            "prompt_ur": "وقت بتانے کے لیے درست ظرفِ زمان منتخب کریں:",
            "prompt_en": "Select the correct accusative adverb of time for 'morning':",
            "answer": "صَبَاحاً", "options": ["صَبَاحاً", "صَبَاحٌ", "صَبَاحٍ", "الْصَبَاحِ"],
            "emoji": "🌅", "hint_ur": "میں نے صبح کے وقت مدینہ منورہ کا سفر کیا۔", "hint_en": "I traveled to Madinah in the morning.",
            "explanation_ur": "درست جواب: 'صَبَاحاً' (ظرف زمان منصوب ہوتا ہے)",
            "explanation_en": "Correct: 'صَبَاحاً' (Adverb of time takes accusative tanween)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 13: لَامُ الْأَمْرِ وَالْجَزْمُ فِي جَوَابِ الطَّلَبِ
    # -------------------------------------------------------------
    units[13] = [
        {
            "id": "b3_u13_q1", "book": 3, "unit_num": 13, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): لامِ امر کا جزم (لِيَكْتُبْ)", "badge_en": "Exercise (6): Jussive with Laam of Command (Li-)",
            "tamreen_title_ar": "أَدْخِلْ (لَامَ الْأَمْرِ) عَلَى الْفِعْلِ الْمُضَارِعِ:",
            "tamreen_title_ur": "غائب پر حکم دینے کے لیے 'لامِ امر' داخل کر کے جزم دیں:",
            "tamreen_title_en": "Enter Laam al-Amr and apply jussive sukoon:",
            "grammar_goal_ur": "لامِ امر مکسورہ (لِـ) مضارع کو جزم دیتی ہے (لِيَخْرُجْ)۔", "grammar_goal_en": "Laam al-amr commands third person and apocopates present verb.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "[ ＿＿＿ ] كُلُّ طَالِبٍ دَفْتَرَهُ الْآنَ ! ",
            "prompt_ur": "ہر طالب علم کو کاپی کھولنے کا حکم دینے کے لیے درست صیغہ منتخب کریں:",
            "prompt_en": "Select the correct verb with Laam al-Amr for 'let him open':",
            "answer": "لِيَفْتَحْ", "options": ["لِيَفْتَحْ", "لِيَفْتَحُ", "لِيَفْتَحَ", "فَتَحَ"],
            "emoji": "📖", "hint_ur": "ہر طالب علم اب اپنی کاپی کھولے!", "hint_en": "Let every student open his notebook now!",
            "explanation_ur": "درست جواب: 'لِيَفْتَحْ' (لامِ امر کے بعد فعل مجزوم ہوتا ہے)",
            "explanation_en": "Correct: 'لِيَفْتَحْ' (Takes jussive sukoon after laam al-amr)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 14: أَدَوَاتُ الشَّرْطِ غَيْرُ الْجَازِمَةِ (إِذَا، لَوْ، لَوْلَا)
    # -------------------------------------------------------------
    units[14] = [
        {
            "id": "b3_u14_q1", "book": 3, "unit_num": 14, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): اقتران جواب 'إِذَا' بالفاء", "badge_en": "Exercise (3): Connecting Result of 'Idhaa' with Faa",
            "tamreen_title_ar": "صِلْ جَوَابَ الشَّرْطِ بِالْفَاءِ عِنْدَمَا يَكُونُ جُمْلَةً طَلَبِيَّةً:",
            "tamreen_title_ur": "جب جوابِ شرط جملہ طلبیہ ہو تو فاء جوڑیں:",
            "tamreen_title_en": "Prefix 'Faa' to the conditional result when it is an imperative:",
            "grammar_goal_ur": "اگر شرط کا جواب امر یا نہی ہو تو اس پر 'فَـ' لانا واجب ہے (فَأَكْرِمْهُ)۔", "grammar_goal_en": "When result of condition is an imperative, faa is mandatory.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "إِذَا جَاءَكَ الضَّيْفُ [ ＿＿＿ ] ! ",
            "prompt_ur": "مہمان کی عزت کرنے کے جوابِ شرط کے لیے درست صیغہ منتخب کریں:",
            "prompt_en": "Select the correct result clause for 'honor him':",
            "answer": "فَأَكْرِمْهُ", "options": ["فَأَكْرِمْهُ", "أَكْرِمْهُ", "يُكْرِمُهُ", "فَأَكْرَمَهُ"],
            "emoji": "🤝", "hint_ur": "جب تمہارے پاس مہمان آئے تو اس کی عزت کرو!", "hint_en": "When a guest comes to you, honor him!",
            "explanation_ur": "درست جواب: 'فَأَكْرِمْهُ' (امر جوابِ شرط بنے تو فاء لانا ضروری ہے)",
            "explanation_en": "Correct: 'فَأَكْرِمْهُ' (Faa is obligatory before imperative in conditional result)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 15: أَدَوَاتُ الشَّرْطِ الْجَازِمَةُ (إِنْ، مَنْ، مَا، مَتَى)
    # -------------------------------------------------------------
    units[15] = [
        {
            "id": "b3_u15_q1", "book": 3, "unit_num": 15, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): جزمِ فعلین (فعلِ شرط و جوابِ شرط)", "badge_en": "Exercise (2): Apocopating Both Condition and Result Verbs",
            "tamreen_title_ar": "اجْزِمْ فِعْلَيِ الشَّرْطِ وَالْجَوَابِ بِـ (مَنْ):",
            "tamreen_title_ur": "اداتِ شرط 'مَنْ' سے فعل شرط اور جواب دونوں کو جزم دیں:",
            "tamreen_title_en": "Apply jussive to both condition and result verbs with 'Man':",
            "grammar_goal_ur": "اداتِ شرط جازمہ دو فعلوں کو جزم دیتی ہے: فعلِ شرط اور جوابِ شرط (مَنْ يَجْتَهِدْ يَنْجَحْ)۔", "grammar_goal_en": "Conditional particle 'Man' apocopates both conditional and consequence verbs.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مَنْ يَجْتَهِدْ [ ＿＿＿ ] فِي الِامْتِحَانِ .",
            "prompt_ur": "جوابِ شرط (کامیاب ہونا) کے لیے درست مجزوم فعل منتخب کریں:",
            "prompt_en": "Select the correct jussive consequence verb for 'he will succeed':",
            "answer": "يَنْجَحْ", "options": ["يَنْجَحْ", "يَنْجَحُ", "يَنْجَحَ", "نَجَحَ"],
            "emoji": "🎓", "hint_ur": "جو محنت کرے گا وہ امتحان میں کامیاب ہو جائے گا۔", "hint_en": "Whoever works hard will succeed in the exam.",
            "explanation_ur": "درست جواب: 'يَنْجَحْ' (جوابِ شرط ہونے کی وجہ سے جزم آئے گی)",
            "explanation_en": "Correct: 'يَنْجَحْ' (Takes jussive sukoon as result of condition)"
        },
        {
            "id": "b3_u15_q2", "book": 3, "unit_num": 15, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): الفرق بين كم الاستفهامية وكم الخبرية", "badge_en": "Exercise (6): Interrogative Kam vs Exclamatory Kam",
            "tamreen_title_ar": "حَوِّلْ (كَمْ) الِاسْتِفْهَامِيَّةَ إِلَى (كَمْ) الْخَبَرِيَّةِ:",
            "tamreen_title_ur": "کم استفہامیہ کو کم خبریہ میں بدلیں:",
            "tamreen_title_en": "Convert interrogative Kam (accusative) to exclamatory Kam (genitive):",
            "grammar_goal_ur": "کم استفہامیہ کا تمیز مفرد منصوب ہوتا ہے جبکہ کم خبریہ کا تمیز مجرور ہوتا ہے۔", "grammar_goal_en": "Interrogative Kam takes singular accusative; exclamatory Kam takes genitive.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "كَمْ طَالِباً غَابَ الْيَوْمَ؟ ➔ كَمْ [ ＿＿＿ ] غَابَ ! ",
            "prompt_ur": "کم خبریہ (بہت سارے طالب علم غیر حاضر ہوئے!) کے لیے درست تمیز منتخب کریں:",
            "prompt_en": "Select the correct genitive noun for exclamatory Kam:",
            "answer": "طَالِبٍ", "options": ["طَالِبٍ", "طَالِباً", "طَالِبٌ", "طُلَّاباً"],
            "emoji": "👨‍🎓", "hint_ur": "کتنے ہی طالب علم غیر حاضر ہوئے!", "hint_en": "How many a student was absent!",
            "explanation_ur": "درست جواب: 'طَالِبٍ' (کم خبریہ کا تمیز مجرور ہوتا ہے)",
            "explanation_en": "Correct: 'طَالِبٍ' (Tamyeez of exclamatory Kam is majroor)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 16: مَزِيدُ الثُّلَاثِيِّ: بَابُ (فَعَّلَ يُفَعِّلُ تَفْعِيلاً)
    # -------------------------------------------------------------
    units[16] = [
        {
            "id": "b3_u16_q1", "book": 3, "unit_num": 16, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): تصریفِ باب تفعیل (فَعَّلَ يُفَعِّلُ)", "badge_en": "Exercise (6): Conjugation of Form II (Fa''ala)",
            "tamreen_title_ar": "صُغِ الْمُضَارِعَ مِنْ بَابِ (فَعَّلَ) بِتَشْدِيدِ الْعَيْنِ:",
            "tamreen_title_ur": "باب تفعیل (عَلَّمَ) سے مضارع بنائیں:",
            "tamreen_title_en": "Form present tense from Form II verb 'عَلَّمَ':",
            "grammar_goal_ur": "باب تفعیل کا مضارع 'يُفَعِّلُ' کے وزن پر آتا ہے (عَلَّمَ -> يُعَلِّمُ)۔", "grammar_goal_en": "Present tense of Form II is YuFa''ilu with shaddah on middle radical.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عَلَّمَ الْأُسْتَاذُ ➔ الْأُسْتَاذُ [ ＿＿＿ ] النَّحْوَ .",
            "prompt_ur": "عَلَّمَ کا درست مضارع منتخب کریں:",
            "prompt_en": "Select the correct present tense of 'عَلَّمَ':",
            "answer": "يُعَلِّمُ", "options": ["يُعَلِّمُ", "يَعْلَمُ", "يُعَلَّمُ", "عَلَّمَ"],
            "emoji": "👨‍🏫", "hint_ur": "استاد نحو سکھاتے ہیں۔", "hint_en": "The professor teaches grammar.",
            "explanation_ur": "درست جواب: 'يُعَلِّمُ' (باب تفعیل کا مضارع يُفَعِّلُ کے وزن پر ہوتا ہے)",
            "explanation_en": "Correct: 'يُعَلِّمُ' (Form II present tense is Yu'allimu)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 17: مَزِيدُ الثُّلَاثِيِّ: بَابُ (أَفْعَلَ يُفْعِلُ إِفْعَالاً)
    # -------------------------------------------------------------
    units[17] = [
        {
            "id": "b3_u17_q1", "book": 3, "unit_num": 17, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): صیاغتِ مصدر از باب إفعال (إِفْعَال)", "badge_en": "Exercise (2): Verbal Noun of Form IV (If'aal)",
            "tamreen_title_ar": "صُغِ الْمَصْدَرَ مِنْ بَابِ (أَفْعَلَ):",
            "tamreen_title_ur": "أَرْسَلَ سے مصدر (إِفْعَال کے وزن پر) بنائیں:",
            "tamreen_title_en": "Form verbal noun (masdar) from Form IV verb 'أَرْسَلَ':",
            "grammar_goal_ur": "باب افعال کا مصدر 'إِفْعَالٌ' کے وزن پر آتا ہے (أَرْسَلَ -> إِرْسَالٌ)۔", "grammar_goal_en": "Masdar of Form IV is formed on pattern If'aal.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَرْسَلَ الْمُدِيرُ الرِّسَالَةَ [ ＿＿＿ ] سَرِيعاً .",
            "prompt_ur": "أَرْسَلَ کا درست مصدر منتخب کریں:",
            "prompt_en": "Select the correct masdar of 'أَرْسَلَ':",
            "answer": "إِرْسَالاً", "options": ["إِرْسَالاً", "رِسَالَةً", "مُرْسَلاً", "تَرْسِيلاً"],
            "emoji": "✉️", "hint_ur": "ڈائریکٹر نے خط کو تیزی سے بھیجا۔", "hint_en": "The director sent the letter quickly.",
            "explanation_ur": "درست جواب: 'إِرْسَالاً' (أَفْعَلَ کا مصدر إِفْعَال آتا ہے)",
            "explanation_en": "Correct: 'إِرْسَالاً' (Form IV masdar is If'aal)"
        },
        {
            "id": "b3_u17_q2", "book": 3, "unit_num": 17, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): صیاغتِ امر از باب افعال (أَفْعِلْ)", "badge_en": "Exercise (3): Imperative of Form IV (Af'il)",
            "tamreen_title_ar": "صُغِ الْأَمْرَ مِنْ بَابِ (أَفْعَلَ) بِهَمْزَةِ قَطْعٍ مَفْتُوحَةٍ:",
            "tamreen_title_ur": "أَغْلَقَ سے ہمزۂ قطع مفتوحہ کے ساتھ فعل امر بنائیں:",
            "tamreen_title_en": "Form imperative from Form IV with cutting hamzah (Af'il):",
            "grammar_goal_ur": "باب افعال کے امر میں ہمزہ قطعیہ مفتوحہ رہتی ہے (أَغْلِقْ)۔", "grammar_goal_en": "Form IV imperative takes hamzatul-qat' with fathah (أَغْلِقْ).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "يَا وَلَدُ، [ ＿＿＿ ] الْبَابَ قَبْلَ النَّوْمِ ! ",
            "prompt_ur": "دروازہ بند کرنے کا حکم دینے کے لیے درست امر منتخب کریں:",
            "prompt_en": "Select the correct Form IV imperative for 'close':",
            "answer": "أَغْلِقْ", "options": ["أَغْلِقْ", "اِغْلِقْ", "تُغْلِقْ", "أَغْلَقَ"],
            "emoji": "🚪", "hint_ur": "اے لڑکے، سونے سے پہلے دروازہ بند کرو!", "hint_en": "O boy, close the door before sleeping!",
            "explanation_ur": "درست جواب: 'أَغْلِقْ' (باب افعال کا امر ہمزۂ قطع مفتوحہ کے ساتھ أَفْعِلْ آتا ہے)",
            "explanation_en": "Correct: 'أَغْلِقْ' (Form IV imperative retains hamzah of qat' with fathah)"
        }
    ]

    return units

if __name__ == "__main__":
    u = get_b3_curriculum()
    print("Units in Book 3:", sorted(u.keys()))
    print("Total Qs in Book 3:", sum(len(v) for v in u.values()))
