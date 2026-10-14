import json, sys
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
for b_idx in range(3):
    b = data['books'][b_idx]
    print(f"\n=== BOOK {b['book_num']} ===")
    for u in b['units']:
        qs = u.get('questions', [])
        t_nums = sorted(list(set(q.get('tamreen_num', 1) for q in qs)))
        print(f"Unit {u['unit_num']}: {u['title_ar']} -> {len(qs)} questions, Tamreens: {t_nums}")
