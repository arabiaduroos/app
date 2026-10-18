import sys, os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('scratch'))
import parse_all_3books_cairo as p

for i, l in enumerate(p.book_map[1]):
    print(f"{i+1}: {l['title']} (Exercises: {len(l['exercises'])})")
