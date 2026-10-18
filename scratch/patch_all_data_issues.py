import json, sys, re, copy
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Helper to find unit
def get_unit(uid):
    for b in data['books']:
        for u in b['units']:
            if u['id'] == uid:
                return u
    return None

# ============================================================================
# 1. FIX BOOK 1 UNIT 3 (b1_u3)
# ============================================================================
u3 = get_unit('b1_u3')
if u3:
    print("Fixing b1_u3...")
    # Clean blocks: Remove Block 27 (contaminated dump)
    cleaned_blocks = []
    for i, b in enumerate(u3.get('blocks', [])):
        if i == 27:
            continue # drop contaminated dump
        cleaned_blocks.append(b)
    
    # Insert sun letters snippet (grammar_pairs) before Part B illustrated lines (which start around block 15)
    # Find where (1) النجم بعيد starts
    part_b_idx = None
    for idx, b in enumerate(cleaned_blocks):
        if 'النَّجْمُ بَعِيدٌ' in (b.get('text', '') or b.get('arabic', '')):
            part_b_idx = idx
            break
    
    snippet_block = {
        'type': 'grammar_pairs',
        'section': 'lesson',
        'title_ar': 'الْحُرُوفُ الشَّمْسِيَّةُ (نَجْمٌ ➔ النَّجْمُ)',
        'title_ur': 'حروف شمسیہ (لامِ تعریف کا مدغم ہونا)',
        'title_en': 'Sun Letters (Assimilation of Lam)',
        'emoji': '☀️',
        'arabic': 'نَجْمٌ ➔ النَّجْمُ • رَجُلٌ ➔ الرَّجُلُ • دِيكٌ ➔ الدِّيكُ • طَالِبٌ ➔ الطَّالِبُ',
        'ur': 'نَجْمٌ (تنوین کے ساتھ) ➔ النَّجْمُ (لام پر جزم نہیں، نون پر تشدید) • رَجُلٌ ➔ الرَّجُلُ',
        'en': 'najmun ➔ an-najmu (Lam assimilates into Nun, receiving shaddah) • rajulun ➔ ar-rajulu',
        'pairs': [
            {'left_ar': 'نَجْمٌ', 'right': 'النَّجْمُ', 'left_ur': 'ستارہ', 'right_ur': '(خاص) ستارہ'},
            {'left_ar': 'رَجُلٌ', 'right': 'الرَّجُلُ', 'left_ur': 'آدمی', 'right_ur': '(خاص) آدمی'},
            {'left_ar': 'دِيكٌ', 'right': 'الدِّيكُ', 'left_ur': 'مرغا', 'right_ur': '(خاص) مرغا'},
            {'left_ar': 'طَالِبٌ', 'right': 'الطَّالِبُ', 'left_ur': 'طالب علم', 'right_ur': '(خاص) طالب علم'}
        ]
    }
    
    if part_b_idx is not None:
        cleaned_blocks.insert(part_b_idx, snippet_block)
    else:
        cleaned_blocks.append(snippet_block)
    
    u3['blocks'] = cleaned_blocks

    # Reconstruct authentic curriculum_flow for Unit 3
    u3['curriculum_flow'] = [
        {
            'id': 'b1_u3_flow_nas1',
            'type': 'nasuddars',
            'item_order': 1,
            'title_ar': 'نَصُّ الدَّرْسِ (الْقِسْمُ أ — مَعْرِفَةٌ وَنَكِرَةٌ: بَيْتٌ : الْبَيْتُ)',
            'title_ur': 'سبق کا بنیادی متن (معرفہ اور نکرہ کا فرق)',
            'title_en': 'Lesson Core Text (Part A — Definite vs Indefinite)',
            'page': 15
        },
        {
            'id': 'b1_u3_flow_t1',
            'type': 'tamreen',
            'tamreen_num': 1,
            'item_order': 2,
            'title_ar': 'تَمْرِين (١): اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ',
            'title_ur': 'مشق (۱): الفاظ کے آخری اعراب کے ساتھ پڑھیں اور لکھیں',
            'title_en': 'Exercise 1: Read & Write with Final Vocalization',
            'question_count': 18,
            'page': 16
        },
        {
            'id': 'b1_u3_flow_t2',
            'type': 'tamreen',
            'tamreen_num': 2,
            'item_order': 3,
            'title_ar': 'تَمْرِين (٢): اقْرَأْ وَاكْتُبْ (قِرَاءَةُ الْجُمَلِ الْمُفِيدَةِ)',
            'title_ur': 'مشق (۲): جملوں کا صحیح تلفظ کے ساتھ مطالعہ',
            'title_en': 'Exercise 2: Read & Write Useful Sentences',
            'question_count': 10,
            'page': 16
        },
        {
            'id': 'b1_u3_flow_t3',
            'type': 'tamreen',
            'tamreen_num': 3,
            'item_order': 4,
            'title_ar': 'تَمْرِين (٣): امْلَأِ الْفَرَاغَ بِوَضْعِ الْكَلِمَةِ الْمُنَاسِبَةِ مِنَ الْقَائِمَةِ',
            'title_ur': 'مشق (۳): دیے گئے الفاظ میں سے مناسب خبر چن کر خالی جگہ پُر کریں',
            'title_en': 'Exercise 3: Fill in the Blanks from the Word Bank',
            'question_count': 6,
            'page': 16
        },
        {
            'id': 'b1_u3_flow_t4',
            'type': 'tamreen',
            'tamreen_num': 4,
            'item_order': 5,
            'title_ar': 'تَمْرِين (٤): امْلَأِ الْفَرَاغَ فِيمَا يَلِي بِوَضْعِ كَلِمَةٍ مُنَاسِبَةٍ (مُبْتَدَأ)',
            'title_ur': 'مشق (۴): مناسب مبتدأ لگا کر با معنی جملے مکمل کریں',
            'title_en': 'Exercise 4: Complete Sentences with a Suitable Subject',
            'question_count': 10,
            'page': 16
        },
        {
            'id': 'b1_u3_flow_q1',
            'type': 'qaida',
            'item_order': 6,
            'title_ar': 'قَاعِدَةٌ: الْحُرُوفُ الشَّمْسِيَّةُ (نَجْمٌ ➔ النَّجْمُ)',
            'title_ur': 'قاعدہ: حروف شمسیہ میں لامِ تعریف مدغم ہو جاتی ہے اور شمسی حرف پر تشدید آتی ہے',
            'title_en': 'Rule: Sun Letters assimilate the Lam of "Al-", giving the letter a Shaddah',
            'rule_summary_ur': 'جب اسم کے شروع میں حروف شمسیہ میں سے کوئی حرف آئے تو «ال» کی لام نہیں پڑھی جاتی بلکہ بعد والے حرف پر تشدید آتی ہے (جیسے: النَّجْمُ، الرَّجُلُ، الدِّيكُ، الطَّالِبُ)۔',
            'rule_summary_en': 'When a word begins with a Sun Letter, the Lam of the definite article is assimilated and not pronounced, and the Sun Letter receives a Shaddah (e.g. an-Najmu, ar-Rajulu, ad-Deeku, at-Taalibu).',
            'page': 18,
            'examples': [
                {'ar': 'نَجْمٌ ➔ النَّجْمُ', 'ur': 'ستارہ ➔ (خاص) ستارہ (انَّجْم)', 'en': 'A star ➔ The star (an-najmu)'},
                {'ar': 'رَجُلٌ ➔ الرَّجُلُ', 'ur': 'آدمی ➔ (خاص) آدمی (ارَّجُل)', 'en': 'A man ➔ The man (ar-rajulu)'},
                {'ar': 'دِيكٌ ➔ الدِّيكُ', 'ur': 'مرغا ➔ (خاص) مرغا (ادِّيك)', 'en': 'A rooster ➔ The rooster (ad-deeku)'},
                {'ar': 'طَالِبٌ ➔ الطَّالِبُ', 'ur': 'طالب علم ➔ (خاص) طالب علم (اطَّالِب)', 'en': 'A student ➔ The student (at-taalibu)'}
            ]
        },
        {
            'id': 'b1_u3_flow_nas2',
            'type': 'nasuddars',
            'item_order': 7,
            'title_ar': 'نَصُّ الدَّرْسِ (الْقِسْمُ ب — جُمَلُ الْحُرُوفِ الشَّمْسِيَّةِ: النَّجْمُ بَعِيدٌ)',
            'title_ur': 'سبق کا متن (حصہ ب — حروف شمسیہ کے جملے)',
            'title_en': 'Lesson Core Text (Part B — Sun Letter Sentences)',
            'page': 18
        },
        {
            'id': 'b1_u3_flow_t5',
            'type': 'tamreen',
            'tamreen_num': 5,
            'item_order': 8,
            'title_ar': 'تَمْرِين (١ — ب): اقْرَأْ وَاكْتُبْ مَعَ ضَبْطِ أَوَاخِرِ الْكَلِمَاتِ',
            'title_ur': 'مشق (۱ — ب): الفاظ کو صحیح اعراب کے ساتھ پڑھیں اور لکھیں',
            'title_en': 'Exercise 1 (Part B): Read & Write with Correct Vocalization',
            'question_count': 12,
            'page': 19
        },
        {
            'id': 'b1_u3_flow_t6',
            'type': 'tamreen',
            'tamreen_num': 6,
            'item_order': 9,
            'title_ar': 'تَمْرِين (٢ — ب): امْلَأِ الْفَرَاغَ فِيمَا يَلِي بِوَضْعِ كَلِمَةٍ مُنَاسِبَةٍ (خَيَارَاتٌ)',
            'title_ur': 'مشق (۲ — ب): خالی جگہ میں مناسب لفظ لگا کر جملہ مکمل کریں (آپشنز کے ساتھ)',
            'title_en': 'Exercise 2 (Part B): Fill in the Blanks with Options',
            'question_count': 6,
            'page': 19
        },
        {
            'id': 'b1_u3_flow_t7',
            'type': 'tamreen',
            'tamreen_num': 7,
            'item_order': 10,
            'title_ar': 'تَمْرِين (٣ — ب): اخْتَرْ كَلِمَةً مِنَ الْقَائِمَةِ (ب) تُنَاسِبُ الَّتِي فِي (أ)',
            'title_ur': 'مشق (۳ — ب): کالم (أ) کے مناسب لفظ کو کالم (ب) سے ملائیں (جوڑے بنائیں)',
            'title_en': 'Exercise 3 (Part B): Match Column (A) with Column (B)',
            'question_count': 7,
            'page': 19
        },
        {
            'id': 'b1_u3_flow_t8',
            'type': 'tamreen',
            'tamreen_num': 8,
            'item_order': 11,
            'title_ar': 'تَمْرِين (٤ — ب): جَدْوَلُ الْحُرُوفِ الشَّمْسِيَّةِ وَالْقَمَرِيَّةِ',
            'title_ur': 'مشق (۴ — ب): شمسی اور قمری حروف کی پہچان اور فرق',
            'title_en': 'Exercise 4 (Part B): Solar vs Lunar Letters Classification',
            'question_count': 14,
            'page': 20
        }
    ]

    # Reconstruct authentic questions for Unit 3
    q_list = []
    
    # Tamreen 1: 18 words vocalization (Masjidun vs Al-Masjidu, etc.)
    t1_words = [
        ('مَسْجِدٌ', 'مَسْجِدُ', 'نکرہ اسم پر تنوین آتی ہے'),
        ('الْمَسْجِدُ', 'الْمَسْجِدٌ', 'الف لام کے ساتھ تنوین نہیں آتی'),
        ('الْمَاءُ', 'الْمَاءٌ', 'الف لام کے ساتھ ضمہ آتا ہے'),
        ('مَاءٌ', 'مَاءُ', 'نکرہ اسم تنوین لیتا ہے'),
        ('الْبَيْتُ', 'الْبَيْتٌ', 'الف لام کے ساتھ تنوین گر جاتی ہے'),
        ('بَابٌ', 'بَابُ', 'نکرہ اسم تنوین لیتا ہے'),
        ('قَلَمٌ', 'قَلَمُ', 'نکرہ اسم تنوین لیتا ہے'),
        ('الْقَلَمُ', 'الْقَلَمٌ', 'معرف باللام پر تنوین ممنوع ہے'),
        ('الْكَلْبُ', 'الْكَلْبٌ', 'معرف باللام پر تنوین نہیں آتی'),
        ('كَلْبٌ', 'كَلْبُ', 'نکرہ اسم پر تنوین آتی ہے'),
        ('قَمِيصٌ', 'قَمِيصُ', 'نکرہ اسم تنوین لیتا ہے'),
        ('وَلَدٌ', 'وَلَدُ', 'نکرہ اسم تنوین لیتا ہے'),
        ('الْحَجَرُ', 'الْحَجَرٌ', 'معرف باللام پر ضمہ آتا ہے'),
        ('الْوَلَدُ', 'الْوَلَدٌ', 'معرف باللام پر ضمہ آتا ہے'),
        ('حِمَارٌ', 'حِمَارُ', 'نکرہ اسم تنوین لیتا ہے'),
        ('الْحِمَارُ', 'الْحِمَارٌ', 'معرف باللام پر تنوین نہیں آتی'),
        ('الْحِصَانُ', 'الْحِصَانٌ', 'معرف باللام پر تنوین نہیں آتی'),
        ('حِصَانٌ', 'حِصَانُ', 'نکرہ اسم تنوین لیتا ہے')
    ]
    for w_correct, w_wrong, expl in t1_words:
        q_list.append({
            'tamreen_num': 1,
            'type': 'emoji_choice',
            'prompt_ar': f'اخْتَرِ الضَّبْطَ الصَّحِيحَ لِلْكَلِمَةِ: ({w_correct})',
            'prompt_ur': 'درست اعراب والا لفظ منتخب کریں:',
            'prompt_en': 'Select the correctly vocalized word:',
            'options': [w_correct, w_wrong],
            'answer': w_correct,
            'strict_tashkeel': True,
            'explanation_ur': f'درست اعراب: {w_correct} ({expl})',
            'explanation_en': f'Correct: {w_correct}'
        })

    # Tamreen 2: 10 reading sentences
    t2_sentences = [
        ('الْمَكْتَبُ مَكْسُورٌ.', 'میز ٹوٹی ہوئی ہے۔', 'The desk is broken.'),
        ('الْمُدَرِّسُ جَدِيدٌ.', 'استاد نیا ہے۔', 'The teacher is new.'),
        ('الْقَمِيصُ وَسِخٌ.', 'قمیض میلی ہے۔', 'The shirt is dirty.'),
        ('اللَّبَنُ بَارِدٌ.', 'دودھ ٹھنڈا ہے۔', 'The milk is cold.'),
        ('الْمَسْجِدُ مَفْتُوحٌ.', 'مسجد کھلی ہے۔', 'The mosque is open.'),
        ('الْحَجَرُ كَبِيرٌ.', 'پتھر بڑا ہے۔', 'The stone is big.'),
        ('اللَّبَنُ بَارِدٌ وَالْمَاءُ حَارٌّ.', 'دودھ ٹھنڈا ہے اور پانی گرم ہے۔', 'The milk is cold and the water is hot.'),
        ('الْمُهَنْدِسُ جَالِسٌ وَالْمُدَرِّسُ وَاقِفٌ.', 'انجینئر بیٹھا ہے اور استاد کھڑا ہے۔', 'The engineer is sitting and the teacher is standing.'),
        ('الْقَمَرُ بَعِيدٌ.', 'چاند دور ہے۔', 'The moon is far.'),
        ('الْمِنْدِيلُ نَظِيفٌ.', 'رومال صاف ہے۔', 'The handkerchief is clean.')
    ]
    for s_ar, s_ur, s_en in t2_sentences:
        distractor = s_ar.replace('مَكْسُورٌ', 'مَفْتُوحٌ').replace('جَدِيدٌ', 'قَدِيمٌ').replace('بَارِدٌ', 'حَارٌّ').replace('وَسِخٌ', 'نَظِيفٌ').replace('كَبِيرٌ', 'صَغِيرٌ').replace('بَعِيدٌ', 'قَرِيبٌ')
        if distractor == s_ar: distractor = s_ar + ' خَطَأٌ'
        q_list.append({
            'tamreen_num': 2,
            'type': 'emoji_choice',
            'prompt_ar': s_ar,
            'prompt_ur': 'جملے کا صحیح ترجمہ اور مفہوم منتخب کریں:',
            'prompt_en': 'Select the correct translation and meaning:',
            'hint_ur': s_ur,
            'hint_en': s_en,
            'options': [s_ur, 'غلط ترجمہ', 'ترجمہ غیر متعلق ہے'],
            'answer': s_ur,
            'explanation_ur': f'{s_ar} — {s_ur}',
            'explanation_en': f'{s_ar} — {s_en}'
        })

    # Tamreen 3: 6 fill_blank from word bank: جَمِيلٌ، وَسِخٌ، حَارٌّ، ثَقِيلٌ، مَفْتُوحٌ، خَفِيفٌ
    t3_fill = [
        ('الْحَجَرُ ...............', 'ثَقِيلٌ', ['ثَقِيلٌ', 'خَفِيفٌ', 'حَارٌّ', 'مَفْتُوحٌ'], 'پتھر بھاری ہے۔ (الْحَجَرُ ثَقِيلٌ)'),
        ('الْقَمَرُ ...............', 'جَمِيلٌ', ['جَمِيلٌ', 'وَسِخٌ', 'حَارٌّ', 'ثَقِيلٌ'], 'چاند خوبصورت ہے۔ (الْقَمَرُ جَمِيلٌ)'),
        ('الْبَابُ ...............', 'مَفْتُوحٌ', ['مَفْتُوحٌ', 'حَارٌّ', 'ثَقِيلٌ', 'خَفِيفٌ'], 'دروازہ کھلا ہے۔ (الْبَابُ مَفْتُوحٌ)'),
        ('الْوَرَقُ ...............', 'خَفِيفٌ', ['خَفِيفٌ', 'ثَقِيلٌ', 'مَفْتُوحٌ', 'حَارٌّ'], 'کاغذ ہلکا ہے۔ (الْوَرَقُ خَفِيفٌ)'),
        ('الْمِنْدِيلُ ...............', 'وَسِخٌ', ['وَسِخٌ', 'حَارٌّ', 'ثَقِيلٌ', 'مَفْتُوحٌ'], 'رومال میلا ہے۔ (الْمِنْدِيلُ وَسِخٌ)'),
        ('اللَّبَنُ ...............', 'حَارٌّ', ['حَارٌّ', 'ثَقِيلٌ', 'خَفِيفٌ', 'مَفْتُوحٌ'], 'دودھ گرم ہے۔ (اللَّبَنُ حَارٌّ)')
    ]
    for prompt, ans, opts, expl in t3_fill:
        q_list.append({
            'tamreen_num': 3,
            'type': 'fill_blank',
            'prompt_ar': prompt,
            'prompt_ur': 'مناسب خبر منتخب کر کے خالی جگہ پُر کریں:',
            'prompt_en': 'Fill in the blank with the appropriate predicate:',
            'options': opts,
            'answer': ans,
            'explanation_ur': expl,
            'explanation_en': f'Correct answer: {ans}'
        })

    # Tamreen 4: 10 fill_blank with Mubtada
    t4_mubtada = [
        ('............... نَظِيفٌ.', 'الْقَمِيصُ', ['الْقَمِيصُ', 'الْحَجَرُ', 'الْبَابُ', 'الْمَاءُ']),
        ('............... مَكْسُورٌ.', 'الْقَلَمُ', ['الْقَلَمُ', 'الْقَمَرُ', 'اللَّبَنُ', 'الْوَلَدُ']),
        ('............... بَارِدٌ.', 'الْمَاءُ', ['الْمَاءُ', 'الْقَمِيصُ', 'الْحِمَارُ', 'الدَّفْتَرُ']),
        ('............... قَرِيبٌ.', 'الْبَيْتُ', ['الْبَيْتُ', 'الْقَمَرُ', 'النَّجْمُ', 'السَّرِيرُ']),
        ('............... بَعِيدٌ.', 'الْمَسْجِدُ', ['الْمَسْجِدُ', 'الْمِنْدِيلُ', 'الْقَلَمُ', 'الْكُرْسِيُّ']),
        ('............... وَاقِفٌ.', 'الْمُدَرِّسُ', ['الْمُدَرِّسُ', 'الْكِتَابُ', 'الْمَكْتَبُ', 'الْوَرَقُ']),
        ('............... جَالِسٌ.', 'الْوَلَدُ', ['الْوَلَدُ', 'الْبَابُ', 'الْقَمِيصُ', 'الْحَجَرُ']),
        ('............... كَبِيرٌ.', 'الْحَجَرُ', ['الْحَجَرُ', 'الْقَلَمُ', 'الْمِنْدِيلُ', 'الْوَرَقُ']),
        ('............... قَدِيمٌ.', 'الْكِتَابُ', ['الْكِتَابُ', 'اللَّبَنُ', 'الْمَاءُ', 'الْوَلَدُ']),
        ('............... جَدِيدٌ.', 'الدَّفْتَرُ', ['الدَّفْتَرُ', 'الْحِمَارُ', 'الْحَصَانُ', 'الْقَمَرُ'])
    ]
    for prompt, ans, opts in t4_mubtada:
        q_list.append({
            'tamreen_num': 4,
            'type': 'fill_blank',
            'prompt_ar': prompt,
            'prompt_ur': 'مناسب مبتدأ منتخب کر کے خالی جگہ پُر کریں:',
            'prompt_en': 'Fill in the blank with the appropriate subject:',
            'options': opts,
            'answer': ans,
            'explanation_ur': f'{ans} {prompt.replace("...............", "").strip()}',
            'explanation_en': f'Correct subject: {ans}'
        })

    # Tamreen 5: Part B - 12 words vocalization
    t5_words = [
        ('الْبَابُ', 'الْبَابٌ'), ('التَّاجِرُ', 'التَّاجِرٌ'), ('النَّجْمُ', 'النَّجْمٌ'), ('الْقَمَرُ', 'الْقَمَرٌ'),
        ('الدِّيكُ', 'الدِّيكٌ'), ('الْمَاءُ', 'الْمَاءٌ'), ('السَّرِيرُ', 'السَّرِيرٌ'), ('الْبَيْتُ', 'الْبَيْتٌ'),
        ('الْمَسْجِدُ', 'الْمَسْجِدٌ'), ('الرَّجُلُ', 'الرَّجُلٌ'), ('السُّكَّرُ', 'السُّكَّرٌ'), ('الْوَرَقُ', 'الْوَرَقٌ')
    ]
    for w_correct, w_wrong in t5_words:
        q_list.append({
            'tamreen_num': 5,
            'type': 'emoji_choice',
            'prompt_ar': f'اخْتَرِ الضَّبْطَ الصَّحِيحَ: ({w_correct})',
            'prompt_ur': 'درست اعراب منتخب کریں:',
            'prompt_en': 'Select the correct vocalization:',
            'options': [w_correct, w_wrong],
            'answer': w_correct,
            'strict_tashkeel': True,
            'explanation_ur': f'معرف باللام پر تنوین نہیں آتی: {w_correct}',
            'explanation_en': f'Correct: {w_correct}'
        })

    # Tamreen 6: Part B Exercise 2 (USER IMAGE 2!) -> 6 fill_blank with 4 options!
    t6_fill = [
        ('............... غَنِيٌّ.', 'التَّاجِرُ', ['التَّاجِرُ', 'الْقَلَمُ', 'الْحَجَرُ', 'الْبَابُ'], 'التَّاجِرُ غَنِيٌّ (تاجر مالدار ہے)'),
        ('............... حُلْوٌ.', 'السُّكَّرُ', ['السُّكَّرُ', 'الدَّفْتَرُ', 'الْمَسْجِدُ', 'السَّرِيرُ'], 'السُّكَّرُ حُلْوٌ (چینی میٹھی ہے)'),
        ('............... مَرِيضٌ.', 'الطَّالِبُ', ['الطَّالِبُ', 'الْمَاءُ', 'الْقَمَرُ', 'الْوَرَقُ'], 'الطَّالِبُ مَرِيضٌ (طالب علم بیمار ہے)'),
        ('............... لَذِيذٌ.', 'التُّفَّاحُ', ['التُّفَّاحُ', 'الْحِمَارُ', 'السَّرِيرُ', 'الدُّكَّانُ'], 'التُّفَّاحُ لَذِيذٌ (سیب لذیذ ہے)'),
        ('............... طَوِيلٌ.', 'الطَّبِيبُ', ['الطَّبِيبُ', 'الْمِنْدِيلُ', 'الدُّكَّانُ', 'الْبَيْتُ'], 'الطَّبِيبُ طَوِيلٌ (ڈاکٹر لمبا ہے)'),
        ('............... قَصِيرٌ.', 'الْمَرِيضُ', ['الْمَرِيضُ', 'النَّجْمُ', 'الْكِتَابُ', 'الْبَابُ'], 'الْمَرِيضُ قَصِيرٌ (مریض ٹھگنے قد کا ہے)')
    ]
    for prompt, ans, opts, expl in t6_fill:
        q_list.append({
            'tamreen_num': 6,
            'type': 'fill_blank',
            'prompt_ar': prompt,
            'prompt_ur': 'مناسب لفظ منتخب کر کے خالی جگہ پُر کریں:',
            'prompt_en': 'Fill in the blank with the appropriate word:',
            'options': opts,
            'answer': ans,
            'explanation_ur': expl,
            'explanation_en': f'Correct: {ans}'
        })

    # Tamreen 7: Part B Exercise 3 (USER IMAGE 2!) -> Column matching / pair_match
    pair_match_q = {
        'tamreen_num': 7,
        'type': 'pair_match',
        'prompt_ar': 'اخْتَرْ كَلِمَةً مِنَ الْقَائِمَةِ (ب) تُنَاسِبُ الْكَلِمَةَ الَّتِي فِي الْقَائِمَةِ (أ):',
        'prompt_ur': 'کالم (أ) کے مناسب لفظ کو کالم (ب) سے ملائیں (جوڑے بنائیں):',
        'prompt_en': 'Match words from Column (A) with Column (B):',
        'pairs': [
            {'left_ar': 'الطَّالِبُ', 'right': 'مَرِيضٌ', 'left_ur': 'طالب علم', 'right_ur': 'بیمار ہے'},
            {'left_ar': 'الدُّكَّانُ', 'right': 'مَفْتُوحٌ', 'left_ur': 'دکان', 'right_ur': 'کھلی ہے'},
            {'left_ar': 'التُّفَّاحُ', 'right': 'لَذِيذٌ', 'left_ur': 'سیب', 'right_ur': 'لذیذ ہے'},
            {'left_ar': 'الْمَاءُ', 'right': 'حَارٌّ', 'left_ur': 'پانی', 'right_ur': 'گرم ہے'},
            {'left_ar': 'الْحَجَرُ', 'right': 'ثَقِيلٌ', 'left_ur': 'پتھر', 'right_ur': 'بھاری ہے'},
            {'left_ar': 'الْقَلَمُ', 'right': 'مَكْسُورٌ', 'left_ur': 'قلم', 'right_ur': 'ٹوٹا ہوا ہے'}
        ],
        'answer': 'الطَّالِبُ مَرِيضٌ • الدُّكَّانُ مَفْتُوحٌ • التُّفَّاحُ لَذِيذٌ • الْمَاءُ حَارٌّ • الْحَجَرُ ثَقِيلٌ • الْقَلَمُ مَكْسُورٌ',
        'explanation_ur': 'الطَّالِبُ مَرِيضٌ • الدُّكَّانُ مَفْتُوحٌ • التُّفَّاحُ لَذِيذٌ • الْمَاءُ حَارٌّ • الْحَجَرُ ثَقِيلٌ • الْقَلَمُ مَكْسُورٌ',
        'explanation_en': 'All matched pairs correct!'
    }
    q_list.append(pair_match_q)

    # Add 6 individual matching questions for Tamreen 7
    individual_pairs = [
        ('الطَّالِبُ', 'مَرِيضٌ', ['مَرِيضٌ', 'مَفْتُوحٌ', 'لَذِيذٌ', 'مَكْسُورٌ']),
        ('الدُّكَّانُ', 'مَفْتُوحٌ', ['مَفْتُوحٌ', 'مَرِيضٌ', 'حَارٌّ', 'ثَقِيلٌ']),
        ('التُّفَّاحُ', 'لَذِيذٌ', ['لَذِيذٌ', 'مَكْسُورٌ', 'حَارٌّ', 'ثَقِيلٌ']),
        ('الْمَاءُ', 'حَارٌّ', ['حَارٌّ', 'لَذِيذٌ', 'مَفْتُوحٌ', 'مَرِيضٌ']),
        ('الْحَجَرُ', 'ثَقِيلٌ', ['ثَقِيلٌ', 'مَكْسُورٌ', 'لَذِيذٌ', 'حَارٌّ']),
        ('الْقَلَمُ', 'مَكْسُورٌ', ['مَكْسُورٌ', 'حَارٌّ', 'ثَقِيلٌ', 'مَفْتُوحٌ'])
    ]
    for m_subj, m_pred, opts in individual_pairs:
        q_list.append({
            'tamreen_num': 7,
            'type': 'emoji_choice',
            'prompt_ar': f'اخْتَرْ مَا يُنَاسِبُ الْمُبْتَدَأَ: ({m_subj})',
            'prompt_ur': f'لفظ «{m_subj}» کے مناسب خبر منتخب کریں:',
            'prompt_en': f'Select the suitable predicate for "{m_subj}":',
            'options': opts,
            'answer': m_pred,
            'explanation_ur': f'{m_subj} {m_pred}',
            'explanation_en': f'{m_subj} {m_pred}'
        })

    # Tamreen 8: 14 pairs of Sun vs Moon letters (14 questions)
    sun_moon_words = [
        ('الْأَبُ', 'قَمَرِيَّةٌ', ['قَمَرِيَّةٌ', 'شَمْسِيَّةٌ']),
        ('التَّاجِرُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ']),
        ('الثَّوْبُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ']),
        ('الْبَابُ', 'قَمَرِيَّةٌ', ['قَمَرِيَّةٌ', 'شَمْسِيَّةٌ']),
        ('الْجَنَّةُ', 'قَمَرِيَّةٌ', ['قَمَرِيَّةٌ', 'شَمْسِيَّةٌ']),
        ('الدِّيكُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ']),
        ('الذَّهَبُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ']),
        ('الْحِمَارُ', 'قَمَرِيَّةٌ', ['قَمَرِيَّةٌ', 'شَمْسِيَّةٌ']),
        ('الرَّجُلُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ']),
        ('الزَّهْرَةُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ']),
        ('السَّمَكُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ']),
        ('الشَّمْسُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ']),
        ('الْقَمَرُ', 'قَمَرِيَّةٌ', ['قَمَرِيَّةٌ', 'شَمْسِيَّةٌ']),
        ('اللَّحْمُ', 'شَمْسِيَّةٌ', ['شَمْسِيَّةٌ', 'قَمَرِيَّةٌ'])
    ]
    for word, ans, opts in sun_moon_words:
        q_list.append({
            'tamreen_num': 8,
            'type': 'emoji_choice',
            'prompt_ar': f'هَلِ اللَّامُ فِي ({word}) شَمْسِيَّةٌ أَمْ قَمَرِيَّةٌ؟',
            'prompt_ur': f'لفظ «{word}» میں لام شمسی ہے یا قمری؟',
            'prompt_en': f'Is the Lam in "{word}" Solar or Lunar?',
            'options': opts,
            'answer': ans,
            'explanation_ur': f'«{word}» کی لام {ans} ہے',
            'explanation_en': f'The Lam in "{word}" is {ans}'
        })

    u3['questions'] = q_list
    print(f"b1_u3 updated: {len(u3['blocks'])} blocks, {len(u3['curriculum_flow'])} flow items, {len(u3['questions'])} questions.")

