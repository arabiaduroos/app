import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for "تمارين" in Book 2 HTML and print what follows each one!
pos = 0
ex_count = 0
while True:
    pos = text.find('تمارين', pos)
    if pos == -1:
        break
    ex_count += 1
    # print surrounding text (up to 800 chars)
    snippet = text[max(0, pos-100):pos+600]
    # extract txt-lines
    lines = re.findall(r'<div class="txt-line"><div>(.*?)</div><div class="ur">(.*?)</div></div>', snippet)
    print(f"\n--- Exercise #{ex_count} (at pos {pos}) ---")
    for ar, ur in lines[:8]:
        print(f"  AR: {ar[:70]}")
        print(f"  UR: {ur[:70]}")
    pos += 6
    if ex_count >= 10:
        break
