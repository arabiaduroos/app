import re, json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

# Authoritative TOC start pages
B1_PAGES = {
    1: 5, 2: 12, 3: 14, 4: 21, 5: 27, 6: 33, 7: 39, 8: 42, 9: 47,
    10: 54, 11: 61, 12: 63, 13: 68, 14: 82, 15: 87, 16: 92, 17: 96,
    18: 100, 19: 105, 20: 109, 21: 114, 22: 117, 23: 120
}

B2_PAGES = {
    1: 5, 2: 12, 3: 18, 4: 26, 5: 30, 6: 36, 7: 46, 8: 55, 9: 59,
    10: 69, 11: 74, 12: 84, 13: 91, 14: 95, 15: 103, 16: 109, 17: 119,
    18: 127, 19: 133, 20: 138, 21: 144, 22: 153, 23: 154, 24: 161,
    25: 167, 26: 173, 27: 180, 28: 193, 29: 205, 30: 213, 31: 218
}

B3_PAGES = {
    1: 5, 2: 20, 3: 28, 4: 41, 5: 49, 6: 59, 7: 64, 8: 69, 9: 74,
    10: 83, 11: 89, 12: 96, 13: 104, 14: 113, 15: 118, 16: 132, 17: 141
}

# Read Cairo md
with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    text = f.read()

b1_idx = text.find('## 📗')
b2_idx = text.find('## 📘')
b3_idx = text.find('## 📙')

b1_raw = text[b1_idx:b2_idx]
b2_raw = text[b2_idx:b3_idx]
b3_raw = text[b3_idx:]

b1_secs = re.split(r'\n###\s+', b1_raw)[1:]
b2_secs = re.split(r'\n###\s+', b2_raw)[2:] # skip Muqaddimah
b3_secs = re.split(r'\n###\s+', b3_raw)[2:] # skip Muqaddimah

print(f"Loaded: Book 1 = {len(b1_secs)}, Book 2 = {len(b2_secs)}, Book 3 = {len(b3_secs)}")
