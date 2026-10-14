const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function main() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9228',
    '--window-size=1024,768',
    'about:blank'
  ]);

  await new Promise(r => setTimeout(r, 1500));

  try {
    const listRes = await fetch('http://localhost:9228/json/list');
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
    await new Promise(r => setTimeout(r, 2500));

    // 1. Click EN+UR
    const r1 = await send('Runtime.evaluate', { expression: "(() => { const b = document.getElementById('selectBothBtn'); if (b) { b.click(); return 'clicked'; } return 'no btn'; })()" });
    console.log("Step 1 (selectBothBtn):", r1);
    await new Promise(r => setTimeout(r, 800));

    // 2. Click Book 2 pill
    const r2 = await send('Runtime.evaluate', { expression: "(() => { const b = document.querySelector('.book-pill[data-book=\"2\"]'); if (b) { b.click(); return 'clicked'; } return 'no b2 pill'; })()" });
    console.log("Step 2 (book 2 pill):", r2);
    await new Promise(r => setTimeout(r, 800));

    // 3. Click Unit 26 exercises button
    const r3 = await send('Runtime.evaluate', { expression: "(() => { const cards = document.querySelectorAll('.journey-unit-card'); if (cards[25]) { cards[25].querySelector('.unit-ex-btn').click(); return 'clicked u26'; } return 'no u26 card'; })()" });
    console.log("Step 3 (u26 card):", r3);
    await new Promise(r => setTimeout(r, 800));

    // 4. Inspect modal cards
    const modalData = await send('Runtime.evaluate', {
      expression: `(() => {
        const cards = document.querySelectorAll('.tamreen-opt-card');
        return {
          count: cards.length,
          items: Array.from(cards).map(c => ({
            num: c.querySelector('.tamreen-opt-num')?.innerText,
            title: c.querySelector('.tamreen-opt-title')?.innerText,
            goal: c.querySelector('.tamreen-opt-goal')?.innerText
          }))
        };
      })()`,
      returnByValue: true
    });
    console.log("Modal Exercises for Book 2 Unit 26:\n", JSON.stringify(modalData.result.value, null, 2));

    // 5. Click first tamreen card (Tamreen 1)
    await send('Runtime.evaluate', { expression: "document.querySelector('.tamreen-opt-card').click()" });
    await new Promise(r => setTimeout(r, 1000));

    // 6. Screenshot
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/browser_quiz_fixed.png', Buffer.from(shot.data, 'base64'));
    console.log("Screenshot saved to scratch/browser_quiz_fixed.png!");

    // 7. Measure Layout
    const layout = await send('Runtime.evaluate', {
      expression: `(() => {
        const stage = document.getElementById('quizStage');
        const sRect = stage.getBoundingClientRect();
        const card = document.querySelector('.q-prompt-card').getBoundingClientRect();
        const grid = document.querySelector('.q-options-grid').getBoundingClientRect();
        const bar = document.getElementById('quizBottomBar').getBoundingClientRect();
        return {
          viewportHeight: window.innerHeight,
          stageHeight: Math.round(sRect.height),
          cardTop: Math.round(card.top),
          cardBottom: Math.round(card.bottom),
          gridTop: Math.round(grid.top),
          gridBottom: Math.round(grid.bottom),
          bottomBarTop: Math.round(bar.top),
          topGap: Math.round(card.top - sRect.top),
          bottomGap: Math.round(bar.top - grid.bottom),
          optionsCount: document.querySelectorAll('.q-option-btn').length,
          optionsTexts: Array.from(document.querySelectorAll('.q-option-btn')).map(b => b.innerText.trim())
        };
      })()`,
      returnByValue: true
    });
    console.log("Layout Geometry in Quiz:\n", JSON.stringify(layout.result.value, null, 2));

    ws.close();
  } finally {
    chrome.kill();
  }
}

main().catch(console.error);
