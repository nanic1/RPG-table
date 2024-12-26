import discord
from discord.ext import commands
import asyncio
from random import randint

# Criação do bot com prefixo '#'
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  

# Prefixo que o bot vai ler os comandos ("&")
bot = commands.Bot(command_prefix="#", intents=intents)

# Saudacoes do bot ao ficar online
@bot.event
async def on_ready():
    print('Bot online!')

# Comando de oi no servidor (#oi)
@bot.command()
async def oi(crtl):
    if crtl.author.id == 812475243603296267:
        await crtl.send('Oiiiii mozinho!!!!!! Seu namorado ti mandou um beijo e disse que ama voce!')
    elif crtl.author.id == 241603673745129472:
        await crtl.message.add_reaction("👑")
    elif crtl.author.id == 204655068434268160:
        await crtl.send("valeu thiago tmj thiago 👍👍👍")
    else:
        await crtl.send(f'Olá {crtl.author.display_name}!')

@bot.command()
async def thiago(self):
    await self.send("vai tomar no cu thiago")

@bot.command()
async def ajuda(dc):
    await dc.send(
        "**#oi**: para receber Oi do nosso querido bot\n"
        "**roll (tipo de dado)**: Usado para rolar uma unidade de dado a escolha do usuário\n"
        "**#rolls (quantidade de dados) (tipo de dado) (adicional):** Usado para rolar múltiplos dados + adicionais se necessário. Lembre-se de sempre dar espaço entre as informações.\n"
        "**#hrolls** (igual **#rolls**): Usado para rolar múltiplos dados e filtrar apenas o maior resultado + adicional caso seja declarado.\n"
        "**#lrolls** (igual **#rolls**): Usado para rolar múltiplos dados e filtrar apenas o menor resultado + adicional caso seja declarado.\n"
        "**#thiago**: ..."
        )

# ----- DADOS -----

