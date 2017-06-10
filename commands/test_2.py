import command_system

def test(messages, connection):
    sql = "SELECT * FROM `playlists`"
    result = connection.execute(sql)
    return result, None


info_command = command_system.Command()

info_command.keys = ['/test2']
info_command.description = 'Тестовая команда'
info_command.process = test
info_command.isShow = False
