import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/madinah_books.json', encoding='utf-8'))

# Exact correct translations for individual vocabulary words that got mismatched in books
CORRECT_VOCAB = {
    'المستشفى': ('ہسپتال', 'The hospital'),
    'المكْتَبَةُ': ('لائبریری / کتب خانہ', 'The library'),
    'المكتبة': ('لائبریری / کتب خانہ', 'The library'),
    'وَلكِنْ': ('لیکن / مگر', 'But / However'),
    'عَقْرَبٌ': ('بچھو', 'Scorpion'),
    'عَقْرَبٌ ج عَقَارِبُ': ('بچھو (جمع: عقارب)', 'Scorpion (pl. scorpions)'),
    'نَعْسَانُ': ('اونگھتا ہوا / نیند کا مارا', 'Sleepy / Drowsy'),
    'يَدٌ': ('ہاتھ', 'Hand'),
    'مِذْيَاعٌ': ('ریڈیو', 'Radio'),
    'مُوْسىً': ('استرا (شیو کا بلیڈ) / موسیٰ', 'Razor / Musa'),
    'مُوْسَى': ('استرا / موسیٰ', 'Razor / Musa'),
    'نَظَرَ': ('اس نے دیکھا (نظر ڈالی)', 'He looked / glanced'),
    'طَبَخَ': ('اس نے پکایا', 'He cooked'),
    'عَبَدَ': ('اس نے عبادت کی', 'He worshipped'),
    'مَنَعَ': ('اس نے روکا / منع کیا', 'He prevented / forbade'),
    'دَائِماً': ('ہمیشہ / لگاتار', 'Always'),
    'مَكْتَبٌ': ('میز / دفتر', 'Desk / Office'),
    'فَعَلَ': ('اس نے کیا', 'He did'),
    'سَجَدَ': ('اس نے سجدہ کیا', 'He prostrated'),
    'دَرَسَ': ('اس نے پڑھا / مطالعہ کیا', 'He studied'),
    'عَرَفَ': ('اس نے جانا / پہچانا', 'He knew / recognized'),
    'رَنَّ': ('بجا (گھنٹی بجی)', 'Rang (bell rang)'),
    'دَوَاءٌ': ('دوا / علاج', 'Medicine'),
    'وَزِيْرُ الخَارِجِيَّةِ': ('وزیر خارجہ', 'Foreign Minister'),
    'مَشَى': ('وہ چلا (پیدل چلا)', 'He walked'),
    'شفاك الله.': ('اللہ آپ کو شفا عطا فرمائے۔', 'May Allah cure you.'),
    'شَفَاكَ اللَّهُ': ('اللہ آپ کو شفا عطا فرمائے۔', 'May Allah cure you.'),
    'نعم.': ('جی ہاں۔', 'Yes.'),
    'لِماذا؟': ('کیوں؟', 'Why?'),
    'لِماذا رَجَعْتَ؟': ('تم کیوں واپس آئے؟', 'Why did you return?'),
    'أمسلمات هنّ؟': ('کیا وہ سب مسلمان عورتیں ہیں؟', 'Are they (females) Muslims?'),
    'أُرِيْدُ قَلَماً.': ('مجھے ایک قلم چاہیے۔', 'I want a pen.'),
    'أَيّهُما أَحْسَنُ؟': ('ان دونوں میں سے کون سا بہتر ہے؟', 'Which of the two is better?'),
    'اُدْخُلْ... ما اسْمُك؟': ('داخل ہو جاؤ... تمہارا نام کیا ہے؟', 'Enter... what is your name?'),
    'نَظَرَ (يَنْظُرُ) • سَكَتَ (يَسْكُتُ) • جَمَعَ (يَجْمَعُ)': ('دیکھا (دیکھتا ہے) • خاموش رہا (خاموش ہوتا ہے) • جمع کیا (جمع کرتا ہے)', 'Looked (looks) • Remained silent (remains silent) • Gathered (gathers)'),
    'نَظَرَ (يَنْظُرُ)': ('اس نے دیکھا (وہ دیکھتا ہے)', 'He looked (he looks)'),
    'سَكَتَ (يَسْكُتُ)': ('وہ خاموش رہا (وہ خاموش ہوتا ہے)', 'He remained silent (he stays silent)'),
    'جَمَعَ (يَجْمَعُ)': ('اس نے جمع کیا (وہ جمع کرتا ہے)', 'He gathered (he gathers)')
}

fixed_count = 0

for b in data['books']:
    for u in b['units']:
        for blk in u.get('blocks', []):
            ar = blk.get('text', '').strip()
            ur = blk.get('ur', '').strip()
            en = blk.get('en', '').strip()
            
            # Check if this exact Arabic string has a known correct translation
            for ar_key, (c_ur, c_en) in CORRECT_VOCAB.items():
                if ar == ar_key or ar.replace('َ','').replace('ُ','').replace('ِ','').replace('ْ','').replace('ّ','') == ar_key.replace('َ','').replace('ُ','').replace('ِ','').replace('ْ','').replace('ّ',''):
                    # Check if current translation is clearly wrong
                    if len(ur) > 25 and len(c_ur) < 25:
                        print(f"Fixing mismatch: ar='{ar}' | old_ur='{ur[:35]}' -> new_ur='{c_ur}'")
                        blk['ur'] = c_ur
                        blk['en'] = c_en
                        fixed_count += 1
                        break
                    elif 'طلبہ: ابھی تک نہیں' in ur and 'طلبہ' not in ar:
                        print(f"Fixing mismatch: ar='{ar}' | old_ur='{ur[:35]}' -> new_ur='{c_ur}'")
                        blk['ur'] = c_ur
                        blk['en'] = c_en
                        fixed_count += 1
                        break
                    elif 'عباس، اپنے اس بھائی' in ur and 'عباس' not in ar:
                        print(f"Fixing mismatch: ar='{ar}' | old_ur='{ur[:35]}' -> new_ur='{c_ur}'")
                        blk['ur'] = c_ur
                        blk['en'] = c_en
                        fixed_count += 1
                        break
                    elif 'آمنہ: ابو محمد' in ur and 'آمنہ' not in ar:
                        print(f"Fixing mismatch: ar='{ar}' | old_ur='{ur[:35]}' -> new_ur='{c_ur}'")
                        blk['ur'] = c_ur
                        blk['en'] = c_en
                        fixed_count += 1
                        break
                    elif 'ابراہیم: انہیں پرسوں' in ur and 'ابراہیم' not in ar:
                        print(f"Fixing mismatch: ar='{ar}' | old_ur='{ur[:35]}' -> new_ur='{c_ur}'")
                        blk['ur'] = c_ur
                        blk['en'] = c_en
                        fixed_count += 1
                        break

print(f"\nTotal mismatched blocks fixed: {fixed_count}")

# Save back to json
with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Write madinah_books.js
with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write('window.MADINAH_DATA = ' + json.dumps(data, ensure_ascii=False) + ';\n')

print("Saved updated madinah_books.json and madinah_books.js!")
