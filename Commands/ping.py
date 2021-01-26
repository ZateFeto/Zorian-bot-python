import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

@commands.has_permissions(administrator=True)

class Ping(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx):
    await ctx.send('Pong!')

def setup(client):
  client.add_cog(Ping(client))