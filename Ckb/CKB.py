#*********************************************************************************************************************************************************
import asyncio
from operator import index      #|
from posixpath import split     #|
from re import M                #|
from typing import Sized, Text
from urllib import response        #|
import discord                  #|
from discord import shard       #|
from discord import file
from discord import message        #|
from discord.colour import Color #|
from discord.embeds import Embed #|
from discord.ext import commands #|
from discord.utils import get
from matplotlib import image    #|
import requests                  #|
from bs4 import BeautifulSoup    #|
import praw                      #|
import os                        #|
import random                    #|
import json
from requests.models import Response    
import async_timeout
import asyncio                  #|
import datetime
import time
import random

#*********************************************************************************************************************************************************
path = os.path.dirname(os.path.abspath(__file__))+"/"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Prefix
client = commands.Bot(command_prefix = '+')
@client.command()
@commands.has_permissions(administrator=True)
async def delete(ctx,*,amount=5):
    await ctx.channel.purge(limit=amount)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Avatar#
@client.command()
async def avatar(ctx,member:discord.Member):
    embed = discord.Embed(color = discord.Color.dark_purple())
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name= "UU good avatar :wink: ",value=f"{member.display_name}") 
    embed.set_image(url="{}".format(member.avatar_url))
    await ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#kedi
@client.command()
async def kedi(ctx):
        response = requests.get('https://aws.random.cat/meow')
        kedii = response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'Uwuu :heart_eyes: ', value = "YwY :laughing: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=kedii['file'])  
        await  ctx.send(embed=embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def dog(ctx):
        Response = requests.get("https://dog.ceo/api/breeds/image/random")
        dog = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'UwU :heart_eyes: ', value = "YwY :laughing: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=dog['message'])
        await  ctx.send(embed=embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def cmd(ctx):
        embed = discord.Embed(title="Bot commands", description="You can used with prefix") #,color=Hex code
        
        embed.add_field(name=" :diamonds: delete", value="clear message")
        embed.add_field(name=" :diamonds: mute", value="muted some one")
        embed.add_field(name=" :diamonds: ban", value="banned some one")
       
        embed.add_field(name=" :large_blue_diamond: cat", value="send random cat image")
        embed.add_field(name=" :large_blue_diamond: dog", value="send random dog image")
        embed.add_field(name=" :large_blue_diamond: avatar", value="show avatar who u tagged")
        embed.add_field(name=" :large_blue_diamond: ball", value="ask some question to bot")
        
       
        embed.add_field(name=" :large_orange_diamond: kickk", value="kick some one")
        embed.add_field(name=" :large_orange_diamond: waifu", value="send random waifu image")
        embed.add_field(name=" :large_orange_diamond: neko", value="send random neko image")
        embed.add_field(name=" :large_orange_diamond: shinobu", value="send random shinobu image")
        embed.add_field(name=" :large_orange_diamond: bly", value="send random bully image")
        embed.add_field(name=":large_orange_diamond: hug", value="hug some one")
        embed.add_field(name=":large_orange_diamond: cry", value="cry :(")
        embed.add_field(name=":large_orange_diamond: kiss", value="kiss some one")
        embed.add_field(name=":large_orange_diamond: lick", value="lick some one")
        embed.add_field(name=":large_orange_diamond: pat", value="pat some one")
        embed.add_field(name=":large_orange_diamond: bonk", value="bonk some one")
        embed.add_field(name=":large_orange_diamond: blush", value="YwY")
        embed.add_field(name=":large_orange_diamond: smile", value="smile")
        embed.add_field(name=":large_orange_diamond: kick", value="kicked some one (gif)")

        await ctx.send(embed=embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def waifu(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/waifu")
        wafi = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=wafi['url'])  
        await  ctx.send(embed=embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def neko(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/neko")
        ne = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=ne['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def shinobu(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/shinobu")
        shinobu = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=shinobu['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def megumin(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/megumin")
        me = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=me['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def cry(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/cry")
        cr = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=cr['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def hug(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/hug")
        hg = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=hg['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def kiss(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/kiss")
        ks = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=ks['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def lick(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/lick")
        lc = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=lc['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def pat(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/pat")
        pt = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=pt['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------   
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def bonk(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/bonk")
        bon = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=bon['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def blush(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/blush")
        bl = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=bl['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command()
async def smile(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/smile")
        sm = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=sm['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command()
async def bly(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/bully")
        kc = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=bly['url'])  
        await  ctx.send(embed=embed)
@client.command()
async def kick(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/kick")
        kc = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=kc['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command()
async def dance(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/dance")
        dance = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=dance['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def wink(ctx):
        Response = requests.get("https://api.waifu.pics/sfw/wink")
        wk = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'uwu ', value = ":smile: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=wk['url'])  
        await  ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   await member.add_roles(mutedRole)
   await member.send(f" you have muted from: - {ctx.guild.name}")
   embed = discord.Embed(title="muted", description=f" muted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been baned from the server.')
@client.command()
@commands.has_permissions(ban_members=True)
async def kickk(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been baned from the server.')

@client.command(aliases=['8ball'])
async def ball(ctx, *, question):
  responses = [
  discord.Embed(title='It is certain.'),
  discord.Embed(title='It is decidedly so.'),
  discord.Embed(title='Without a doubt.'),
  discord.Embed(title='Yes - definitely.'),
  discord.Embed(title='You may rely on it.'),
  discord.Embed(title='Most likely.'),
  discord.Embed(title='Outlook good.'),
  discord.Embed(title='Yes.'),
  discord.Embed(title='Signs point to yes.'),
  discord.Embed(title='Reply hazy, try again.'),
  discord.Embed(title='Ask again later.'),
  discord.Embed(title='Better not tell you now.'),
  discord.Embed(title='Cannot predict now.'),
  discord.Embed(title='Concentrate and ask again.'),
  discord.Embed(title="Don't count on it."),
  discord.Embed(title='My reply is no.'),
  discord.Embed(title='My sources say no.'),
  discord.Embed(title='Outlook not very good.'),
  discord.Embed(title='Very doubtful.')
    ]
  responses = random.choice(responses)
  await ctx.send(content=f'Question: {question}\nAnswer:', embed=responses)
        
 
        

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
client.run('')