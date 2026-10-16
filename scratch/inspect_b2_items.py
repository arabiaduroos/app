import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/b2_raw_exercises.json', 'r', encoding='utf-8') as f:
    b2 = json.load(f)

for u in b2:
    if u['unit_num'] in [3, 5, 10, 14, 20, 26, 27, 28]:
        print(f"\n================ Unit {u['unit_num']}: {u['title']} ================")
        for i, ex in enumerate(u['exercises']):
            print(f"  Ex {i+1}: {ex['header_ar'][:60]} ({len(ex['items'])} items)")
            for it in ex['items'][:2]:
                print(f"     * {it['ar'][:65]}")
