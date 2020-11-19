import psycopg2
from .encrypt import encrypt
from .decrypt import decrypt


class DB:
    def __init__(self, user, dbname, password):
        self.conn = psycopg2.connect(
            host='localhost',
            database=dbname,
            user=user,
            password=password
        )
        self.cur = self.conn.cursor()

    def savedata(self, data):
        encrypted = encrypt(data['password'].encode('utf-8'))
        print(encrypted)
        sql = 'INSERT INTO domains VALUES (%s, %s, %s, %s, %s)'
        self.cur.execute(sql, (data['username'], data['email'], data['url'], encrypted, data['notes']))
        self.conn.commit()
    
    def getdata(self, sql):
        return self.cur.execute(
            sql)

