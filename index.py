import discord
from discord import guild
from discord.ext import commands
from api import *

bot = commands.Bot(command_prefix='!', description='This is my bot')

@bot.command()
async def hi(word):
    await word.send('Hola!')

@bot.command()
async def bitcoin(word):
    price = getPrice()
    date = getDate()
    coin = getCoin()
    embed = discord.Embed(title=date, description=coin+' '+price, color=discord.Color.blue())
    await word.send(embed=embed)

@bot.event
async def on_ready():
    print('Im ready')


bot.run('')
