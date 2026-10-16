import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

b2 = d['books'][1]
print(f"Book 2 has {len(b2['units'])} units:")
total_q = 0
for u in b2['units']:
    q_count = len(u.get('questions', []))
    total_q += q_count
    tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in u.get('questions', []))))
    print(f"  Unit {u['unit_num']:2d} ({u['id']}): {q_count} questions | Tamreens: {tamreens}")
print(f"Total Book 2 questions currently: {total_q}")
