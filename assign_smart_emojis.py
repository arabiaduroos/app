# assign_smart_emojis.py
# Intelligently assigns accurate emojis based on Arabic and Urdu/English words
# Eliminates generic book emoji 📖 spam and fixes near/far emojis

import json, re

def strip_tashkeel(s):
    if not s: return ''
    return re.sub(r'[\u064b-\u065f\u0670\u0640]', '', str(s)).strip()

KEYWORD_EMOJI_RULES = [
    # People & Roles
    (r'(طبيب|طبيبة|doctor|ڈاکٹر)', '👨‍⚕️'),
    (r'(ممرض|ممرضة|nurse|نرس)', '👩‍⚕️'),
    (r'(مدرس|معلم|استاذ|أستاذ|teacher|استاد)', '🧑‍🏫'),
    (r'(طالب|طالبة|تلميذ|student|طالب علم)', '👨‍🎓'),
    (r'(ولد|صبي|boy|لڑکا)', '👦'),
    (r'(بنت|فتاة|girl|لڑکی)', '👧'),
    (r'(رجل|man|آدمی)', '🧔'),
    (r'(امرأة|نساء|woman|عورت)', '👩'),
    (r'(تاجر|merchant|تاجر)', '👳'),
    (r'(مهندس|engineer|انجینئر)', '👷'),
    (r'(إمام|امام|imam|امام)', '👳'),
    (r'(مدير|principal|director|پرنسپل|ہیڈ ماسٹر)', '👨‍💼'),
    (r'(مريض|sick|patient|بیمار)', '🤒'),
    (r'(أب|اب|والد|father|باپ|والد)', '👨'),
    (r'(أم|ام|والدة|mother|ماں|والدہ)', '👩'),
    (r'(أخ|اخ|brother|بھائی)', '👦'),
    (r'(أخت|اخت|sister|بہن)', '👧'),
    (r'(ابن|أبناء|son|بیٹا)', '👦'),
    (r'(جد|جدة|grandfather|دادا|نانا)', '👴'),
    (r'(حاج|حجاج|pilgrim|حاجی)', '🕋'),
    (r'(ضيف|ضيوف|guest|مہمان)', '👥'),
    (r'(طفل|طفلة|baby|child|بچہ)', '👶'),

    # Animals
    (r'(كلب|كلاب|dog|کتا)', '🐕'),
    (r'(قط|قطة|هرة|cat|بلی)', '🐈'),
    (r'(حمار|حمير|donkey|گدھا)', '🐴'),
    (r'(حصان|خيل|horse|گھوڑا)', '🐎'),
    (r'(جمل|ناقة|إبل|camel|اونٹ)', '🐪'),
    (r'(ديك|rooster|مرغا)', '🐓'),
    (r'(دجاجة|chicken|hen|مرغی)', '🐔'),
    (r'(بقرة|بقر|cow|گائے)', '🐄'),
    (r'(بطة|duck|بطخ)', '🦆'),
    (r'(سمك|سمكة|fish|مچھلی)', '🐟'),
    (r'(عصفور|طائر|طيور|bird|پرندہ)', '🐦'),
    (r'(فيل|elephant|ہاتھی)', '🐘'),
    (r'(أسد|اسد|lion|شیر)', '🦁'),
    (r'(غنم|شاة|خروف|sheep|بھیڑ|بکری)', '🐑'),

    # Objects & Household
    (r'(بيت|منزل|دار|house|گھر)', '🏠'),
    (r'(مسجد|جامع|mosque|مسجد)', '🕌'),
    (r'(كعبة|kaaba|کعبہ)', '🕋'),
    (r'(باب|door|دروازہ)', '🚪'),
    (r'(مفتاح|key|چابی)', '🔑'),
    (r'(قلم|pen|قلم)', '🖊️'),
    (r'(دفتر|كراسة|notebook|کاپی)', '📓'),
    (r'(كتاب|مصحف|book|کتاب)', '📖'),
    (r'(مكتب|طاولة|desk|table|میز)', '🗄️'),
    (r'(سرير|فراش|bed|بستر|چارپائی)', '🛏️'),
    (r'(كرسي|chair|کرسی)', '🪑'),
    (r'(قميص|ثوب|shirt|قمیض)', '👕'),
    (r'(منديل|handkerchief|رومال)', '🧣'),
    (r'(ساعة|watch|clock|گھڑی)', '⌚'),
    (r'(نظارة|glasses|عینک)', '👓'),
    (r'(حقيبة|شنطة|bag|بستہ)', '🎒'),
    (r'(حذاء|shoes|جوتا)', '👞'),
    (r'(صندوق|box|ڈبہ)', '📦'),
    (r'(تلفاز|تلفزيون|tv|ٹیلی ویژن)', '📺'),
    (r'(هاتف|جوال|phone|فون)', '📱'),

    # Places & Transport
    (r'(مدرسة|school|اسکول)', '🏫'),
    (r'(جامعة|كلية|university|یونیورسٹی)', '🏛️'),
    (r'(فصل|صف|classroom|کلاس)', '🏫'),
    (r'(غرفة|حجرة|room|کمرہ)', '🛋️'),
    (r'(مطبخ|kitchen|باورچی خانہ)', '🍳'),
    (r'(حمام|مرحاض|bathroom|غسل خانہ|بیت الخلا)', '🚿'),
    (r'(دكان|سوق|متجر|shop|market|دکان|بازار)', '🏪'),
    (r'(مستشفى|hospital|ہسپتال)', '🏥'),
    (r'(مطار|airport|ہوائی اڈا)', '✈️'),
    (r'(سيارة|car|گاڑی)', '🚗'),
    (r'(دراجة|bicycle|سائیکل)', '🚲'),
    (r'(حافلة|باص|bus|بس)', '🚌'),
    (r'(طائرة|plane|جہاز)', '✈️'),
    (r'(قطار|train|ٹرین|ریل)', '🚆'),
    (r'(سفينة|قارب|ship|boat|کشتی)', '🚢'),
    (r'(طريق|شارع|road|street|سڑک|راستہ)', '🛣️'),

    # Food & Drink
    (r'(ماء|water|پانی)', '💧'),
    (r'(لبن|حليب|milk|دودھ)', '🥛'),
    (r'(سكر|sugar|چینی)', '🍬'),
    (r'(شاي|tea|چائے)', '🍵'),
    (r'(قهوة|coffee|coffee|قہوہ)', '☕'),
    (r'(عصير|juice|شربت|جوس)', '🧃'),
    (r'(خبز|bread|روٹی)', '🍞'),
    (r'(لحم|meat|گوشت)', '🥩'),
    (r'(تفاح|apple|سیب)', '🍎'),
    (r'(عنب|grapes|انگور)', '🍇'),
    (r'(موز|banana|کیلا)', '🍌'),
    (r'(تمر|dates|کھجور)', '🌴'),
    (r'(طعام|أكل|food|کھانا)', '🍽️'),

    # Nature & Sky
    (r'(نجم|نجوم|star|ستارہ)', '⭐'),
    (r'(قمر|هلال|moon|چاند)', '🌙'),
    (r'(شمس|sun|سورج)', '☀️'),
    (r'(سماء|sky|آسمان)', '🌌'),
    (r'(حجر|صخر|stone|پتھر)', '🪨'),
    (r'(ورق|ورقة|paper|کاغذ)', '📄'),
    (r'(شجر|شجرة|tree|درخت)', '🌳'),
    (r'(زهرة|وردة|flower|پھول)', '🌸'),
    (r'(مطر|rain|بارش)', '🌧️'),
    (r'(بحر|sea|سمندر)', '🌊'),
    (r'(جبل|mountain|پہاڑ)', '🏔️'),

    # Countries
    (r'(يابان|japan|جاپان)', '🇯🇵'),
    (r'(صين|china|چین)', '🇨🇳'),
    (r'(هند|india|ہندوستان|بھارت)', '🇮🇳'),
    (r'(فلبين|philippines|فلپائن)', '🇵🇭'),
    (r'(مصر|egypt|مصر)', '🇪🇬'),
    (r'(مكة|مدينة|سعودية|saudi|مکہ|مدینہ)', '🕋'),

    # Actions
    (r'(ذهب|خرج|مشى|walk|went|نکلا|گیا)', '🚶'),
    (r'(رجع|عاد|return|واپس)', '🔙'),
    (r'(جلس|جالس|sit|sitting|بیٹھا)', '🪑'),
    (r'(قام|واقف|stand|standing|کھڑا)', '🧍'),
    (r'(صلى|صلاة|pray|نماز)', '🕌')
]

