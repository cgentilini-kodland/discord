import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emodji

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def smile(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run("MTU1MzA3Njk4NDY5ODExMDA0NQ.GowIWU.vvMTG4j7Ih5VpEA9uR7dp0-PoxhZ5FSZqmP-MA")
