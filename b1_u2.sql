-- =====================================================
-- BOOK 1, UNIT 2: الدَّرْسُ الثَّانِي
-- =====================================================

-- 1. UNIT METADATA
INSERT INTO public.units (id, book_num, unit_num, title_ar, topic_ar, topic_en, topic_ur, emoji)
VALUES
  ('b1_u2', 1, 2, 'الدَّرْسُ الثَّانِي', 'ذٰلِكَ (اسْمُ الْإِشَارَةِ لِلْبَعِيدِ)', 'That is (ذٰلِكَ) — Distant Demonstrative', 'اسم اشارہ بعید (ذٰلِكَ: وہ) — دور کی چیزوں کے لیے', '⭐')
ON CONFLICT (id) DO UPDATE SET title_ar = EXCLUDED.title_ar, topic_ar = EXCLUDED.topic_ar, topic_en = EXCLUDED.topic_en, topic_ur = EXCLUDED.topic_ur, emoji = EXCLUDED.emoji;

-- 2. LESSON CARDS
-- Near & Distant contrast sentences feature both emojis (near big, far small)
-- Mountain emoji ⛰️ used for stone / rock (حَجَرٌ)
-- Concludes with a single comprehensive table card for الْكَلِمَاتُ الْجَدِيدَةُ
DELETE FROM public.lesson_cards WHERE unit_id = 'b1_u2';
INSERT INTO public.lesson_cards (unit_id, card_order, arabic, trans_ur, trans_en, emoji)
VALUES
  ('b1_u2', 1, 'ذَلِـــكَ', 'وہ', 'That', '👉'),
  ('b1_u2', 2, 'مَا ذٰلِكَ؟ ذٰلِكَ نَجْمٌ.', 'وہ کیا ہے؟ وہ ایک ستارہ ہے۔', 'What is that? That is a star.', '⭐'),
  ('b1_u2', 3, 'هٰذَا مَسْجِدٌ وَذٰلِكَ بَيْتٌ.', 'یہ ایک مسجد ہے اور وہ ایک گھر ہے۔', 'This is a mosque and that is a house.', '🕌 🏠'),
  ('b1_u2', 4, 'هٰذَا حِصَانٌ وَذٰلِكَ حِمَارٌ.', 'یہ ایک گھوڑا ہے اور وہ ایک گدھا ہے۔', 'This is a horse and that is a donkey.', '🐎 🐴'),
  ('b1_u2', 5, 'أَذٰلِكَ كَلْبٌ؟ لَا، ذٰلِكَ قِطٌّ.', 'کیا وہ کتا ہے؟ نہیں، وہ ایک بلی ہے۔', 'Is that a dog? No, that is a cat.', '🐈'),
  ('b1_u2', 6, 'مَا ذٰلِكَ؟ ذٰلِكَ سَرِيرٌ.', 'وہ کیا ہے؟ وہ ایک بستر ہے۔', 'What is that? That is a bed.', '🛏️'),
  ('b1_u2', 7, 'مَنْ هٰذَا وَمَنْ ذٰلِكَ؟ هٰذَا مُدَرِّسٌ وَذٰلِكَ إِمَامٌ.', 'یہ کون ہے اور وہ کون ہے؟ یہ استاد ہے اور وہ امام ہے۔', 'Who is this and who is that? This is a teacher and that is an Imam.', '🧑‍🏫 👳'),
  ('b1_u2', 8, 'مَا ذٰلِكَ؟ ذٰلِكَ حَجَرٌ.', 'وہ کیا ہے؟ وہ ایک پتھر ہے۔', 'What is that? That is a stone.', '⛰️'),
  ('b1_u2', 9, 'هٰذَا سُكَّرٌ وَذٰلِكَ لَبَنٌ.', 'یہ چینی ہے اور وہ دودھ ہے۔', 'This is sugar and that is milk.', '🍬 🥛'),
  ('b1_u2', 10, 'مَنْ ذٰلِكَ؟ ذٰلِكَ إِمَامٌ.', 'وہ کون ہے؟ وہ ایک امام ہیں۔', 'Who is that? That is an Imam.', '👳'),
  ('b1_u2', 11, 'أَذٰلِكَ قِطٌّ؟ لَا، ذٰلِكَ كَلْبٌ.', 'کیا وہ بلی ہے؟ نہیں، وہ ایک کتا ہے۔', 'Is that a cat? No, that is a dog.', '🐕'),
  ('b1_u2', 12, 'مَا هٰذَا؟ هٰذَا حَجَرٌ.', 'یہ کیا ہے؟ یہ ایک پتھر ہے۔', 'What is this? This is a stone.', '⛰️'),
  -- كَلِمَاتٌ جَدِيدَةٌ (SINGLE VOCABULARY TABLE AT LESSON END)
  ('b1_u2', 13, 'الْكَلِمَاتُ الْجَدِيدَةُ', 'نئے الفاظ', 'New Vocabulary', '🗂️');

