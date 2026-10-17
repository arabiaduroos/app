import json

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

samples = []
for b in data['books']:
    for u in b.get('units', []):
        if u.get('questions'):
            samples.append({
                'book': b.get('book_id') or b.get('id'),
                'unit': u.get('id'),
                'tamreens_in_unit': list(set(q.get('tamreen_num') for q in u['questions'])),
                'q_sample': u['questions'][:3]
            })
            if len(samples) >= 4:
                break
    if len(samples) >= 4:
        break

with open('scratch/sample_q.json', 'w', encoding='utf-8') as out:
    json.dump(samples, out, indent=2, ensure_ascii=False)

print("Saved samples to scratch/sample_q.json")
