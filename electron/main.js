const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');

// sin límite de cuadros del sistema: el límite lo controla el propio juego (Ajustes > Límite de FPS)
app.commandLine.appendSwitch('autoplay-policy', 'no-user-gesture-required');
app.commandLine.appendSwitch('ignore-gpu-blocklist');
app.commandLine.appendSwitch('disable-frame-rate-limit');
app.commandLine.appendSwitch('disable-gpu-vsync');

function crear() {
  Menu.setApplicationMenu(null);
  const w = new BrowserWindow({
    width: 1280, height: 720, backgroundColor: '#000000',
    autoHideMenuBar: true, title: 'Mini Doom',
    icon: path.join(__dirname, 'icon.png'),
    webPreferences: { backgroundThrottling: false }
  });
  w.loadFile(path.join(__dirname, 'app', 'index.html'));
  // F11: pantalla completa
  w.webContents.on('before-input-event', (e, i) => {
    if (i.type === 'keyDown' && i.key === 'F11') { w.setFullScreen(!w.isFullScreen()); e.preventDefault(); }
  });
}

app.whenReady().then(crear);
app.on('window-all-closed', () => app.quit());
