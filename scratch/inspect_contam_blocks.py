import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for target in [('b1_u3', 27), ('b1_u9', 37), ('b1_u13', 39)]:
    uid, blk_idx = target
    for b in d['books']:
        for u in b['units']:
            if u['id'] == uid:
                blk = u['blocks'][blk_idx]
                print(f"=== {uid} (Unit {u['unit_num']}) Block {blk_idx} ===")
                print(f"Type: {blk.get('type')}, Sec: {blk.get('section')}, Title: {blk.get('title_ar')}")
                words = blk.get('words', [])
                print(f"Total words: {len(words)}")
                for i, w in enumerate(words):
                    print(f"  [{i}] ar: {w.get('ar')} | ur: {w.get('ur')}")
