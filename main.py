from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline, get_keyboard_inline_2
from database.database import initialize_db, add_user, get_user

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.reply('Привет, я третий бот', reply_markup=get_keyboard_1())
    else:
        await message.reply('Привет, я третий бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://clck.ru/3Asn6h', caption= 'Вот тебе кот!', reply_markup=get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://clck.ru/3Aso98', caption= 'Вот тебе собака!', reply_markup=get_keyboard_inline_2())

@dp.message_handler(lambda message: message.text == 'Перейти на первую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото кота', reply_markup=get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)