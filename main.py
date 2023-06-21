from aiogram import Bot,Dispatcher,executor,types
import logging


bot = Bot('6132652196:AAEjBCc7CI_J8GATiFhCe5JuIW69x_hvblA')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

START_TEXT = """Привет, я бот, который будет модератором в твоем канале или беседе🤖 
Все что тебе нужно сделать это скопировать ссылку на меня - https://t.me/moderator123123bot
Теперь добавь меня в любую из своих бесед/каналов😄
Важно понимать что я буду в обсуждение канала, то есть в его чате❗️
Сделай меня админом и никто не будет рекламировать свои услуги и писать маты😡"""

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(START_TEXT)


@dp.message_handler()
async def echo(message: types.Message):
    if 'https://t.me/' in message.text:
        await message.delete()
    if 'сука' in message.text:
        await message.delete()
    if 'блять' in message.text:
        await message.delete()
    if 'иди нахуй' in message.text:
        await message.delete()
    if 'шлюха' in message.text:
        await message.delete()
    if 'хуесос' in message.text:
        await message.delete()
    if 'выебываешься' in message.text:
        await message.delete()
    if 'ублюдок' in message.text:
        await message.delete()
    if 'хуйло' in message.text:
        await message.delete()
    if 'я твой рот ебал' in message.text:
        await message.delete()
    if 'ебать' in message.text:
        await message.delete()
    if 'пиздец' in message.text:
        await message.delete()
    if 'хуй' in message.text:
        await message.delete()
    if 'хуйня' in message.text:
        await message.delete()
    if 'блядь' in message.text:
        await message.delete()
    if 'блядина' in message.text:
        await message.delete()
    if 'уебок' in message.text:
        await message.delete()
    if 'сучка' in message.text:
        await message.delete()
    if 'лох' in message.text:
        await message.delete()
    if 'пидр' in message.text:
        await message.delete()
    if 'пидарас' in message.text:
        await message.delete()
    if 'хуйлан' in message.text:
        await message.delete()
    if 'залупа' in message.text:
        await message.delete()
    if 'пенис' in message.text:
        await message.delete()
    if 'соси' in message.text:
        await message.delete()
    if 'хер' in message.text:
        await message.delete()






















executor.start_polling(dp)
