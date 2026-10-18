import json, sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

b1 = [b for b in master_data['books'] if b['book_num'] == 1][0]
u4 = [u for u in b1['units'] if u['unit_num'] == 4][0]
u5 = [u for u in b1['units'] if u['unit_num'] == 5][0]

print("Book 1 Unit 4 current questions:", len(u4.get('questions', [])))
print("Book 1 Unit 5 current questions:", len(u5.get('questions', [])))
