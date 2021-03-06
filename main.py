import os, sys, discord, platform, random, aiohttp, json, asyncio
from discord.ext import commands
from replit import db
from keep_alive import keep_alive

from discord import voice_client

intents = discord.Intents.all()

client = commands.Bot(command_prefix = os.getenv('BOT_PREFIX'))
# bot = commands.Bot(command_prefix = os.getenv('BOT_PREFIX'))

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  client.load_extension(f'Commands.{extension}')
  client.load_extension(f'Music.{extension}')

@client.command()
async def unload(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  client.load_extension(f'Commands.{extension}')
  client.load_extension(f'Music.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('./Commands'):
  if filename.endswith('.py'):
    client.load_extension(f'Commands.{filename[:-3]}')

for filename in os.listdir('./Music'):
  if filename.endswith('.py'):
    client.load_extension(f'Music.{filename[:-3]}')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


keep_alive()
client.run(os.getenv('BOT_TOKEN'))
