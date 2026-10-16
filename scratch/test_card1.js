const { spawn } = require('child_process');
const fs = require('fs');
const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless=new', '--disable-gpu', '--remote-debugging-port=9243', 'http://localhost:8080/index.html'
]);

setTimeout(async () => {
  const tabs = await (await fetch('http://localhost:9243/json/list')).json();
  const target = tabs.find(t => t.url.includes('localhost:8080')) || tabs[0];
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);
  let id = 1;
  const send = (m, p = {}) => new Promise(res => {
    const reqId = id++;
    const h = e => { const d = JSON.parse(e.data); if (d.id === reqId) { ws.removeEventListener('message', h); res(d.result); } };
    ws.addEventListener('message', h);
    ws.send(JSON.stringify({ id: reqId, method: m, params: p }));
  });
  await send('Emulation.setDeviceMetricsOverride', { width: 1280, height: 720, deviceScaleFactor: 1, mobile: false });
  await send('Runtime.evaluate', { expression: "document.getElementById('selectBothBtn').click();" });
  await new Promise(r => setTimeout(r, 600));
  await send('Runtime.evaluate', { expression: "document.querySelectorAll('.journey-unit-card .unit-read-btn')[2].click();" });
  await new Promise(r => setTimeout(r, 600));
  const metrics = await send('Runtime.evaluate', {
    expression: "(() => { const s = document.getElementById('lessonStage'); return { scrollHeight: s.scrollHeight, clientHeight: s.clientHeight, hasScrollbar: s.scrollHeight > s.clientHeight }; })()",
    returnByValue: true
  });
  console.log('Card 1 metrics:', metrics.result.value);
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/unit3_card1_after.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved scratch/unit3_card1_after.png');
  chrome.kill();
  process.exit(0);
}, 2000);
