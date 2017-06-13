import importlib
import os

from command_system import command_list
from core.telegram import sendMessage
from core.sql import MysqlConnection

connection = MysqlConnection()

def load_modules():
   files = os.listdir("commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(messages):
    global connection
    bodys_p = messages.text.split()
    bodys_s = messages.text.split('_')
    if len(bodys_p) == 1 and len(bodys_s) > 1:
        body = bodys_s[0]
    else:
        body = bodys_p[0]

    message = ["Список команд: /help"]
    command = False
    options = None
	
    if messages.reply_to_message is not None:
        import locals.ru as lang
        if messages.reply_to_message.text == "/setname" or messages.reply_to_message.text == lang.set_name or messages.reply_to_message.text == lang.busy_name:
            body = "/reply!setname"
        elif messages.reply_to_message.text == lang.how_count_workes_stone:
            body = "/reply!count_workes_stone"
        elif messages.reply_to_message.text == lang.how_time_workes_stone:
            body = "/reply!time_workes_stone"
        elif messages.reply_to_message.text == lang.how_count_workes_wood:
            body = "/reply!count_workes_wood"
        elif messages.reply_to_message.text == lang.how_time_workes_wood:
            body = "/reply!time_workes_wood"

    for c in command_list:
        for k in c.keys:
            if k == body:
                message, options = c.process(messages, connection)
                command = True
                break
        if command:
            break

    return message, options

def create_answer(bot, messages):
   load_modules()
   message, options = get_answer(messages)
   sendMessage(bot, messages.chat.id, message, options)