-- 3. EXERCISE QUESTIONS (Strictly the 4 translation questions from textbook tamreen)
DELETE FROM public.questions WHERE unit_id = 'b1_u2';
INSERT INTO public.questions (id, unit_id, tamreen_num, question_order, type, prompt_ar, prompt_ur, prompt_en, answer, options, strict_tashkeel, hint_ur, hint_en, explanation_ur, explanation_en, emoji)
VALUES
  ('b1_u2_t1_q1', 'b1_u2', 1, 1, 'sentence_reading', 'اقْرَأْ وَتَرْجِمْ: هٰذَا سُكَّرٌ وَذٰلِكَ لَبَنٌ.', 'جملے کا درست ترجمہ منتخب کریں:', 'Select the correct translation:', 'یہ چینی ہے اور وہ دودھ ہے • This is sugar and that is milk', '["یہ چینی ہے اور وہ دودھ ہے • This is sugar and that is milk","وہ چینی ہے اور یہ دودھ ہے • That is sugar and this is milk","یہ پانی ہے اور وہ دودھ ہے • This is water and that is milk","یہ چینی ہے اور وہ چائے ہے • This is sugar and that is tea"]'::jsonb, TRUE, 'سُكَّرٌ (چینی) اور لَبَنٌ (دودھ)', 'Sugar and milk', 'صحیح ترجمہ: "یہ چینی ہے اور وہ دودھ ہے۔" کیونکہ هٰذَا قریب کے لیے اور ذٰلِكَ بعید کے لیے آتا ہے۔', 'Correct translation: "This is sugar and that is milk." Hatha is for near and Dhalika for distant.', '🍬 🥛'),
  ('b1_u2_t1_q2', 'b1_u2', 1, 2, 'sentence_reading', 'اقْرَأْ وَتَرْجِمْ: مَنْ ذٰلِكَ؟ ذٰلِكَ إِمَامٌ.', 'جملے کا درست ترجمہ منتخب کریں:', 'Select the correct translation:', 'وہ کون ہے؟ وہ ایک امام ہے • Who is that? That is an Imam', '["وہ کون ہے؟ وہ ایک امام ہے • Who is that? That is an Imam","یہ کون ہے؟ یہ ایک امام ہے • Who is this? This is an Imam","وہ کون ہے؟ وہ ایک استاد ہے • Who is that? That is a teacher","وہ کیا ہے؟ وہ ایک ستارہ ہے • What is that? That is a star"]'::jsonb, TRUE, 'مَنْ (کون) اور ذٰلِكَ (وہ)', 'Who is that? That is an Imam', 'صحیح ترجمہ: "وہ کون ہے؟ وہ ایک امام ہے۔" عاقل بعید کے لیے "مَنْ ذٰلِكَ" پوچھا جاتا ہے۔', 'Correct translation: "Who is that? That is an Imam." Man Dhalika is used for distant rational persons.', '👳'),
  ('b1_u2_t1_q3', 'b1_u2', 1, 3, 'sentence_reading', 'اقْرَأْ وَتَرْجِمْ: أَذٰلِكَ قِطٌّ؟ لَا، ذٰلِكَ كَلْبٌ.', 'جملے کا درست ترجمہ منتخب کریں:', 'Select the correct translation:', 'کیا وہ بلی ہے؟ نہیں، وہ کتا ہے • Is that a cat? No, that is a dog', '["کیا وہ بلی ہے؟ نہیں، وہ کتا ہے • Is that a cat? No, that is a dog","کیا یہ بلی ہے؟ نہیں، یہ کتا ہے • Is this a cat? No, this is a dog","کیا وہ کتا ہے؟ نہیں، وہ بلی ہے • Is that a dog? No, that is a cat","کیا وہ گدھا ہے؟ نہیں، وہ گھوڑا ہے • Is that a donkey? No, that is a horse"]'::jsonb, TRUE, 'قِطٌّ (بلی) اور كَلْبٌ (کتا)', 'Cat and dog', 'صحیح ترجمہ: "کیا وہ بلی ہے؟ نہیں، وہ کتا ہے۔"', 'Correct translation: "Is that a cat? No, that is a dog."', '🐕'),
  ('b1_u2_t1_q4', 'b1_u2', 1, 4, 'sentence_reading', 'اقْرَأْ وَتَرْجِمْ: مَا هٰذَا؟ هٰذَا حَجَرٌ.', 'جملے کا درست ترجمہ منتخب کریں:', 'Select the correct translation:', 'یہ کیا ہے؟ یہ ایک پتھر ہے • What is this? This is a stone', '["یہ کیا ہے؟ یہ ایک پتھر ہے • What is this? This is a stone","وہ کیا ہے؟ وہ ایک پتھر ہے • What is that? That is a stone","یہ کیا ہے؟ یہ ایک چابی ہے • What is this? This is a key","یہ کون ہے؟ یہ ایک تاجر ہے • Who is this? This is a merchant"]'::jsonb, TRUE, 'حَجَرٌ یعنی پتھر', 'Hajar means stone', 'صحیح ترجمہ: "یہ کیا ہے؟ یہ ایک پتھر ہے۔" حَجَرٌ کا مطلب پتھر ہے۔', 'Correct translation: "What is this? This is a stone." Hajar means stone.', '⛰️')
ON CONFLICT (id) DO UPDATE SET prompt_ar = EXCLUDED.prompt_ar, prompt_ur = EXCLUDED.prompt_ur, prompt_en = EXCLUDED.prompt_en, answer = EXCLUDED.answer, options = EXCLUDED.options, strict_tashkeel = EXCLUDED.strict_tashkeel, hint_ur = EXCLUDED.hint_ur, hint_en = EXCLUDED.hint_en, explanation_ur = EXCLUDED.explanation_ur, explanation_en = EXCLUDED.explanation_en, emoji = EXCLUDED.emoji;
