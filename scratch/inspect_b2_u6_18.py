import sys, json
sys.stdout.reconfigure(encoding='utf-8')

b2 = json.load(open('scratch/b2_raw_exercises.json', encoding='utf-8'))
for u in b2[5:18]:
    u_num = u['unit_num']
    print(f"\n==================== UNIT {u_num}: {u['title']} ====================")
    for i, ex in enumerate(u['exercises'], 1):
        hdr = ex['header_ar'].replace('\n', ' ')
        items = ex['items']
        print(f"  Ex [{i}] ({len(items)} items): {hdr[:80]}")
        for j, it in enumerate(items[:3], 1):
            ar = it.get('ar', '').replace('\n', ' ')
            print(f"     ({j}) {ar[:70]}")
