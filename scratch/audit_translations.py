import json, re

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
print(f"Loaded {len(data['books'])} books.")

arabic_chars = re.compile(r'[\u0600-\u06ff]')
latin_chars = re.compile(r'[a-zA-Z]')

bad_en_count = 0
bad_ur_count = 0

for b_idx, book in enumerate(data['books'], 1):
    for u_idx, unit in enumerate(book['units'], 1):
        for blk_idx, blk in enumerate(unit.get('blocks', [])):
            en = blk.get('english', '')
            ur = blk.get('urdu', '')
            ar = blk.get('arabic', '')
            
            # Bad english: has Arabic and no Latin letters
            if en and arabic_chars.search(en) and not latin_chars.search(en):
                bad_en_count += 1
                if bad_en_count <= 10:
                    print(f"Book {b_idx} Unit {u_idx} Blk {blk_idx} Bad EN: ar='{ar[:20]}' en='{en[:30]}'")
            
            # Bad english: identical to arabic
            elif en and en.strip() == ar.strip():
                bad_en_count += 1
                if bad_en_count <= 10:
                    print(f"Book {b_idx} Unit {u_idx} Blk {blk_idx} Identical EN: ar='{ar[:20]}' en='{en[:30]}'")

print(f"Total bad English fields found: {bad_en_count}")
print(f"Total bad Urdu fields found: {bad_ur_count}")
