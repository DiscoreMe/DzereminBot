import pymysql
from settings import sql_host, sql_database, sql_user, sql_password
class MysqlConnection:
    def __init__(self):
        self.connection = pymysql.connect(host=sql_host, user=sql_user, password=sql_password,
                                    db=sql_database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, )
    def execute(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor

    def close(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()