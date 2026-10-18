import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for level 2 headings
h2s = re.findall(r'^##\s+(.+)$', text, re.MULTILINE)
print("H2 headings:", h2s)

# Look for level 3 headings
h3s = re.findall(r'^###\s+(.+)$', text, re.MULTILINE)
print(f"Total H3 headings: {len(h3s)}")
print("First 10 H3 headings:")
for h in h3s[:10]:
    print(" ", h)
