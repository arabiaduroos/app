import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# English translation mapping dictionary for common Madinah Arabic words & patterns
EN_DICT = {
    'المدرسة': 'The school', 'الفصل': 'The classroom', 'الحمام': 'The bathroom', 'المرحاض': 'The toilet',
    'المطبخ': 'The kitchen', 'الغرفة': 'The room', 'الجامعة': 'The university', 'السوق': 'The market',
    'اليابان': 'Japan', 'الصين': 'China', 'الهند': 'India', 'الفلبين': 'The Philippines',
    'المدير': 'The director / principal', 'ذهب': 'He went', 'خرج': 'He exited',
    'الرسول': 'The Messenger', 'الكعبة': 'The Kaaba', 'الاسم': 'The name', 'الابن': 'The son',
    'العم': 'The paternal uncle', 'الخال': 'The maternal uncle', 'الحقيبة': 'The bag', 'السيارة': 'The car',
    'الشارع': 'The street', 'مغلق': 'Closed', 'تحت': 'Under', 'هناك': 'There', 'المهندس': 'The engineer',
    'مضاف': 'Possessed (Mudhaf)', 'مضاف إليه': 'Possessor (Mudhaf Ilayh)',
    'ذكي': 'Intelligent / Smart', 'أذكياء': 'Intelligent (pl.)',
    'غبي': 'Foolish / Dull', 'أغبياء': 'Foolish (pl.)',
    'خلق': 'Good character / manners', 'أخلاق': 'Manners / Morals (pl.)',
    'مائة': 'One hundred', 'ألف': 'One thousand', 'روبية': 'Rupee', 'روبيات': 'Rupees',
    'متزوج': 'Married', 'عزب': 'Bachelor / Unmarried', 'أعزاب': 'Bachelors',
    'يهودي': 'Jewish', 'يهود': 'Jews', 'معجم': 'Dictionary', 'معاجم': 'Dictionaries',
    'دولار': 'Dollar', 'دولارات': 'Dollars', 'صفحة': 'Page', 'صفحات': 'Pages',
    'ناجح': 'Successful', 'ناجحون': 'Successful (pl.)', 'غال': 'Expensive',
    'كم': 'Sleeve', 'أكمام': 'Sleeves',
    'لقاء': 'Meeting', 'جيد': 'Good', 'جيب': 'Pocket', 'جيوب': 'Pockets',
    'نهر': 'River', 'أنهار': 'Rivers', 'برقية': 'Telegram', 'برقيات': 'Telegrams',
    'مصرف': 'Bank', 'مصارف': 'Banks', 'مكتب البريد': 'Post office',
    'مهجع': 'Dormitory', 'مهاجع': 'Dormitories', 'كوكب': 'Planet / Star', 'كواكب': 'Planets',
    'واسع': 'Spacious / Wide', 'فريق': 'Team', 'فرق': 'Teams', 'شقيق': 'Full brother',
    'أشقاء': 'Full brothers', 'ثمن': 'Price', 'عالم': 'World', 'عوالم': 'Worlds',
    'شهير': 'Famous', 'شهر': 'Month', 'شهور': 'Months', 'أشهر': 'Months',
    'لاعب': 'Player', 'لاعبون': 'Players', 'في المنام': 'In a dream', 'الأزهر': 'Al-Azhar',
    'عقرب': 'Scorpion', 'عقارب': 'Scorpions', 'حذاء': 'Shoe', 'أحذية': 'Shoes',
    'جنة': 'Garden / Paradise', 'جنات': 'Gardens', 'نعسان': 'Sleepy / Drowsy',
    'كوب': 'Cup / Tumbler', 'أكواب': 'Cups', 'صوت': 'Voice / Sound', 'أصوات': 'Voices',
    'يد': 'Hand', 'أيد': 'Hands', 'زوج': 'Spouse / Pair', 'أزواج': 'Spouses',
    'مذياع': 'Radio', 'جو': 'Weather / Atmosphere', 'غريب': 'Stranger', 'غرباء': 'Strangers',
    'موسى': 'Razor', 'مظلم': 'Dark', 'كنس': 'He swept', 'يكنس': 'He sweeps',
    'نظر': 'He looked', 'ينظر': 'He looks', 'سكت': 'He became silent', 'يسكت': 'He is silent',
    'جمع': 'He collected', 'يجمع': 'He collects', 'طبخ': 'He cooked', 'يطبخ': 'He cooks',
    'قطع': 'He cut', 'يقطع': 'He cuts', 'حلق': 'He shaved', 'يحلق': 'He shaves',
    'عبد': 'He worshipped', 'يعبد': 'He worships', 'علم': 'He knew', 'يعلم': 'He knows',
    'منع': 'He prevented', 'يمنع': 'He prevents', 'عاذ': 'He sought refuge', 'يعوذ': 'He seeks refuge',
    'سيارة الأجرة': 'Taxi', 'صف': 'Row / Class', 'صفوف': 'Rows', 'أخير': 'Last / Final'
}

