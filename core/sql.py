import pymysql
class MysqlConnection:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='',
                                    db='telegram', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, )
    def execute(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchone()

    def close(self):
        self.connection.close()