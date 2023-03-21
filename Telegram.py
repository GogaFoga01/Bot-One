import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = 'Yor Token' # Указать ТОкен Бота телеграмм
CHAT_ID = "Your Chat_ID" # https://t.me/getmyid_bot Бот для получения ID
DISCORD_BOT_URL = 'Your Https' # Ссылку заменить на своего  бота

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def send_to_telegram(data: str):
    await bot.send_message(chat_id=CHAT_ID, text=data)


async def send_discord_output():
    while True:
        try:
            # Send GET request to the Discord bot's URL to get the latest output
            response = requests.get(DISCORD_BOT_URL)
            output = response.text

            # Send the output to the user
            await bot.send_message(chat_id=CHAT_ID, text=output)

            # Wait for 10 seconds before checking for new output
            await asyncio.sleep(10)

        except Exception as e:
            logging.error(f"Error sending Discord output: {e}")
            await asyncio.sleep(10)

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