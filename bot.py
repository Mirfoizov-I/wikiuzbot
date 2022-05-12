import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

ADMINS=[843041627]

wikipedia.set_lang('uz')

API_TOKEN = '5284094363:AAELsEmYL6RxdYF0VrMgUNLDO3-n1rq9-2M'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	"""
	This handler will be called when user sends `/start` or `/help` command
	"""
	await message.reply(f"Salom 👋 {message.from_user.full_name}! \n"
						 "🌱 Wikipedia Qidiruvi Botiga Xush Kelibsiz!")
	if message.from_user.username:
		user_n = message.from_user.username
	else:
		user_n = "usernami yo'q"
	msg = f"{message.from_user.full_name} va @{user_n} foydalanuvchi Wikipedia botdan foydalandi"
	await bot.send_message(chat_id=ADMINS[0], text=msg)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user send command
    """
    await message.reply(f"✅ Wikipedia Qidiruvi Botidan foydalanish uchun bizga maqolani mavzusini yuboring! \n"
                         "❗️ Maqola mavzusi to'g'ri kiritilmasa yoki Wikipediada majud bo'lmasa, Siz kiritgan mavzudagi maqola topilmaganligi bo'yicha xabar yuboriladi!")


@dp.message_handler()
async def sendWiki(message: types.Message):
	try:
		respond=wikipedia.summary(message.text)
		await message.reply(respond)
	except:
		await message.reply("Bu mavzuga iod maqola topilmadi")

		
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
