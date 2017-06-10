import command_system

def test(messages, connection):
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT COUNT(*) FROM `playlists`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    connection.close()
    return 'test', None


info_command = command_system.Command()

info_command.keys = ['/test2']
info_command.description = 'Тестовая команда'
info_command.process = test
info_command.isShow = False
