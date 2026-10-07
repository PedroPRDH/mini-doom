# Mini Doom: proyecto para APK

Contiene el juego (www/index.html), la app instalable (PWA) y todo lo necesario para generar un APK de Android.

## Opción A: APK en la nube, sin instalar nada (recomendada)
1. Crea un repositorio nuevo en github.com y sube TODO el contenido de esta carpeta (incluida `.github`).
   Si el navegador no sube la carpeta oculta `.github`, crea el archivo `.github/workflows/apk.yml` desde GitHub con "Add file > Create new file" y pega el contenido del que viene aquí.
2. Entra en la pestaña **Actions**, elige **Construir APK** y pulsa **Run workflow**.
3. A los 5 o 8 minutos, abre la ejecución y descarga **MiniDoom-apk**. Dentro está `app-debug.apk`.
4. Pásalo al celular e instálalo (hay que permitir "instalar apps desconocidas").

## Opción B: instalar como app sin APK (PWA)
Sube la carpeta `www` a GitHub Pages, Netlify o similar, ábrela en Chrome del celular y toca "Instalar app". Si quieres un APK a partir de esa URL, usa pwabuilder.com.

## Opción C: en tu computadora
Necesitas Node 18 o superior, JDK 17 y Android Studio (para el SDK).
```
npm install
npx cap add android
npx cap sync android
cd android && ./gradlew assembleDebug
```
El APK queda en `android/app/build/outputs/apk/debug/app-debug.apk`.

El APK de depuración sirve para uso personal. Para subirlo a Google Play hay que firmarlo con tu propia llave.
