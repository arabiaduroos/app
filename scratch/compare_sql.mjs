import fs from 'fs';

const sql = fs.readFileSync('b1_u3.sql', 'utf8');
const cardMatches = [...sql.matchAll(/\('b1_u3',\s*(\d+),\s*'([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'([^']+)'\)/g)];
console.log('Total card inserts in b1_u3.sql:', cardMatches.length);
if (cardMatches.length > 0) {
  cardMatches.slice(-3).forEach(m => {
    console.log(`Card ${m[1]}: ${m[2]} -> ${m[4]}`);
  });
}

const qMatches = [...sql.matchAll(/INSERT INTO public\.questions/g)];
console.log('Questions insert statements:', qMatches.length);
const qRows = [...sql.matchAll(/\('b1_u3_t\d+_q\d+',\s*'b1_u3'/g)];
console.log('Total question rows in b1_u3.sql:', qRows.length);
