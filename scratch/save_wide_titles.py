import fitz

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')

# Let's save a wide crop y: 50 to 300 for pages 5 to 35 to see lesson titles
for p in range(5, 36):
    crop = doc1[p].get_pixmap(clip=fitz.Rect(50, 40, 550, 180))
    crop.save(f'scratch/b1_headers/title_p{p}.png')

print("Saved title crops for p5 to p35")
