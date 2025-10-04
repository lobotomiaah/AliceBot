import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ O bot {bot.user} está online!")

async def load_commands():
    for filename in os.listdir("C:\\Users\\lobotomia\\Downloads\\AliceBot\\commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"commands.{filename[:-3]}")
            print(f"✔ Comando {filename} carregado!")

async def main():
    async with bot:
        await load_commands()
        await bot.start(TOKEN)

asyncio.run(main())
