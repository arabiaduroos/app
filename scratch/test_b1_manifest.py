import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect Book 1 in detail
with open('transcriptions/Madinah-Book-1.html', 'r', encoding='utf-8') as f:
    b1_html = f.read()

# Let's write a targeted extractor for Book 1 lessons
# We can extract each unit section
sections = re.findall(r'<section class="unit-card" id="b1_u(\d+)">([\s\S]*?)(?=</section>)', b1_html)

b1_manifest = []

B1_PAGES = {
    1: 5, 2: 12, 3: 14, 4: 21, 5: 27, 6: 33, 7: 39, 8: 42, 9: 47,
    10: 54, 11: 61, 12: 63, 13: 68, 14: 82, 15: 87, 16: 92, 17: 96,
    18: 100, 19: 105, 20: 109, 21: 114, 22: 117, 23: 120
}

# We can also check the PDF pages to assign exact page numbers to each tamreen!
# For example, in Lesson 4:
# P. 21: Section (أ) intro
# P. 22: Tamreen 1 (11 questions), Tamreen 2 (13 words), Tamreen 3 (6 sentences)
# P. 23: Tamreen 3 cont. (sentences 7-10), Snippet: محمد vs آمنة (16 names), Tamreen 4 (14 names)
# P. 24: Section (ب) dialogue
# P. 25: Tamreen 1 (6 questions), Tamreen 2 (9 phrases), Tamreen 3 (7 sentences)
# P. 26: Tamreen 4 (5 fill blanks) + vocab

print(f"Book 1 sections: {len(sections)}")
