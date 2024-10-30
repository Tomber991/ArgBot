import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env
token = os.getenv('DISCORD_TOKEN')  # Lee el token desde la variable de entorno

# Verifica si el token se ha cargado correctamente
if token is None:
    print("Error: El token de Discord no se ha cargado. Verifica el archivo .env.")
else:
    print("El token se ha cargado correctamente.")

# Resto del código para inicializar el bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

bot = commands.Bot(command_prefix='/arg ', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} está listo para repartir mates y buena onda.')
    await bot.change_presence(activity="Bip BiP BOp")

async def load_extensions():
    await bot.load_extension('cogs.comandos')

async def main():
    await load_extensions()
    await bot.start(token)

import asyncio
asyncio.run(main())
