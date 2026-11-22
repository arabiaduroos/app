import re

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add QAMARI_ITEMS and SHAMSI_ITEMS after VOCAB_REGISTRY
target_vocab_end = """    'b1_u3': [
      { ar: 'الْقَمَرُ', ur: 'چاند', en: 'The moon', emoji: '🌕' },
      { ar: 'جَدِيدٌ', ur: 'نیا', en: 'New', emoji: '✨' },
      { ar: 'قَدِيمٌ', ur: 'پرانا', en: 'Old', emoji: '⏳' },
      { ar: 'وَسِخٌ', ur: 'میلا / گندا', en: 'Dirty', emoji: '🧺' },
      { ar: 'نَظِيفٌ', ur: 'صاف', en: 'Clean', emoji: '🧼' },
      { ar: 'حَارٌّ', ur: 'گرم', en: 'Hot', emoji: '♨️' },
      { ar: 'بَارِدٌ', ur: 'ٹھنڈا', en: 'Cold', emoji: '🧊' },
      { ar: 'صَغِيرٌ', ur: 'چھوٹا', en: 'Small', emoji: '🔹' },
      { ar: 'كَبِيرٌ', ur: 'بڑا', en: 'Big', emoji: '🔷' },
      { ar: 'مَفْتُوحٌ', ur: 'کھلا', en: 'Open', emoji: '🚪' },
      { ar: 'مَكْسُورٌ', ur: 'ٹوٹا ہوا', en: 'Broken', emoji: '💔' },
      { ar: 'ثَقِيلٌ', ur: 'بھاری', en: 'Heavy', emoji: '🏋️' },
      { ar: 'خَفِيفٌ', ur: 'ہلکا', en: 'Light', emoji: '🪶' },
      { ar: 'جَمِيلٌ', ur: 'خوبصورت', en: 'Beautiful', emoji: '🌸' },
      { ar: 'وَاقِفٌ', ur: 'کھڑا', en: 'Standing', emoji: '🧍' },
      { ar: 'جَالِسٌ', ur: 'بیٹھا', en: 'Sitting', emoji: '🪑' },
      { ar: 'حُلْوٌ', ur: 'میٹھا', en: 'Sweet', emoji: '🍬' },
      { ar: 'مَرِيضٌ', ur: 'بیمار', en: 'Sick', emoji: '🤒' },
      { ar: 'الدُّكَّانُ', ur: 'دکان', en: 'The shop', emoji: '🏪' },
      { ar: 'غَنِيٌّ', ur: 'امیر / مالدار', en: 'Rich', emoji: '💰' },
      { ar: 'طَوِيلٌ', ur: 'لمبا', en: 'Tall', emoji: '📏' },
      { ar: 'فَقِيرٌ', ur: 'غریب', en: 'Poor', emoji: '🪙' },
      { ar: 'قَصِيرٌ', ur: 'چھوٹے قد کا', en: 'Short', emoji: '📐' },
      { ar: 'التُّفَّاحُ', ur: 'سیب', en: 'The apple', emoji: '🍎' }
    ]
  };"""

