import discord
from discord.ext import commands
import random
import requests
import os
from dotenv import load_dotenv
import sqlite3

# Conectar a la base de datos en modo solo lectura
def conectar_db():
    conn = sqlite3.connect("file:textos.db?mode=ro", uri=True)  # Abrir la base en modo solo lectura
    return conn

# Función genérica para obtener una frase aleatoria de una tabla dada
def obtener_frase_aleatoria(conn, categoria):
    cursor = conn.cursor()
    cursor.execute(f"SELECT texto FROM {categoria} ORDER BY RANDOM() LIMIT 1;")
    resultado = cursor.fetchone()
    return resultado[0] if resultado else None

load_dotenv()
GIPHY_TOKEN=os.getenv('GIPHY_API_TOKEN')


class ComandosArgentinos(commands.Cog):
    """COG de comandos principales para el Bot"""
    def __init__(self, bot):
        self.bot = bot
        self.conn=conectar_db()

    def BuscarGifs(self, termino):
        """Método utilizado para la busqueda de Gifs"""
        url = "https://api.giphy.com/v1/gifs/search"
        parametros={
            "api_key": GIPHY_TOKEN,
            "q": termino,
            "limit": 1
        }
        respuesta=requests.get(url,params=parametros)

        if respuesta.status_code==200:
            datos=respuesta.json()
            if datos["data"]:
                return datos["data"][0]["images"]["original"]["url"]
        return None

    @commands.command(name="gif")
    async def gif(self, ctx, *, termino: str):
        gif_url=self.BuscarGifs(termino)
        if gif_url:
            await ctx.send(f"{termino}: {gif_url}")
        else:
            await ctx.send(f"No encontré ningún GIF de {termino}, che 😞")

    @commands.command(name='mate')
    async def mate(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Tenés que mencionarle a alguien para cebarle un mate!")
        else:
            await ctx.send(f"{ctx.author.display_name} le está cebando un mate a {member.display_name} 🧉")

    # TRABAJANDO

    # Responder con Gifs
    # Utilizacion de SqLite3
    
    @commands.command(name='che')
    async def che(self, ctx):
        trm="saludo"
        gif_url=self.BuscarGifs(trm)

        obtener_frase_aleatoria(self.conn,saludos)

        #frase = random.choice(textos.frases)
        #await ctx.send(frase)

    @commands.command(name='dicho')
    async def dicho(self, ctx):
        refran = random.choice(textos.dichos)
        await ctx.send(dichos)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        canal = discord.utils.get(member.guild.text_channels, name='general')
        if canal:
            await canal.send(f"Q ondaaa, {member.display_name}! Bienvenido al server Pá")
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:  # Evita que el bot procese sus propios mensajes
            return
        # Lógica de reacciones
        if "fernet" in message.content.lower() or "mate" in message.content.lower():
            await message.add_reaction("🧉")
        if "asado" in message.content.lower():
            await message.add_reaction("🍖")

# Agregar la función setup para registrar el Cog
async def setup(bot):
    print("Cog 'ComandosArgentinos' cargado.")  # Mensaje de debug
    await bot.add_cog(ComandosArgentinos(bot))
