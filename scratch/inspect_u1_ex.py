import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-1.html', encoding='utf-8') as f:
    content = f.read()

u3_start = content.find('id="b1_u3"')
u4_start = content.find('id="b1_u4"')
u3_content = content[u3_start:u4_start]

lines = u3_content.split('</div>')
print(f"Total div blocks in Unit 3: {len(lines)}")
for l in lines:
    clean = re.sub(r'<[^>]+>', ' ', l).strip()
    if any(k in clean for k in ['تمرين', 'تـمـــــارين', 'تمارين', 'اقرأ', 'اِقرأ', 'امْلَأ', 'صل']):
        print('->', clean[:100])
print(f"Total div blocks in Unit 2: {len(lines)}")
for l in lines:
    clean = re.sub(r'<[^>]+>', ' ', l).strip()
    if clean:
        print('->', clean[:100])
