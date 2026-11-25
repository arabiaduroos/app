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

server.listen(8092, async () => {
  console.log('Server running on 8092');
  const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--remote-debugging-port=9224',
    '--user-data-dir=' + path.join(process.cwd(), 'scratch/chrome_vocab_test')
  ]);

  await new Promise(r => setTimeout(r, 1200));

  const listRes = await fetch('http://127.0.0.1:9224/json');
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
    await send('Page.navigate', { url: 'http://127.0.0.1:8092/index.html' });
    await new Promise(r => setTimeout(r, 1500));

    // Dismiss splash overlay
    await send('Runtime.evaluate', {
      expression: `(function() {
        const btn = document.getElementById('selectEnglishBtn');
        if (btn) btn.click();
        const splash = document.getElementById('splashOverlay');
        if (splash) splash.remove();
      })()`
    });
    await new Promise(r => setTimeout(r, 600));

    // Navigate to Unit 2, Card 13 (the vocab card)
    const cardInfo = await send('Runtime.evaluate', {
      expression: `(function() {
        const u2 = window.app.DATA.books[0].units.find(u => u.id === 'b1_u2');
        if (!u2) return { error: 'b1_u2 not found' };
        
        window.app.openLessonCardReader(u2);
        
        // Go to card 13 (index 12)
        window.app.lessonReader.index = 12;
        window.app.renderCurrentLessonCard();
        
        const cardEl = document.getElementById('lessonCardStage') || document.querySelector('.lesson-page-card');
        const grid = document.querySelector('.vocab-words-grid');
        const tiles = document.querySelectorAll('.vocab-word-tile');
        
        return {
          cardCount: window.app.lessonReader.cards.length,
          currentIndex: window.app.lessonReader.index,
          gridClass: grid ? grid.className : null,
          tileCount: tiles.length,
          cardRect: cardEl ? {
            width: cardEl.offsetWidth,
            height: cardEl.offsetHeight
          } : null,
          firstTileRect: tiles[0] ? {
            width: tiles[0].offsetWidth,
            height: tiles[0].offsetHeight
          } : null
        };
      })()`,
      returnByValue: true
    });
    console.log('Unit 2 Card 13 render info:', JSON.stringify(cardInfo.result.value, null, 2));

    // 1. Desktop Screenshot (1024x600)
    await send('Emulation.setDeviceMetricsOverride', {
      width: 1024,
      height: 600,
      deviceScaleFactor: 1,
      mobile: false
    });
    await new Promise(r => setTimeout(r, 500));
    const shotDesktop = await send('Page.captureScreenshot', { format: 'png' });
    const shotDesktopPath = path.join('C:\\Users\\Person\\.gemini\\antigravity\\brain\\548db058-a481-48f4-9024-0b3a7fd2647c', 'unit2_card13_decent_medium_desktop.png');
    fs.writeFileSync(shotDesktopPath, Buffer.from(shotDesktop.data, 'base64'));
    console.log('Saved desktop screenshot to:', shotDesktopPath);

    // 2. Mobile Screenshot (390x844)
    await send('Emulation.setDeviceMetricsOverride', {
      width: 390,
      height: 844,
      deviceScaleFactor: 2,
      mobile: true
    });
    await new Promise(r => setTimeout(r, 500));
    const shotMobile = await send('Page.captureScreenshot', { format: 'png' });
    const shotMobilePath = path.join('C:\\Users\\Person\\.gemini\\antigravity\\brain\\548db058-a481-48f4-9024-0b3a7fd2647c', 'unit2_card13_responsive_mobile.png');
    fs.writeFileSync(shotMobilePath, Buffer.from(shotMobile.data, 'base64'));
    console.log('Saved mobile screenshot to:', shotMobilePath);

    chrome.kill();
    server.close();
    process.exit(0);
  };
});
