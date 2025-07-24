import telebot

bot = telebot.TeleBot("8419710130:AAHT51c68nSRSh20nUUMpSVJ1p8hdGQWEgM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
