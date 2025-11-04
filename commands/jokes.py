from discord.ext import commands
import random

class joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def piadadetio(self, ctx: commands.Context, piada: str = None):
        await ctx.reply(print(random.choice("teste")))