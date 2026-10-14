const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function main() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9223',
    '--window-size=1024,768',
    'about:blank'
  ]);

  await new Promise(r => setTimeout(r, 1500));

  try {
    const listRes = await fetch('http://localhost:9223/json/list');
    const tabs = await listRes.json();
    const tab = tabs.find(t => t.type === 'page') || tabs[0];
    console.log("Connecting to WS:", tab.webSocketDebuggerUrl);

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

    console.log("Navigating to http://localhost:8080/index.html...");
    await send('Page.navigate', { url: 'http://localhost:8080/index.html' });
    await new Promise(r => setTimeout(r, 2000));

    // 1. Click EN+UR
    await send('Runtime.evaluate', { expression: "document.getElementById('selectBothBtn').click()" });
    await new Promise(r => setTimeout(r, 600));

    // 2. Click Book 2 pill
    await send('Runtime.evaluate', { expression: "document.querySelector('.book-pill[data-book=\"2\"]').click()" });
    await new Promise(r => setTimeout(r, 600));

    // 3. Click Unit 26 exercises button
    await send('Runtime.evaluate', { expression: "document.querySelectorAll('.journey-unit-card')[25].querySelector('.unit-ex-btn').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Inspect modal tamreens
    const modalData = await send('Runtime.evaluate', {
      expression: `({
        title: document.getElementById('tamreenSelectorTitle').innerText,
        optionsCount: document.querySelectorAll('.tamreen-opt-card').length,
        optionsTexts: Array.from(document.querySelectorAll('.tamreen-opt-card .tamreen-opt-title')).map(el => el.innerText)
      })`,
      returnByValue: true
    });
    console.log("Modal Data for Unit 26:", JSON.stringify(modalData.result.value, null, 2));

    // 4. Click first tamreen card
    await send('Runtime.evaluate', { expression: "document.querySelector('.tamreen-opt-card').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Capture screenshot of quiz
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/browser_quiz_fixed.png', Buffer.from(shot.data, 'base64'));
    console.log("Screenshot written to scratch/browser_quiz_fixed.png!");

    // Check bounds of stage and options
    const layout = await send('Runtime.evaluate', {
      expression: `(() => {
        const stage = document.getElementById('quizStage');
        const sRect = stage.getBoundingClientRect();
        const card = document.querySelector('.q-prompt-card').getBoundingClientRect();
        const grid = document.querySelector('.q-options-grid').getBoundingClientRect();
        const bar = document.getElementById('quizBottomBar').getBoundingClientRect();
        return {
          stageTop: sRect.top,
          stageBottom: sRect.bottom,
          stageHeight: sRect.height,
          cardTop: card.top,
          gridBottom: grid.bottom,
          bottomBarTop: bar.top,
          spaceAboveCard: card.top - sRect.top,
          spaceBelowGrid: bar.top - grid.bottom
        };
      })()`,
      returnByValue: true
    });
    console.log("Layout Geometry:", JSON.stringify(layout.result.value, null, 2));

    ws.close();
  } finally {
    chrome.kill();
  }
}

main().catch(console.error);
