import fitz

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')

for p in range(len(doc1)):
    # Let's crop the center of the page around y=750..790 to see page number
    page = doc1[p]
    # Also let's check what lessons start on what PDF pages
    # Let's save crops for pages 1 to 10
    if p < 10:
        pix = page.get_pixmap(clip=fitz.Rect(100, 50, 500, 250))
        pix.save(f'scratch/b1_p{p+1}_top.png')
print("Saved top crops for pages 1 to 10")
