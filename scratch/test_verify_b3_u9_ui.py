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
    '--window-size=1200,900',
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

    def evaluate(expr):
        mid = send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
        res = recv_msg(mid)
        val = res.get('result', {}).get('result', {}).get('value')
        if val is None and 'result' in res.get('result', {}):
            print("EVAL ERROR/RESULT:", res['result']['result'])
        return val

    def capture_screenshot(path):
        mid = send_cmd("Page.captureScreenshot")
        res = recv_msg(mid)
        img_b64 = res['result']['data']
        with open(path, 'wb') as f:
            f.write(base64.b64decode(img_b64))
        print(f"Screenshot saved: {path}")

    # 1. Click both language button
    evaluate("document.getElementById('selectBothBtn').click();")
    time.sleep(0.5)

    # 2. Click Book 3 tab
    evaluate("document.querySelector('[data-book=\"3\"]').click();")
    time.sleep(0.5)

    # 3. Find Unit 9 card and inspect it
    u9_info = evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b3_u9\"]');
            if (!card) return 'b3_u9 card not found!';
            const exBtn = card.querySelector('.unit-ex-btn');
            return {
                title: card.querySelector('.unit-card-title').textContent,
                exBtnText: exBtn ? exBtn.textContent : 'none'
            };
        })()
    """)
    print("Unit 9 card info:", u9_info)

    # 4. Click the Tamreen button on Book 3 Unit 9
    evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b3_u9\"]');
            const btn = card.querySelector('.unit-ex-btn');
            btn.click();
        })()
    """)
    time.sleep(0.8)

    # 5. Check what is rendered inside the Tamreen Selector modal
    selector_info = evaluate("""
        (() => {
            const modal = document.getElementById('tamreenSelectorModal');
            const isVisible = !modal.classList.contains('hidden');
            const badge = document.getElementById('tamreenUnitBadge').textContent;
            const options = Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card')).map(c => ({
                num: c.querySelector('.tamreen-opt-num') ? c.querySelector('.tamreen-opt-num').textContent.trim() : '',
                title: c.querySelector('.tamreen-opt-title') ? c.querySelector('.tamreen-opt-title').textContent.trim() : '',
                meta: c.querySelector('.tamreen-opt-meta') ? c.querySelector('.tamreen-opt-meta').textContent.trim() : ''
            }));
            return { isVisible, badge, optionsCount: options.length, options };
        })()
    """)
    print("\nTamreen Selector Modal Info:")
    print("  Is Visible:", selector_info.get('isVisible'))
    print("  Badge:", selector_info.get('badge'))
    print("  Total Options Rendered:", selector_info.get('optionsCount'))
    print("\n  Exercises Rendered in Selector:")
    for opt in selector_info.get('options', []):
        print(f"    [{opt['num']}] {opt['title']} ({opt['meta']})")

    # Capture Tamreen Selector screenshot
    capture_screenshot('scratch/b3_u9_tamreen_selector.png')

    # 6. Click on All Exercises card
    evaluate("""
        (() => {
            const allOpt = document.querySelector('.tamreen-opt-card.all-tamreens');
            if (allOpt) allOpt.click();
        })()
    """)
    time.sleep(0.8)

    # 7. Check Quiz state
    quiz_info = evaluate("""
        (() => {
            const modal = document.getElementById('quizOverlay');
            const isVisible = !modal.classList.contains('hidden');
            const stage = document.getElementById('quizStage');
            const badge = stage.querySelector('.q-badge') ? stage.querySelector('.q-badge').textContent : '';
            const promptAr = stage.querySelector('.q-prompt-big-text') ? stage.querySelector('.q-prompt-big-text').textContent : '';
            const promptTrans = stage.querySelector('.q-prompt-hint') ? stage.querySelector('.q-prompt-hint').textContent : '';
            const options = Array.from(stage.querySelectorAll('.q-option-btn')).map(b => b.textContent.trim());
            return { isVisible, badge, promptAr, promptTrans, options };
        })()
    """)
    print("\nQuiz Modal Info:")
    print("  Is Visible:", quiz_info.get('isVisible'))
    print("  Badge:", quiz_info.get('badge'))
    print("  Prompt Arabic:", quiz_info.get('promptAr'))
    print("  Prompt Translation:", quiz_info.get('promptTrans'))
    print("  Options:", quiz_info.get('options'))

    # Capture Quiz Screenshot
    capture_screenshot('scratch/b3_u9_quiz_q1.png')

    # 8. Select option 0 and click check
    evaluate("""
        (() => {
            const firstOpt = document.querySelector('.q-option-btn');
            if (firstOpt) firstOpt.click();
            const checkBtn = document.getElementById('quizCheckBtn');
            if (checkBtn) checkBtn.click();
        })()
    """)
    time.sleep(0.5)

    capture_screenshot('scratch/b3_u9_quiz_feedback.png')
    print("\nVerification completed successfully!")

finally:
    proc.terminate()
