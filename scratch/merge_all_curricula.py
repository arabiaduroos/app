import sys, json, os
sys.stdout.reconfigure(encoding='utf-8')

from book2_curriculum import get_book2_questions
from book3_curriculum import get_book3_questions

# 1. Load base json
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Get Book 2 questions grouped by unit
b2_questions = get_book2_questions()
b2_by_unit = {}
for q in b2_questions:
    b2_by_unit.setdefault(q['unit_num'], []).append(q)

for u_idx, u in enumerate(data['books'][1]['units']):
    u_num = u_idx + 1
    if u_num in b2_by_unit:
        u['questions'] = b2_by_unit[u_num]

# 3. Get Book 3 questions grouped by unit
b3_questions = get_book3_questions()
b3_by_unit = {}
for q in b3_questions:
    b3_by_unit.setdefault(q['unit_num'], []).append(q)

for u_idx, u in enumerate(data['books'][2]['units']):
    u_num = u_idx + 1
    if u_num in b3_by_unit:
        u['questions'] = b3_by_unit[u_num]

# 4. Save updated json
with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 5. Save updated js file
with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write('window.MADINAH_BOOKS = ')
    json.dump(data, f, ensure_ascii=False)
    f.write(';')

print("Successfully merged and updated both data/madinah_books.json and data/madinah_books.js!")

# 6. Verification Report
print("\n=== VERIFICATION REPORT ===")
for b_idx, b in enumerate(data['books']):
    print(f"\n--- BOOK {b_idx+1}: {b.get('title_ar')} ({len(b['units'])} Units) ---")
    total_q = 0
    for u_idx, u in enumerate(b['units']):
        qs = u.get('questions', [])
        total_q += len(qs)
        t_nums = sorted(list(set(q.get('tamreen_num') for q in qs)))
        print(f"  Unit {u_idx+1} ({u.get('title_ar')}): {len(qs)} questions across Tamreens {t_nums}")
    print(f"Total Book {b_idx+1} questions: {total_q}")
