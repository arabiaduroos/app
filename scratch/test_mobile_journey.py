import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys
sys.stdout.reconfigure(encoding='utf-8')

temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9899

proc = subprocess.Popen([
    chrome,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}',
    f'--remote-debugging-port={port}',
    '--window-size=390,844',
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

    # Select Urdu
    send_cmd("Runtime.evaluate", {"expression": "document.getElementById('selectUrduBtn').click();"})
    time.sleep(0.5)

    # Capture mobile screenshot of journey view
    m = send_cmd("Page.captureScreenshot", {"format": "png"})
    res = recv_msg(m)
    out_path = os.path.abspath(r'scratch\mobile_home_journey.png')
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(res["result"]["data"]))
    print("Mobile journey view saved to:", out_path)

finally:
    proc.terminate()
