import os, sys, discord, platform, random, aiohttp, json, asyncio, requests
from discord.ext import commands
from replit import db

@commands.has_permissions(administrator=True)

class BotStatus(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def BSGame(self, ctx, *, botgamestatus):
    await self.client.change_presence(activity=discord.Game(f"{botgamestatus}"))

  @commands.command()
  async def BSWatching(self, ctx, *, botwatchingstatus):
    activity = discord.Activity(name=(f"{botwatchingstatus}"), type=discord.ActivityType.watching)
    await self.client.change_presence(activity=activity)
  
def setup(client):
  client.add_cog(BotStatus(client))

  # status=discord.Status.online, fel awel
  # BotPlayingWhat = []
