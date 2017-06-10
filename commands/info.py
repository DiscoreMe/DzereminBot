import command_system

def command(messages, connection):
    message = 'Статистика персонажа'
    return message, None


info_command = command_system.Command()

info_command.keys = ['/info', 'инфо']
info_command.description = 'Статистика персонажа'
info_command.process = command
