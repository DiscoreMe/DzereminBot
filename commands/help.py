import command_system

def help(messages, connection):
    message = ''
    for c in command_system.command_list:
        if c.isShow:
            message += c.keys[0] + ' - ' + c.description + '\n'
    return message, None


info_command = command_system.Command()

info_command.keys = ['/help']
info_command.description = 'Список команд'
info_command.process = help
