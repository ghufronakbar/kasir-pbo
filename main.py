from admin import Admin
from kasir import Kasir
from penjualan import Penjualan
from produk import Produk
import mysql.connector

l = "Lans Coffee Shop"
class Main:
    def play(self):
        Kasir(l).connectDatabase()
        Kasir(l).kasirToko()
        passwordwrong = Admin().loginKasir()
        if passwordwrong == 1 :
            Admin().mainMenu()
            while True:
                try:
                    pilihmenu = int(input("Pilih Menu : "))
                    print()
                    if pilihmenu == 1:
                        Penjualan(l).transaksi()
                        Penjualan(l).cetakNota()
                    elif pilihmenu == 2:
                        Produk(l).tampilProduk()
                    elif pilihmenu == 3:
                        Produk(l).tambahProduk()
                    elif pilihmenu == 4:
                        Produk(l).editProduk()
                    elif pilihmenu == 5:
                        Produk(l).hapusProduk()
                    elif pilihmenu == 6:
                        Penjualan(l).riwayatPenjualan()
                    elif pilihmenu == 7:
                        print("Terimakasih telah menggunakan program ini")
                        break
                    else:
                        print("MENU SALAH")
                except:
                    print("MENU SALAH")
        else :
            print("Password Salah")

Main().play()
