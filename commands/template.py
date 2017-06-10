import command_system

def help(messages, connection):
    message = 'Hello world!'
    return message, None


info_command = command_system.Command()

info_command.keys = ['/help']
info_command.description = 'Список команд'
info_command.process = help
info_command.isShow = False
