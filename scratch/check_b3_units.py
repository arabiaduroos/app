import json
import sys

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for b in data['books']:
    if b.get('book_num') == 3:
        for u in b.get('units', []):
            sys.stdout.buffer.write(f"id: {u['id']}, unit_num: {u.get('unit_num')}, anchor: {u.get('anchor')}, title_ar: {u.get('title_ar')}, topic_en: {u.get('topic_en')}, q_count: {len(u.get('questions', []))}\n".encode('utf-8'))
