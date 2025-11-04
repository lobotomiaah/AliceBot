from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx: commands.Context, operacao: str = None, num1: str = None, num2: str = None):
        
        if not operacao or not num1 or not num2:
            await ctx.reply("Uso correto: `.calc <operacao> <num1> <num2>`\nExemplo: `.calc soma 10 5`")
            return
        
      
        try:
            num1 = float(num1.replace(",", "."))
            num2 = float(num2.replace(",", "."))
        except ValueError:
            await ctx.reply("Você precisa digitar números válidos!")
            return

        resultado = None
        operacao = operacao.lower()

        
        if operacao == "soma":
            resultado = num1 + num2
        elif operacao == "sub":
            resultado = num1 - num2
        elif operacao == "multi":
            resultado = num1 * num2
        elif operacao == "div":
            if num2 != 0:
                resultado = num1 / num2
            else:
                await ctx.reply("Não é possível dividir por zero!")
                return
        else:
            await ctx.reply("Operação inválida! Use: soma, sub, multi, div")
            return

        await ctx.reply(f"Resultado é {resultado}")

async def setup(bot):
    await bot.add_cog(Calculator(bot))
