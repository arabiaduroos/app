# -*- coding: utf-8 -*-
"""
Master Curriculum Synchronizer and Verifier
Generates, validates, and syncs Book 1, Book 2, and Book 3.
"""
import json, sys, os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(r'C:\Users\Person\Desktop\Dr Vaniya Ar\scratch')

from build_b2_expanded_curriculum import get_b2_complete_curriculum
from build_b3_full_units import get_b3_complete_dataset
from build_b3_u10_u17_deep import get_b3_units_10_to_17_deep

print("=== 1. Loading existing base dataset ===")
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Book 1: Already has 208 questions across all 23 units
b1_units = data['books'][0]['units']
b1_total = sum(len(u.get('questions', [])) for u in b1_units)
print(f"Book 1: {len(b1_units)} units with {b1_total} questions.")

# Book 2: Complete 31 units
print("\n=== 2. Updating Book 2 (31 Units) ===")
b2_curriculum = get_b2_complete_curriculum()
b2_units = data['books'][1]['units']
b2_total = 0
for idx, u in enumerate(b2_units):
    u_num = idx + 1
    if u_num in b2_curriculum:
        qs = b2_curriculum[u_num]
        u['questions'] = qs
        b2_total += len(qs)
print(f"Book 2: Updated {len(b2_units)} units with {b2_total} questions.")

# Book 3: Deep authentic curriculum (Units 1-17)
print("\n=== 3. Updating Book 3 (17 Units) ===")
b3_full = get_b3_complete_dataset()
b3_deep_10_17 = get_b3_units_10_to_17_deep()
b3_full.update(b3_deep_10_17)

b3_units = data['books'][2]['units']
b3_total = 0
for idx, u in enumerate(b3_units):
    u_num = idx + 1
    u_id = f"b3_u{u_num}"
    if u_id in b3_full:
        qs = b3_full[u_id]
        u['questions'] = qs
        b3_total += len(qs)
        tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in qs)))
        print(f"  B3 Unit {u_num:2d} ({u.get('title')}) -> {len(qs):2d} questions (Tamreens: {tamreens})")
    else:
        print(f"  ERROR: B3 Unit {u_id} missing from dataset!")

print(f"Book 3: Updated {len(b3_units)} units with {b3_total} questions.")

# Rigorous Global Integrity Validation
print("\n=== 4. Running Rigorous Global Validation ===")
validation_errors = 0
grand_total = 0
all_q_ids = set()

for b_idx, book in enumerate(data['books']):
    b_num = b_idx + 1
    units = book.get('units', [])
    for u_idx, unit in enumerate(units):
        u_num = u_idx + 1
        qs = unit.get('questions', [])
        grand_total += len(qs)
        if len(qs) == 0:
            print(f"  [ERROR] Book {b_num} Unit {u_num} has 0 questions!")
            validation_errors += 1
        for q_idx, q in enumerate(qs):
            qid = q.get('id', f'q_{b_num}_{u_num}_{q_idx}')
            if qid in all_q_ids:
                print(f"  [ERROR] Duplicate question ID: {qid}")
                validation_errors += 1
            all_q_ids.add(qid)

            p_ar = q.get('prompt_ar', '').strip()
            p_ur = q.get('prompt_ur', '').strip()
            p_en = q.get('prompt_en', '').strip()
            ans = q.get('answer', '').strip()
            opts = q.get('options', [])

            if not p_ar:
                print(f"  [ERROR] {qid}: Empty prompt_ar!")
                validation_errors += 1
            if not p_ur and not p_en:
                print(f"  [ERROR] {qid}: Both prompt_ur and prompt_en are empty!")
                validation_errors += 1
            if q.get('type') == 'pair_match':
                if not q.get('pairs') or len(q.get('pairs')) == 0:
                    print(f"  [ERROR] {qid}: pair_match question has no pairs!")
                    validation_errors += 1
            else:
                if not ans:
                    print(f"  [ERROR] {qid}: Empty answer!")
                    validation_errors += 1
                if ans not in opts:
                    print(f"  [ERROR] {qid}: Answer '{ans}' not in options {opts}!")
                    validation_errors += 1
            if not isinstance(q.get('tamreen_num'), int) or q.get('tamreen_num') <= 0:
                print(f"  [ERROR] {qid}: Invalid tamreen_num '{q.get('tamreen_num')}'!")
                validation_errors += 1

print(f"\n==========================================")
print(f"VALIDATION SUMMARY:")
print(f"Total Books: {len(data['books'])}")
print(f"Total Units: {len(b1_units) + len(b2_units) + len(b3_units)}")
print(f"GRAND TOTAL QUESTIONS: {grand_total}")
print(f"VALIDATION ERRORS: {validation_errors}")
print(f"==========================================")

if validation_errors == 0:
    print("\nSaving updated dataset to data/madinah_books.json...")
    with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Syncing dataset to data/madinah_books.js...")
    with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
        f.write("/**\n * Madinah Arabic Course - Master Synchronized Dataset\n */\n")
        f.write("window.MADINAH_BOOKS = ")
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
        f.write(";\n\n")
        f.write("window.MADINAH_DATA = window.MADINAH_BOOKS;\n")

    print("SYNC AND VERIFICATION COMPLETE! Both JSON and JS updated successfully.")
else:
    print(f"\nABORTING SAVE due to {validation_errors} errors!")
    sys.exit(1)
