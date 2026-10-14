import subprocess, time, json, urllib.request, urllib.parse

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Launch Chrome with remote debugging
proc = subprocess.Popen([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--window-size=1200,800',
    'about:blank'
])

time.sleep(1.5)

try:
    # Get WebSocket debugger URL
    resp = urllib.request.urlopen('http://localhost:9222/json/list')
    tabs = json.loads(resp.read())
    print("Tabs found:", len(tabs))
    ws_url = tabs[0]['webSocketDebuggerUrl']
    print("WS URL:", ws_url)
finally:
    proc.terminate()
