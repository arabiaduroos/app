import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')
b2_secs = re.split(r'\n###\s+', text[b2_idx:b3_idx])[2:]

# Let's inspect how exercises are labeled in each lesson of Book 2
for idx, sec in enumerate(b2_secs, 1):
    lines = [l.strip() for l in sec.split('\n') if l.strip()]
    header = lines[0]
    # Find all exercise headers
    exs = []
    for l in lines:
        if re.match(r'^(?:-\s*)?(?:[0-9]+|[۱-۹]+|\([0-9]+\))\s*[\-\.]\s*', l):
            exs.append(l[:60])
        elif l.startswith('#### ✍️') and not any(k in l for k in ['تمارين', 'تـمـارين', 'تَمَارِيْن']):
            exs.append(l[:60])
    print(f"B2 L{idx} ({header[:35]}): {len(exs)} exercises")
