#- * -coding: utf - 8 - * -

    import telebot;
bot = telebot.TeleBot('817988164:AAEDUAowZiTowLVs9yl7gv31CgoX_QA0Zjg');

@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else :
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

name = '';
surname = '';
age = 0;
@bot.message_handler(content_types = ['text'])
def start(message):
    if message.text == '/reg':
    bot.send_message(message.from_user.id, "Как тебя зовут?");
bot.register_next_step_handler(message, get_name);#
следующий шаг– функция get_name
else :
    bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
global name;
name = message.text;
bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
bot.register_next_step_handler(message, get_surnme);

def get_surname(message):
    global surname;
surname = message.text;
bot.send_message('Сколько тебе лет?');
bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
while age == 0: #проверяем что возраст изменился
try:
age = int(message.text)# проверяем, что возраст введен корректно
except Exception:
    bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')

bot.polling(none_stop = True, interval = 0)