const { spawn } = require('child_process');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const fs = require('fs');

async function main() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9227',
    'about:blank'
  ]);
  await new Promise(r => setTimeout(r, 1500));

  try {
    const listRes = await fetch('http://localhost:9227/json/list');
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
        console.log('[BROWSER CONSOLE]', msg.params.type, msg.params.args.map(a => a.value).join(' '));
      }
      if (msg.method === 'Runtime.exceptionThrown') {
        console.error('[BROWSER EXCEPTION]', msg.params.exceptionDetails);
      }
    });

    await send('Runtime.enable');
    await send('Page.enable');
    
    // Set up load listener BEFORE navigate
    const loadPromise = new Promise(resolve => {
      const handler = (evt) => {
        const msg = JSON.parse(evt.data);
        if (msg.method === 'Page.loadEventFired') {
          ws.removeEventListener('message', handler);
          resolve();
        }
      };
      ws.addEventListener('message', handler);
    });

    console.log("Navigating to http://localhost:8080/index.html...");
    await send('Page.navigate', { url: 'http://localhost:8080/index.html' });
    await loadPromise;
    console.log("Page loaded!");
    await new Promise(r => setTimeout(r, 1000));

    const check = await send('Runtime.evaluate', {
      expression: '({ hasBooks: typeof window.MADINAH_BOOKS !== "undefined", booksCount: window.MADINAH_BOOKS?.books?.length, splashHidden: document.getElementById("splashOverlay")?.classList.contains("hidden") })',
      returnByValue: true
    });
    console.log("Page status:", check.result.value);

    // Click EN+UR
    console.log("Clicking selectBothBtn...");
    await send('Runtime.evaluate', { expression: "document.getElementById('selectBothBtn').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Click Book 2 pill
    console.log("Clicking Book 2 pill...");
    await send('Runtime.evaluate', { expression: "document.querySelector('.book-pill[data-book=\"2\"]').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Check cards
    const cardsData = await send('Runtime.evaluate', {
      expression: `(() => {
        const cards = document.querySelectorAll('.journey-unit-card');
        return {
          count: cards.length,
          unit26Title: cards[25]?.querySelector('.unit-card-title')?.innerText
        };
      })()`,
      returnByValue: true
    });
    console.log("Cards Data:", cardsData.result.value);

    // Click Unit 26 exercises button
    console.log("Clicking Unit 26 exercises button...");
    await send('Runtime.evaluate', { expression: "document.querySelectorAll('.journey-unit-card')[25].querySelector('.unit-ex-btn').click()" });
    await new Promise(r => setTimeout(r, 800));

    const modalData = await send('Runtime.evaluate', {
      expression: `(() => {
        const modal = document.getElementById('tamreenSelectorModal');
        const opts = document.querySelectorAll('.tamreen-opt-card');
        return {
          modalHidden: modal.classList.contains('hidden'),
          optsCount: opts.length,
          titles: Array.from(opts).map(o => o.querySelector('.tamreen-opt-title')?.innerText)
        };
      })()`,
      returnByValue: true
    });
    console.log("Modal Data for Unit 26:", JSON.stringify(modalData.result.value, null, 2));

    // Click Tamreen 1
    console.log("Clicking Tamreen 1...");
    await send('Runtime.evaluate', { expression: "document.querySelector('.tamreen-opt-card').click()" });
    await new Promise(r => setTimeout(r, 1000));

    // Screenshot of quiz
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/browser_quiz_fixed.png', Buffer.from(shot.data, 'base64'));
    console.log("Captured quiz screenshot to scratch/browser_quiz_fixed.png!");

    // Layout check
    const layout = await send('Runtime.evaluate', {
      expression: `(() => {
        const stage = document.getElementById('quizStage');
        const sRect = stage.getBoundingClientRect();
        const card = document.querySelector('.q-prompt-card').getBoundingClientRect();
        const grid = document.querySelector('.q-options-grid').getBoundingClientRect();
        const bar = document.getElementById('quizBottomBar').getBoundingClientRect();
        return {
          stageHeight: Math.round(sRect.height),
          cardTop: Math.round(card.top),
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
