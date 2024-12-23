import discord
from discord.ext import commands
import asyncio
from random import randint

# Criação do bot com prefixo '&'
intents = discord.Intents.default()
intents.message_content = True  # Permite que o bot leia o conteúdo das mensagens

# Prefixo que o bot vai ler os comandos ("&")
bot = commands.Bot(command_prefix="#", intents=intents)

# Saudacoes do bot ao ficar online
@bot.event
async def online():
    print('Bot online!')

# Comando de oi no servidor (&oi)
@bot.command()
async def oi(crtl):
    if crtl.author.display_name == 'nico':
        await crtl.send(f'Oiiiii mozinho!!!!!! Seu namorado ti mandou um beijo e disse que ama voce!')
    else:
        await crtl.send(f'Olá {crtl.author.display_name}!')

@bot.command()
async def thiago(self):
    await self.send("vai tomar no cu thiago")

@bot.command()
async def ajuda(dc):
    await dc.send('**#oi**: para receber Oi do nosso querido bot (Easter Egg se você for o Cesar)\n**roll (tipo de dado)**: Usado para rolar uma unidade de dado a escolha do usuário\n**#rolls (quantidade de dados) (tipo de dado) (adicional):** Usado para rolar múltiplos dados + adicionais se necessário. Lembre-se de sempre dar espaço entre as informações.\n**#thiago**: vai tomar no cu thiago')

# ----- DADOS -----
@bot.command()
async def roll(ctx, tipo: str):
    dados = {
        "d4": 4,
        "d6": 6,
        "d10": 10,
        "d20": 20,
        "d30": 30,
        "d50": 50,
        "d100": 100
    }
    if tipo not in dados:
        await ctx.send("Tipo de dado inválido! Escolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    dado_num = dados[tipo]
    dado_final = randint(1, dado_num)
    await ctx.send(f"Você jogou um {tipo}. Resultado: {dado_final}")

# Abaixo, uma função otimizada para rolar os dados, onde é fornecido o número de vezes que o dado sera rolado e o tipo dos dados que seram jogados
@bot.command()
async def rolls(ctx, vezes: int, tipo: str, adicional: int = 0):
    dados = {
        "d4": 4,
        "d6": 6,
        "d10": 10,
        "d20": 20,
        "d30": 30,
        "d50": 50,
        "d100": 100
    }

    if tipo not in dados:
        await ctx.send("Tipo de dado inválido! Escolha entre: d4, d6, d10, d20, d30, d50 ou d100.")
        return
    if vezes <= 0:
        await ctx.send("O número de dados lançados não pode ser igual a zero")
        return

    dado_num = dados[tipo]

    # Rolls!
    resultados = [randint(1, dado_num) for _ in range(vezes)]
    resultados_formatados = "\n".join(f"{i+1} - {resultado}" for i, resultado in enumerate(resultados))
    resultados_final = sum(resultados) + adicional

    if adicional == 0:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\nResultado: {resultados_final}")
    else:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\n Resultado ( + {adicional} ): {resultados_final}")
    
bot.run('INSIRA SEU TOKEN AQUI')