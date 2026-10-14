import sys, json
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
for b in data['books']:
    for u in b['units']:
        if u['unit_num'] == 14:
            print(f"Book {b['book_num']} Unit 14: {u['title_ar']}")
            for i, blk in enumerate(u.get('blocks', [])):
                t = blk.get('text', '')
                ur = blk.get('ur', '')
                if any(w in t for w in ['نَظَرَ', 'سَكَتَ', 'جَمَعَ']) or 'سیڑھیوں' in ur:
                    print(f"   Block {i}:")
                    print(f"      text: {t}")
                    print(f"      ur:   {ur}")
                    print(f"      en:   {blk.get('en')}")
