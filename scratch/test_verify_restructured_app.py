import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys

sys.stdout.reconfigure(encoding='utf-8')

# Start Python HTTP server on port 8092
server_proc = subprocess.Popen([
    sys.executable, '-m', 'http.server', '8092'
], cwd=os.path.abspath('.'))

time.sleep(1.5)

temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9896

chrome_proc = subprocess.Popen([
    chrome,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}',
    f'--remote-debugging-port={port}',
    '--window-size=1200,900',
    'http://localhost:8092/index.html'
])

try:
    time.sleep(2.5)
    resp = urllib.request.urlopen(f'http://localhost:{port}/json/list')
    tabs = json.loads(resp.read().decode('utf-8'))
    target_tab = [t for t in tabs if 'localhost:8092' in t.get('url', '')][0]
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

    print("\n--- TEST 1: Select Language & Verify Journey Cards with Curriculum Chips ---")
    evaluate("document.getElementById('selectUrduBtn').click();")
    time.sleep(0.5)

    u4_chips = evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b1_u4\"]');
            if (!card) return null;
            const chips = Array.from(card.querySelectorAll('.unit-curr-chip')).map(c => c.textContent.trim());
            return {
                title: card.querySelector('.unit-card-title').textContent.trim(),
                chips: chips
            };
        })()
    """)
    print("Book 1 Unit 4 Card:", u4_chips)
    assert len(u4_chips['chips']) >= 2, "Unit 4 chips should include tamreens, qaidas, and questions!"
    capture_screenshot("scratch/test_journey_chips.png")

    print("\n--- TEST 2: Open Tamreen Selector for Book 1 Unit 4 & Verify Textbook Flow ---")
    evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b1_u4\"]');
            card.querySelector('.unit-ex-btn').click();
        })()
    """)
    time.sleep(0.6)

    flow_items = evaluate("""
        (() => {
            const items = Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card'));
            return items.map(it => ({
                isAll: it.classList.contains('all-tamreens'),
                isNas: it.classList.contains('is-nasuddars'),
                isTam: it.classList.contains('is-tamreen'),
                isQai: it.classList.contains('is-qaida'),
                title: it.querySelector('.tamreen-opt-title') ? it.querySelector('.tamreen-opt-title').textContent.trim() : '',
                meta: it.querySelector('.tamreen-opt-meta') ? it.querySelector('.tamreen-opt-meta').textContent.trim() : ''
            }));
        })()
    """)
    print(f"Rendered Flow Items in Tamreen Selector: {len(flow_items)}")
    for idx, it in enumerate(flow_items):
        kind = 'ALL' if it['isAll'] else ('NAS' if it['isNas'] else ('QAIDA' if it['isQai'] else 'TAMREEN'))
        print(f"  [{idx}] {kind}: {it['title']} | {it['meta']}")

    assert len(flow_items) == 12, f"Expected 1 all + 11 flow items = 12, got {len(flow_items)}"
    capture_screenshot("scratch/test_b1_u4_flow_selector.png")

    print("\n--- TEST 3: Click Qaida Item in Flow & Verify Standalone Qaida Modal ---")
    evaluate("""
        (() => {
            const qCard = document.querySelector('#tamreenOptionsList .is-qaida');
            qCard.click();
        })()
    """)
    time.sleep(0.5)

    qaida_modal_info = evaluate("""
        (() => {
            const modal = document.getElementById('qaidaModal');
            const isVisible = !modal.classList.contains('hidden');
            const title = document.getElementById('qaidaModalTitle').textContent.trim();
            const examples = Array.from(modal.querySelectorAll('.qaida-example-card')).map(e => ({
                ar: e.querySelector('.qaida-example-ar').textContent.trim(),
                trans: e.querySelector('.qaida-example-trans').textContent.trim()
            }));
            return { isVisible, title, examplesCount: examples.length, examples: examples.slice(0, 3) };
        })()
    """)
    print("Qaida Modal Info:", qaida_modal_info)
    assert qaida_modal_info['isVisible'], "Qaida modal must be visible!"
    assert qaida_modal_info['examplesCount'] > 0, "Qaida modal must render examples!"
    capture_screenshot("scratch/test_qaida_modal.png")

    # Close Qaida Modal
    evaluate("document.getElementById('closeQaidaModalBtn').click();")
    time.sleep(0.4)

    print("\n--- TEST 4: Start Full Lesson Quiz & Verify In-Quiz Qaida Intermission Card ---")
    evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b1_u4\"]');
            card.querySelector('.unit-ex-btn').click();
        })()
    """)
    time.sleep(0.4)

    # Click "جَمِيعُ الدَّرْسِ"
    evaluate("""
        (() => {
            const allBtn = document.querySelector('#tamreenOptionsList .all-tamreens');
            allBtn.click();
        })()
    """)
    time.sleep(0.6)

    # If first item is nasuddars, lesson reader modal opens. Click start exercises button to proceed into quiz
    is_reader_open = evaluate("!document.getElementById('lessonReaderModal').classList.contains('hidden')")
    if is_reader_open:
        print("Nasuddars reader opened! Clicking 'Start Exercises' button...")
        evaluate("document.getElementById('readerCloseBtn').click(); window.app.startQuiz(window.MADINAH_BOOKS.books[0].units[3], null);")
        time.sleep(0.6)

    quiz_info_q1 = evaluate("""
        (() => {
            const qz = window.app.quiz;
            return {
                open: !document.getElementById('quizOverlay').classList.contains('hidden'),
                index: qz ? qz.index : -1,
                total: qz ? qz.questions.length : -1,
                tamreenNum: qz && qz.questions[qz.index] ? qz.questions[qz.index].tamreen_num : -1,
                prompt: document.querySelector('.q-prompt-big-text') ? document.querySelector('.q-prompt-big-text').textContent.trim() : ''
            };
        })()
    """)
    print("Quiz Q1 Info:", quiz_info_q1)
    assert quiz_info_q1['open'], "Quiz must be open!"
    assert quiz_info_q1['total'] == 75, f"Book 1 Unit 4 must have 75 questions, got {quiz_info_q1['total']}"

    # Now jump quiz.index to index 34 (the start of Tamreen 4, right after Tamreen 3 where Qaida occurs)
    print("\n--- Advancing quiz to Tamreen 4 transition to test In-Quiz Qaida Intermission ---")
    evaluate("""
        (() => {
            window.app.quiz.index = 34; // Tamreen 4 Q1
            window.app.renderCurrentQuizQuestion();
        })()
    """)
    time.sleep(0.5)

    in_quiz_qaida_info = evaluate("""
        (() => {
            const card = document.querySelector('.in-quiz-qaida-card');
            const checkBtn = document.getElementById('quizCheckBtn');
            return {
                hasInQuizQaidaCard: Boolean(card),
                title: card ? card.querySelector('.in-quiz-qaida-title').textContent.trim() : '',
                btnText: checkBtn ? checkBtn.textContent.trim() : '',
                currentPendingKey: window.app.quiz.currentPendingQaidaKey
            };
        })()
    """)
    print("In-Quiz Qaida Card:", in_quiz_qaida_info)
    assert in_quiz_qaida_info['hasInQuizQaidaCard'], "In-quiz Qaida intermission card MUST render before Tamreen 4!"
    assert "آمِنَةُ" in in_quiz_qaida_info['title'] or "مُحَمَّدٌ" in in_quiz_qaida_info['title'], f"Expected Muhammad/Aminah rule title, got {in_quiz_qaida_info['title']}"
    capture_screenshot("scratch/test_in_quiz_qaida.png")

    # Click the "فَہِمْتُ (جاری رکھیں)" button
    print("Clicking 'فَہِمْتُ' button to advance from Qaida intermission into Tamreen 4 question...")
    evaluate("document.getElementById('quizCheckBtn').click();")
    time.sleep(0.5)

    after_qaida_info = evaluate("""
        (() => {
            const card = document.querySelector('.in-quiz-qaida-card');
            const q = window.app.quiz.questions[window.app.quiz.index];
            return {
                hasInQuizQaidaCard: Boolean(card),
                tamreenNum: q ? q.tamreen_num : -1,
                prompt: document.querySelector('.q-prompt-big-text') ? document.querySelector('.q-prompt-big-text').textContent.trim() : '',
                index: window.app.quiz.index
            };
        })()
    """)
    print("After Qaida Continuation:", after_qaida_info)
    assert not after_qaida_info['hasInQuizQaidaCard'], "Qaida intermission card should disappear after clicking continue!"
    assert after_qaida_info['tamreenNum'] == 4, f"Should be in Tamreen 4, got {after_qaida_info['tamreenNum']}"

    # Close quiz
    evaluate("window.app.closeQuiz();")
    time.sleep(0.4)

    print("\n--- TEST 5: Verify Book 1 Unit 5 Flow (Tamreens 1-9 & 2 Qaidas) ---")
    evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b1_u5\"]');
            card.querySelector('.unit-ex-btn').click();
        })()
    """)
    time.sleep(0.5)

    u5_flow = evaluate("""
        (() => {
            const items = Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card'));
            return items.map(it => ({
                isQaida: it.classList.contains('is-qaida'),
                isTamreen: it.classList.contains('is-tamreen'),
                title: it.querySelector('.tamreen-opt-title') ? it.querySelector('.tamreen-opt-title').textContent.trim() : ''
            }));
        })()
    """)
    print(f"Book 1 Unit 5 Flow items: {len(u5_flow)}")
    qaida_titles = [it['title'] for it in u5_flow if it['isQaida']]
    print("Unit 5 Qaidas in Flow:", qaida_titles)
    assert len(u5_flow) == 13, f"Expected 1 all + 12 flow items = 13, got {len(u5_flow)}"
    assert len(qaida_titles) == 2, f"Expected 2 Qaidas (Yaa-Nida & Ismun/Ibnun), got {len(qaida_titles)}"
    capture_screenshot("scratch/test_b1_u5_flow_selector.png")

    evaluate("document.getElementById('closeTamreenSelectorBtn').click();")
    time.sleep(0.4)

    print("\n--- TEST 6: Verify Book 3 Unit 9 Unabridged 93 Questions ---")
    evaluate("document.querySelector('[data-book=\"3\"]').click();")
    time.sleep(0.5)

    u9_info = evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b3_u9\"]');
            if (!card) return null;
            const chips = Array.from(card.querySelectorAll('.unit-curr-chip')).map(c => c.textContent.trim());
            return {
                title: card.querySelector('.unit-card-title').textContent.trim(),
                chips: chips
            };
        })()
    """)
    print("Book 3 Unit 9 Card:", u9_info)
    assert any("93" in c for c in u9_info['chips']), f"Book 3 Unit 9 must show 93 questions in chips: {u9_info['chips']}"

    print("\n=======================================================")
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
    print("=======================================================")

finally:
    chrome_proc.kill()
    server_proc.kill()
