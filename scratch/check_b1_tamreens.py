import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== Book 1 Current Tamreens ===")
for u_idx, u in enumerate(data['books'][0]['units']):
    qs = u.get('questions', [])
    t_set = sorted(list(set(q.get('tamreen_num') for q in qs)))
    print(f"Unit {u_idx+1} ({u.get('title_ar')}): {len(qs)} questions, Tamreens: {t_set}")
