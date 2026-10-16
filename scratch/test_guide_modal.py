import subprocess, os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
out_path = os.path.abspath(r'scratch\screenshot_install_modal.png')

# We can tell Chrome to open index.html and evaluate a script via DevTools or we can test an HTML test harness or headless automation
# Let's write a small script that launches Chrome with remote debugging and uses Python socket/json to send CDP commands
import json, urllib.request, time

proc = subprocess.Popen([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9333',
    '--window-size=1200,900',
    'http://localhost:8080/index.html'
])

try:
    time.sleep(2)
    tabs = json.loads(urllib.request.urlopen('http://localhost:9333/json/list').read())
    ws_url = tabs[0]['webSocketDebuggerUrl']
    print("Connected to tab:", tabs[0]['title'])

    # We can connect using a raw socket or simple websocket handshake
    import socket, base64, os, struct

    # Simple websocket client implementation in pure standard library
    host = 'localhost'
    port = 9333
    path = ws_url.split(f'{host}:{port}')[1]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    key = base64.b64encode(os.urandom(16)).decode('utf-8')
    req = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}:{port}\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        f"Sec-WebSocket-Key: {key}\r\n"
        "Sec-WebSocket-Version: 13\r\n\r\n"
    )
    s.sendall(req.encode('utf-8'))

    # Read handshake response
    resp = b""
    while b"\r\n\r\n" not in resp:
        resp += s.recv(1024)

    print("WebSocket Handshake Success!")

    def send_cdp(method, params=None, msg_id=1):
        payload = json.dumps({"id": msg_id, "method": method, "params": params or {}}).encode('utf-8')
        # Masked websocket frame from client
        frame = bytearray()
        frame.append(0x81) # text frame, fin
        length = len(payload)
        mask_key = os.urandom(4)
        if length < 126:
            frame.append(0x80 | length)
        elif length < 65536:
            frame.append(0x80 | 126)
            frame.extend(struct.pack('>H', length))
        else:
            frame.append(0x80 | 127)
            frame.extend(struct.pack('>Q', length))
        frame.extend(mask_key)
        masked_payload = bytearray(payload[i] ^ mask_key[i % 4] for i in range(len(payload)))
        frame.extend(masked_payload)
        s.sendall(frame)

    def recv_cdp():
        # Read frame
        header = s.recv(2)
        if not header: return None
        length = header[1] & 0x7f
        if length == 126:
            length = struct.unpack('>H', s.recv(2))[0]
        elif length == 127:
            length = struct.unpack('>Q', s.recv(8))[0]
        data = b""
        while len(data) < length:
            data += s.recv(length - len(data))
        return json.loads(data.decode('utf-8'))

    # Enable Runtime and Page
    send_cdp("Runtime.enable", msg_id=1)
    time.sleep(0.5)

    # Click the splash install button
    send_cdp("Runtime.evaluate", {"expression": "document.getElementById('splashInstallBtn').click();"}, msg_id=2)
    time.sleep(1)

    # Capture screenshot
    send_cdp("Page.captureScreenshot", {"format": "png"}, msg_id=3)
    
    # Wait for screenshot response
    start = time.time()
    img_data = None
    while time.time() - start < 5:
        msg = recv_cdp()
        if msg and msg.get("id") == 3:
            img_data = msg["result"]["data"]
            break

    if img_data:
        with open(out_path, "wb") as f:
            f.write(base64.b64decode(img_data))
        print("Install guide screenshot saved successfully to:", out_path)
    else:
        print("Failed to capture screenshot")

finally:
    proc.terminate()
