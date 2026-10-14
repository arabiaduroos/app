const { spawn } = require('child_process');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function main() {
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9230',
    'about:blank'
  ]);
  await new Promise(r => setTimeout(r, 1500));
  try {
    const listRes = await fetch('http://localhost:9230/json/list');
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
      if (msg.method === 'Network.responseReceived') {
        console.log('[NETWORK RESPONSE]', msg.params.response.url, msg.params.response.status, msg.params.response.mimeType);
      }
      if (msg.method === 'Network.loadingFailed') {
        console.log('[NETWORK FAILED]', msg.params);
      }
      if (msg.method === 'Runtime.exceptionThrown') {
        console.log('[EXCEPTION]', msg.params.exceptionDetails.text, msg.params.exceptionDetails.exception);
      }
    });

    await send('Network.enable');
    await send('Runtime.enable');
    await send('Page.enable');

    console.log("Navigating...");
    await send('Page.navigate', { url: 'http://localhost:8080/index.html' });
    await new Promise(r => setTimeout(r, 3000));

    ws.close();
  } finally {
    chrome.kill();
  }
}
main().catch(console.error);
