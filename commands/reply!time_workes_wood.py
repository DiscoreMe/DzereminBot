import command_system

def command(messages, connection):
    import locals.ru as lang
    from telebot.types import ForceReply
    try:
        time = int(messages.text)
        if time < 1 or time > 10:
            return [lang.how_time_workes_wood], {"reply_markup": ForceReply()}
        connection.execute("UPDATE `extraction` SET `Times` = {}, `TimesAll` = {}, `Ready` = 1 WHERE `tID` = {}".format(time*60, time*60, messages.chat.id))
        connection.commit()
        return [lang.work_add], None
    except:
        return [lang.how_time_workes_wood], {"reply_markup": ForceReply()}


info_command = command_system.Command()

info_command.keys = ['/reply!time_workes_wood']
info_command.description = 'time_workes_wood'
info_command.process = command
info_command.isShow = False