def clean_ar(s):
    # remove vowels/tashkeel for lookup
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED]', '', s).strip()

def get_en_translation(ar_word, ur_word):
    # Look up in EN_DICT
    ar_base = clean_ar(ar_word)
    # Check direct match
    if ar_base in EN_DICT:
        return EN_DICT[ar_base]
    # Check without parentheses (ج ...)
    base_no_parens = re.sub(r'\(.*?\)', '', ar_base).strip()
    if base_no_parens in EN_DICT:
        return EN_DICT[base_no_parens]
    
    # Try common Urdu hints
    ur = ur_word.lower()
    if 'اسکول' in ur or 'مدرسہ' in ur: return 'School'
    if 'کلاس' in ur or 'جماعت' in ur: return 'Classroom'
    if 'غسل خانہ' in ur: return 'Bathroom'
    if 'بیت الخلا' in ur: return 'Toilet / Restroom'
    if 'باورچی' in ur: return 'Kitchen'
    if 'کمرہ' in ur: return 'Room'
    if 'یونیورسٹی' in ur or 'جامعہ' in ur: return 'University'
    if 'بازار' in ur or 'مارکیٹ' in ur: return 'Market'
    if 'جاپان' in ur: return 'Japan'
    if 'چین' in ur: return 'China'
    if 'ہندوستان' in ur or 'بھارت' in ur: return 'India'
    if 'فلپائن' in ur: return 'Philippines'
    if 'پرنسپل' in ur or 'مدیر' in ur: return 'Director / Principal'
    if 'گیا' in ur: return 'Went'
    if 'نکلا' in ur: return 'Exited / Left'
    if 'رسول' in ur: return 'Messenger'
    if 'کعبہ' in ur: return 'The Kaaba'
    if 'نام' in ur: return 'Name'
    if 'بیٹا' in ur: return 'Son'
    if 'چچا' in ur: return 'Paternal uncle'
    if 'ماموں' in ur: return 'Maternal uncle'
    if 'بستہ' in ur or 'تھیلا' in ur: return 'Bag'
    if 'گاڑی' in ur or 'کار' in ur: return 'Car'
    if 'سڑک' in ur: return 'Street'
    if 'بند' in ur: return 'Closed'
    if 'نیچے' in ur: return 'Under / Beneath'
    if 'وہاں' in ur: return 'There'
    if 'انجینئر' in ur: return 'Engineer'
    if 'ڈاکٹر' in ur or 'طبیب' in ur: return 'Doctor'
    if 'استاد' in ur or 'ٹیچر' in ur: return 'Teacher'
    if 'طالب علم' in ur: return 'Student'
    if 'تاجر' in ur: return 'Merchant / Trader'
    if 'کتا' in ur: return 'Dog'
    if 'بلی' in ur: return 'Cat'
    if 'گدھا' in ur: return 'Donkey'
    if 'گھوڑا' in ur: return 'Horse'
    if 'اونٹ' in ur: return 'Camel'
    if 'مرغا' in ur: return 'Rooster'
    if 'رومال' in ur: return 'Handkerchief'
    if 'قمیض' in ur: return 'Shirt'
    if 'گھر' in ur: return 'House'
    if 'مسجد' in ur: return 'Mosque'
    if 'دروازہ' in ur: return 'Door'
    if 'کتاب' in ur: return 'Book'
    if 'قلم' in ur: return 'Pen'
    if 'چابی' in ur: return 'Key'
    if 'میز' in ur: return 'Desk'
    if 'کرسی' in ur: return 'Chair'
    if 'بستر' in ur: return 'Bed'
    if 'ستارہ' in ur: return 'Star'
    if 'چاند' in ur: return 'Moon'
    if 'سورج' in ur: return 'Sun'
    if 'پانی' in ur: return 'Water'
    if 'دودھ' in ur: return 'Milk'
    if 'روٹی' in ur: return 'Bread'
    if 'شادی شدہ' in ur: return 'Married'
    if 'کنوارا' in ur: return 'Bachelor / Unmarried'
    if 'یہودی' in ur: return 'Jewish'
    if 'ڈکشنری' in ur or 'لغت' in ur: return 'Dictionary'
    if 'ڈالر' in ur: return 'Dollar'
    if 'صفحہ' in ur: return 'Page'
    if 'کامیاب' in ur: return 'Successful'
    if 'مہنگا' in ur: return 'Expensive'
    if 'سستا' in ur: return 'Cheap'
    if 'سو' in ur or '۱۰۰' in ur: return 'One hundred'
    if 'ہزار' in ur or '۱۰۰۰' in ur: return 'One thousand'
    if 'روپیہ' in ur: return 'Rupee'
    if 'آستین' in ur: return 'Sleeve'
    if 'ذہین' in ur: return 'Intelligent'
    if 'کند ذہن' in ur or 'بیوقوف' in ur: return 'Dull / Foolish'
    if 'اخلاق' in ur: return 'Good character / Manners'
    if 'بچھو' in ur: return 'Scorpion'
    if 'جوتا' in ur or 'جوتے' in ur: return 'Shoe / Shoes'
    if 'جنت' in ur or 'باغ' in ur: return 'Garden / Paradise'
    if 'اونگھتا' in ur or 'نیند' in ur: return 'Sleepy / Drowsy'
    if 'گلاس' in ur or 'پیالہ' in ur: return 'Glass / Cup'
    if 'آواز' in ur: return 'Voice / Sound'
    if 'ہاتھ' in ur: return 'Hand'
    if 'شوہر' in ur or 'بیوی' in ur or 'جوڑا' in ur: return 'Spouse / Pair'
    if 'ریڈیو' in ur: return 'Radio'
    if 'موسم' in ur or 'فضا' in ur: return 'Weather / Atmosphere'
    if 'اجنبی' in ur or 'پردیسی' in ur: return 'Stranger'
    if 'استرا' in ur: return 'Razor'
    if 'تاریک' in ur or 'اندھیرا' in ur: return 'Dark'
    if 'جھاڑو' in ur: return 'Swept / Sweeps'
    if 'دیکھا' in ur or 'دیکھتا' in ur: return 'Looked / Looks'
    if 'خاموش' in ur: return 'Silent'
    if 'جمع کیا' in ur or 'اکٹھا' in ur: return 'Collected'
    if 'پکایا' in ur or 'پکاتا' in ur: return 'Cooked'
    if 'کاٹا' in ur: return 'Cut'
    if 'مونڈھا' in ur or 'شیو' in ur: return 'Shaved'
    if 'عبادت' in ur: return 'Worshipped'
    if 'جانا' in ur or 'معلوم' in ur: return 'Knew / Learned'
    if 'روکا' in ur or 'منع' in ur: return 'Prevented / Forbade'
    if 'پناہ' in ur: return 'Sought refuge'
    if 'ٹیکسی' in ur: return 'Taxi'
    if 'قطار' in ur: return 'Row / Line'
    if 'آخری' in ur: return 'Last / Final'

    return ur_word

print("Translation module ready.")
