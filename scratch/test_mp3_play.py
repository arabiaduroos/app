import os
import subprocess
import json

test_html = """<!DOCTYPE html>
<html>
<body>
<audio id="player" src="test_hamed.mp3"></audio>
<script>
const a = document.getElementById('player');
a.oncanplaythrough = () => {
  document.body.innerHTML += '<div id="res">CAN_PLAY</div>';
};
a.onerror = () => {
  document.body.innerHTML += '<div id="res">ERROR_' + (a.error ? a.error.code : 'unknown') + '</div>';
};
</script>
</body>
</html>
"""

with open("scratch/test_mp3_page.html", "w", encoding="utf-8") as f:
    f.write(test_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out = subprocess.check_output([
    chrome_path, "--headless", "--disable-gpu",
    "--virtual-time-budget=2000",
    "--dump-dom",
    os.path.abspath("scratch/test_mp3_page.html")
]).decode("utf-8")

print("Result in DOM:", "CAN_PLAY" in out, "ERROR" in out)
