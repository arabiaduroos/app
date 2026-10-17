with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if 'id=' in line and any(k in line.lower() for k in ['tamreen', 'modal', 'quiz', 'selector']):
        print(f"Line {i}: {line.strip()}")
