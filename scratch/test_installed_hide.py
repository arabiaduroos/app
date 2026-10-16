import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys
sys.stdout.reconfigure(encoding='utf-8')

temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9896

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

    # 1. Check before installation
    m = send_cmd("Runtime.evaluate", {
        "expression": "(() => { "
                      "  const wrap = document.querySelector('.splash-install-wrap'); "
                      "  const btn = document.getElementById('splashInstallBtn'); "
                      "  return JSON.stringify({ wrapVisible: wrap.style.display !== 'none', btnVisible: btn.style.display !== 'none' }); "
                      "})()"
    })
    res = recv_msg(m)
    print("BEFORE INSTALL:", res["result"]["result"]["value"])

    # 2. Simulate installation (appinstalled event)
    m = send_cmd("Runtime.evaluate", {
        "expression": "(() => { "
                      "  window.dispatchEvent(new Event('appinstalled')); "
                      "  const wrap = document.querySelector('.splash-install-wrap'); "
                      "  const btn = document.getElementById('splashInstallBtn'); "
                      "  const topbar = document.getElementById('topbarInstallBtn'); "
                      "  return JSON.stringify({ "
                      "    storedFlag: localStorage.getItem('madinah_pwa_installed'), "
                      "    splashWrapDisplay: wrap.style.display, "
                      "    splashBtnDisplay: btn.style.display, "
                      "    topbarDisplay: topbar.style.display, "
                      "    isAppInstalled: window.isAppInstalled ? window.isAppInstalled() : 'checked' "
                      "  }); "
                      "})()"
    })
    res = recv_msg(m)
    print("AFTER INSTALL SIMULATION:")
    print(json.dumps(json.loads(res["result"]["result"]["value"]), indent=2))

    # 3. Capture screenshot of splash screen with install button DISAPPEARED
    m = send_cmd("Page.captureScreenshot", {"format": "png"})
    res = recv_msg(m)
    out_path = os.path.abspath(r'scratch\splash_screen_installed_hidden.png')
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(res["result"]["data"]))
    print("Screenshot of installed splash screen saved to:", out_path)

finally:
    proc.terminate()
