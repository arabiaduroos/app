import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix b1_u3_q9 in Book 1 Unit 3
for q in data['books'][0]['units'][2]['questions']:
    if q.get('id') == 'b1_u3_q9':
        print("Found b1_u3_q9:", q['options'], "Answer:", q['answer'])
        # Replace 'مَفْتوحٌ' with 'مَفْتُوحٌ' in options
        q['options'] = [q['answer'] if opt == 'مَفْتوحٌ' else opt for opt in q['options']]
        print("Fixed options:", q['options'])

with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write('window.MADINAH_BOOKS = ')
    json.dump(data, f, ensure_ascii=False)
    f.write(';\nwindow.MADINAH_DATA = window.MADINAH_BOOKS;\n')

print("Fixed b1_u3_q9 and updated data/madinah_books.json and data/madinah_books.js")
