def sendMessage(bot=None,chat_id=None,messages=None,options=None):
    reply_markup = None
    if options is not None:
        if options['reply_markup'] is not None:
            reply_markup = options['reply_markup']
    for i in messages:
        bot.send_message(chat_id=chat_id,text=i, reply_markup=reply_markup, parse_mode="Markdown")