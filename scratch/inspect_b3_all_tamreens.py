import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\scratch\b3_raw_exercises.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

for item in raw:
    u_num = item['unit_num']
    print(f"\n=== BOOK 3 UNIT {u_num}: {item.get('title')} ===")
    for ex_idx, ex in enumerate(item.get('exercises', []), 1):
        header = ex.get('header_ar') or ex.get('title_ar') or f'Ex {ex_idx}'
        items_count = len(ex.get('items', []))
        print(f"  Tamreen {ex_idx} ({items_count} items): {header[:70]}")
