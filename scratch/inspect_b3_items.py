import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\scratch\b3_raw_exercises.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

for item in raw:
    u_num = item['unit_num']
    exercises = item.get('exercises', [])
    print(f"\n================ Book 3 Unit {u_num}: {item.get('title')} ================")
    for ex_idx, ex in enumerate(exercises, 1):
        hdr = ex.get('header_ar') or ex.get('title_ar') or f'Ex {ex_idx}'
        items = ex.get('items', [])
        print(f"  Tamreen {ex_idx} ({len(items)} items): {hdr[:60]}")
        for it in items[:2]:
            print(f"     -> ar: {it.get('ar', '')[:50]}")
