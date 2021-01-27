import discord, os
from discord.ext import commands

# intents = discord.Intents.all()

@commands.has_permissions(administrator=True)

class SUserM(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vcmute(self, ctx, user: discord.Member, *, reason="No reason provided"):
      if not user.voice.mute:
        await user.edit(mute=True)
        await ctx.send(f"Successfully muted {user}!")
      elif user.voice.mute:
        await ctx.send(f"{user} is already muted!")
      elif ctx is None:
        await ctx.send(f"Who do you want to mute?")
      elif user.voice_state is None:
        await ctx.send(f"{user} is not in a voice channel!")

    @commands.command()
    async def vcunmute(self, ctx, user: discord.Member, *, reason="No reason provided"):
      if user.voice.mute:
        await user.edit(mute=False)
        await ctx.send(f"Successfully unmuted {user}!")
      elif not user.voice.mute:
        await ctx.send(f"{user} is already unmuted!")
      elif ctx is None:
        await ctx.send(f"Who do you want to mute?")
      elif user.voice_state is None:
        await ctx.send(f"{user} is not in a voice channel!")

def setup(client):
  client.add_cog(SUserM(client))
