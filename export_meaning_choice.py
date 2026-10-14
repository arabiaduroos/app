import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
books = data if isinstance(data, list) else data['books']

all_meaning_choice = []
for b in books:
    for u in b['units']:
        for qi, q in enumerate(u.get('questions', [])):
            if q.get('type') == 'meaning_choice':
                all_meaning_choice.append({
                    'book': b['book_num'],
                    'unit': u['unit_num'],
                    'qi': qi,
                    'prompt': q.get('prompt_ar'),
                    'hint_ur': q.get('hint_ur'),
                    'hint_en': q.get('hint_en'),
                    'answer': q.get('answer'),
                    'options': q.get('options')
                })

print(f"Total meaning_choice questions: {len(all_meaning_choice)}")
with open('all_meaning_choice.json', 'w', encoding='utf-8') as f:
    json.dump(all_meaning_choice, f, ensure_ascii=False, indent=2)
print("Saved to all_meaning_choice.json")
