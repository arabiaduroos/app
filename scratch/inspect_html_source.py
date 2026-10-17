import sys, re

sys.stdout.reconfigure(encoding='utf-8')

for b_num in [1, 2, 3]:
    fname = rf'C:\Users\Person\Documents\GitHub\app\transcriptions\Madinah-Book-{b_num}.html'
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find unit cards or headings
    unit_ids = re.findall(r'id=["\'](unit-[0-9]+)["\']', html)
    print(f"\n==========================================")
    print(f"Book {b_num} HTML ({len(html)} chars): {len(unit_ids)} units found")
    print(f"==========================================")
    print(f"Unit IDs: {unit_ids[:10]} ... {unit_ids[-5:] if len(unit_ids) > 5 else ''}")

    # Search for exercises / tamreens in HTML
    tamreen_matches = re.findall(r'(تَمَارِين|تَمْرِين|تـمـارين|تـمرين|exercise|tamreen)', html, re.IGNORECASE)
    print(f"Exercise keyword occurrences: {len(tamreen_matches)}")
