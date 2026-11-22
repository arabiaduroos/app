import os
import subprocess

with open("scratch/test_vocab_perfect.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Noto Kufi with Lateef
html = html.replace("--font-kufi: 'Noto Kufi Arabic', system-ui, sans-serif;", "--font-kufi: 'Lateef', 'Traditional Arabic', serif;")
html = html.replace("var(--font-kufi)", "'Lateef', 'Traditional Arabic', serif")
html = html.replace("font-family: var(--font-kufi)", "font-family: 'Lateef', 'Traditional Arabic', serif")

# Also add font-size boost for Lateef because Lateef glyphs are slightly smaller and need 1.35x-1.4x font size!
html = html.replace("</head>", """<style>
  :root {
    --font-arabic: 'Lateef', 'Traditional Arabic', serif !important;
    --font-kufi: 'Lateef', 'Traditional Arabic', serif !important;
  }
  .ar-font, [lang="ar"], .vocab-tile-ar, .word-ar, .lesson-card-arabic, .gt-word, .letter-tag, .banner-title, .banner-rule-ar {
    font-family: 'Lateef', 'Traditional Arabic', serif !important;
  }
  .vocab-words-grid.grid-6-cols .vocab-tile-ar {
    font-size: 1.35rem !important;
    line-height: 1.15 !important;
  }
  .lesson-card-arabic {
    font-size: 2.5rem !important;
  }
  .gt-word {
    font-size: 2.2rem !important;
  }
</style></head>""")

test_file = "scratch/test_lateef_render.html"
with open(test_file, "w", encoding="utf-8") as f:
    f.write(html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
brain_dir = r"C:\Users\Person\.gemini\antigravity\brain\548db058-a481-48f4-9024-0b3a7fd2647c"
png_path = os.path.join(brain_dir, "vocab_lateef_font_preview.png")

subprocess.run([
    chrome_path, "--headless", "--disable-gpu",
    f"--screenshot={png_path}",
    "--window-size=1000,700",
    os.path.abspath(test_file)
])

print("Lateef preview captured:", os.path.exists(png_path))
