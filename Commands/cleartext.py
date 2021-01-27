import os, sys, discord, platform, random, aiohttp, json, asyncio
from discord.ext import commands

@commands.has_permissions(administrator=True)

class ClearText(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def TClear(self, ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    if amount == 1:
      await ctx.send(f'{amount} Message was deleted')
      await asyncio.sleep(5)
      await ctx.channel.purge(limit=1)
    else:
      await ctx.send(f'{amount} Messages were deleted')
      await asyncio.sleep(5)
      await ctx.channel.purge(limit=1)
      
def setup(client):
  client.add_cog(ClearText(client))