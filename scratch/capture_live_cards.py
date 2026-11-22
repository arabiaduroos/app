import os
import subprocess
import time

brain_dir = r"C:\Users\Person\.gemini\antigravity\brain\548db058-a481-48f4-9024-0b3a7fd2647c"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
app_dir = r"c:\Users\Person\Documents\GitHub\app"

test_cards = [
    ("app_live_c2_transform.png", 17, "Card 18: Option C2 Transformation (نجم -> النجم)"),
    ("app_live_qamari_card.png", 32, "Card 33: Moon Letters 7x2 Table"),
    ("app_live_shamsi_card.png", 33, "Card 34: Sun Letters 7x2 Table"),
    ("app_live_vocab_card.png", 34, "Card 35: Kalimatul Jadeeda Table")
]

# Read original index.html
with open(os.path.join(app_dir, "index.html"), "r", encoding="utf-8") as f:
    orig_html = f.read()

for filename, card_idx, desc in test_cards:
    # Inject script before </body> to bypass language modal and open reader directly to target card
    injection = f"""
    <script>
      localStorage.setItem('madinah_lang', 'both');
      window.addEventListener('DOMContentLoaded', () => {{
        setTimeout(() => {{
          const u3 = window.app.DATA.books[0].units.find(u => u.id === 'b1_u3');
          window.app.openLessonCardReader(u3);
          window.app.lessonReader.index = {card_idx};
          window.app.renderCurrentLessonCard();
        }}, 200);
      }});
    </script>
    </body>
    """
    modified_html = orig_html.replace("</body>", injection)
    test_html_path = os.path.join(brain_dir, "scratch", f"test_run_{card_idx}.html")
    with open(test_html_path, "w", encoding="utf-8") as f:
        f.write(modified_html)
    
    png_path = os.path.join(brain_dir, filename)
    subprocess.run([
        chrome_path, "--headless", "--disable-gpu",
        "--virtual-time-budget=2000",
        f"--screenshot={png_path}",
        "--window-size=1000,700",
        test_html_path
    ])
    print(f"Captured {filename}: {os.path.exists(png_path)}")
