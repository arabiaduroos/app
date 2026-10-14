import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for b_num in [1, 2, 3]:
    fname = f'transcriptions/Madinah-Book-{b_num}.html'
    try:
        content = open(fname, encoding='utf-8').read()
        print(f"Book {b_num} HTML length: {len(content)}")
        # Count sections
        sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\']', content)
        print(f"  Sections found: {len(sections)}, examples: {sections[:5]}")
    except Exception as e:
        print(f"Book {b_num} error: {e}")
