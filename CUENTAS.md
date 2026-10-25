# Cuentas online y clasificatoria (Firebase, plan gratuito)

1. https://console.firebase.google.com → Agregar proyecto (sin Analytics).
2. Build → Authentication → Comenzar → Sign-in method: activar **Google** y **Correo electrónico/contraseña**.
   Settings → Authorized domains: agregar `pedroprdh.github.io`.
3. Build → Firestore Database → Crear base de datos (modo producción) → pestaña **Reglas** → pegar el contenido de `firestore.rules` → Publicar.
4. Project settings → General → Tus apps → Web (`</>`) → registrar app → copiar el objeto `firebaseConfig`.
5. Pasarle ese objeto a Claude para incrustarlo en el juego (no son claves secretas: la seguridad la dan las reglas).