# Roll
@bot.command()
async def roll(ctx, tipo: str = None):
    dados = {
        "d4": 4,
        "d6": 6,
        "d10": 10,
        "d20": 20,
        "d30": 30,
        "d50": 50,
        "d100": 100
    }
    if tipo is None:
        await ctx.send("Para usar o comando **#roll**, você precisa informar apos o comando o tipo de dado que você quer lançar.\nEscolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    if tipo not in dados:
        await ctx.send("Tipo de dado inválido! Escolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    dado_num = dados[tipo]
    dado_final = randint(1, dado_num)
    await ctx.send(f"Você jogou um {tipo}. Resultado: {dado_final}")
        
# Abaixo, uma função otimizada para rolar os dados, onde é fornecido o número de vezes que o dado sera rolado e o tipo dos dados que seram jogados

# Rolls
@bot.command()
async def rolls(ctx, vezes: int, tipo: str = None, adicional: int = 0):
    dados = {
        "d4": 4,
        "d6": 6,
        "d10": 10,
        "d20": 20,
        "d30": 30,
        "d50": 50,
        "d100": 100
    }
    if vezes <= 0:
        await ctx.send("O número de dados lançados não pode ser igual a zero")
        return
    if tipo is None:
        await ctx.send("Para usar o comando **#rolls**, você precisa informar apos o comando a quantidade de dados que você quer jogar, o tipo de dado que você quer lançar e se for necessário, a quantidade de adicional que você quer que adicione ao resultado total.\nEscolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    if tipo not in dados:
        await ctx.send("Tipo de dado inválido!\nEscolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    
    dado_num = dados[tipo]

    resultados = [randint(1, dado_num) for _ in range(vezes)]
    resultados_formatados = "\n".join(f"{i+1} - {resultado}" for i, resultado in enumerate(resultados))
    resultados_final = sum(resultados) + adicional

    if adicional == 0:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\nResultado: {resultados_final}")
    else:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\n Resultado ( + {adicional} ): {resultados_final}")

@rolls.error
async def rolls_erro (dc, erro):
    if isinstance(erro, commands.MissingRequiredArgument):
        await dc.send("Para usar o comando **#rolls**, você precisa informar apos o comando a quantidade de dados que você quer jogar, o tipo de dado que você quer lançar e se for necessário, a quantidade de adicional que você quer que adicione ao resultado total.\nEscolha entre: d4, d6, d10, d20, d30, d50 ou d100.\n\nExemplo:\n\n**#rolls** 2 d20 3\n\nResposta:\n\nVocê rolou 2 dados d20\n1 - x\n2 - y\n\nResultado ( + 3 ): z")
    else:
        await dc.send("Ocorreu um erro ao executar o comando. Verifique o formato digitando **#rolls**.")


@bot.command()
async def hrolls(ctx, vezes: int, tipo: str = None, adicional: int = 0):
    dados = {
        "d4": 4,
        "d6": 6,
        "d10": 10,
        "d20": 20,
        "d30": 30,
        "d50": 50,
        "d100": 100
    }
    if vezes <= 0:
        await ctx.send("O número de dados lançados não pode ser igual a zero")
        return
    if tipo is None:
        await ctx.send("Para usar o comando **#hrolls**, você precisa informar apos o comando a quantidade de dados que você quer jogar, o tipo de dado que você quer lançar e se for necessário, a quantidade de adicional que você quer que adicione ao resultado total.\nEscolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    if tipo not in dados:
        await ctx.send("Tipo de dado inválido!\nEscolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    
    dado_num = dados[tipo]

    resultados = [randint(1, dado_num) for _ in range(vezes)]
    resultados_formatados = "\n".join(f"{i+1} - {resultado}" for i, resultado in enumerate(resultados))
    resultados_final = max(resultados) + adicional

    if adicional == 0:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\nResultado: {resultados_final}")
    else:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\n Resultado ( + {adicional} ): {resultados_final}")

@hrolls.error
async def hrolls_erro (dc, erro):
    if isinstance(erro, commands.MissingRequiredArgument):
        await dc.send(
            "Para usar o comando **#hrolls**, você precisa informar após o comando a quantidade de dados que você quer jogar, o tipo de dado que você quer lançar e se for necessário, a quantidade de adicional que você quer que adicione ao **maior dado** tirado entre os jogados.\n"
            "Escolha entre: d4, d6, d10, d20, d30, d50 ou d100.\n\n"
            "Exemplo:\n\n"
            "**#highrolls** 2 d20 3\n\n"
            "Resposta:\n\n"
            "Você rolou 2 dados d20\n"
            "1 - x\n"
            "2 - y\n\n"
            "Resultado ( + 3 ): z"
            )
    else:
        await dc.send("Ocorreu um erro ao executar o comando. Verifique o formato digitando **#hrolls**.")

@bot.command()
async def lrolls(ctx, vezes: int, tipo: str = None, adicional: int = 0):
    dados = {
        "d4": 4,
        "d6": 6,
        "d10": 10,
        "d20": 20,
        "d30": 30,
        "d50": 50,
        "d100": 100
    }
    if vezes <= 0:
        await ctx.send("O número de dados lançados não pode ser igual a zero")
        return
    if tipo is None:
        await ctx.send("Para usar o comando **#lrolls**, você precisa informar apos o comando a quantidade de dados que você quer jogar, o tipo de dado que você quer lançar e se for necessário, a quantidade de adicional que você quer que adicione ao menor dado tirado entre os jogados.\nEscolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    if tipo not in dados:
        await ctx.send("Tipo de dado inválido!\nEscolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    
    dado_num = dados[tipo]

    resultados = [randint(1, dado_num) for _ in range(vezes)]
    resultados_formatados = "\n".join(f"{i+1} - {resultado}" for i, resultado in enumerate(resultados))
    resultados_final = min(resultados) + adicional

    if adicional == 0:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\nResultado: {resultados_final}")
    else:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\n Resultado ( + {adicional} ): {resultados_final}")


@lrolls.error
async def lrolls_erro(ctx, erro):
    if isinstance(erro, commands.MissingRequiredArgument):
        await ctx.send(
            "Para usar o comando **#lrolls**, você precisa informar após o comando a quantidade de dados que você quer jogar, o tipo de dado que você quer lançar e se for necessário, a quantidade de adicional que você quer que adicione ao **menor dado** tirado entre os jogados.\n"
            "Escolha entre: d4, d6, d10, d20, d30, d50 ou d100.\n\n"
            "Exemplo:\n\n"
            "**#highrolls** 2 d20 3\n\n"
            "Resposta:\n\n"
            "Você rolou 2 dados d20\n"
            "1 - x\n"
            "2 - y\n\n"
            "Resultado ( + 3 ): z"
            )
    else:
        await ctx.send("Ocorreu um erro ao executar o comando. Verifique o formato digitando **#lrolls**.")


bot.run('INSIRA SEU TOKEN AQUI')