import sys, re

sys.stdout.reconfigure(encoding='utf-8')

for b_num, fname in [(2, 'transcriptions/Madinah-Book-2.html'), (3, 'transcriptions/Madinah-Book-3.html')]:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # search for lesson markers
    pattern = re.compile(r'<div class="txt-line"><div>\s*(?:\([0-9]+\)\s*)?(الْدَّرْسُ|الدَّرْسُ|الدرس)\s+([^<]+)</div><div class="ur">([^<]+)</div></div>')
    matches = list(pattern.finditer(html))
    print(f"\nBook {b_num} ({fname}): {len(matches)} matches")
    for i, m in enumerate(matches):
        print(f"  Lesson {i+1}: {m.group(1)} {m.group(2)}  |  {m.group(3)}")
