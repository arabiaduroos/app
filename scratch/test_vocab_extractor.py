import re
from bs4 import BeautifulSoup
import json

def parse_html_vocab(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    sections = soup.find_all('section', class_='unit-card')
    print(f"File {filename}: found {len(sections)} unit sections")

    unit_vocabs = {}
    for sec in sections:
        sec_id = sec.get('id', '')
        # Find sec-hdr with الكلمات الجديدة
        vocab_hdr = None
        for hdr in sec.find_all(class_='sec-hdr'):
            if 'الكلمات الجديدة' in hdr.get_text():
                vocab_hdr = hdr
                break
        if not vocab_hdr:
            continue

        words = []
        # Siblings after vocab_hdr
        curr = vocab_hdr.next_sibling
        while curr:
            if curr.name == 'section':
                break
            if curr.name == 'div' and 'txt-line' in curr.get('class', []):
                inner_divs = curr.find_all('div')
                if len(inner_divs) >= 1:
                    ar_div = inner_divs[0]
                    # strip leading emojis from ar
                    ar_text = re.sub(r'^[^\w\s\(\)\.\-\u0600-\u06FF]+', '', ar_div.get_text()).strip()
                    
                    ur_div = curr.find(class_='ur')
                    ur_text = ur_div.get_text().strip() if ur_div else ''
                    
                    en_div = curr.find(class_='en')
                    en_text = en_div.get_text().strip() if en_div else ''
                    
                    words.append({
                        'ar_raw': ar_text,
                        'ur_raw': ur_text,
                        'en_raw': en_text
                    })
            curr = curr.next_sibling
        if words:
            unit_vocabs[sec_id] = words

    return unit_vocabs

b1_vocab = parse_html_vocab('transcriptions/Madinah-Book-1.html')
print("Book 1 units with vocab:", list(b1_vocab.keys()))
for u, w in list(b1_vocab.items())[:3]:
    print(f"--- {u} ---")
    for row in w[:5]:
        print("  AR:", row['ar_raw'])
        print("  UR:", row['ur_raw'])

b2_vocab = parse_html_vocab('transcriptions/Madinah-Book-2.html')
print("Book 2 units with vocab:", list(b2_vocab.keys()))
for u, w in list(b2_vocab.items())[:3]:
    print(f"--- {u} ---")
    for row in w[:5]:
        print("  AR:", row['ar_raw'])
        print("  UR:", row['ur_raw'])
