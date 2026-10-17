import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Book 1
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    current_data = json.load(f)

print("=== CURRENT DATASET SUMMARY ===")
for b in current_data['books']:
    b_num = b.get('book_num')
    total_q = sum(len(u.get('questions', [])) for u in b.get('units', []))
    print(f"Book {b_num}: {len(b.get('units', []))} units, total questions: {total_q}")
    for u in b.get('units', []):
        qs = u.get('questions', [])
        tamreens = sorted(list(set(q.get('tamreen_num') for q in qs if q.get('tamreen_num'))))
        print(f"  {u.get('id')}: {len(qs)} questions, tamreens: {tamreens}")
