# -*- coding: utf-8 -*-
"""
Master Synchronization and Verification Script for Madinah Arabic Books 1, 2, 3
Incorporates comprehensive exercises for all units, with special focus on Book 3 Unit 9 (17 Tamreens).
"""

import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(r'C:\Users\Person\Desktop\Dr Vaniya Ar\scratch')

from build_b2_expanded_curriculum import get_b2_complete_curriculum
from build_b3_u1_u8 import get_b3_units_1_to_8
from build_b3_u9_questions import get_b3_u9_complete_questions
from build_b3_u10_u17 import get_b3_units_10_to_17

print("Loading existing base dataset...")
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# -----------------------------------------------------------------------------
# 1. BOOK 2 UPDATE
# -----------------------------------------------------------------------------
b2_curriculum = get_b2_complete_curriculum()
b2_units = data['books'][1]['units']
print(f"\nUpdating Book 2 ({len(b2_units)} units)...")

b2_q_total = 0
for u_idx, u in enumerate(b2_units):
    u_num = u_idx + 1
    if u_num in b2_curriculum:
        qs = b2_curriculum[u_num]
        u['questions'] = qs
        b2_q_total += len(qs)
        tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in qs)))
        print(f"  B2 Unit {u_num:2d} -> {len(qs):2d} questions (Tamreens: {tamreens})")
    else:
        print(f"  ERROR: B2 Unit {u_num} missing from b2_curriculum!")

print(f"Book 2 total questions: {b2_q_total}")

# -----------------------------------------------------------------------------
# 2. BOOK 3 UPDATE
# -----------------------------------------------------------------------------
b3_curriculum = {}
b3_curriculum.update(get_b3_units_1_to_8())
b3_curriculum[9] = get_b3_u9_complete_questions()
b3_curriculum.update(get_b3_units_10_to_17())

b3_units = data['books'][2]['units']
print(f"\nUpdating Book 3 ({len(b3_units)} units)...")

b3_q_total = 0
for u_idx, u in enumerate(b3_units):
    u_num = u_idx + 1
    if u_num in b3_curriculum:
        qs = b3_curriculum[u_num]
        u['questions'] = qs
        b3_q_total += len(qs)
        tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in qs)))
        print(f"  B3 Unit {u_num:2d} -> {len(qs):2d} questions (Tamreens: {tamreens})")
    else:
        print(f"  ERROR: B3 Unit {u_num} missing from b3_curriculum!")

print(f"Book 3 total questions: {b3_q_total}")

# -----------------------------------------------------------------------------
# 3. GLOBAL RIGOROUS VALIDATION
# -----------------------------------------------------------------------------
print("\n" + "="*70)
print("RUNNING GLOBAL RIGOROUS INTEGRITY VALIDATION")
print("="*70)

validation_errors = 0
grand_total_q = 0

for b_idx, b in enumerate(data['books']):
    b_num = b_idx + 1
    b_title = b.get('title_ar') or f"Book {b_num}"
    u_list = b.get('units', [])
    b_q_cnt = 0
    print(f"\nValidating Book {b_num}: {b_title} ({len(u_list)} units)...")
    
    for u_idx, u in enumerate(u_list):
        u_num = u_idx + 1
        qs = u.get('questions', [])
        b_q_cnt += len(qs)
        
        if len(qs) == 0:
            print(f"  [CRITICAL ERROR] Unit {u.get('id')} has 0 questions!")
            validation_errors += 1
            
        for q_idx, q in enumerate(qs):
            qid = q.get('id', f'q_{q_idx}')
            p_ar = q.get('prompt_ar', '').strip()
            p_ur = q.get('prompt_ur', '').strip()
            p_en = q.get('prompt_en', '').strip()
            ans = q.get('answer', '').strip()
            opts = q.get('options', [])
            t_num = q.get('tamreen_num')
            
            # Check 1: Empty prompts
            if not p_ar:
                print(f"  [ERROR] Empty Arabic prompt in {qid}")
                validation_errors += 1
            if not p_ur:
                print(f"  [ERROR] Empty Urdu prompt in {qid}")
                validation_errors += 1
            if not p_en:
                print(f"  [ERROR] Empty English prompt in {qid}")
                validation_errors += 1
                
            # Check 2: Translation matching Arabic
            if p_ar == p_ur:
                print(f"  [ERROR] Arabic duplicate in Urdu prompt in {qid}: {p_ar}")
                validation_errors += 1
            if p_ar == p_en:
                print(f"  [ERROR] Arabic duplicate in English prompt in {qid}: {p_ar}")
                validation_errors += 1
                
            # Check 3: Answer in options
            if q.get('type') not in ('match_pairs', 'pair_match'):
                if ans not in opts:
                    print(f"  [ERROR] Answer '{ans}' not found in options {opts} in {qid}")
                    validation_errors += 1
                    
            # Check 4: Tamreen num
            if not t_num or not isinstance(t_num, int):
                print(f"  [ERROR] Invalid tamreen_num '{t_num}' in {qid}")
                validation_errors += 1

    print(f"Book {b_num} total verified questions: {b_q_cnt}")
    grand_total_q += b_q_cnt

print("\n" + "="*70)
print(f"GRAND TOTAL QUESTIONS ACROSS ALL 3 BOOKS: {grand_total_q}")
print(f"TOTAL VALIDATION ERRORS: {validation_errors}")
print("="*70)

if validation_errors == 0:
    print("\nSUCCESS: All data passed 100% of strict validation checks!")
    print("Writing to data/madinah_books.json...")
    with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("Writing to data/madinah_books.js...")
    with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
        f.write('window.MADINAH_BOOKS = ')
        json.dump(data, f, ensure_ascii=False)
        f.write(';\nwindow.MADINAH_DATA = window.MADINAH_BOOKS;\n')
        
    print("All files updated successfully!")
else:
    print(f"\nABORTING WRITE: {validation_errors} errors found! Please fix before updating dataset.")
