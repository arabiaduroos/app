import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\scratch\b3_raw_exercises.json', 'r', encoding='utf-8') as f:
    b3_raw = json.load(f)

print("=== SAMPLE ITEMS FROM BOOK 3 ===")
for item in b3_raw[:4]:
    u_num = item['unit_num']
    print(f"\nUnit {u_num}: {item['title']}")
    for ex in item['exercises'][:3]:
        hdr = ex.get('header_ar') or ''
        items = ex.get('items', [])
        print(f"  Ex: {hdr[:50]} (items: {len(items)})")
        for it in items[:3]:
            print(f"     ar: {it.get('ar')}")
            print(f"     ur: {it.get('ur')}")
