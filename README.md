# 🤖 ArgBot 🇦🇷

¡Bienvenido a **ArgBot**! Este es un bot de Discord que trae todo el espíritu argentino al servidor. Desde frases bien argentas hasta comandos con reacciones, tiene alta buena onda! 🧉

---

## 🚀 Funcionalidades

### 📜 Comandos Principales
- **`/arg che`**  
  Tirá frases bien argentas, no es ningún Bot aburrido 😎  
  *Ejemplo:*  
  `¿Qué onda, che?`

- **`/arg dicho`**  
  Compartí refranes típicos argentinos para sonar como un abuelo sabio.  
  *Ejemplo:*  
  `Más vale pájaro en mano que cien volando.`

- **`/arg gif <tema>`**  
  Busca y envía GIFs directamente desde Giphy para cualquier término.  
  *Ejemplo:*  
  `/arg gif mate` -> ![GIF](https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif)

- **`/arg mate <usuario>`**  
  Cebale un mate a alguien, porque la amistad es lo más grande!  
  *Ejemplo:*  
  `@Tomber está cebando un mate a @Usuario 🧉`

### 🤖 Respuestas Automáticas
- Agrega reacciones como 🧉 o 🍖 si alguien menciona palabras como "fernet", "mate" o "asado".

### 🎉 Bienvenida
- Le da la bienvenida a los nuevos miembros al estilo argentino.  
  *Ejemplo:*  
  `Q ondaaa, @NuevoMiembro! Bienvenido al server Pá 👋`

---

## 🛠️ Instalación

### 🔧 Requisitos
- Python 3.8 o superior.
- [Discord.py](https://discordpy.readthedocs.io/en/stable/) (`pip install discord.py`)
- [Requests](https://docs.python-requests.org/en/master/) (`pip install requests`)
- Una cuenta en [Giphy Developers](https://developers.giphy.com/) para obtener tu **API Key**.

### 📥 Configuración
1. Cloná el repositorio:
   ```bash
   git clone https://github.com/TuUsuario/Bot-Argentino.git
   cd Bot-Argentino

    Instalá las dependencias:

pip install -r requirements.txt

Configurá las variables de entorno: Creá un archivo .env y añadí lo siguiente:

DISCORD_TOKEN=tu_token_de_discord
GIPHY_API_TOKEN=tu_token_de_giphy

¡Ejecutá el bot!

    python main.py

🗂️ Estructura del Proyecto

Argbot/
- main.py                 # Archivo principal para ejecutar el bot
- cogs                    # Carpeta que contiene modulos de comandos
- frases.db               # Base de datos SQLite con frases argentinas
- requirements.txt        # Dependencias del proyecto
- .env                    # Tokens de Discord y Giphy (excluido de git)
- README.md               # Este hermoso archivo

📚 Tecnologías Usadas

    Discord.py: Librería para interactuar con la API de Discord.
    SQLite: Base de datos ligera para almacenar frases y datos.
    Giphy API: Para buscar y compartir GIFs.

🌟 Cómo Contribuir

    Hacé un fork del proyecto.
    Creá una nueva rama para tus cambios:

    git checkout -b mi-nueva-funcionalidad

    Subí tus cambios y hacé un pull request.

🧉 Licencia

Este proyecto está bajo la Licencia MIT. ¡Usalo libremente, pero cebá un mate a la comunidad compartiéndolo! 😁

¡Gracias por usar Bot Argentino! Si te gusta, dejá tu ⭐ en GitHub.
Si tenés sugerencias, ¡abrí un issue o mandame un mensaje por Discord! 🇦🇷
