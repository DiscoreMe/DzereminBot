import command_system

def command(messages, connection):
    import locals.ru as lang
    message = ["Error #0"]
    result = connection.execute("SELECT `id`, `Nickname`, `Level`, `Money`, `Wood`, `Stone`, `Houses` FROM `users` WHERE `tID`= " + str(messages.chat.id))
    result = result.fetchone()
    if result is not None:
        if result["Nickname"] == None:
            result["Nickname"] = lang.no_name
        message = [lang.hero_info.format(result["Nickname"], result["Level"], result["Money"], result["Wood"], result["Stone"], result["Houses"], result["Houses"]*3)]
    return message, None


info_command = command_system.Command()

info_command.keys = ['/info', 'инфо', "🔍"]
info_command.description = 'Статистика персонажа'
info_command.process = command
