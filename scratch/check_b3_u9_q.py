import json
import sys

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for b in data['books']:
    if b.get('book_num') == 3:
        for u in b.get('units', []):
            if u['id'] == 'b3_u9':
                sys.stdout.buffer.write(json.dumps(u['questions'], indent=2, ensure_ascii=False).encode('utf-8'))
