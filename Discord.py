import discord
import Telegram

# Replace YOUR_TOKEN_HERE with your bot's token
TOKEN = "MTA4NjE5OTM5NzU5Mjg1ODY0NA.GpEFVQ.IaDiPsm-k2VTYLI2flTeaYEIC5CcGE5GkQX4Q0"
intents = discord.Intents.all()
client = discord.Client(intents=intents)
CHANNEL_ID = 1086194776111579310


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
        await main.send_to_telegram(output)


client.run(TOKEN)
