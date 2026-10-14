import sys, json
sys.stdout.reconfigure(encoding='utf-8')

# Definition of authentic numbered exercises for all 31 units of Book 2
# Each unit maps to a list of Tamreens, each with its authentic questions

BOOK2_TAMREENS = {
    # Unit 1 (الدرس الأول)
    1: [
        {
            "num": 1,
            "title_ar": "التَّمْرِينُ (1): أجب عن الأسئلة الآتية",
            "title_ur": "مشق (1): سوالات کے جوابات دیں (مکالمے کی بنیاد پر)",
            "title_en": "Exercise (1): Answer the questions based on the lesson dialogue",
            "goal_ur": "درس کے مفہوم اور قرآنی/عربی طرزِ سوال و جواب کی فہم",
            "goal_en": "Comprehend dialogue text and answer questions accurately in Arabic",
            "questions": [
                {
                    "prompt_ar": "مِنْ أَيْنَ هَاشِمٌ؟",
                    "prompt_ur": "صحیح جواب منتخب کریں:",
                    "prompt_en": "Select the correct answer:",
                    "answer": "هُوَ مِنَ الْهِنْدِ",
                    "options": ["هُوَ مِنَ الْهِنْدِ", "هُوَ مِنَ الْيَابَانِ", "هُوَ مِنَ الصِّينِ", "هُوَ مِنَ الْكُوَيْتِ"],
                    "emoji": "🇮🇳",
                    "hint_ur": "ہاشم بھارت (انڈیا) سے ہے",
                    "hint_en": "Hashim is from India."
                },
                {
                    "prompt_ar": "بِكَمْ سَاعَةُ هَاشِمٍ؟",
                    "prompt_ur": "صحیح جواب منتخب کریں:",
                    "prompt_en": "Select the correct answer:",
                    "answer": "هِيَ بِمِائَةِ رِيَالٍ",
                    "options": ["هِيَ بِمِائَةِ رِيَالٍ", "هِيَ بِعَشَرَةِ رِيَالَاتٍ", "هِيَ بِأَلْفِ رِيَالٍ", "هِيَ مَجَّانًا"],
                    "emoji": "⌚",
                    "hint_ur": "ہاشم کی گھڑی سو (100) ریال کی ہے",
                    "hint_en": "His watch cost 100 Riyals."
                },
                {
                    "prompt_ar": "كَمْ أَخًا لِهَاشِمٍ؟",
                    "prompt_ur": "صحیح جواب منتخب کریں:",
                    "prompt_en": "Select the correct answer:",
                    "answer": "لَهُ ثَلَاثَةُ إِخْوَةٍ",
                    "options": ["لَهُ ثَلَاثَةُ إِخْوَةٍ", "لَهُ أَرْبَعَةُ إِخْوَةٍ", "لَهُ أَخٌ وَاحِدٌ", "لَيْسَ لَهُ إِخْوَةٌ"],
                    "emoji": "👨‍👦‍👦",
                    "hint_ur": "ہاشم کے تین بھائی ہیں",
                    "hint_en": "Hashim has three brothers."
                }
            ]
        },
        {
            "num": 2,
            "title_ar": "التَّمْرِينُ (2): اتِّصَالُ الضَّمَائِرِ بِـ (إِنَّ)",
            "title_ur": "مشق (2): (إِنَّ) کے ساتھ متصل ضمائر کا درست استعمال",
            "title_en": "Exercise (2): Attaching pronouns to Inna (Innahu, Innahum, Innee...)",
            "goal_ur": "ضمیر منفصل کو (إِنَّ) کے ساتھ ضمیر متصل میں تبدیل کرنا",
            "goal_en": "Transforming independent pronouns into attached pronouns with Inna",
            "questions": [
                {
                    "prompt_ar": "هُوَ تَاجِرٌ ➔ [ ＿＿＿ ] تَاجِرٌ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "إِنَّهُ",
                    "options": ["إِنَّهُ", "إِنَّهُمْ", "إِنَّكَ", "إِنَّنِي"],
                    "emoji": "💼",
                    "hint_ur": "هُوَ کے ساتھ إِنَّهُ بنتا ہے",
                    "hint_en": "With 'huwa', it becomes 'innahu'."
                },
                {
                    "prompt_ar": "أَنَا طَالِبٌ ➔ [ ＿＿＿ ] طَالِبٌ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "إِنَّنِي",
                    "options": ["إِنَّنِي", "إِنَّهُ", "إِنَّكَ", "إِنَّكُمْ"],
                    "emoji": "👨‍🎓",
                    "hint_ur": "أَنَا کے ساتھ إِنَّنِي یا إِنِّي بنتا ہے",
                    "hint_en": "With 'ana', it becomes 'innee' or 'innanee'."
                },
                {
                    "prompt_ar": "هُمْ أَذْكِيَاءُ ➔ [ ＿＿＿ ] أَذْكِيَاءُ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "إِنَّهُمْ",
                    "options": ["إِنَّهُمْ", "إِنَّهُ", "إِنَّهَا", "إِنَّكُمْ"],
                    "emoji": "🧠",
                    "hint_ur": "هُمْ کے ساتھ إِنَّهُمْ بنتا ہے",
                    "hint_en": "With 'hum', it becomes 'innahum'."
                }
            ]
        },
        {
            "num": 3,
            "title_ar": "التَّمْرِينُ (3): إِعْرَابُ اسْمِ (إِنَّ)",
            "title_ur": "مشق (3): (إِنَّ) کے اسم کا اعراب (نصب)",
            "title_en": "Exercise (3): Case ending of Ism Inna (Accusative / Fathah)",
            "goal_ur": "اسمِ إنّ کو ہمیشہ منصوب (فتحة) کرنا",
            "goal_en": "Making the noun following Inna accusative (mansoob with fathah)",
            "questions": [
                {
                    "prompt_ar": "الدَّرْسُ صَعْبٌ ➔ إِنَّ [ ＿＿＿ ] صَعْبٌ .",
                    "prompt_ur": "صحیح اعراب منتخب کریں:",
                    "prompt_en": "Select the correct form:",
                    "answer": "الدَّرْسَ",
                    "options": ["الدَّرْسَ", "الدَّرْسُ", "الدَّرْسِ", "الدَّرْسْ"],
                    "emoji": "📖",
                    "hint_ur": "اسمِ إنّ منصوب (زبر/فتحة) ہوتا ہے",
                    "hint_en": "Ism Inna is mansoob (takes fathah)."
                },
                {
                    "prompt_ar": "السَّيَّارَةُ جَمِيلَةٌ ➔ إِنَّ [ ＿＿＿ ] جَمِيلَةٌ .",
                    "prompt_ur": "صحیح اعراب منتخب کریں:",
                    "prompt_en": "Select the correct form:",
                    "answer": "السَّيَّارَةَ",
                    "options": ["السَّيَّارَةَ", "السَّيَّارَةُ", "السَّيَّارَةِ", "السَّيَّارَةْ"],
                    "emoji": "🚗",
                    "hint_ur": "إنّ کا اسم زبر کے ساتھ: السَّيَّارَةَ",
                    "hint_en": "Ism Inna takes fathah: as-sayyaarata."
                }
            ]
        },
        {
            "num": 4,
            "title_ar": "التَّمْرِينُ (4): اسْتِعْمَالُ (أَمْ) فِي الِاسْتِفْهَامِ",
            "title_ur": "مشق (4): ہمزۂ استفہام کے ساتھ (أَمْ) کا استعمال",
            "title_en": "Exercise (4): Using 'Am' (or) in interrogative sentences",
            "goal_ur": "دو متبادلات کے درمیان سوال میں (أَمْ) کا درست استعمال",
            "goal_en": "Using 'am' correctly when offering alternatives with hamzat al-istifhaam",
            "questions": [
                {
                    "prompt_ar": "أَمِنَ الْهِنْدِ أَنْتَ [ ＿＿＿ ] مِنْ بَاكِسْتَانَ؟",
                    "prompt_ur": "مناسب لفظ منتخب کریں:",
                    "prompt_en": "Select the appropriate word:",
                    "answer": "أَمْ",
                    "options": ["أَمْ", "أَوْ", "ثُمَّ", "وَ"],
                    "emoji": "❓",
                    "hint_ur": "ہمزۂ استفہام کے بعد 'یا' کے معنی میں 'أَمْ' آتا ہے",
                    "hint_en": "After the interrogative hamzah, 'am' is used for 'or'."
                },
                {
                    "prompt_ar": "أَطَبِيبٌ أَنْتَ [ ＿＿＿ ] مُهَنْدِسٌ؟",
                    "prompt_ur": "مناسب لفظ منتخب کریں:",
                    "prompt_en": "Select the appropriate word:",
                    "answer": "أَمْ",
                    "options": ["أَمْ", "أَوْ", "بَلْ", "لَكِنْ"],
                    "emoji": "👨‍⚕️",
                    "hint_ur": "أَ کے بعد متبادل کے لیے أَمْ استعمال ہوتا ہے",
                    "hint_en": "Use 'am' with hamzat al-istifhaam."
                }
            ]
        },
        {
            "num": 5,
            "title_ar": "التَّمْرِينُ (5): اسْمُ التَّفْضِيلِ (أَفْعَلُ مِنْ)",
            "title_ur": "مشق (5): اسم التفضیل کا وزن (أَفْعَلُ مِنْ)",
            "title_en": "Exercise (5): Comparative adjective (Af'alu min)",
            "goal_ur": "صفت سے اسمِ تفضیل (أَفْعَلُ) بنانا",
            "goal_en": "Forming comparative adjectives on the pattern of Af'alu",
            "questions": [
                {
                    "prompt_ar": "حَامِدٌ طَوِيلٌ وَعَلِيٌّ قَصِيرٌ ➔ حَامِدٌ [ ＿＿＿ ] مِنْ عَلِيٍّ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "أَطْوَلُ",
                    "options": ["أَطْوَلُ", "طَوِيلٌ", "أَقْصَرُ", "طَوِيلَةٌ"],
                    "emoji": "📏",
                    "hint_ur": "طويل سے اسم تفضیل: أَطْوَلُ (زیادہ لمبا)",
                    "hint_en": "Comparative of taweel is atwalu (taller)."
                },
                {
                    "prompt_ar": "الْقَاهِرَةُ كَبِيرَةٌ وَدِمَشْقُ صَغِيرَةٌ ➔ الْقَاهِرَةُ [ ＿＿＿ ] مِنْ دِمَشْقَ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "أَكْبَرُ",
                    "options": ["أَكْبَرُ", "كَبِيرَةٌ", "أَصْغَرُ", "أَكْبَرِ"],
                    "emoji": "🏙️",
                    "hint_ur": "كبيرة سے اسم تفضیل: أَكْبَرُ",
                    "hint_en": "Comparative of kabeer is akbaru (larger)."
                }
            ]
        },
        {
            "num": 6,
            "title_ar": "التَّمْرِينُ (6): اسْتِعْمَالُ (ذُو) بِمَعْنَى صَاحِب",
            "title_ur": "مشق (6): (ذُو) کا استعمال (والا / صاحب)",
            "title_en": "Exercise (6): Using 'Dhu' (possessor of / endowed with)",
            "goal_ur": "ذو کے بعد والے اسم کو ہمیشہ مضاف الیہ (مجرور) بنانا",
            "goal_en": "Understanding that 'Dhu' is mudaaf and governs a genitive (majroor) noun",
            "questions": [
                {
                    "prompt_ar": "هَذَا الرَّجُلُ ذُو [ ＿＿＿ ] كَثِيرٍ .",
                    "prompt_ur": "صحیح اعراب منتخب کریں:",
                    "prompt_en": "Select the correct form:",
                    "answer": "مَالٍ",
                    "options": ["مَالٍ", "مَالٌ", "مَالًا", "مَالْ"],
                    "emoji": "💰",
                    "hint_ur": "ذو کے بعد اسم مجرور (زیر/کسرة) ہوتا ہے: ذُو مَالٍ",
                    "hint_en": "The noun after 'Dhu' is majroor (takes kasrah)."
                },
                {
                    "prompt_ar": "مُحَمَّدٌ طَالِبٌ ذُو [ ＿＿＿ ] حَسَنٍ .",
                    "prompt_ur": "صحیح اعراب منتخب کریں:",
                    "prompt_en": "Select the correct form:",
                    "answer": "خُلُقٍ",
                    "options": ["خُلُقٍ", "خُلُقٌ", "خُلُقًا", "خُلُقْ"],
                    "emoji": "⭐",
                    "hint_ur": "ذُو خُلُقٍ: اچھے اخلاق والا",
                    "hint_en": "Dhu khuluqin: of noble character."
                }
            ]
        },
        {
            "num": 7,
            "title_ar": "التَّمْرِينُ (7): الأَعْدَادُ الْمُرَكَّبَةُ (11 - 19)",
            "title_ur": "مشق (7): مرکب اعداد (11 سے 19 تک) کے احکام",
            "title_en": "Exercise (7): Compound numbers (11 to 19)",
            "goal_ur": "مرکب عدد کے دونوں اجزاء کو مبنی بر فتحہ اور تمیز کو مفرد منصوب رکھنا",
            "goal_en": "Recognizing that compound numbers (11-19) are indeclinable on fathah and their noun is singular accusative",
            "questions": [
                {
                    "prompt_ar": "رَأَيْتُ فِي الْمَسْجِدِ [ ＿＿＿ ] طَالِبًا .",
                    "prompt_ur": "صحیح عدد منتخب کریں:",
                    "prompt_en": "Select the correct number:",
                    "answer": "أَحَدَ عَشَرَ",
                    "options": ["أَحَدَ عَشَرَ", "أَحَدُ عَشَرَ", "إِحْدَى عَشْرَةَ", "أَحَدِ عَشَرِ"],
                    "emoji": "🕌",
                    "hint_ur": "گیارہ مذکر کے لیے: أَحَدَ عَشَرَ (دونوں پر زبر)",
                    "hint_en": "For 11 masculine: Ahada 'ashara (both parts have fathah)."
                },
                {
                    "prompt_ar": "فِي هَذَا الْفَصْلِ [ ＿＿＿ ] كِتَابًا .",
                    "prompt_ur": "صحیح عدد منتخب کریں:",
                    "prompt_en": "Select the correct number:",
                    "answer": "تِسْعَةَ عَشَرَ",
                    "options": ["تِسْعَةَ عَشَرَ", "تِسْعُ عَشْرَةَ", "تِسْعَةُ عَشَرَ", "تِسْعَ عَشَرَ"],
                    "emoji": "📚",
                    "hint_ur": "19 مذکر کے لیے: تِسْعَةَ عَشَرَ",
                    "hint_en": "For 19 masculine: tis'ata 'ashara."
                }
            ]
        },
        {
            "num": 8,
            "title_ar": "التَّمْرِينُ (8): اسْتِعْمَالُ (غَالٍ) وَ(غَالِيَةٌ)",
            "title_ur": "مشق (8): اسم منقوص (غَالٍ) اور مؤنث (غَالِيَةٌ) کا استعمال",
            "title_en": "Exercise (8): Using 'Ghaalin' (expensive masc.) and 'Ghaaliyah' (fem.)",
            "goal_ur": "مذکر و مؤنث کے اعتبار سے غالٍ اور غالية کا درست انتخاب",
            "goal_en": "Applying 'Ghaalin' for masculine and 'Ghaaliyatun' for feminine nouns",
            "questions": [
                {
                    "prompt_ar": "هَذَا الْقَلَمُ [ ＿＿＿ ] جِدًّا .",
                    "prompt_ur": "صحیح صفت منتخب کریں:",
                    "prompt_en": "Select the correct adjective:",
                    "answer": "غَالٍ",
                    "options": ["غَالٍ", "غَالِيَةٌ", "غَالِي", "غَالِيًا"],
                    "emoji": "🖊️",
                    "hint_ur": "قلم مذکر ہے اس لیے: غَالٍ (اصل میں غَالِيٌ تھا)",
                    "hint_en": "Al-Qalam is masculine: ghaalin."
                },
                {
                    "prompt_ar": "هَذِهِ السَّاعَةُ [ ＿＿＿ ] جِدًّا .",
                    "prompt_ur": "صحیح صفت منتخب کریں:",
                    "prompt_en": "Select the correct adjective:",
                    "answer": "غَالِيَةٌ",
                    "options": ["غَالِيَةٌ", "غَالٍ", "غَالِي", "غَالِيَاتٌ"],
                    "emoji": "⌚",
                    "hint_ur": "ساعت مؤنث ہے اس لیے: غَالِيَةٌ",
                    "hint_en": "As-Saa'ah is feminine: ghaaliyah."
                }
            ]
        }
    ],

    # Unit 2 (الدرس الثاني)
    2: [
        {
            "num": 1,
            "title_ar": "التَّمْرِينُ (1): أجب عن الأسئلة الآتية",
            "title_ur": "مشق (1): سوالات کے جوابات دیں",
            "title_en": "Exercise (1): Answer the questions based on the dialogue",
            "goal_ur": "سبق کے متن کی فہم اور عربی میں جواب دینا",
            "goal_en": "Comprehension of the dialogue and answering questions in Arabic",
            "questions": [
                {
                    "prompt_ar": "مِنْ أَيْنَ هِشَامٌ؟",
                    "prompt_ur": "صحیح جواب منتخب کریں:",
                    "prompt_en": "Select the correct answer:",
                    "answer": "هُوَ مِنْ وَاشِنْطُنَ",
                    "options": ["هُوَ مِنْ وَاشِنْطُنَ", "هُوَ مِنَ الْهِنْدِ", "هُوَ مِنْ لَنْدَنَ", "هُوَ مِنَ الْيَابَانِ"],
                    "emoji": "🏛️",
                    "hint_ur": "ہشام واشنگٹن سے ہے",
                    "hint_en": "Hisham is from Washington."
                },
                {
                    "prompt_ar": "أَمُسْلِمَاتٌ بَنَاتُ هِشَامٍ؟",
                    "prompt_ur": "صحیح جواب منتخب کریں:",
                    "prompt_en": "Select the correct answer:",
                    "answer": "لَا، لَسْنَ بِمُسْلِمَاتٍ",
                    "options": ["لَا، لَسْنَ بِمُسْلِمَاتٍ", "نَعَمْ، هُنَّ مُسْلِمَاتٌ", "لَسْنَ فِي الْبَيْتِ", "هُنَّ صَغِيرَاتٌ"],
                    "emoji": "👧",
                    "hint_ur": "نہیں، وہ مسلمان نہیں ہیں",
                    "hint_en": "No, they are not Muslim."
                }
            ]
        },
        {
            "num": 2,
            "title_ar": "التَّمْرِينُ (2): تَصْرِيفُ (لَيْسَ) مَعَ الضَّمَائِرِ",
            "title_ur": "مشق (2): (لَيْسَ) کی مختلف ضمائر کے ساتھ گردان",
            "title_en": "Exercise (2): Conjugation of 'Laysa' with pronouns (laysa, laysoo, laysat, lasna...)",
            "goal_ur": "مختلف فاعل کے مطابق ليس کا درست صیغہ لانا",
            "goal_en": "Conjugating 'Laysa' accurately according to subject pronouns",
            "questions": [
                {
                    "prompt_ar": "الطُّلَّابُ [ ＿＿＿ ] فِي الْفَصْلِ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "لَيْسُوا",
                    "options": ["لَيْسُوا", "لَيْسَ", "لَيْسَتْ", "لَسْنَ"],
                    "emoji": "👨‍🎓",
                    "hint_ur": "جمع مذکر غائب کے ساتھ: لَيْسُوا",
                    "hint_en": "For 3rd person masculine plural: laysoo."
                },
                {
                    "prompt_ar": "آمِنَةُ [ ＿＿＿ ] فِي الْمَطْبَخِ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "لَيْسَتْ",
                    "options": ["لَيْسَتْ", "لَيْسَ", "لَسْنَ", "لَسْتِ"],
                    "emoji": "👩",
                    "hint_ur": "واحد مؤنث غائب کے ساتھ: لَيْسَتْ",
                    "hint_en": "For 3rd person feminine singular: laysat."
                },
                {
                    "prompt_ar": "الطَّالِبَاتُ [ ＿＿＿ ] فِي الْمَكْتَبَةِ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "لَسْنَ",
                    "options": ["لَسْنَ", "لَيْسُوا", "لَيْسَتْ", "لَسْتُمْ"],
                    "emoji": "👩‍🎓",
                    "hint_ur": "جمع مؤنث کے ساتھ: لَسْنَ",
                    "hint_en": "For feminine plural: lasna."
                },
                {
                    "prompt_ar": "أَنَا [ ＿＿＿ ] بِمُهَنْدِسٍ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "لَسْتُ",
                    "options": ["لَسْتُ", "لَيْسَ", "لَسْنَا", "لَسْتَ"],
                    "emoji": "👷",
                    "hint_ur": "متکلم کے ساتھ: لَسْتُ",
                    "hint_en": "For 1st person singular: lastu."
                }
            ]
        },
        {
            "num": 3,
            "title_ar": "التَّمْرِينُ (3): إِعْرَابُ خَبَرِ (لَيْسَ) وَدُخُولُ الْبَاءِ الزَّائِدَةِ",
            "title_ur": "مشق (3): (لَيْسَ) کی خبر کا اعراب اور باء زائدہ کا دخول",
            "title_en": "Exercise (3): Case of Khabar Laysa and the additional Baa (bi-faqeeri)",
            "goal_ur": "خبرِ لیس کو منصوب یا باء زائدہ کے ساتھ مجرور لفظاً منصوب معناً بنانا",
            "goal_en": "Understanding the predicate of Laysa with the reinforcing particle 'bi-'",
            "questions": [
                {
                    "prompt_ar": "الْمَاءُ بَارِدٌ ➔ لَيْسَ الْمَاءُ [ ＿＿＿ ] .",
                    "prompt_ur": "صحیح اعراب منتخب کریں:",
                    "prompt_en": "Select the correct form:",
                    "answer": "بِبَارِدٍ",
                    "options": ["بِبَارِدٍ", "بِبَارِدٌ", "بِبَارِدًا", "بَارِدٌ"],
                    "emoji": "💧",
                    "hint_ur": "باء کے ساتھ مجرور ہوتا ہے: بِبَارِدٍ (یا بغیر باء کے: بَارِدًا)",
                    "hint_en": "With 'bi-', it is majroor: bi-baaredin."
                },
                {
                    "prompt_ar": "حَامِدٌ فَقِيرٌ ➔ لَيْسَ حَامِدٌ [ ＿＿＿ ] .",
                    "prompt_ur": "صحیح اعراب منتخب کریں:",
                    "prompt_en": "Select the correct form:",
                    "answer": "بِفَقِيرٍ",
                    "options": ["بِفَقِيرٍ", "بِفَقِيرٌ", "بِفَقِيرًا", "فَقِيرٌ"],
                    "emoji": "🧔",
                    "hint_ur": "لیس کی خبر پر باء زائدہ: بِفَقِيرٍ",
                    "hint_en": "Khabar of laysa with baa: bi-faqeerin."
                }
            ]
        },
        {
            "num": 4,
            "title_ar": "التَّمْرِينُ (4): النَّفْيُ بِـ (لَيْسَ) فِي الْجَوَابِ",
            "title_ur": "مشق (4): نفی کے سوالات میں (لَيْسَ) کا استعمال",
            "title_en": "Exercise (4): Negative answers using 'Laysa'",
            "goal_ur": "سوال کے جواب میں لیس کے مناسب صیغے کا استعمال",
            "goal_en": "Forming negative answers accurately with Laysa",
            "questions": [
                {
                    "prompt_ar": "أَمُتَزَوِّجٌ أَنْتَ؟ ➔ لَا، [ ＿＿＿ ] بِمُتَزَوِّجٍ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "لَسْتُ",
                    "options": ["لَسْتُ", "لَيْسَ", "لَسْتَ", "لَسْنَا"],
                    "emoji": "💍",
                    "hint_ur": "جواب دینے والا کہتا ہے: لَسْتُ",
                    "hint_en": "The speaker says: lastu."
                },
                {
                    "prompt_ar": "أَجُدُدٌ أَنْتُمْ؟ ➔ لَا، [ ＿＿＿ ] بِجُدُدٍ .",
                    "prompt_ur": "خالی جگہ پُر کریں:",
                    "prompt_en": "Fill in the blank:",
                    "answer": "لَسْنَا",
                    "options": ["لَسْنَا", "لَسْتُمْ", "لَيْسُوا", "لَسْتُ"],
                    "emoji": "👥",
                    "hint_ur": "ہم کے لیے: لَسْنَا (ہم نئے نہیں ہیں)",
                    "hint_en": "For 'we': lasnaa."
                }
            ]
        }
    ]
}

print("Book 2 defined units test successfully loaded.")
