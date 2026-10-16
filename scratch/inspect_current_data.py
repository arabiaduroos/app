import sys, json
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
for i, b in enumerate(data['books']):
    units = b['units']
    q_counts = [len(u.get('questions', [])) for u in units]
    total_q = sum(q_counts)
    print(f"Book {i+1}: {b.get('title_ar', '')} ({len(units)} units) - Total Questions: {total_q}")
    zeros = [u_i+1 for u_i, c in enumerate(q_counts) if c == 0]
    print(f"   Units with questions: {len(units) - len(zeros)} / {len(units)}")
    if zeros:
        print(f"   Units with 0 questions: {zeros}")
