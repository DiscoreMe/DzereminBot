import command_system

def command(messages, connection):
    import locals.ru as lang
    from telebot.types import ForceReply
    return [lang.set_name], {"reply_markup": ForceReply()}


info_command = command_system.Command()

info_command.keys = ['/setname']
info_command.description = 'Set name'
info_command.process = command
