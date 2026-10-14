import sys, re, json, html
sys.stdout.reconfigure(encoding='utf-8')

# Load existing JSON
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

print(f"Loaded master_data with {len(master_data['books'])} books.")
for b in master_data['books']:
    print(f"Book {b['book_num']}: {len(b['units'])} units")
