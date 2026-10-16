const { spawn } = require('child_process');
const fs = require('fs');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function run() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9240',
    'http://localhost:8080/index.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));

  try {
    const listRes = await fetch('http://localhost:9240/json/list');
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
    // Set standard laptop viewport (1280 x 720)
    await send('Emulation.setDeviceMetricsOverride', {
      width: 1280,
      height: 720,
      deviceScaleFactor: 1,
      mobile: false
    });

    await new Promise(r => setTimeout(r, 1000));

    // Dismiss splash
    await send('Runtime.evaluate', { expression: `document.getElementById('selectBothBtn').click();` });
    await new Promise(r => setTimeout(r, 800));

    // Open Book 1 Unit 3 Reader
    const openRes = await send('Runtime.evaluate', {
      expression: `(() => {
        // Unit 3 is the 3rd unit card
        const readBtns = document.querySelectorAll('.journey-unit-card .unit-read-btn');
        if (readBtns[2]) {
          readBtns[2].click();
          return true;
        }
        return false;
      })()`,
      returnByValue: true
    });
    console.log('Opened Unit 3 reader:', openRes.result.value);
    await new Promise(r => setTimeout(r, 500));

    // Advance to Card 15 (click Next 14 times)
    const cardRes = await send('Runtime.evaluate', {
      expression: `(() => {
        const nextBtn = document.getElementById('lessonNextBtn');
        for (let i = 0; i < 14; i++) {
          if (nextBtn) nextBtn.click();
        }
        const stage = document.getElementById('lessonStage');
        const card = document.getElementById('lessonPageCard');
        const grid = document.querySelector('.vocab-table-grid');
        return {
          counter: document.getElementById('readerCardCounter').innerText,
          stageScrollHeight: stage.scrollHeight,
          stageClientHeight: stage.clientHeight,
          stageHasScrollbar: stage.scrollHeight > stage.clientHeight,
          cardHeight: card.offsetHeight,
          gridHeight: grid ? grid.offsetHeight : null
        };
      })()`,
      returnByValue: true
    });
    console.log('Unit 3 Card 15 metrics AFTER fix:', cardRes.result.value);

    // Screenshot
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/unit3_card15_after.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved scratch/unit3_card15_after.png');

    ws.close();
  } finally {
    chrome.kill();
    process.exit(0);
  }
}

run();
