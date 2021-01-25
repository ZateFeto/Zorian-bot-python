import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

intents = discord.Intents(members = True)

class Example2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def yodawg(self, ctx, *, member: discord.Member = None):
      await ctx.send('here dawg.')
      member = member or ctx.author
      if self._last_member is None or self._last_member.id != member.id:
        await ctx.send('sup {0.mention} dawg~'.format(member))

def setup(bot):

    bot.add_cog(Example2(bot))
