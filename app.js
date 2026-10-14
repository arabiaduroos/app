// ============================================================================
// دروس اللغة العربية • Madinah Arabic Web App Engine
// Duolingo-style Minimalist Architecture
// Fonts: Noto Kufi Arabic (for Arabic) & Noto Nastaliq Urdu (for Urdu)
// ============================================================================

(function () {
  'use strict';

  const DATA = window.MADINAH_DATA || window.MADINAH_BOOKS || { books: [] };
  const STORAGE_KEY = 'madinah_duo_state_v4';

  const BOOK_COLORS = {
    1: { main: '#58cc02', dark: '#46a302' },
    2: { main: '#1cb0f6', dark: '#1899d6' },
    3: { main: '#ce82ff', dark: '#a559d9' }
  };

  const UI_STRINGS = {
    ur: {
      langBadge: '🇵🇰 اردو',
      brandSub: 'دُرُوسُ اللُّغَةِ الْعَرَبِيَّةِ',
      bookPill: (n) => `الكتاب ${n}`,
      bookHeroBadge: (bnum, count) => `📗 کتاب ${bnum} • کل ${count} اسباق`,
      bookProgress: (done, total, pct) => `${total} میں سے ${done} اسباق مکمل (${pct}%)`,
      unitBadge: (num) => `سبق ${num}`,
      unitReadBtn: '📖 سبق پڑھیں',
      unitExBtn: '✍️ تمارین',
      unitCompleted: 'مکمل ✅',
      readerBadge: (unum, title) => `📖 سبق ${unum}: ${title}`,
      readerCardCounter: (cur, tot) => `کارڈ ${cur} از ${tot}`,
      readerPrev: '➡️ پچھلا',
      readerNext: 'اگلا ⬅️',
      readerStartExercises: 'اب سبق کی تمارین حل کریں ✍️',
      modeCards: '🃏 بطاقات',
      modeFull: '📄 مکمل متن',
      checkBtn: 'چیک کریں',
      continueBtn: 'جاری رکھیں ⬅️',
      skipBtn: 'چھوڑیں',
      finishBtn: 'مکمل کریں ⬅️',
      peekBtnLabel: 'سبق',
      peekTitle: '📖 سبق اور ترجمہ کی مراجعہ',
      questionCounter: (badge, cur, tot) => `${badge} • سوال ${cur} از ${tot}`,
      correctTitle: 'ماشاءاللہ! بالکل درست جواب 🎉',
      wrongTitle: 'غلط جواب!',
      completeTitle: 'ماشاءاللہ! آپ نے اس سبق کی تمارین مکمل کر لیں!',
      completeEarnedXP: 'حاصل کردہ پوائنٹس',
      completeAccuracy: 'درستگی کا تناسب',
      completeMastery: 'مہارت کا درجہ',
      completeSavedTitle: 'پیشرفت محفوظ کر لی گئی!',
      completeSavedSub: 'واپس جانے کے لیے «مکمل کریں» پر کلک کریں۔'
    },
    en: {
      langBadge: '🇬🇧 English',
      brandSub: 'Madinah Arabic Course',
      bookPill: (n) => `Book ${n}`,
      bookHeroBadge: (bnum, count) => `📗 Book ${bnum} • ${count} Units`,
      bookProgress: (done, total, pct) => `${done} of ${total} units completed (${pct}%)`,
      unitBadge: (num) => `Unit ${num}`,
      unitReadBtn: '📖 Read Lesson',
      unitExBtn: '✍️ Exercises',
      unitCompleted: 'Completed ✅',
      readerBadge: (unum, title) => `📖 Unit ${unum}: ${title}`,
      readerCardCounter: (cur, tot) => `Card ${cur} of ${tot}`,
      readerPrev: '➡️ Previous',
      readerNext: 'Next ⬅️',
      readerStartExercises: 'Solve Chapter Exercises Now ✍️',
      modeCards: '🃏 Cards',
      modeFull: '📄 Full Text',
      checkBtn: 'Check',
      continueBtn: 'Continue ⬅️',
      skipBtn: 'Skip',
      finishBtn: 'Finish ⬅️',
      peekBtnLabel: 'Lesson',
      peekTitle: '📖 Lesson & Translation Reference',
      questionCounter: (badge, cur, tot) => `${badge} • Question ${cur} of ${tot}`,
      correctTitle: 'Awesome! Correct Answer 🎉',
      wrongTitle: 'Incorrect!',
      completeTitle: 'Well Done! Exercises Completed!',
      completeEarnedXP: 'XP Earned',
      completeAccuracy: 'Accuracy',
      completeMastery: 'Mastery Level',
      completeSavedTitle: 'Progress Saved!',
      completeSavedSub: 'Click "Finish" to return to the units journey.'
    },
    both: {
      langBadge: '🌐 EN + UR',
      brandSub: 'دُرُوسُ اللُّغَةِ الْعَرَبِيَّةِ • Madinah Arabic',
      bookPill: (n) => `الكتاب ${n} • Book ${n}`,
      bookHeroBadge: (bnum, count) => `📗 کتاب ${bnum} • Book ${bnum} (${count} Units)`,
      bookProgress: (done, total, pct) => `${done}/${total} مکمل (${pct}%) Completed`,
      unitBadge: (num) => `سبق ${num} • Unit ${num}`,
      unitReadBtn: '📖 سبق پڑھیں • Read',
      unitExBtn: '✍️ تمارین • Exercises',
      unitCompleted: 'مکمل ✅ Done',
      readerBadge: (unum, title) => `📖 سبق ${unum} • Unit ${unum}: ${title}`,
      readerCardCounter: (cur, tot) => `Card ${cur} of ${tot}`,
      readerPrev: '➡️ Previous • پچھلا',
      readerNext: 'Next • اگلا ⬅️',
      readerStartExercises: 'Solve Exercises Now • تمارین حل کریں ✍️',
      modeCards: '🃏 Cards • بطاقات',
      modeFull: '📄 Full • مکمل متن',
      checkBtn: 'چیک کریں • Check',
      continueBtn: 'Continue • جاری رکھیں ⬅️',
      skipBtn: 'چھوڑیں • Skip',
      finishBtn: 'Finish • مکمل کریں ⬅️',
      peekBtnLabel: 'Lesson • سبق',
      peekTitle: '📖 مراجعہ • Reference',
      questionCounter: (badge, cur, tot) => `${badge} • ${cur}/${tot}`,
      correctTitle: 'ماشاءاللہ! Correct Answer 🎉',
      wrongTitle: 'غلط جواب! • Incorrect',
      completeTitle: 'ماشاءاللہ! Well Done! تمارین مکمل!',
      completeEarnedXP: 'Points • پوائنٹس',
      completeAccuracy: 'Accuracy • درستگی',
      completeMastery: 'Mastery • مہارت',
      completeSavedTitle: 'Saved • محفوظ!',
      completeSavedSub: 'Click Finish to continue.'
    }
  };

  let state = {
    lang: 'ur', // 'ur' or 'en'
    currentBook: 1,
    currentUnitId: 'b1_u1',
    completed: {}, // unitId -> crowns (1..3)
    xp: 0,
    streak: 1,
    showTashkeel: true,
    fontScaleIndex: 0,
    darkMode: false
  };

  const FONT_SCALES = [1, 1.1, 1.22];

  // Minimal Lesson Card Reader State
  let lessonReader = {
    unit: null,
    cards: [],
    index: 0,
    mode: 'cards' // 'cards' or 'full'
  };

  // Duolingo Exercises State
  let quiz = {
    unit: null,
    questions: [],
    index: 0,
    hearts: 5,
    correctCount: 0,
    selectedOption: null,
    sbSelectedIndices: [],
    pairLeftIdx: null,
    pairRightIdx: null,
    pairMatchedCount: 0,
    answered: false
  };

  function t() {
    return UI_STRINGS[state.lang] || UI_STRINGS.ur;
  }

  function loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        state = Object.assign({}, state, parsed);
      }
    } catch (e) {
      console.warn('Could not load saved state:', e);
    }
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      console.warn('Could not save state:', e);
    }
  }

  function stripTashkeel(str) {
    if (!str) return '';
    return str.replace(/[\u064b-\u065f\u0670\u0640]/g, '').trim();
  }

  function formatAr(str) {
    if (!str) return '';
    return str; // Harakaat is ALWAYS present everywhere!
  }

  function getUnitTransTopic(unit) {
    if (!unit) return '';
    if (state.lang === 'ur') return unit.topic_ur || '';
    if (state.lang === 'en') return unit.topic_en || '';
    if (unit.topic_ur && unit.topic_en && unit.topic_ur !== unit.topic_en) {
      return `${unit.topic_ur} • ${unit.topic_en}`;
    }
    return unit.topic_ur || unit.topic_en || '';
  }

  function getBookTransTitle(book) {
    if (!book) return '';
    if (state.lang === 'ur') return book.title_ur || '';
    if (state.lang === 'en') return book.title_en || '';
    if (book.title_ur && book.title_en && book.title_ur !== book.title_en) {
      return `${book.title_ur} • ${book.title_en}`;
    }
    return book.title_ur || book.title_en || '';
  }

  // Synthesized Duolingo-style audio chimes
  let audioCtx = null;
  function playSound(type) {
    try {
      if (!audioCtx) {
        const AC = window.AudioContext || window.webkitAudioContext;
        if (AC) audioCtx = new AC();
      }
      if (!audioCtx) return;
      if (audioCtx.state === 'suspended') audioCtx.resume();

      const now = audioCtx.currentTime;
      if (type === 'correct') {
        const notes = [523.25, 659.25];
        notes.forEach((freq, idx) => {
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + idx * 0.09);
          gain.gain.setValueAtTime(0.14, now + idx * 0.09);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.09 + 0.22);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(now + idx * 0.09);
          osc.stop(now + idx * 0.09 + 0.23);
        });
      } else if (type === 'wrong') {
        const notes = [220, 185];
        notes.forEach((freq, idx) => {
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + idx * 0.11);
          gain.gain.setValueAtTime(0.15, now + idx * 0.11);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.11 + 0.22);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(now + idx * 0.11);
          osc.stop(now + idx * 0.11 + 0.23);
        });
      } else if (type === 'win') {
        const notes = [523.25, 659.25, 783.99, 1046.5];
        notes.forEach((freq, idx) => {
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + idx * 0.1);
          gain.gain.setValueAtTime(0.15, now + idx * 0.1);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.1 + 0.3);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(now + idx * 0.1);
          osc.stop(now + idx * 0.1 + 0.32);
        });
      }
    } catch (e) {
      // Ignore audio context errors
    }
  }

  // Arabic TTS
  function speakArabic(text) {
    if (!('speechSynthesis' in window) || !text) return;
    try {
      window.speechSynthesis.cancel();
      const clean = text.replace(/\[.*?\]/g, '').replace(/[•|⬅️➡️]/g, ' ').trim();
      const utter = new SpeechSynthesisUtterance(clean);
      utter.lang = 'ar-SA';
      utter.rate = 0.88;
      const voices = window.speechSynthesis.getVoices();
      const arVoice = voices.find(v => v.lang && v.lang.toLowerCase().startsWith('ar'));
      if (arVoice) utter.voice = arVoice;
      window.speechSynthesis.speak(utter);
    } catch (e) {
      // Ignore TTS errors
    }
  }

  function getBook(bookNum) {
    return DATA.books.find(b => b.book_num === Number(bookNum)) || DATA.books[0];
  }

  function findUnitById(unitId) {
    for (const b of DATA.books) {
      const u = b.units.find(x => x.id === unitId);
      if (u) return { book: b, unit: u };
    }
    const b0 = DATA.books[0];
    return { book: b0, unit: b0.units[0] };
  }

  function applyThemeAndPrefs() {
    document.body.dataset.lang = state.lang;
    document.body.classList.toggle('dark-mode', !!state.darkMode);
    document.getElementById('themeIcon').textContent = state.darkMode ? '☀️' : '🌙';
    document.documentElement.dir = (state.lang === 'en') ? 'ltr' : 'rtl';

    const scale = FONT_SCALES[state.fontScaleIndex % FONT_SCALES.length];
    document.documentElement.style.setProperty('--font-scale', String(scale));

    const colors = BOOK_COLORS[state.currentBook] || BOOK_COLORS[1];
    document.documentElement.style.setProperty('--book-accent', colors.main);
    document.documentElement.style.setProperty('--book-accent-dark', colors.dark);
  }

  function applyLocalizationStrings() {
    const L = t();
    document.getElementById('activeLangBadge').textContent = L.langBadge;
    document.getElementById('brandSubText').textContent = L.brandSub;

    [1, 2, 3].forEach(n => {
      const el = document.getElementById(`bookPillLabel${n}`);
      if (el) el.textContent = L.bookPill(n);
    });

    document.getElementById('quizPeekBtnLabel').textContent = L.peekBtnLabel;
    document.getElementById('peekLessonTitle').textContent = L.peekTitle;
    document.getElementById('lessonPrevBtn').textContent = L.readerPrev;
    document.getElementById('lessonNextBtn').textContent = L.readerNext;
    document.getElementById('lessonStartExercisesLabel').textContent = L.readerStartExercises;
    document.getElementById('readerModeCardBtn').textContent = L.modeCards;
    document.getElementById('readerModeFullBtn').textContent = L.modeFull;
  }

  function updateHeaderStats() {
    document.getElementById('statStreak').textContent = state.streak;
    document.getElementById('statXP').textContent = state.xp;

    DATA.books.forEach(b => {
      const doneInBook = b.units.filter(u => (state.completed[u.id] || 0) > 0).length;
      const el = document.getElementById(`pillCount${b.book_num}`);
      if (el) el.textContent = `${doneInBook}/${b.units.length}`;
    });

    document.querySelectorAll('#bookSwitcher .book-pill').forEach(btn => {
      btn.classList.toggle('active', Number(btn.dataset.book) === Number(state.currentBook));
    });
  }

  function selectLearnerLanguage(langCode) {
    state.lang = (langCode === 'en' || langCode === 'both') ? langCode : 'ur';
    saveState();
    playSound('correct');
    document.getElementById('splashOverlay').classList.add('hidden');
    applyThemeAndPrefs();
    applyLocalizationStrings();
    updateHeaderStats();
    renderJourneyView();
  }

  // ============================================================================
  // MAIN JOURNEY VIEW (STREAMLINED MINIMALIST UNITS GRID)
  // ============================================================================
  function renderJourneyView() {
    const book = getBook(state.currentBook);
    if (!book) return;
    const L = t();

    // 1. Book Hero Banner
    const doneCount = book.units.filter(u => (state.completed[u.id] || 0) > 0).length;
    const pct = Math.round((doneCount / Math.max(1, book.units.length)) * 100);

    document.getElementById('bookHeroBadge').textContent = L.bookHeroBadge(book.book_num, book.units.length);
    document.getElementById('bookHeroTitle').textContent = formatAr(book.title_ar);
    document.getElementById('bookHeroDesc').textContent = getBookTransTitle(book);
    document.getElementById('bookProgressCount').textContent = L.bookProgress(doneCount, book.units.length, pct);
    document.getElementById('bookProgressPercent').textContent = `${pct}%`;
    document.getElementById('bookProgressFill').style.width = `${pct}%`;

    // 2. Units Grid
    const grid = document.getElementById('journeyUnitsGrid');
    grid.innerHTML = '';

    book.units.forEach(unit => {
      const card = document.createElement('div');
      const crowns = state.completed[unit.id] || 0;
      card.className = 'journey-unit-card' + (crowns > 0 ? ' completed' : '');

      const transTopic = getUnitTransTopic(unit);

      card.innerHTML = `
        <div>
          <div class="unit-card-header">
            <span class="unit-card-em">${unit.emoji}</span>
            <span class="unit-card-badge">${crowns > 0 ? `👑 ${crowns}` : L.unitBadge(unit.unit_num)}</span>
          </div>
          <div class="unit-card-body">
            <h3 class="unit-card-title ar-font">${formatAr(unit.title_ar)}</h3>
            <p class="unit-card-sub">${transTopic}</p>
          </div>
        </div>
        <div class="unit-card-actions">
          <button class="duo-btn duo-btn-outline unit-read-btn">${L.unitReadBtn}</button>
          <button class="duo-btn duo-btn-green unit-ex-btn">${L.unitExBtn}</button>
        </div>
      `;

      card.querySelector('.unit-read-btn').addEventListener('click', () => {
        openLessonCardReader(unit);
      });

      card.querySelector('.unit-ex-btn').addEventListener('click', () => {
        openTamreenSelector(unit);
      });

      grid.appendChild(card);
    });
  }

  // ============================================================================
  // MINIMAL LESSON CARD READER (STYLED EXACTLY LIKE QUESTION CARDS!)
  // ============================================================================
  function isIdenticalToAr(s, ar) {
    if (!s || !ar) return false;
    const cleanS = stripTashkeel(s).replace(/[\s\.\,\?\!\:\-\—\(\)]+/g, '');
    const cleanAr = stripTashkeel(ar).replace(/[\s\.\,\?\!\:\-\—\(\)]+/g, '');
    return cleanS === cleanAr || s.trim() === ar.trim();
  }

  function getValidUr(ur, ar) {
    if (!ur) return '';
    const trimmed = String(ur).trim();
    if (!trimmed || isIdenticalToAr(trimmed, ar)) return '';
    return trimmed;
  }

  function getValidEn(en, ar) {
    if (!en) return '';
    const trimmed = String(en).trim();
    if (!trimmed) return '';
    // English translation must contain Latin letters and cannot match the Arabic source
    if (!/[a-zA-Z]/.test(trimmed)) return '';
    if (isIdenticalToAr(trimmed, ar)) return '';
    return trimmed;
  }

  function splitLongCard(rawAr, rawUr, rawEn, speaker, emoji) {
    function makeCard(a, u, e) {
      let aClean = (a || '').trim();
      if (speaker && !aClean.startsWith(speaker)) {
        aClean = `${speaker}: ${aClean}`;
      }
      const validU = getValidUr(u, aClean);
      const validE = getValidEn(e, aClean);
      let t = '';
      if (state.lang === 'ur') t = validU;
      else if (state.lang === 'en') t = validE;
      else t = validU && validE ? `${validU} • ${validE}` : (validU || validE);

      return {
        emoji: emoji || '📖',
        arabic: aClean,
        ur: validU,
        en: validE,
        trans: t
      };
    }

    const arClean = (rawAr || '').trim();
    const urClean = (rawUr || '').trim();
    const enClean = (rawEn || '').trim();

    // If already compact, keep as single card
    if (arClean.length <= 80) {
      return [makeCard(arClean, urClean, enClean)];
    }

    // Strategy 1: Split at ellipsis '…' or '...'
    if (arClean.includes('…') || arClean.includes('...')) {
      const partsAr = arClean.split(/[…|\.{3}]/);
      if (partsAr.length >= 2 && partsAr[0].trim().length >= 15 && partsAr[1].trim().length >= 15) {
        const partsUr = urClean ? urClean.split(/[…|\.{3}]/) : [];
        const partsEn = enClean ? enClean.split(/[…|\.{3}]/) : [];
        const p1Ar = partsAr[0].trim().replace(/\.+$/, '') + '.';
        const p1Ur = partsUr.length >= 1 ? partsUr[0].trim().replace(/\.+$/, '') + '.' : urClean;
        const p1En = partsEn.length >= 1 ? partsEn[0].trim().replace(/\.+$/, '') + '.' : enClean;
        const p2Ar = partsAr.slice(1).join('…').trim();
        const p2Ur = partsUr.length >= 2 ? partsUr.slice(1).join('...').trim() : '';
        const p2En = partsEn.length >= 2 ? partsEn.slice(1).join('...').trim() : '';
        return [makeCard(p1Ar, p1Ur, p1En), ...splitLongCard(p2Ar, p2Ur, p2En, speaker, emoji)];
      }
    }

    // Strategy 2: Split at first question mark followed by another clause
    if (arClean.includes('؟') && arClean.length > 80) {
      const qIdx = arClean.indexOf('؟');
      if (qIdx >= 18 && qIdx <= arClean.length - 20) {
        const p1Ar = arClean.substring(0, qIdx + 1).trim();
        const restAr = arClean.substring(qIdx + 1).trim();

        let urIdx = urClean.indexOf('؟');
        if (urIdx === -1) urIdx = urClean.indexOf('?');
        let p1Ur = urClean, p2Ur = '';
        if (urIdx >= 10 && urIdx <= urClean.length - 10) {
          p1Ur = urClean.substring(0, urIdx + 1).trim();
          p2Ur = urClean.substring(urIdx + 1).trim();
        }

        let enIdx = enClean.indexOf('?');
        if (enIdx === -1) enIdx = enClean.indexOf('؟');
        let p1En = enClean, p2En = '';
        if (enIdx >= 10 && enIdx <= enClean.length - 10) {
          p1En = enClean.substring(0, enIdx + 1).trim();
          p2En = enClean.substring(enIdx + 1).trim();
        }

        return [makeCard(p1Ar, p1Ur, p1En), ...splitLongCard(restAr, p2Ur, p2En, speaker, emoji)];
      }
    }

    return [makeCard(arClean, urClean, enClean)];
  }

  const AR_EMOJI_RULES = [
    [/(طبيب|طبيبة|doctor|ڈاکٹر)/i, '👨‍⚕️'],
    [/(ممرض|ممرضة|nurse|نرس)/i, '👩‍⚕️'],
    [/(مدرس|معلم|استاذ|أستاذ|teacher|استاد)/i, '🧑‍🏫'],
    [/(طالب|طالبة|تلميذ|student|طالب علم)/i, '👨‍🎓'],
    [/(ولد|صبي|boy|لڑکا)/i, '👦'],
    [/(بنت|فتاة|girl|لڑکی)/i, '👧'],
    [/(رجل|man|آدمی)/i, '🧔'],
    [/(امرأة|نساء|woman|عورت)/i, '👩'],
    [/(تاجر|merchant|تاجر)/i, '👳'],
    [/(مهندس|engineer|انجینئر)/i, '👷'],
    [/(إمام|امام|imam|امام)/i, '👳'],
    [/(مدير|principal|director|پرنسپل)/i, '👨‍💼'],
    [/(مريض|sick|patient|بیمار)/i, '🤒'],
    [/(أب|اب|والد|father|باپ)/i, '👨'],
    [/(أم|ام|والدة|mother|ماں)/i, '👩'],
    [/(أخ|اخ|brother|بھائی)/i, '👦'],
    [/(أخت|اخت|sister|بہن)/i, '👧'],
    [/(ابن|أبناء|son|بیٹا)/i, '👦'],
    [/(جد|جدة|grandfather|دادا)/i, '👴'],
    [/(حاج|حجاج|pilgrim|حاجی)/i, '🕋'],
    [/(ضيف|ضيوف|guest|مہمان)/i, '👥'],
    [/(طفل|طفلة|baby|child|بچہ)/i, '👶'],
    [/(كلب|كلاب|dog|کتا)/i, '🐕'],
    [/(قط|قطة|هرة|cat|بلی)/i, '🐈'],
    [/(حمار|حمير|donkey|گدھا)/i, '🐴'],
    [/(حصان|خيل|horse|گھوڑا)/i, '🐎'],
    [/(جمل|ناقة|إبل|camel|اونٹ)/i, '🐪'],
    [/(ديك|rooster|مرغا)/i, '🐓'],
    [/(دجاجة|chicken|hen|مرغی)/i, '🐔'],
    [/(بقرة|بقر|cow|گائے)/i, '🐄'],
    [/(بطة|duck|بطخ)/i, '🦆'],
    [/(سمك|سمكة|fish|مچھلی)/i, '🐟'],
    [/(عصفور|طائر|طيور|bird|پرندہ)/i, '🐦'],
    [/(فيل|elephant|ہاتھی)/i, '🐘'],
    [/(أسد|اسد|lion|شیر)/i, '🦁'],
    [/(غنم|شاة|خروف|sheep|بھیڑ)/i, '🐑'],
    [/(بيت|منزل|دار|house|گھر)/i, '🏠'],
    [/(مسجد|جامع|mosque|مسجد)/i, '🕌'],
    [/(كعبة|kaaba|کعبہ)/i, '🕋'],
    [/(باب|door|دروازہ)/i, '🚪'],
    [/(مفتاح|key|چابی)/i, '🔑'],
    [/(قلم|pen|قلم)/i, '🖊️'],
    [/(دفتر|كراسة|notebook|کاپی)/i, '📓'],
    [/(كتاب|مصحف|book|کتاب)/i, '📖'],
    [/(مكتب|طاولة|desk|table|میز)/i, '🗄️'],
    [/(سرير|فراش|bed|بستر)/i, '🛏️'],
    [/(كرسي|chair|کرسی)/i, '🪑'],
    [/(قميص|ثوب|shirt|قمیض)/i, '👕'],
    [/(منديل|handkerchief|رومال)/i, '🧣'],
    [/(ساعة|watch|clock|گھڑی)/i, '⌚'],
    [/(نظارة|glasses|عینک)/i, '👓'],
    [/(حقيبة|شنطة|bag|بستہ)/i, '🎒'],
    [/(حذاء|shoes|جوتا)/i, '👞'],
    [/(صندوق|box|ڈبہ)/i, '📦'],
    [/(تلفاز|تلفزيون|tv)/i, '📺'],
    [/(هاتف|جوال|phone|فون)/i, '📱'],
    [/(مدرسة|school|اسکول)/i, '🏫'],
    [/(جامعة|كلية|university|یونیورسٹی)/i, '🏛️'],
    [/(فصل|صف|classroom|کلاس)/i, '🏫'],
    [/(غرفة|حجرة|room|کمرہ)/i, '🛋️'],
    [/(مطبخ|kitchen|باورچی خانہ)/i, '🍳'],
    [/(حمام|مرحاض|bathroom|غسل خانہ)/i, '🚿'],
    [/(دكان|سوق|متجر|shop|market|دکان|بازار)/i, '🏪'],
    [/(مستشفى|hospital|ہسپتال)/i, '🏥'],
    [/(مطار|airport|ہوائی اڈا)/i, '✈️'],
    [/(سيارة|car|گاڑی)/i, '🚗'],
    [/(دراجة|bicycle|سائیکل)/i, '🚲'],
    [/(حافلة|باص|bus|بس)/i, '🚌'],
    [/(طائرة|plane|جہاز)/i, '✈️'],
    [/(قطار|train|ٹرین)/i, '🚆'],
    [/(سفينة|قارب|ship|boat|کشتی)/i, '🚢'],
    [/(طريق|شارع|road|street|سڑک)/i, '🛣️'],
    [/(ماء|water|پانی)/i, '💧'],
    [/(لبن|حليب|milk|دودھ)/i, '🥛'],
    [/(سكر|sugar|چینی)/i, '🍬'],
    [/(شاي|tea|چائے)/i, '🍵'],
    [/(قهوة|coffee|قہوہ)/i, '☕'],
    [/(عصير|juice|شربت)/i, '🧃'],
    [/(خبز|bread|روٹی)/i, '🍞'],
    [/(لحم|meat|گوشت)/i, '🥩'],
    [/(تفاح|apple|سیب)/i, '🍎'],
    [/(عنب|grapes|انگور)/i, '🍇'],
    [/(موز|banana|کیلا)/i, '🍌'],
    [/(تمر|dates|کھجور)/i, '🌴'],
    [/(طعام|أكل|food|کھانا)/i, '🍽️'],
    [/(نجم|نجوم|star|ستارہ)/i, '⭐'],
    [/(قمر|هلال|moon|چاند)/i, '🌙'],
    [/(شمس|sun|سورج)/i, '☀️'],
    [/(سماء|sky|آسمان)/i, '🌌'],
    [/(حجر|صخر|stone|پتھر)/i, '🏔️'],
    [/(ورق|ورقة|paper|کاغذ)/i, '📄'],
    [/(شجر|شجرة|tree|درخت)/i, '🌳'],
    [/(زهرة|وردة|flower|پھول)/i, '🌸'],
    [/(مطر|rain|بارش)/i, '🌧️'],
    [/(بحر|sea|سمندر)/i, '🌊'],
    [/(جبل|mountain|پہاڑ)/i, '🏔️'],
    [/(يابان|japan|جاپان)/i, '🇯🇵'],
    [/(صين|china|چین)/i, '🇨🇳'],
    [/(هند|india|ہند)/i, '🇮🇳'],
    [/(فلبين|philippines|فلپائن)/i, '🇵🇭'],
    [/(مصر|egypt|مصر)/i, '🇪🇬'],
    [/(مكة|مدينة|سعودية|saudi|مکہ|مدینہ)/i, '🕋'],
    [/(ذهب|خرج|مشى|walk|went|نکلا|گیا)/i, '🚶'],
    [/(رجع|عاد|return|واپس)/i, '🔙'],
    [/(جلس|جالس|sit|sitting|بیٹھا)/i, '🪑'],
    [/(قام|واقف|stand|standing|کھڑا)/i, '🧍'],
    [/(صلى|صلاة|pray|نماز)/i, '🕌']
  ];

  function getContextualEmoji(arText, urText, enText) {
    const combined = (stripTashkeel(arText || '') + ' ' + (urText || '') + ' ' + (enText || '')).toLowerCase();
    for (let i = 0; i < AR_EMOJI_RULES.length; i++) {
      if (AR_EMOJI_RULES[i][0].test(combined)) {
        return AR_EMOJI_RULES[i][1];
      }
    }
    return null;
  }

  function sanitizeEmoji(em) {
    if (!em) return null;
    return String(em).replace(/\u{1FACF}/gu, '🐴').replace(/🫏/g, '🐴');
  }

  function extractCardsFromUnit(unit) {
    const cards = [];

    (unit.blocks || []).forEach(b => {
      // STRICT FILTER: Never include exercises in the lesson reading cards!
      const sec = b.section || 'lesson';
      const bt = b.type;
      const rawText = (b.text || '').trim();

      if (sec === 'exercises' || bt === 'exercise_line') return;
      if (/^(تمارين|تمرين|التدريبات|اقرأ واكتب)/.test(rawText)) return;

      const rawUr = (b.ur || '').trim();
      const rawEn = (b.en || '').trim();
      const validUr = getValidUr(rawUr, rawText);
      const validEn = getValidEn(rawEn, rawText);
      let transTxt = '';
      if (state.lang === 'ur') transTxt = validUr;
      else if (state.lang === 'en') transTxt = validEn;
      else transTxt = validUr && validEn ? `${validUr} • ${validEn}` : (validUr || validEn);

      // Only set near/far emojis if BOTH are genuinely defined on the block!
      const hasNearFar = Boolean(b.near_emoji && b.far_emoji);
      const nearEm = hasNearFar ? sanitizeEmoji(b.near_emoji) : null;
      const farEm = hasNearFar ? sanitizeEmoji(b.far_emoji) : null;

      const rawBlockEmoji = sanitizeEmoji(b.emoji);
      const isGenericBook = (rawBlockEmoji === '📖' || rawBlockEmoji === '📚');
      const talkingAboutBook = /(كتاب|دفتر|مصحف|book|کتاب)/i.test(stripTashkeel(rawText) + ' ' + validUr + ' ' + validEn);

      let resolvedEmoji = rawBlockEmoji;
      if (!resolvedEmoji || (isGenericBook && !talkingAboutBook)) {
        resolvedEmoji = getContextualEmoji(rawText, validUr, validEn) || (b.speaker_emoji ? sanitizeEmoji(b.speaker_emoji) : null) || '💬';
      }

      if (bt === 'grammar_pairs') {
        cards.push({
          type: 'grammar_pairs',
          emoji: sanitizeEmoji(b.emoji) || '⚖️',
          arabic: rawText,
          ur: validUr,
          en: validEn,
          pairs: b.pairs || []
        });
      } else if (bt === 'vocab_table' && Array.isArray(b.words)) {
        const words = b.words;
        const CHUNK_SIZE = 16;
        for (let i = 0; i < words.length; i += CHUNK_SIZE) {
          const chunk = words.slice(i, i + CHUNK_SIZE);
          const partLabel = words.length > CHUNK_SIZE ? ` (${i + 1}-${i + chunk.length})` : '';
          cards.push({
            type: 'vocab_table',
            emoji: '🗂️',
            arabic: b.title_ar || 'الْكَلِمَاتُ الْجَدِيدَةُ',
            title_ar: (b.title_ar || 'الْكَلِمَاتُ الْجَدِيدَةُ') + partLabel,
            title_ur: (b.title_ur || 'نئے الفاظ') + partLabel,
            title_en: (b.title_en || 'New Vocabulary') + partLabel,
            words: chunk
          });
        }
      } else if (bt === 'emoji_grid' && Array.isArray(b.cards)) {
        b.cards.forEach(c => {
          const cText = (c.text || '').trim();
          const cValidUr = getValidUr(c.ur, cText);
          const cValidEn = getValidEn(c.en, cText);
          const cEmoji = sanitizeEmoji(c.emoji) || getContextualEmoji(cText, cValidUr, cValidEn) || '💬';
          cards.push({
            emoji: cEmoji,
            arabic: cText,
            ur: cValidUr,
            en: cValidEn,
            trans: state.lang === 'ur' ? cValidUr : (state.lang === 'en' ? cValidEn : (cValidUr && cValidEn ? `${cValidUr} • ${cValidEn}` : (cValidUr || cValidEn)))
          });
        });
      } else if ((bt === 'illustrated_line' || bt === 'text') && /\(\d+\)/.test(rawText)) {
        // Split numbered sentences into individual cards
        const rawItems = rawText.split(/(?=\(\d+\))/).map(s => s.trim()).filter(Boolean);
        if (rawItems.length > 1) {
          const urItems = rawUr.split(/(?=\([۱-۹\d]+\)|\(\d+\))/).map(s => s.trim()).filter(Boolean);
          const enItems = rawEn.split(/(?=\(\d+\))/).map(s => s.trim()).filter(Boolean);
          rawItems.forEach((subAr, sIdx) => {
            const subUr = getValidUr((urItems[sIdx] || '').replace(/[•\s]+$/, ''), subAr);
            const subEn = getValidEn((enItems[sIdx] || '').replace(/[•\s]+$/, ''), subAr);
            const lineEmoji = getContextualEmoji(subAr, subUr, subEn) || resolvedEmoji || '💬';
            const cardObj = {
              emoji: lineEmoji,
              arabic: subAr.replace(/[•\s]+$/, ''),
              ur: subUr,
              en: subEn,
              trans: state.lang === 'ur' ? subUr : (state.lang === 'en' ? subEn : (subUr && subEn ? `${subUr} • ${subEn}` : (subUr || subEn)))
            };
            if (hasNearFar && nearEm && farEm) {
              cardObj.near_emoji = nearEm;
              cardObj.far_emoji = farEm;
            }
            cards.push(cardObj);
          });
        } else {
          const splitItems = splitLongCard(rawText, validUr, validEn, '', resolvedEmoji);
          splitItems.forEach(item => {
            if (hasNearFar && nearEm && farEm) {
              item.near_emoji = nearEm;
              item.far_emoji = farEm;
            }
          });
          cards.push(...splitItems);
        }
      } else if (bt === 'illustrated_line') {
        const splitItems = splitLongCard(rawText, validUr, validEn, '', resolvedEmoji);
        splitItems.forEach(item => {
          if (hasNearFar && nearEm && farEm) {
            item.near_emoji = nearEm;
            item.far_emoji = farEm;
          }
        });
        cards.push(...splitItems);
      } else if (bt === 'dialogue') {
        const dlgEmoji = sanitizeEmoji(b.speaker_emoji) || getContextualEmoji(b.text, validUr, validEn) || '🗣️';
        const splitItems = splitLongCard(b.text, validUr, validEn, b.speaker, dlgEmoji);
        cards.push(...splitItems);
      } else if (bt === 'section_header') {
        if (!/^(تمارين|تمرين)/.test(rawText)) {
          cards.push({
            emoji: sanitizeEmoji(b.emoji) || '📌',
            arabic: rawText,
            ur: validUr,
            en: validEn,
            trans: transTxt
          });
        }
      } else if ((bt === 'table_row' || bt === 'vocab_row') && Array.isArray(b.cells)) {
        cards.push({
          emoji: sanitizeEmoji(b.emoji) || '🔹',
          arabic: b.cells.join(' • '),
          ur: validUr,
          en: validEn,
          trans: transTxt
        });
      } else if (bt === 'text' && rawText && !/^[=\-•\s\(\)]+$/.test(rawText)) {
        const splitItems = splitLongCard(rawText, validUr, validEn, '', resolvedEmoji);
        cards.push(...splitItems);
      }
    });

    if (cards.length === 0) {
      cards.push({
        emoji: '📖',
        arabic: unit.title_ar,
        ur: unit.topic_ur || '',
        en: unit.topic_en || '',
        trans: getUnitTransTopic(unit)
      });
    }

    return cards;
  }

  function openLessonCardReader(unit) {
    lessonReader.unit = unit;
    lessonReader.cards = extractCardsFromUnit(unit);
    lessonReader.index = 0;
    lessonReader.mode = 'cards';

    const L = t();
    document.getElementById('readerUnitBadge').textContent = L.readerBadge(unit.unit_num, formatAr(unit.title_ar));
    document.getElementById('lessonReaderModal').classList.remove('hidden');

    setReaderMode('cards');
    renderCurrentLessonCard();
  }

  function closeLessonCardReader() {
    document.getElementById('lessonReaderModal').classList.add('hidden');
  }

  function setReaderMode(mode) {
    lessonReader.mode = mode;
    const isCard = mode === 'cards';
    document.getElementById('readerModeCardBtn').classList.toggle('active', isCard);
    document.getElementById('readerModeFullBtn').classList.toggle('active', !isCard);
    document.getElementById('lessonCardViewport').classList.toggle('hidden', !isCard);
    document.getElementById('lessonFullScroll').classList.toggle('hidden', isCard);

    if (!isCard) {
      renderLessonFullText();
    }
  }

  function renderCurrentLessonCard() {
    const L = t();
    const total = lessonReader.cards.length;
    const cur = lessonReader.index;
    const card = lessonReader.cards[cur];

    // Progress bar and counter
    const pct = Math.round(((cur + 1) / Math.max(1, total)) * 100);
    document.getElementById('readerProgressFill').style.width = `${pct}%`;
    document.getElementById('readerCardCounter').textContent = L.readerCardCounter(cur + 1, total);

    const cardContainer = document.getElementById('lessonPageCard');
    const emEl = document.getElementById('lessonCardEmoji');
    const arEl = document.getElementById('lessonCardArabic');
    const transEl = document.getElementById('lessonCardTrans');
    const speakBtn = document.getElementById('lessonCardSpeakBtn');

    // Clean up any dynamic tables/grids previously added
    const oldPairs = cardContainer.querySelector('.grammar-pairs-grid');
    if (oldPairs) oldPairs.remove();
    const oldVocab = cardContainer.querySelector('.vocab-table-card');
    if (oldVocab) oldVocab.remove();

    arEl.style.display = 'block';
    transEl.style.display = 'block';
    arEl.className = 'lesson-card-arabic ar-font';

    if (card.type === 'grammar_pairs') {
      emEl.innerHTML = card.emoji || '⚖️';
      arEl.style.display = 'none';
      transEl.style.display = 'none';

      const grid = document.createElement('div');
      grid.className = 'grammar-pairs-grid';
      (card.pairs || []).forEach(p => {
        const row = document.createElement('div');
        row.className = 'grammar-pair-card';
        let indefTrans = p.ur_indef || '';
        let defTrans = p.ur_def || '';
        if (state.lang === 'en') {
          indefTrans = p.en_indef || '';
          defTrans = p.en_def || '';
        } else if (state.lang === 'both') {
          indefTrans = `${p.ur_indef || ''} • ${p.en_indef || ''}`;
          defTrans = `${p.ur_def || ''} • ${p.en_def || ''}`;
        }

        row.innerHTML = `
          <div class="grammar-pair-side">
            <span class="pair-ar ar-font preserve-tashkeel">${p.indef}</span>
            <span class="pair-trans">${indefTrans}</span>
          </div>
          <span class="grammar-arrow">➔</span>
          <div class="grammar-pair-side">
            <span class="pair-ar ar-font preserve-tashkeel">${p.def}</span>
            <span class="pair-trans">${defTrans}</span>
          </div>
        `;
        row.addEventListener('click', () => speakArabic(`${p.indef} ${p.def}`));
        grid.appendChild(row);
      });
      cardContainer.appendChild(grid);
      speakBtn.onclick = () => speakArabic(card.arabic);

    } else if (card.type === 'vocab_table') {
      emEl.innerHTML = card.emoji || '🗂️';
      arEl.style.display = 'none';
      transEl.style.display = 'none';

      const vCard = document.createElement('div');
      vCard.className = 'vocab-table-card';
      const vTitle = state.lang === 'ur' ? card.title_ur : (state.lang === 'en' ? card.title_en : `${card.title_ur} • ${card.title_en}`);
      vCard.innerHTML = `<div class="vocab-table-title">${card.title_ar} — ${vTitle}</div>`;

      const grid = document.createElement('div');
      grid.className = 'vocab-table-grid';
      (card.words || []).forEach(w => {
        const cell = document.createElement('div');
        cell.className = 'vocab-cell';
        let meaning = w.ur || '';
        if (state.lang === 'en') meaning = w.en || '';
        else if (state.lang === 'both') meaning = `${w.ur || ''} • ${w.en || ''}`;

        cell.innerHTML = `
          <span class="vocab-cell-ar ar-font">${formatAr(w.ar)}</span>
          <span class="vocab-cell-meaning">${meaning}</span>
        `;
        cell.addEventListener('click', () => speakArabic(w.ar));
        grid.appendChild(cell);
      });
      vCard.appendChild(grid);
      cardContainer.appendChild(vCard);
      speakBtn.onclick = () => speakArabic((card.words || []).map(w => w.ar).join(' '));

    } else {
      // Standard Card
      if (card.near_emoji && card.far_emoji) {
        emEl.innerHTML = `
          <div class="near-far-emojis">
            <div class="em-item-wrap">
              <span class="em-near">${card.near_emoji}</span>
              <span class="em-tag near">هٰذَا (Near)</span>
            </div>
            <span class="em-arrow">➔</span>
            <div class="em-item-wrap">
              <span class="em-far">${card.far_emoji}</span>
              <span class="em-tag far">ذٰلِكَ (Far)</span>
            </div>
          </div>
        `;
      } else {
        emEl.textContent = card.emoji || '💬';
      }

      arEl.textContent = formatAr(card.arabic);
      const arLen = (card.arabic || '').length;
      if (arLen > 90) arEl.classList.add('text-long');
      else if (arLen > 50) arEl.classList.add('text-medium');

      if (state.lang === 'both') {
        const urText = getValidUr(card.ur, card.arabic);
        const enText = getValidEn(card.en, card.arabic);
        if (urText || enText) {
          transEl.innerHTML = `
            <div class="card-trans-both">
              ${urText ? `<div class="trans-ur ur-font">${urText}</div>` : ''}
              ${enText ? `<div class="trans-en en-font">${enText}</div>` : ''}
            </div>
          `;
          transEl.style.display = 'block';
        } else {
          transEl.style.display = 'none';
        }
      } else {
        const rawTrans = state.lang === 'ur' ? (card.ur || '') : (card.en || '');
        const cleanTrans = state.lang === 'ur' ? getValidUr(rawTrans, card.arabic) : getValidEn(rawTrans, card.arabic);
        if (!cleanTrans) {
          transEl.style.display = 'none';
          transEl.textContent = '';
        } else {
          transEl.textContent = cleanTrans;
          transEl.style.display = 'block';
          transEl.dir = state.lang === 'en' ? 'ltr' : 'rtl';
          transEl.className = 'lesson-card-trans ' + (state.lang === 'ur' ? 'ur-font' : 'en-font');
        }
      }

      speakBtn.onclick = () => speakArabic(card.arabic);
    }

    const lessonStage = document.querySelector('.lesson-stage');
    if (lessonStage) lessonStage.scrollTop = 0;

    // Navigation Buttons
    const prevBtn = document.getElementById('lessonPrevBtn');
    const nextBtn = document.getElementById('lessonNextBtn');
    const startExBtn = document.getElementById('lessonStartExercisesBtn');

    prevBtn.disabled = cur === 0;

    const isLastCard = cur >= total - 1;
    if (isLastCard) {
      nextBtn.classList.add('hidden');
      startExBtn.classList.remove('hidden');
    } else {
      nextBtn.classList.remove('hidden');
      startExBtn.classList.add('hidden');
    }
  }

  function renderLessonFullText() {
    const container = document.getElementById('lessonFullScroll');
    container.innerHTML = '';

    lessonReader.cards.forEach((card, idx) => {
      const row = document.createElement('div');
      row.className = 't-illus-row';
      let cleanTrans = '';
      if (state.lang === 'both') {
        const u = getValidUr(card.ur, card.arabic);
        const e = getValidEn(card.en, card.arabic);
        cleanTrans = u && e ? `${u} • ${e}` : (u || e);
      } else if (state.lang === 'ur') {
        cleanTrans = getValidUr(card.ur, card.arabic);
      } else {
        cleanTrans = getValidEn(card.en, card.arabic);
      }
      row.innerHTML = `
        <div class="t-illus-left">
          <span class="t-illus-em">${card.emoji}</span>
          <div>
            <div class="t-illus-ar ar-font">${formatAr(card.arabic)}</div>
            ${cleanTrans ? `<div class="t-illus-trans" dir="${state.lang === 'en' ? 'ltr' : 'rtl'}">${cleanTrans}</div>` : ''}
          </div>
        </div>
        <span class="tts-hint">🔊</span>
      `;
      row.addEventListener('click', () => speakArabic(card.arabic));
      container.appendChild(row);
    });
  }

  function prevLessonCard() {
    if (lessonReader.index > 0) {
      lessonReader.index -= 1;
      renderCurrentLessonCard();
    }
  }

  function nextLessonCard() {
    if (lessonReader.index < lessonReader.cards.length - 1) {
      lessonReader.index += 1;
      renderCurrentLessonCard();
    }
  }

  // ============================================================================
  // DUOLINGO CHAPTER EXERCISES (التمارين) QUIZ ENGINE
  // ============================================================================
  function openTamreenSelector(unit) {
    if (!unit) return;
    const L = t();
    document.getElementById('tamreenUnitBadge').textContent = L.unitBadge(unit.unit_num) + ' • ' + formatAr(unit.title_ar);

    const titleEl = document.getElementById('tamreenSelectorTitle');
    if (state.lang === 'ur') {
      titleEl.textContent = 'مشق (تمرین) کا انتخاب کریں';
    } else if (state.lang === 'en') {
      titleEl.textContent = 'Select Exercise (Tamreen)';
    } else {
      titleEl.textContent = 'اخْتَرْ التَّمْرِينَ • Select Exercise';
    }

    const list = document.getElementById('tamreenOptionsList');
    list.innerHTML = '';

    const questions = unit.questions || [];
    
    // Group questions by tamreen_num
    const tamreenMap = {};
    questions.forEach(q => {
      const num = q.tamreen_num || 1;
      if (!tamreenMap[num]) {
        tamreenMap[num] = {
          num: num,
          title_ar: q.tamreen_title_ar || q.badge_ar || `التَّمْرِينُ (${num})`,
          title_ur: q.tamreen_title_ur || q.badge_ur || `مشق نمبر (${num})`,
          title_en: q.tamreen_title_en || q.badge_en || `Exercise (${num})`,
          goal_ur: q.grammar_goal_ur || '',
          goal_en: q.grammar_goal_en || '',
          count: 0
        };
      }
      tamreenMap[num].count += 1;
    });

    const tamreens = Object.values(tamreenMap).sort((a, b) => a.num - b.num);

    tamreens.forEach(tItem => {
      const card = document.createElement('div');
      card.className = 'tamreen-opt-card';

      let displayTitle = '';
      let displayGoal = '';
      if (state.lang === 'ur') {
        displayTitle = tItem.title_ur || tItem.title_ar;
        displayGoal = tItem.goal_ur;
      } else if (state.lang === 'en') {
        displayTitle = tItem.title_en || tItem.title_ar;
        displayGoal = tItem.goal_en;
      } else {
        displayTitle = `${tItem.title_ar} • ${tItem.title_ur || tItem.title_en}`;
        displayGoal = (tItem.goal_ur && tItem.goal_en) ? `${tItem.goal_ur} • ${tItem.goal_en}` : (tItem.goal_ur || tItem.goal_en);
      }

      const qLabel = state.lang === 'ur' ? `${tItem.count} سوالات` : (state.lang === 'en' ? `${tItem.count} Questions` : `${tItem.count} سوالات • Questions`);

      card.innerHTML = `
        <div class="tamreen-opt-num">${tItem.num}</div>
        <div class="tamreen-opt-info">
          <div class="tamreen-opt-title ar-font">${displayTitle}</div>
          ${displayGoal ? `<div class="tamreen-opt-goal">${displayGoal}</div>` : ''}
          <div class="tamreen-opt-meta">${qLabel}</div>
        </div>
      `;

      card.addEventListener('click', () => {
        closeTamreenSelector();
        startQuiz(unit, tItem.num);
      });
      list.appendChild(card);
    });

    // Also add "All Exercises" card if more than 1 tamreen
    if (tamreens.length > 1) {
      const allCard = document.createElement('div');
      allCard.className = 'tamreen-opt-card all-tamreens';
      
      let allTitle = state.lang === 'ur' ? 'جَمِيعُ التَّمَارِينِ (تمام مشقیں حل کریں)' : (state.lang === 'en' ? 'All Exercises (Play full sequence)' : 'جَمِيعُ التَّمَارِينِ • All Exercises');
      let allSub = state.lang === 'ur' ? `سبق کی تمام ${questions.length} مشقیں یکے بعد دیگرے حل کریں` : `Solve all ${questions.length} exercises in sequence`;

      allCard.innerHTML = `
        <div class="tamreen-opt-num">⭐</div>
        <div class="tamreen-opt-info">
          <div class="tamreen-opt-title ar-font">${allTitle}</div>
          <div class="tamreen-opt-goal">${allSub}</div>
          <div class="tamreen-opt-meta">${questions.length} questions</div>
        </div>
      `;
      allCard.addEventListener('click', () => {
        closeTamreenSelector();
        startQuiz(unit, null);
      });
      list.appendChild(allCard);
    }

    document.getElementById('tamreenSelectorModal').classList.remove('hidden');
  }

  function closeTamreenSelector() {
    document.getElementById('tamreenSelectorModal').classList.add('hidden');
  }

  function startQuiz(unit, tamreenNum = null) {
    if (!unit) return;
    closeLessonCardReader();
    closeTamreenSelector();

    quiz.unit = unit;
    quiz.tamreenNum = tamreenNum;

    const allQs = (unit.questions && unit.questions.length > 0)
      ? unit.questions
      : generateFallbackQuestions(unit);

    quiz.questions = tamreenNum
      ? allQs.filter(q => (q.tamreen_num || 1) === tamreenNum)
      : allQs;

    // Safety fallback
    if (quiz.questions.length === 0) quiz.questions = allQs;

    quiz.index = 0;
    quiz.hearts = 5;
    quiz.correctCount = 0;
    quiz.answered = false;

    document.getElementById('quizOverlay').classList.remove('hidden');
    renderCurrentQuizQuestion();
  }

  function closeQuiz() {
    document.getElementById('quizOverlay').classList.add('hidden');
    document.getElementById('peekLessonBackdrop').classList.add('hidden');
    updateHeaderStats();
    renderJourneyView();
  }

  function toggleLessonPeekDrawer() {
    const backdrop = document.getElementById('peekLessonBackdrop');
    const isHidden = backdrop.classList.contains('hidden');
    if (isHidden) {
      const body = document.getElementById('peekLessonBody');
      body.innerHTML = '';
      const cards = extractCardsFromUnit(quiz.unit);
      cards.forEach(card => {
        const row = document.createElement('div');
        row.className = 't-illus-row';
        row.innerHTML = `
          <div class="t-illus-left">
            <span class="t-illus-em">${card.emoji}</span>
            <div>
              <div class="t-illus-ar ar-font">${formatAr(card.arabic)}</div>
              ${card.trans ? `<div class="t-illus-trans">${card.trans}</div>` : ''}
            </div>
          </div>
          <span class="tts-hint">🔊</span>
        `;
        row.addEventListener('click', () => speakArabic(card.arabic));
        body.appendChild(row);
      });
      backdrop.classList.remove('hidden');
    } else {
      backdrop.classList.add('hidden');
    }
  }

  function generateFallbackQuestions(unit) {
    const cards = extractCardsFromUnit(unit);
    return cards.slice(0, 4).map(c => ({
      type: 'emoji_choice',
      badge_ar: 'تَمْرِينٌ',
      badge_ur: 'مشق: پہچان',
      badge_en: 'Exercise: Match',
      emoji: c.emoji,
      prompt_ar: 'مَا هٰذَا؟',
      prompt_ur: 'درست جملہ منتخب کریں:',
      prompt_en: 'Select the correct sentence:',
      sub_ur: unit.topic_ur || '',
      sub_en: unit.topic_en || '',
      options: [c.arabic],
      answer: c.arabic,
      explanation_ur: `درست جواب: ${c.arabic}`,
      explanation_en: `Correct answer: ${c.arabic}`
    }));
  }

  function renderCurrentQuizQuestion() {
    const L = t();
    const stage = document.getElementById('quizStage');
    const bottomBar = document.getElementById('quizBottomBar');
    const checkBtn = document.getElementById('quizCheckBtn');
    const skipBtn = document.getElementById('quizSkipBtn');

    // CRITICAL: Guarantee scroll is reset to top so question headers are NEVER cut off!
    stage.scrollTop = 0;

    bottomBar.className = 'quiz-bottombar';
    checkBtn.textContent = L.checkBtn;
    checkBtn.disabled = true;
    skipBtn.textContent = L.skipBtn;
    skipBtn.classList.remove('hidden');

    quiz.answered = false;
    quiz.selectedOption = null;
    quiz.sbSelectedIndices = [];
    quiz.pairLeftIdx = null;
    quiz.pairRightIdx = null;
    quiz.pairMatchedCount = 0;

    document.getElementById('quizHeartsCount').textContent = quiz.hearts;
    const pct = Math.round(((quiz.index) / Math.max(1, quiz.questions.length)) * 100);
    document.getElementById('quizProgressFill').style.width = `${Math.max(8, pct)}%`;

    if (quiz.index >= quiz.questions.length) {
      renderQuizCompletion();
      return;
    }

    const q = quiz.questions[quiz.index];
    stage.innerHTML = '';
    stage.scrollTop = 0;

    // 1. Clean Minimalist Question Header Bar (no boxed container, no leaked sub-topics!)
    const headerRow = document.createElement('div');
    headerRow.className = 'q-header-row';

    let badgeTxt = '';
    const tNum = q.tamreen_num || 1;
    if (state.lang === 'ur') badgeTxt = `مشق (${tNum})`;
    else if (state.lang === 'en') badgeTxt = `Exercise (${tNum})`;
    else badgeTxt = `مشق (${tNum}) • Ex. ${tNum}`;

    const badge = document.createElement('div');
    badge.className = 'q-badge';
    badge.textContent = `${badgeTxt} • ${quiz.index + 1}/${quiz.questions.length}`;

    let promptInst = '';
    if (state.lang === 'ur') promptInst = q.prompt_ur || q.prompt_ar || '';
    else if (state.lang === 'en') promptInst = q.prompt_en || q.prompt_ar || '';
    else promptInst = (q.prompt_ur && q.prompt_en) ? `${q.prompt_ur} • ${q.prompt_en}` : (q.prompt_ur || q.prompt_en || '');

    const inst = document.createElement('h3');
    inst.className = 'q-instruction';
    inst.textContent = promptInst;
    inst.dir = state.lang === 'en' ? 'ltr' : 'rtl';

    headerRow.appendChild(badge);
    if (promptInst) {
      headerRow.appendChild(inst);
    }
    stage.appendChild(headerRow);

    // 2. Prompt Card
    const promptCard = document.createElement('div');
    promptCard.className = 'q-prompt-card';
    
    let miniLabel = '';
    let bigText = q.prompt_ar || '';
    let subHint = '';
    if (state.lang === 'ur') subHint = q.hint_ur || '';
    else if (state.lang === 'en') subHint = q.hint_en || '';
    else subHint = (q.hint_ur && q.hint_en) ? `${q.hint_ur} • ${q.hint_en}` : (q.hint_ur || q.hint_en || '');

    let isBigAr = true;
    let audioTarget = q.answer || q.prompt_ar;

    // Detect if prompt is an instruction (e.g. "اختر العبارة الصحيحة" or "ترجم إلى العربية")
    const isInstructionPrompt = /^(اخْتَرْ|اخْتَرِ|تَرْجِمْ|اختر|ترجم)/.test((q.prompt_ar || '').trim());
    const hasTranslationHint = Boolean(q.hint_en || q.hint_ur);

    if (isInstructionPrompt && hasTranslationHint) {
      // Small instruction label above
      miniLabel = q.prompt_ar;
      if (state.lang === 'ur') bigText = q.hint_ur || '';
      else if (state.lang === 'en') bigText = q.hint_en || '';
      else bigText = (q.hint_ur && q.hint_en) ? `${q.hint_ur} • ${q.hint_en}` : (q.hint_ur || q.hint_en || '');
      subHint = '';
      isBigAr = false;
      audioTarget = q.answer; // speak the Arabic answer
    } else {
      // Standard Arabic prompt (e.g. "ذَهَبَ إِلَى السُّوقِ" or "مَا هٰذَا؟")
      bigText = q.prompt_ar;
      isBigAr = true;
      audioTarget = q.full_sentence || q.prompt_ar || q.answer;
    }

    const resolvedPromptEmoji = sanitizeEmoji(q.emoji) || getContextualEmoji(q.prompt_ar, q.hint_ur, q.hint_en) || (quiz.unit && sanitizeEmoji(quiz.unit.emoji)) || '💬';
    promptCard.innerHTML = `
      <span class="q-prompt-emoji">${resolvedPromptEmoji}</span>
      <div class="q-prompt-content">
        ${miniLabel ? `<div class="q-prompt-mini-label ar-font">${miniLabel}</div>` : ''}
        <div class="q-prompt-big-text ${isBigAr ? 'ar-font' : (state.lang === 'ur' ? 'ur-font' : 'en-font')}">${bigText}</div>
        ${subHint ? `<div class="q-prompt-hint ${state.lang === 'ur' ? 'ur-font' : 'en-font'}">${subHint}</div>` : ''}
      </div>
      <button class="q-speak-btn" title="Listen">🔊</button>
    `;
    promptCard.querySelector('.q-speak-btn').addEventListener('click', () => {
      speakArabic(audioTarget);
    });
    stage.appendChild(promptCard);

    // 3. Question Options / Interaction
    if (q.type === 'emoji_choice' || q.type === 'dialogue_qa' || q.type === 'fill_blank' || q.type === 'meaning_choice') {
      const grid = document.createElement('div');
      grid.className = 'q-options-grid';
      (q.options || []).forEach((opt, i) => {
        const btn = document.createElement('button');
        btn.className = 'q-option-btn';
        btn.dataset.opt = opt;

        const isArabicText = /[\u0600-\u06ff]/.test(opt) && !/[\u0679\u0686\u0698\u0695\u06ba\u06be\u06c1\u06d2]/.test(opt);
        // IN GRAMMAR EXERCISES: ALWAYS preserve tashkeel on Arabic options!
        const displayText = opt;

        btn.innerHTML = `
          <span class="${isArabicText ? 'ar-font preserve-tashkeel' : (state.lang === 'ur' ? 'ur-font' : 'en-font')}">${displayText}</span>
          <span class="key-num">${i + 1}</span>
        `;
        btn.addEventListener('click', () => {
          if (quiz.answered) return;
          quiz.selectedOption = opt;
          grid.querySelectorAll('.q-option-btn').forEach(b => b.classList.remove('selected'));
          btn.classList.add('selected');
          checkBtn.disabled = false;
          if (isArabicText) speakArabic(opt);
        });
        grid.appendChild(btn);
      });
      stage.appendChild(grid);
    } else if (q.type === 'sentence_builder') {
      const well = document.createElement('div');
      well.className = 'sb-answer-well';
      const bank = document.createElement('div');
      bank.className = 'sb-word-bank';

      function refreshSentenceBuilder() {
        well.innerHTML = '';
        bank.innerHTML = '';

        quiz.sbSelectedIndices.forEach((tileIdx, pos) => {
          const word = q.tiles[tileIdx];
          const tileBtn = document.createElement('button');
          tileBtn.className = 'word-tile ar-font';
          tileBtn.textContent = word;
          tileBtn.addEventListener('click', () => {
            if (quiz.answered) return;
            quiz.sbSelectedIndices.splice(pos, 1);
            refreshSentenceBuilder();
          });
          well.appendChild(tileBtn);
        });

        q.tiles.forEach((word, tileIdx) => {
          const used = quiz.sbSelectedIndices.includes(tileIdx);
          const tileBtn = document.createElement('button');
          tileBtn.className = 'word-tile ar-font' + (used ? ' used' : '');
          tileBtn.textContent = word;
          tileBtn.addEventListener('click', () => {
            if (quiz.answered || used) return;
            quiz.sbSelectedIndices.push(tileIdx);
            speakArabic(word);
            refreshSentenceBuilder();
          });
          bank.appendChild(tileBtn);
        });

        checkBtn.disabled = quiz.sbSelectedIndices.length === 0;
      }

      stage.appendChild(well);
      stage.appendChild(bank);
      refreshSentenceBuilder();
    } else if (q.type === 'pair_match') {
      const cols = document.createElement('div');
      cols.className = 'pairs-columns';
      const leftCol = document.createElement('div');
      leftCol.className = 'pairs-col';
      const rightCol = document.createElement('div');
      rightCol.className = 'pairs-col';

      // Column Headers (Tamreen 12)
      const leftHeader = document.createElement('div');
      leftHeader.className = 'pairs-column-header ar-font';
      leftHeader.textContent = state.lang === 'ur' ? 'الْقَائِمَةُ (أ)' : (state.lang === 'en' ? 'Column (A)' : 'الْقَائِمَةُ (أ) • Column A');
      leftCol.appendChild(leftHeader);

      const rightHeader = document.createElement('div');
      rightHeader.className = 'pairs-column-header ar-font';
      rightHeader.textContent = state.lang === 'ur' ? 'الْقَائِمَةُ (ب)' : (state.lang === 'en' ? 'Column (B)' : 'الْقَائِمَةُ (ب) • Column B');
      rightCol.appendChild(rightHeader);

      const pairs = q.pairs || [];
      const rightShuffled = pairs.map((p, idx) => ({ text: p.right, origIdx: idx }))
        .sort(() => Math.random() - 0.5);

      pairs.forEach((p, idx) => {
        const btn = document.createElement('button');
        btn.className = 'pair-tile ar-font';
        btn.dataset.idx = idx;
        const leftText = p.left_ar || (state.lang === 'ur' ? p.left_ur : p.left_en);
        btn.textContent = leftText;
        btn.addEventListener('click', () => {
          if (quiz.answered || btn.classList.contains('matched')) return;
          leftCol.querySelectorAll('.pair-tile').forEach(b => b.classList.remove('selected'));
          btn.classList.add('selected');
          quiz.pairLeftIdx = idx;
          if (p.left_ar) speakArabic(p.left_ar);
          tryMatchPair(leftCol, rightCol, pairs.length);
        });
        leftCol.appendChild(btn);
      });

      rightShuffled.forEach(item => {
        const btn = document.createElement('button');
        btn.className = 'pair-tile ar-font';
        btn.dataset.idx = item.origIdx;
        btn.textContent = item.text;
        btn.addEventListener('click', () => {
          if (quiz.answered || btn.classList.contains('matched')) return;
          rightCol.querySelectorAll('.pair-tile').forEach(b => b.classList.remove('selected'));
          btn.classList.add('selected');
          quiz.pairRightIdx = item.origIdx;
          speakArabic(item.text);
          tryMatchPair(leftCol, rightCol, pairs.length);
        });
        rightCol.appendChild(btn);
      });

      cols.appendChild(leftCol);
      cols.appendChild(rightCol);
      stage.appendChild(cols);
    }
  }

  function tryMatchPair(leftCol, rightCol, totalPairs) {
    if (quiz.pairLeftIdx === null || quiz.pairRightIdx === null) return;
    const lBtn = leftCol.querySelector(`.pair-tile[data-idx="${quiz.pairLeftIdx}"]`);
    const rBtn = rightCol.querySelector(`.pair-tile[data-idx="${quiz.pairRightIdx}"]`);

    if (quiz.pairLeftIdx === quiz.pairRightIdx) {
      playSound('correct');
      lBtn.classList.remove('selected');
      rBtn.classList.remove('selected');
      lBtn.classList.add('matched');
      rBtn.classList.add('matched');
      quiz.pairMatchedCount += 1;
      quiz.pairLeftIdx = null;
      quiz.pairRightIdx = null;

      if (quiz.pairMatchedCount >= totalPairs) {
        quiz.selectedOption = 'matched';
        document.getElementById('quizCheckBtn').disabled = false;
        handleQuizCheck();
      }
    } else {
      playSound('wrong');
      setTimeout(() => {
        if (lBtn) lBtn.classList.remove('selected');
        if (rBtn) rBtn.classList.remove('selected');
      }, 280);
      quiz.pairLeftIdx = null;
      quiz.pairRightIdx = null;
    }
  }

  function handleQuizCheck() {
    const L = t();
    const q = quiz.questions[quiz.index];
    if (!q) return;

    if (quiz.answered) {
      quiz.index += 1;
      renderCurrentQuizQuestion();
      return;
    }

    quiz.answered = true;
    let isCorrect = false;

    if (q.type === 'emoji_choice' || q.type === 'dialogue_qa' || q.type === 'fill_blank' || q.type === 'meaning_choice') {
      if (q.strict_tashkeel) {
        // Strict comparison with diacritics for vowel ending drills
        isCorrect = (quiz.selectedOption || '').trim() === (q.answer || '').trim();
      } else {
        isCorrect = stripTashkeel(quiz.selectedOption) === stripTashkeel(q.answer);
      }

      document.querySelectorAll('.q-option-btn').forEach(btn => {
        btn.disabled = true;
        const match = q.strict_tashkeel
          ? btn.dataset.opt.trim() === q.answer.trim()
          : stripTashkeel(btn.dataset.opt) === stripTashkeel(q.answer);
        if (match) {
          btn.classList.add('correct');
        } else if (btn.classList.contains('selected') && !isCorrect) {
          btn.classList.add('wrong');
        }
      });
    } else if (q.type === 'sentence_builder') {
      // In ordering questions, ignore commas, periods, and punctuation
      const built = quiz.sbSelectedIndices.map(i => q.tiles[i]).join(' ');
      const normalizeSentence = s => stripTashkeel(s).replace(/[\.\،\,\?\؟\!\:\"\']/g, '').replace(/\s+/g, ' ').trim();
      isCorrect = normalizeSentence(built) === normalizeSentence(q.answer);
    } else if (q.type === 'pair_match') {
      isCorrect = true;
    }

    const bottomBar = document.getElementById('quizBottomBar');
    const feedbackIcon = document.getElementById('feedbackIcon');
    const feedbackTitle = document.getElementById('feedbackTitle');
    const feedbackSub = document.getElementById('feedbackSub');
    const checkBtn = document.getElementById('quizCheckBtn');
    const skipBtn = document.getElementById('quizSkipBtn');

    skipBtn.classList.add('hidden');
    checkBtn.disabled = false;
    checkBtn.textContent = L.continueBtn;

    let expl = q.answer;
    if (state.lang === 'ur') expl = q.explanation_ur || q.answer;
    else if (state.lang === 'en') expl = q.explanation_en || q.answer;
    else expl = (q.explanation_ur && q.explanation_en) ? `${q.explanation_ur} • ${q.explanation_en}` : (q.explanation_ur || q.explanation_en || q.answer);

    if (isCorrect) {
      quiz.correctCount += 1;
      playSound('correct');
      bottomBar.className = 'quiz-bottombar state-correct';
      feedbackIcon.textContent = '🎉';
      feedbackTitle.textContent = L.correctTitle;
      const formattedAns = q.strict_tashkeel ? q.answer : formatAr(q.answer);
      if (expl && expl !== q.answer) {
        feedbackSub.innerHTML = `<span class="ar-font preserve-tashkeel">${formattedAns}</span><div style="margin-top:4px;font-size:0.92em;opacity:0.95;">${expl}</div>`;
      } else {
        feedbackSub.innerHTML = `<span class="ar-font preserve-tashkeel">${formattedAns}</span>`;
      }
    } else {
      quiz.hearts = Math.max(1, quiz.hearts - 1);
      document.getElementById('quizHeartsCount').textContent = quiz.hearts;
      playSound('wrong');
      bottomBar.className = 'quiz-bottombar state-wrong';
      feedbackIcon.textContent = '❌';
      feedbackTitle.textContent = L.wrongTitle;

      const formattedAns = q.strict_tashkeel ? q.answer : formatAr(q.answer);
      let ansLabel = '';
      if (state.lang === 'ur') {
        ansLabel = `اصل جواب یہ تھا: <strong class="ar-font preserve-tashkeel" style="font-size:1.15em;">${formattedAns}</strong>`;
        if (q.explanation_ur && q.explanation_ur !== q.answer) {
          ansLabel += `<div style="margin-top:4px;font-size:0.92em;opacity:0.95;">${q.explanation_ur}</div>`;
        }
      } else if (state.lang === 'en') {
        ansLabel = `The correct answer was: <strong class="ar-font preserve-tashkeel" style="font-size:1.15em;">${formattedAns}</strong>`;
        if (q.explanation_en && q.explanation_en !== q.answer) {
          ansLabel += `<div style="margin-top:4px;font-size:0.92em;opacity:0.95;">${q.explanation_en}</div>`;
        }
      } else {
        ansLabel = `اصل جواب یہ تھا: <strong class="ar-font preserve-tashkeel" style="font-size:1.15em;">${formattedAns}</strong> • Correct answer was: <strong class="ar-font preserve-tashkeel" style="font-size:1.15em;">${formattedAns}</strong>`;
        if (q.explanation_ur || q.explanation_en) {
          const detail = (q.explanation_ur && q.explanation_en) ? `${q.explanation_ur} • ${q.explanation_en}` : (q.explanation_ur || q.explanation_en);
          ansLabel += `<div style="margin-top:4px;font-size:0.92em;opacity:0.95;">${detail}</div>`;
        }
      }
      feedbackSub.innerHTML = ansLabel;
    }
  }

  function renderQuizCompletion() {
    const L = t();
    playSound('win');
    const stage = document.getElementById('quizStage');
    const bottomBar = document.getElementById('quizBottomBar');
    const checkBtn = document.getElementById('quizCheckBtn');
    const skipBtn = document.getElementById('quizSkipBtn');

    document.getElementById('quizProgressFill').style.width = '100%';
    bottomBar.className = 'quiz-bottombar state-correct';
    skipBtn.classList.add('hidden');

    const earnedXp = 20 + quiz.correctCount * 2;
    state.xp += earnedXp;
    const prevCrowns = state.completed[quiz.unit.id] || 0;
    state.completed[quiz.unit.id] = Math.min(3, prevCrowns + 1);
    saveState();

    const accuracy = Math.round((quiz.correctCount / Math.max(1, quiz.questions.length)) * 100);

    stage.innerHTML = `
      <div style="text-align:center;padding:24px 10px">
        <div style="font-size:4.5rem;margin-bottom:10px">🏆</div>
        <h2 style="font-size:2rem;margin:0 0 8px">${L.completeTitle}</h2>
        <p style="color:var(--text-muted);font-size:1.15rem;margin:0 0 24px">
          ${quiz.unit.emoji} <span class="ar-font">${formatAr(quiz.unit.title_ar)}</span> — ${getUnitTransTopic(quiz.unit)}
        </p>
        <div style="display:flex;justify-content:center;gap:16px;flex-wrap:wrap">
          <div class="stat-chip" style="min-width:140px;padding:12px">
            <span style="font-size:1.8rem">⚡</span>
            <div>
              <strong style="font-size:1.3rem">+${earnedXp} XP</strong>
              <div style="font-size:0.85rem;color:var(--text-muted)">${L.completeEarnedXP}</div>
            </div>
          </div>
          <div class="stat-chip" style="min-width:140px;padding:12px">
            <span style="font-size:1.8rem">🎯</span>
            <div>
              <strong style="font-size:1.3rem">${accuracy}%</strong>
              <div style="font-size:0.85rem;color:var(--text-muted)">${L.completeAccuracy}</div>
            </div>
          </div>
          <div class="stat-chip" style="min-width:140px;padding:12px">
            <span style="font-size:1.8rem">👑</span>
            <div>
              <strong style="font-size:1.3rem">${state.completed[quiz.unit.id]} / 3</strong>
              <div style="font-size:0.85rem;color:var(--text-muted)">${L.completeMastery}</div>
            </div>
          </div>
        </div>
      </div>
    `;

    document.getElementById('feedbackIcon').textContent = '👑';
    document.getElementById('feedbackTitle').textContent = L.completeSavedTitle;
    document.getElementById('feedbackSub').textContent = L.completeSavedSub;
    checkBtn.disabled = false;
    checkBtn.textContent = L.finishBtn;
    checkBtn.onclick = () => {
      checkBtn.onclick = null;
      closeQuiz();
    };
  }

  // ============================================================================
  // EVENT BINDINGS
  // ============================================================================
  function bindEvents() {
    // Splash Screen
    document.getElementById('selectUrduBtn').addEventListener('click', () => selectLearnerLanguage('ur'));
    document.getElementById('selectEnglishBtn').addEventListener('click', () => selectLearnerLanguage('en'));
    const bothBtn = document.getElementById('selectBothBtn');
    if (bothBtn) {
      bothBtn.addEventListener('click', () => selectLearnerLanguage('both'));
    }

    // Topbar Language Switch
    document.getElementById('switchLangBtn').addEventListener('click', () => {
      document.getElementById('splashOverlay').classList.remove('hidden');
    });

    document.getElementById('brandHomeBtn').addEventListener('click', () => {
      renderJourneyView();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Book Switcher
    document.querySelectorAll('#bookSwitcher .book-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        state.currentBook = Number(btn.dataset.book);
        const b = getBook(state.currentBook);
        if (b && b.units.length > 0) {
          state.currentUnitId = b.units[0].id;
        }
        applyThemeAndPrefs();
        updateHeaderStats();
        renderJourneyView();
      });
    });

    // Font Size Adjuster
    document.getElementById('fontSizeBtn').addEventListener('click', () => {
      state.fontScaleIndex = (state.fontScaleIndex + 1) % FONT_SCALES.length;
      applyThemeAndPrefs();
      saveState();
    });

    // Dark Mode Toggle
    document.getElementById('themeToggleBtn').addEventListener('click', () => {
      state.darkMode = !state.darkMode;
      applyThemeAndPrefs();
      saveState();
    });

    // Minimal Lesson Card Reader Events
    document.getElementById('readerCloseBtn').addEventListener('click', closeLessonCardReader);
    document.getElementById('lessonPrevBtn').addEventListener('click', prevLessonCard);
    document.getElementById('lessonNextBtn').addEventListener('click', nextLessonCard);
    document.getElementById('lessonStartExercisesBtn').addEventListener('click', () => {
      if (lessonReader.unit) {
        openTamreenSelector(lessonReader.unit);
      }
    });

    // Tamreen Selector Modal Events
    document.getElementById('closeTamreenSelectorBtn').addEventListener('click', closeTamreenSelector);
    document.getElementById('tamreenSelectorModal').addEventListener('click', (e) => {
      if (e.target.id === 'tamreenSelectorModal') closeTamreenSelector();
    });

    document.getElementById('readerModeCardBtn').addEventListener('click', () => setReaderMode('cards'));
    document.getElementById('readerModeFullBtn').addEventListener('click', () => setReaderMode('full'));

    // Quiz Overlay Events
    document.getElementById('quizCloseBtn').addEventListener('click', closeQuiz);
    document.getElementById('quizPeekLessonBtn').addEventListener('click', toggleLessonPeekDrawer);
    document.getElementById('closePeekBtn').addEventListener('click', toggleLessonPeekDrawer);
    document.getElementById('peekLessonBackdrop').addEventListener('click', (e) => {
      if (e.target.id === 'peekLessonBackdrop') toggleLessonPeekDrawer();
    });

    document.getElementById('quizCheckBtn').addEventListener('click', () => {
      if (quiz.index < quiz.questions.length) {
        handleQuizCheck();
      }
    });

    document.getElementById('quizSkipBtn').addEventListener('click', () => {
      quiz.index += 1;
      renderCurrentQuizQuestion();
    });

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      // If quiz is open
      const quizOpen = !document.getElementById('quizOverlay').classList.contains('hidden');
      if (quizOpen) {
        if (e.key === 'Escape') {
          const peek = document.getElementById('peekLessonBackdrop');
          if (!peek.classList.contains('hidden')) {
            peek.classList.add('hidden');
          } else {
            closeQuiz();
          }
        } else if (['1', '2', '3', '4'].includes(e.key) && !quiz.answered) {
          const idx = Number(e.key) - 1;
          const optBtns = document.querySelectorAll('.q-option-btn');
          if (optBtns[idx]) optBtns[idx].click();
        } else if (e.key === 'Enter') {
          const checkBtn = document.getElementById('quizCheckBtn');
          if (!checkBtn.disabled) checkBtn.click();
        }
        return;
      }

      // If lesson reader is open
      const readerOpen = !document.getElementById('lessonReaderModal').classList.contains('hidden');
      if (readerOpen) {
        if (e.key === 'Escape') {
          closeLessonCardReader();
        } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          nextLessonCard();
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          prevLessonCard();
        }
      }
    });
  }

  function init() {
    loadState();
    applyLocalizationStrings();
    applyThemeAndPrefs();
    updateHeaderStats();
    bindEvents();
    renderJourneyView();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
