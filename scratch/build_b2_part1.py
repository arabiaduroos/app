import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Part 1 of Book 2 Curriculum: Units 1 to 15
def get_b2_part1_units():
    units = {}
    
    # -------------------------------------------------------------
    # UNIT 1: إِنَّ وَأَخَوَاتُهَا • لَعَلَّ • ذُو • مِائَةٌ وَأَلْفٌ
    # -------------------------------------------------------------
    units[1] = [
        {
            "id": "b2_u1_q1", "book": 2, "unit_num": 1, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ مکالمہ", "badge_en": "Exercise (1): Dialogue Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "درج ذیل سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the following questions:",
            "grammar_goal_ur": "عربی سوالیہ جملوں کا فہم اور درست جواب کی ساخت۔", "grammar_goal_en": "Comprehending interrogative sentences and formulating correct responses.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مِنْ أَيْنَ هَاشِمٌ؟ [ ＿＿＿ ]",
            "prompt_ur": "ہاشم کہاں سے ہے؟ درست جواب منتخب کریں:", "prompt_en": "Where is Hashim from? Select the correct answer:",
            "answer": "هُوَ مِنَ الْهِنْدِ .",
            "options": ["هُوَ مِنَ الْهِنْدِ .", "هُوَ مِنَ الْيَابَانِ .", "هُوَ مِنَ الصِّينِ .", "هُوَ مِنَ الْبَاكِسْتَانِ ."],
            "emoji": "🇮🇳", "hint_ur": "وہ ہندوستان سے ہے۔", "hint_en": "He is from India.",
            "explanation_ur": "درست جواب: 'هُوَ مِنَ الْهِنْدِ .' (سبق کے مکالمے کے مطابق ہاشم ہندوستان سے ہے)",
            "explanation_en": "Correct answer: 'هُوَ مِنَ الْهِنْدِ .' (According to the lesson dialogue, Hashim is from India)"
        },
        {
            "id": "b2_u1_q2", "book": 2, "unit_num": 1, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): درست و غلط جملوں کی پہچان", "badge_en": "Exercise (2): True or False Verification",
            "tamreen_title_ar": "ضَعْ عَلَامَةَ (صح) أَوْ (×):", "tamreen_title_ur": "درست جملے کے سامنے (صح) اور غلط کے سامنے (×) لگائیں:", "tamreen_title_en": "Mark true sentences with (✓) and false with (✗):",
            "grammar_goal_ur": "صفت و موصوف اور سبق کے فہم کی جانچ۔", "grammar_goal_en": "Testing comprehension of adjectives and lesson facts.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هَاشِمٌ طَالِبٌ [ ＿＿＿ ]",
            "prompt_ur": "ہاشم کیسا طالب علم ہے؟ درست صفت منتخب کریں:", "prompt_en": "What kind of student is Hashim? Select the correct adjective:",
            "answer": "مُجْتَهِدٌ",
            "options": ["مُجْتَهِدٌ", "كَسْلَانُ", "غَبِيٌّ", "ضَعِيفٌ"],
            "emoji": "👨‍🎓", "hint_ur": "ہاشم ایک محنتی طالب علم ہے۔", "hint_en": "Hashim is a hardworking student.",
            "explanation_ur": "درست جواب: 'مُجْتَهِدٌ' (ہاشم محنتی طالب علم ہے)",
            "explanation_en": "Correct answer: 'مُجْتَهِدٌ' (hardworking student)"
        },
        {
            "id": "b2_u1_q3", "book": 2, "unit_num": 1, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): ضمیروں پر (إِنَّ) کا داخل ہونا", "badge_en": "Exercise (4): Attaching Pronouns to Inna",
            "tamreen_title_ar": "أَدْخِلْ (إِنَّ) عَلَى الْجُمَلِ الآتِيَةِ:", "tamreen_title_ur": "درج ذیل جملوں پر 'إِنَّ' داخل کریں:", "tamreen_title_en": "Enter 'Inna' onto the following pronoun sentences:",
            "grammar_goal_ur": "منفصل ضمیروں کا 'إنّ' کے ساتھ متصل منصوب ضمیر میں تبدیل ہونا۔", "grammar_goal_en": "Converting detached subject pronouns to attached accusative pronouns with Inna.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هُوَ تَاجِرٌ ➔ [ ＿＿＿ ] تَاجِرٌ .",
            "prompt_ur": "هُوَ تَاجِرٌ پر إِنَّ داخل کریں:", "prompt_en": "Enter Inna onto 'هُوَ تَاجِرٌ':",
            "answer": "إِنَّهُ",
            "options": ["إِنَّهُ", "إِنَّ هُوَ", "إِنَّكَ", "إِنَّهُمْ"],
            "emoji": "💼", "hint_ur": "بلاشبہ وہ ایک تاجر ہے۔", "hint_en": "Indeed, he is a merchant.",
            "explanation_ur": "درست جواب: 'إِنَّهُ' (إنّ کے ساتھ ضمیر 'هو' متصل ہو کر 'إنّه' بنتی ہے)",
            "explanation_en": "Correct answer: 'إِنَّهُ' (With Inna, the pronoun 'huwa' becomes the attached 'innahu')"
        },
        {
            "id": "b2_u1_q4", "book": 2, "unit_num": 1, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): ضمیروں پر (إِنَّ) کا داخل ہونا", "badge_en": "Exercise (4): Attaching Pronouns to Inna",
            "tamreen_title_ar": "أَدْخِلْ (إِنَّ) عَلَى الْجُمَلِ الآتِيَةِ:", "tamreen_title_ur": "درج ذیل جملوں پر 'إِنَّ' داخل کریں:", "tamreen_title_en": "Enter 'Inna' onto the following pronoun sentences:",
            "grammar_goal_ur": "متکلم کی ضمیر کے ساتھ 'إِنَّنِي' یا 'إِنِّي' کی ساخت۔", "grammar_goal_en": "Forming 1st person singular with Inna (innanee / innee).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا طَالِبٌ ➔ [ ＿＿＿ ] طَالِبٌ .",
            "prompt_ur": "أَنَا طَالِبٌ پر إِنَّ داخل کریں:", "prompt_en": "Enter Inna onto 'أَنَا طَالِبٌ':",
            "answer": "إِنِّي",
            "options": ["إِنِّي", "إِنَّ أَنَا", "إِنَّنَا", "إِنَّكَ"],
            "emoji": "👨‍🎓", "hint_ur": "بلاشبہ میں ایک طالب علم ہوں۔", "hint_en": "Indeed, I am a student.",
            "explanation_ur": "درست جواب: 'إِنِّي' (یا 'إِنَّنِي')",
            "explanation_en": "Correct answer: 'إِنِّي' (or 'إِنَّنِي')"
        },
        {
            "id": "b2_u1_q5", "book": 2, "unit_num": 1, "tamreen_num": 6,
            "badge_ar": "التَّمْرِينُ (6)", "badge_ur": "مشق (6): اسم پر (إِنَّ) کا داخل ہونا اور اعراب", "badge_en": "Exercise (6): Inna with Nouns & I'rab",
            "tamreen_title_ar": "أَدْخِلْ (إِنَّ) وَاضْبِطْ أَوَاخِرَ الْكَلِمَاتِ:", "tamreen_title_ur": "'إِنَّ' داخل کریں اور الفاظ کے آخری اعراب درست کریں:", "tamreen_title_en": "Enter 'Inna' and apply correct voweling to word endings:",
            "grammar_goal_ur": "إنّ کے اسم کا منسوب (زبر) اور خبر کا مرفوع (پیش) ہونا۔", "grammar_goal_en": "Recognizing that Inna's noun takes accusative fathah and predicate takes nominative dammah.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الدَّرْسُ صَعْبٌ ➔ [ ＿＿＿ ] صَعْبٌ .",
            "prompt_ur": "درست اعراب والا لفظ منتخب کریں:", "prompt_en": "Select the correctly voweled noun for Inna:",
            "answer": "إِنَّ الدَّرْسَ",
            "options": ["إِنَّ الدَّرْسَ", "إِنَّ الدَّرْسُ", "إِنَّ الدَّرْسِ", "إِنَّ دَرْساً"],
            "emoji": "📖", "hint_ur": "بے شک سبق مشکل ہے۔", "hint_en": "Indeed, the lesson is difficult.",
            "explanation_ur": "درست جواب: 'إِنَّ الدَّرْسَ' (إنّ اپنے اسم کو زبر/نصب دیتی ہے: اسمُ إنّ منصوب بالفتحة)",
            "explanation_en": "Correct answer: 'إِنَّ الدَّرْسَ' (Inna makes its noun accusative with fathah)"
        },
        {
            "id": "b2_u1_q6", "book": 2, "unit_num": 1, "tamreen_num": 7,
            "badge_ar": "التَّمْرِينُ (7)", "badge_ur": "مشق (7): اسم تفضیل (أَفْعَلُ مِنْ)", "badge_en": "Exercise (7): Comparative Degree (Af'alu min)",
            "tamreen_title_ar": "صُغِ اسْمَ التَّفْضِيلِ عَلَى وَزْنِ (أَفْعَلُ):", "tamreen_title_ur": "اسم تفضیل کو وزن 'أَفْعَلُ مِنْ' پر لائیں:", "tamreen_title_en": "Form the comparative degree on the pattern 'Af'alu min':",
            "grammar_goal_ur": "عربی میں دو چیزوں کا موازنہ کرنے کے لیے اسم تفضیل 'أفعل من' کا استعمال۔", "grammar_goal_en": "Using the comparative pattern 'Af'alu min' to compare two entities.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هَاشِمٌ طَوِيلٌ وَحَامِدٌ [ ＿＿＿ ] مِنْهُ .",
            "prompt_ur": "طَوِيلٌ کا اسم تفضیل منتخب کریں:", "prompt_en": "Select the comparative form of 'طَوِيلٌ':",
            "answer": "أَطْوَلُ",
            "options": ["أَطْوَلُ", "أَكْبَرُ", "طَوِيلٌ", "أَطْوَلِ"],
            "emoji": "📏", "hint_ur": "ہاشم لمبا ہے اور حامد اس سے زیادہ لمبا ہے۔", "hint_en": "Hashim is tall, and Hamid is taller than him.",
            "explanation_ur": "درست جواب: 'أَطْوَلُ' (طويل کا اسم تفضیل 'أَفْعَلُ' کے وزن پر 'أَطْوَلُ' بنتا ہے)",
            "explanation_en": "Correct answer: 'أَطْوَلُ' (Comparative of taweel on the pattern of af'alu is atwalu)"
        },
        {
            "id": "b2_u1_q7", "book": 2, "unit_num": 1, "tamreen_num": 8,
            "badge_ar": "التَّمْرِينُ (8)", "badge_ur": "مشق (8): کلمہ (ذُو) کا استعمال", "badge_en": "Exercise (8): Using the Particle 'Dhu' (Owner of)",
            "tamreen_title_ar": "اسْتَعْمِلْ كَلِمَةَ (ذُو) بِمَعْنَى صَاحِب:", "tamreen_title_ur": "صاحب/والا کے معنی میں 'ذُو' کا درست استعمال:", "tamreen_title_en": "Use 'Dhu' meaning possessor/owner:",
            "grammar_goal_ur": "'ذو' ہمیشہ مضاف ہوتا ہے اور اس کے بعد والا اسم مجرور ہوتا ہے۔", "grammar_goal_en": "Understanding that 'Dhu' is always mudhaf and followed by a genitive mudhaf ilayh.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذَا الطَّالِبُ ذُو [ ＿＿＿ ] حَسَنٍ .",
            "prompt_ur": "درست اعراب والا لفظ منتخب کریں:", "prompt_en": "Select the correct genitive word following 'ذُو':",
            "answer": "خُلُقٍ",
            "options": ["خُلُقٍ", "خُلُقٌ", "خُلُقاً", "الْخُلُقُ"],
            "emoji": "🌟", "hint_ur": "یہ طالب علم اچھے اخلاق والا ہے۔", "hint_en": "This student has good character.",
            "explanation_ur": "درست جواب: 'خُلُقٍ' (ذو کے بعد مضاف الیہ ہمیشہ مجرور ہوتا ہے)",
            "explanation_en": "Correct answer: 'خُلُقٍ' (The noun after Dhu is mudhaf ilayh and always majroor)"
        },
        {
            "id": "b2_u1_q8", "book": 2, "unit_num": 1, "tamreen_num": 10,
            "badge_ar": "التَّمْرِينُ (10)", "badge_ur": "مشق (10): (لَعَلَّ) کا استعمال", "badge_en": "Exercise (10): Using 'La'alla' (Perhaps / Hope)",
            "tamreen_title_ar": "أَدْخِلْ (لَعَلَّ) عَلَى الْجُمَلِ الآتِيَةِ:", "tamreen_title_ur": "'لَعَلَّ' داخل کریں (یہ 'إِنَّ' کی بہنوں میں سے ہے):", "tamreen_title_en": "Enter 'La'alla' (one of the sisters of Inna):",
            "grammar_goal_ur": "'لعلّ' امید یا اندیشے کے لیے آتا ہے اور إنّ کی طرح اسم کو نصب دیتا ہے۔", "grammar_goal_en": "Using 'La'alla' for hope/fear and applying accusative case to its subject.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هُوَ مَرِيضٌ ➔ [ ＿＿＿ ] مَرِيضٌ .",
            "prompt_ur": "هُوَ مَرِيضٌ پر لَعَلَّ داخل کریں:", "prompt_en": "Enter La'alla onto 'هُوَ مَرِيضٌ':",
            "answer": "لَعَلَّهُ",
            "options": ["لَعَلَّهُ", "لَعَلَّ هُوَ", "لَعَلَّكَ", "إِنَّهُ"],
            "emoji": "🤒", "hint_ur": "شاید وہ بیمار ہے۔", "hint_en": "Perhaps he is sick.",
            "explanation_ur": "درست جواب: 'لَعَلَّهُ' (لعلّ کے ساتھ ضمیر متصل ہو جاتی ہے)",
            "explanation_en": "Correct answer: 'لَعَلَّهُ' (Pronoun attaches to La'alla as -hu)"
        },
        {
            "id": "b2_u1_q9", "book": 2, "unit_num": 1, "tamreen_num": 11,
            "badge_ar": "التَّمْرِينُ (11)", "badge_ur": "مشق (11): (غَالٍ) بمقابلہ (غَالِيَةٌ)", "badge_en": "Exercise (11): 'Ghalin' vs 'Ghaliyah'",
            "tamreen_title_ar": "أَكْمِلْ بِـ (غَالٍ) أَوْ (غَالِيَةٌ):", "tamreen_title_ur": "مذکر کے لیے 'غَالٍ' اور مؤنث کے لیے 'غَالِيَةٌ' لگائیں:", "tamreen_title_en": "Fill in the blank with masculine 'غَالٍ' or feminine 'غَالِيَةٌ':",
            "grammar_goal_ur": "اسم منقوص 'غالٍ' کی مذکر اور مؤنث شکلوں کا امتیاز۔", "grammar_goal_en": "Distinguishing masculine defective noun 'ghalin' from regular feminine 'ghaliyah'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هٰذِهِ السَّيَّارَةُ [ ＿＿＿ ] .",
            "prompt_ur": "مؤنث اسم (السَّيَّارَةُ) کے لیے درست صفت منتخب کریں:", "prompt_en": "Select the correct adjective for the feminine noun 'السَّيَّارَةُ':",
            "answer": "غَالِيَةٌ",
            "options": ["غَالِيَةٌ", "غَالٍ", "رَخِيصٌ", "غَالِي"],
            "emoji": "🚗", "hint_ur": "یہ گاڑی مہنگی ہے۔", "hint_en": "This car is expensive.",
            "explanation_ur": "درست جواب: 'غَالِيَةٌ' (سیارۃ مؤنث ہے اس لیے صفت مؤنث آئے گی)",
            "explanation_en": "Correct answer: 'غَالِيَةٌ' (Sayyarah is feminine, so it takes feminine ghaliyah)"
        },
        {
            "id": "b2_u1_q10", "book": 2, "unit_num": 1, "tamreen_num": 12,
            "badge_ar": "التَّمْرِينُ (12)", "badge_ur": "مشق (12): (مِائَة) اور (أَلْف) کا معدود", "badge_en": "Exercise (12): Counted Nouns with 100 & 1000",
            "tamreen_title_ar": "تَأَمَّلْ مَعْدُودَ (مِائَة) وَ (أَلْف):", "tamreen_title_ur": "'مائة' اور 'ألف' کے بعد معدود کے اعراب کا مشاہدہ کریں:", "tamreen_title_en": "Observe the case of counted nouns after Mi'ah (100) and Alf (1000):",
            "grammar_goal_ur": "سو اور ہزار کا معدود ہمیشہ مفرد مجرور (زیر کے ساتھ) ہوتا ہے۔", "grammar_goal_en": "Counted nouns with 100 and 1000 are always singular genitive (majroor).",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "عِنْدِي مِائَةُ [ ＿＿＿ ] .",
            "prompt_ur": "مِائَةُ کے بعد درست معدود منتخب کریں:", "prompt_en": "Select the correct counted noun after 'مِائَةُ':",
            "answer": "رِيَالٍ",
            "options": ["رِيَالٍ", "رِيَالاً", "رِيَالٌ", "رِيَالَاتٍ"],
            "emoji": "💵", "hint_ur": "میرے پاس ایک سو ریال ہیں۔", "hint_en": "I have one hundred riyals.",
            "explanation_ur": "درست جواب: 'رِيَالٍ' (سو اور ہزار کا معدود مفرد مجرور ہوتا ہے)",
            "explanation_en": "Correct answer: 'رِيَالٍ' (Counted noun with 100 is singular majroor)"
        }
    ]

    # -------------------------------------------------------------
    # UNIT 2: لَيْسَ وَخَبَرُهَا الْمَجْرُورُ بِالْبَاءِ
    # -------------------------------------------------------------
    units[2] = [
        {
            "id": "b2_u2_q1", "book": 2, "unit_num": 2, "tamreen_num": 1,
            "badge_ar": "التَّمْرِينُ (1)", "badge_ur": "مشق (1): فہمِ مکالمہ", "badge_en": "Exercise (1): Dialogue Comprehension",
            "tamreen_title_ar": "أَجِبْ عَنِ الْأَسْئِلَةِ الآتِيَةِ:", "tamreen_title_ur": "درج ذیل سوالات کے جوابات دیں:", "tamreen_title_en": "Answer the following questions:",
            "grammar_goal_ur": "عربی سوالات کے جوابات میں منفی جملے کا استعمال۔", "grammar_goal_en": "Using negative structures in response to comprehension questions.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "مِنْ أَيْنَ هِشَامٌ؟ [ ＿＿＿ ]",
            "prompt_ur": "ہشام کہاں سے ہے؟ درست جواب منتخب کریں:", "prompt_en": "Where is Hisham from? Select the correct answer:",
            "answer": "هُوَ مِنْ نِيُويُورْكَ .",
            "options": ["هُوَ مِنْ نِيُويُورْكَ .", "هُوَ مِنْ وَاشِنْطُنَ .", "هُوَ مِنَ الْهِنْدِ .", "هُوَ مِنَ الْيَابَانِ ."],
            "emoji": "🏙️", "hint_ur": "وہ نیویارک سے ہے۔", "hint_en": "He is from New York.",
            "explanation_ur": "درست جواب: 'هُوَ مِنْ نِيُويُورْكَ .' (ہشام واشنگٹن سے نہیں بلکہ نیویارک سے ہے)",
            "explanation_en": "Correct answer: 'هُوَ مِنْ نِيُويُورْكَ .' (Hisham is from New York)"
        },
        {
            "id": "b2_u2_q2", "book": 2, "unit_num": 2, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): (لَيْسَ) کے ساتھ نفی اور بائے زائدہ", "badge_en": "Exercise (2): Negation with Laysa & Ba",
            "tamreen_title_ar": "أَدْخِلْ (لَيْسَ) مَعَ الْبَاءِ عَلَى الْجُمَلِ الآتِيَةِ:", "tamreen_title_ur": "'لَيْسَ' داخل کریں اور خبر پر 'بِـ' لگائیں:", "tamreen_title_en": "Enter 'Laysa' and attach preposition 'bi-' to the predicate:",
            "grammar_goal_ur": "لیس کی خبر پر بائے زائدہ داخل ہو کر لفظاً مجرور ہو جاتی ہے۔", "grammar_goal_en": "Attaching emphasizing 'bi-' to the predicate of Laysa making it genitive in form.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "الْبَيْتُ جَدِيدٌ ➔ لَيْسَ الْبَيْتُ [ ＿＿＿ ] .",
            "prompt_ur": "درست خبر منتخب کریں:", "prompt_en": "Select the correct predicate with 'bi-':",
            "answer": "بِجَدِيدٍ",
            "options": ["بِجَدِيدٍ", "بِجَدِيدٌ", "بِجَدِيداً", "جَدِيدٌ"],
            "emoji": "🏠", "hint_ur": "گھر نیا نہیں ہے۔", "hint_en": "The house is not new.",
            "explanation_ur": "درست جواب: 'بِجَدِيدٍ' (لیس کی خبر پر 'بِـ' لگنے سے دو زیر/جر آتی ہے)",
            "explanation_en": "Correct answer: 'بِجَدِيدٍ' (Preposition 'bi-' makes the predicate majroor with kasrah)"
        },
        {
            "id": "b2_u2_q3", "book": 2, "unit_num": 2, "tamreen_num": 2,
            "badge_ar": "التَّمْرِينُ (2)", "badge_ur": "مشق (2): مؤنث کے لیے (لَيْسَتْ)", "badge_en": "Exercise (2): Feminine Form 'Laysat'",
            "tamreen_title_ar": "انْفِ الْجُمْلَةَ الْمُؤَنَّثَةَ بِـ (لَيْسَتْ):", "tamreen_title_ur": "مؤنث جملے کی نفی 'لَيْسَتْ' کے ساتھ کریں:", "tamreen_title_en": "Negate the feminine sentence using 'Laysat':",
            "grammar_goal_ur": "مؤنث فاعل کے ساتھ 'لَيْسَتْ' کی تانیث۔", "grammar_goal_en": "Using the feminine form 'Laysat' with feminine subjects.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "السَّيَّارَةُ قَدِيمَةٌ ➔ [ ＿＿＿ ] السَّيَّارَةُ بِقَدِيمَةٍ .",
            "prompt_ur": "مؤنث کے لیے درست نفی کا کلمہ منتخب کریں:", "prompt_en": "Select the correct feminine negative verb:",
            "answer": "لَيْسَتِ",
            "options": ["لَيْسَتِ", "لَيْسَ", "لَسْتُ", "مَا"],
            "emoji": "🚗", "hint_ur": "گاڑی پرانی نہیں ہے۔", "hint_en": "The car is not old.",
            "explanation_ur": "درست جواب: 'لَيْسَتِ' (السیارۃ مؤنث ہے اس لیے تائے تانیث کے ساتھ 'لَیْسَتْ' آئے گا)",
            "explanation_en": "Correct answer: 'لَيْسَتِ' (Feminine subject takes Laysat)"
        },
        {
            "id": "b2_u2_q4", "book": 2, "unit_num": 2, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): تصریفِ (لَيْسَ) مع الضمائر", "badge_en": "Exercise (3): Conjugating Laysa with Pronouns",
            "tamreen_title_ar": "صَرِّفْ (لَيْسَ) مَعَ الضَّمِيرِ (أَنَا):", "tamreen_title_ur": "'أنا' (میں) کے ساتھ 'لَيْسَ' کی درست گردان منتخب کریں:", "tamreen_title_en": "Conjugate 'Laysa' with 1st person singular 'أَنَا':",
            "grammar_goal_ur": "متکلم کے ساتھ 'لَسْتُ' کی ساخت اور یاء کا حذف۔", "grammar_goal_en": "Forming 1st person 'lastu' with elision of the medial yaa.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنَا مُهَنْدِسٌ ➔ [ ＿＿＿ ] بِمُهَنْدِسٍ .",
            "prompt_ur": "درست صیغہ منتخب کریں:", "prompt_en": "Select the correct conjugated form for 'I am not':",
            "answer": "لَسْتُ",
            "options": ["لَسْتُ", "لَيْسَ أَنَا", "لَيْسْتُ", "لَسْنَا"],
            "emoji": "👷", "hint_ur": "میں انجینئر نہیں ہوں۔", "hint_en": "I am not an engineer.",
            "explanation_ur": "درست جواب: 'لَسْتُ' (أنا کے ساتھ 'لَسْتُ' بنتا ہے)",
            "explanation_en": "Correct answer: 'لَسْتُ' (With Ana, it conjugates to Lastu)"
        },
        {
            "id": "b2_u2_q5", "book": 2, "unit_num": 2, "tamreen_num": 3,
            "badge_ar": "التَّمْرِينُ (3)", "badge_ur": "مشق (3): جمع مذکر کے ساتھ (لَيْسُوا)", "badge_en": "Exercise (3): Plural Form 'Laysū'",
            "tamreen_title_ar": "صَرِّفْ (لَيْسَ) مَعَ جَمْعِ الْمُذَكَّرِ (هُمْ):", "tamreen_title_ur": "'هُمْ' (وہ سب) کے ساتھ 'لَيْسَ' کی درست شکل:", "tamreen_title_en": "Conjugate 'Laysa' with 3rd person plural masculine 'هُمْ':",
            "grammar_goal_ur": "جمع مذکر غائب کے ساتھ 'لَيْسُوا' کی ساخت۔", "grammar_goal_en": "Forming 3rd person plural masculine 'laysū'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "هُمْ طُلَّابٌ ➔ هُمْ [ ＿＿＿ ] بِطُلَّابٍ .",
            "prompt_ur": "درست صیغہ منتخب کریں:", "prompt_en": "Select the correct plural form:",
            "answer": "لَيْسُوا",
            "options": ["لَيْسُوا", "لَسْتُمْ", "لَسْنَا", "لَيْسَ"],
            "emoji": "👥", "hint_ur": "وہ سب طلبہ نہیں ہیں۔", "hint_en": "They are not students.",
            "explanation_ur": "درست جواب: 'لَيْسُوا' (جمع مذکر غائب کے لیے واؤ جمع کے ساتھ 'لَيْسُوا' آتا ہے)",
            "explanation_en": "Correct answer: 'لَيْسُوا' (Plural masculine takes Laysū)"
        },
        {
            "id": "b2_u2_q6", "book": 2, "unit_num": 2, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): سوال (أَلَيْسَ كَذٰلِكَ؟) کا جواب", "badge_en": "Exercise (4): Answering Negative Question with 'Balaa'",
            "tamreen_title_ar": "أَجِبْ عَنِ السُّؤَالِ الْمَنْفِيِّ بـ (بَلَى):", "tamreen_title_ur": "منفی سوال کا اثبات میں جواب دینے کے لیے 'بَلَى' (کیوں نہیں / بالکل) کا استعمال:", "tamreen_title_en": "Answering a negative question in the affirmative using 'Balaa' (Yes indeed):",
            "grammar_goal_ur": "ہمزہ استفہام مع نفی کے جواب میں 'بَلَى' کا اصول سمجھنا۔", "grammar_goal_en": "Using 'Balaa' (yes indeed/on the contrary) to affirm a negative question.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَلَسْتَ بِطَالِبٍ؟ ➔ [ ＿＿＿ ] ، أَنَا طَالِبٌ .",
            "prompt_ur": "اثبات میں جواب کے لیے درست کلمہ منتخب کریں:", "prompt_en": "Select the correct affirming particle for a negative question:",
            "answer": "بَلَى",
            "options": ["بَلَى", "نَعَمْ", "لَا", "أَجَلْ"],
            "emoji": "🙋‍♂️", "hint_ur": "کیا تم طالب علم نہیں ہو؟ کیوں نہیں، میں طالب علم ہوں۔", "hint_en": "Are you not a student? Yes indeed, I am a student.",
            "explanation_ur": "درست جواب: 'بَلَى' (منفی سوال کے جواب میں اثبات کے لیے 'بلى' آتا ہے)",
            "explanation_en": "Correct answer: 'بَلَى' ('Balaa' is used to affirm a negative question)"
        },
        {
            "id": "b2_u2_q7", "book": 2, "unit_num": 2, "tamreen_num": 4,
            "badge_ar": "التَّمْرِينُ (4)", "badge_ur": "مشق (4): مخاطب کے لیے (لَسْتَ)", "badge_en": "Exercise (4): 2nd Person Singular 'Lasta'",
            "tamreen_title_ar": "صَرِّفْ (لَيْسَ) مَعَ (أَنْتَ):", "tamreen_title_ur": "'أَنْتَ' (تم) کے ساتھ 'لَيْسَ' کی درست گردان منتخب کریں:", "tamreen_title_en": "Conjugate 'Laysa' with 2nd person masculine 'أَنْتَ':",
            "grammar_goal_ur": "مخاطب مذکر کے ساتھ 'لَسْتَ' کی ساخت۔", "grammar_goal_en": "Forming 2nd person singular masculine 'lasta'.",
            "type": "fill_blank", "strict_tashkeel": True,
            "prompt_ar": "أَنْتَ فَقِيرٌ ➔ [ ＿＿＿ ] بِفَقِيرٍ .",
            "prompt_ur": "أَنْتَ کے لیے درست منفی فعل منتخب کریں:", "prompt_en": "Select the correct form for 'you are not':",
            "answer": "لَسْتَ",
            "options": ["لَسْتَ", "لَسْتُ", "لَيْسَ", "لَسْتِ"],
            "emoji": "👉", "hint_ur": "تم غریب نہیں ہو۔", "hint_en": "You are not poor.",
            "explanation_ur": "درست جواب: 'لَسْتَ' (أنتَ کے ساتھ تا پر زبر کے ساتھ 'لَسْتَ' آتا ہے)",
            "explanation_en": "Correct answer: 'لَسْتَ' (With Anta, it conjugates to Lasta)"
        }
    ]

    return units

print("Book 2 Part 1 generator module loaded successfully.")
