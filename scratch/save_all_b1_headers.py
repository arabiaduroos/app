import fitz, os

doc1 = fitz.open('pdfs/Madinah-Book-1.pdf')

# Let's save a collage or thumbnails of headers for Book 1
os.makedirs('scratch/b1_headers', exist_ok=True)

# For each page from 5 to 125, save the top header
for p in range(5, len(doc1)):
    page = doc1[p]
    # Header is at top: fitz.Rect(100, 60, 500, 160)
    crop = page.get_pixmap(clip=fitz.Rect(100, 60, 500, 160))
    crop.save(f'scratch/b1_headers/p{p}.png')

print("Saved all Book 1 headers from p5 to end")
