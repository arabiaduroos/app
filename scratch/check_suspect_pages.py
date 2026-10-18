import fitz

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')

# Let's inspect pages where lessons start
# Known so far:
# Lesson 1: Page 5
# Lesson 2: Page 12
# Lesson 3: Page 14
# Lesson 4: Page 21
# Lesson 5: Page 27
# Let's check pages 33, 34, 35, 36, 37, 38 to find Lesson 6 and 7
for p in range(27, 45):
    # let's save image and print
    pass

# Let's write a script to save crops of specific suspect pages
suspects = [5, 12, 14, 21, 27, 33, 34, 35, 36, 37, 38, 42, 43, 44, 45, 46, 50, 51, 52, 53, 58, 59, 60, 65, 66, 67, 71, 72, 73, 78, 79, 80, 84, 85, 86, 91, 92, 93, 97, 98, 99, 103, 104, 105, 110, 111, 112, 116, 117, 118, 121, 122, 123]

for p in suspects:
    crop = doc1[p].get_pixmap(clip=fitz.Rect(100, 40, 500, 160))
    crop.save(f'scratch/b1_headers/cand_p{p}.png')

print("Saved candidate crops.")
