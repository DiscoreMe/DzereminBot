import telebot
import settings
import messageHandler
import threading
import time
import core.query_processing
from core.sql import MysqlConnection

bot = telebot.TeleBot(settings.token)

@bot.message_handler(content_types=["text"])
def echo(message):
    messageHandler.create_answer(bot, message)

@bot.callback_query_handler(func=lambda call: True)
def callback_echo(call):
    call.message.text = call.data
    messageHandler.create_answer(bot, call.message)

def start_polling():
    global bot
    while 1:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print("Error: ", end='')
            print(e)
            bot.stop_polling()
            bot = telebot.TeleBot(settings.token)
            continue
        else:
            bot.stop_polling()
            bot = telebot.TeleBot(settings.token)
            break

def update():
    connection = MysqlConnection()
    while 1:
        core.query_processing.Query_Processing(bot, connection)
        time.sleep(5)

if __name__ == '__main__':

    bot_polling = threading.Thread(target=start_polling)
    updater = threading.Thread(target=update)

    bot_polling.start()
    updater.start()