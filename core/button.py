import telebot.types as types

def returnKeyboardButton(keyboards=None):
    markup = types.ReplyKeyboardMarkup()
    for keys in keyboards:
        items = []
        for i in keys:
            items.append(types.KeyboardButton(i))
        markup.add(items)
    return markup