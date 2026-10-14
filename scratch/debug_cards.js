const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function main() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9224',
    '--window-size=1024,768',
    'about:blank'
  ]);
  await new Promise(r => setTimeout(r, 1500));
  try {
    const listRes = await fetch('http://localhost:9224/json/list');
    const tabs = await listRes.json();
    const tab = tabs.find(t => t.type === 'page') || tabs[0];
    const ws = new WebSocket(tab.webSocketDebuggerUrl);
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

    await send('Page.enable');
    await send('Runtime.enable');
    await send('Page.navigate', { url: 'http://localhost:8080/index.html' });
    await new Promise(r => setTimeout(r, 2000));

    // Click EN+UR
    await send('Runtime.evaluate', { expression: "document.getElementById('selectBothBtn').click()" });
    await new Promise(r => setTimeout(r, 600));

    // Click Book 2 pill
    await send('Runtime.evaluate', { expression: "document.querySelector('.book-pill[data-book=\"2\"]').click()" });
    await new Promise(r => setTimeout(r, 1000));

    const info = await send('Runtime.evaluate', {
      expression: `(() => {
        const cards = document.querySelectorAll('.journey-unit-card');
        return {
          totalCards: cards.length,
          cardTitles: Array.from(cards).slice(0, 5).map(c => c.querySelector('.unit-banner-title')?.innerText),
          c25: cards[25]?.querySelector('.unit-banner-title')?.innerText,
          c25ExBtn: !!cards[25]?.querySelector('.unit-ex-btn')
        };
      })()`,
      returnByValue: true
    });
    console.log("Card Info:", JSON.stringify(info.result.value, null, 2));

    ws.close();
  } finally {
    chrome.kill();
  }
}
main().catch(console.error);
