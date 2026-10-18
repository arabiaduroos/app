import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('data/madinah_books.json', encoding='utf-8'))
for b_idx, b in enumerate(d['books'], 1):
    for u in b['units']:
        for i, blk in enumerate(u.get('blocks', [])):
            if blk.get('type') == 'vocab_table':
                words = blk.get('words', [])
                has_ex = any('(' in w.get('ar', '') or 'اقرأ' in w.get('ar', '') or 'تمرين' in w.get('ar', '') or 'املأ' in w.get('ar', '') for w in words)
                if len(words) > 18 or has_ex:
                    print(f"Book {b_idx} Unit {u['unit_num']} ({u['id']}) blk {i}: {len(words)} words, has_ex={has_ex}")
