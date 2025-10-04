import sqlite3
from discord.ext import commands

class Criar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="criar_ficha")
    async def criar_ficha(self, ctx, nome: str, classe: str,persona:str, nivel: int = 1):
        try:
            conn = sqlite3.connect("rpg.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO fichas (usuario_id, nome, classe) VALUES (?, ?, ?, ?)",
                (ctx.author.id, nome, classe, persona)
            )
            conn.commit()
            await ctx.reply(f"Personagem {nome} criado com sucesso!") 
        except Exception :
            await ctx.reply(f"Uso correto:`.criar_ficha <nome> <classe> <persona>`\nExemplo:`.criar_ficha alice arqueira Aeon")
        finally:
            conn.close()

async def setup(bot):
    await bot.add_cog(Criar(bot))
