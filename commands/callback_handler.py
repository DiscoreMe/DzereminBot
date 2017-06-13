import command_system

def command(messages, connection):
    mess = messages.text.split("_")
    if len(mess) == 1:
        return ["Error #2"], None
    from commands.callback import test
    selector = {
        "test": test.test()
    }
    try: return selector[mess[1]]
    except: return ["Error #3"], None


info_command = command_system.Command()

info_command.keys = ['callback']
info_command.description = 'Callback'
info_command.process = command
info_command.isShow = False
