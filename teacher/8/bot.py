import telebot
key = '1765842295:AAH_Vj8ti5WSjsU5mUFS7U3tOY2AmCinkAY'
print('Start bot')
bot = telebot.TeleBot(key)

@bot.message_handler()
def start_message(message):
    print(message.text)
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()