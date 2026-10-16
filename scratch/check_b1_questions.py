import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

b1 = d['books'][0]
print(f"Book 1 has {len(b1['units'])} units:")
for u in b1['units']:
    q_count = len(u.get('questions', []))
    tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in u.get('questions', []))))
    print(f"  Unit {u['unit_num']:2d} ({u['id']}): {q_count} questions | Tamreens: {tamreens}")
