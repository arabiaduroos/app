import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Book 3 Lesson 9
b3 = [b for b in data['books'] if b['book_num'] == 3][0]
u9 = [u for u in b3['units'] if u['unit_num'] == 9][0]

print("Book 3 Unit 9 Title:", u9.get('title_ar'))
print("Total questions in B3 U9:", len(u9.get('questions', [])))
print("\nUnique tamreen_num in B3 U9:")
tamreens = {}
for q in u9.get('questions', []):
    t_num = q.get('tamreen_num')
    tamreens[t_num] = tamreens.get(t_num, 0) + 1

for t_num, count in sorted(tamreens.items()):
    sample = [q for q in u9['questions'] if q.get('tamreen_num') == t_num][0]
    print(f"Tamreen {t_num}: {count} questions | Title Ar: {sample.get('tamreen_title_ar')} | Title Ur: {sample.get('tamreen_title_ur')} | Title En: {sample.get('tamreen_title_en')}")

print("\n--- SAMPLE QUESTION ---")
print(json.dumps(u9['questions'][0], ensure_ascii=False, indent=2))
