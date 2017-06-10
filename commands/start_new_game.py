import command_system

def command(messages, connection):
    import locals.ru as lang
    return "query", {"sendmessages":[lang.welcome_1, lang.welcome_2]}


info_command = command_system.Command()

info_command.keys = ['/start']
info_command.description = 'Start new game'
info_command.process = command
info_command.isShow = False
