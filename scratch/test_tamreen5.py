import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys

sys.stdout.reconfigure(encoding='utf-8')
temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9896

proc = subprocess.Popen([
    chrome, '--headless=new', '--disable-gpu', f'--user-data-dir={temp_dir}', f'--remote-debugging-port={port}',
    '--window-size=1200,900', 'http://localhost:8080/index.html'
])

try:
    time.sleep(2)
    resp = urllib.request.urlopen(f'http://localhost:{port}/json/list')
    tabs = json.loads(resp.read().decode('utf-8'))
    target_tab = [t for t in tabs if 'localhost:8080' in t.get('url', '')][0]
    ws_url = target_tab['webSocketDebuggerUrl']

    host = 'localhost'
    path = ws_url.split(f'{host}:{port}')[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    key = base64.b64encode(os.urandom(16)).decode('utf-8')
    req = f'GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n'
    s.sendall(req.encode('utf-8'))
    resp_data = b''
    while b'\r\n\r\n' not in resp_data:
        resp_data += s.recv(1024)

    msg_id = 1
    def send_cmd(method, params=None):
        global msg_id
        mid = msg_id
        msg_id += 1
        payload = json.dumps({'id': mid, 'method': method, 'params': params or {}}).encode('utf-8')
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
            data = b''
            while len(data) < length:
                chunk = s.recv(min(length - len(data), 65536))
                if not chunk: break
                data += chunk
            msg = json.loads(data.decode('utf-8'))
            if msg.get('id') == target_id:
                return msg

    send_cmd('Runtime.enable')
    recv_msg(1)

    def evaluate(expr):
        mid = send_cmd('Runtime.evaluate', {'expression': expr, 'returnByValue': True})
        res = recv_msg(mid)
        return res.get('result', {}).get('result', {}).get('value')

    evaluate('document.getElementById("selectBothBtn").click();')
    evaluate('document.querySelector(\'[data-book="3"]\').click();')
    time.sleep(0.5)

    evaluate('document.querySelector(\'[data-unit-id="b3_u9"] .unit-ex-btn\').click();')
    time.sleep(0.5)

    res = evaluate('''
        (() => {
            const cards = Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card'));
            const t5 = cards.find(c => {
                const numEl = c.querySelector('.tamreen-opt-num');
                return numEl && numEl.textContent.trim() === '5';
            });
            if (t5) {
                t5.click();
                return 'Clicked Tamreen 5';
            }
            return 'Tamreen 5 not found';
        })()
    ''')
    print('Action:', res)
    time.sleep(0.5)

    q_info = evaluate('''
        (() => {
            const stage = document.getElementById('quizStage');
            const badge = stage.querySelector('.q-badge') ? stage.querySelector('.q-badge').textContent : '';
            const promptAr = stage.querySelector('.q-prompt-big-text') ? stage.querySelector('.q-prompt-big-text').textContent : '';
            const options = Array.from(stage.querySelectorAll('.q-option-btn')).map(b => b.textContent.trim());
            return { badge, promptAr, optionsCount: options.length, options };
        })()
    ''')
    print('Tamreen 5 Quiz Info:', json.dumps(q_info, ensure_ascii=False, indent=2))

finally:
    proc.terminate()
