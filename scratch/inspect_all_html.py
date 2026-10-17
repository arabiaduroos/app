import re

for book_num in [1, 2, 3]:
    filepath = rf'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-{book_num}.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        units = re.findall(r'<div class="unit-header">.*?<h2 class="unit-title">(.*?)</h2>', content, re.DOTALL)
        tamreens = re.findall(r'🔹\s*(\d+)-\s*•\s*(.*?)(?:<|\n)', content)
        print(f"Book {book_num}: {len(units)} units, {len(tamreens)} tamreen markers found, total chars: {len(content)}")
        for u in units[:5]:
            # clean tags
            clean_u = re.sub(r'<[^>]+>', '', u).strip()
            print(f"  Unit: {clean_u}")
    except Exception as e:
        print(f"Book {book_num} error: {e}")
