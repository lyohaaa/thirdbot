from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard_inline = InlineKeyboardMarkup(row_width= 1)
but_inline = InlineKeyboardButton('Посмотреть', url='https://www.purina.ru/cats/breed-library')
but_inline2 = InlineKeyboardButton('Посмотреть', url='https://www.purina.ru/cats/breed-library')
keyboard_inline.add(but_inline, but_inline2)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.reply('Привет, я второй бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://clck.ru/3Asn6h', caption= 'Вот тебе кот!', reply_markup=keyboard_inline)

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://clck.ru/3Aso98', caption= 'Вот тебе собака!')

@dp.message_handler(lambda message: message.text == 'Перейти на первую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото кота', reply_markup=get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)