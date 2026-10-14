import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-3.html', encoding='utf-8').read()

def inspect_b3_unit(u_id):
    m = re.search(r'<section[^>]*id=["\']' + u_id + r'["\']>(.*?)</section>', content, re.DOTALL)
    if not m:
        print(f"Unit {u_id} not found!")
        return
    s_html = m.group(1)
    lines = re.findall(r'<div class=["\'](?:txt-line|heading|ar-title)[^"\']*["\']>(.*?)</div>', s_html)
    clean = [re.sub(r'<[^>]+>', ' ', l).strip() for l in lines]
    clean = [l for l in clean if len(l) > 2]
    print(f"\n==================== {u_id} ({len(clean)} lines) ====================")
    for idx, l in enumerate(clean[:30]):
        if any(kw in l for kw in ['تمرين', 'تمارين', 'أجب', 'تأمل', 'عَيِّنْ', 'عيّن', 'اقرأ', 'هات', 'استخرج', 'ضع', 'املأ', 'حوّل', '1-', '2-', '3-', 'صغ']):
            print(f"{idx}: {l}")

for uid in [f'b3_u{i}' for i in range(2, 19)]:
    inspect_b3_unit(uid)
