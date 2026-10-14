import sys, json, os
sys.stdout.reconfigure(encoding='utf-8')

# Load existing books dataset
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Current questions count:")
for i, b in enumerate(data['books']):
    q_count = sum(len(u.get('questions', [])) for u in b['units'])
    print(f"Book {i+1}: {len(b['units'])} units, {q_count} questions")
