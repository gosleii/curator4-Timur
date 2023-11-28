import telebot

bot = telebot.TeleBot('6677530632:AAGqCPdmfqWVaA6r7AEW_vVUR2bWok80RU4')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message.chat.id, 'Привет! Я бот')

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.reply_to(message.chat.id, 'Это бот попугай')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.reply_to(message, 'Ты сказал: ' + message.text)

bot.infinity_polling()