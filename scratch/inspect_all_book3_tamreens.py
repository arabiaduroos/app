import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-3.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)

for i in range(2, len(lessons)):
    l_text = lessons[i]
    title_match = re.search(r'(الدَّرْسُ\s+[^\n<]+)', l_text)
    title = title_match.group(1) if title_match else f"Lesson {i-1}"
    
    # Extract text after the first '✍️'
    parts = l_text.split('✍️')
    if len(parts) > 1:
        ex_content = parts[1]
        # Find all numbered items like (1), (2), 1-, 2-, or bold items
        items = re.findall(r'<div class="txt-line"><div>([^<]+)</div>', ex_content)
        print(f"\n==================== Book 3 Lesson {i-1}: {title} ====================")
        print(f"  Total lines in exercises: {len(items)}")
        for it in items[:6]:
            print(f"    - {it[:80]}")
        if len(items) > 6:
            print(f"    ... and {len(items)-6} more lines")
