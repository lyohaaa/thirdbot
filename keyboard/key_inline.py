from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://www.purina.ru/cats/breed-library')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://www.purina.ru/cats/breed-library')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline

def get_keyboard_inline_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=2)
    but_inline_3 = InlineKeyboardButton('Посмотреть', url='https://clck.ru/3AuBAx')
    but_inline_4 = InlineKeyboardButton('Посмотреть', url='https://clck.ru/3AuBAx')
    keyboard_inline_2.add(but_inline_3, but_inline_4)
    return keyboard_inline_2
