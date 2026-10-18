import sys
sys.path.append('scratch')
from test_full_parser import b1_data

sys.stdout.reconfigure(encoding='utf-8')

l4 = b1_data[3]
print("=== Lesson 4 Items ===")
for it in l4['items']:
    print(f"p. {it['page']} | {it['badge']} | {it['desc']} | {it['count']} qs")

l5 = b1_data[4]
print("\n=== Lesson 5 Items ===")
for it in l5['items']:
    print(f"p. {it['page']} | {it['badge']} | {it['desc']} | {it['count']} qs")
