from kasir import Kasir

class Admin(Kasir):
    def __init__(self, namatoko="Lans Coffee Shop", idlogin = None, passwordlogin = None, namakasirlogin = None, teleponkasirlogin = None) :
        super().__init__(namatoko)
        self.idlogin = idlogin
        self.passwordlogin = passwordlogin
        self.namakasirlogin = namakasirlogin
        self.teleponkasirlogin = teleponkasirlogin
    def loginKasir(self):
        try:
            import mysql.connector
            conn = mysql.connector.connect(
            host = 'localhost',
            database = 'kelompok2_kasir',
            user = 'root',
            password = ''
            )
            cursor = conn.cursor()
            print("==============")
            print("LOGIN AS ADMIN")
            print("==============")
            idconfirm = input("Masukkan ID : ")
            passwordconfirm = input("Masukkan Password : ")
            print()
            cursor.execute('''SELECT * from adminkasir WHERE id_kasir = %s'''%(idconfirm))
            resultlogin = cursor.fetchall()
            for row in resultlogin:
                self.idlogin = row[0]
                self.passwordlogin = row [1]
                self.namakasirlogin = row[2]
                self.teleponkasirlogin = row[3]
                if str(self.idlogin) == str(idconfirm) and str(self.passwordlogin) == (passwordconfirm) :
                    print("\nLogin Berhasil\n")
                    pwrong = 1
                    print("Selamat Datang "+self.namakasirlogin)
                    return pwrong
                else:
                    print("\nPassword Salah\n")
                    pwrong = 0
                    return pwrong
        except:
            print("\nPassword Salah\n")
            pwrong = 0
            return pwrong

    def mainMenu(self):
        print()
        print("========== MAIN MENU ==========")
        print("1. Mulai Kasir")
        print("2. Lihat Daftar Produk")
        print("3. Tambah Produk")
        print("4. Edit Produk")
        print("5. Hapus Produk")
        print("6. Lihat Riwayat Penjualan")
        print("7. Keluar Program")
        print()




