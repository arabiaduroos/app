import os
import subprocess

with open("scratch/test_reader_c35.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the script to wait until init is done
old_script = """<script>
  localStorage.setItem('madinah_lang', 'both');
  window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
      const u3 = window.app.DATA.books[0].units.find(u => u.id === 'b1_u3');
      window.app.openLessonCardReader(u3);
      window.app.lessonReader.index = 34; // Card 35
      window.app.renderCurrentLessonCard();
    }, 200);
  });
</script>"""

new_script = """<script>
  localStorage.setItem('madinah_lang', 'both');
  window.addEventListener('load', () => {
    setTimeout(() => {
      // Force reader open on Unit 3, Card 35
      const u3 = window.app.DATA.books[0].units.find(u => u.id === 'b1_u3');
      window.app.openLessonCardReader(u3);
      window.app.lessonReader.index = 34; // Card 35
      window.app.renderCurrentLessonCard();
      document.getElementById('lessonReaderModal').classList.remove('hidden');
      document.getElementById('lessonReaderModal').style.zIndex = '99999';
    }, 1200);
  });
</script>"""

html = html.replace(old_script, new_script)

with open("scratch/test_reader_c35.html", "w", encoding="utf-8") as f:
    f.write(html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
brain_dir = r"C:\Users\Person\.gemini\antigravity\brain\548db058-a481-48f4-9024-0b3a7fd2647c"
png_path = os.path.join(brain_dir, "vocab_card_verified_clean.png")

subprocess.run([
    chrome_path, "--headless", "--disable-gpu",
    "--virtual-time-budget=4000",
    f"--screenshot={png_path}",
    "--window-size=1200,720",
    os.path.abspath("scratch/test_reader_c35.html")
])

print("Screenshot generated:", os.path.exists(png_path))
