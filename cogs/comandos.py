import discord
from discord.ext import commands
import random
from scripts import textos  # Asegúrate de que 'textos' esté en un módulo llamado 'scripts' o ajusta esta importación.

class ComandosArgentinos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(name='mate')
    async def mate(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("¡Tenés que mencionarle a alguien para cebarle un mate!")
        else:
            await ctx.send(f"{ctx.author.display_name} le está cebando un mate a {member.display_name} 🍵")

    @commands.command(name='che')
    async def che(self, ctx):
        frase = random.choice(textos.frases)
        await ctx.send(frase)

    @commands.command(name='dicho')
    async def dicho(self, ctx):
        refran = random.choice(textos.refranes)
        await ctx.send(refran)




    @commands.Cog.listener()
    async def on_member_join(self, member):
        canal = discord.utils.get(member.guild.text_channels, name='general')
        if canal:
            await canal.send(f"Q ondaaa, {member.display_name}! Bienvenido al server Pá")
"""
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:  # Evita que el bot procese sus propios mensajes
            return
        # Lógica de reacciones
        if "fernet" in message.content.lower() or "mate" in message.content.lower():
            await message.add_reaction("🧉")
        if "asado" in message.content.lower():
            await message.add_reaction("🍖")

        await self.bot.process_commands(message)  # Asegura el procesamiento de comandos
"""

# Agregar la función setup para registrar el Cog
async def setup(bot):
    print("Cog 'ComandosArgentinos' cargado.")  # Mensaje de debug
    await bot.add_cog(ComandosArgentinos(bot))
