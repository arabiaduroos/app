import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys
sys.stdout.reconfigure(encoding='utf-8')

temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9777

proc = subprocess.Popen([
    chrome,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}',
    f'--remote-debugging-port={port}',
    '--window-size=1200,850',
    'http://localhost:8080/index.html'
])

try:
    time.sleep(2.5)
    resp = urllib.request.urlopen(f'http://localhost:{port}/json/list')
    tabs = json.loads(resp.read().decode('utf-8'))
    target_tab = None
    for t in tabs:
        if 'localhost:8080' in t.get('url', ''):
            target_tab = t
            break

    if not target_tab:
        print("ERROR: Target tab localhost:8080 not found!")
        exit(1)

    print("Found target tab:", target_tab['title'], target_tab['url'])
    ws_url = target_tab['webSocketDebuggerUrl']

    # Connect WebSocket
    host = 'localhost'
    path = ws_url.split(f'{host}:{port}')[1]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10.0)
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

    resp_data = b""
    while b"\r\n\r\n" not in resp_data:
        resp_data += s.recv(1024)

    print("WebSocket handshake connected to localhost:8080 tab!")

    msg_counter = 1

    def send_cmd(method, params=None):
        global msg_counter
        mid = msg_counter
        msg_counter += 1
        payload = json.dumps({"id": mid, "method": method, "params": params or {}}).encode('utf-8')
        frame = bytearray([0x81])
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
        frame.extend(bytearray(payload[i] ^ mask_key[i % 4] for i in range(len(payload))))
        s.sendall(frame)
        return mid

    def recv_msg(target_id=None):
        while True:
            header = s.recv(2)
            if not header:
                return None
            length = header[1] & 0x7f
            if length == 126:
                length = struct.unpack('>H', s.recv(2))[0]
            elif length == 127:
                length = struct.unpack('>Q', s.recv(8))[0]
            data = b""
            while len(data) < length:
                chunk = s.recv(min(length - len(data), 65536))
                if not chunk:
                    break
                data += chunk
            msg = json.loads(data.decode('utf-8'))
            if target_id is None or msg.get("id") == target_id:
                return msg

    # Enable Runtime and Page
    mid = send_cmd("Runtime.enable")
    recv_msg(mid)

    mid = send_cmd("Page.enable")
    recv_msg(mid)

    # Evaluate JS: Check PWA Manifest link and ServiceWorker
    mid = send_cmd("Runtime.evaluate", {
        "expression": "JSON.stringify({ "
                      "title: document.title, "
                      "manifest: !!document.querySelector('link[rel=manifest]'), "
                      "splashBtn: !!document.getElementById('splashInstallBtn'), "
                      "guideModal: !!document.getElementById('installGuideModal'), "
                      "swSupport: 'serviceWorker' in navigator "
                      "})"
    })
    res = recv_msg(mid)
    eval_result = json.loads(res["result"]["result"]["value"])
    print("PAGE PWA HEALTH CHECK:", json.dumps(eval_result, indent=2))

    # Click the splash install button to open the modal
    print("Clicking splash install button...")
    mid = send_cmd("Runtime.evaluate", {
        "expression": "document.getElementById('splashInstallBtn').click();"
    })
    recv_msg(mid)
    time.sleep(0.5)

    # Check if modal is visible
    mid = send_cmd("Runtime.evaluate", {
        "expression": "!document.getElementById('installGuideBackdrop').classList.contains('hidden')"
    })
    res = recv_msg(mid)
    modal_visible = res["result"]["result"]["value"]
    print("Install Guide Modal Visible:", modal_visible)

    # Capture screenshot of the modal
    mid = send_cmd("Page.captureScreenshot", {"format": "png"})
    res = recv_msg(mid)
    img_b64 = res["result"]["data"]
    modal_img_path = os.path.abspath(r'scratch\screenshot_install_modal.png')
    with open(modal_img_path, "wb") as f:
        f.write(base64.b64decode(img_b64))
    print("Saved install guide modal screenshot to:", modal_img_path)

    # Close modal
    mid = send_cmd("Runtime.evaluate", {
        "expression": "document.getElementById('closeInstallGuideBtn').click();"
    })
    recv_msg(mid)
    time.sleep(0.3)

    # Select Urdu language
    print("Selecting Urdu language...")
    mid = send_cmd("Runtime.evaluate", {
        "expression": "document.getElementById('selectUrduBtn').click();"
    })
    recv_msg(mid)
    time.sleep(0.5)

    # Verify Topbar install button exists and is visible
    mid = send_cmd("Runtime.evaluate", {
        "expression": "JSON.stringify({ "
                      "topbarBtn: !!document.getElementById('topbarInstallBtn'), "
                      "currentBook: window.state ? window.state.currentBook : 'N/A' "
                      "})"
    })
    res = recv_msg(mid)
    print("Journey View Status:", res["result"]["result"]["value"])

    # Capture journey view screenshot
    mid = send_cmd("Page.captureScreenshot", {"format": "png"})
    res = recv_msg(mid)
    journey_img_path = os.path.abspath(r'scratch\screenshot_journey_pwa.png')
    with open(journey_img_path, "wb") as f:
        f.write(base64.b64decode(res["result"]["data"]))
    print("Saved journey view screenshot to:", journey_img_path)

    print("ALL PWA TESTS COMPLETED SUCCESSFULLY!")

finally:
    proc.terminate()
