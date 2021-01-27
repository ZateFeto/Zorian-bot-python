import os, sys, discord, platform, random, aiohttp, json, asyncio
from discord.ext import commands

@commands.has_permissions(administrator=True)

class ShowPFP(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def PFP(self, ctx, user: discord.Member):
    await ctx.send(user.avatar_url)
      
def setup(client):
  client.add_cog(ShowPFP(client))