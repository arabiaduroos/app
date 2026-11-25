import fs from 'fs';

const SUPABASE_CONFIG = {
  url: 'https://hjmmbmhcgwkqsciywbwr.supabase.co/rest/v1',
  anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhqbW1ibWhjZ3drcXNjaXl3YndyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTIzNTA2NzEsImV4cCI6MjEwNzkyNjY3MX0.8EiK47mBB3uH0eZ8gWtqwMcs3_HfpyC6iPN17KDvAFw'
};

async function fetchTable(endpoint) {
  const res = await fetch(`${SUPABASE_CONFIG.url}/${endpoint}`, {
    headers: {
      'apikey': SUPABASE_CONFIG.anonKey,
      'Authorization': `Bearer ${SUPABASE_CONFIG.anonKey}`
    }
  });
  if (!res.ok) throw new Error(`${res.status}: ${res.statusText}`);
  return await res.json();
}

async function deepAudit() {
  console.log('Fetching all tables from Supabase...');
  const [books, units, cards, questions] = await Promise.all([
    fetchTable('books?select=*&order=book_num.asc'),
    fetchTable('units?select=*&order=unit_num.asc'),
    fetchTable('lesson_cards?select=*&order=card_order.asc'),
    fetchTable('questions?select=*&order=tamreen_num.asc,question_order.asc')
  ]);

  console.log('\n--- 1. BOOKS IN SUPABASE ---');
  books.forEach(b => {
    console.log(`Book ${b.book_num}: "${b.title_en}" (${b.title_ar}) - color: ${b.color}, icon: ${b.icon}`);
  });

  console.log('\n--- 2. UNITS IN SUPABASE ---');
  units.forEach(u => {
    const uCards = cards.filter(c => c.unit_id === u.id);
    const uQuestions = questions.filter(q => q.unit_id === u.id);
    console.log(`Unit ${u.id} (Book ${u.book_num}, Unit ${u.unit_num}): "${u.title_ar}" (${u.topic_en})`);
    console.log(`  Cards: ${uCards.length}, Questions: ${uQuestions.length}`);
  });

  console.log('\n--- 3. LESSON CARDS AUDIT ---');
  const cardUnits = [...new Set(cards.map(c => c.unit_id))];
  console.log('Units with cards:', cardUnits);
  for (const uid of cardUnits) {
    const uc = cards.filter(c => c.unit_id === uid).sort((a,b) => a.card_order - b.card_order);
    console.log(`\nUnit ${uid} (${uc.length} cards):`);
    console.log(`  First card: [order ${uc[0].card_order}] ${uc[0].arabic} -> ${uc[0].trans_en}`);
    const lastCard = uc[uc.length - 1];
    console.log(`  Last card: [order ${lastCard.card_order}] ${lastCard.arabic} -> ${lastCard.trans_en}`);
    
    // Check for vocab cards
    const vocabCards = uc.filter(c => {
      const ar = c.arabic || '';
      return ar.includes('الْكَلِمَاتُ الْجَدِيدَةُ') || ar.includes('الكلمات الجديدة');
    });
    console.log(`  Vocab cards in ${uid}: ${vocabCards.length}`);
    vocabCards.forEach(vc => {
      console.log(`    Order ${vc.card_order}: id=${vc.id}, arabic="${vc.arabic}", trans_en="${vc.trans_en}", emoji="${vc.emoji}"`);
      console.log(`    Fields present:`, Object.keys(vc));
      if (vc.words) console.log(`    words count:`, vc.words.length);
      else console.log(`    words column: undefined/null`);
    });

    // Check for nulls or missing fields
    const missingFields = uc.filter(c => !c.arabic || !c.trans_en || !c.trans_ur);
    if (missingFields.length > 0) {
      console.log(`  WARNING: ${missingFields.length} cards missing arabic/trans!`);
    } else {
      console.log(`  All ${uc.length} cards have arabic, trans_ur, trans_en.`);
    }
  }

  console.log('\n--- 4. QUESTIONS AUDIT ---');
  for (const uid of cardUnits) {
    const uq = questions.filter(q => q.unit_id === uid).sort((a,b) => (a.tamreen_num - b.tamreen_num) || (a.question_order - b.question_order));
    console.log(`\nUnit ${uid} (${uq.length} questions):`);
    const tamreens = [...new Set(uq.map(q => q.tamreen_num))];
    tamreens.forEach(t => {
      const tq = uq.filter(q => q.tamreen_num === t);
      console.log(`  Tamreen ${t}: ${tq.length} questions (types: ${[...new Set(tq.map(q=>q.type))].join(', ')})`);
    });

    // Integrity check on questions:
    const invalidQ = uq.filter(q => !q.prompt_ar || !q.answer || !Array.isArray(q.options) || q.options.length < 2);
    if (invalidQ.length > 0) {
      console.log(`  WARNING: ${invalidQ.length} questions invalid:`, invalidQ.map(q => q.id));
    } else {
      console.log(`  All ${uq.length} questions have valid prompts, answers, and options arrays.`);
    }

    // Check if correct answer is always among options
    const missingAnsInOpt = uq.filter(q => !q.options.some(opt => opt.trim() === q.answer.trim()));
    if (missingAnsInOpt.length > 0) {
      console.log(`  WARNING: ${missingAnsInOpt.length} questions where answer is NOT in options!`);
      missingAnsInOpt.forEach(q => console.log(`    ${q.id}: ans="${q.answer}", options=${JSON.stringify(q.options)}`));
    } else {
      console.log(`  All ${uq.length} questions have their answer included in options.`);
    }
  }

  console.log('\n--- 5. COMPARISON WITH EMBEDDED LOCAL APP DATA ---');
  const appContent = fs.readFileSync('app.js', 'utf8');
  const match = appContent.match(/let DATA = ({.*?});\s*\n/s);
  if (match) {
    const localData = JSON.parse(match[1]);
    console.log('Local DATA books count:', localData.books.length);
    localData.books.forEach(b => {
      console.log(`Local Book ${b.book_num} units:`, (b.units || []).map(u => `${u.id} (${(u.cards||[]).length}c, ${(u.questions||[]).length}q)`));
    });
  }
}

deepAudit().catch(console.error);
