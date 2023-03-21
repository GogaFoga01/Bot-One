import discord
import Telegram

# Replace YOUR_TOKEN_HERE with your bot's token
TOKEN = 'Yor Token'# Токен бота Дискорда
intents = discord.Intents.all()
client = discord.Client(intents=intents)
CHANNEL_ID = 'CHANNEL_ID' # Указать ID канала с которого бот получает сообщения


@client.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID:
        return

    if message.content:
        author = message.author.name

        role_mention = message.role_mentions[0] if message.role_mentions else None
        role_name = role_mention.name if role_mention else "Не назначен"

        content = message.content.replace(role_mention.mention, "") if role_mention else message.content

        output = f"Состовитель: {author}\nИсполнитель: {role_name}\nТело Задачи: {content}"
        print(output)
        await Telegram.send_to_telegram(output)


client.run(TOKEN)
