import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append('scratch')

import build_book1_full
import build_book2_complete
import build_book3_complete

print("Loading data/madinah_books.json...")
with open('data/madinah_books.json', encoding='utf-8') as f:
    data = json.load(f)

# 1. Retrieve all questions
print("Generating authentic questions for all 3 books...")
b1_questions = build_book1_full.get_book1_questions_all()
b2_questions = build_book2_complete.build_b2_all()
b3_questions = build_book3_complete.build_b3_all()

print(f"Book 1 generated: {len(b1_questions)} units, {sum(len(v) for v in b1_questions.values())} questions")
print(f"Book 2 generated: {len(b2_questions)} units, {sum(len(v) for v in b2_questions.values())} questions")
print(f"Book 3 generated: {len(b3_questions)} units, {sum(len(v) for v in b3_questions.values())} questions")

# 2. Sanitize and inject into books
for book in data['books']:
    b_num = book['book_num']
    print(f"\nProcessing Book {b_num} ({len(book['units'])} units)...")
    
    for unit in book['units']:
        u_num = unit['unit_num']
        
        # Sanitize blocks
        for blk in unit.get('blocks', []):
            ar = blk.get('text', '')
            ur = blk.get('ur', '')
            en = blk.get('en', '')
            
            # Clean pure Arabic from English
            if en and re.search(r'[\u0600-\u06ff]', en) and not re.search(r'[a-zA-Z]', en):
                blk['en'] = ''
            elif en and en.strip() == ar.strip():
                blk['en'] = ''
                
            # Clean identical Arabic from Urdu
            if ur and ur.strip() == ar.strip():
                blk['ur'] = ''
                
            # Specific fixes for corrupted Urdu vocab entries
            if ar == 'نَصْرانِيٌ ج نَصَارَى' and ur == 'نصاریٰ)':
                blk['ur'] = 'عیسائی (جمع: نصاریٰ)'
            elif ar == 'الرَّكْعَةُ ج رَكَعاتٌ' and ur == 'رکعات)':
                blk['ur'] = 'رکعت (جمع: رکعات)'
            elif ar == 'الثَمَنُ نِصْفٌ' and ur == 'دن/ایام)':
                blk['ur'] = 'قیمت / آدھا'
            elif ar == 'الرِيالُ ج رِيالاتٌ' and ur == 'ریالات)':
                blk['ur'] = 'ریال (جمع: ریالات)'
            elif ar == 'البَلَـدُ ج بِـلادٌ' and ur == 'بلاد)':
                blk['ur'] = 'شہر / ملک (جمع: بلاد)'
            elif ar == 'الحَرفُ ج حُرُوفٌ' and ur == 'حروف)':
                blk['ur'] = 'حرف (جمع: حروف)'
            elif ar == 'الفِنْجَانُ ج فَناجِيـن' and ur == 'فناجین)':
                blk['ur'] = 'پیالی (جمع: فناجین)'
            elif ar == 'المَدْرَسةُ ج مَدارِسُ' and ur == 'مدارس)':
                blk['ur'] = 'مدرسہ (جمع: مدارس)'
            elif ar == 'المَسْجِدُ ج مساجِدُ' and ur == 'مساجد)':
                blk['ur'] = 'مسجد (جمع: مساجد)'
            elif ar == 'اِمْرَأَة) قَرِيْبٌ' and ur == 'اِمْرَأَة)':
                blk['ur'] = 'عورت) قریب ہے'
                
            # Specific fix for ذلك نجم
            if 'مَا ذٰلِكَ؟ ذٰلِكَ نَجْمٌ' in ar and ur == 'وہ کیا ہے؟ وہ ایک ستارہ ہے۔':
                blk['ur'] = 'وہ کیا ہے؟ وہ ستارہ ہے۔'
                
        # Inject authentic questions
        if b_num == 1:
            qs = b1_questions.get(u_num, [])
        elif b_num == 2:
            qs = b2_questions.get(u_num, [])
        elif b_num == 3:
            qs = b3_questions.get(u_num, [])
        else:
            qs = []
            
        unit['questions'] = qs

# 3. Write data/madinah_books.json
print("\nSaving updated data/madinah_books.json...")
with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 4. Write data/madinah_books.js
print("Generating data/madinah_books.js...")
js_content = 'window.MADINAH_DATA = ' + json.dumps(data, ensure_ascii=False) + ';\n'
with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("SUCCESS: All books compiled and saved to madinah_books.json and madinah_books.js!")
