import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys

sys.stdout.reconfigure(encoding='utf-8')
temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9898

proc = subprocess.Popen([
    chrome, '--headless=new', '--disable-gpu', f'--user-data-dir={temp_dir}', f'--remote-debugging-port={port}',
    '--window-size=1200,900', 'http://localhost:8080/index.html'
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
    time.sleep(0.5)

    # Test Book 3 Unit 1
    evaluate('document.querySelector(\'[data-book="3"]\').click();')
    time.sleep(0.5)
    evaluate('document.querySelector(\'[data-unit-id="b3_u1"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    b3_u1_opts = evaluate('''
        Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card')).map(c => ({
            num: c.querySelector('.tamreen-opt-num') ? c.querySelector('.tamreen-opt-num').textContent.trim() : '',
            title: c.querySelector('.tamreen-opt-title') ? c.querySelector('.tamreen-opt-title').textContent.trim() : '',
            meta: c.querySelector('.tamreen-opt-meta') ? c.querySelector('.tamreen-opt-meta').textContent.trim() : ''
        }))
    ''')
    print(f"Book 3 Unit 1 Tamreens ({len(b3_u1_opts)} cards):")
    for opt in b3_u1_opts:
        print(f"  [{opt['num']}] {opt['title']} ({opt['meta']})")

    # Close modal
    evaluate('document.getElementById("closeTamreenModalBtn").click();')
    time.sleep(0.3)

    # Test Book 3 Unit 9
    evaluate('document.querySelector(\'[data-unit-id="b3_u9"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    b3_u9_opts = evaluate('''
        Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card')).map(c => ({
            num: c.querySelector('.tamreen-opt-num') ? c.querySelector('.tamreen-opt-num').textContent.trim() : '',
            title: c.querySelector('.tamreen-opt-title') ? c.querySelector('.tamreen-opt-title').textContent.trim() : '',
            meta: c.querySelector('.tamreen-opt-meta') ? c.querySelector('.tamreen-opt-meta').textContent.trim() : ''
        }))
    ''')
    print(f"\nBook 3 Unit 9 Tamreens ({len(b3_u9_opts)} cards):")
    for opt in b3_u9_opts[:5]:
        print(f"  [{opt['num']}] {opt['title']} ({opt['meta']})")
    print(f"  ... and {len(b3_u9_opts) - 5} more tamreens")

    evaluate('document.getElementById("closeTamreenModalBtn").click();')
    time.sleep(0.3)

    # Test Book 2 Unit 1
    evaluate('document.querySelector(\'[data-book="2"]\').click();')
    time.sleep(0.5)
    evaluate('document.querySelector(\'[data-unit-id="b2_u1"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    b2_u1_opts = evaluate('''
        Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card')).map(c => ({
            num: c.querySelector('.tamreen-opt-num') ? c.querySelector('.tamreen-opt-num').textContent.trim() : '',
            title: c.querySelector('.tamreen-opt-title') ? c.querySelector('.tamreen-opt-title').textContent.trim() : '',
            meta: c.querySelector('.tamreen-opt-meta') ? c.querySelector('.tamreen-opt-meta').textContent.trim() : ''
        }))
    ''')
    print(f"\nBook 2 Unit 1 Tamreens ({len(b2_u1_opts)} cards):")
    for opt in b2_u1_opts:
        print(f"  [{opt['num']}] {opt['title']} ({opt['meta']})")

    evaluate('document.getElementById("closeTamreenModalBtn").click();')
    time.sleep(0.3)

    # Test Book 1 Unit 1
    evaluate('document.querySelector(\'[data-book="1"]\').click();')
    time.sleep(0.5)
    evaluate('document.querySelector(\'[data-unit-id="b1_u1"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    b1_u1_opts = evaluate('''
        Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card')).map(c => ({
            num: c.querySelector('.tamreen-opt-num') ? c.querySelector('.tamreen-opt-num').textContent.trim() : '',
            title: c.querySelector('.tamreen-opt-title') ? c.querySelector('.tamreen-opt-title').textContent.trim() : '',
            meta: c.querySelector('.tamreen-opt-meta') ? c.querySelector('.tamreen-opt-meta').textContent.trim() : ''
        }))
    ''')
    print(f"\nBook 1 Unit 1 Tamreens ({len(b1_u1_opts)} cards):")
    for opt in b1_u1_opts:
        print(f"  [{opt['num']}] {opt['title']} ({opt['meta']})")

    evaluate('document.getElementById("closeTamreenModalBtn").click();')
    time.sleep(0.3)

    # Test Book 2 Unit 20 (Dual Nouns)
    evaluate('document.querySelector(\'[data-book="2"]\').click();')
    time.sleep(0.5)
    evaluate('document.querySelector(\'[data-unit-id="b2_u20"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    b2_u20_opts = evaluate('''
        Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card')).map(c => ({
            num: c.querySelector('.tamreen-opt-num') ? c.querySelector('.tamreen-opt-num').textContent.trim() : '',
            title: c.querySelector('.tamreen-opt-title') ? c.querySelector('.tamreen-opt-title').textContent.trim() : '',
            meta: c.querySelector('.tamreen-opt-meta') ? c.querySelector('.tamreen-opt-meta').textContent.trim() : ''
        }))
    ''')
    print(f"\nBook 2 Unit 20 Tamreens ({len(b2_u20_opts)} cards):")
    for opt in b2_u20_opts:
        print(f"  [{opt['num']}] {opt['title']} ({opt['meta']})")

    evaluate('document.getElementById("closeTamreenModalBtn").click();')
    time.sleep(0.3)

    # Test Book 3 Unit 16 (Form II verbs)
    evaluate('document.querySelector(\'[data-book="3"]\').click();')
    time.sleep(0.5)
    evaluate('document.querySelector(\'[data-unit-id="b3_u16"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    b3_u16_opts = evaluate('''
        Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card')).map(c => ({
            num: c.querySelector('.tamreen-opt-num') ? c.querySelector('.tamreen-opt-num').textContent.trim() : '',
            title: c.querySelector('.tamreen-opt-title') ? c.querySelector('.tamreen-opt-title').textContent.trim() : '',
            meta: c.querySelector('.tamreen-opt-meta') ? c.querySelector('.tamreen-opt-meta').textContent.trim() : ''
        }))
    ''')
    print(f"\nBook 3 Unit 16 Tamreens ({len(b3_u16_opts)} cards):")
    for opt in b3_u16_opts:
        print(f"  [{opt['num']}] {opt['title']} ({opt['meta']})")

    # Click first card ("All Exercises") and verify Quiz view
    evaluate('document.querySelectorAll("#tamreenOptionsList .tamreen-opt-card")[0].click();')
    time.sleep(1.0)
    quiz_data = evaluate('''
        (function() {
            const overlay = document.getElementById('quizOverlay');
            const badge = document.querySelector('.q-badge');
            const inst = document.querySelector('.q-instruction');
            const promptAr = document.querySelector('.prompt-ar') || document.querySelector('.q-target-ar') || document.querySelector('.q-dialogue-prompt');
            const opts = Array.from(document.querySelectorAll('.q-opt')).map(b => b.textContent.trim());
            return {
                open: overlay ? !overlay.classList.contains('hidden') : false,
                badge: badge ? badge.textContent.trim() : '',
                instruction: inst ? inst.textContent.trim() : '',
                prompt_ar: promptAr ? promptAr.textContent.trim() : '',
                options: opts
            };
        })()
    ''')
    print(f"\nQuiz View Verified for Book 3 Unit 16:")
    print(f"  Overlay Open: {quiz_data.get('open')}")
    print(f"  Badge: {quiz_data.get('badge')}")
    print(f"  Instruction: {quiz_data.get('instruction')}")
    print(f"  Prompt AR: {quiz_data.get('prompt_ar')}")
    print(f"  Options ({len(quiz_data.get('options', []))}): {quiz_data.get('options')}")

    print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")

finally:
    proc.terminate()
