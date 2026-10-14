import json

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
b1 = data['books'][0]
u1 = b1['units'][0]
print(f"Unit 1: {u1.get('title_ar')} ({u1.get('title_en')})")
print(f"Total blocks: {len(u1.get('blocks', []))}")
for i, b in enumerate(u1.get('blocks', [])):
    b_type = b.get('type')
    txt = b.get('text', '')
    if b_type == 'emoji_grid':
        cards = b.get('cards', [])
        print(f"Block {i+1}: emoji_grid with {len(cards)} cards: {[c.get('text') for c in cards[:4]]}")
    else:
        print(f"Block {i+1} [{b_type}]: {txt[:70]}")
