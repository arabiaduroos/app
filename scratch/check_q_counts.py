import json
import sys

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for b in data['books']:
    print(f"\n================ BOOK {b.get('book_id', b.get('id'))} ================")
    for u in b.get('units', []):
        uid = u.get('id') or u.get('unit_id')
        title = u.get('title') or u.get('unit_title')
        q_count = len(u.get('questions', []))
        sys.stdout.buffer.write(f"Unit {uid}: {title} -> {q_count} questions\n".encode('utf-8'))
