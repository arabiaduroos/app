import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('data/madinah_books.json', encoding='utf-8'))
u3 = d['books'][0]['units'][2]
print(f"Unit 3 total questions: {len(u3.get('questions', []))}")
tamreens = {}
for q in u3.get('questions', []):
    tnum = q.get('tamreen_num', 1)
    tamreens[tnum] = tamreens.get(tnum, 0) + 1
print("Tamreens in questions:", tamreens)
for i, q in enumerate(u3.get('questions', [])):
    print(f"[{i}] T{q.get('tamreen_num')} type={q.get('type')}: prompt={q.get('prompt_ar')} ans={q.get('answer')}")
