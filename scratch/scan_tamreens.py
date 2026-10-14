import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-All-Books-Cairo.md', encoding='utf-8') as f:
    text = f.read()

# Let's find all headers with 'الدرس' or 'تمرين'
lines = text.splitlines()

current_book = ""
current_lesson = ""
lesson_tamreens = {} # (book, lesson) -> list of tamreens

for line in lines:
    line_s = line.strip()
    if 'الجزء الأول' in line_s or 'الْجُزْءُ الْأَوَّلُ' in line_s:
        current_book = "Book 1"
    elif 'الجزء الثاني' in line_s or 'الْجُزْءُ الثَّانِي' in line_s:
        current_book = "Book 2"
    elif 'الجزء الثالث' in line_s or 'الْجُزْءُ الثَّالِثُ' in line_s:
        current_book = "Book 3"

    if line_s.startswith('### ') and ('الدَّرْسُ' in line_s or 'الدرس' in line_s):
        current_lesson = line_s.replace('###', '').strip()
        key = (current_book, current_lesson)
        if key not in lesson_tamreens:
            lesson_tamreens[key] = []
    elif 'تمرين' in line_s or 'تـمـــــارين' in line_s or 'تَدْرِيب' in line_s or 'تدريب' in line_s or 'التمارين' in line_s:
        key = (current_book, current_lesson)
        if key in lesson_tamreens:
            lesson_tamreens[key].append(line_s)

print(f"Total lessons found: {len(lesson_tamreens)}")
for (b, l), t_list in list(lesson_tamreens.items())[:15]:
    print(f"\n{b} -> {l}")
    print(f"  Tamreens count: {len(t_list)}")
    for t in t_list[:8]:
        print(f"    - {t[:70]}")
