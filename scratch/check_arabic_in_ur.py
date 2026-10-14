import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))

urdu_only_chars = re.compile(r'[\u0679\u0686\u0698\u0695\u06ba\u06be\u06c1\u06d2\u0626]')
common_urdu_words = ['ہے', 'ہیں', 'کا', 'کی', 'کے', 'کو', 'سے', 'میں', 'پر', 'اور', 'کیا', 'وہ', 'یہ', 'نہیں', 'تھا', 'تھی', 'تھے', 'گیا', 'گئے', 'کہ', 'نے', 'آپ', 'تم', 'ہم', 'میرا', 'تیرا', 'اس', 'ان', 'سب', 'والا', 'والے', 'والی', 'شربت', 'خوش', 'گنتی']

for b in data['books']:
    for u in b['units']:
        for blk in u.get('blocks', []):
            ur = blk.get('ur', '')
            ar = blk.get('text', '')
            en = blk.get('en', '')
            
            # Check if ur has Arabic but no Urdu words/letters
            if ur and not any(w in ur for w in common_urdu_words) and not urdu_only_chars.search(ur):
                if re.search(r'[\u0600-\u06ff]', ur):
                    print(f"B{b['book_num']} U{u['unit_num']} : ar='{ar}' | ur='{ur}'")