replacement_vocab_end = """    'b1_u3': [
      { ar: 'الْقَمَرُ', ur: 'چاند', en: 'The moon', emoji: '🌕' },
      { ar: 'جَدِيدٌ', ur: 'نیا', en: 'New', emoji: '✨' },
      { ar: 'قَدِيمٌ', ur: 'پرانا', en: 'Old', emoji: '⏳' },
      { ar: 'وَسِخٌ', ur: 'میلا / گندا', en: 'Dirty', emoji: '🧺' },
      { ar: 'نَظِيفٌ', ur: 'صاف', en: 'Clean', emoji: '🧼' },
      { ar: 'حَارٌّ', ur: 'گرم', en: 'Hot', emoji: '♨️' },
      { ar: 'بَارِدٌ', ur: 'ٹھنڈا', en: 'Cold', emoji: '🧊' },
      { ar: 'صَغِيرٌ', ur: 'چھوٹا', en: 'Small', emoji: '🔹' },
      { ar: 'كَبِيرٌ', ur: 'بڑا', en: 'Big', emoji: '🔷' },
      { ar: 'مَفْتُوحٌ', ur: 'کھلا', en: 'Open', emoji: '🚪' },
      { ar: 'مَكْسُورٌ', ur: 'ٹوٹا ہوا', en: 'Broken', emoji: '💔' },
      { ar: 'ثَقِيلٌ', ur: 'بھاری', en: 'Heavy', emoji: '🏋️' },
      { ar: 'خَفِيفٌ', ur: 'ہلکا', en: 'Light', emoji: '🪶' },
      { ar: 'جَمِيلٌ', ur: 'خوبصورت', en: 'Beautiful', emoji: '🌸' },
      { ar: 'وَاقِفٌ', ur: 'کھڑا', en: 'Standing', emoji: '🧍' },
      { ar: 'جَالِسٌ', ur: 'بیٹھا', en: 'Sitting', emoji: '🪑' },
      { ar: 'حُلْوٌ', ur: 'میٹھا', en: 'Sweet', emoji: '🍬' },
      { ar: 'مَرِيضٌ', ur: 'بیمار', en: 'Sick', emoji: '🤒' },
      { ar: 'الدُّكَّانُ', ur: 'دکان', en: 'The shop', emoji: '🏪' },
      { ar: 'غَنِيٌّ', ur: 'امیر / مالدار', en: 'Rich', emoji: '💰' },
      { ar: 'طَوِيلٌ', ur: 'لمبا', en: 'Tall', emoji: '📏' },
      { ar: 'فَقِيرٌ', ur: 'غریب', en: 'Poor', emoji: '🪙' },
      { ar: 'قَصِيرٌ', ur: 'چھوٹے قد کا', en: 'Short', emoji: '📐' },
      { ar: 'التُّفَّاحُ', ur: 'سیب', en: 'The apple', emoji: '🍎' }
    ]
  };

  const QAMARI_ITEMS = [
    { letter: 'أ', word: 'اَلْـأَبُ', en: 'The father', ur: 'باپ', em: '👨' },
    { letter: 'ب', word: 'اَلْـبَابُ', en: 'The door', ur: 'دروازہ', em: '🚪' },
    { letter: 'ج', word: 'اَلْـجَنَّةُ', en: 'The garden', ur: 'باغ / جنت', em: '🌳' },
    { letter: 'ح', word: 'اَلْـحِمَارُ', en: 'The donkey', ur: 'گدھا', em: '🐴' },
    { letter: 'خ', word: 'اَلْـخُبْزُ', en: 'The bread', ur: 'روٹی', em: '🍞' },
    { letter: 'ع', word: 'اَلْـعَيْنُ', en: 'The eye', ur: 'آنکھ', em: '👁️' },
    { letter: 'غ', word: 'اَلْـغَدَاءُ', en: 'The lunch', ur: 'دوپہر کا کھانا', em: '🍲' },
    { letter: 'ف', word: 'اَلْـفَمُ', en: 'The mouth', ur: 'منہ', em: '👄' },
    { letter: 'ق', word: 'اَلْـقَمَرُ', en: 'The moon', ur: 'چاند', em: '🌕' },
    { letter: 'ك', word: 'اَلْـكَلْبُ', en: 'The dog', ur: 'کتا', em: '🐕' },
    { letter: 'م', word: 'اَلْـمَاءُ', en: 'The water', ur: 'پانی', em: '💧' },
    { letter: 'و', word: 'اَلْـوَلَدُ', en: 'The boy', ur: 'لڑکا', em: '👦' },
    { letter: 'هـ', word: 'اَلْـهَوَاءُ', en: 'The air', ur: 'ہوا', em: '💨' },
    { letter: 'ي', word: 'اَلْـيَدُ', en: 'The hand', ur: 'ہاتھ', em: '✋' }
  ];

  const SHAMSI_ITEMS = [
    { letter: 'ت', word: 'الـتَّاجِرُ', en: 'The merchant', ur: 'تاجر', em: '🧑‍💼' },
    { letter: 'ث', word: 'الـثَّوْبُ', en: 'The garment', ur: 'کپڑا', em: '👘' },
    { letter: 'د', word: 'الـدِّيكُ', en: 'The rooster', ur: 'مرغا', em: '🐓' },
    { letter: 'ذ', word: 'الـذَّهَبُ', en: 'The gold', ur: 'سونا', em: '💰' },
    { letter: 'ر', word: 'الـرَّجُلُ', en: 'The man', ur: 'آدمی', em: '🧔' },
    { letter: 'ز', word: 'الـزَّهْرَةُ', en: 'The flower', ur: 'پھول', em: '🌸' },
    { letter: 'س', word: 'الـسَّمَكُ', en: 'The fish', ur: 'مچھلی', em: '🐟' },
    { letter: 'ش', word: 'الـشَّمْسُ', en: 'The sun', ur: 'سورج', em: '☀️' },
    { letter: 'ص', word: 'الـصَّدْرُ', en: 'The chest', ur: 'سینہ', em: '🛡️' },
    { letter: 'ض', word: 'الـضَّيْفُ', en: 'The guest', ur: 'مہمان', em: '🤝' },
    { letter: 'ط', word: 'الـطَّالِبُ', en: 'The student', ur: 'طالب علم', em: '👨‍🎓' },
    { letter: 'ظ', word: 'الـظَّهْرُ', en: 'The back', ur: 'پیٹھ', em: '👤' },
    { letter: 'ل', word: 'الـلَّحْمُ', en: 'The meat', ur: 'گوشت', em: '🥩' },
    { letter: 'ن', word: 'الـنَّجْمُ', en: 'The star', ur: 'ستارہ', em: '⭐' }
  ];"""

