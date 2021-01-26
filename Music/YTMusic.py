import discord
from discord.ext import commands

...

client = commands.Bot(command_prefix="!")
@client.command(pass_context=True)
async def play_youtube_url(self, ctx, youtube_url):
    channel = ctx.message.author.voice.voice_channel 
    # http://discordpy.readthedocs.io/en/latest/api.html#discord.Member.voice
    # http://discordpy.readthedocs.io/en/latest/api.html#discord.VoiceState.voice_channel
    if youtube_url.startswith('https://www.youtube.com/watch?v='):
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player(youtube_url)
        player.start()
    else:
        return 'URL_ERROR'

...

client.run("token")