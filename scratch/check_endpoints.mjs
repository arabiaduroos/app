const SUPABASE_CONFIG = {
  url: 'https://hjmmbmhcgwkqsciywbwr.supabase.co/rest/v1',
  anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhqbW1ibWhjZ3drcXNjaXl3YndyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTIzNTA2NzEsImV4cCI6MjEwNzkyNjY3MX0.8EiK47mBB3uH0eZ8gWtqwMcs3_HfpyC6iPN17KDvAFw'
};

async function checkB1U3Cards() {
  const r = await fetch(`${SUPABASE_CONFIG.url}/lesson_cards?unit_id=eq.b1_u3&order=card_order.asc`, {
    headers: {
      'apikey': SUPABASE_CONFIG.anonKey,
      'Authorization': 'Bearer ' + SUPABASE_CONFIG.anonKey
    }
  });
  const cards = await r.json();
  console.log('Total cards in Supabase for b1_u3:', cards.length);
  cards.slice(-5).forEach(c => {
    console.log(`Order ${c.card_order} [id=${c.id}]: ${c.arabic} -> ${c.trans_en}`);
  });
}

checkB1U3Cards().catch(console.error);
