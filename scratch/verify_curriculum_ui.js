const { spawn } = require('child_process');
const fs = require('fs');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function run() {
  console.log('Launching headless Chrome...');
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9235',
    'http://localhost:8080/index.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));

  try {
    const listRes = await fetch('http://localhost:9235/json/list');
    const tabs = await listRes.json();
    const targetTab = tabs.find(t => t.url.includes('localhost:8080')) || tabs[0];
    console.log('Connected to target tab:', targetTab.url);
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

    const consoleLogs = [];
    const exceptions = [];
    ws.addEventListener('message', (evt) => {
      const msg = JSON.parse(evt.data);
      if (msg.method === 'Runtime.consoleAPICalled') {
        consoleLogs.push(msg.params.args.map(a => a.value).join(' '));
      }
      if (msg.method === 'Runtime.exceptionThrown') {
        exceptions.push(msg.params.exceptionDetails);
        console.error('[EXCEPTION]', JSON.stringify(msg.params.exceptionDetails));
      }
    });

    await send('Runtime.enable');
    await send('Page.enable');
    await send('Emulation.setDeviceMetricsOverride', {
      width: 1280,
      height: 850,
      deviceScaleFactor: 1,
      mobile: false
    });

    await new Promise(r => setTimeout(r, 1000));

    // Helper for screenshots
    async function takeScreenshot(name) {
      const shot = await send('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(`scratch/${name}.png`, Buffer.from(shot.data, 'base64'));
      console.log(`Saved screenshot scratch/${name}.png`);
    }

    // 1. Dismiss splash with Urdu + English
    await send('Runtime.evaluate', {
      expression: `document.getElementById('selectBothBtn').click();`
    });
    await new Promise(r => setTimeout(r, 800));

    // 2. Open Book 1 Unit 1 Tamreen Selector Modal
    const modalRes1 = await send('Runtime.evaluate', {
      expression: `(() => {
        const btn = document.querySelector('.journey-unit-card .unit-ex-btn');
        if (btn) btn.click();
        const options = Array.from(document.querySelectorAll('.tamreen-opt-card')).map(c => c.innerText.replace(/\\n/g, ' '));
        return { open: !document.getElementById('tamreenSelectorModal').classList.contains('hidden'), options };
      })()`,
      returnByValue: true
    });
    console.log('Book 1 Unit 1 Selector Modal:', modalRes1.result.value);
    await takeScreenshot('modal_b1_u1_selector');

    // 3. Click "All Exercises" (starred card) to launch combined exercise
    await send('Runtime.evaluate', {
      expression: `(() => {
        const allCard = document.querySelector('.tamreen-opt-card.all-tamreens');
        if (allCard) allCard.click();
      })()`
    });
    await new Promise(r => setTimeout(r, 800));
    await takeScreenshot('quiz_b1_u1_all_exercises');

    // Close quiz
    await send('Runtime.evaluate', {
      expression: `document.getElementById('quizCloseBtn').click();`
    });
    await new Promise(r => setTimeout(r, 500));

    // 4. Switch to Book 2
    await send('Runtime.evaluate', {
      expression: `document.querySelectorAll('.book-pill')[1].click();`
    });
    await new Promise(r => setTimeout(r, 800));

    // Open Book 2 Unit 1 Tamreen Selector Modal
    const modalRes2 = await send('Runtime.evaluate', {
      expression: `(() => {
        const btn = document.querySelector('.journey-unit-card .unit-ex-btn');
        if (btn) btn.click();
        const options = Array.from(document.querySelectorAll('.tamreen-opt-card')).map(c => c.innerText.replace(/\\n/g, ' '));
        return { open: !document.getElementById('tamreenSelectorModal').classList.contains('hidden'), options };
      })()`,
      returnByValue: true
    });
    console.log('Book 2 Unit 1 Selector Modal:', modalRes2.result.value);
    await takeScreenshot('modal_b2_u1_selector');

    // Launch combined quiz in Book 2 Unit 1
    await send('Runtime.evaluate', {
      expression: `(() => {
        const allCard = document.querySelector('.tamreen-opt-card.all-tamreens');
        if (allCard) allCard.click();
      })()`
    });
    await new Promise(r => setTimeout(r, 800));
    await takeScreenshot('quiz_b2_u1_all_exercises');

    // Close quiz
    await send('Runtime.evaluate', {
      expression: `document.getElementById('quizCloseBtn').click();`
    });
    await new Promise(r => setTimeout(r, 500));

    // 5. Switch to Book 3
    await send('Runtime.evaluate', {
      expression: `document.querySelectorAll('.book-pill')[2].click();`
    });
    await new Promise(r => setTimeout(r, 800));

    // Open Book 3 Unit 1 Tamreen Selector Modal
    const modalRes3 = await send('Runtime.evaluate', {
      expression: `(() => {
        const btn = document.querySelector('.journey-unit-card .unit-ex-btn');
        if (btn) btn.click();
        const options = Array.from(document.querySelectorAll('.tamreen-opt-card')).map(c => c.innerText.replace(/\\n/g, ' '));
        return { open: !document.getElementById('tamreenSelectorModal').classList.contains('hidden'), options };
      })()`,
      returnByValue: true
    });
    console.log('Book 3 Unit 1 Selector Modal:', modalRes3.result.value);
    await takeScreenshot('modal_b3_u1_selector');

    // Launch combined quiz in Book 3 Unit 1
    await send('Runtime.evaluate', {
      expression: `(() => {
        const allCard = document.querySelector('.tamreen-opt-card.all-tamreens');
        if (allCard) allCard.click();
      })()`
    });
    await new Promise(r => setTimeout(r, 800));
    await takeScreenshot('quiz_b3_u1_all_exercises');

    console.log('\n--- VERIFICATION RESULT ---');
    console.log('Total Exceptions:', exceptions.length);
    console.log('Finished capturing all verification screenshots!');

    ws.close();
  } catch (err) {
    console.error('Error during test:', err);
  } finally {
    chrome.kill();
    process.exit(0);
  }
}

run();
