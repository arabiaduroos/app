import json

with open(r'C:\Users\Person\Documents\GitHub\app\scratch\b3_raw_exercises.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

for item in raw:
    if item['unit_num'] == 9:
        with open('scratch/sample_u9_raw.json', 'w', encoding='utf-8') as out:
            json.dump(item, out, indent=2, ensure_ascii=False)
        print("Dumped Unit 9 to scratch/sample_u9_raw.json")
        break
