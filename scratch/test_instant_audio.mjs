import { spawn } from 'child_process';

const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless',
  '--disable-gpu',
  '--remote-debugging-port=9230',
  '--window-size=1024,576',
  'file:///C:/Users/Person/Documents/GitHub/app/index.html?unit=b1_u3&card=35'
]);

setTimeout(async () => {
  try {
    const res = await fetch('http://localhost:9230/json');
    const tabs = await res.json();
    const wsUrl = tabs[0].webSocketDebuggerUrl;
    const ws = new WebSocket(wsUrl);
    ws.onopen = () => {
      ws.send(JSON.stringify({
        id: 1,
        method: 'Runtime.evaluate',
        params: {
          expression: `(async () => {
            return JSON.stringify({
              appExposed: typeof window.app !== 'undefined',
              currentCard: document.getElementById('readerCardCounter')?.textContent,
              vocabTilesCount: document.querySelectorAll('.vocab-word-tile').length
            });
          })()`,
          awaitPromise: true,
          returnByValue: true
        }
      }));
    };
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.id === 1) {
        console.log('TEST RESULT:\n', data.result.result.value);
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
