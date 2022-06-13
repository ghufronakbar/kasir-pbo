class Kasir:
    def __init__(self, namatoko) :
        self.namatoko = namatoko
    
    def kasirToko(self):
        print("Kasir "+str(self.namatoko))

    def connectDatabase(self):
        import mysql.connector
        conn = mysql.connector.connect(
        host = 'localhost',
        database = 'kelompok2_kasir',
        user = 'root',
        password = ''
        )
        cursor = conn.cursor()


