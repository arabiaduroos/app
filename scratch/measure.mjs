import { spawn } from 'child_process';

const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless',
  '--disable-gpu',
  '--remote-debugging-port=9229',
  '--window-size=1024,576',
  'file:///C:/Users/Person/Documents/GitHub/app/index.html?unit=b1_u3&card=35'
]);

setTimeout(async () => {
  try {
    const res = await fetch('http://localhost:9229/json');
    const tabs = await res.json();
    const wsUrl = tabs[0].webSocketDebuggerUrl;
    const ws = new WebSocket(wsUrl);
    ws.onopen = () => {
      ws.send(JSON.stringify({
        id: 1,
        method: 'Runtime.evaluate',
        params: {
          expression: `(() => {
            const stage = document.querySelector('.lesson-stage');
            const card = document.querySelector('.lesson-page-card');
            const topbar = document.querySelector('.reader-topbar');
            const bottombar = document.querySelector('.lesson-bottombar');
            const grid = document.querySelector('.vocab-words-grid');
            const headerBox = document.querySelector('.vocab-table-header-box');
            const counter = document.getElementById('readerCardCounter')?.textContent;
            const tile = document.querySelector('.vocab-word-tile');
            return JSON.stringify({
              counter,
              windowH: window.innerHeight,
              topbarH: topbar?.offsetHeight,
              bottombarH: bottombar?.offsetHeight,
              stageH: stage?.offsetHeight,
              stageScrollH: stage?.scrollHeight,
              cardH: card?.offsetHeight,
              gridH: grid?.offsetHeight,
              gridRows: grid ? window.getComputedStyle(grid).gridTemplateRows.split(' ').length : 0,
              gridCols: grid ? window.getComputedStyle(grid).gridTemplateColumns.split(' ').length : 0,
              tileH: tile?.offsetHeight,
              wordsCount: grid?.children?.length,
              hasScrollbar: stage ? stage.scrollHeight > stage.clientHeight : false
            });
          })()`,
          returnByValue: true
        }
      }));
    };
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.id === 1) {
        console.log('576H VOCAB LAYOUT STATS:\n', JSON.stringify(JSON.parse(data.result.result.value), null, 2));
        ws.close();
        chrome.kill();
        process.exit(0);
      }
    };
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 2000);
