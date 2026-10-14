import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-1.html', encoding='utf-8') as f:
    lines = f.readlines()

print('Total lines in Madinah-Book-1.html:', len(lines))
for i, line in enumerate(lines[:100]):
    print(f'{i+1}: {line.strip()[:100]}')
