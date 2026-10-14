import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_vocab_from_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Split by section
    sections = re.findall(r'<section class="unit-card"[^>]*id="([^"]+)"([\s\S]*?)</section>', html)
    print(f"{filename}: found {len(sections)} sections")

    unit_vocab_data = {}
    for uid, sec in sections:
        if 'الكلمات الجديدة' not in sec:
            continue
        # Get part after الكلمات الجديدة
        vpart = re.split(r'<div class="sec-hdr">[^<]*الكلمات الجديدة[^<]*</div>', sec)[1]
        lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', vpart)
        
        words = []
        for ar_div, ur_div in lines:
            # Clean ar
            ar_clean = re.sub(r'<[^>]+>', '', ar_div).strip()
            ar_clean = re.sub(r'^[^\w\s\(\)\.\-\u0600-\u06FF]+', '', ar_clean).strip()
            # Clean ur
            ur_clean = re.sub(r'<[^>]+>', '', ur_div).strip() if ur_div else ''
            
            # Skip empty or separators like = • =
            if not ar_clean or re.match(r'^[=\-•\s]+$', ar_clean):
                continue
            
            # If line has bullet separation
            if '•' in ar_clean and '•' in ur_clean:
                ar_items = [x.strip() for x in ar_clean.split('•') if x.strip()]
                ur_items = [x.strip() for x in ur_clean.split('•') if x.strip()]
                # Pair 1-to-1 if lengths match
                if len(ar_items) == len(ur_items):
                    for a, u in zip(ar_items, ur_items):
                        words.append({'ar': a, 'ur': u})
                else:
                    words.append({'ar': ar_clean, 'ur': ur_clean})
            elif '•' in ur_clean and not ('•' in ar_clean):
                # Arabic separated by spaces, ur by bullets
                # e.g. "الرسول الكَعْبةَ الاسْمُ الابـْنُ" vs "رسول • کعبہ • نام • بیٹا"
                ur_items = [x.strip() for x in ur_clean.split('•') if x.strip()]
                # Try splitting ar by spaces
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

print(f"Book 1 units with vocab: {len(b1_vocab)}")
print(f"Book 2 units with vocab: {len(b2_vocab)}")

# Print sample from Book 1 and Book 2
for uid in ['b1_u4', 'b1_u5', 'b2_u2', 'b2_u14']:
    if uid in b1_vocab:
        print(f"\n--- {uid} (B1) ---")
        for w in b1_vocab[uid]:
            print(f"  {w['ar']}  -->  {w['ur']}")
    elif uid in b2_vocab:
        print(f"\n--- {uid} (B2) ---")
        for w in b2_vocab[uid]:
            print(f"  {w['ar']}  -->  {w['ur']}")
