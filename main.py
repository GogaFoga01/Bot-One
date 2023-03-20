import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '5753731786:AAHh7dSDsqgWKJsPJNttUKZvY87Fw6zy3Lc'
CHAT_ID = 570109198 # Chat ID of the user who will receive the messages
DISCORD_BOT_URL = 'https://discord.com/api/oauth2/authorize?client_id=1086199397592858644&permissions=8&scope=bot' # https://discord.com/api/oauth2/authorize?client_id=1086199397592858644&permissions=8&scope=bot

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def send_discord_output():
    while True:
        try:
            # Send GET request to the Discord bot's URL to get the latest output
            response = requests.get(DISCORD_BOT_URL)
            output = response.text

            # Send the output to the user
            await bot.send_message(chat_id=CHAT_ID, text=output)

            # Wait for 10 seconds before checking for new output
            await asyncio.sleep(100)

        except Exception as e:
            logging.error(f"Error sending Discord output: {e}")
            await asyncio.sleep(100)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm your Discord to Telegram relay bot!\nSend /help to see available commands.")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    help_text = "Available commands:\n/start - Start the bot\n/help - Show this help message"
    await message.reply(help_text)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(send_discord_output())
    executor.start_polling(dp, skip_updates=True)
