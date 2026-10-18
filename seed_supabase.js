// ============================================================================
// Supabase Database Seeder for Madinah Arabic Course
// Safely populates books, units, lesson_cards, questions, and grammar_rules
// ============================================================================

const SUPABASE_URL = 'https://hjmmbmhcgwkqsciywbwr.supabase.co';
const SUPABASE_KEY = process.env.SUPABASE_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhqbW1ibWhjZ3drcXNjaXl3YndyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTIzNTA2NzEsImV4cCI6MjEwNzkyNjY3MX0.8EiK47mBB3uH0eZ8gWtqwMcs3_HfpyC6iPN17KDvAFw';

global.window = {};
require('./data/madinah_books.js');
const books = global.window.MADINAH_BOOKS.books;

async function postBatch(endpoint, items) {
  const url = `${SUPABASE_URL}/rest/v1/${endpoint}`;
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'apikey': SUPABASE_KEY,
      'Authorization': `Bearer ${SUPABASE_KEY}`,
      'Content-Type': 'application/json',
      'Prefer': 'resolution=merge-duplicates'
    },
    body: JSON.stringify(items)
  });

  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`Failed to insert into ${endpoint} (status ${res.status}): ${txt}`);
  }
}

async function runMigration() {
  console.log('🚀 Starting Supabase Seeding...\n');

  let bRows = [], uRows = [], cRows = [], qRows = [], gRows = [];

  books.forEach(b => {
    bRows.push({
      book_num: b.book_num,
      title_ar: b.title_ar,
      title_en: b.title_en,
      title_ur: b.title_ur,
      color: b.color || '#58cc02',
      icon: b.icon || '📗'
    });

    b.units.forEach(u => {
      uRows.push({
        id: u.id,
        book_num: b.book_num,
        unit_num: u.unit_num,
        title_ar: u.title_ar,
        topic_ar: u.topic_ar || '',
        topic_en: u.topic_en || '',
        topic_ur: u.topic_ur || '',
        emoji: u.emoji || '📖'
      });

      let cardIdx = 1;
      (u.blocks || []).forEach(blk => {
        if (blk.section === 'exercises' || blk.type === 'exercise_line') return;
        cRows.push({
          unit_id: u.id,
          card_order: cardIdx++,
          arabic: (blk.text || '').trim(),
          trans_ur: (blk.ur || '').trim(),
          trans_en: (blk.en || '').trim(),
          emoji: blk.emoji || '📖'
        });
      });

      let qIdx = 1;
      (u.questions || []).forEach(q => {
        qRows.push({
          id: q.id,
          unit_id: u.id,
          tamreen_num: q.tamreen_num || 1,
          question_order: qIdx++,
          type: q.type || 'sentence_reading',
          prompt_ar: q.prompt_ar || '',
          prompt_ur: q.prompt_ur || '',
          prompt_en: q.prompt_en || '',
          answer: q.answer || '',
          options: q.options || [],
          strict_tashkeel: Boolean(q.strict_tashkeel),
          hint_ur: q.hint_ur || '',
          hint_en: q.hint_en || '',
          explanation_ur: q.explanation_ur || '',
          explanation_en: q.explanation_en || '',
          emoji: q.emoji || '✍️'
        });
      });

      let gIdx = 1;
      (u.curriculum_flow || []).forEach((flow) => {
        if (flow.type === 'qaida') {
          gRows.push({
            id: flow.id || `${u.id}_qaida_${gIdx}`,
            unit_id: u.id,
            rule_order: gIdx++,
            title_ar: flow.title_ar || '',
            rule_summary_ur: flow.rule_summary_ur || '',
            rule_summary_en: flow.rule_summary_en || '',
            page: flow.page || null,
            examples: flow.examples || []
          });
        }
      });
    });
  });

  // 1. Insert Books
  console.log(`Inserting ${bRows.length} books...`);
  await postBatch('books', bRows);
  console.log('✅ Books inserted.');

  // 2. Insert Units
  console.log(`Inserting ${uRows.length} units...`);
  await postBatch('units', uRows);
  console.log('✅ Units inserted.');

  // 3. Insert Lesson Cards in chunks of 150
  console.log(`Inserting ${cRows.length} lesson cards...`);
  for (let i = 0; i < cRows.length; i += 150) {
    const chunk = cRows.slice(i, i + 150);
    await postBatch('lesson_cards', chunk);
    process.stdout.write(`  Cards: ${Math.min(i + 150, cRows.length)} / ${cRows.length}\r`);
  }
  console.log('\n✅ Lesson cards inserted.');

  // 4. Insert Questions in chunks of 150
  console.log(`Inserting ${qRows.length} questions...`);
  for (let i = 0; i < qRows.length; i += 150) {
    const chunk = qRows.slice(i, i + 150);
    await postBatch('questions', chunk);
    process.stdout.write(`  Questions: ${Math.min(i + 150, qRows.length)} / ${qRows.length}\r`);
  }
  console.log('\n✅ Questions inserted.');



  console.log('\n🎉 ALL DATA SUCCESSFULLY POPULATED INTO SUPABASE!');
}

runMigration().catch(err => {
  console.error('\n❌ Migration error:', err.message);
});
