import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('data/madinah_books.json', encoding='utf-8'))
u3 = d['books'][0]['units'][2]
print('Total blocks in b1_u3:', len(u3['blocks']))
for i, b in enumerate(u3['blocks']):
    txt = b.get('text', '') or b.get('arabic', '')
    print(f"Block {i}: type={b.get('type')}, sec={b.get('section')}, title={b.get('title_ar')}, text={txt[:35]}, words={len(b.get('words', []))}")
