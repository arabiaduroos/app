import sys, json
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))

for b_idx, book in enumerate(data['books']):
    print(f"\n=================== BOOK {b_idx+1}: {book.get('title_ar')} ===================")
    mismatches = 0
    total_q = 0
    for u_idx, unit in enumerate(book['units']):
        qs = unit.get('questions', [])
        total_q += len(qs)
        for q in qs:
            p_ar = q.get('prompt_ar', '')
            p_ur = q.get('prompt_ur', '')
            # Check if prompt_ur is identical to prompt_ar or empty
            if p_ar and p_ur:
                if p_ar.strip() == p_ur.strip():
                    mismatches += 1
                    print(f"Mismatch in Unit {u_idx+1} Q {q.get('id')}: AR='{p_ar}' UR='{p_ur}'")
    print(f"Total Questions: {total_q}, Exact Arabic == Urdu duplicates: {mismatches}")
