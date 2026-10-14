const { spawn } = require('child_process');
const fs = require('fs');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function testWithWindowSize(width, height, shotName) {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    `--window-size=${width},${height}`,
    '--remote-debugging-port=9232',
    'http://localhost:8080/index.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));

  try {
    const listRes = await fetch('http://localhost:9232/json/list');
    const tabs = await listRes.json();
    const targetTab = tabs.find(t => t.url.includes('localhost:8080')) || tabs[0];
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

    // Click EN + UR
    await send('Runtime.evaluate', { expression: "document.getElementById('selectBothBtn').click()" });
    await new Promise(r => setTimeout(r, 600));

    // Switch to Book 2
    await send('Runtime.evaluate', { expression: "document.querySelector('.book-pill[data-book=\"2\"]').click()" });
    await new Promise(r => setTimeout(r, 600));

    // Open Tamreens modal for Unit 26
    await send('Runtime.evaluate', { expression: "document.querySelectorAll('.journey-unit-card')[25].querySelector('.unit-ex-btn').click()" });
    await new Promise(r => setTimeout(r, 600));

    // Click Tamreen 1
    await send('Runtime.evaluate', { expression: "document.querySelectorAll('.tamreen-opt-card')[0].click()" });
    await new Promise(r => setTimeout(r, 600));

    // Capture screenshot
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`scratch/${shotName}`, Buffer.from(shot.data, 'base64'));
    console.log(`Saved scratch/${shotName}`);

    const layout = await send('Runtime.evaluate', {
      expression: `(() => {
        const stage = document.getElementById('quizStage');
        const sRect = stage.getBoundingClientRect();
        const card = document.querySelector('.q-prompt-card')?.getBoundingClientRect();
        const grid = document.querySelector('.q-options-grid')?.getBoundingClientRect();
        const bar = document.getElementById('quizBottomBar')?.getBoundingClientRect();
        return {
          viewportWidth: window.innerWidth,
          viewportHeight: window.innerHeight,
          stageTop: Math.round(sRect.top),
          stageBottom: Math.round(sRect.bottom),
          stageHeight: Math.round(sRect.height),
          cardTop: card ? Math.round(card.top) : null,
          gridBottom: grid ? Math.round(grid.bottom) : null,
          bottomBarTop: bar ? Math.round(bar.top) : null,
          spaceAboveCard: card ? Math.round(card.top - sRect.top) : null,
          spaceBelowGrid: (grid && bar) ? Math.round(bar.top - grid.bottom) : null
        };
      })()`,
      returnByValue: true
    });
    console.log(`Layout for ${width}x${height}:`, layout.result.value);

    ws.close();
  } finally {
    chrome.kill();
  }
}

async function main() {
  await testWithWindowSize(1280, 800, 'quiz_desktop_1280x800.png');
  await new Promise(r => setTimeout(r, 1000));
  await testWithWindowSize(390, 844, 'quiz_mobile_390x844.png');
}

main().catch(console.error);
