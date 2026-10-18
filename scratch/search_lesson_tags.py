import sys, re

sys.stdout.reconfigure(encoding='utf-8')

for b_num, fname in [(2, 'transcriptions/Madinah-Book-2.html'), (3, 'transcriptions/Madinah-Book-3.html')]:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # search for any tag containing "الدرس" or "الدَّرْسُ"
    found = re.findall(r'<([^>]+)>([^<]*?(?:الْدَّرْسُ|الدَّرْسُ|الدرس)[^<]*?)</\1>', html)
    print(f"\nBook {b_num}: Total tags with 'الدرس': {len(found)}")
    seen = set()
    for tag, text in found:
        t_clean = text.strip()
        if len(t_clean) < 60 and t_clean not in seen:
            seen.add(t_clean)
            print(f"  <{tag}>: {t_clean}")
