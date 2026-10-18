import json, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('scratch/tamreens_overview.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for b_name in list(d.keys())[:2]:
    print(f"\n*** {b_name} ***")
    for u in d[b_name]:
        print(f"{u['unit_id'].upper()} ({u['title_ar']} - {u['topic_en']}) [{u['total_questions']} qs]:")
        for t in u['tamreens']:
            print(f"   - Ex {t['num']}: {t['badge_ur']} | {t['badge_en']} ({t['count']} questions)")
