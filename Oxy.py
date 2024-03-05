import discord
from discord.ext import commands, tasks

# Ваш токен бота
TOKEN = 'MTIxNDY5NDIwNDk5MTYwNjkyNQ.GRxE35.ox9CqE0fVbDCdYwdkbf4xrRsFiNz-YLUwHzXQc'

# Префикс для команд бота
PREFIX = '!'

# Создаем объект клиента
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

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

