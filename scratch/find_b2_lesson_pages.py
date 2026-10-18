import fitz
from PIL import Image
import os

# Let's inspect where lessons start in Book 2
doc2 = fitz.open('pdfs/Madinah-Book-2.pdf')
print("Book 2 total pages:", len(doc2))

# In Book 2, pages 0 to 4 are covers/intro.
# Let's check pages where lesson titles appear.
# In Book 2, lesson titles have big text in the upper third: "الدرس الأول", "الدرس الثاني", etc.
# Let's find pages with high concentration of text or check every page.
# Even simpler: we can inspect them by writing a script that detects dark text in the title region
# or inspect pages 5 to 222.

lesson_candidates = []
for p in range(4, len(doc2)):
    im = Image.open(f'scratch/b2_tops/top_{p}.png').convert('L')
    w, h = im.size
    # check title banner: center region
    crop = im.crop((int(0.2*w), int(0.08*h), int(0.8*w), int(0.45*h)))
    dark = sum(1 for px in crop.getdata() if px < 100)
    if dark > 800:
        lesson_candidates.append((p, dark))

print(f"Book 2 candidates ({len(lesson_candidates)}):")
for p, d in lesson_candidates:
    print(f"Page {p}: {d}")
