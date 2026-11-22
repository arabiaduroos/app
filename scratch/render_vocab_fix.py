import os
import subprocess

brain_dir = r"C:\Users\Person\.gemini\antigravity\brain\548db058-a481-48f4-9024-0b3a7fd2647c"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
app_dir = r"c:\Users\Person\Documents\GitHub\app"

with open(os.path.join(app_dir, "styles.css"), "r", encoding="utf-8") as f:
    css_content = f.read()

with open("scratch/patch_preview.css", "r", encoding="utf-8") as f:
    patch_css = f.read()

full_css = css_content + "\n" + patch_css

with open("scratch/full_test.css", "w", encoding="utf-8") as f:
    f.write(full_css)

with open(os.path.join(app_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Replace css link with full_test.css
html = html.replace('href="styles.css?v=10"', 'href="scratch/full_test.css"')
# Add no-referrer meta
html = html.replace('<head>', '<head><meta name="referrer" content="no-referrer">')

injection = """
<script>
  localStorage.setItem('madinah_lang', 'both');
  window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
      const u3 = window.app.DATA.books[0].units.find(u => u.id === 'b1_u3');
      window.app.openLessonCardReader(u3);
      window.app.lessonReader.index = 34; // Card 35
      window.app.renderCurrentLessonCard();
    }, 200);
  });
</script>
</body>
"""
html = html.replace("</body>", injection)

with open("scratch/test_reader_c35.html", "w", encoding="utf-8") as f:
    f.write(html)

# Capture at 1000x700
png_path = os.path.join(brain_dir, "vocab_card_no_overlap_1000.png")
subprocess.run([
    chrome_path, "--headless", "--disable-gpu",
    "--virtual-time-budget=2000",
    f"--screenshot={png_path}",
    "--window-size=1000,700",
    os.path.abspath("scratch/test_reader_c35.html")
])

# Capture at 1280x720 (Standard laptop resolution like in the user's screenshot)
png_path_laptop = os.path.join(brain_dir, "vocab_card_no_overlap_laptop.png")
subprocess.run([
    chrome_path, "--headless", "--disable-gpu",
    "--virtual-time-budget=2000",
    f"--screenshot={png_path_laptop}",
    "--window-size=1280,720",
    os.path.abspath("scratch/test_reader_c35.html")
])

print("Generated screenshots:", os.path.exists(png_path), os.path.exists(png_path_laptop))
