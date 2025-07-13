import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import os
from dotenv import load_dotenv
load_dotenv()



FFMPEG_EXECUTABLE = r"C:\ffmpeg\bin\ffmpeg.exe"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="@", intents=intents)

queues = {}

async def connect_to_voice_channel(ctx):
    """Conecta al canal de voz del usuario."""
    channel = ctx.author.voice.channel
    voice_client = await channel.connect()
    return voice_client

@bot.command()
async def play(ctx, *, url):
    """Reproduce música desde un enlace de YouTube."""
    if ctx.author.voice is None:
        await ctx.send("¡Necesitas unirte a un canal de voz primero!")
        return

    voice_client = ctx.voice_client

    if voice_client is None:
        voice_client = await connect_to_voice_channel(ctx)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'loglevel': 'error',
        'default_search': 'ytsearch',
        'noplaylist': True
    }

    try:
        loading_msg = await ctx.send("⏳ Ten paciencia, estoy procesando tu cancion...")

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']
            title = info.get('title', 'Sin título')

        ffmpeg_opts = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

        source = discord.FFmpegPCMAudio(audio_url, executable=FFMPEG_EXECUTABLE, **ffmpeg_opts)
        voice_client.play(source, after=lambda e: print('Song finished'))

        await ctx.send(f"🎵 Reproduciendo: {title}")

    except Exception as e:
        await ctx.send(f"Hubo un error al intentar reproducir la canción: {e}")

@bot.command()
async def pause(ctx):
    """Pausa la música."""
    if ctx.voice_client is None:
        await ctx.send("No estoy reproduciendo música.")
        return

    ctx.voice_client.pause()
    await ctx.send("Música pausada.")

@bot.command()
async def resume(ctx):
    """Reanuda la música."""
    if ctx.voice_client is None:
        await ctx.send("No estoy reproduciendo música.")
        return

    ctx.voice_client.resume()
    await ctx.send("Música reanudada.")

@bot.command()
async def stop(ctx):
    """Detiene la música y desconecta al bot."""
    if ctx.voice_client is None:
        await ctx.send("No estoy reproduciendo música.")
        return

    ctx.voice_client.stop()
    await ctx.voice_client.disconnect()
    await ctx.send("Desconectado del canal de voz.")

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="🎧 Soy el MVP del sonido. Si vas a poner música, que sea con clase. Déjamelo a mí.🎵"
        ),
        status=discord.Status.online
    )
    print(f'Bot conectado como {bot.user}')



bot.run(os.getenv("DISCORD_TOKEN"))


