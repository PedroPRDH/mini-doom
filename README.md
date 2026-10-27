# Mini Doom

Un clon de Doom para celular y PC, hecho con Three.js. Todo el juego vive en un único archivo (`index.html`): modelos 3D, texturas, música y efectos de sonido van incluidos, así que funciona sin conexión (salvo las cuentas y la clasificatoria).

Proyecto personal, sin fines comerciales.

## Jugar

| Plataforma | Cómo |
|---|---|
| **Navegador** (sin instalar nada) | https://pedroprdh.github.io/mini-doom/ — también se puede "Instalar app" desde Chrome |
| **Android** | Pestaña **Actions** → "Construir APK" → última ejecución → artefacto **MiniDoom-apk** (`app-debug.apk`). Hay que permitir "instalar apps desconocidas" |
| **Windows** | [Releases → pc-latest](../../releases/tag/pc-latest) → `MiniDoom-PC.exe` (portable, sin instalación). Windows puede mostrar el aviso de SmartScreen porque no está firmado: "Más información → Ejecutar de todas formas" |

Cada push a `main` regenera automáticamente la web, el APK y el `.exe`.

## Contenido

- **10 niveles**: 6 en el Infierno (el sexto es el jefe: el Icono del Pecado) y 4 en la Tierra (ciudad, parque, autopista, azotea).
- **22 tipos de enemigos**, con IA por mapa de flujo, esquive y alerta en grupo.
- **8 armas**: pistola, escopeta, ametralladora, plasma, superescopeta, lanzacohetes, BFG y **motosierra** (corte continuo cuerpo a cuerpo; lo que mata con ella suelta vida, munición o armadura con más frecuencia).
- **Botas** (se desbloquean al vencer al Icono del Pecado): doble salto y deslizamiento / salto por las paredes. Los niveles de la Tierra son multinivel y están pensados para esa movilidad.
- **Rueda de armas**: mantener ARMA (o Q) abre un selector radial con el mundo en cámara lenta (o en pausa, desde Ajustes).
- **Guardado** automático al empezar cada nivel y botón *Continuar*.
- **Modo rejugar**: al terminar el juego se puede elegir cualquier nivel y jugarlo con las 8 armas y las botas desde el inicio.
- **Cuentas y clasificatoria**: ingreso con Google (solo en la web) o con correo y contraseña. Ranking global de monstruos eliminados, juegos completados, victorias contra el Icono del Pecado, niveles superados y muertes.

## Controles

**Celular**
- Joystick izquierdo: moverse · deslizar a la derecha: mirar.
- **FUEGO**: disparar; mientras se mantiene, arrastrar el dedo también apunta.
- **ARMA**: tocar = siguiente arma · mantener = rueda de armas (arrastrar hacia el arma y soltar).
- **DASH** y **SALTO** (con las botas).

**PC (mouse y teclado)**
- `WASD` mover · mouse apuntar · clic izquierdo disparar · clic derecho dash · `Espacio` saltar · `Shift` correr.
- `Q` (mantener) rueda de armas · rueda del mouse o `1`–`8` cambiar de arma · `Esc` pausa · `F11` pantalla completa (versión .exe).

**Mando** (Xbox / estándar)
- Stick izquierdo mover (clic del stick = correr) · stick derecho apuntar · `RT` disparar · `A` saltar · `B` o `LT` dash.
- `RB` / `LB` o cruceta: cambiar de arma · `Y` (mantener) rueda de armas, elegir con el stick derecho · `Start` pausa.

La interfaz táctil se oculta sola al detectar mouse o mando, y vuelve si se toca la pantalla.

## Ajustes útiles

Dificultad, resolución 3D, resolución dinámica, texturas, luces, partículas, sacudida de cámara, sensibilidad, música y efectos, **límite de FPS (30 / 60 / 120 / 144 / sin límite)**, contador de FPS (simple o detallado), cinemáticas y comportamiento de la rueda de armas.

## Cuentas online (Firebase)

Usa Firebase Authentication y Cloud Firestore (plan gratuito). Las reglas de seguridad están en [`firestore.rules`](firestore.rules) y los pasos para montarlo en tu propio proyecto en [`CUENTAS.md`](CUENTAS.md). La configuración web de Firebase está incrustada en el juego (no es secreta: la seguridad la dan las reglas).

Limitaciones conocidas:
- Google no permite su login dentro de apps embebidas, así que en el APK y en el `.exe` el acceso es con correo y contraseña.
- Es un juego del lado del cliente: las reglas limitan cuánto puede subir cada contador por escritura, pero no impiden del todo que alguien falsee estadísticas.

## Estructura del repositorio

```
index.html                  el juego completo (web, APK y PC lo usan)
manifest.webmanifest, sw.js instalación como app (PWA)
electron/                   envoltorio de escritorio (Electron) → .exe portable
src/levels/                 generadores de niveles (Python)
src/tools/                  generador de modelos y niveles de detalle (Python)
.github/workflows/
  main.yml                  construye el APK (Capacitor)
  pc.yml                    construye el .exe (Electron) y lo publica en la release pc-latest
  web.yml                   publica la web en GitHub Pages
firestore.rules             reglas de la base de datos
```

`index.html` es un archivo generado (≈30 MB) a partir del código fuente del juego, los modelos 3D y el audio; por eso los generadores de `src/` están aparte.

## Compilar a mano

**APK**: Node 18+, JDK 17 y Android SDK.
```
npm install
npx cap add android
npx cap sync android
cd android && ./gradlew assembleDebug
```
**PC**: dentro de `electron/`, copiar `index.html` a `electron/app/` y el icono a `electron/icon.png`, luego `npm install && npx electron-builder --win portable`.

El APK de depuración sirve para uso personal. Para publicar en Google Play hay que firmarlo con una llave propia.
