import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

def clean(s):
    if not s: return ''
    # remove tatweel, tashkeel, emojis
    s = re.sub(r'[\u0640\u064b-\u065f\u0670]', '', s)
    return s.strip()

ex_words = ['اقرا واكتب', 'اجب عن', 'املا الفراغ', 'اختر كلمة', 'حول', 'ضع في', 'اشر الى', 'هات جمع', 'تامل ما يلي', 'صل بين', 'صحح', 'صل ']

results = []

for b_idx, book in enumerate(d['books'], 1):
    for u in book['units']:
        uid = u['id']
        unum = u['unit_num']
        for b_idx_blk, blk in enumerate(u.get('blocks', [])):
            btype = blk.get('type')
            sec = blk.get('section')
            
            if btype == 'vocab_table':
                words = blk.get('words', [])
                leaked = []
                for w in words:
                    c_ar = clean(w.get('ar', ''))
                    if any(kw in c_ar for kw in ex_words) or re.search(r'\(\d+\)\s*\.{3,}|\(\d+\)\s*…+', c_ar):
                        leaked.append(w.get('ar', ''))
                if leaked:
                    results.append({
                        'book': b_idx, 'unit': unum, 'uid': uid, 'blk_idx': b_idx_blk,
                        'btype': btype, 'sec': sec,
                        'leak_count': len(leaked),
                        'total_words': len(words),
                        'sample': leaked[0][:60]
                    })

print(f"Total blocks with leaked exercises in vocab_tables: {len(results)}")
for r in results:
    print(f"Book {r['book']} Unit {r['unit']} ({r['uid']} blk {r['blk_idx']} words={r['total_words']}): {r['leak_count']} leaks -> {r['sample']}")
