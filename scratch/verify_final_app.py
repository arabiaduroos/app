import os
import subprocess

brain_dir = r"C:\Users\Person\.gemini\antigravity\brain\548db058-a481-48f4-9024-0b3a7fd2647c"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
app_dir = r"c:\Users\Person\Documents\GitHub\app"

with open(os.path.join(app_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Inject helper to open Unit 3 Card 35
helper = """
<script>
  localStorage.setItem('madinah_duo_state_v4', JSON.stringify({ lang: 'both', currentBook: 1, completed: {} }));
  window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('splashOverlay').classList.add('hidden');
    setTimeout(() => {
      const u3 = window.app.DATA.books[0].units.find(u => u.id === 'b1_u3');
      window.app.openLessonCardReader(u3);
      window.app.lessonReader.index = 34; // Card 35
      window.app.renderCurrentLessonCard();
    }, 100);
  });
</script>
</body>
"""

test_html = html.replace("</body>", helper)
test_file = os.path.join(brain_dir, "scratch", "test_final_c35.html")
with open(test_file, "w", encoding="utf-8") as f:
    f.write(test_html)

png_path = os.path.join(brain_dir, "vocab_final_verified.png")
subprocess.run([
    chrome_path, "--headless", "--disable-gpu",
    "--virtual-time-budget=2000",
    f"--screenshot={png_path}",
    "--window-size=1280,720",
    test_file
])

print("Final screenshot captured:", os.path.exists(png_path))
