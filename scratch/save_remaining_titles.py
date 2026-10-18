import fitz

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')

# Let's save crops from p25 to p127 in step to find all lesson headers
for p in range(27, 126):
    crop = doc1[p].get_pixmap(clip=fitz.Rect(50, 40, 550, 180))
    crop.save(f'scratch/b1_headers/title_p{p}.png')

print("Saved title crops up to p125")
