import json

# 1. Update b1_u3.sql
with open('b1_u3.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

old_sql_tail = """  -- SUMMARY TABLE & VOCABULARY TABLE
  ('b1_u3', 33, 'الْحُرُوفُ الْقَمَرِيَّةُ وَالْحُرُوفُ الشَّمْسِيَّةُ', 'حروفِ قمریہ (أ ب ج ح خ ع غ ف ق ك م و هـ ي) • حروفِ شمسیہ (ت ث د ذ ر ز س ش ص ض ط ظ ل ن)', 'Moon Letters (clear ''l'' sound) • Sun Letters (assimilated ''l'' sound into shaddah)', '🌙 ☀️'),
  ('b1_u3', 34, 'الْكَلِمَاتُ الْجَدِيدَةُ', 'نئے الفاظ', 'New Vocabulary', '🗂️');"""

new_sql_tail = """  -- DEDICATED SUN & MOON LETTERS TABLES (SPLIT INTO 2 PAGES, ZERO SCROLL)
  ('b1_u3', 33, 'الْحُرُوفُ الْقَمَرِيَّةُ', 'حروفِ قمریہ (لام ظاہر، ساکن پڑھی جائے گی)', 'Moon Letters (The ''l'' sound is clearly pronounced)', '🌙'),
  ('b1_u3', 34, 'الْحُرُوفُ الشَّمْسِيَّةُ', 'حروفِ شمسیہ (لام مدغم، حرف پر تشدید کے ساتھ)', 'Sun Letters (The ''l'' is silent and assimilates into a shaddah)', '☀️'),
  -- FINAL CARD: VOCABULARY GRID (الْكَلِمَاتُ الْجَدِيدَةُ)
  ('b1_u3', 35, 'الْكَلِمَاتُ الْجَدِيدَةُ', 'نئے الفاظ', 'New Vocabulary', '🗂️');"""

sql = sql.replace(old_sql_tail, new_sql_tail)

with open('b1_u3.sql', 'w', encoding='utf-8') as f:
    f.write(sql)
with open('chapter_output.sql', 'w', encoding='utf-8') as f:
    f.write(sql)
print("Updated b1_u3.sql and chapter_output.sql")

# 2. Update DATA inside app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_code = f.read()

start_marker = 'let DATA = '
start = app_code.find(start_marker)
end = app_code.find(';\n', start)
json_str = app_code[start + len(start_marker):end]
data = json.loads(json_str)

b1 = data['books'][0]
for u in b1['units']:
    if u['id'] == 'b1_u3':
        cards = u['cards']
        # Find index of card 33 and 34
        new_cards = []
        for c in cards:
            if c['card_order'] < 33:
                new_cards.append(c)
        new_cards.append({
            'id': 76,
            'unit_id': 'b1_u3',
            'card_order': 33,
            'type': 'qamari_table',
            'arabic': 'الْحُرُوفُ الْقَمَرِيَّةُ',
            'trans_ur': 'حروفِ قمریہ (لام ظاہر، ساکن پڑھی جائے گی)',
            'trans_en': "Moon Letters (The 'l' sound is clearly pronounced)",
            'emoji': '🌙'
        })
        new_cards.append({
            'id': 77,
            'unit_id': 'b1_u3',
            'card_order': 34,
            'type': 'shamsi_table',
            'arabic': 'الْحُرُوفُ الشَّمْسِيَّةُ',
            'trans_ur': 'حروفِ شمسیہ (لام مدغم، حرف پر تشدید کے ساتھ)',
            'trans_en': "Sun Letters (The 'l' is silent and assimilates into a shaddah)",
            'emoji': '☀️'
        })
        new_cards.append({
            'id': 78,
            'unit_id': 'b1_u3',
            'card_order': 35,
            'type': 'vocab_table',
            'arabic': 'الْكَلِمَاتُ الْجَدِيدَةُ',
            'title_ar': 'الْكَلِمَاتُ الْجَدِيدَةُ',
            'title_ur': 'نئے الفاظ',
            'title_en': 'New Vocabulary',
            'trans_ur': 'نئے الفاظ',
            'trans_en': 'New Vocabulary',
            'emoji': '🗂️'
        })
        u['cards'] = new_cards
        print(f"Updated unit b1_u3 in DATA! Total cards: {len(u['cards'])}")

new_json_str = json.dumps(data, ensure_ascii=False)
app_code = app_code[:start + len(start_marker)] + new_json_str + app_code[end:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("Updated app.js DATA object successfully!")
