import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)

for num in [15, 16, 17, 18, 20, 21, 23, 25, 26, 27, 28, 29, 30, 31]:
    idx = num + 1
    if idx < len(lessons):
        l_text = lessons[idx]
        title_match = re.search(r'(الدَّرْسُ\s+[^\n<]+)', l_text)
        title = title_match.group(1) if title_match else f"Lesson {num}"
        print(f"\n{'='*25} Book 2 Lesson {num}: {title} {'='*25}")
        
        # Find txt-lines
        lines = re.findall(r'<div class="txt-line"><div>(.*?)</div>(?:<div class="ur">(.*?)</div>)?</div>', l_text)
        ex_headers = []
        for ar, ur in lines:
            clean_ar = re.sub(r'<[^>]+>', '', ar).strip()
            norm_ar = re.sub(r'^[\u2600-\u27bf\U0001f300-\U0001f9ff\s]+', '', clean_ar)
            if re.match(r'^[0-9]+\s*-', norm_ar):
                ex_headers.append(norm_ar)
        for eh in ex_headers[:6]:
            print(f"  {eh[:75]}")
