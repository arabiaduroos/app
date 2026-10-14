const { spawn } = require('child_process');
const fs = require('fs');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function testUnit14Reader() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--window-size=1280,800',
    '--remote-debugging-port=9236',
    'http://localhost:8080/index.html'
  ]);
  await new Promise(r => setTimeout(r, 2000));

  try {
    const listRes = await fetch('http://localhost:9236/json/list');
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

    // Open Lesson Reader for Unit 14 (index 13)
    await send('Runtime.evaluate', { expression: "document.querySelectorAll('.journey-unit-card')[13].querySelector('.unit-read-btn').click()" });
    await new Promise(r => setTimeout(r, 800));

    // Click next button 19 times to reach Card 20
    for (let step = 1; step <= 19; step++) {
      await send('Runtime.evaluate', { expression: "document.getElementById('lessonNextBtn').click()" });
      await new Promise(r => setTimeout(r, 80));
    }
    await new Promise(r => setTimeout(r, 600));

    const card20Info = await send('Runtime.evaluate', {
      expression: `(() => {
        return {
          counter: document.getElementById('readerCardCounter')?.innerText,
          hasVocabTable: !!document.querySelector('.vocab-table-card'),
          title: document.querySelector('.vocab-table-title')?.innerText,
          cellCount: document.querySelectorAll('.vocab-cell')?.length,
          firstCell: document.querySelector('.vocab-cell')?.innerText
        };
      })()`,
      returnByValue: true
    });
    console.log('Card 20 info:', card20Info.result.value);

    // Screenshot of Card 20
    const shot1 = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/unit14_vocab_card20.png', Buffer.from(shot1.data, 'base64'));
    console.log('Saved scratch/unit14_vocab_card20.png');

    // Click next to go to Card 21
    await send('Runtime.evaluate', { expression: "document.getElementById('lessonNextBtn').click()" });
    await new Promise(r => setTimeout(r, 600));

    const card21Info = await send('Runtime.evaluate', {
      expression: `(() => {
        return {
          counter: document.getElementById('readerCardCounter')?.innerText,
          hasVocabTable: !!document.querySelector('.vocab-table-card'),
          title: document.querySelector('.vocab-table-title')?.innerText,
          cellCount: document.querySelectorAll('.vocab-cell')?.length,
          firstCell: document.querySelector('.vocab-cell')?.innerText
        };
      })()`,
      returnByValue: true
    });
    console.log('Card 21 info:', card21Info.result.value);

    // Screenshot of Card 21
    const shot2 = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/unit14_vocab_card21.png', Buffer.from(shot2.data, 'base64'));
    console.log('Saved scratch/unit14_vocab_card21.png');

    // Also test "Full Text" mode
    await send('Runtime.evaluate', { expression: "document.getElementById('readerModeFullBtn').click()" });
    await new Promise(r => setTimeout(r, 600));

    const fullInfo = await send('Runtime.evaluate', {
      expression: `(() => {
        return {
          fullTables: document.querySelectorAll('.vocab-table-card.full-text-vocab')?.length,
          fullRows: document.querySelectorAll('.t-illus-row')?.length
        };
      })()`,
      returnByValue: true
    });
    console.log('Full text mode info:', fullInfo.result.value);

    ws.close();
  } finally {
    chrome.kill();
  }
}

testUnit14Reader().catch(console.error);
