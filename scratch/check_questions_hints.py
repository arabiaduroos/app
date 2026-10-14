import json, re

data = json.load(open('data/madinah_books.json', encoding='utf-8'))
for b in data['books']:
    for u in b['units']:
        for q in u.get('questions', []):
            hint_en = q.get('hint_en', '')
            hint_ur = q.get('hint_ur', '')
            prompt_ar = q.get('prompt_ar', '')
            
            # Check if hint_en equals prompt_ar or has pure arabic
            if hint_en and (hint_en == prompt_ar or (re.search(r'[\u0600-\u06ff]', hint_en) and not re.search(r'[a-zA-Z]', hint_en))):
                print(f"B{b['book_num']} U{u['unit_num']} Q {q.get('id')}: hint_en equals arabic! '{hint_en}'")
                
            if hint_ur and hint_ur == prompt_ar:
                print(f"B{b['book_num']} U{u['unit_num']} Q {q.get('id')}: hint_ur equals arabic! '{hint_ur}'")
print("Check completed.")
