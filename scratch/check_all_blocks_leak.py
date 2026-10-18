import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== CHECKING ALL 71 UNITS FOR LEAKED EXERCISES IN BLOCKS ===")

ex_keywords = [
    r'اقرأ واكتب',
    r'أجب عن',
    r'املأ الفراغ',
    r'اختر كلمة',
    r'حوّل',
    r'ضع في',
    r'أشر إلى',
    r'هات جمع',
    r'تأمل ما يلي',
    r'صل بين',
    r'صحح',
    r'\(\d+\)\s*\.{3,}',
    r'\(\d+\)\s*…+'
]
regex = re.compile('|'.join(ex_keywords))

results = []

for b_idx, book in enumerate(d['books'], 1):
    for u in book['units']:
        uid = u['id']
        unum = u['unit_num']
        for b_idx_blk, blk in enumerate(u.get('blocks', [])):
            btype = blk.get('type')
            sec = blk.get('section')
            
            # 1. Check vocab_table
            if btype == 'vocab_table':
                words = blk.get('words', [])
                leaked_words = [w for w in words if regex.search(w.get('ar', ''))]
                if leaked_words:
                    results.append({
                        'book': b_idx, 'unit': unum, 'uid': uid, 'blk_idx': b_idx_blk,
                        'btype': btype, 'sec': sec,
                        'leak_count': len(leaked_words),
                        'total_words': len(words),
                        'sample': leaked_words[0]['ar'][:60]
                    })
            
            # 2. Check other blocks that aren't marked section='exercises'
            elif sec != 'exercises' and btype != 'exercise_line':
                text = blk.get('arabic', '') or blk.get('text', '')
                if regex.search(text):
                    results.append({
                        'book': b_idx, 'unit': unum, 'uid': uid, 'blk_idx': b_idx_blk,
                        'btype': btype, 'sec': sec,
                        'leak_count': 1,
                        'total_words': 0,
                        'sample': text[:60]
                    })

print(f"Total blocks with leaked exercises: {len(results)}")
for r in results:
    print(f"Book {r['book']} Unit {r['unit']} ({r['uid']} blk {r['blk_idx']} type={r['btype']} sec={r['sec']}): {r['leak_count']} leaks -> {r['sample']}")
