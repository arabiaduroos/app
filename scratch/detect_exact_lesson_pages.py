from PIL import Image
import os

print("Scanning for lesson headers...")
# Let's inspect each image and check pixel patterns
# On lesson start pages, there's a characteristic title in the top 60-120px
detected = []
for p in range(5, 126):
    f = f'scratch/b1_headers/title_p{p}.png'
    if os.path.exists(f):
        im = Image.open(f).convert('L')
        # Crop center top: x in [150, 450], y in [20, 80]
        crop = im.crop((150, 10, 450, 70))
        # Count dark pixels
        dark = sum(1 for px in crop.getdata() if px < 100)
        if dark > 300: # threshold for header text
            detected.append((p, dark))

print(f"Detected {len(detected)} candidate pages:")
for p, d in detected:
    print(f"  Page {p} (dark={d})")
