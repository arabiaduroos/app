import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\scratch\b2_raw_exercises.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

for item in raw[5:]:
    u_num = item['unit_num']
    exercises = item.get('exercises', [])
    print(f"Book 2 Unit {u_num:2d} ({item.get('title')}): {len(exercises)} exercises")
    for ex in exercises[:4]:
        hdr = ex.get('header_ar') or ex.get('title_ar') or ''
        items_cnt = len(ex.get('items', []))
        print(f"   Ex ({items_cnt} items): {hdr[:60]}")
