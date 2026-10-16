import sys, json
sys.stdout.reconfigure(encoding='utf-8')

b3 = json.load(open('scratch/b3_raw_exercises.json', encoding='utf-8'))
for u in b3:
    u_num = u['unit_num']
    print(f"\n==================== BOOK 3 UNIT {u_num}: {u['title']} ====================")
    for i, ex in enumerate(u['exercises'], 1):
        hdr = ex['header_ar'].replace('\n', ' ')
        items = ex['items']
        print(f"  Ex [{i}] ({len(items)} items): {hdr[:80]}")
        for j, it in enumerate(items[:2], 1):
            ar = it.get('ar', '').replace('\n', ' ')
            print(f"     ({j}) {ar[:70]}")
