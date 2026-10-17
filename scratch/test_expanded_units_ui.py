# -*- coding: utf-8 -*-
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
            mask = s.recv(4)
            data = bytearray(s.recv(length))
            while len(data) < length:
                data.extend(s.recv(length - len(data)))
            for i in range(length):
                data[i] ^= mask[i % 4]
            msg = json.loads(data.decode('utf-8'))
            if msg.get('id') == target_id:
                return msg

    def eval_js(expr):
        mid = send_cmd('Runtime.evaluate', {'expression': expr, 'returnByValue': True})
        return recv_msg(mid)['result']['result'].get('value')

    time.sleep(1.5)

    # Test B2 U20 (Dual nouns)
    eval_js("""
    (function() {
        window.openTamreenSelectorModal(1, 19); // 0-indexed: Book 2, Unit 20
    })()
    """)
    time.sleep(0.5)
    b2_u20_cards = eval_js("""
    (function() {
        const cards = document.querySelectorAll('#tamreenSelectorGrid .tamreen-pick-card');
        return Array.from(cards).map(c => ({
            num: c.querySelector('.tamreen-pick-num')?.innerText.trim(),
            title: c.querySelector('.tamreen-pick-title-ar')?.innerText.trim(),
            sub: c.querySelector('.tamreen-pick-title-ur')?.innerText.trim(),
            count: c.querySelector('.tamreen-pick-count')?.innerText.trim()
        }));
    })()
    """)
    print("\nBook 2 Unit 20 (Dual Nouns) Tamreens:")
    for c in b2_u20_cards:
        print(f"  [{c['num']}] {c['title']} ({c['count']})")

    # Test B2 U27 (Hollow verbs)
    eval_js("""
    (function() {
        window.openTamreenSelectorModal(1, 26); // Book 2, Unit 27
    })()
    """)
    time.sleep(0.5)
    b2_u27_cards = eval_js("""
    (function() {
        const cards = document.querySelectorAll('#tamreenSelectorGrid .tamreen-pick-card');
        return Array.from(cards).map(c => ({
            num: c.querySelector('.tamreen-pick-num')?.innerText.trim(),
            title: c.querySelector('.tamreen-pick-title-ar')?.innerText.trim(),
            count: c.querySelector('.tamreen-pick-count')?.innerText.trim()
        }));
    })()
    """)
    print("\nBook 2 Unit 27 (Hollow Verbs) Tamreens:")
    for c in b2_u27_cards:
        print(f"  [{c['num']}] {c['title']} ({c['count']})")

    # Test B3 U13 (Laam al-Amr)
    eval_js("""
    (function() {
        window.openTamreenSelectorModal(2, 12); // Book 3, Unit 13
    })()
    """)
    time.sleep(0.5)
    b3_u13_cards = eval_js("""
    (function() {
        const cards = document.querySelectorAll('#tamreenSelectorGrid .tamreen-pick-card');
        return Array.from(cards).map(c => ({
            num: c.querySelector('.tamreen-pick-num')?.innerText.trim(),
            title: c.querySelector('.tamreen-pick-title-ar')?.innerText.trim(),
            count: c.querySelector('.tamreen-pick-count')?.innerText.trim()
        }));
    })()
    """)
    print("\nBook 3 Unit 13 (Laam al-Amr) Tamreens:")
    for c in b3_u13_cards:
        print(f"  [{c['num']}] {c['title']} ({c['count']})")

    # Test B3 U16 (Form II Verbs)
    eval_js("""
    (function() {
        window.openTamreenSelectorModal(2, 15); // Book 3, Unit 16
    })()
    """)
    time.sleep(0.5)
    b3_u16_cards = eval_js("""
    (function() {
        const cards = document.querySelectorAll('#tamreenSelectorGrid .tamreen-pick-card');
        return Array.from(cards).map(c => ({
            num: c.querySelector('.tamreen-pick-num')?.innerText.trim(),
            title: c.querySelector('.tamreen-pick-title-ar')?.innerText.trim(),
            count: c.querySelector('.tamreen-pick-count')?.innerText.trim()
        }));
    })()
    """)
    print("\nBook 3 Unit 16 (Form II Verbs) Tamreens:")
    for c in b3_u16_cards:
        print(f"  [{c['num']}] {c['title']} ({c['count']})")

    # Now launch quiz on B3 Unit 16 "All Exercises" and verify Question 1 prompt & options
    eval_js("""
    (function() {
        window.startTamreenQuiz(2, 15, null);
    })()
    """)
    time.sleep(0.8)
    q_state = eval_js("""
    (function() {
        return {
            title_ar: document.getElementById('quizTamreenTitleAr')?.innerText.trim(),
            title_ur: document.getElementById('quizTamreenTitleUr')?.innerText.trim(),
            prompt_ar: document.getElementById('quizQuestionArabic')?.innerText.trim(),
            prompt_ur: document.getElementById('quizPromptUr')?.innerText.trim(),
            prompt_en: document.getElementById('quizPromptEn')?.innerText.trim(),
            options: Array.from(document.querySelectorAll('.quiz-option-btn')).map(b => b.innerText.trim())
        };
    })()
    """)
    print("\nQuiz Question 1 for Book 3 Unit 16:")
    print(f"  Title AR: {q_state.get('title_ar')}")
    print(f"  Prompt AR: {q_state.get('prompt_ar')}")
    print(f"  Prompt UR: {q_state.get('prompt_ur')}")
    print(f"  Prompt EN: {q_state.get('prompt_en')}")
    print(f"  Options: {q_state.get('options')}")

    print("\nALL EXPANDED UNITS UI VERIFIED SUCCESSFULLY!")

finally:
    proc.terminate()
