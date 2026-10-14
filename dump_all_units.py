import json

with open('scratch_b3_texts.json', encoding='utf-8') as f:
    texts = json.load(f)

by_unit = {}
for idx, item in enumerate(texts):
    u = item['unit']
    by_unit.setdefault(u, []).append((idx, item))

for u in sorted(by_unit.keys()):
    with open(f'unit_{u}_dump.txt', 'w', encoding='utf-8') as out:
        for idx, item in by_unit[u]:
            spk = f"[{item['speaker']}] " if item.get('speaker') else ""
            out.write(f"--- ITEM {idx} ({item['type']}) {spk}---\n{item['ar']}\n\n")

print("Dumped all units to unit_X_dump.txt files")
