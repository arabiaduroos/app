import sys, json
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
for b in data['books']:
    for u in b['units']:
        for q in u.get('questions', []):
            if 'وَقَفَ السَّائِقُ' in q.get('prompt_ar', ''):
                print(json.dumps(q, ensure_ascii=False, indent=2))
