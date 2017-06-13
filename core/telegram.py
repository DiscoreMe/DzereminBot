def sendMessage(bot=None,chat_id=None,messages=None,options=None):
    reply_markup = None
    parse_mode = "Markdown"
    if options is not None:
        try: reply_markup = options['reply_markup']
        except: pass
        try: parse_mode = options['parse_mode']
        except: pass
    for i in messages:
        bot.send_message(chat_id=chat_id,text=i, reply_markup=reply_markup, parse_mode=parse_mode)