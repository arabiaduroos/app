import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('data/madinah_books.json', encoding='utf-8'))
print('Books:', len(d['books']))
for b in d['books']:
    b_id = b.get('book_id') or b.get('id') or b.get('book_num') or b.get('title_ar')
    total_q = sum(len(u.get('questions', [])) for u in b['units'])
    print(f"Book {b_id} (keys: {list(b.keys())}): {len(b['units'])} units, total questions: {total_q}")
    for u in b['units'][:3]:
        q_types = set(q.get('type') for q in u.get('questions', []))
        tamreens = set(q.get('tamreen') for q in u.get('questions', []) if 'tamreen' in q)
        print(f"   Unit {u.get('unit_num')} ({u.get('title_ar')}): {len(u.get('questions', []))} questions, types: {q_types}, tamreens: {tamreens}")
