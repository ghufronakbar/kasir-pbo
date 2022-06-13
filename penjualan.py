import imp
from mimetypes import init
from kasir import Kasir
import datetime

class Penjualan(Kasir):
    def __init__(self, namatoko, total=0):
        super().__init__(namatoko)
        self.total=total

    def transaksi(self):
        import mysql.connector
        conn = mysql.connector.connect(
        host = 'localhost',
        database = 'kelompok2_kasir',
        user = 'root',
        password = ''
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produk")
        myresult = cursor.fetchall()
        print("=======================================================================")
        print("=============================Daftar Produk=============================")
        print("=======================================================================")
        print("ID \t\t\t Nama Produk \t\t\t Harga")
        for row in myresult:
            print(row[0],"\t\t\t",row[1],"\t\t",row[2])
            listharga = row[2]
        print("\n")
        total = 0
        ketbarang = ""

        while True :
            a = int(input("Masukkan kode barang \t: ")) 
            b = int(input("Masukkan jumlah barang \t: "))
            print()
            while True :
                cursor.execute('''SELECT * from produk WHERE id_produk = %s'''%(a))
                orderbarang = cursor.fetchall()
                for x in orderbarang:
                    hargabarang = x[2] * b
                    hargaorder = hargabarang
                    ketbarangadd = (str(x[1])+"x"+str(b)+" : "+ str(hargabarang)+"\n")
                    ketbarang = ketbarang + ketbarangadd
                    print("Keranjang : ")
                    print(ketbarang)
                    total += int(hargaorder)
                    self.total = total
                    print("Total belanjaan : ",total)             
                    again = str.upper(input("\nApakah ingin menambah produk? (Y/T) : "))
                    if again == "Y":
                        print()
                    else:
                        konfirmasi = str.upper(input("\nKonfirmasi pesanan (Y/T) : "))
                        print()
                        if konfirmasi == "Y":
                            totalkonfirmasi = self.total
                            datedb = datetime.datetime.now()
                            '''print("=========NOTA=========")
                            print(ketbarang)
                            print("Total : Rp "+ str(totalkonfirmasi))
                            print(datedb)
                            print()'''
                            notaprint = "=========NOTA=========\n"+ketbarang+"\nTotal : Rp "+str(totalkonfirmasi)+"\n"+str(datedb)+"\n"
                            print(notaprint)
                            cursor.execute('INSERT INTO riwayat(date,keterangan,total)VALUES("%s","%s",%i)'%(datedb,ketbarang,totalkonfirmasi))
                            conn.commit()
                            return notaprint
                        else:
                            total = 0
                        break
                    break
                break
            
            
    def cetakNota(self):
        print("===== Terima Kasih Telah Berbelanja di %s ====="%(self.namatoko))
        print()

    def riwayatPenjualan(self):
        import mysql.connector
        conn = mysql.connector.connect(
        host = 'localhost',
        database = 'kelompok2_kasir',
        user = 'root',
        password = ''
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM riwayat")
        myresult = cursor.fetchall()
        print("=======================================================================")
        print("===========================Riwayat Penjualan===========================")
        print("=======================================================================")
        print("ID \t\t\t Tanggal \t\t\t Keterangan \t\t\t Total")
        totalpenghasilan = 0
        for row in myresult:
            print(row[0],"\t\t\t",row[1],"\t\t",row[2],"\t\t",row[3])
            totalpenghasilan += row[3]
        print("\nTotal Penghasilan : Rp "+str(totalpenghasilan)+"\n")

