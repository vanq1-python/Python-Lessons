import telebot

# Замените 'YOUR_API_TOKEN' на токен, полученный от BotFather
API_TOKEN = '7149233019:AAG2Gb_2dksUOIboL_IR6I9hYJi3V4R2Uw8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == "привет":
        bot.reply_to(message, "Привет! Как я могу помочь?")
    elif message.text.lower() == "как дела?":
        bot.reply_to(message, "У меня всё хорошо, спасибо! А у тебя?")
    else:
        bot.reply_to(message, "Извини, я не понимаю тебя.")


# Запуск бота
bot.polling()