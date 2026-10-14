import os, sys, json, re

with open('scratch_b2_texts.json', encoding='utf-8') as f:
    b2_texts = json.load(f)

print(f"Total texts: {len(b2_texts)}")

# Check units
units = {}
for i, item in enumerate(b2_texts):
    u = item.get('unit', 0)
    if u not in units:
        units[u] = []
    units[u].append((i, item))

print(f"Total units: {len(units)}")
for u in sorted(units.keys()):
    print(f"Unit {u}: {len(units[u])} items")
