import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys

temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9889

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

    mid = 1
    def send_cmd(method, params=None):
        global mid
        m = mid
        mid += 1
        payload = json.dumps({"id": m, "method": method, "params": params or {}}).encode('utf-8')
        frame = bytearray([0x81, 0x80 | len(payload)])
        mask_key = os.urandom(4)
        frame.extend(mask_key)
        frame.extend(bytearray(payload[i] ^ mask_key[i % 4] for i in range(len(payload))))
        s.sendall(frame)
        return m

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

    # Let's inspect what happens during click
    m = send_cmd("Runtime.evaluate", {
        "expression": "(() => { "
                      "  const btn = document.getElementById('splashInstallBtn'); "
                      "  const backdrop = document.getElementById('installGuideBackdrop'); "
                      "  const before = backdrop.className; "
                      "  btn.click(); "
                      "  const after = backdrop.className; "
                      "  return { before, after, btnFound: !!btn, backdropFound: !!backdrop }; "
                      "})()"
    })
    res = recv_msg(m)
    print("Click Evaluation Result:", json.dumps(res, indent=2))
finally:
    proc.terminate()
