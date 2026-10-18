import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect Book 1 HTML and Cairo markdown first
with open('transcriptions/Madinah-Book-1.html', 'r', encoding='utf-8') as f:
    b1_html = f.read()

with open('transcriptions/Madinah-Book-2.html', 'r', encoding='utf-8') as f:
    b2_html = f.read()

with open('transcriptions/Madinah-Book-3.html', 'r', encoding='utf-8') as f:
    b3_html = f.read()

print("Loaded all 3 HTML files successfully.")
