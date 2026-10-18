import fitz

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')
doc2 = fitz.open('pdfs/Madinah-Book-2.pdf')
doc3 = fitz.open('pdfs/Madinah-Book-3.pdf')

print(f"Book 1 pages: {len(doc1)}")
print(f"Book 2 pages: {len(doc2)}")
print(f"Book 3 pages: {len(doc3)}")

# Let's check page 1 to 10 of Book 1
for p in range(1, 10):
    page = doc1[p]
    pix = page.get_pixmap()
    # Bottom center is where page number is printed
    # Let's save a small crop of the bottom of page 5
    if p == 4: # index 4 = PDF page 5
        rect = fitz.Rect(200, 700, 400, 800)
        crop = page.get_pixmap(clip=rect)
        crop.save('scratch/b1_p5_bottom.png')
print("Done")
