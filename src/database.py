import psycopg2

class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='localhost',
            database='dbname',
            user='user',
            password='pass'
        )
        self.cur = self.conn.cursor()

    def savedata(self, sql, data):
        self.cur.execute(
            sql,
            tuple(data))
    
    def getdata(self, sql):
        return self.cur.execute(
            sql)

DATABASE = DB()