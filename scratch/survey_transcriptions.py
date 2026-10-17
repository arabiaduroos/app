import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

headings = re.findall(r'^(#+ [^\n]+)', text, re.MULTILINE)
print(f"Total markdown headings: {len(headings)}")

# Find all book headings and lesson headings
current_book = None
book_lessons = {}
for h in headings:
    if 'الكتاب' in h or 'الجزء' in h or 'المجلد' in h or 'Book' in h:
        current_book = h
        book_lessons[current_book] = []
    elif 'الدرس' in h or 'الدَّرْسُ' in h:
        if current_book not in book_lessons:
            book_lessons[current_book] = []
        book_lessons[current_book].append(h)

for b, l_list in book_lessons.items():
    print(f"\n{b} -> {len(l_list)} lessons")
    for l in l_list[:5]:
        print(f"  {l}")
    if len(l_list) > 5:
        print(f"  ... and {len(l_list) - 5} more")
