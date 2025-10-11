import sqlite3
import os
import re
from discord.ext import commands

DB_DIR = "database"
DB_PATH = os.path.join(DB_DIR, "rpg.db")

def get_connection():
    os.makedirs(DB_DIR, exist_ok=True)
    return sqlite3.connect(DB_PATH)

class Personagens(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._create_table()

    def _create_table(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fichas (
                usuario_id INTEGER,
                nome TEXT,
                classe TEXT,
                persona TEXT,
                nivel INTEGER DEFAULT 1,
                xp INTEGER DEFAULT 0,
                PRIMARY KEY (usuario_id, nome)
            )
        ''')
        conn.commit()
        conn.close()

    @commands.command(name="criar_ficha")
    async def criar_ficha(self, ctx, nome: str, classe: str, persona: str):
        if not nome or not classe or not persona:
            await ctx.reply("Uso: `.criar_ficha <nome> <classe> <persona>`")
            return

        if nome.strip().isdigit():
            await ctx.reply("Erro: o nome não pode ser apenas números.")
            return

        if len(nome) > 50 or len(classe) > 30 or len(persona) > 30:
            await ctx.reply("Erro: nome/classe/persona muito longos.")
            return

        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO fichas (usuario_id, nome, classe, persona) VALUES (?, ?, ?, ?)",
                (ctx.author.id, nome.strip(), classe.strip(), persona.strip())
            )
            conn.commit()
            await ctx.reply(f"Personagem **{nome}** criado com sucesso! (Nível: 1, XP: 0)")

        except sqlite3.IntegrityError:
            await ctx.reply(f"Erro: Já existe um personagem com o nome **{nome}** para este usuário.")
        except sqlite3.Error as e:
            await ctx.reply(f"Ocorreu um erro no banco de dados:\n```{e}```")
        except Exception as e:
            await ctx.reply(f"Erro inesperado:\n```{e}```")
        finally:
            if conn:
                conn.close()

    @criar_ficha.error
    async def criar_ficha_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Uso correto: `.criar_ficha <nome> <classe> <persona>`\nExemplo: `.criar_ficha Alice Arqueira Aeon`")
        else:
            await ctx.reply(f"Erro ao processar o comando:\n```{error}```")

async def setup(bot):
    await bot.add_cog(Personagens(bot))
