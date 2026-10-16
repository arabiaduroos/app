import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/b3_raw_exercises.json', 'r', encoding='utf-8') as f:
    b3 = json.load(f)

for u in b3:
    print(f"\n=================== Book 3 Unit {u['unit_num']}: {u['title']} ({len(u['exercises'])} exercises) ===================")
    for i, ex in enumerate(u['exercises']):
        print(f"  Ex {i+1}: {ex['header_ar'][:70]} ({len(ex['items'])} items)")
        for item in ex['items'][:2]:
            print(f"      - {item['ar'][:65]}")
