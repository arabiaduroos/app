import sys, json
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
b2 = data['books'][1]
u14 = [u for u in b2['units'] if u['unit_num'] == 14][0]
print(f"Total blocks in Book 2 Unit 14: {len(u14.get('blocks', []))}")
for i, blk in enumerate(u14.get('blocks', [])):
    print(f"[{i:2d}] {blk.get('type')}: ar='{blk.get('text', '')}'")
    print(f"     ur='{blk.get('ur', '')}'")
    print(f"     en='{blk.get('en', '')}'")
