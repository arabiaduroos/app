import sys, os, json

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('scratch'))
import parse_all_3books_cairo as p

b1 = p.book_map[1]
for l in b1:
    if 'الخامس' in l['title']:
        print(f"=== {l['title']} ===")
        for i, ex in enumerate(l['exercises']):
            print(f"  [{i+1}] {ex['title']} -> {len(ex['items'])} items")
            for it in ex['items'][:2]:
                print(f"       * {it[:70]}")
