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
GIPHY_TOKEN = os.getenv('GIPHY_API_TOKEN')


class ComandosArgentinos(commands.Cog):
    """COG de comandos principales para el Bot"""
    def __init__(self, bot):
        self.bot = bot
        self.conn = conectar_db()

    def buscar_gifs(self, termino):
        """Método utilizado para la búsqueda de Gifs"""
        url = "https://api.giphy.com/v1/gifs/search"
        parametros = {
            "api_key": GIPHY_TOKEN,
            "q": termino,
            "limit": 1
        }
        respuesta = requests.get(url, params=parametros)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            if datos["data"]:
                return datos["data"][0]["images"]["original"]["url"]
        return None

    @commands.command(name='che')
    async def che(self, ctx):
        try:
            # Obtener frase de la base de datos
            frase = obtener_frase_aleatoria(self.conn, "frases")
            if not frase:
                frase = "No encontré ningún saludo, che 🤷‍♂️"

            # Obtener el GIF
            gif_url = self.buscar_gifs("Argentina")
            if not gif_url:
                gif_url = None  # Si no hay GIF, no se agrega al embed

            # Crear embed para enviar mensaje + GIF
            embed = discord.Embed(
                title="Qondaa!",
                description=frase,
                color=discord.Color.blue()
            )
            if gif_url:
                embed.set_image(url=gif_url)

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"Hubo un problema: {e}")

# Agregar la función setup para registrar el Cog
async def setup(bot):
    print("Cog 'ComandosArgentinos' cargado.")  # Mensaje de debug
    await bot.add_cog(ComandosArgentinos(bot))
