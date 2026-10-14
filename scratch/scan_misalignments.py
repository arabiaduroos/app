import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))

print("=== CHECKING FOR MISALIGNED TRANSLATIONS ACROSS ALL BOOKS ===")
mismatches = []

for b in data['books']:
    b_num = book_num = b['book_num']
    for u in b['units']:
        u_num = u['unit_num']
        for i, blk in enumerate(u.get('blocks', [])):
            ar = blk.get('text', '').strip()
            ur = blk.get('ur', '').strip()
            en = blk.get('en', '').strip()
            
            ar_words = len(ar.split())
            ur_words = len(ur.split())
            en_words = len(en.split())
            
            # If Arabic is 1-2 words, but Urdu or English is a whole dialogue / long sentence (e.g. > 7 words)
            if ar_words <= 2 and (ur_words > 7 or en_words > 7):
                mismatches.append((b_num, u_num, i, ar, ur, en))

print(f"Total severe length mismatches found: {len(mismatches)}")
for b_num, u_num, i, ar, ur, en in mismatches[:25]:
    print(f"B{b_num} U{u_num} Blk {i}: ar='{ar}' | ur='{ur[:40]}...' | en='{en[:40]}...'")
