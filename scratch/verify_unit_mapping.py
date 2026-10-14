import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Book 2
b2_html = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()
b2_sections = [s for s in re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', b2_html, re.DOTALL) if 'مقدمة' not in s[1][:400] and 'مُقَدِّمَة' not in s[1][:400]]

print(f"Book 2 json units: {len(data['books'][1]['units'])}, html non-intro sections: {len(b2_sections)}")
for i in range(min(len(data['books'][1]['units']), len(b2_sections))):
    u_json = data['books'][1]['units'][i]
    s_id, s_html = b2_sections[i]
    h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
    h2_text = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else ''
    print(f"  Unit {i+1}: json='{u_json.get('title_ar')}' vs html_sec={s_id} '{h2_text[:30]}'")

# Book 3
b3_html = open('transcriptions/Madinah-Book-3.html', encoding='utf-8').read()
b3_sections = [s for s in re.findall(r'<section[^>]*id=["\']([^"\']+)["\']>(.*?)</section>', b3_html, re.DOTALL) if 'مقدمة' not in s[1][:400] and 'مُقَدِّمَة' not in s[1][:400]]

print(f"\nBook 3 json units: {len(data['books'][2]['units'])}, html non-intro sections: {len(b3_sections)}")
for i in range(min(len(data['books'][2]['units']), len(b3_sections))):
    u_json = data['books'][2]['units'][i]
    s_id, s_html = b3_sections[i]
    h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_html)
    h2_text = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else ''
    print(f"  Unit {i+1}: json='{u_json.get('title_ar')}' vs html_sec={s_id} '{h2_text[:30]}'")
