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
  return await res.json();
}

async function testAssemble() {
  const [books, units, cards, questions] = await Promise.all([
    fetchTable('books?select=*&order=book_num.asc'),
    fetchTable('units?select=*&order=unit_num.asc'),
    fetchTable('lesson_cards?select=*&order=card_order.asc'),
    fetchTable('questions?select=*&order=tamreen_num.asc,question_order.asc')
  ]);

  // Read app.js functions
  const appCode = fs.readFileSync('app.js', 'utf8');
  
  // Extract assembleData and extractCardsFromUnit logic
  const vm = await import('vm');
  const sandbox = {
    console,
    SUPABASE_CONFIG,
    stripTashkeel: (s) => (s || '').replace(/[\u064B-\u065F\u0670]/g, '').trim(),
    sanitizeEmoji: (e) => e,
    formatAr: (s) => s,
    getValidUr: (u, a) => u || '',
    getValidEn: (e, a) => e || '',
    getContextualEmoji: () => '',
    isIdenticalToAr: () => false,
    state: { lang: 'en' }
  };

  // Run in VM to simulate exact app behavior
  const script = new vm.Script(`
    ${appCode.substring(appCode.indexOf('function assembleData'), appCode.indexOf('function loadCachedSupabaseData'))}
    ${appCode.substring(appCode.indexOf('const VOCAB_REGISTRY'), appCode.indexOf('function getUnitVocabWords'))}
    ${appCode.substring(appCode.indexOf('function getUnitVocabWords'), appCode.indexOf('function openTamreenSelector'))}
    globalThis.assembleData = assembleData;
    globalThis.extractCardsFromUnit = extractCardsFromUnit;
  `);

  const context = vm.createContext(sandbox);
  script.runInContext(context);

  const assembled = sandbox.assembleData(books, units, cards, questions);
  console.log('Assembled Books:', assembled.books.length);
  
  assembled.books[0].units.forEach(u => {
    const extracted = sandbox.extractCardsFromUnit(u);
    console.log(`Unit ${u.id}: cards from Supabase = ${u.cards.length}, extracted cards in reader = ${extracted.length}`);
    const vocabCards = extracted.filter(c => c.type === 'vocab_table');
    console.log(`  Vocab cards in reader: ${vocabCards.length}`);
    vocabCards.forEach((vc, idx) => {
      console.log(`    Vocab Card ${idx+1}: "${vc.title_en}" with ${vc.words ? vc.words.length : 0} words`);
    });
  });
}

testAssemble().catch(console.error);
