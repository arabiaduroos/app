const { spawn } = require('child_process');
const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless=new',
  '--disable-gpu',
  '--remote-debugging-port=9230',
  'http://localhost:8080/index.html'
]);

setTimeout(async () => {
  try {
    const list = await (await fetch('http://localhost:9230/json/list')).json();
    const tab = list.find(t => t.url.includes('localhost:8080')) || list[0];
    const ws = new WebSocket(tab.webSocketDebuggerUrl);
    await new Promise(r => ws.onopen = r);
    ws.onmessage = (e) => {
      const msg = JSON.parse(e.data);
      if (msg.method === 'Runtime.consoleAPICalled') {
        console.log('LOG:', msg.params.args.map(a => a.value || a.description || JSON.stringify(a)));
      }
      if (msg.method === 'Runtime.exceptionThrown') {
        console.error('EXCEPTION:', JSON.stringify(msg.params.exceptionDetails));
      }
    };
    let id = 1;
    const send = (m, p={}) => new Promise(res => {
      const reqId = id++;
      const h = (e) => {
        const d = JSON.parse(e.data);
        if (d.id === reqId) { ws.removeEventListener('message', h); res(d.result); }
      };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: reqId, method: m, params: p }));
    });
    await send('Runtime.enable');
    await send('Page.enable');
    await new Promise(r => setTimeout(r, 1000));

    const dom = await send('Runtime.evaluate', {
      expression: `(() => {
        return {
          readyState: document.readyState,
          gridFound: !!document.getElementById('journeyUnitsGrid'),
          gridChildCount: document.getElementById('journeyUnitsGrid')?.children.length,
          splashHidden: document.getElementById('splashOverlay')?.classList.contains('hidden'),
          cardsCount: document.querySelectorAll('.journey-unit-card').length,
          errors: window.__errors || []
        };
      })()`,
      returnByValue: true
    });
    console.log('DOM info:', dom.result.value);
    ws.close();
  } catch(e) {
    console.error(e);
  } finally {
    chrome.kill();
  }
}, 1500);
