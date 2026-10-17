import json

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for b in data['books']:
    u = b['units'][0]
    print(f"Book {b.get('book_num')} unit 0 keys: {list(u.keys())}")
    print(f"  title_ar: {u.get('title_ar')}")
    print(f"  title_en: {u.get('title_en')}")
