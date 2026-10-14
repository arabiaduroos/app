import json, re

d = json.load(open('data/madinah_books.json', encoding='utf-8'))
for b in d['books']:
    for u in b['units']:
        # check blocks
        for blk in u.get('blocks', []):
            for row in blk.get('rows', []):
                ar = row.get('arabic', '')
                ur = row.get('urdu', '')
                en = row.get('english', '')
                if ar and ur and ar == ur:
                    print(f"[Block Row Match] Book {b['book_num']} Unit {u['unit_num']}: AR='{ar}' == UR='{ur}'")
                if ar and en and ar == en:
                    print(f"[Block Row Match] Book {b['book_num']} Unit {u['unit_num']}: AR='{ar}' == EN='{en}'")
        # check questions
        for q in u.get('questions', []):
            par = q.get('prompt_ar', '')
            pur = q.get('hint_ur', '') or q.get('prompt_ur', '')
            pen = q.get('hint_en', '') or q.get('prompt_en', '')
            ans = q.get('answer', '')
            if par and (par == pur or par == pen):
                print(f"[Question Match] Book {b['book_num']} Unit {u['unit_num']}: prompt_ar='{par}' equals hint")
            if ans and (ans == pur or ans == pen):
                print(f"[Question Match] Book {b['book_num']} Unit {u['unit_num']}: ans='{ans}' equals hint")
            # also check if prompt_ur has pure arabic
            if pur and pur == par:
                print(f"[Question Match] prompt_ur == par: {par}")
