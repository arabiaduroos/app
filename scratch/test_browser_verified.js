const { spawn } = require('child_process');
const fs = require('fs');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function testBrowser() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9228',
    'http://localhost:8080/index.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));

  try {
    const listRes = await fetch('http://localhost:9228/json/list');
    const tabs = await listRes.json();
    console.log('Tabs:', tabs.map(t => ({ url: t.url, title: t.title })));
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

    ws.addEventListener('message', (evt) => {
      const msg = JSON.parse(evt.data);
      if (msg.method === 'Runtime.consoleAPICalled') {
        console.log('[CONSOLE]', msg.params.args.map(a => a.value).join(' '));
      }
      if (msg.method === 'Runtime.exceptionThrown') {
        console.error('[EXCEPTION]', JSON.stringify(msg.params.exceptionDetails));
      }
    });

    await send('Runtime.enable');
    await send('Page.enable');

    // Wait a moment for page scripts to finish initializing
    await new Promise(r => setTimeout(r, 1500));

    const check = await send('Runtime.evaluate', {
      expression: '({ url: window.location.href, hasBooks: typeof window.MADINAH_BOOKS !== "undefined", booksCount: window.MADINAH_BOOKS ? window.MADINAH_BOOKS.books.length : 0 })',
      returnByValue: true
    });
    console.log('Check result:', check.result.value);

    // Click EN + UR button on splash
    await send('Runtime.evaluate', { expression: "document.getElementById('selectBothBtn').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Switch to Book 2
    await send('Runtime.evaluate', { expression: "document.querySelector('.book-pill[data-book=\"2\"]').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Get units in Book 2
    const uInfo = await send('Runtime.evaluate', {
      expression: `(() => {
        const cards = document.querySelectorAll('.journey-unit-card');
        return {
          totalCards: cards.length,
          firstTitle: cards[0]?.querySelector('.unit-card-title')?.innerText,
          u26Title: cards[25]?.querySelector('.unit-card-title')?.innerText
        };
      })()`,
      returnByValue: true
    });
    console.log('Book 2 units info:', uInfo.result.value);

    // Open Tamreens modal for Unit 26 (index 25)
    await send('Runtime.evaluate', { expression: "document.querySelectorAll('.journey-unit-card')[25].querySelector('.unit-ex-btn').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Check modal contents
    const modalInfo = await send('Runtime.evaluate', {
      expression: `(() => {
        const opts = document.querySelectorAll('.tamreen-opt-card');
        return {
          count: opts.length,
          items: Array.from(opts).map(o => ({
            num: o.querySelector('.tamreen-opt-num')?.innerText,
            title: o.querySelector('.tamreen-opt-title')?.innerText,
            goal: o.querySelector('.tamreen-opt-goal')?.innerText
          }))
        };
      })()`,
      returnByValue: true
    });
    console.log('Modal Options for Unit 26:', JSON.stringify(modalInfo.result.value, null, 2));

    // Screenshot of the Tamreens modal
    const modalShot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/unit26_tamreens_modal.png', Buffer.from(modalShot.data, 'base64'));
    console.log('Saved scratch/unit26_tamreens_modal.png');

    // Click on Tamreen 1 to open the quiz
    await send('Runtime.evaluate', { expression: "document.querySelectorAll('.tamreen-opt-card')[0].click()" });
    await new Promise(r => setTimeout(r, 800));

    // Check quiz layout and screenshot
    const quizShot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/quiz_layout_fixed.png', Buffer.from(quizShot.data, 'base64'));
    console.log('Saved scratch/quiz_layout_fixed.png');

    const layout = await send('Runtime.evaluate', {
      expression: `(() => {
        const stage = document.getElementById('quizStage');
        const sRect = stage.getBoundingClientRect();
        const card = document.querySelector('.q-prompt-card')?.getBoundingClientRect();
        const grid = document.querySelector('.q-options-grid')?.getBoundingClientRect();
        const bar = document.getElementById('quizBottomBar')?.getBoundingClientRect();
        return {
          viewportHeight: window.innerHeight,
          stageHeight: Math.round(sRect.height),
          cardTop: card ? Math.round(card.top) : null,
          gridBottom: grid ? Math.round(grid.bottom) : null,
          bottomBarTop: bar ? Math.round(bar.top) : null,
          spaceAbove: card ? Math.round(card.top - sRect.top) : null,
          spaceBelow: (grid && bar) ? Math.round(bar.top - grid.bottom) : null
        };
      })()`,
      returnByValue: true
    });
    console.log('Quiz Layout measurements:', layout.result.value);

    ws.close();
  } finally {
    chrome.kill();
  }
}

testBrowser().catch(console.error);
