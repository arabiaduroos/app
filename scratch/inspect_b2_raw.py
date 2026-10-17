import json
import sys

with open(r'C:\Users\Person\Documents\GitHub\app\scratch\b2_raw_exercises.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

print(f"Total units in b2_raw_exercises: {len(raw)}")
for item in raw:
    u_num = item['unit_num']
    exercises = item.get('exercises', [])
    total_items = sum(len(ex.get('items', [])) for ex in exercises)
    sys.stdout.buffer.write(f"Unit {u_num:2d}: {item.get('title')} -> {len(exercises)} exercises, {total_items} items\n".encode('utf-8'))
