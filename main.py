import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

from discord.ext.commands import Bot

def setup(bot):
    bot.add_cog(MembersCog(bot))

bot.add_cog(Greetings(bot))

load_extension(Greetings)


client = discord.Client()


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
