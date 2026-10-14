import json, sys
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('data/madinah_books.json', encoding='utf-8'))
u1 = d['books'][0]['units'][0]
print(f"\nUnit 1 Questions: ({len(u1.get('questions', []))})")
for i, q in enumerate(u1.get('questions', [])):
    print(f"Q{i+1}: Tamreen={q.get('tamreen_num')} [{q.get('type')}] prompt='{q.get('prompt_ar')}', ans='{q.get('answer')}'")
