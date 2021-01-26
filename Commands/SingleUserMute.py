import discord, os
from discord.ext import commands

@commands.has_permissions(administrator=True)

class SUserM(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vcmute(self, ctx, user: discord.Member, *, reason="No reason provided"):
        await user.edit(mute=True)
        await ctx.send(f"Successfully muted {user}!")

def setup(client):
  client.add_cog(SUserM(client))
