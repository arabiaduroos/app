import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# We can parse HTML using regex since bs4 wasn't installed, or simple tag parsing
def inspect_book(fname, bnum):
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find each unit-card
    units = re.findall(r'<section class="unit-card"[^>]*id="([^"]+)"([\s\S]*?)</section>', html)
    print(f"\n=================== BOOK {bnum} ({len(units)} units) ===================")
    for uid, ucontent in units:
        title_m = re.search(r'<h2 class="unit-title">[\s\S]*?<span>([^<]*)</span>\s*([^<]+)</h2>', ucontent)
        title = title_m.group(2).strip() if title_m else uid
        
        # Look for exercises/tamreens
        # Lines with (1), (2), تمرين, تمارين, اقرأ واكتب, etc.
        lines = re.findall(r'<div class="txt-line"><div>([\s\S]*?)</div>(?:<div class="ur">([\s\S]*?)</div>)?</div>', ucontent)
        dlgs = re.findall(r'<div class="dlg-row">[\s\S]*?<div class="ur">([\s\S]*?)</div>', ucontent)
        
        # Check for exercise markers in lines
        ex_lines = []
        for ar, ur in lines:
            ar_clean = re.sub(r'<[^>]+>', '', ar).strip()
            ur_clean = re.sub(r'<[^>]+>', '', ur).strip() if ur else ''
            if any(k in ar_clean for k in ['تمرين', 'تمارين', 'التدريب', 'أجب', 'اقرأ', 'كوّن', 'ضع', 'املأ', 'حوّل', 'أدخل', 'تأمل']):
                ex_lines.append((ar_clean, ur_clean))
        
        print(f"Unit {uid}: '{title}' | total txt lines: {len(lines)}, dlgs: {len(dlgs)}, ex markers: {len(ex_lines)}")
        if ex_lines:
            for el in ex_lines[:3]:
                print(f"    EX: {el[0][:60]} --> {el[1][:60]}")

inspect_book('transcriptions/Madinah-Book-1.html', 1)
inspect_book('transcriptions/Madinah-Book-2.html', 2)
inspect_book('transcriptions/Madinah-Book-3.html', 3)
