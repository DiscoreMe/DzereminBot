import command_system

def command(messages, connection):
    import locals.ru as lang
    if messages.reply_to_message is None:
        return ["Error #1"], None
    if len(messages.text) < 3 or len(messages.text) > 15:
        from telebot.types import ForceReply
        return [lang.set_name_length, lang.set_name], {"reply_markup": ForceReply()}
    result = connection.execute("SELECT `Nickname` FROM `users` WHERE `Nickname`= \"{}\"".format(messages.text))
    if result.fetchone() is not None:
        from telebot.types import ForceReply
        return [lang.busy_name], {"reply_markup": ForceReply()}
    connection.execute("UPDATE `users` SET `Nickname` = \"{}\" WHERE `tID` = {}".format(messages.text, messages.chat.id))
    connection.commit()
    return [lang.set_name_successfully.format(messages.text)], None


info_command = command_system.Command()

info_command.keys = ['/reply!setname']
info_command.description = 'replysetname'
info_command.process = command
info_command.isShow = False
