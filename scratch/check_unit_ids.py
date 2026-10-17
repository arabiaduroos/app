import json

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for b_idx, b in enumerate(data['books']):
    print(f"\nBook index {b_idx}: book_id={b.get('book_id')}, book_num={b.get('book_num')}, total units={len(b.get('units', []))}")
    for u in b.get('units', []):
        print(f"  {u.get('id')}: unit_num={u.get('unit_num')}, title={u.get('title')}")
