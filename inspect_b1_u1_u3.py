import json

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
b1 = data['books'][0]

for u_idx in [0, 1, 2]:
    u = b1['units'][u_idx]
    print(f"\n==================== UNIT {u_idx+1}: {u['title_ar']} ====================")
    for b_idx, blk in enumerate(u.get('blocks', [])):
        bt = blk.get('type')
        txt = blk.get('text', '')
        ur = blk.get('ur', '')
        en = blk.get('en', '')
        if bt == 'emoji_grid':
            cards = blk.get('cards', [])
            print(f"Block {b_idx+1} [emoji_grid] ({len(cards)} cards): {[c.get('text') for c in cards]}")
        else:
            print(f"Block {b_idx+1} [{bt}]: {txt}")
            if ur or en:
                print(f"    UR: {ur}")
                print(f"    EN: {en}")
