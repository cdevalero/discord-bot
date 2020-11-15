import discord
from discord import guild
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='This is my bot')

@bot.command()
async def ping(word):
    await word.send('Hola ricardo')

@bot.command()
async def sum(word, numOne: int, numTwo: int):
    await word.send(numOne + numTwo)

@bot.command()
async def info(word):
    embed = discord.Embed(title=f'{word.guild.name}', description='Hola a todos a mi prueba de bost', color=discord.Color.blue())
    await word.send(embed=embed)

@bot.event
async def on_ready():
    print('Im ready')


bot.run('')