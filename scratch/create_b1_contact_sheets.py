from PIL import Image, ImageDraw, ImageFont
import os

# Create 6 composite sheets:
# Sheet 1: pp 5 to 24
# Sheet 2: pp 25 to 44
# Sheet 3: pp 45 to 64
# Sheet 4: pp 65 to 84
# Sheet 5: pp 85 to 104
# Sheet 6: pp 105 to 125

ranges = [
    (5, 24),
    (25, 44),
    (45, 64),
    (65, 84),
    (85, 104),
    (105, 125)
]

for sheet_idx, (start_p, end_p) in enumerate(ranges, 1):
    count = end_p - start_p + 1
    strip_w = 550
    strip_h = 50
    sheet = Image.new('RGB', (strip_w, strip_h * count), (255, 255, 255))
    draw = ImageDraw.Draw(sheet)
    
    for idx, p in enumerate(range(start_p, end_p + 1)):
        f = f'scratch/b1_all_headers/p{p}.png'
        if os.path.exists(f):
            im = Image.open(f).resize((strip_w - 70, strip_h))
            sheet.paste(im, (70, idx * strip_h))
            # draw page number
            draw.text((10, idx * strip_h + 15), f"P. {p}", fill=(200, 0, 0))
            draw.line([(0, idx * strip_h), (strip_w, idx * strip_h)], fill=(220, 220, 220))
            
    sheet.save(f'scratch/b1_sheet_{sheet_idx}.png')

print("Saved all 6 composite sheets.")
