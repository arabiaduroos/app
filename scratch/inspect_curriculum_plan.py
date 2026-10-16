import sys, json
sys.stdout.reconfigure(encoding='utf-8')

b2 = json.load(open('scratch/b2_raw_exercises.json', encoding='utf-8'))
print(f"Book 2 Total Units: {len(b2)}")
for u in b2:
    unit_num = u['unit_num']
    exs = u['exercises']
    print(f"Unit {unit_num} ({u['title']}): {len(exs)} exercises")
    for i, ex in enumerate(exs, 1):
        hdr = ex['header_ar'].replace('\n', ' ')
        print(f"   [{i}] {hdr[:70]} ({len(ex['items'])} items)")

b3 = json.load(open('scratch/b3_raw_exercises.json', encoding='utf-8'))
print(f"\nBook 3 Total Units: {len(b3)}")
for u in b3:
    unit_num = u['unit_num']
    exs = u['exercises']
    print(f"Unit {unit_num} ({u['title']}): {len(exs)} exercises")
    for i, ex in enumerate(exs, 1):
        hdr = ex['header_ar'].replace('\n', ' ')
        print(f"   [{i}] {hdr[:70]} ({len(ex['items'])} items)")
