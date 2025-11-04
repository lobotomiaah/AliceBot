from discord.ext import commands
import typing
import wavelink

class music(commands.cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def 