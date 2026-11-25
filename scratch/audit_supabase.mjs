const SUPABASE_CONFIG = {
  url: 'https://hjmmbmhcgwkqsciywbwr.supabase.co/rest/v1',
  anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhqbW1ibWhjZ3drcXNjaXl3YndyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTIzNTA2NzEsImV4cCI6MjEwNzkyNjY3MX0.8EiK47mBB3uH0eZ8gWtqwMcs3_HfpyC6iPN17KDvAFw'
};

async function fetchTable(endpoint) {
  const t0 = Date.now();
  const res = await fetch(`${SUPABASE_CONFIG.url}/${endpoint}`, {
    headers: {
      'apikey': SUPABASE_CONFIG.anonKey,
      'Authorization': `Bearer ${SUPABASE_CONFIG.anonKey}`
    }
  });
  const ms = Date.now() - t0;
  if (!res.ok) {
    const errText = await res.text();
    return { ok: false, status: res.status, statusText: res.statusText, ms, error: errText };
  }
  const data = await res.json();
  return { ok: true, status: res.status, ms, count: data.length, data };
}

async function run() {
  console.log('=== AUDITING LIVE SUPABASE DATA ===');
  
  const tables = [
    'books?select=*&order=book_num.asc',
    'units?select=*&order=unit_num.asc',
    'lesson_cards?select=*&order=card_order.asc',
    'questions?select=*&order=tamreen_num.asc,question_order.asc'
  ];

  for (const t of tables) {
    const r = await fetchTable(t);
    const tableName = t.split('?')[0];
    if (r.ok) {
      console.log(`[PASS] ${tableName}: ${r.count} rows (${r.ms}ms)`);
      if (r.count > 0) {
        console.log(`  Sample row keys:`, Object.keys(r.data[0]));
      }
    } else {
      console.log(`[FAIL] ${tableName}: Status ${r.status} ${r.statusText} (${r.ms}ms) - ${r.error}`);
    }
  }
}

run().catch(console.error);
