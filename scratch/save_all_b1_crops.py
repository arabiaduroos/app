import fitz
from PIL import Image
import os

doc = fitz.open('pdfs/Madinah-Book-1.pdf')

# Let's save a crop of y: 40..160, x: 100..500 for every single page from 5 to 125
os.makedirs('scratch/b1_all_headers', exist_ok=True)

for p in range(5, 126):
    pix = doc[p].get_pixmap(dpi=100)
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    # The header title "الدرس" is in top area
    crop = im.crop((int(pix.width * 0.15), int(pix.height * 0.03), int(pix.width * 0.85), int(pix.height * 0.15)))
    crop.save(f'scratch/b1_all_headers/p{p}.png')

print("Saved all 121 header crops of Book 1.")
