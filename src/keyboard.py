from telebot import types

def create_keyboard(*keys,row_width=2,resize_keyboard=True):
    markup = types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard)
    buttons = map(types.KeyboardButton, keys)
    markup.add(*buttons)
    return markup
