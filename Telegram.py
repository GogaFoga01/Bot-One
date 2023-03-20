import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types
import Discord
from Discord import on_message


API_TOKEN = '5753731786:AAHh7dSDsqgWKJsPJNttUKZvY87Fw6zy3Lc'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

TOKEN = "MTA4NjE5OTM5NzU5Mjg1ODY0NA.GpEFVQ.IaDiPsm-k2VTYLI2flTeaYEIC5CcGE5GkQX4Q0"
intents = discord.Intents.all()
client = discord.Client(intents=intents)
CHANNEL_ID = 1086194776111579310

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await Discord.on_message.output

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
