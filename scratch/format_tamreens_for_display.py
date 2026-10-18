import json, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('scratch/tamreens_overview.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for book_name, units in d.items():
    print(f"\n=======================================================")
    print(f"  {book_name} ({len(units)} Units)")
    print(f"=======================================================")
    for u in units:
        print(f"\n[{u['unit_id'].upper()}] {u['title_ar']} — {u['topic_en']}")
        print(f"  Total Questions: {u['total_questions']} across {len(u['tamreens'])} Tamreens:")
        for t in u['tamreens']:
            print(f"    • Tamreen ({t['num']}): {t['badge_ar']} | {t['badge_ur']} | {t['badge_en']} ({t['count']} questions)")
