import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys
sys.stdout.reconfigure(encoding='utf-8')

temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9895

proc = subprocess.Popen([
    chrome,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}',
    f'--remote-debugging-port={port}',
    '--window-size=1200,800',
    'http://localhost:8080/index.html'
])

try:
    time.sleep(2.5)
    resp = urllib.request.urlopen(f'http://localhost:{port}/json/list')
    tabs = json.loads(resp.read().decode('utf-8'))
    target_tab = [t for t in tabs if 'localhost:8080' in t.get('url', '')][0]
    ws_url = target_tab['webSocketDebuggerUrl']

    host = 'localhost'
    path = ws_url.split(f'{host}:{port}')[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    key = base64.b64encode(os.urandom(16)).decode('utf-8')
    req = f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n"
    s.sendall(req.encode('utf-8'))
    resp_data = b""
    while b"\r\n\r\n" not in resp_data:
        resp_data += s.recv(1024)

    msg_id = 1
    def send_cmd(method, params=None):
        global msg_id
        mid = msg_id
        msg_id += 1
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

    def recv_msg(target_id):
        while True:
            header = s.recv(2)
            length = header[1] & 0x7f
            if length == 126:
                length = struct.unpack('>H', s.recv(2))[0]
            elif length == 127:
                length = struct.unpack('>Q', s.recv(8))[0]
            data = b""
            while len(data) < length:
                chunk = s.recv(min(length - len(data), 65536))
                if not chunk: break
                data += chunk
            msg = json.loads(data.decode('utf-8'))
            if msg.get("id") == target_id:
                return msg

    send_cmd("Runtime.enable")
    recv_msg(1)

    # 1. Select language (Both: Urdu + English as shown in user screenshot!)
    print("Selecting language: both (English + Urdu)...")
    m = send_cmd("Runtime.evaluate", {
        "expression": "document.getElementById('selectBothBtn').click();"
    })
    recv_msg(m)
    time.sleep(0.5)

    # 2. Switch to Book 3
    print("Switching to Book 3...")
    m = send_cmd("Runtime.evaluate", {
        "expression": "document.querySelector(\"#bookSwitcher .book-pill[data-book='3']\").click();"
    })
    recv_msg(m)
    time.sleep(0.5)

    # 3. Find Unit 11 and click Read Lesson
    print("Opening Unit 11 Lesson Reader...")
    m = send_cmd("Runtime.evaluate", {
        "expression": "(() => { "
                      "  const cards = document.querySelectorAll('.journey-unit-card'); "
                      "  for (const c of cards) { "
                      "    if (c.textContent.includes('11') || c.textContent.includes('الحادي عشر') || c.textContent.includes('الْحَادِيَ عَشَرَ')) { "
                      "      c.querySelector('.unit-read-btn').click(); "
                      "      return true; "
                      "    } "
                      "  } "
                      "  return false; "
                      "})()"
    })
    recv_msg(m)
    time.sleep(1.0)

    # 4. Click Full Text Mode button (#readerModeFullBtn)
    print("Clicking Full Text Mode button...")
    m = send_cmd("Runtime.evaluate", {
        "expression": "document.getElementById('readerModeFullBtn').click();"
    })
    recv_msg(m)
    time.sleep(0.8)

    # 5. Verify the first element in full scroll
    m = send_cmd("Runtime.evaluate", {
        "expression": "(() => { "
                      "  const stage = document.getElementById('lessonStage'); "
                      "  const fullScroll = document.getElementById('lessonFullScroll'); "
                      "  const firstRow = fullScroll.querySelector('.t-illus-row'); "
                      "  const stageRect = stage.getBoundingClientRect(); "
                      "  const firstRect = firstRow.getBoundingClientRect(); "
                      "  return JSON.stringify({ "
                      "    stageTop: stageRect.top, "
                      "    firstRowTop: firstRect.top, "
                      "    firstRowArabic: firstRow.querySelector('.t-illus-ar').textContent, "
                      "    firstRowTrans: firstRow.querySelector('.t-illus-trans').textContent, "
                      "    isFullyVisible: firstRect.top >= stageRect.top "
                      "  }); "
                      "})()"
    })
    res = recv_msg(m)
    print("RAW RES:", json.dumps(res, indent=2))
    check_info = json.loads(res.get("result", {}).get("result", {}).get("value", "{}"))
    print("FIRST SENTENCE VISIBILITY CHECK:")
    print(json.dumps(check_info, indent=2, ensure_ascii=False))

    # 6. Capture full view screenshot
    m = send_cmd("Page.captureScreenshot", {"format": "png"})
    res = recv_msg(m)
    out_path = os.path.abspath(r'scratch\screenshot_fixed_full_view.png')
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(res["result"]["data"]))
    print("Full view screenshot saved to:", out_path)

    # 7. Switch back to Cards mode and capture screenshot
    print("Switching back to Cards mode...")
    m = send_cmd("Runtime.evaluate", {
        "expression": "document.getElementById('readerModeCardBtn').click();"
    })
    recv_msg(m)
    time.sleep(0.5)

    m = send_cmd("Page.captureScreenshot", {"format": "png"})
    res = recv_msg(m)
    card_path = os.path.abspath(r'scratch\screenshot_fixed_card_view.png')
    with open(card_path, "wb") as f:
        f.write(base64.b64decode(res["result"]["data"]))
    print("Card view screenshot saved to:", card_path)

finally:
    proc.terminate()
