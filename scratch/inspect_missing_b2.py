import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('transcriptions/Madinah-Book-2.html', encoding='utf-8').read()

def inspect_unit(u_id):
    m = re.search(r'<section[^>]*id=["\']' + u_id + r'["\']>(.*?)</section>', content, re.DOTALL)
    if not m:
        print(f"Unit {u_id} not found!")
        return
    s_html = m.group(1)
    lines = re.findall(r'<div class=["\'](?:txt-line|heading|ar-title)[^"\']*["\']>(.*?)</div>', s_html)
    clean = [re.sub(r'<[^>]+>', ' ', l).strip() for l in lines]
    clean = [l for l in clean if len(l) > 2]
    print(f"\n==================== {u_id} ({len(clean)} lines) ====================")
    for idx, l in enumerate(clean[:35]):
        print(f"{idx}: {l}")

for uid in ['b2_u8', 'b2_u9', 'b2_u10', 'b2_u11', 'b2_u12', 'b2_u13', 'b2_u17', 'b2_u18', 'b2_u20', 'b2_u21', 'b2_u23', 'b2_u24', 'b2_u25', 'b2_u27', 'b2_u31']:
    inspect_unit(uid)
