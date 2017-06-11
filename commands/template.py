import command_system

def command(messages, connection):
    message = ''
    return [message], None


info_command = command_system.Command()

info_command.keys = ['/helpq']
info_command.description = 'Список команд'
info_command.process = command
info_command.isShow = False
