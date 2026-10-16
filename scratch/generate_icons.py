import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('icons', exist_ok=True)

def create_pwa_icon(size, output_path, is_maskable=False):
    # Canvas
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle/rounded rect
    margin = 0 if is_maskable else int(size * 0.05)
    r = int(size * 0.22) if not is_maskable else 0
    bg_box = [margin, margin, size - margin, size - margin]
    
    # Gradient-like background (rich Islamic emerald green to deep teal)
    draw.rounded_rectangle(bg_box, radius=r, fill=(22, 163, 74, 255)) # emerald-600
    
    # Subtle inner border/ring
    inner_margin = margin + int(size * 0.03)
    inner_r = max(4, r - int(size * 0.03))
    draw.rounded_rectangle([inner_margin, inner_margin, size - inner_margin, size - inner_margin],
                           radius=inner_r, outline=(88, 204, 2, 180), width=max(2, int(size * 0.015)))

    # Draw Mosque Silhouette in Center
    cx = size // 2
    cy = size // 2 + int(size * 0.05)
    scale = size / 512.0
    
    # Dome
    dome_w = int(140 * scale)
    dome_h = int(150 * scale)
    dome_top = cy - int(90 * scale)
    draw.ellipse([cx - dome_w // 2, dome_top - int(30 * scale), cx + dome_w // 2, dome_top + dome_h], fill=(255, 255, 255, 255))
    
    # Main building base
    base_w = int(160 * scale)
    base_h = int(110 * scale)
    base_top = cy + int(10 * scale)
    draw.rectangle([cx - base_w // 2, base_top, cx + base_w // 2, base_top + base_h], fill=(255, 255, 255, 255))
    
    # Minarets (Left & Right)
    min_w = int(32 * scale)
    min_h = int(190 * scale)
    min_left_x = cx - int(120 * scale)
    min_right_x = cx + int(120 * scale)
    min_top = cy - int(80 * scale)
    
    # Left minaret
    draw.rectangle([min_left_x - min_w // 2, min_top, min_left_x + min_w // 2, base_top + base_h], fill=(255, 255, 255, 255))
    draw.polygon([(min_left_x - min_w // 2, min_top), (min_left_x + min_w // 2, min_top), (min_left_x, min_top - int(35 * scale))], fill=(245, 158, 11, 255)) # amber top
    
    # Right minaret
    draw.rectangle([min_right_x - min_w // 2, min_top, min_right_x + min_w // 2, base_top + base_h], fill=(255, 255, 255, 255))
    draw.polygon([(min_right_x - min_w // 2, min_top), (min_right_x + min_w // 2, min_top), (min_right_x, min_top - int(35 * scale))], fill=(245, 158, 11, 255)) # amber top
    
    # Central crescent & star on dome
    finial_top = dome_top - int(65 * scale)
    draw.rectangle([cx - int(4 * scale), finial_top, cx + int(4 * scale), dome_top - int(15 * scale)], fill=(245, 158, 11, 255))
    draw.ellipse([cx - int(16 * scale), finial_top - int(24 * scale), cx + int(16 * scale), finial_top + int(8 * scale)], fill=(245, 158, 11, 255))
    draw.ellipse([cx - int(10 * scale), finial_top - int(28 * scale), cx + int(20 * scale), finial_top + int(2 * scale)], fill=(22, 163, 74, 255)) # cut for crescent
    
    # Arched door
    door_w = int(46 * scale)
    door_h = int(68 * scale)
    door_bottom = base_top + base_h
    door_top = door_bottom - door_h
    draw.ellipse([cx - door_w // 2, door_top, cx + door_w // 2, door_top + int(40 * scale)], fill=(22, 163, 74, 255))
    draw.rectangle([cx - door_w // 2, door_top + int(20 * scale), cx + door_w // 2, door_bottom], fill=(22, 163, 74, 255))

    img.save(output_path, 'PNG')
    print(f"Generated icon: {output_path} ({size}x{size})")

# Generate 192, 512, and maskable icons
create_pwa_icon(192, 'icons/icon-192.png', is_maskable=False)
create_pwa_icon(512, 'icons/icon-512.png', is_maskable=False)
create_pwa_icon(512, 'icons/icon-maskable.png', is_maskable=True)

# Also create clean vector SVG icon
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#16a34a"/>
      <stop offset="100%" stop-color="#15803d"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="112" fill="url(#bgGrad)"/>
  <rect x="24" y="24" width="464" height="464" rx="92" fill="none" stroke="#58cc02" stroke-width="8" opacity="0.6"/>
  <!-- Central Mosque Silhouette -->
  <g fill="#ffffff">
    <!-- Minarets -->
    <rect x="120" y="180" width="32" height="200" rx="4"/>
    <path d="M120 180 L152 180 L136 145 Z" fill="#f59e0b"/>
    <rect x="360" y="180" width="32" height="200" rx="4"/>
    <path d="M360 180 L392 180 L376 145 Z" fill="#f59e0b"/>
    <!-- Dome -->
    <ellipse cx="256" cy="225" rx="76" ry="85"/>
    <rect x="176" y="270" width="160" height="110"/>
    <!-- Crescent Finial -->
    <rect x="252" y="115" width="8" height="40" fill="#f59e0b"/>
    <circle cx="256" cy="105" r="16" fill="#f59e0b"/>
    <circle cx="262" cy="101" r="14" fill="#16a34a"/>
    <!-- Arch Door -->
    <path d="M233 380 L233 340 Q256 315 279 340 L279 380 Z" fill="#16a34a"/>
  </g>
</svg>'''

with open('icons/icon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
print("Generated vector icon: icons/icon.svg")
