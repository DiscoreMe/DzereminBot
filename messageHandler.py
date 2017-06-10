import os
import importlib
from command_system import command_list
from core.telegram import sendMessage

def load_modules():
   files = os.listdir("commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(messages, connection):
    body = messages.text.split()[0]
    message = "Список команд: /help"
    command = False
    options = None
    for c in command_list:
        for k in c.keys:
            if k == body:
                message, options = c.process(messages, connection)
                command = True
                break
        if command:
            break
    return message, options

def create_answer(bot, messages, connection):
   load_modules()
   message, options = get_answer(messages, connection)
   sendMessage(bot, messages.chat.id, message, options)