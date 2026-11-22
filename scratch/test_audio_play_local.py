import os
import subprocess

test_html = """<!DOCTYPE html>
<html>
<body>
<script>
const a = new Audio('../audio/aud_d4c49c94cb.mp3');
a.oncanplaythrough = () => {
  document.body.innerHTML = '<div id="status">AUDIO_SUCCESS</div>';
};
a.onerror = () => {
  document.body.innerHTML = '<div id="status">AUDIO_ERROR_' + (a.error ? a.error.code : 'unknown') + '</div>';
};
</script>
</body>
</html>
"""

with open("scratch/test_audio_play_file.html", "w", encoding="utf-8") as f:
    f.write(test_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out = subprocess.check_output([
    chrome_path, "--headless", "--disable-gpu",
    "--virtual-time-budget=2000",
    "--dump-dom",
    os.path.abspath("scratch/test_audio_play_file.html")
]).decode("utf-8")

print("Result:", "AUDIO_SUCCESS" in out, "AUDIO_ERROR" in out)
