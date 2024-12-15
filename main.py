import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from cogs import secrets

load_dotenv()  # Carga el archivo .env

token = os.getenv('DISCORD_TOKEN')  # Lee el token desde la variable de entorno
BOT_PREFIX=os.getenv('BOT_PREFIX', "/")

# Verifica si el token se ha cargado correctamente
def Token_Is_Load():
    if token is None:
        print("Error: El token de Discord no se ha cargado. Verifica el archivo .env.")
    else:
        print("El token se ha cargado correctamente.")


# Resto del código para inicializar el bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user.name} está listo para repartir mates y buena onda.')
    
async def load_extensions():
    await bot.load_extension('cogs.general')

# Carga automática de cogs desde la carpeta 'cogs'
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        cog_name = f'cogs.{filename[:-3]}'
        bot.load_extension(cog_name)

Token_Is_Load()
async def main():

    await load_extensions()
    await bot.start(token)

import asyncio
asyncio.run(main())
