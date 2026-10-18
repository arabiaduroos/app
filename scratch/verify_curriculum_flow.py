import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for b_idx, b in enumerate(data['books'], 1):
    print(f"\n=== BOOK {b_idx}: {b['title_ar']} ===")
    for u in b['units'][:6]:
        flow_types = [item['type'] for item in u.get('curriculum_flow', [])]
        print(f"Unit {u['unit_num']}: {len(u.get('curriculum_flow', []))} flow items {flow_types[:6]} | {len(u.get('questions', []))} questions")
