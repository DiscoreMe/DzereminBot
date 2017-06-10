import command_system

def getLists(messages, connection):
    message = ''
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name FROM `playlists` WHERE player_id = " + str(messages.chat.id))
        result = cursor.fetchall()
        print(result)
        if result is None:
            message = "На данный момент у вас нет списков. Для создания списка введите /createlist название"
        else:
            for res in result:
                message += "{} - /list_{}\n".format(res['name'], res['id'])
    return message, None


info_command = command_system.Command()

info_command.keys = ['/getlists']
info_command.description = 'Показать список листов'
info_command.process = getLists
