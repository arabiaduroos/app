import json

with open(r'C:\Users\Person\Documents\GitHub\app\scratch\b3_raw_exercises.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

# Find Unit 9
for item in raw:
    if item['unit_num'] == 9:
        print("Unit 9 exercises sample:")
        for ex in item['exercises'][:4]:
            print(f"\nEx num: {ex.get('tamreen_num')}, title_ar: {ex.get('title_ar')}")
            for it in ex.get('items', [])[:3]:
                print(f"   item: {it}")
