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

server.listen(8094, async () => {
  const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--remote-debugging-port=9226',
    '--user-data-dir=' + path.join(process.cwd(), 'scratch/chrome_u3_test')
  ]);

  await new Promise(r => setTimeout(r, 1200));
  const listRes = await fetch('http://127.0.0.1:9226/json');
  const tabs = await listRes.json();
  const ws = new WebSocket(tabs[0].webSocketDebuggerUrl);

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
    await send('Page.enable');
    await send('Page.navigate', { url: 'http://127.0.0.1:8094/index.html' });
    await new Promise(r => setTimeout(r, 1500));

    await send('Runtime.evaluate', {
      expression: `(function() {
        const btn = document.getElementById('selectEnglishBtn');
        if (btn) btn.click();
        const splash = document.getElementById('splashOverlay');
        if (splash) splash.remove();
      })()`
    });
    await new Promise(r => setTimeout(r, 500));

    // Open Unit 3 vocab card
    const res = await send('Runtime.evaluate', {
      expression: `(function() {
        const u3 = window.app.DATA.books[0].units.find(u => u.id === 'b1_u3');
        window.app.openLessonCardReader(u3);
        const vocabIdx = window.app.lessonReader.cards.findIndex(c => c.id && String(c.id).includes('vocab'));
        const targetIdx = vocabIdx !== -1 ? vocabIdx : window.app.lessonReader.cards.length - 2;
        window.app.lessonReader.index = targetIdx;
        window.app.renderCurrentLessonCard();
        return {
          title: window.app.lessonReader.cards[targetIdx].title_en,
          wordsCount: (window.app.lessonReader.cards[targetIdx].words || []).length
        };
      })()`,
      returnByValue: true
    });
    console.log('Unit 3 Vocab Card:', res.result.value);

    await send('Emulation.setDeviceMetricsOverride', { width: 1024, height: 600, deviceScaleFactor: 1, mobile: false });
    await new Promise(r => setTimeout(r, 400));
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    const p = path.join('C:\\Users\\Person\\.gemini\\antigravity\\brain\\548db058-a481-48f4-9024-0b3a7fd2647c', 'unit3_vocab_part1_verified.png');
    fs.writeFileSync(p, Buffer.from(shot.data, 'base64'));
    console.log('Saved unit 3 vocab screenshot to:', p);

    chrome.kill();
    server.close();
    process.exit(0);
  };
});
