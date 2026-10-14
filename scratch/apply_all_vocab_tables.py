import re
import json
import sys
from build_complete_vocab_tables import get_en_translation

sys.stdout.reconfigure(encoding='utf-8')

# Load raw extracted vocab
with open('scratch/extracted_vocab_raw.json', 'r', encoding='utf-8') as f:
    raw_vocab = json.load(f)

# Load existing dataset
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

b1_data = raw_vocab['b1']
b2_data = raw_vocab['b2']

# Map Book 1
b1_units = {u['id']: u for u in dataset['books'][0]['units']}
for html_uid, words in b1_data.items():
    if html_uid in b1_units:
        unit = b1_units[html_uid]
        # Remove old vocab_row blocks
        unit['blocks'] = [b for b in unit.get('blocks', []) if b.get('type') != 'vocab_row' and b.get('section') != 'vocabulary']
        
        # Build clean words list
        clean_words = []
        for w in words:
            ar = w['ar']
            ur = w['ur']
            en = get_en_translation(ar, ur)
            clean_words.append({'ar': ar, 'ur': ur, 'en': en})
        
        if clean_words:
            vocab_block = {
                'type': 'vocab_table',
                'section': 'vocabulary',
                'title_ar': 'الْكَلِمَاتُ الْجَدِيدَةُ',
                'title_ur': 'نئے الفاظ',
                'title_en': 'New Vocabulary',
                'emoji': '🗂️',
                'words': clean_words
            }
            unit['blocks'].append(vocab_block)
            print(f"Added vocab_table to Book 1 {html_uid} ({len(clean_words)} words)")

# Map Book 2: b2_u(N+1) in HTML -> b2_uN in JSON
b2_units = {u['id']: u for u in dataset['books'][1]['units']}
for html_uid, words in b2_data.items():
    m = re.match(r'b2_u(\d+)', html_uid)
    if not m:
        continue
    html_num = int(m.group(1))
    target_num = html_num - 1 # shifted due to muqaddimah
    target_id = f"b2_u{target_num}"
    
    if target_id in b2_units:
        unit = b2_units[target_id]
        # Remove old vocab_row blocks
        unit['blocks'] = [b for b in unit.get('blocks', []) if b.get('type') != 'vocab_row' and b.get('section') != 'vocabulary']
        
        # Build clean words list
        clean_words = []
        for w in words:
            ar = w['ar']
            ur = w['ur']
            en = get_en_translation(ar, ur)
            clean_words.append({'ar': ar, 'ur': ur, 'en': en})
        
        if clean_words:
            vocab_block = {
                'type': 'vocab_table',
                'section': 'vocabulary',
                'title_ar': 'الْكَلِمَاتُ الْجَدِيدَةُ',
                'title_ur': 'نئے الفاظ',
                'title_en': 'New Vocabulary',
                'emoji': '🗂️',
                'words': clean_words
            }
            unit['blocks'].append(vocab_block)
            print(f"Added vocab_table to Book 2 {target_id} from {html_uid} ({len(clean_words)} words)")

# Check if any vocab_row remains anywhere
remaining_vr = 0
for b in dataset['books']:
    for u in b['units']:
        for blk in u.get('blocks', []):
            if blk.get('type') == 'vocab_row':
                remaining_vr += 1

print(f"\nRemaining vocab_row blocks across all books: {remaining_vr}")

# Save to data/madinah_books.json
with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

# Save to data/madinah_books.js
js_content = 'window.MADINAH_BOOKS = ' + json.dumps(dataset, ensure_ascii=False) + ';\nwindow.MADINAH_DATA = window.MADINAH_BOOKS;\n'
with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Saved updated data/madinah_books.json and data/madinah_books.js successfully!")
