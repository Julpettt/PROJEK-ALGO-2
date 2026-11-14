import csv
import os




print("""
                        🍔 SELAMAT DATANG 🍔

███╗   ███╗ █████╗ ██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗██╗   ██╗██╗   ██╗
████╗ ████║██╔══██╗██║ ██╔╝██╔══██╗████╗  ██║██║ ██╔╝██║   ██║╚██╗ ██╔╝
██╔████╔██║███████║█████╔╝ ███████║██╔██╗ ██║█████╔╝ ██║   ██║ ╚████╔╝
██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══██║██║╚██╗██║██╔═██╗ ██║   ██║  ╚██╔╝
██║ ╚═╝ ██║██║  ██║██║  ██╗██║  ██║██║ ╚████║██║  ██╗╚██████╔╝   ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═══╝╚═╝  ╚═╝ ╚═════╝    ╚═╝

             🍔  Solusi Cerdas untuk Pemesanan Makanan  🍔
""")

folder_path = os.path.dirname(os.path.abspath(__file__))
FILE_MENU = os.path.join(folder_path, 'menu.csv')
data_transaksi = os.path.join(folder_path, 'data_transaksi.csv')

def menu_utama():
    while True:
        print("\n===== MENU UTAMA =====")
        print("[1]. Tampilkan Menu Makanan")
        print("[2]. Cari menu")
        print("[3]. Pesan makanan")
        print("[4]. Hitung Total Pembayaran")
        print("[5]. Riwayat Transaksi")
        print("[6]. Keluar")

        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            cari_menu()
        elif pilihan == "3":
            print ("Fitur pemesanan makanan belum tersedia.")
        elif pilihan == "4":
            print ("Fitur perhitungan total pembayaran belum tersedia.")
        elif pilihan == "5":
            print ("Fitur riwayat transaksi belum tersedia.")
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def siapkan_file():
    if not os.path.exists(FILE_MENU):
        with open(FILE_MENU, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Harga", "Stock"])
            writer.writerow([1, "Nasi Goreng", 15000, 20])
            writer.writerow([2, "Mie Goreng", 12000, 15])
            writer.writerow([3, "Ayam Bakar", 25000, 10])
            writer.writerow([4, "Sate Ayam", 20000, 25])

    if not os.path.exists(data_transaksi):
        with open(data_transaksi, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID Transaksi", "ID Menu", "Jumlah", "Total Harga"])
    
def tampilkan_menu():
    with open(FILE_MENU, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader, None)

        print("\n===== DAFTAR MENU MAKANAN =====")
        print("ID | Nama Makanan | Harga | Stock")

        for data in reader:
            if len(data) >= 4:
                print(
                    data[0], "|",
                    data[1], "|",
                    "Rp", data[2], "|",
                    data[3]
                )

def cari_menu():
    keyword = input("Masukkan nama menu yang ingin dicari: ")

    with open(FILE_MENU, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader, None)

        print("\n===== HASIL PENCARIAN =====")
        ditemukan = False

        for data in reader:
            if len(data) >= 4:
                if keyword.lower() in data[1].lower():
                    print(
                        data[0], "|",
                        data[1], "|",
                        "Rp", data[2], "|",
                        data[3]
                    )
                    ditemukan = True

        if not ditemukan:
            print("Menu tidak ditemukan.")
            return

siapkan_file()
menu_utama()
cari_menu()