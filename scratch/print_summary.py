import json, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('=== MADINAH ARABIC MASTER CURRICULUM AUDIT ===')
grand_total_qs = 0
for b in data['books']:
    b_id = f"Book {b.get('book_num', '?')}"
    b_title = b['title_ar']
    units = b['units']
    total_b_qs = sum(len(u.get('questions', [])) for u in units)
    grand_total_qs += total_b_qs
    print(f"\n[{b_id.upper()}] {b_title} ({len(units)} Units, {total_b_qs} Questions):")
    for u in units:
        qs = u.get('questions', [])
        tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in qs)))
        print(f"  • {u['id'].upper()} ({u['title_ar']}): {len(qs)} qs | Tamreens: {tamreens}")

print(f"\n=======================================================")
print(f"GRAND TOTAL QUESTIONS ACROSS 71 UNITS: {grand_total_qs}")
print(f"=======================================================")
