import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all lines starting with '####' or containing 'تمارين' or 'تمرين'
lines = text.split('\n')
print(f"Total lines in file: {len(lines)}")

exercise_sections = []
current_lesson = ""
current_book = ""

for i, line in enumerate(lines):
    if line.startswith('## '):
        current_book = line
    elif line.startswith('### '):
        current_lesson = line
    elif '####' in line or 'تمارين' in line or 'تَمَارِين' in line or 'تَمْرِين' in line:
        exercise_sections.append((i, current_book, current_lesson, line))

print(f"Total exercise markers found: {len(exercise_sections)}")
for item in exercise_sections[:40]:
    print(f"L{item[0]}: [{item[2][:30]}] {item[3]}")
