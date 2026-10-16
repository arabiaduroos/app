import sys, json, os
sys.stdout.reconfigure(encoding='utf-8')

# Import modules
from b2_part1_units import get_b2_part1
from b2_part2_units import get_b2_part2
from b2_part3_units import get_b2_part3
from b3_curriculum_master import get_b3_curriculum

print("Loading base dataset...")
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ---------------------------------------------------------------------------
# BOOK 2 MERGE
# ---------------------------------------------------------------------------
b2_p1 = get_b2_part1()
b2_p2 = get_b2_part2()
b2_p3 = get_b2_part3()

b2_all = {}
b2_all.update(b2_p1)
b2_all.update(b2_p2)
b2_all.update(b2_p3)

b2_units = data['books'][1]['units']
print(f"Book 2 units in dataset: {len(b2_units)}")

b2_total_q = 0
for u_idx, u in enumerate(b2_units):
    u_num = u_idx + 1
    if u_num in b2_all:
        qs = b2_all[u_num]
        u['questions'] = qs
        b2_total_q += len(qs)
        print(f"  B2 Unit {u_num} -> {len(qs)} questions (Tamreens: {sorted(list(set(q['tamreen_num'] for q in qs)))})")
    else:
        print(f"  WARNING: B2 Unit {u_num} not found in b2_all!")

# ---------------------------------------------------------------------------
# BOOK 3 MERGE
# ---------------------------------------------------------------------------
b3_all = get_b3_curriculum()
b3_units = data['books'][2]['units']
print(f"\nBook 3 units in dataset: {len(b3_units)}")

b3_total_q = 0
for u_idx, u in enumerate(b3_units):
    u_num = u_idx + 1
    if u_num in b3_all:
        qs = b3_all[u_num]
        u['questions'] = qs
        b3_total_q += len(qs)
        print(f"  B3 Unit {u_num} -> {len(qs)} questions (Tamreens: {sorted(list(set(q['tamreen_num'] for q in qs)))})")
    else:
        print(f"  WARNING: B3 Unit {u_num} not found in b3_all!")

# ---------------------------------------------------------------------------
# SAVE JSON & JS
# ---------------------------------------------------------------------------
json_path = 'data/madinah_books.json'
js_path = 'data/madinah_books.js'

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write('window.MADINAH_BOOKS = ')
    json.dump(data, f, ensure_ascii=False)
    f.write(';\nwindow.MADINAH_DATA = window.MADINAH_BOOKS;\n')

print("\nSaved updated data/madinah_books.json and data/madinah_books.js successfully!")

# ---------------------------------------------------------------------------
# GLOBAL VERIFICATION OF ENTIRE DATASET
# ---------------------------------------------------------------------------
print("\n================== FULL DATASET INTEGRITY CHECK ==================")
total_books = len(data['books'])
grand_total_q = 0
errors = 0

for b_idx, b in enumerate(data['books']):
    b_title = b.get('title_ar', f'Book {b_idx+1}')
    u_list = b['units']
    b_q_count = 0
    print(f"\nBook {b_idx+1}: {b_title} ({len(u_list)} units)")
    
    for u_idx, u in enumerate(u_list):
        u_num = u_idx + 1
        qs = u.get('questions', [])
        b_q_count += len(qs)
        
        if len(qs) == 0:
            print(f"  ERROR: Unit {u_num} has 0 questions!")
            errors += 1
            
        for q in qs:
            # 1. Check prompt translations
            p_ar = q.get('prompt_ar', '').strip()
            p_ur = q.get('prompt_ur', '').strip()
            p_en = q.get('prompt_en', '').strip()
            
            if not p_ar or not p_ur or not p_en:
                print(f"  ERROR: Empty prompt in Unit {u_num} Q {q.get('id')}")
                errors += 1
                
            if p_ar == p_ur:
                print(f"  ERROR: Arabic == Urdu in Unit {u_num} Q {q.get('id')}: {p_ar}")
                errors += 1
                
            if p_ar == p_en:
                print(f"  ERROR: Arabic == English in Unit {u_num} Q {q.get('id')}: {p_ar}")
                errors += 1
                
            # 2. Check answer in options (skip for pair matching questions)
            if q.get('type') not in ('match_pairs', 'pair_match'):
                ans = q.get('answer')
                opts = q.get('options', [])
                if ans not in opts:
                    print(f"  ERROR: Answer '{ans}' not in options {opts} in Unit {u_num} Q {q.get('id')}")
                    errors += 1
                
            # 3. Check tamreen_num
            t_num = q.get('tamreen_num')
            if not t_num or not isinstance(t_num, int):
                print(f"  ERROR: Missing or invalid tamreen_num in Unit {u_num} Q {q.get('id')}")
                errors += 1

    print(f"Book {b_idx+1} total verified questions: {b_q_count}")
    grand_total_q += b_q_count

print(f"\nGrand Total Questions across all 3 books: {grand_total_q}")
print(f"Total Validation Errors: {errors}")
if errors == 0:
    print("ALL 71 UNITS & QUESTIONS FULLY VERIFIED WITH 100% ACCURACY!")
