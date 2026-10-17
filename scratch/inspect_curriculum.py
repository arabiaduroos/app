import json

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Root keys:", list(data.keys()))
if 'books' in data:
    for i, b in enumerate(data['books']):
        print(f"Book {i} keys:", list(b.keys()))
        b_id = b.get('id') or b.get('book_id') or b.get('bookNumber') or f"Book {i+1}"
        b_title = b.get('title') or b.get('book_title') or ""
        units = b.get('units') or b.get('chapters') or []
        print(f"Book {b_id}: {b_title} with {len(units)} units")
        total_q = sum(len(u.get('questions', [])) for u in units)
        print(f"  Total questions: {total_q}")
        for u in units:
            u_id = u.get('id') or u.get('unit_id') or u.get('unitNumber')
            u_title = u.get('title') or u.get('name') or ""
            qs = u.get('questions', [])
            tamreens = sorted(list(set(q.get('tamreen_num') for q in qs if q.get('tamreen_num') is not None)))
            print(f"    Unit {u_id} ({u_title[:30]}): {len(qs)} questions across tamreens: {tamreens}")
