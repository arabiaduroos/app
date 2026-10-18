import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\.gemini\antigravity\brain\871510d4-1766-4c62-b894-0270b402a9f3\madinah_curriculum_tamreens_manifest.md', encoding='utf-8') as f:
    text = f.read()

lines = [l for l in text.splitlines() if l.startswith('| Book ')]

total_qs = 0
by_book = {1: {'items': 0, 'qs': 0, 'types': {}}, 2: {'items': 0, 'qs': 0, 'types': {}}, 3: {'items': 0, 'qs': 0, 'types': {}}}

for l in lines:
    parts = [p.strip() for p in l.split('|')[1:-1]]
    if len(parts) < 5:
        continue
    lesson, page, item_type, desc, q_count_str = parts
    m_b = re.search(r'Book (\d+)', lesson)
    if not m_b: continue
    b_num = int(m_b.group(1))
    
    # parse count
    m_c = re.search(r'(\d+)', q_count_str)
    c = int(m_c.group(1)) if m_c else 1
    
    by_book[b_num]['items'] += 1
    by_book[b_num]['qs'] += c
    
    # item kind
    kind = 'tamreen'
    if 'نَصّ' in item_type:
        kind = 'nasuddars'
    elif 'قَاعِدَة' in item_type or 'Snippet' in item_type:
        kind = 'qaida'
    by_book[b_num]['types'][kind] = by_book[b_num]['types'].get(kind, 0) + 1

for b_num in [1, 2, 3]:
    print(f"Book {b_num}: {by_book[b_num]['items']} items, {by_book[b_num]['qs']} total questions/parts, types: {by_book[b_num]['types']}")
