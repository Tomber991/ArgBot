# main.py
"""
    Código bien Argentino, por Tomber991
"""

import discord
from discord.ext import commands
from dotenv import load_doten
import asyncio

load_dotenv()

# Obtener el token de Discord
token = os.getenv('DISCORD_TOKEN')

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

# Crear el bot
bot = commands.Bot(command_prefix='arg> ', intents=intents)

# Evento on_ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} está listo para repartir mates y buena onda.')

# Función asíncrona para cargar la extensión
async def load_extensions():
    await bot.load_extension('comandos')  # Cargar el módulo de comandos como extensión

# Ejecutar el bot
async def main():
    await load_extensions()
    await bot.start(token)

# Iniciar el loop de eventos
asyncio.run(main())
