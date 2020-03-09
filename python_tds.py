import pytds


class MsSql:
    def __init__(self, host=None, user=None, passwd=None) -> None:
        self.conn = pytds.connect(dsn=host, user=user, password=passwd, autocommit=True)

    def query(self, sql=None):
        cur = self.conn.cursor()
        res = cur.execute(sql)
        return res

    def update(self, sql=None):
        cur = self.conn.cursor()
        cur.execute(sql)


ms = MsSql('localhost', 'sa', 'DBG@2020')
for row in ms.query('select name,age from p2aes.dbo.test'):
    print(f"{row[0]}: {row[1]}")
