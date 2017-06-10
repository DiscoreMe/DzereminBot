import telebot
import settings
import messageHandler

bot = telebot.TeleBot(settings.token)
import pymysql.cursors
connection = pymysql.connect(host='localhost',user='root',password='',
                             db='telegram',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

@bot.message_handler(content_types=["text"])
def echo(message):
    messageHandler.create_answer(bot, message, connection)

if __name__ == '__main__':
    bot.polling(none_stop=True)
    print('1')
    connection.close()