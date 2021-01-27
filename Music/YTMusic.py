import discord, os, platform, random, aiohttp, json, asyncio, youtube_dl
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

@commands.has_permissions(administrator=True)

# players = {}

class YTMB(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Zjoin(self, ctx):
      await ctx.message.author.voice.channel.connect()

    @commands.command()
    async def Zleave(self, ctx):
      guild = ctx.message.guild
      voice_client = guild.voice_client
      await voice_client.disconnect()

    @commands.command(pass_context=True)       
    async def Zplay(self, ctx, url):
      
        if not ctx.message.author.voice:
            await ctx.send('you are not connected to a voice channel')
            return

        else:
            channel = ctx.message.author.voice.channel

        voice_client = await channel.connect()

        guild = ctx.message.guild
        ydl_opts = {
          'format': 'bestaudio/best',
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': 'mp3',
              'preferredquality': '192',
              }],
        }   

        def endSong(guild, path):
            os.remove(path) 
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file = ydl.extract_info(url, download=True)
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

        await ctx.send(f'**Music: **{url}')

        while voice_client.is_playing():
            await asyncio.sleep(1)
        else:
            await voice_client.disconnect()
            print("Disconnected")

def setup(client):
  client.add_cog(YTMB(client))
