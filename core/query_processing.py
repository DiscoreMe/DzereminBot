def Query_Processing(bot, connection):
    result = connection.execute("SELECT * FROM `extraction`")
    result = result.fetchall()
    len_result = len(result)
    if len_result > 0:
        import locals.ru as lang
        from core.telegram import sendMessage
        for i in result:
            if i["Ready"] == False:
                continue
            if i["Times"] > 0:
                connection.execute("UPDATE `extraction` SET `Times` = {} WHERE `id` = {}".format(i['Times']-5, i["id"]))
                connection.commit()
            else:
                res = connection.execute("SELECT `Wood`, `Stone` FROM `users` WHERE `tID` = {}".format(i["tID"]))
                res = res.fetchone()
                n_mat = 0
                sql_mat = ""
                if i["Material"] == "Wood":
                    n_mat = 2
                    sql_mat = "Wood"
                else:
                    n_mat = 1
                    sql_mat = "Stone"
                formula = i["Peasants"] * i["TimesAll"]//60 * n_mat + res[sql_mat]
                connection.execute("UPDATE `users` SET `{}` = {} WHERE `tID` = {}".format(sql_mat, formula, i["tID"]))
                connection.execute("DELETE FROM `extraction` WHERE `id` = {}".format(i["id"]))
                connection.commit()
                sendMessage(bot, i["tID"], [lang.workes_return.format(formula, sql_mat)])