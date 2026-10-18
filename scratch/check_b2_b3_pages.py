import fitz

doc2 = fitz.open('pdfs/Madinah-Book-2.pdf')
doc3 = fitz.open('pdfs/Madinah-Book-3.pdf')

print("Doc 2 pages:", len(doc2))
print("Doc 3 pages:", len(doc3))

# Let's inspect pages 5, 6, 7 of Doc 2
for p in [4, 5, 6, 7]:
    doc2[p].get_pixmap().save(f'scratch/b2_page_{p}.png')

# Let's inspect pages 4, 5, 6 of Doc 3
for p in [3, 4, 5, 6]:
    doc3[p].get_pixmap().save(f'scratch/b3_page_{p}.png')

print("Saved b2 and b3 test pages.")
