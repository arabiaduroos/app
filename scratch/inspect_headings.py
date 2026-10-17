import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML size:", len(html))

# Find all h1, h2, h3, h4 tags
headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html, re.DOTALL)
print(f"Total headings (h1-h4): {len(headings)}")
for h in headings[:25]:
    clean_h = re.sub(r'<[^>]+>', '', h).strip()
    print(" ", clean_h[:80])
