import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

b1 = d['books'][0]
mismatches = 0
for u in b1['units']:
    for q in u.get('questions', []):
        ar = q.get('prompt_ar', '')
        ur = q.get('prompt_ur', '')
        en = q.get('prompt_en', '')
        # Check if arabic appears verbatim inside ur or en (meaning not translated)
        if q.get('answer') == ur or (len(ur) > 3 and ur == ar):
            print(f"Mismatched Q in {u['id']}: AR={ar} | UR={ur}")
            mismatches += 1

print(f"Book 1 check complete. Untranslated/verbatim mismatches: {mismatches}")
