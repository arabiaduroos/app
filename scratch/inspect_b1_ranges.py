import fitz

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')

# Let's write a python script to scan where the lesson headers appear
# We can check the pixel distribution or save crops of pages to find all 23 lessons
print("Book 1 total pages:", len(doc1))

# Let's inspect pages 5 to 127 in steps, or save small header thumbnails to inspect
# Specifically let's inspect the pages around:
# Lesson 1: 5-11
# Lesson 2: 12-13
# Lesson 3: 14-20
# Lesson 4: 21-26
# Lesson 5: 27-32
# etc.