# ============================================================================
# 2. FIX BOOK 1 UNIT 9 (b1_u9)
# ============================================================================
u9 = get_unit('b1_u9')
if u9:
    print("Fixing b1_u9...")
    for b in u9.get('blocks', []):
        if b.get('type') == 'vocab_table':
            words = b.get('words', [])
            if len(words) > 15:
                # Keep only genuine vocabulary words (first 12 words)
                b['words'] = words[:12]
                print(f"Cleaned b1_u9 vocab_table from {len(words)} to {len(b['words'])} words.")

# ============================================================================
# 3. FIX BOOK 1 UNIT 13 (b1_u13)
# ============================================================================
u13 = get_unit('b1_u13')
if u13:
    print("Fixing b1_u13...")
    for b in u13.get('blocks', []):
        if b.get('type') == 'vocab_table':
            words = b.get('words', [])
            if len(words) > 10:
                # Keep only genuine vocabulary words
                b['words'] = [w for w in words[:10] if not re.search(r'(\.{3,}|…+|\(\d+\)|حوّل|اقرأ)', w.get('ar', ''))]
                print(f"Cleaned b1_u13 vocab_table from {len(words)} to {len(b['words'])} words.")

# ============================================================================
# 4. FIX BOOK 2 UNIT 29 (b2_u29)
# ============================================================================
u29 = get_unit('b2_u29')
if u29:
    print("Fixing b2_u29...")
    for b in u29.get('blocks', []):
        if b.get('type') == 'vocab_table':
            words = b.get('words', [])
            if len(words) > 10:
                # Words 0-4 are vocabulary
                b['words'] = words[:5]
                print(f"Cleaned b2_u29 vocab_table from {len(words)} to {len(b['words'])} words.")

# Save updated JSON and JS
with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write('/**\n * Madinah Arabic Course - Master Synchronized Dataset\n */\nwindow.MADINAH_BOOKS = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

print("Successfully patched and synchronized data/madinah_books.json & js!")
