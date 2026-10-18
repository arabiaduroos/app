import glob, os
from PIL import Image

# Let's see which pages in Book 1 have the lesson header box
# In the original Madinah book 1, each lesson has a distinctive header banner at the top
# Let's inspect pages by looking at pixel statistics in the header area
results = []
for p in range(5, 126):
    f = f'scratch/b1_pages/top_{p}.png'
    if os.path.exists(f):
        im = Image.open(f).convert('L')
        w, h = im.size
        # The lesson title is in the top-middle
        # Let's crop x from 0.2*w to 0.8*w, y from 0.05*h to 0.5*h
        crop = im.crop((int(0.2*w), int(0.05*h), int(0.8*w), int(0.55*h)))
        # Count dark pixels (< 120)
        pixels = list(crop.getdata())
        dark = sum(1 for px in pixels if px < 120)
        results.append((p, dark))

# Print pages with high dark pixel count in the banner
print("Pages sorted by dark pixels or showing candidates:")
for p, d in results:
    if d > 2500:
        print(f"Page {p}: {d}")
