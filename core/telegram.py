def sendMessage(bot=None,chat_id=None,text=None,options=None):
    reply_markup = None
    if options is not None and options['sendmessages'] is not None:
        for i in options['sendmessages']:
            bot.send_message(chat_id=chat_id, text=i)
    else:
        if options is not None:
            if options['keyboards'] is not None:
                reply_markup = options['keyboards']
        bot.send_message(chat_id=chat_id,text=text, reply_markup=reply_markup)