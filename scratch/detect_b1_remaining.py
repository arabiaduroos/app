from PIL import Image

def is_lesson_header(p):
    im = Image.open(f'scratch/b1_headers/h_p{p}.png').convert('L')
    # The title "الدرس" is centered between x=150 and x=450, y=20 and y=90
    crop = im.crop((150, 15, 450, 85))
    dark = sum(1 for px in crop.getdata() if px < 100)
    return dark

results = []
for p in range(38, 126):
    d = is_lesson_header(p)
    if d > 280:
        results.append((p, d))

print(f"Detected {len(results)} candidate pages:")
for p, d in results:
    print(f"Page {p} (dark={d})")
