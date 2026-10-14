import json, re

d = json.load(open('data/madinah_books.json', encoding='utf-8'))
count = 0
for b in d['books']:
    for u in b['units']:
        for blk in u.get('blocks', []):
            for r in blk.get('rows', []):
                en = r.get('english', '')
                # Check if english field contains Arabic script
                if re.search(r'[\u0600-\u06ff]', en) and not re.search(r'[a-zA-Z]', en):
                    print(f"Book {b['book_num']} Unit {u['unit_num']} Block '{blk.get('heading','')}' has Arabic in 'english': {en[:50]}")
                    count += 1

print(f"Total rows with Arabic in English field: {count}")
