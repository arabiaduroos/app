import os
import subprocess

with open("scratch/test_vocab_perfect.html", "r", encoding="utf-8") as f:
    html = f.read()

# Render Card 18 with Lateef
html = html.replace("window.app.lessonReader.index = 34;", "window.app.lessonReader.index = 17;")
html = html.replace("Card 35 of 35", "Card 18 of 35")
html = html.replace("--font-kufi: 'Noto Kufi Arabic', system-ui, sans-serif;", "--font-kufi: 'Lateef', 'Traditional Arabic', serif;")
html = html.replace("var(--font-kufi)", "'Lateef', 'Traditional Arabic', serif")

html = html.replace("</head>", """<style>
  :root {
    --font-arabic: 'Lateef', 'Traditional Arabic', serif !important;
    --font-kufi: 'Lateef', 'Traditional Arabic', serif !important;
  }
  .ar-font, [lang="ar"], .vocab-tile-ar, .word-ar, .lesson-card-arabic, .gt-word, .letter-tag, .banner-title, .banner-rule-ar {
    font-family: 'Lateef', 'Traditional Arabic', serif !important;
  }
  .gt-word {
    font-size: 2.3rem !important;
    line-height: 1.3 !important;
  }
  .gt-connector .gt-connector-al {
    font-size: 1.45rem !important;
  }
</style></head>""")

test_file = "scratch/test_c2_lateef.html"
with open(test_file, "w", encoding="utf-8") as f:
    f.write(html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
brain_dir = r"C:\Users\Person\.gemini\antigravity\brain\548db058-a481-48f4-9024-0b3a7fd2647c"
png_path = os.path.join(brain_dir, "c2_lateef_preview.png")

subprocess.run([
    chrome_path, "--headless", "--disable-gpu",
    f"--screenshot={png_path}",
    "--window-size=1000,700",
    os.path.abspath(test_file)
])

print("C2 Lateef preview captured:", os.path.exists(png_path))
