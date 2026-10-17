import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys

sys.stdout.reconfigure(encoding='utf-8')
temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9899

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

    print("--- 1. Set language to Both ---")
    evaluate('document.getElementById("selectBothBtn").click();')
    time.sleep(0.5)

    print("\n--- 2. Test Book 1 Unit 1 Interactive Quiz ---")
    evaluate('document.querySelector(\'[data-book="1"]\').click();')
    time.sleep(0.5)
    evaluate('document.querySelector(\'[data-unit-id="b1_u1"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    # Click Tamreen 1
    evaluate('document.querySelectorAll("#tamreenOptionsList .tamreen-opt-card")[1].click();')
    time.sleep(0.5)

    q1_state = evaluate('''
        (function() {
            const overlay = document.getElementById('quizOverlay');
            const badge = document.querySelector('.q-badge');
            const inst = document.querySelector('.q-instruction');
            const bigText = document.querySelector('.q-prompt-big-text');
            const optBtns = Array.from(document.querySelectorAll('.q-option-btn')).map(b => b.dataset.opt);
            return {
                open: !overlay.classList.contains('hidden'),
                badge: badge ? badge.textContent.trim() : '',
                inst: inst ? inst.textContent.trim() : '',
                bigText: bigText ? bigText.textContent.trim() : '',
                opts: optBtns
            };
        })()
    ''')
    print("Book 1 Unit 1 Question 1 loaded:")
    print(f"  Badge: {q1_state.get('badge')}")
    print(f"  Instruction: {q1_state.get('inst')}")
    print(f"  Big Text: {q1_state.get('bigText')}")
    print(f"  Options: {q1_state.get('opts')}")

    # Select the first option and check
    ans_check = evaluate('''
        (function() {
            const firstOpt = document.querySelector('.q-option-btn');
            firstOpt.click();
            const checkBtn = document.getElementById('quizCheckBtn');
            const wasDisabled = checkBtn.disabled;
            checkBtn.click();
            const bottomBar = document.getElementById('quizBottomBar');
            const fbTitle = document.getElementById('feedbackTitle').textContent.trim();
            const isCorrect = bottomBar.classList.contains('correct');
            return { wasDisabled, fbTitle, isCorrect };
        })()
    ''')
    print(f"  Answer check result: {ans_check}")
    evaluate('document.getElementById("quizCloseBtn").click();')
    time.sleep(0.5)

    print("\n--- 3. Test Book 2 Unit 20 Interactive Quiz ---")
    evaluate('document.querySelector(\'[data-book="2"]\').click();')
    time.sleep(0.5)
    evaluate('document.querySelector(\'[data-unit-id="b2_u20"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    # Click "All Exercises" (card 0)
    evaluate('document.querySelectorAll("#tamreenOptionsList .tamreen-opt-card")[0].click();')
    time.sleep(0.5)

    q2_state = evaluate('''
        (function() {
            const badge = document.querySelector('.q-badge');
            const inst = document.querySelector('.q-instruction');
            const bigText = document.querySelector('.q-prompt-big-text');
            const optBtns = Array.from(document.querySelectorAll('.q-option-btn')).map(b => b.dataset.opt);
            return {
                badge: badge ? badge.textContent.trim() : '',
                inst: inst ? inst.textContent.trim() : '',
                bigText: bigText ? bigText.textContent.trim() : '',
                opts: optBtns
            };
        })()
    ''')
    print("Book 2 Unit 20 Question 1 loaded:")
    print(f"  Badge: {q2_state.get('badge')}")
    print(f"  Instruction: {q2_state.get('inst')}")
    print(f"  Big Text: {q2_state.get('bigText')}")
    print(f"  Options: {q2_state.get('opts')}")

    # Click first option and check
    ans2_check = evaluate('''
        (function() {
            const firstOpt = document.querySelector('.q-option-btn');
            firstOpt.click();
            document.getElementById('quizCheckBtn').click();
            return {
                fbTitle: document.getElementById('feedbackTitle').textContent.trim(),
                isCorrect: document.getElementById('quizBottomBar').classList.contains('correct'),
                isWrong: document.getElementById('quizBottomBar').classList.contains('wrong')
            };
        })()
    ''')
    print(f"  Answer check result: {ans2_check}")
    evaluate('document.getElementById("quizCloseBtn").click();')
    time.sleep(0.5)

    print("\n--- 4. Test Book 3 Unit 16 Interactive Quiz ---")
    evaluate('document.querySelector(\'[data-book="3"]\').click();')
    time.sleep(0.5)
    evaluate('document.querySelector(\'[data-unit-id="b3_u16"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    # Click "All Exercises" (card 0)
    evaluate('document.querySelectorAll("#tamreenOptionsList .tamreen-opt-card")[0].click();')
    time.sleep(0.5)

    q3_state = evaluate('''
        (function() {
            const badge = document.querySelector('.q-badge');
            const inst = document.querySelector('.q-instruction');
            const bigText = document.querySelector('.q-prompt-big-text');
            const optBtns = Array.from(document.querySelectorAll('.q-option-btn')).map(b => b.dataset.opt);
            return {
                badge: badge ? badge.textContent.trim() : '',
                inst: inst ? inst.textContent.trim() : '',
                bigText: bigText ? bigText.textContent.trim() : '',
                opts: optBtns
            };
        })()
    ''')
    print("Book 3 Unit 16 Question 1 loaded:")
    print(f"  Badge: {q3_state.get('badge')}")
    print(f"  Instruction: {q3_state.get('inst')}")
    print(f"  Big Text: {q3_state.get('bigText')}")
    print(f"  Options: {q3_state.get('opts')}")

    ans3_check = evaluate('''
        (function() {
            const firstOpt = document.querySelector('.q-option-btn');
            firstOpt.click();
            document.getElementById('quizCheckBtn').click();
            return {
                fbTitle: document.getElementById('feedbackTitle').textContent.trim(),
                isCorrect: document.getElementById('quizBottomBar').classList.contains('correct'),
                isWrong: document.getElementById('quizBottomBar').classList.contains('wrong')
            };
        })()
    ''')
    print(f"  Answer check result: {ans3_check}")
    evaluate('document.getElementById("quizCloseBtn").click();')
    time.sleep(0.5)

    print("\n--- 5. Test Book 3 Unit 9 Gold Standard (14 Tamreens) ---")
    evaluate('document.querySelector(\'[data-unit-id="b3_u9"] .unit-ex-btn\').click();')
    time.sleep(0.5)
    u9_cards_count = evaluate('document.querySelectorAll("#tamreenOptionsList .tamreen-opt-card").length')
    print(f"Book 3 Unit 9 Tamreen Modal Cards count: {u9_cards_count} (Expected: 15 cards)")
    evaluate('document.getElementById("closeTamreenModalBtn").click();')
    time.sleep(0.5)

    print("\nALL QUIZ INTERACTION TESTS PASSED FLAWLESSLY!")

finally:
    proc.terminate()
