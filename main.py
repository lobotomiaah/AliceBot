import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".",intents=intents)
@bot.event
async def on_ready():
    print("o bot esta pronto")
@bot.command()
async def oi(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"oi {nome}")

bot.run("MTQyMjcyNDE0ODcxMDQ3Mzc3MA.GnflN7.92CWXwXZoH0Rvz6DssetnthpSQquVa5i8hXfM4")
