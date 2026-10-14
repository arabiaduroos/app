import json

with open('scratch_b3_texts.json', encoding='utf-8') as f:
    texts = json.load(f)

with open('unit2_dump.txt', 'w', encoding='utf-8') as out:
    for idx in range(10, 103):
        item = texts[idx]
        spk = f"[{item['speaker']}] " if item.get('speaker') else ""
        out.write(f"--- ITEM {idx} ({item['type']}) {spk}---\n{item['ar']}\n\n")
