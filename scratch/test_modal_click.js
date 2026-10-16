const { spawn } = require('child_process');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function run() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9232',
    'http://localhost:8080/index.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));

  try {
    const listRes = await fetch('http://localhost:9232/json/list');
    const tabs = await listRes.json();
    console.log('Available tabs:', tabs.map(t => ({ id: t.id, url: t.url, title: t.title })));
    const targetTab = tabs.find(t => t.url.includes('localhost:8080')) || tabs[0];
    console.log('Target tab URL:', targetTab.url);
    const ws = new WebSocket(targetTab.webSocketDebuggerUrl);
    await new Promise(r => ws.onopen = r);

    let id = 1;
    function send(method, params = {}) {
      return new Promise(resolve => {
        const reqId = id++;
        const handler = (evt) => {
          const data = JSON.parse(evt.data);
          if (data.id === reqId) {
            ws.removeEventListener('message', handler);
            resolve(data.result);
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id: reqId, method, params }));
      });
    }

    await send('Runtime.enable');
    await send('Page.enable');
    await new Promise(r => setTimeout(r, 1000));

    // Dismiss splash
    await send('Runtime.evaluate', { expression: `document.getElementById('selectBothBtn').click();` });
    await new Promise(r => setTimeout(r, 1000));

    // Check if unit cards exist
    const res1 = await send('Runtime.evaluate', {
      expression: `(() => {
        const btns = document.querySelectorAll('.unit-ex-btn');
        const cards = document.querySelectorAll('.journey-unit-card, .unit-card');
        const grid = document.getElementById('journeyUnitsGrid');
        return {
          btnsCount: btns.length,
          cardsCount: cards.length,
          gridChildren: grid ? grid.children.length : null,
          bodyHtmlSlice: document.body.innerHTML.slice(0, 300)
        };
      })()`,
      returnByValue: true
    });
    console.log('DOM check:', res1.result.value);

    // Click first button
    const res2 = await send('Runtime.evaluate', {
      expression: `(() => {
        const btn = document.querySelector('.journey-unit-card .unit-ex-btn');
        if (btn) {
          btn.click();
          const modal = document.getElementById('tamreenSelectorModal');
          const isHidden = modal.classList.contains('hidden');
          const optionsCount = document.querySelectorAll('.tamreen-opt-card').length;
          return { isHidden, optionsCount };
        }
        return 'no btn';
      })()`,
      returnByValue: true
    });
    console.log('After clicking unit-ex-btn:', res2.result.value);

    ws.close();
  } finally {
    chrome.kill();
    process.exit(0);
  }
}

run();
