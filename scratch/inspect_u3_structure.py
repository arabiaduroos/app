with open('transcriptions/Madinah-Book-1.html', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('id="b1_u3"')
idx2 = content.find('id="b1_u4"')
u3_text = content[idx1:idx2]

print("Length of u3_text:", len(u3_text))

# Print lines with class="txt-line" or class="sec-hdr" or table
import re
items = re.findall(r'<div class="(?:txt-line|sec-hdr|illus-line)">.*?</div></div>|<div class="sec-hdr">.*?</div>', u3_text, re.DOTALL)
for it in items:
    clean = re.sub(r'<.*?>', ' ', it)
    clean = ' '.join(clean.split())
    if any(k in clean for k in ['حُرُوف', 'شَمْس', 'قَمَر', 'نَجْم', 'تَاجِر', 'تَمَارِين', 'تمرين', 'الكلمات الجديدة']):
        print("MATCH:", clean)
