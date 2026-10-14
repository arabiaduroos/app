import sys, json
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
for b in data['books']:
    for u in b['units']:
        for blk in u.get('blocks', []):
            if 'سَكَتَ' in blk.get('text', ''):
                print(f"B{b['book_num']} U{u['unit_num']}:", blk)
