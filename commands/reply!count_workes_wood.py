import command_system

def command(messages, connection):
    import locals.ru as lang
    if messages.reply_to_message is None:
        return ["Error #1"], None
    result_user = connection.execute("SELECT `Houses` FROM `users` WHERE `tID` = {}".format(messages.reply_to_message.chat.id))
    result_extracts = connection.execute("SELECT `Peasants`, `Ready` FROM `extraction` WHERE `tID` = {}".format(messages.reply_to_message.chat.id))
    result_user = result_user.fetchone()
    result_extracts = result_extracts.fetchall()
    workers = result_user["Houses"] * 3
    for i in result_extracts:
        if i["Ready"] is False:
            continue
        workers = workers - i["Peasants"]
    from telebot.types import ForceReply
    try:
        w_int = int(messages.text)
        if w_int == 0:
            return [lang.work_cancel], None
        elif workers < w_int or w_int < 0:
            return [lang.few_workers, lang.how_count_workes_wood], {"reply_markup": ForceReply()}
        else:
            connection.execute("INSERT INTO `extraction` (`tID`, `Peasants`, `Material`) VALUES ({}, {}, \"Wood\")".format(messages.chat.id, messages.text))
            connection.commit()
            return [lang.how_time_workes_wood], {"reply_markup": ForceReply()}
    except:
        return [lang.how_count_workes_wood], {"reply_markup": ForceReply()}

info_command = command_system.Command()

info_command.keys = ['/reply!count_workes_wood']
info_command.description = 'count_workes_wood'
info_command.process = command
info_command.isShow = False
