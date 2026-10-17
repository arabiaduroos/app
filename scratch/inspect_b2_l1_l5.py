import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)

for i in range(2, 7): # Lessons 1 to 5
    l_text = lessons[i]
    title_match = re.search(r'(الدَّرْسُ\s+[^\n<]+)', l_text)
    title = title_match.group(1) if title_match else f"Lesson {i-1}"
    print(f"\n{'='*30} Book 2 Lesson {i-1}: {title} {'='*30}")
    
    # Split by exercise header
    parts = l_text.split('✍️')
    if len(parts) > 1:
        ex_content = parts[1]
        # Find txt-lines
        txt_lines = re.findall(r'<div class="txt-line"><div>(.*?)</div>(?:<div class="ur">(.*?)</div>)?</div>', ex_content)
        for ar, ur in txt_lines[:25]:
            # remove html tags
            clean_ar = re.sub(r'<[^>]+>', '', ar).strip()
            clean_ur = re.sub(r'<[^>]+>', '', ur).strip() if ur else ''
            print(f"  AR: {clean_ar[:60]}")
            if clean_ur and clean_ur != clean_ar:
                print(f"  UR: {clean_ur[:60]}")
