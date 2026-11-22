import http.server
import socketserver
import subprocess
import json
import threading
import time

PORT = 8998
results = {}
running = True

class TestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        global results, running
        results = json.loads(post_data.decode('utf-8'))
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')
        running = False

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

server = socketserver.TCPServer(("", PORT), TestHandler)
def run_server():
    while running:
        server.handle_request()

t = threading.Thread(target=run_server)
t.daemon = True
t.start()

test_html = f"""<!DOCTYPE html>
<html>
<body>
<script>
async function run() {{
  function getVoicesPromise() {{
    return new Promise(resolve => {{
      let v = window.speechSynthesis.getVoices();
      if (v.length) return resolve(v);
      window.speechSynthesis.onvoiceschanged = () => {{
        resolve(window.speechSynthesis.getVoices());
      }};
      setTimeout(() => resolve(window.speechSynthesis.getVoices()), 1000);
    }});
  }}

  const voices = await getVoicesPromise();
  const voiceList = voices.map(v => ({{
    name: v.name,
    lang: v.lang
  }}));

  let audioError = null;
  let audioCanPlay = false;
  try {{
    const a = new Audio('https://translate.google.com/translate_tts?ie=UTF-8&tl=ar&client=tw-ob&q=%D8%A7%D9%8E%D9%84%D9%92%D8%A8%D9%8E%D9%8A%D9%92%D8%AA%D9%8F');
    await new Promise((res) => {{
      a.oncanplaythrough = () => {{ audioCanPlay = true; res(); }};
      a.onerror = (e) => {{ audioError = 'Audio error: ' + (a.error ? a.error.code : 'unknown'); res(); }};
      setTimeout(() => res(), 1500);
    }});
  }} catch (e) {{
    audioError = e.message;
  }}

  const data = {{
    voices: voiceList,
    audioCanPlay,
    audioError
  }};

  await fetch('http://localhost:{PORT}', {{
    method: 'POST',
    headers: {{ 'Content-Type': 'application/json' }},
    body: JSON.stringify(data)
  }});
  window.close();
}}
run();
</script>
</body>
</html>
"""

with open("scratch/test_audio_diag2.html", "w", encoding="utf-8") as f:
    f.write(test_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
proc = subprocess.Popen([
    chrome_path, "--headless", "--disable-gpu",
    f"http://localhost:{PORT}/scratch/test_audio_diag2.html"
])

for _ in range(30):
    if not running:
        break
    time.sleep(0.2)

proc.terminate()
print("DIAGNOSTIC RESULTS:")
print(json.dumps(results, indent=2))
server.server_close()
