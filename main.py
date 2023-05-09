import discord
import asyncio
from pytube import YouTube
from collections import deque
from discord.ext import commands
from config import config


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# Создаем пустую очередь треков
queue_of_music = deque()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = ctx.voice_client

    if not voice_client:
        await channel.connect()
        voice_client = ctx.voice_client

    try:
        video = YouTube(url)
        audio_url = video.streams.get_audio_only().url

        # Добавляем URL песни в очередь
        queue_of_music.append(url)

        # Если текущий трек не проигрывается, начинаем воспроизведение
        if not voice_client.is_playing():
            await play_song(ctx)

    except Exception as e:
        print(e)
        await ctx.send("Произошла ошибка при воспроизведении аудио.")

async def play_song(ctx):
    voice_client = ctx.voice_client

    if len(queue_of_music) == 0:
        # Если очередь пуста, завершаем воспроизведение
        # await voice_client.disconnect()
        return

    url = queue_of_music.popleft()
    video = YouTube(url)
    audio_url = video.streams.get_audio_only().url

    # Проигрываем текущий трек
    voice_client.play(discord.FFmpegPCMAudio(audio_url, executable="ffmpeg\\bin\\ffmpeg.exe"), after=lambda e: asyncio.run_coroutine_threadsafe(play_song(ctx), bot.loop))

@bot.command()
async def skip(ctx):
    voice_client = ctx.voice_client

    if voice_client.is_playing():
        # Пропускаем текущий трек

        voice_client.stop()
        await ctx.send("Текущий трек пропущен.")
    else:
        await ctx.send("В данный момент ничего не проигрывается.")

@bot.command()
async def resume(ctx):
    voice_client = ctx.voice_client

    if voice_client.is_paused():
        # Возобновляем проигрывание
        voice_client.resume()
        await ctx.send("Проигрывание возобновлено.")
    else:
        await ctx.send("В данный момент ничего не приостановлено.")

@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client

    if voice_client.is_playing() or voice_client.is_paused():
        # Останавливаем проигрывание и очищаем очередь
        voice_client.stop()
        queue_of_music.clear()
        await ctx.send("Проигрывание остановлено и очередь очищена.")
    else:
        await ctx.send("В данный момент ничего не проигрывается.")

@bot.command()
async def pause(ctx):
    voice_client = ctx.voice_client

    if voice_client.is_playing():
        # Приостанавливаем проигрывание
        voice_client.pause()
        await ctx.send("Проигрывание приостановлено.")
    else:
        await ctx.send("В данный момент ничего не проигрывается.")

@bot.command()
async def queue(ctx):
    # Отправляем сообщение с текущей очередью
    if len(queue_of_music) == 0:
        await ctx.send("Очередь пуста.")
    else:
        queue_list = "\n".join(queue_of_music)
        await ctx.send(f"Очередь песен:\n{queue_list}")

if __name__ == "__main__":
    bot.run("MTEwMzMzMTA5NTg5MTY5MzY1MQ.G-VPd6.D0SLWEC9S95UQcAJgD0tZor2t3NqL7tJ0uF9vA")