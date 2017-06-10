import telebot
import settings
import messageHandler
import threading
import time

bot = telebot.TeleBot(settings.token)

@bot.message_handler(content_types=["text"])
def echo(message):
    messageHandler.create_answer(bot, message)

def start_polling():
    global bot
    while 1:
        try:
            bot.polling(none_stop=True)
        except:
            bot.stop_polling()
            bot = telebot.TeleBot(settings.token)
            continue
        else:
            bot.stop_polling()
            bot = telebot.TeleBot(settings.token)
            break

def update():
    while 1:
        time.sleep(60)

if __name__ == '__main__':

    bot_polling = threading.Thread(target=start_polling)
    updater = threading.Thread(target=update)

    bot_polling.start()
    updater.start()