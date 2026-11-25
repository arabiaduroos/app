import http from 'http';
import fs from 'fs';
import path from 'path';
import { spawn } from 'child_process';

const server = http.createServer((req, res) => {
  let file = req.url.split('?')[0].replace(/^\//, '') || 'index.html';
  let filePath = path.join(process.cwd(), file);
  if (!fs.existsSync(filePath)) { res.writeHead(404); res.end('Not found'); return; }
  let ext = path.extname(filePath);
  let mime = ext === '.html' ? 'text/html' : ext === '.js' ? 'application/javascript' : ext === '.css' ? 'text/css' : ext === '.mp3' ? 'audio/mpeg' : 'application/octet-stream';
  res.writeHead(200, { 'Content-Type': mime, 'Access-Control-Allow-Origin': '*' });
  fs.createReadStream(filePath).pipe(res);
});

server.listen(8090, async () => {
  console.log('Server running on 8090');
  const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--remote-debugging-port=9223',
    '--user-data-dir=' + path.join(process.cwd(), 'scratch/chrome_quiz_test')
  ]);

  await new Promise(r => setTimeout(r, 1200));

  const listRes = await fetch('http://127.0.0.1:9223/json');
  const tabs = await listRes.json();
  const wsUrl = tabs[0].webSocketDebuggerUrl;

  const ws = new WebSocket(wsUrl);
  let id = 1;
  const pending = new Map();
  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (pending.has(data.id)) {
      const cb = pending.get(data.id);
      pending.delete(data.id);
      cb(data.result);
    }
  };

  const send = (method, params = {}) => new Promise((resolve) => {
    const curId = id++;
    pending.set(curId, resolve);
    ws.send(JSON.stringify({ id: curId, method, params }));
  });

  ws.onopen = async () => {
    console.log('CDP connected');
    await send('Page.enable');
    await send('Page.navigate', { url: 'http://127.0.0.1:8090/index.html' });
    await new Promise(r => setTimeout(r, 1500));

    // Dismiss splash overlay by selecting English
    await send('Runtime.evaluate', {
      expression: `(function() {
        const btn = document.getElementById('selectEnglishBtn');
        if (btn) btn.click();
        const splash = document.getElementById('splashOverlay');
        if (splash) splash.remove();
      })()`
    });
    await new Promise(r => setTimeout(r, 600));

    // Open Unit 3 Tamreen 1
    const testResult = await send('Runtime.evaluate', {
      expression: `(function() {
        if (!window.app || !window.app.DATA) return { error: 'window.app not ready' };
        const u3 = window.app.DATA.books[0].units.find(u => u.id === 'b1_u3');
        if (!u3) return { error: 'b1_u3 not found' };
        
        // Start quiz for unit 3 tamreen 1
        window.app.startQuiz(u3, 1);
        
        const promptCard = document.querySelector('.q-prompt-card');
        const hintEl = document.querySelector('.q-prompt-hint');
        const promptText = document.querySelector('.q-prompt-big-text');
        const instruction = document.querySelector('.q-instruction');
        
        return {
          opened: true,
          instructionText: instruction ? instruction.textContent : null,
          promptBigText: promptText ? promptText.textContent : null,
          hasHintElement: Boolean(hintEl),
          hintContent: hintEl ? hintEl.textContent : null,
          promptCardHtml: promptCard ? promptCard.innerHTML : null
        };
      })()`,
      returnByValue: true
    });

    console.log('Test evaluation result:', JSON.stringify(testResult, null, 2));

    await send('Emulation.setDeviceMetricsOverride', {
      width: 1024,
      height: 600,
      deviceScaleFactor: 1,
      mobile: false
    });
    await new Promise(r => setTimeout(r, 400));

    // 1. Screenshot of clean prompt card (NO SPOILER)
    const shot1 = await send('Page.captureScreenshot', { format: 'png' });
    const shot1Path = path.join('C:\\Users\\Person\\.gemini\\antigravity\\brain\\548db058-a481-48f4-9024-0b3a7fd2647c', 'quiz_no_spoiler_verified.png');
    fs.writeFileSync(shot1Path, Buffer.from(shot1.data, 'base64'));
    console.log('Saved no-spoiler screenshot to:', shot1Path);

    // 2. Select answer 'ثَقِيلٌ' and click Check to verify post-answer explanation drawer
    const checkResult = await send('Runtime.evaluate', {
      expression: `(function() {
        const optionBtns = Array.from(document.querySelectorAll('.q-option-btn'));
        const targetBtn = optionBtns.find(b => b.textContent.includes('ثَقِيلٌ')) || optionBtns[0];
        targetBtn.click();
        
        document.getElementById('quizCheckBtn').click();
        
        const feedbackTitle = document.getElementById('feedbackTitle');
        const feedbackSub = document.getElementById('feedbackSub');
        const explText = document.querySelector('.feedback-expl-text');
        
        return {
          checked: true,
          feedbackTitle: feedbackTitle ? feedbackTitle.textContent : null,
          feedbackSub: feedbackSub ? feedbackSub.textContent : null,
          explanationText: explText ? explText.textContent : null
        };
      })()`,
      returnByValue: true
    });
    console.log('Check evaluation result:', JSON.stringify(checkResult, null, 2));

    await new Promise(r => setTimeout(r, 400));
    // 3. Screenshot of post-check feedback drawer with explanation
    const shot2 = await send('Page.captureScreenshot', { format: 'png' });
    const shot2Path = path.join('C:\\Users\\Person\\.gemini\\antigravity\\brain\\548db058-a481-48f4-9024-0b3a7fd2647c', 'quiz_feedback_drawer_verified.png');
    fs.writeFileSync(shot2Path, Buffer.from(shot2.data, 'base64'));
    console.log('Saved feedback drawer screenshot to:', shot2Path);

    chrome.kill();
    server.close();
    process.exit(0);
  };
});
