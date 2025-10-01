import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".",intents=intents)
@bot.event
async def on_ready():
    print("o bot esta pronto")
@bot.command()
async def calc(ctx:commands.Context,operacao:str, num1:str, num2:str):
    if not operacao or not num1 or not num2:
         await ctx.reply("Uso correto: `.calc <operacao> <num1> <num2>`\nExemplo: `.calc soma 10 5`")
         return
    try:
        num1 = float(num1.replace(",","."))
        num2 = float(num2.replace(",","."))
    except ValueError:
        await ctx.reply("Voce precisa digitar numeros validos!")
        return
    resultado = None    
    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "sub":
        resultado = num1 - num2
    elif operacao == "multi":
        resultado = num1 * num2
    elif operacao == "div":
        if num2 !=0:
         resultado = num1 / num2
        else:
             await ctx.reply("não é possivel dividir por zero")
             return
    else:
       await ctx.reply("Operação inválida! Use: soma, sub, multi, div")
       return
    await ctx.reply(f"Resultado é {resultado}")



   

    

bot.run("MTQyMjcyNDE0ODcxMDQ3Mzc3MA.GnflN7.92CWXwXZoH0Rvz6DssetnthpSQquVa5i8hXfM4")