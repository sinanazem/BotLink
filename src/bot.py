import telebot
import os
from telebot import types

from src.keyboard import create_keyboard
from src.utils import readjson, writejson,writetxt,readtxt
from src.constant import keyboards
bot = telebot.TeleBot(os.environ["TELEGRAM_TOKE"])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
   bot.send_message(message.chat.id,
    f'Hi Dear {message.chat.first_name}',
    reply_markup=keyboards.main)

@bot.message_handler(commands=['link', 'get'])
def send_welcome(message):
#    print(readtxt('data.txt'))
   bot.send_message(message.chat.id,str(readtxt('data.txt')))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    writejson(message.json,'data.json')
    if 'http' in message.text  :
        writetxt(message.text,'data.txt')
    bot.send_message(
        message.chat.id,
         f'Link?',
         reply_markup=keyboards.main)

bot.infinity_polling()