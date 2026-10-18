import fitz
from PIL import Image

doc = fitz.open('pdfs/Madinah-Book-1.pdf')

# Let's save a thumbnail crop of the top of each page from page 5 to 125
# and inspect them to find where each lesson starts
import os
os.makedirs('scratch/b1_pages', exist_ok=True)

for p in range(5, 126):
    pix = doc[p].get_pixmap(dpi=150)
    # The header title is usually in the top 20%
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    top = im.crop((0, 0, pix.width, int(pix.height * 0.22)))
    top.save(f'scratch/b1_pages/top_{p}.png')

print("Saved all Book 1 page tops.")
