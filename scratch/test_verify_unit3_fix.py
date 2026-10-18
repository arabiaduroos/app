import subprocess, time, json, urllib.request, socket, base64, os, struct, tempfile, sys

sys.stdout.reconfigure(encoding='utf-8')

# Start Python HTTP server on port 8094
server_proc = subprocess.Popen([
    sys.executable, '-m', 'http.server', '8094'
], cwd=os.path.abspath('.'))

time.sleep(1.5)

temp_dir = tempfile.mkdtemp()
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
port = 9898

chrome_proc = subprocess.Popen([
    chrome,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}',
    f'--remote-debugging-port={port}',
    '--window-size=1200,900',
    'http://localhost:8094/index.html'
])

try:
    time.sleep(2.5)
    resp = urllib.request.urlopen(f'http://localhost:{port}/json/list')
    tabs = json.loads(resp.read().decode('utf-8'))
    target_tab = [t for t in tabs if 'localhost:8094' in t.get('url', '')][0]
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

    print("\n--- STEP 1: Select Language & Inspect Unit 3 Lesson Cards in Reader ---")
    evaluate("document.getElementById('selectUrduBtn').click();")
    time.sleep(0.5)

    # Click Read Lesson on Unit 3
    evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b1_u3\"]');
            card.querySelector('.unit-read-btn').click();
        })()
    """)
    time.sleep(0.6)

    reader_info = evaluate("""
        (() => {
            const counter = document.getElementById('readerCardCounter').textContent.trim();
            const bigText = document.querySelector('.lesson-card-ar') ? document.querySelector('.lesson-card-ar').textContent.trim() : '';
            const isVocabTable = Boolean(document.querySelector('.lesson-vocab-grid'));
            return { counter, bigText, isVocabTable };
        })()
    """)
    print("Lesson Reader Initial Card:", reader_info)

    # Inspect all cards in reader
    all_cards_info = evaluate("""
        (() => {
            const u3 = window.MADINAH_BOOKS.books[0].units[2];
            return {
                title: u3.title_ar,
                blocksCount: u3.blocks.length
            };
        })()
    """)
    print("Unit 3 Data Structure:", all_cards_info)

    # Walk through cards to check snippet and ensure NO exercise cards exist in reader
    cards_dump = evaluate("""
        (() => {
            const found = [];
            let maxSteps = 40;
            while (maxSteps-- > 0) {
                const counter = document.getElementById('readerCardCounter').textContent.trim();
                const cardAr = document.querySelector('.lesson-card-ar') ? document.querySelector('.lesson-card-ar').textContent.trim() : '';
                const title = document.querySelector('.lesson-card-meta-bar') ? document.querySelector('.lesson-card-meta-bar').textContent.trim() : '';
                const isGrid = Boolean(document.querySelector('.lesson-vocab-grid'));
                found.push({ counter, cardAr: cardAr.substring(0, 40), title, isGrid });
                
                const nextBtn = document.getElementById('lessonNextBtn');
                if (nextBtn.disabled || nextBtn.classList.contains('hidden')) break;
                nextBtn.click();
            }
            return found;
        })()
    """)
    print(f"\nTotal Lesson Cards Walked: {len(cards_dump)}")
    for c in cards_dump:
        print(f"  {c['counter']} | grid={c['isGrid']} | {c['cardAr']}")

    # Assertions: No exercise leaks in cards
    for c in cards_dump:
        ar = c['cardAr']
        assert "املأ الفراغ" not in ar, f"Exercise leaked in reader: {ar}"
        assert "اختر كلمة" not in ar, f"Exercise leaked in reader: {ar}"
        assert "اقرأ واكتب" not in ar, f"Exercise leaked in reader: {ar}"
        assert "..." not in ar and "…" not in ar, f"Fill blank dots leaked in reader: {ar}"

    capture_screenshot("scratch/test_u3_reader_clean.png")

    # Close reader
    evaluate("document.getElementById('readerCloseBtn').click();")
    time.sleep(0.4)

    print("\n--- STEP 2: Open Tamreen Selector for Unit 3 & Verify Exercises ---")
    evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b1_u3\"]');
            card.querySelector('.unit-ex-btn').click();
        })()
    """)
    time.sleep(0.5)

    u3_flow = evaluate("""
        (() => {
            const items = Array.from(document.querySelectorAll('#tamreenOptionsList .tamreen-opt-card'));
            return items.map(it => ({
                isAll: it.classList.contains('all-tamreens'),
                isQaida: it.classList.contains('is-qaida'),
                isTamreen: it.classList.contains('is-tamreen'),
                title: it.querySelector('.tamreen-opt-title') ? it.querySelector('.tamreen-opt-title').textContent.trim() : '',
                meta: it.querySelector('.tamreen-opt-meta') ? it.querySelector('.tamreen-opt-meta').textContent.trim() : ''
            }));
        })()
    """)
    print(f"Rendered Flow Items in Unit 3: {len(u3_flow)}")
    for idx, it in enumerate(u3_flow):
        print(f"  [{idx}] {it['title']} | {it['meta']}")

    assert len(u3_flow) == 12, f"Expected 1 all + 11 items = 12, got {len(u3_flow)}"
    capture_screenshot("scratch/test_u3_flow_selector.png")

    print("\n--- STEP 3: Start Tamreen 6 (Part B Exercise 2: Fill in blanks with options) ---")
    # Click Tamreen 6 card
    evaluate("""
        (() => {
            const cards = Array.from(document.querySelectorAll('#tamreenOptionsList .is-tamreen'));
            // Tamreen 6 is the 6th tamreen item (index 5 of tamreens)
            const t6Card = cards.find(c => c.textContent.includes('تَمْرِين (٢ — ب)'));
            if (t6Card) t6Card.click();
        })()
    """)
    time.sleep(0.6)

    q_t6_info = evaluate("""
        (() => {
            const open = !document.getElementById('quizOverlay').classList.contains('hidden');
            const prompt = document.querySelector('.q-prompt-big-text') ? document.querySelector('.q-prompt-big-text').textContent.trim() : '';
            const opts = Array.from(document.querySelectorAll('.q-option-btn span:first-child')).map(s => s.textContent.trim());
            const tamreenNum = window.app.quiz.questions[window.app.quiz.index].tamreen_num;
            return { open, prompt, opts, tamreenNum, total: window.app.quiz.questions.length };
        })()
    """)
    print("Tamreen 6 (Fill-in-the-blank with options):", q_t6_info)
    assert q_t6_info['open'], "Quiz overlay must be open!"
    assert q_t6_info['tamreenNum'] == 6, f"Expected Tamreen 6, got {q_t6_info['tamreenNum']}"
    assert "غَنِيٌّ" in q_t6_info['prompt'], f"Expected غَنِيٌّ in prompt, got {q_t6_info['prompt']}"
    assert len(q_t6_info['opts']) == 4, f"Expected 4 multiple-choice options, got {len(q_t6_info['opts'])}"
    assert "التَّاجِرُ" in q_t6_info['opts'], f"Expected التَّاجِرُ in options: {q_t6_info['opts']}"
    capture_screenshot("scratch/test_u3_t6_fill_blank_options.png")

    # Select correct option and check
    print("Selecting correct option 'التَّاجِرُ' and checking answer...")
    evaluate("""
        (() => {
            const optBtn = Array.from(document.querySelectorAll('.q-option-btn')).find(b => b.textContent.includes('التَّاجِرُ'));
            optBtn.click();
            document.getElementById('quizCheckBtn').click();
        })()
    """)
    time.sleep(0.5)

    feedback_info = evaluate("""
        (() => {
            const title = document.getElementById('feedbackTitle').textContent.trim();
            const sub = document.getElementById('feedbackSub').textContent.trim();
            return { title, sub };
        })()
    """)
    print("Feedback after answering:", feedback_info)
    assert "درست" in feedback_info['title'] or "ماشاءاللہ" in feedback_info['title'] or "Awesome" in feedback_info['title'], f"Answer must be recognized as correct: {feedback_info}"

    # Close quiz
    evaluate("window.app.closeQuiz();")
    time.sleep(0.4)

    print("\n--- STEP 4: Start Tamreen 7 (Part B Exercise 3: Column matching / pair_match) ---")
    evaluate("""
        (() => {
            const card = document.querySelector('[data-unit-id=\"b1_u3\"]');
            card.querySelector('.unit-ex-btn').click();
        })()
    """)
    time.sleep(0.4)

    evaluate("""
        (() => {
            const cards = Array.from(document.querySelectorAll('#tamreenOptionsList .is-tamreen'));
            const t7Card = cards.find(c => c.textContent.includes('تَمْرِين (٣ — ب)'));
            if (t7Card) t7Card.click();
        })()
    """)
    time.sleep(0.6)

    pair_info = evaluate("""
        (() => {
            const isPairMatch = Boolean(document.querySelector('.pairs-columns'));
            const leftCol = Array.from(document.querySelectorAll('.pairs-col:first-child .pair-tile')).map(b => b.textContent.trim());
            const rightCol = Array.from(document.querySelectorAll('.pairs-col:last-child .pair-tile')).map(b => b.textContent.trim());
            return { isPairMatch, leftCol, rightCol };
        })()
    """)
    print("Tamreen 7 (Pair Match UI):", pair_info)
    assert pair_info['isPairMatch'], "Tamreen 7 must render interactive Duolingo pair match!"
    assert len(pair_info['leftCol']) == 6, f"Expected 6 words in Column A, got {len(pair_info['leftCol'])}"
    assert len(pair_info['rightCol']) == 6, f"Expected 6 words in Column B, got {len(pair_info['rightCol'])}"
    capture_screenshot("scratch/test_u3_t7_pair_match.png")

    # Close quiz
    evaluate("window.app.closeQuiz();")
    time.sleep(0.4)

    print("\n=======================================================")
    print("ALL UNIT 3 VERIFICATION TESTS PASSED WITH 100% SUCCESS!")
    print("=======================================================")

finally:
    chrome_proc.kill()
    server_proc.kill()
