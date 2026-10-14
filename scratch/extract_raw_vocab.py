import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_vocab_from_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    sections = re.findall(r'<section class="unit-card"[^>]*id="([^"]+)"([\s\S]*?)</section>', html)
    unit_vocab_data = {}
    for uid, sec in sections:
        if 'الكلمات الجديدة' not in sec:
            continue
        vpart = re.split(r'<div class="sec-hdr">[^<]*الكلمات الجديدة[^<]*</div>', sec)[1]
        lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', vpart)
        
        words = []
        for ar_div, ur_div in lines:
            ar_clean = re.sub(r'<[^>]+>', '', ar_div).strip()
            ar_clean = re.sub(r'^[^\w\s\(\)\.\-\u0600-\u06FF]+', '', ar_clean).strip()
            ur_clean = re.sub(r'<[^>]+>', '', ur_div).strip() if ur_div else ''
            
            if not ar_clean or re.match(r'^[=\-•\s]+$', ar_clean):
                continue
            
            if '•' in ar_clean and '•' in ur_clean:
                ar_items = [x.strip() for x in ar_clean.split('•') if x.strip()]
                ur_items = [x.strip() for x in ur_clean.split('•') if x.strip()]
                if len(ar_items) == len(ur_items):
                    for a, u in zip(ar_items, ur_items):
                        words.append({'ar': a, 'ur': u})
                else:
                    words.append({'ar': ar_clean, 'ur': ur_clean})
            elif '•' in ur_clean and not ('•' in ar_clean):
                ur_items = [x.strip() for x in ur_clean.split('•') if x.strip()]
                ar_items = [x.strip() for x in ar_clean.split() if x.strip()]
                if len(ar_items) == len(ur_items):
                    for a, u in zip(ar_items, ur_items):
                        words.append({'ar': a, 'ur': u})
                else:
                    words.append({'ar': ar_clean, 'ur': ur_clean})
            else:
                words.append({'ar': ar_clean, 'ur': ur_clean})

        if words:
            unit_vocab_data[uid] = words

    return unit_vocab_data

b1_vocab = extract_vocab_from_html('transcriptions/Madinah-Book-1.html')
b2_vocab = extract_vocab_from_html('transcriptions/Madinah-Book-2.html')

all_words = []
for uid, words in b1_vocab.items():
    for w in words:
        all_words.append({'book': 1, 'uid': uid, 'ar': w['ar'], 'ur': w['ur']})
for uid, words in b2_vocab.items():
    for w in words:
        all_words.append({'book': 2, 'uid': uid, 'ar': w['ar'], 'ur': w['ur']})

print(f"Total vocabulary items extracted: {len(all_words)}")
with open('scratch/extracted_vocab_raw.json', 'w', encoding='utf-8') as f:
    json.dump({'b1': b1_vocab, 'b2': b2_vocab, 'all': all_words}, f, ensure_ascii=False, indent=2)

print("Saved scratch/extracted_vocab_raw.json")
