import typing
import discord
from discord.ext import commands

def create_overwrites(ctx, *objects):
    overwrites = {obj: discord.PermissionOverwrite(view_channel=True) for obj in objects}
    overwrites.setdefault(ctx.guild.default_role, discord.PermissionOverwrite(view_channel=False))
    overwrites[ctx.guild.me] = discord.PermissionOverwrite(view_channel=True)
    return overwrites

class SecretCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(hidden=True)
    async def secret(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.send('cayate amigo!', delete_after=5)

    @secret.command()
    @commands.guild_only()
    async def text(self, ctx: commands.Context, name: str, *objects: typing.Union[discord.Role, discord.Member]):
        overwrites = create_overwrites(ctx, *objects)
        await ctx.guild.create_text_channel(
            name,
            overwrites=overwrites,
            topic='Top secret text channel. Any leakage of this channel may result in serious trouble.',
            reason='Este canal es privado pá, ojo con lo q decís.',
        )

    @secret.command()
    @commands.guild_only()
    async def voice(self, ctx: commands.Context, name: str, *objects: typing.Union[discord.Role, discord.Member]):
        overwrites = create_overwrites(ctx, *objects)
        await ctx.guild.create_voice_channel(
            name,
            overwrites=overwrites,
            reason='Este canal es privado pá, ojo con lo q hablas.',
        )

    @secret.command()
    @commands.guild_only()
    async def emoji(self, ctx: commands.Context, emoji: discord.PartialEmoji, *roles: discord.Role):
        emoji_bytes = await emoji.read()
        await ctx.guild.create_custom_emoji(
            name=emoji.name,
            image=emoji_bytes,
            roles=roles,
            reason='Eu, este emoji es privado, te aviso nomás',
        )
