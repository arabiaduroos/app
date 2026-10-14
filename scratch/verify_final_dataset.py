import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))

print("=== FINAL DATASET VERIFICATION ===")
total_questions = 0

expected_units = {1: 23, 2: 31, 3: 17}

for book in data['books']:
    b_num = book['book_num']
    units = book['units']
    print(f"\nBook {b_num}: {len(units)} units (Expected: {expected_units[b_num]})")
    assert len(units) == expected_units[b_num], f"Unit count mismatch for Book {b_num}"
    
    b_q_count = 0
    for u in units:
        u_num = u['unit_num']
        qs = u.get('questions', [])
        b_q_count += len(qs)
        assert len(qs) > 0, f"Book {b_num} Unit {u_num} has 0 questions!"
        
        # Check tamreens
        tamreens = sorted(list(set(q.get('tamreen_num', 1) for q in qs)))
        
        # Check that no questions have bad data
        for q in qs:
            assert q.get('prompt_ar'), f"Missing prompt_ar in {q.get('id')}"
            assert q.get('answer'), f"Missing answer in {q.get('id')}"
            assert q.get('badge_ar'), f"Missing badge_ar in {q.get('id')}"
            assert q.get('tamreen_num'), f"Missing tamreen_num in {q.get('id')}"
            
    print(f"  Total questions in Book {b_num}: {b_q_count}")
    total_questions += b_q_count

print(f"\nALL CHECKS PASSED! Total questions across all 3 books: {total_questions}")
