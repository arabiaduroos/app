import json

with open('scratch_b1_texts.json', encoding='utf-8') as f:
    texts = json.load(f)

with open('scratch_b1_dump.txt', 'w', encoding='utf-8') as out:
    for u in range(1, 24):
        unit_items = [x for x in texts if x['unit'] == u]
        out.write(f"=== UNIT {u} ({len(unit_items)} items) ===\n")
        for idx, item in enumerate(unit_items):
            spk = f"[{item['speaker']}] " if item.get('speaker') else ""
            out.write(f"  {idx+1}. ({item['type']}) {spk}{item['ar']}\n")
