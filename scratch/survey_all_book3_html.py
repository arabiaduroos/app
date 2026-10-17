import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-3.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)
print(f"Book 3 total sections: {len(lessons)}")

for i in range(2, len(lessons)):
    l_text = lessons[i]
    title_match = re.search(r'(الدَّرْسُ\s+[^\n<]+)', l_text)
    title = title_match.group(1) if title_match else f"Lesson {i-1}"
    
    sec_tamreens = re.findall(r'<div class="sec-hdr">✍️\s*([^<]+)</div>', l_text)
    ex_lines = re.findall(r'<div class="txt-line"><div>([0-9]+-[^<]+)</div>', l_text)
    
    print(f"\n==================== Book 3 Lesson {i-1}: {title} ====================")
    print(f"  Exercise Sections: {sec_tamreens}")
    print(f"  Numbered Exercise Prompts ({len(ex_lines)}):")
    for el in ex_lines[:8]:
        print(f"    - {el[:80]}")
    if len(ex_lines) > 8:
        print(f"    ... and {len(ex_lines)-8} more")
