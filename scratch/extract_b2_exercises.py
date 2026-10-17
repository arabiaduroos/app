import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)

b2_lessons_data = []

for i in range(2, len(lessons)):
    l_text = lessons[i]
    title_match = re.search(r'(الدَّرْسُ\s+[^\n<]+)', l_text)
    title = title_match.group(1) if title_match else f"Lesson {i-1}"
    
    parts = l_text.split('✍️')
    ex_list = []
    if len(parts) > 1:
        ex_content = parts[1]
        lines = re.findall(r'<div class="txt-line"><div>(.*?)</div>(?:<div class="ur">(.*?)</div>)?</div>', ex_content)
        current_tamreen = None
        for ar, ur in lines:
            clean_ar = re.sub(r'<[^>]+>', '', ar).strip()
            clean_ur = re.sub(r'<[^>]+>', '', ur).strip() if ur else ''
            
            # Check if this line is a tamreen header like '1- أجب عن الأسئلة الآتية:' or '2- تأمل ما يلي:'
            m_num = re.match(r'^([0-9]+)\s*-\s*(.*)', clean_ar)
            if m_num:
                num = int(m_num.group(1))
                t_title = m_num.group(2)
                current_tamreen = {"num": num, "title_ar": t_title, "title_ur": clean_ur, "items": []}
                ex_list.append(current_tamreen)
            elif current_tamreen is not None:
                if clean_ar and not clean_ar.startswith('####'):
                    current_tamreen["items"].append((clean_ar, clean_ur))
                    
    b2_lessons_data.append({"lesson_num": i-1, "title": title, "tamreens": ex_list})

print(f"Parsed {len(b2_lessons_data)} lessons for Book 2.")
for ld in b2_lessons_data:
    t_summary = [f"T{t['num']} ({len(t['items'])} items)" for t in ld['tamreens']]
    print(f"Lesson {ld['lesson_num']:2d} ({ld['title'][:25]}): {len(ld['tamreens'])} tamreens -> {', '.join(t_summary[:5])}")