def detect_contextual_emoji(text, ur_text="", en_text=""):
    combined = (strip_tashkeel(text) + ' ' + str(ur_text) + ' ' + str(en_text)).lower()
    for pattern, emoji in KEYWORD_EMOJI_RULES:
        if re.search(r'\b' + pattern + r'\b', combined) or re.search(pattern, combined):
            return emoji
    return None

data = json.load(open('data/madinah_books.json', encoding='utf-8'))

updated_blocks_count = 0

for b_idx, book in enumerate(data['books']):
    b_num = book['book_num']
    for u_idx, unit in enumerate(book['units']):
        u_num = unit['unit_num']
        
        for blk in unit.get('blocks', []):
            txt = blk.get('text', '')
            ur_txt = blk.get('ur', '')
            en_txt = blk.get('en', '')
            cur_em = blk.get('emoji')

            # Clean donkey emoji
            if cur_em:
                blk['emoji'] = blk['emoji'].replace('\U0001facf', '🐴').replace('🫏', '🐴')

            # STRICT PURITY ON near_emoji & far_emoji:
            # ONLY Book 1 Unit 2 Lesson sentences contrasting هذا and ذلك should have near/far!
            if b_num == 1 and u_num == 2 and 'وَذٰلِكَ' in txt:
                # Keep near/far for Book 1 Lesson 2
                pass
            else:
                # Remove from everywhere else!
                if 'near_emoji' in blk: del blk['near_emoji']
                if 'far_emoji' in blk: del blk['far_emoji']

            # If emoji is missing, empty, or generic book 📖 on non-book text:
            is_generic_book = (cur_em == '📖' or cur_em == '📚')
            talking_about_book = bool(re.search(r'(كتاب|دفتر|مصحف|book|کتاب)', strip_tashkeel(txt) + ' ' + str(ur_txt) + ' ' + str(en_txt)))
            
            if not cur_em or (is_generic_book and not talking_about_book):
                detected = detect_contextual_emoji(txt, ur_txt, en_txt)
                if detected:
                    blk['emoji'] = detected
                    updated_blocks_count += 1
                elif not cur_em:
                    blk['emoji'] = '💬'

            # Also fix emoji_grid cards if any
            if blk.get('type') == 'emoji_grid':
                for c in blk.get('cards', []):
                    c_em = c.get('emoji')
                    if c_em:
                        c['emoji'] = c['emoji'].replace('\U0001facf', '🐴').replace('🫏', '🐴')
                    c_txt = c.get('text', '')
                    if not c.get('emoji') or (c.get('emoji') == '📖' and not re.search(r'(كتاب|دفتر|book)', c_txt)):
                        det = detect_contextual_emoji(c_txt, c.get('ur', ''), c.get('en', ''))
                        if det: c['emoji'] = det

        # Also fix unit questions emojis
        for q in unit.get('questions', []):
            q_em = q.get('emoji')
            if q_em:
                q['emoji'] = q['emoji'].replace('\U0001facf', '🐴').replace('🫏', '🐴')
            q_txt = q.get('answer', '') + ' ' + q.get('prompt_ar', '')
            if not q_em or (q_em == '📖' and not re.search(r'(كتاب|دفتر|book)', q_txt)):
                det = detect_contextual_emoji(q_txt, q.get('hint_ur', ''), q.get('hint_en', ''))
                if det: q['emoji'] = det

with open('data/madinah_books.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('data/madinah_books.js', 'w', encoding='utf-8') as f:
    f.write('window.MADINAH_DATA = ' + json.dumps(data, ensure_ascii=False) + ';\n')

print(f"SUCCESS: Assigned contextual emojis to {updated_blocks_count} blocks!")
print("Cleaned near_emoji and far_emoji so ONLY Book 1 Unit 2 'هذا ... وذلك' contrast sentences have them!")
