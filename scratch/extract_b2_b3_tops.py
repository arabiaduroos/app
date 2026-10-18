import fitz
from PIL import Image
import os

doc2 = fitz.open('pdfs/Madinah-Book-2.pdf')
doc3 = fitz.open('pdfs/Madinah-Book-3.pdf')

os.makedirs('scratch/b2_tops', exist_ok=True)
os.makedirs('scratch/b3_tops', exist_ok=True)

# Save page tops for Book 2 (223 pages)
for p in range(len(doc2)):
    pix = doc2[p].get_pixmap(dpi=72)
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    top = im.crop((0, 0, pix.width, int(pix.height * 0.25)))
    top.save(f'scratch/b2_tops/top_{p}.png')

# Save page tops for Book 3 (144 pages)
for p in range(len(doc3)):
    pix = doc3[p].get_pixmap(dpi=72)
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    top = im.crop((0, 0, pix.width, int(pix.height * 0.25)))
    top.save(f'scratch/b3_tops/top_{p}.png')

print("Saved tops for Book 2 and Book 3.")
