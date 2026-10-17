with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if 'unit-card' in line or 'renderunit' in line.lower() or 'unitslist' in line.lower():
        print(f"Line {i}: {line.strip()[:100]}")
