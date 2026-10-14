# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from build_trans_p1 import TRANSLATIONS_P1
from build_trans_p2 import TRANSLATIONS_P2
from build_trans_p3 import TRANSLATIONS_P3
from build_trans_p4 import TRANSLATIONS_P4

def main():
    with open('scratch_b1_texts.json', encoding='utf-8') as f:
        texts = json.load(f)

    print(f"Total texts in scratch_b1_texts.json: {len(texts)}")

    combined = {}
    combined.update(TRANSLATIONS_P1)
    combined.update(TRANSLATIONS_P2)
    combined.update(TRANSLATIONS_P3)
    combined.update(TRANSLATIONS_P4)

    print(f"Total entries in combined: {len(combined)}")

    # Check for missing
    missing = []
    for item in texts:
        ar = item['ar']
        if ar not in combined:
            missing.append(ar)

    if missing:
        print(f"ERROR: {len(missing)} items missing!")
        for m in missing[:10]:
            print(f"  Missing: {repr(m)}")
        sys.exit(1)

    # Check for Latin characters in Urdu
    latin_issues = []
    for ar, trans in combined.items():
        ur = trans.get('ur', '')
        en = trans.get('en', '')
        if not ur or not en:
            print(f"ERROR: Empty translation for {repr(ar)}")
            sys.exit(1)
        if re.search(r'[a-zA-Z]', ur):
            latin_issues.append((ar, ur))

    if latin_issues:
        print(f"ERROR: Latin characters found in Urdu translation: {len(latin_issues)}")
        for ar, ur in latin_issues:
            print(f"  {repr(ar)} -> {ur}")
        sys.exit(1)

    # Build final map in exact order of scratch_b1_texts.json
    final_map = {}
    for item in texts:
        ar = item['ar']
        final_map[ar] = combined[ar]

    output_path = 'c:/Users/Person/Desktop/Dr Vaniya Ar/scratch_b1_trans.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_map, f, ensure_ascii=False, indent=2)

    print(f"Successfully wrote {len(final_map)} translations to {output_path}")

    # Verify readback
    with open(output_path, encoding='utf-8') as f:
        readback = json.load(f)

    print(f"Verification: read back {len(readback)} keys from {output_path}")
    assert len(readback) == len(texts) == 523
    print("ALL CHECKS PASSED PERFECTLY!")

if __name__ == '__main__':
    main()
