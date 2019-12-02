# -*- coding: utf-8 -*-

from telebot import types
import telebot;
bot = telebot.TeleBot('695844249:AAGYTqvhE00LU2B8pVUpjQPtVnJU4Hz0vGQ');

name = '';
surname = '';
age = 0;

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('Да', 'Нет')
    global age;
    age = message.text;
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+', тебя зовут '+name+' '+surname+'?', reply_markup=keyboard1)
    bot.register_next_step_handler(message, remember_me);

@bot.message_handler(content_types=['text'])
def  remember_me(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Запомню ;) Напиши /reg')
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Напиши /reg')

bot.polling(none_stop=True, interval=0)