if target_vocab_end in code:
    code = code.replace(target_vocab_end, replacement_vocab_end, 1)
    print("1. Added QAMARI_ITEMS and SHAMSI_ITEMS")
else:
    print("Warning: target_vocab_end not found!")

# 2. Update extractCardsFromUnit in unit.cards.forEach
target_extract = """        // If this is a separate card for an individual word already inside the vocab list,
        // do NOT add it because it is already showcased in the vocab grid card!
        const cleanAr = stripTashkeel(rawAr);
        if (vocabWordSet.has(cleanAr) && !rawAr.includes(' ') && !rawAr.includes('؟')) {
          return;
        }"""

replacement_extract = """        // Split combined Sun & Moon letters card into 2 separate cards (Moon page, Sun page)
        const cleanCardAr = stripTashkeel(rawAr);
        if (cleanCardAr.includes('الحروف القمرية') && cleanCardAr.includes('الشمسية')) {
          cardsList.push({
            id: `${c.id}_qamari`,
            arabic: 'الْحُرُوفُ الْقَمَرِيَّةُ',
            trans_ur: 'حروفِ قمریہ (لام ظاہر، ساکن پڑھی جائے گی)',
            trans_en: "Moon Letters (The 'l' sound is clearly pronounced)",
            ur: 'حروفِ قمریہ (لام ظاہر، ساکن پڑھی جائے گی)',
            en: "Moon Letters (The 'l' sound is clearly pronounced)",
            trans: "Moon Letters (clear 'l' sound) • حروفِ قمریہ",
            emoji: '🌙',
            type: 'qamari_table'
          });
          cardsList.push({
            id: `${c.id}_shamsi`,
            arabic: 'الْحُرُوفُ الشَّمْسِيَّةُ',
            trans_ur: 'حروفِ شمسیہ (لام مدغم، حرف پر تشدید کے ساتھ)',
            trans_en: "Sun Letters (The 'l' is silent and assimilates into a shaddah)",
            ur: 'حروفِ شمسیہ (لام مدغم، حرف پر تشدید کے ساتھ)',
            en: "Sun Letters (The 'l' is silent and assimilates into a shaddah)",
            trans: "Sun Letters (silent 'l' + shaddah) • حروفِ شمسیہ",
            emoji: '☀️',
            type: 'shamsi_table'
          });
          return;
        }

        // Split multi-pair transformation cards (separated by •) into individual Option C2 cards
        if (c.arabic && (c.arabic.includes('➔') || c.arabic.includes('->')) && c.arabic.includes('•')) {
          const arParts = c.arabic.split('•').map(s => s.trim()).filter(Boolean);
          const urParts = (c.trans_ur || c.ur || '').split('•').map(s => s.trim());
          const enParts = (c.trans_en || c.en || '').split('•').map(s => s.trim());
          arParts.forEach((pairAr, pIdx) => {
            const pairUr = urParts[pIdx] || '';
            const pairEn = enParts[pIdx] || '';
            const pairEmoji = getContextualEmoji(pairAr, pairUr, pairEn) || '⭐';
            cardsList.push({
              id: `${c.id}_${pIdx + 1}`,
              arabic: pairAr,
              trans_ur: pairUr,
              trans_en: pairEn,
              ur: pairUr,
              en: pairEn,
              trans: state.lang === 'ur' ? pairUr : (state.lang === 'en' ? pairEn : (pairUr && pairEn ? `${pairUr} • ${pairEn}` : (pairUr || pairEn))),
              emoji: pairEmoji,
              type: 'grammar_transform'
            });
          });
          return;
        }

        // If this is a separate card for an individual word already inside the vocab list,
        // do NOT add it because it is already showcased in the vocab grid card!
        const cleanAr = stripTashkeel(rawAr);
        if (vocabWordSet.has(cleanAr) && !rawAr.includes(' ') && !rawAr.includes('؟')) {
          return;
        }"""

