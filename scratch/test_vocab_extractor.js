const fs = require('fs');

function parseVocabSections(filename) {
  const content = fs.readFileSync(filename, 'utf8');
  const sections = content.split('<section class="unit-card"');
  const results = {};

  sections.forEach((sec, idx) => {
    if (idx === 0) return;
    const idMatch = sec.match(/id="([^"]+)"/);
    const unitId = idMatch ? idMatch[1] : `unit_${idx}`;

    if (!sec.includes('الكلمات الجديدة')) return;

    const parts = sec.split(/<div class="sec-hdr">[^<]*الكلمات الجديدة[^<]*<\/div>/);
    if (parts.length < 2) return;

    const vocabPart = parts[1];
    // Find all txt-line inside vocabPart
    const lineMatches = vocabPart.matchAll(/<div class="txt-line">([\s\S]*?)<\/div>\s*<\/div>/g);
    const rows = [];
    for (const lm of lineMatches) {
      const lineHtml = lm[1];
      // First div is Arabic, second is ur
      const divMatches = [...lineHtml.matchAll(/<div[^>]*>([\s\S]*?)<\/div>/g)];
      if (divMatches.length >= 1) {
        let ar = divMatches[0][1].replace(/<[^>]+>/g, '').trim();
        ar = ar.replace(/^[^\w\s\(\)\.\-\u0600-\u06FF]+/, '').trim();
        let ur = divMatches[1] ? divMatches[1][1].replace(/<[^>]+>/g, '').trim() : '';
        rows.push({ ar, ur });
      }
    }
    if (rows.length > 0) {
      results[unitId] = rows;
    }
  });

  return results;
}

const b1 = parseVocabSections('transcriptions/Madinah-Book-1.html');
console.log('Book 1 units with vocab:', Object.keys(b1));
for (const u of Object.keys(b1).slice(0, 3)) {
  console.log(`=== ${u} ===`);
  b1[u].slice(0, 4).forEach(r => console.log('  AR:', r.ar, '--> UR:', r.ur));
}

const b2 = parseVocabSections('transcriptions/Madinah-Book-2.html');
console.log('Book 2 units with vocab:', Object.keys(b2));
for (const u of Object.keys(b2).slice(0, 3)) {
  console.log(`=== ${u} ===`);
  b2[u].slice(0, 4).forEach(r => console.log('  AR:', r.ar, '--> UR:', r.ur));
}
