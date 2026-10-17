import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

b1 = data['books'][0]
print(f"Book 1: {b1['title_ar']} ({len(b1['units'])} units)")
for u in b1['units']:
    qs = u.get('questions', [])
    tamreens = sorted(list(set(q.get('tamreen_num') for q in qs)))
    types = set(q.get('type') for q in qs)
    print(f"  {u['id']} ({u.get('title')}): {len(qs)} questions across tamreens {tamreens}")
