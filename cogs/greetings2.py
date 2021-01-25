import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

class Greetings2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
        if msg.startswith('~hello'):
            await message.channel.send('Hello!')


    @commands.command()
        if msg.startswith('~hello'):
            await message.channel.send('Hello!')


def setup(bot):

    bot.add_cog(Greetings2(bot))

