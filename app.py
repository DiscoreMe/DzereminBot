import telebot
from docutils.nodes import thead

import settings
import messageHandler
import threading
import time

connection = None
bot = None

def main():
    global bot, connection
    bot = telebot.TeleBot(settings.token)
    import pymysql.cursors
    connection = pymysql.connect(host='localhost',user='root',password='',
                                 db='telegram',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

    @bot.message_handler(content_types=["text"])
    def echo(message):
        messageHandler.create_answer(bot, message, connection)

def start_bot():
    bot.polling(none_stop=True)

def test():
    while 1:
        print('1')
        time.sleep(5)

if __name__ == '__main__':
    main()
    bot_polling = threading.Thread(target=start_bot)
    testing = threading.Thread(target=test)

    bot_polling.start()
    testing.start()

    connection.close()