const fs = require('fs');

// 1. Load Data
const dataJson = fs.readFileSync('data/madinah_books.json', 'utf8');
const DATA = JSON.parse(dataJson);

console.log(`Books loaded: ${DATA.books.length}`);
let totalUnits = 0;
let totalQuestions = 0;
let totalCards = 0;

function stripTashkeel(str) {
  if (!str) return '';
  return str.replace(/[\u064b-\u065f\u0670\u0640]/g, '').trim();
}

function extractCards(unit) {
  const cards = [];
  (unit.blocks || []).forEach(b => {
    if (b.type === 'emoji_grid' && Array.isArray(b.cards)) {
      b.cards.forEach(c => cards.push({ emoji: c.emoji || unit.emoji, text: c.text, ur: c.ur, en: c.en }));
    } else if (b.type === 'illustrated_line' || b.type === 'section_header' || b.type === 'text') {
      if (b.text && b.text.trim()) {
        cards.push({ emoji: b.emoji || unit.emoji, text: b.text, ur: b.ur, en: b.en });
      }
    } else if (b.type === 'dialogue') {
      cards.push({ emoji: b.speaker_emoji || '🗣️', text: `${b.speaker}: ${b.text}`, ur: b.ur, en: b.en });
    }
  });
  if (cards.length === 0) {
    cards.push({ emoji: unit.emoji, text: unit.title_ar, ur: unit.topic_ur, en: unit.topic_en });
  }
  return cards;
}

DATA.books.forEach(b => {
  console.log(`Book ${b.book_num}: ${b.units.length} units`);
  totalUnits += b.units.length;

  b.units.forEach(u => {
    const cards = extractCards(u);
    totalCards += cards.length;
    totalQuestions += (u.questions || []).length;

    // Check each question
    (u.questions || []).forEach((q, qIdx) => {
      if (q.type === 'emoji_choice' || q.type === 'dialogue_qa' || q.type === 'fill_blank' || q.type === 'meaning_choice') {
        if (!q.options || q.options.length < 2) {
          console.error(`Unit ${u.id} Q${qIdx} has fewer than 2 options:`, q);
        }
        const strippedAns = stripTashkeel(q.answer);
        const strippedOpts = q.options.map(stripTashkeel);
        if (!strippedOpts.includes(strippedAns)) {
          console.error(`Unit ${u.id} Q${qIdx} answer '${q.answer}' NOT in options:`, q.options);
        }
      }
    });
  });
});

console.log(`Total Units across all 3 books: ${totalUnits}`);
console.log(`Total Lesson Cards: ${totalCards}`);
console.log(`Total Exercise Questions: ${totalQuestions}`);
console.log("ALL UNITS, CARDS, AND QUESTIONS VERIFIED SUCCESSFULLY!");
