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
        encrypted = (data['username'], data['email'], data['url'], encrypt(data['password'].encode('utf-8')), data['notes'])
        sql = 'INSERT INTO domains VALUES (%s, %s, %s, %s, %s)'
        self.cur.execute(sql, tuple(encrypted))
        self.conn.commit()
    
    def getdata(self, elem):
        condition = ''
        for k, v in elem.items():
            condition += k + " LIKE '%" + v + "%' AND " 
        condition = condition[:-5] + ';'
        self.cur.execute(f'SELECT * FROM domains WHERE ' + condition)
        return self.cur.fetchone()
    
    def getall(self):
        sql = "SELECT * FROM domains"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def deleteEntry(self, elem):
        condition = ''
        for k, v in elem.items():
            condition += k + " LIKE '%" + v + "%' AND " 
        condition = condition[:-5] + ';'
        self.cur.execute('DELETE FROM domains WHERE ' +  condition)
        self.conn.commit()
        return



if __name__ == "__main__":
    DB('shagri', 'manager', 'lynx100210165').getdata({'foo' : 'bar', 'bar' : 'foo'})

