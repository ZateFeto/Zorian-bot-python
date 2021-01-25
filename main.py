import os, sys, discord, platform, random, aiohttp, json, requests
from discord.ext import commands
from replit import db
from keep_alive import keep_alive

from discord.ext.commands import Bot

# bot.load_extension('cogs.greetings')

client = discord.Client()

bot = discord.ext.commands.Bot(command_prefix = "$");

bot.load_extension('cogs.greetings')
bot.load_extension('cogs.greetings2')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('~hello'):
    await message.channel.send('Hello!')

keep_alive()
client.run(os.getenv('BOT_TOKEN'))
