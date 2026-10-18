import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== SCANNING ALL UNITS ACROSS ALL 3 BOOKS FOR CONTAMINATION ===")

issues = []

for b_idx, book in enumerate(d['books'], 1):
    for u in book['units']:
        unit_id = u['id']
        unit_num = u['unit_num']
        
        for b_idx_blk, block in enumerate(u.get('blocks', [])):
            b_type = block.get('type')
            b_sec = block.get('section')
            b_words = block.get('words', [])
            
            if b_type == 'vocab_table':
                for w_idx, w in enumerate(b_words):
                    ar = w.get('ar', '')
                    if re.search(r'(تمارين|تمرين|اقرأ واكتب|اِمْلأ|اختر كلمة|\(\d+\)\s*\.{3,}|\(\d+\)\s*…+)', ar):
                        issues.append({
                            'book': b_idx,
                            'unit': unit_num,
                            'unit_id': unit_id,
                            'block_idx': b_idx_blk,
                            'issue': 'Exercise in vocab_table',
                            'sample': ar[:60]
                        })
                        break
                    elif re.search(r'\(\d+\)\s*[\u0600-\u06ff]+', ar) and len(b_words) > 15:
                        issues.append({
                            'book': b_idx,
                            'unit': unit_num,
                            'unit_id': unit_id,
                            'block_idx': b_idx_blk,
                            'issue': 'Numbered reading sentences in vocab_table',
                            'sample': ar[:60]
                        })
                        break

print(f"Total contaminated vocab_tables found: {len(issues)}")
for iss in issues:
    print(f"Book {iss['book']} Unit {iss['unit']} ({iss['unit_id']} blk {iss['block_idx']}): {iss['issue']} -> {iss['sample']}")
