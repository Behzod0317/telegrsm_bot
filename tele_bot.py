from transliterate import to_cyrillic,to_latin
import telebot
import telegram

Token = "5854229940:AAH-IMQKzszTbN9otCpFxD_xEtb2NhxFEZ8"
bot = telebot.TeleBot(Token,parse_mode=None)

@bot.message_handler(commands=['start'])

def send_welcome(message):

    answer = "Hello! Welcome"
    answer += "\nEnter text"
    bot.reply_to(message,answer)
    # message = update.message.text
    # username = update.message.chat.username
    # reply = f'{message} {username}'
    # context.bot.send_message(chat_id=update.message.chat_id, text=reply)


@bot.message_handler(commands=['help'])

def help_user(message):
    answer = "The task of this bot is to convert Latin text to Krill or Krill to Latin."
    bot.reply_to(message,answer)


@bot.message_handler(func=lambda message : True)

def echo_all(message):

    msg = message.text
    if msg.isascii():
        answer =to_cyrillic(msg)

    else:
        answer = to_latin(msg)

    bot.reply_to(message,answer)



bot.polling()