if target_extract in code:
    code = code.replace(target_extract, replacement_extract, 1)
    print("2. Updated extractCardsFromUnit splitting logic")
else:
    print("Warning: target_extract not found!")

# 3. Update cleanup in renderCurrentLessonCard
target_cleanup = """    // Clean up any dynamic tables/grids previously added
    const oldPairs = cardContainer.querySelector('.grammar-pairs-grid');
    if (oldPairs) oldPairs.remove();
    const oldVocab = cardContainer.querySelector('.vocab-table-card');
    if (oldVocab) oldVocab.remove();
    const oldTransform = cardContainer.querySelector('.grammar-transform-container');
    if (oldTransform) oldTransform.remove();"""

replacement_cleanup = """    // Clean up any dynamic tables/grids previously added
    const oldPairs = cardContainer.querySelector('.grammar-pairs-grid');
    if (oldPairs) oldPairs.remove();
    const oldVocab = cardContainer.querySelector('.vocab-table-card');
    if (oldVocab) oldVocab.remove();
    const oldTransform = cardContainer.querySelector('.grammar-transform-container');
    if (oldTransform) oldTransform.remove();
    const oldLetterTable = cardContainer.querySelector('.letter-table-card');
    if (oldLetterTable) oldLetterTable.remove();"""

if target_cleanup in code:
    code = code.replace(target_cleanup, replacement_cleanup, 1)
    print("3. Updated cleanup in renderCurrentLessonCard")
else:
    print("Warning: target_cleanup not found!")

# 4. Update isTransform and add isQamari / isShamsi handling in renderCurrentLessonCard
target_render_cond = """    cardContainer.classList.remove('is-vocab-table', 'is-grammar-pairs', 'is-grammar-transform');
    const stageEl = document.getElementById('lessonStage');
    if (stageEl) stageEl.classList.toggle('has-vocab-card', isVocab);"""

replacement_render_cond = """    const isQamari = card.type === 'qamari_table' || (card.arabic && stripTashkeel(card.arabic).includes('الحروف القمرية') && !stripTashkeel(card.arabic).includes('الشمسية'));
    const isShamsi = card.type === 'shamsi_table' || (card.arabic && stripTashkeel(card.arabic).includes('الحروف الشمسية') && !stripTashkeel(card.arabic).includes('القمرية'));

    cardContainer.classList.remove('is-vocab-table', 'is-grammar-pairs', 'is-grammar-transform', 'is-letter-table');
    const stageEl = document.getElementById('lessonStage');
    if (stageEl) stageEl.classList.toggle('has-vocab-card', isVocab || isQamari || isShamsi);"""

if target_render_cond in code:
    code = code.replace(target_render_cond, replacement_render_cond, 1)
    print("4. Updated render condition flags")
else:
    print("Warning: target_render_cond not found!")

# 5. Update C2 alif-lam regex highlighting
target_c2_highlight = """      // Highlight ONLY alif-lam: "الـ" (without touching following letters like noon)
      let defArFormatted = defAr;
      if (defAr.startsWith('الْ') || defAr.startsWith('ٱلْ')) {
        defArFormatted = `<span class="gt-al">الْـ</span><span class="gt-base">${defAr.slice(3)}</span>`;
      } else if (defAr.startsWith('ال') || defAr.startsWith('ٱل')) {
        defArFormatted = `<span class="gt-al">الـ</span><span class="gt-base">${defAr.slice(2)}</span>`;
      }"""

replacement_c2_highlight = """      // Highlight ONLY alif-lam: "الـ" (without touching following letters like noon)
      let defArFormatted = defAr;
      const alMatch = defAr.match(/^([اأإٱ][\\u064B-\\u065F]?ل[\\u064B-\\u065F]?)(.*)$/);
      if (alMatch) {
        defArFormatted = `<span class="gt-al">${alMatch[1]}ـ</span><span class="gt-base">${alMatch[2]}</span>`;
      }"""

