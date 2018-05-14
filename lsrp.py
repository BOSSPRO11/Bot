# lsrp

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='bot ')
cr = "Bot de BOSSPRO le super Dev  V1.0"

print (discord.__version__)

@bot.event
async def on_ready():
    print ("bot activé !")
    await bot.change_presence(game=discord.Game(name='Hacker Léane...'), status=discord.Status("online"))

@bot.event
async def on_member_join(member):
    channel = member.server.get_channel("445626330545913858")   # A RECONFIG
    embed = discord.Embed(title="OMG {0} viens d'arriver, on va s'amuser^^".format(member.name), color=0x77B255)
    embed.set_thumbnail(url="http://mowzy.fr/bot/in2.png")
    embed.set_footer(text=cr)
    await bot.send_message(channel, embed=embed)



@bot.command(pass_context=True)
async def mp(ctx):
    embed = discord.Embed(title="Salut tu est très intelligent et je te trouve magnifique", color=0x77B255)
    embed.set_footer(text=cr)
    le_user = ctx.message.author
    await asyncio.sleep(0.01)
    await bot.delete_message(ctx.message)
    await bot.send_message(le_user, embed=embed)



@bot.command(pass_context=True)
async def aurevoir(ctx):
    embed = discord.Embed(title="à demain {}, passes une bonne soirée poto !".format(ctx.message.author.name), color=0x77B255)
    embed.set_footer(text=cr)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def bonjour(ctx):
    embed = discord.Embed(title="Bonjour {} !".format(ctx.message.author.name), color=0x77B255)
    embed.set_footer(text=cr)
    await bot.say(embed=embed)





bot.run("") # A RECONFIG