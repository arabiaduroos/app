import fitz

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')

# Let's inspect pages 5 to 127 in Book 1 to find where each lesson header appears
# We can save crops of the top of each page or use OCR/pixel detection, or look at the text
# In doc1, some pages have minimal text, but let's check what pages have "الدرس"
lesson_pages = []

for p in range(5, len(doc1)):
    # Let's check top of page (y: 30 to 180)
    page = doc1[p]
    # In doc1, the text is sometimes present or empty, but let's check text first
    txt = page.get_text()
    if 'الدرس' in txt or 'Lesson' in txt:
        print(f"Page {p}: {txt.strip()[:60]}")
