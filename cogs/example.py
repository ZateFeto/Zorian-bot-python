import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

class Example(commands.Cog):

  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is surfing with ya.')

  # Commands
  @commands.command()
  async def uhere(self, ctx):
    await ctx.send('yeah im here bruv.')

def setup(client):
  client.add_cog(Example(client))