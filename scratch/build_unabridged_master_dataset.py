import json, re, sys, os, random

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

# Load existing dataset
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Load Cairo transcription
with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo_md = f.read()

# Load Manifest
with open(r'C:\Users\Person\.gemini\antigravity\brain\871510d4-1766-4c62-b894-0270b402a9f3\madinah_curriculum_tamreens_manifest.md', 'r', encoding='utf-8') as f:
    manifest_md = f.read()

# Helper distractor functions
def make_vocalization_opts(correct_word):
    base = re.sub(r'[\u064b-\u0652]$', '', correct_word.strip())
    opt_damma = base + 'ُ'
    opt_kasra = base + 'ِ'
    opt_fatha = base + 'َ'
    opt_tanween = base + 'ٌ' if not base.startswith('ال') else base + 'ُ'
    
    opts = [correct_word]
    for c in [opt_kasra, opt_damma, opt_fatha, opt_tanween, base + 'ْ']:
        if c != correct_word and c not in opts:
            opts.append(c)
        if len(opts) == 4:
            break
    while len(opts) < 4:
        opts.append(base + 'ـ')
    random.shuffle(opts)
    return opts

def make_mcq_opts(correct_ans, alt_pool):
    opts = [correct_ans]
    for alt in alt_pool:
        if alt != correct_ans and alt not in opts:
            opts.append(alt)
        if len(opts) == 4:
            break
    defaults = ["نَعَمْ", "لَا", "صَحِيحٌ", "خَاطِئٌ", "فِي الْمَسْجِدِ", "عَلَى الْمَكْتَبِ", "فِي الْبَيْتِ"]
    for d in defaults:
        if len(opts) >= 4: break
        if d != correct_ans and d not in opts:
            opts.append(d)
    random.shuffle(opts)
    return opts

# Authoritative printed pages
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

# Split sections
b1_idx = cairo_md.find('## 📗')
b2_idx = cairo_md.find('## 📘')
b3_idx = cairo_md.find('## 📙')

b1_secs = re.split(r'\n###\s+', cairo_md[b1_idx:b2_idx])[1:]
b2_secs = re.split(r'\n###\s+', cairo_md[b2_idx:b3_idx])[2:]
b3_secs = re.split(r'\n###\s+', cairo_md[b3_idx:])[2:]

print("Parser initialized.")
