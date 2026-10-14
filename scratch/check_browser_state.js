const { spawn } = require('child_process');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function main() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9225',
    'about:blank'
  ]);
  await new Promise(r => setTimeout(r, 1500));

  try {
    const listRes = await fetch('http://localhost:9225/json/list');
    const tabs = await listRes.json();
    const ws = new WebSocket(tabs[0].webSocketDebuggerUrl);
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
        console.error('[EXCEPTION]', msg.params.exceptionDetails);
      }
    });

    await send('Runtime.enable');
    await send('Page.enable');
    await send('Page.navigate', { url: 'http://localhost:8080/index.html' });
    await new Promise(r => setTimeout(r, 2000));

    const check = await send('Runtime.evaluate', {
      expression: '({ hasBooks: typeof window.MADINAH_BOOKS !== "undefined", booksCount: window.MADINAH_BOOKS ? window.MADINAH_BOOKS.books.length : 0 })',
      returnByValue: true
    });
    console.log('Check result:', check.result.value);

    // Click EN+UR
    await send('Runtime.evaluate', { expression: "document.getElementById('selectBothBtn').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Click Book 2 pill
    await send('Runtime.evaluate', { expression: "document.querySelector('.book-pill[data-book=\"2\"]').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Check cards
    const cardInfo = await send('Runtime.evaluate', {
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
    console.log('Card info:', cardInfo.result.value);

    // Open Tamreens modal for Unit 26
    await send('Runtime.evaluate', { expression: "document.querySelectorAll('.journey-unit-card')[25].querySelector('.unit-ex-btn').click()" });
    await new Promise(r => setTimeout(r, 800));

    const modalInfo = await send('Runtime.evaluate', {
      expression: `(() => {
        const opts = document.querySelectorAll('.tamreen-opt-card');
        return {
          optionsCount: opts.length,
          titles: Array.from(opts).map(o => o.querySelector('.tamreen-opt-title')?.innerText),
          goals: Array.from(opts).map(o => o.querySelector('.tamreen-opt-goal')?.innerText)
        };
      })()`,
      returnByValue: true
    });
    console.log('Modal info for Unit 26:', modalInfo.result.value);

    // Click Tamreen 1
    await send('Runtime.evaluate', { expression: "document.querySelector('.tamreen-opt-card').click()" });
    await new Promise(r => setTimeout(r, 800));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/browser_quiz_fixed.png', Buffer.from(shot.data, 'base64'));
    console.log("Quiz screenshot saved to scratch/browser_quiz_fixed.png!");

    // Layout check
    const layout = await send('Runtime.evaluate', {
      expression: `(() => {
        const stage = document.getElementById('quizStage');
        const sRect = stage.getBoundingClientRect();
        const card = document.querySelector('.q-prompt-card').getBoundingClientRect();
        const grid = document.querySelector('.q-options-grid').getBoundingClientRect();
        const bar = document.getElementById('quizBottomBar').getBoundingClientRect();
        return {
          stageTop: Math.round(sRect.top),
          stageBottom: Math.round(sRect.bottom),
          stageHeight: Math.round(sRect.height),
          cardTop: Math.round(card.top),
          cardBottom: Math.round(card.bottom),
          gridTop: Math.round(grid.top),
          gridBottom: Math.round(grid.bottom),
          bottomBarTop: Math.round(bar.top),
          spaceAboveCard: Math.round(card.top - sRect.top),
          spaceBelowGrid: Math.round(bar.top - grid.bottom)
        };
      })()`,
      returnByValue: true
    });
    console.log("Layout Geometry:", layout.result.value);

    ws.close();
  } finally {
    chrome.kill();
  }
}

main().catch(console.error);
