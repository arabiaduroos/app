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

server.listen(8095, async () => {
  const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--incognito',
    '--remote-debugging-port=9225',
    '--disable-cache',
    '--user-data-dir=' + path.join(process.cwd(), 'scratch/chrome_fresh_' + Date.now())
  ]);

  await new Promise(r => setTimeout(r, 1200));

  const listRes = await fetch('http://127.0.0.1:9225/json');
  const tabs = await listRes.json();
  const wsUrl = tabs[0].webSocketDebuggerUrl;

  const ws = new WebSocket(wsUrl);
  let msgId = 1;
  const pending = new Map();

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pending.has(msg.id)) {
      pending.get(msg.id)(msg);
      pending.delete(msg.id);
    }
  };

  function send(method, params = {}) {
    return new Promise(resolve => {
      const id = msgId++;
      pending.set(id, resolve);
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  if (ws.readyState !== 1) {
    await new Promise(r => { ws.onopen = r; });
  }
  await send('Page.enable');
  await send('DOM.enable');
  await send('Network.enable');
  await send('Network.setCacheDisabled', { cacheDisabled: true });

  // Test 1: Unit 2 Card 13 (Urdu, Desktop 1366x768)
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1366,
    height: 768,
    deviceScaleFactor: 1,
    mobile: false
  });
  await send('Page.navigate', { url: 'http://localhost:8095/?book=1&unit=b1_u2&card=13&lang=ur' });
  await new Promise(r => setTimeout(r, 2000));

  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/Person/.gemini/antigravity/brain/548db058-a481-48f4-9024-0b3a7fd2647c/vocab_u2_c13_ur_centered.png', Buffer.from(shot1.result.data, 'base64'));
  console.log('Saved vocab_u2_c13_ur_centered.png');

  // Test 2: Unit 2 Card 13 (English, Desktop 1366x768)
  await send('Page.navigate', { url: 'http://localhost:8095/?book=1&unit=b1_u2&card=13&lang=en' });
  await new Promise(r => setTimeout(r, 1500));

  const shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/Person/.gemini/antigravity/brain/548db058-a481-48f4-9024-0b3a7fd2647c/vocab_u2_c13_en_centered.png', Buffer.from(shot2.result.data, 'base64'));
  console.log('Saved vocab_u2_c13_en_centered.png');

  // Test 3: Unit 2 Card 13 (Mobile 412x850)
  await send('Emulation.setDeviceMetricsOverride', {
    width: 412,
    height: 850,
    deviceScaleFactor: 2,
    mobile: true
  });
  await send('Page.navigate', { url: 'http://localhost:8095/?book=1&unit=b1_u2&card=13&lang=ur' });
  await new Promise(r => setTimeout(r, 1500));

  const shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/Person/.gemini/antigravity/brain/548db058-a481-48f4-9024-0b3a7fd2647c/vocab_u2_c13_mobile.png', Buffer.from(shot3.result.data, 'base64'));
  console.log('Saved vocab_u2_c13_mobile.png');

  // Test 4: Unit 3 Card 35 (Part 1, 12 words) Desktop
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1366,
    height: 768,
    deviceScaleFactor: 1,
    mobile: false
  });
  await send('Page.navigate', { url: 'http://localhost:8095/?book=1&unit=b1_u3&card=35&lang=ur' });
  await new Promise(r => setTimeout(r, 1500));

  const shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/Person/.gemini/antigravity/brain/548db058-a481-48f4-9024-0b3a7fd2647c/vocab_u3_c35_desktop.png', Buffer.from(shot4.result.data, 'base64'));
  console.log('Saved vocab_u3_c35_desktop.png');

  // Check metrics
  const evalRes = await send('Runtime.evaluate', {
    expression: `(() => {
      const stage = document.getElementById('lessonStage');
      const card = document.getElementById('lessonPageCard');
      const body = document.body;
      return {
        bodyScrollHeight: body.scrollHeight,
        bodyClientHeight: body.clientHeight,
        bodyOverflow: getComputedStyle(body).overflow,
        stageOverflow: getComputedStyle(stage).overflow,
        stageJustify: getComputedStyle(stage).justifyContent,
        hasEmojis: !!card.querySelector('.vocab-tile-em'),
        hasSpeakers: !!card.querySelector('.vocab-tile-speaker'),
        soundHint: card.querySelector('.vocab-sound-hint') ? card.querySelector('.vocab-sound-hint').textContent : null,
        tilesCount: card.querySelectorAll('.vocab-word-tile').length
      };
    })()`,
    returnByValue: true
  });
  console.log('Final Metrics:', JSON.stringify(evalRes, null, 2));

  chrome.kill();
  server.close();
  process.exit(0);
});
