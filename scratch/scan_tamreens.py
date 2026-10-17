import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Book 3 Unit 1, Book 3 Unit 2, Book 2 Unit 1, Book 2 Unit 2 to see the exercise format
lessons = re.split(r'\n###\s+', text)
print(f"Total sections split by '### ': {len(lessons)}")

for l in lessons:
    first_line = l.split('\n')[0]
    if 'الدَّرْسُ الْأَوَّلُ — الْإِعْرَابُ' in first_line or 'الدَّرْسُ الثَّانِي — وَاوُ الْحَالِ' in first_line:
        print(f"\n==================== {first_line} ====================")
        # Find all tamreens or bold lines or numbered lists
        lines = l.split('\n')
        for idx, line in enumerate(lines):
            if any(k in line for k in ['تَمْرِين', 'التَّمْرِين', 'تَمَارِين', 'التَّمَارِين', 'اقْرَأْ', 'أَجِبْ', 'تَأَمَّلْ', 'عَيِّنْ', 'اسْتَخْرِجْ', 'هَاتِ']):
                print(f"  Line {idx}: {line[:120]}")
