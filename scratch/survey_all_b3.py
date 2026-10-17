import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'\n##\s+', text)
book3_text = ""
for p in parts:
    if 'الجزء الثالث' in p or 'الْجُزْءُ الثَّالِثُ' in p:
        book3_text = p
        break

lessons = re.split(r'\n###\s+', book3_text)

for idx in range(1, len(lessons)):
    l = lessons[idx]
    header = l.split('\n')[0]
    tamreen_parts = re.split(r'####\s*✍️\s*تمـ*ارِين*|####\s*✍️\s*تمـ*ارين', l)
    if len(tamreen_parts) > 1:
        ex_content = tamreen_parts[1]
        print(f"\n==================== Lesson {idx}: {header[:50]} ====================")
        lines = [line for line in ex_content.split('\n') if line.strip() and not line.startswith('---')]
        print(f"Total non-empty lines in exercises: {len(lines)}")
        for line in lines[:10]:
            print(f"  {line[:100]}")