if target_c2_highlight in code:
    code = code.replace(target_c2_highlight, replacement_c2_highlight, 1)
    print("5. Updated C2 alif-lam regex highlighting")
else:
    print("Warning: target_c2_highlight not found!")

# 6. Add isQamari / isShamsi block in renderCurrentLessonCard before isVocab
target_is_vocab = """    } else if (isVocab) {"""

replacement_letter_tables = """    } else if (isQamari || isShamsi) {
      cardContainer.classList.add('is-letter-table');
      emEl.innerHTML = isQamari ? '🌙' : '☀️';
      arEl.style.display = 'none';
      transEl.style.display = 'none';

      const items = isQamari ? QAMARI_ITEMS : SHAMSI_ITEMS;
      const bannerClass = isQamari ? 'is-qamari' : 'is-shamsi';
      const letterClass = isQamari ? 'is-qamari' : 'is-shamsi';
      const alSpanClass = isQamari ? 'al-qamari' : 'al-shamsi';
      const bannerTitleAr = isQamari ? 'اَلْحُرُوفُ الْقَمَرِيَّةُ' : 'اَلْحُرُوفُ الشَّمْسِيَّةُ';
      const bannerTitleEn = isQamari ? 'Moon Letters' : 'Sun Letters';
      const bannerRuleAr = isQamari ? 'لَامٌ ظَاهِرَةٌ سَاكِنَةٌ (تُنْطَقُ اللَّامُ)' : 'لَامٌ مُدْغَمَةٌ (لَا تُنْطَقُ اللَّامُ وَتُشَدَّدُ الْحَرْفُ)';
      const bannerRuleEn = isQamari ? "Clear 'L' Sound (al-qamaru)" : "Silent 'L' with Shaddah (ash-shamsu)";
      const bannerIcon = isQamari ? '🌙' : '☀️';

      const tableCard = document.createElement('div');
      tableCard.className = 'letter-table-card';

      const banner = document.createElement('div');
      banner.className = `letter-table-banner ${bannerClass}`;
      banner.innerHTML = `
        <div class="banner-title kufi-font">
          <span>${bannerIcon}</span>
          <span>${bannerTitleAr} (${bannerTitleEn})</span>
        </div>
        <div class="banner-rule">
          <span class="banner-rule-ar kufi-font">${bannerRuleAr}</span>
          <span class="banner-rule-en">${bannerRuleEn}</span>
        </div>
      `;
      tableCard.appendChild(banner);

      const grid = document.createElement('div');
      grid.className = 'items-grid';

      items.forEach((item, idx) => {
        const row = document.createElement('div');
        row.className = `table-row ${isShamsi ? 'shamsi-row' : ''}`;

        // Format word with colored prefix
        let wordFormatted = item.word;
        if (isQamari) {
          wordFormatted = `<span class="${alSpanClass}">اَلْـ</span><span>${item.word.replace('اَلْـ', '')}</span>`;
        } else {
          wordFormatted = `<span class="${alSpanClass}">الـ</span><span>${item.word.replace('الـ', '')}</span>`;
        }

        let transEn = item.en;
        let transUr = item.ur;

        row.innerHTML = `
          <div class="row-ar-side">
            <span class="row-num">${idx + 1}</span>
            <span class="letter-tag ${letterClass}">${item.letter}</span>
            <span class="word-ar kufi-font">${wordFormatted}</span>
          </div>
          <div class="row-meaning-side">
            <span class="row-em-icon">${item.em}</span>
            <div class="meaning-text">
              <span class="en-text">${transEn}</span>
              <span class="ur-text ur-font">${transUr}</span>
            </div>
            <span class="audio-btn-sm" title="Listen">🔊</span>
          </div>
        `;

        row.addEventListener('click', (e) => {
          e.stopPropagation();
          speakArabic(item.word);
        });

        grid.appendChild(row);
      });

      tableCard.appendChild(grid);
      cardContainer.appendChild(tableCard);
      speakBtn.onclick = () => speakArabic(items.map(it => it.word).join('، '));

    } else if (isVocab) {"""

if target_is_vocab in code:
    code = code.replace(target_is_vocab, replacement_letter_tables, 1)
    print("6. Added isQamari / isShamsi rendering in renderCurrentLessonCard")
else:
    print("Warning: target_is_vocab not found!")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Finished patching app.js successfully!")
