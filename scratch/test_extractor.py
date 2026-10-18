import sys, re

sys.stdout.reconfigure(encoding='utf-8')

for b_num in [1, 2, 3]:
    fname = f'transcriptions/Madinah-Book-{b_num}.html'
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    
    sections = re.findall(r'<section class="unit-card" id="([^"]+)">([\s\S]*?)(?=</section>)', c)
    print(f"Book {b_num}: {len(sections)} unit sections found")
    for s_id, s_content in sections[:3]:
        # get title
        m_title = re.search(r'<h2 class="unit-title">([\s\S]*?)</h2>', s_content)
        title = m_title.group(1).strip() if m_title else "No title"
        title_clean = re.sub(r'<[^>]+>', '', title).strip()
        print(f"  {s_id}: {title_clean}")
