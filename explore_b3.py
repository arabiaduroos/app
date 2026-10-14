import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    with open('data/madinah_books.json', encoding='utf-8') as f:
        d = json.load(f)
    b3 = d['books'][2]
    for u in b3['units']:
        print(f"Unit {u['unit_num']}: {u.get('title_ar')} | {u.get('topic_ar')}")

if __name__ == '__main__':
    main()
