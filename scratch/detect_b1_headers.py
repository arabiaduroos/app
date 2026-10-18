from PIL import Image
import os

lesson_starts = []

for p in range(5, 125):
    img_path = f'scratch/b1_headers/p{p}.png'
    if os.path.exists(img_path):
        im = Image.open(img_path).convert('L')
        # Check central area where "( ) الدرس" is printed
        # Width: 400, Height: 100
        # Count dark pixels (< 100)
        pixels = list(im.getdata())
        dark_pixels = sum(1 for px in pixels if px < 100)
        # If there is significant text in the header area
        if dark_pixels > 600:
            lesson_starts.append((p, dark_pixels))

print(f"Candidate header pages: {len(lesson_starts)}")
for p, count in lesson_starts:
    print(f"Page {p}: dark_pixels={count}")
