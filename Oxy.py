import discord
from discord.ext import commands, tasks

# Ваш токен бота
TOKEN = 'ваш_токен_бота'

# Префикс для команд бота
PREFIX = '!'

# Создаем объект клиента
bot = commands.Bot(command_prefix=PREFIX)

# Функция для отправки новости в виде embed
async def send_news(channel_id, news_content):
    channel = bot.get_channel(channel_id)
    
    embed = discord.Embed(
        title="Новость от JuniperBot",
        description=news_content,
        color=discord.Color.blue()
    )
    
    await channel.send(embed=embed)

# Команда для отправки новостей
@bot.command()
async def send(ctx, channel_id: int, *, news_content):
    await send_news(channel_id, news_content)

# Обработка события подключения к Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Запускаем бота
bot.run(TOKEN)
