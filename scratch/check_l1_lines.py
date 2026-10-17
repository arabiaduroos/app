import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

lessons = re.split(r'<h2[^>]*>', html)
l1 = lessons[2]
lines = re.findall(r'<div class="txt-line"><div>(.*?)</div>', l1)
print('Total txt-lines in Lesson 1:', len(lines))
for i, line in enumerate(lines):
    if any(k in line for k in ['أجب', 'تأمل', 'اقرأ', 'أدخل', 'صل', 'كون', 'تمارين']):
        print(f'{i}: {line[:80]}')
