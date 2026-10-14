const fs = require('fs');
const d = JSON.parse(fs.readFileSync('data/madinah_books.json', 'utf8'));

let found = 0;
d.books.forEach(b => {
  b.units.forEach(u => {
    (u.blocks || []).forEach((blk, idx) => {
      const ur = blk.ur || '';
      const en = blk.en || '';
      const text = blk.text || (blk.cells ? blk.cells.join(' ') : '');
      const type = blk.type;
      if (type !== 'dialogue') {
        if (/^(آمنہ|آمنة|حامد|المدرس|أحمد|محمد|سعاد|زينب|عائشة|خالد|بلال|علي|ياسر|مريم|فاطمة)\s*[:：]/.test(ur) ||
            /^(Amina|Hamid|Teacher|Mudarris|Ahmad|Muhammad|Suad|Zaynab|Aisha|Khalid|Bilal|Ali|Yasir|Maryam|Fatima)\s*[:：]/.test(en)) {
          console.log(`Book ${b.book_num} Unit ${u.unit_num} Block ${idx} Type ${type}:`);
          console.log('  AR:', text);
          console.log('  UR:', ur);
          console.log('  EN:', en);
          found++;
        }
      }
    });
  });
});
console.log('Total dialogue mismatches on non-dialogue blocks:', found);
