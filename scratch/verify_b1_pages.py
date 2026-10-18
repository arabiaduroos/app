import fitz

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')

for p in [5, 10, 15, 20, 23, 27, 30, 40, 50, 60, 70, 80]:
    page = doc1[p]
    # Crop the page number area
    rect = fitz.Rect(250, 750, 350, 790)
    crop = page.get_pixmap(clip=rect)
    crop.save(f'scratch/b1_check_p{p}.png')

print("Saved verification crops.")
