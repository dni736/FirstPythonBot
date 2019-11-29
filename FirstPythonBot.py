# -*- coding: utf-8 -*-

import telebot;
bot = telebot.TeleBot('817988164:AAF1xNleSZocgSEdBpn34GFu5UGKswSzQdM');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == "привет":
    		bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
	elif message.text == "/help":
    		bot.send_message(message.from_user.id, "Напиши привет")
	else:
    		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)