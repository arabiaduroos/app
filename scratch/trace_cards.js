const { spawn } = require('child_process');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function main() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9229',
    'about:blank'
  ]);
  await new Promise(r => setTimeout(r, 1500));
  try {
    const listRes = await fetch('http://localhost:9229/json/list');
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

    await send('Runtime.enable');
    await send('Page.enable');
    await send('Page.navigate', { url: 'http://localhost:8080/index.html' });
    await new Promise(r => setTimeout(r, 2000));

    // Check localStorage before click
    const s0 = await send('Runtime.evaluate', {
      expression: '({ stateLang: window.state ? window.state.lang : "no state", booksLen: window.MADINAH_BOOKS ? window.MADINAH_BOOKS.books.length : "no books" })',
      returnByValue: true
    });
    console.log('Initial state:', s0.result.value);

    // Click selectBothBtn
    await send('Runtime.evaluate', { expression: "document.getElementById('selectBothBtn').click()" });
    await new Promise(r => setTimeout(r, 500));

    // Check count of cards in Book 1 (default)
    const c1 = await send('Runtime.evaluate', {
      expression: 'document.querySelectorAll(".journey-unit-card").length',
      returnByValue: true
    });
    console.log('Book 1 cards count:', c1.result.value);

    // Switch to Book 2
    await send('Runtime.evaluate', { expression: 'document.querySelector("#bookSwitcher .book-pill[data-book=\\"2\\"]").click()' });
    await new Promise(r => setTimeout(r, 500));

    const c2 = await send('Runtime.evaluate', {
      expression: 'document.querySelectorAll(".journey-unit-card").length',
      returnByValue: true
    });
    console.log('Book 2 cards count:', c2.result.value);

    // Titles of Book 2 cards
    const titles = await send('Runtime.evaluate', {
      expression: 'Array.from(document.querySelectorAll(".journey-unit-card .unit-card-title")).map(el => el.innerText)',
      returnByValue: true
    });
    console.log('Book 2 card titles count:', titles.result.value.length);
    console.log('First title:', titles.result.value[0]);
    console.log('Unit 26 title:', titles.result.value[25]);

    // Click Unit 26 exercises button
    await send('Runtime.evaluate', {
      expression: 'document.querySelectorAll(".journey-unit-card")[25].querySelector(".unit-ex-btn").click()'
    });
    await new Promise(r => setTimeout(r, 500));

    // Modal options
    const mOpts = await send('Runtime.evaluate', {
      expression: 'Array.from(document.querySelectorAll(".tamreen-opt-card .tamreen-opt-title")).map(el => el.innerText)',
      returnByValue: true
    });
    console.log('Unit 26 Modal options:', mOpts.result.value);

    ws.close();
  } finally {
    chrome.kill();
  }
}
main().catch(console.error);
