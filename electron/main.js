const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');
const http = require('http');
const fs = require('fs');

// sin límite de cuadros del sistema: el límite lo controla el propio juego (Ajustes > Límite de FPS)
app.commandLine.appendSwitch('autoplay-policy', 'no-user-gesture-required');
app.commandLine.appendSwitch('ignore-gpu-blocklist');
app.commandLine.appendSwitch('disable-frame-rate-limit');
app.commandLine.appendSwitch('disable-gpu-vsync');

// Servidor local (127.0.0.1) para que las cuentas online funcionen (no funcionan desde file://)
function servir(cb) {
  const dir = path.join(__dirname, 'app');
  const mime = { '.html': 'text/html; charset=utf-8', '.png': 'image/png', '.js': 'text/javascript', '.json': 'application/json' };
  const srv = http.createServer((q, r) => {
    let f = path.join(dir, decodeURIComponent(q.url.split('?')[0]));
    if (q.url === '/' || f.endsWith(path.sep)) f = path.join(dir, 'index.html');
    if (!f.startsWith(dir)) { r.writeHead(403); r.end(); return; }
    fs.readFile(f, (e, d) => {
      if (e) { r.writeHead(404); r.end(); return; }
      r.writeHead(200, { 'Content-Type': mime[path.extname(f)] || 'application/octet-stream' });
      r.end(d);
    });
  });
  let tried = false;
  srv.on('error', () => { if (!tried) { tried = true; srv.listen(0, '127.0.0.1', () => cb(srv.address().port)); } });
  srv.listen(47831, '127.0.0.1', () => cb(47831));
}

function crear() {
  Menu.setApplicationMenu(null);
  const w = new BrowserWindow({
    width: 1280, height: 720, backgroundColor: '#000000',
    autoHideMenuBar: true, title: 'Mini Doom',
    icon: path.join(__dirname, 'icon.png'),
    webPreferences: { backgroundThrottling: false }
  });
  servir(p => w.loadURL('http://127.0.0.1:' + p + '/'));
  // F11: pantalla completa
  w.webContents.on('before-input-event', (e, i) => {
    if (i.type === 'keyDown' && i.key === 'F11') { w.setFullScreen(!w.isFullScreen()); e.preventDefault(); }
  });
}

app.whenReady().then(crear);
app.on('window-all-closed', () => app.quit());
