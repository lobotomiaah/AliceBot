from discord.ext import commands
import random

class PiadaDeTio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.piadas = [
            "Por que o computador foi ao médico? Porque ele tinha um vírus!",
            "Você conhece a piada da escalada? Ah não, melhor não ─ talvez você suba!",
            "Qual é o cúmulo da rapidez? Correr tanto que a sombra cansou!",
            "Você conhece a piada do pônei? Pô nei eu.",
            "Você sabe qual é o rei dos queijos?  O reiqueijão.",
            "Qual o nome do telefone que fica no meio do mato? Telegrama.",
            "Qual é o idoso matemático que joga futsal? O pivô!"
        ]

    @commands.command(name="piadadetio")
    async def piadadetio(self, ctx: commands.Context, *, adicional: str = None):
        """Envia uma piada de tio aleatória. Se quiser, pode adicionar algo extra."""
        piada_escolhida = random.choice(self.piadas)
        if adicional:
            piada_escolhida += f" + {adicional}"
        await ctx.reply(piada_escolhida)

async def setup(bot):
    await bot.add_cog(PiadaDeTio(bot))
