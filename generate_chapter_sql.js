const fs = require('fs');

global.window = {};
require('./data/madinah_books.js');
const books = global.window.MADINAH_BOOKS.books;

function sqlEscape(str) {
  if (str === null || str === undefined) return 'NULL';
  return "'" + String(str).replace(/'/g, "''") + "'";
}

function sqlJson(obj) {
  if (!obj) return "'[]'::jsonb";
  return "'" + JSON.stringify(obj).replace(/'/g, "''") + "'::jsonb";
}

function generateBooksSQL() {
  let sql = `-- =====================================================\n-- 0. INITIAL SETUP: THE 3 MADINAH ARABIC BOOKS\n-- =====================================================\n`;
  sql += `INSERT INTO public.books (book_num, title_ar, title_en, title_ur, color, icon)\nVALUES\n`;
  const bVals = books.map(b => {
    return `  (${b.book_num}, ${sqlEscape(b.title_ar)}, ${sqlEscape(b.title_en)}, ${sqlEscape(b.title_ur)}, ${sqlEscape(b.color || '#58cc02')}, ${sqlEscape(b.icon || '📗')})`;
  });
  sql += bVals.join(',\n') + `\nON CONFLICT (book_num) DO UPDATE SET title_ar = EXCLUDED.title_ar, title_en = EXCLUDED.title_en, title_ur = EXCLUDED.title_ur, color = EXCLUDED.color, icon = EXCLUDED.icon;\n\n`;
  return sql;
}

function generateUnitSQL(bookNum, unitNum) {
  const b = books.find(item => item.book_num === bookNum);
  if (!b) throw new Error(`Book ${bookNum} not found`);
  const u = b.units.find(item => item.unit_num === unitNum);
  if (!u) throw new Error(`Unit ${unitNum} in Book ${bookNum} not found`);

  let sql = `-- =====================================================\n`;
  sql += `-- BOOK ${bookNum}, UNIT ${unitNum}: ${u.title_ar}\n`;
  sql += `-- =====================================================\n\n`;

  // 1. Unit meta
  sql += `-- 1. UNIT METADATA\n`;
  sql += `INSERT INTO public.units (id, book_num, unit_num, title_ar, topic_ar, topic_en, topic_ur, emoji)\nVALUES\n`;
  sql += `  (${sqlEscape(u.id)}, ${b.book_num}, ${u.unit_num}, ${sqlEscape(u.title_ar)}, ${sqlEscape(u.topic_ar || '')}, ${sqlEscape(u.topic_en || '')}, ${sqlEscape(u.topic_ur || '')}, ${sqlEscape(u.emoji || '📖')})\nON CONFLICT (id) DO UPDATE SET title_ar = EXCLUDED.title_ar, topic_ar = EXCLUDED.topic_ar, topic_en = EXCLUDED.topic_en, topic_ur = EXCLUDED.topic_ur, emoji = EXCLUDED.emoji;\n\n`;

  // 2. Lesson Cards
  let cardIdx = 1;
  const cardRows = [];
  (u.blocks || []).forEach(blk => {
    if (blk.section === 'exercises' || blk.type === 'exercise_line') return;
    cardRows.push(`  (${sqlEscape(u.id)}, ${cardIdx++}, ${sqlEscape((blk.text || '').trim())}, ${sqlEscape((blk.ur || '').trim())}, ${sqlEscape((blk.en || '').trim())}, ${sqlEscape(blk.emoji || '📖')})`);
  });

  sql += `-- 2. LESSON CARDS (${cardRows.length} cards for reading & pronunciation)\n`;
  sql += `DELETE FROM public.lesson_cards WHERE unit_id = ${sqlEscape(u.id)};\n`;
  if (cardRows.length > 0) {
    sql += `INSERT INTO public.lesson_cards (unit_id, card_order, arabic, trans_ur, trans_en, emoji)\nVALUES\n` + cardRows.join(',\n') + ';\n\n';
  }

  // 3. Questions
  let qIdx = 1;
  const qRows = [];
  // Sort questions in order of tamreen
  const sortedQuestions = [...(u.questions || [])].sort((a, b) => (Number(a.tamreen_num) || 1) - (Number(b.tamreen_num) || 1));
  sortedQuestions.forEach(q => {
    qRows.push(`  (${sqlEscape(q.id)}, ${sqlEscape(u.id)}, ${q.tamreen_num || 1}, ${qIdx++}, ${sqlEscape(q.type || 'sentence_reading')}, ${sqlEscape(q.prompt_ar || '')}, ${sqlEscape(q.prompt_ur || '')}, ${sqlEscape(q.prompt_en || '')}, ${sqlEscape(q.answer || '')}, ${sqlJson(q.options || [])}, ${q.strict_tashkeel ? 'TRUE' : 'FALSE'}, ${sqlEscape(q.hint_ur || '')}, ${sqlEscape(q.hint_en || '')}, ${sqlEscape(q.explanation_ur || '')}, ${sqlEscape(q.explanation_en || '')}, ${sqlEscape(q.emoji || '✍️')})`);
  });

  sql += `-- 3. EXERCISE QUESTIONS (${qRows.length} questions in order of tamreens)\n`;
  if (qRows.length > 0) {
    sql += `INSERT INTO public.questions (id, unit_id, tamreen_num, question_order, type, prompt_ar, prompt_ur, prompt_en, answer, options, strict_tashkeel, hint_ur, hint_en, explanation_ur, explanation_en, emoji)\nVALUES\n` + qRows.join(',\n') + `\nON CONFLICT (id) DO UPDATE SET prompt_ar = EXCLUDED.prompt_ar, prompt_ur = EXCLUDED.prompt_ur, prompt_en = EXCLUDED.prompt_en, answer = EXCLUDED.answer, options = EXCLUDED.options, strict_tashkeel = EXCLUDED.strict_tashkeel, hint_ur = EXCLUDED.hint_ur, hint_en = EXCLUDED.hint_en, explanation_ur = EXCLUDED.explanation_ur, explanation_en = EXCLUDED.explanation_en, emoji = EXCLUDED.emoji;\n`;
  }

  return sql;
}

const targetBook = parseInt(process.argv[2] || '1', 10);
const targetUnit = parseInt(process.argv[3] || '1', 10);

let output = '';
if (targetBook === 1 && targetUnit === 1) {
  output += generateBooksSQL();
}
output += generateUnitSQL(targetBook, targetUnit);

fs.writeFileSync('./chapter_output.sql', output, 'utf8');
console.log(`Successfully generated SQL for Book ${targetBook}, Unit ${targetUnit}`);
console.log(`Saved to chapter_output.sql (${output.length} characters)`);
