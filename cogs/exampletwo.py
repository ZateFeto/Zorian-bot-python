import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

class Greet(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.command()
  async def sayit(self, ctx):
    await ctx.send('no i wont!')

def setup(client):
  client.add_cog(Greet(client))