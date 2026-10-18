import fitz

doc2 = fitz.open('pdfs/Madinah-Book-2.pdf')
print("Book 2 total pages:", len(doc2))
for p in range(len(doc2) - 4, len(doc2)):
    doc2[p].get_pixmap(dpi=150).save(f'scratch/b2_end_p{p}.png')

doc3 = fitz.open('pdfs/Madinah-Book-3.pdf')
print("Book 3 total pages:", len(doc3))
for p in range(len(doc3) - 4, len(doc3)):
    doc3[p].get_pixmap(dpi=150).save(f'scratch/b3_end_p{p}.png')

print("Saved end pages for Book 2 and 3.")
