import json, re, sys, os, random
sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)

# Load existing dataset
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

with open('transcriptions/Madinah-All-Books-Cairo.md', 'r', encoding='utf-8') as f:
    cairo_md = f.read()

b1_idx = cairo_md.find('## 📗')
b2_idx = cairo_md.find('## 📘')
b1_secs = re.split(r'\n###\s+', cairo_md[b1_idx:b2_idx])[1:]

B1_PAGES = {
    1: 5, 2: 12, 3: 14, 4: 21, 5: 27, 6: 33, 7: 39, 8: 42, 9: 47,
    10: 54, 11: 61, 12: 63, 13: 68, 14: 82, 15: 87, 16: 92, 17: 96,
    18: 100, 19: 105, 20: 109, 21: 114, 22: 117, 23: 120
}

from compile_complete_master_dataset import make_vocalization_opts, make_sentence_reading_opts, make_mcq_opts, extract_exercises_from_lines, process_exercise_to_questions

# Import detailed generators for U1, U4, U5
# Let's inspect how many questions we get with detailed U1, U4, U5 and generic for others
print("Imported successfully.")
