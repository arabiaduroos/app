import os
import subprocess

test_html = """<!DOCTYPE html>
<html>
<head>
  <meta name="referrer" content="no-referrer">
</head>
<body>
<script>
const a = new Audio('https://translate.google.com/translate_tts?ie=UTF-8&tl=ar&client=tw-ob&q=%D8%A7%D9%8E%D9%84%D9%92%D8%A8%D9%8E%D9%8A%D9%92%D8%AA%D9%8F');
a.oncanplaythrough = () => {
  document.body.innerHTML += '<div id="res">GOOGLE_TTS_CAN_PLAY</div>';
};
a.onerror = () => {
  document.body.innerHTML += '<div id="res">GOOGLE_TTS_ERROR_' + (a.error ? a.error.code : 'unknown') + '</div>';
};
</script>
</body>
</html>
"""

with open("scratch/test_no_referrer.html", "w", encoding="utf-8") as f:
    f.write(test_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out = subprocess.check_output([
    chrome_path, "--headless", "--disable-gpu",
    "--virtual-time-budget=3000",
    "--dump-dom",
    os.path.abspath("scratch/test_no_referrer.html")
]).decode("utf-8")

print(out)
