import command_system

def command(messages, connection):
    import locals.ru as lang
    mess = messages.text.split('_')
    len_mess = len(mess)
    if len_mess == 1:
        return [lang.menu_workes], {"parse_mode": None}
    if len_mess >= 2:
        from telebot.types import ForceReply
        if mess[1] == "wood":
            return [lang.how_count_workes_wood], {"reply_markup": ForceReply()}
        elif mess[1] == "stone":
            return [lang.how_count_workes_stone], {"reply_markup": ForceReply()}
        else:
            return [lang.menu_workes], {"parse_mode": None}
    return [lang.menu_workes], {"parse_mode": None}


info_command = command_system.Command()

info_command.keys = ['/extract']
info_command.description = 'Показать список работ'
info_command.process = command
