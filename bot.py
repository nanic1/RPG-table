import discord
from discord.ext import commands
import asyncio
from random import randint

# Variaveis necessarias para o código
dado4 = randint(1, 4)
dado6 = randint(1, 6)
dado10 = randint(1, 10)
dado20 = randint(1, 20)
dado30 = randint(1, 30)
dado50 = randint(1, 50)
dado100 = randint(1, 100)

# Criação do bot com prefixo '&'
intents = discord.Intents.default()
intents.message_content = True  # Permite que o bot leia o conteúdo das mensagens

# Prefixo que o bot vai ler os comandos ("&")
bot = commands.Bot(command_prefix="&", intents=intents)

# Saudacoes do bot ao ficar online
@bot.event
async def online():
    print('Bot online!')

# Comando de oi no servidor (&oi)
@bot.command()
async def oi(crtl):
    if crtl.author.display_name == 'nico':
        await crtl.send(f'Ola {crtl.author.display_name}!!! Seu namorado ti mandou um beijo e disse que ama voce!')
    else:
        await crtl.send(f'Ola {crtl.author.display_name}!')

@bot.command()
async def ajuda(dc):
    await dc.send(f'**&oi**: para receber Oi do nosso querido bot\n**&rolar (quantidade de dados) (tipo de dados) (adicional):** Usado para rolar vários dados + adicionais se necessário. Lembre-se de sempre dar espaço entre as informações.')

# ----- DADOS -----
# Abaixo, uma função otimizada para rolar os dados, onde é fornecido o número de vezes que o dado sera rolado e o tipo dos dados que seram jogados
@bot.command()
async def rolar(ctx, vezes: int, tipo: str, adicional: int = 0):
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

    # Número máximo de faces do dado
    dado_num = dados[tipo]

    # Realizando as rolagens
    resultados = [randint(1, dado_num) for _ in range(vezes)]
    resultados_formatados = "\n".join(f"{i+1} - {resultado}" for i, resultado in enumerate(resultados))
    resultados_final = sum(resultados) + adicional

    if adicional == 0:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\nResultado: {resultados_final}")
    else:
        await ctx.send(f"Você rolou {vezes} dados {tipo}.\n{resultados_formatados}\n\n Resultado ( + {adicional} ): {resultados_final}")
    
bot.run('INSIRA SEU TOKEN AQUI')