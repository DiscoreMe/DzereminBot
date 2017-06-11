import command_system

def command(messages, connection):
    import locals.ru as lang
    cmd = [lang.welcome_1, lang.welcome_2]
    result = connection.execute("SELECT tID FROM `users` WHERE `tID`= "+str(messages.chat.id))
    if result.fetchone() == None:
        connection.execute("INSERT INTO `users` SET `tID` = "+str(messages.chat.id))
        connection.commit()
        cmd.insert(0,lang.register_ok)
    return cmd, None


info_command = command_system.Command()

info_command.keys = ['/start']
info_command.description = 'Start new game'
info_command.process = command
info_command.isShow = False
