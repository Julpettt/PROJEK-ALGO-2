import csv
import pathlib
from datetime import datetime

BASE_DIR = pathlib.Path(__file__).resolve().parent
DIR_DATA = BASE_DIR / "data"
DIR_DATA.mkdir(exist_ok=True)

FILE_MENU      = DIR_DATA / "menu.csv"
FILE_USER      = DIR_DATA / "user.csv"
FILE_TRANSAKSI = DIR_DATA / "transaksi.csv"
FILE_DETAIL    = DIR_DATA / "data_transaksi.csv"

def init_data():
    if not FILE_USER.exists():
        with open(FILE_USER, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Username", "Password", "Role"])
            w.writerow(["admin", "admin123", "Admin"])
            w.writerow(["pembeli", "12345", "User"])

    if not FILE_MENU.exists():
        with open(FILE_MENU, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["ID", "Nama", "Kategori", "Harga", "Stok"])
            w.writerow(["1", "Nasi Goreng",    "Makanan", "15000", "20"])
            w.writerow(["2", "Mie Goreng",     "Makanan", "12000", "15"])
            w.writerow(["3", "Kentang Goreng", "Snack",   "18000", "10"])

    if not FILE_TRANSAKSI.exists():
        with open(FILE_TRANSAKSI, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["id_transaksi", "username", "total"])

    if not FILE_DETAIL.exists():
        with open(FILE_DETAIL, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["ID Transaksi", "ID Menu", "Jumlah", "Total Harga"])

def baca_menu():
    menu = []
    if not FILE_MENU.exists():
        return menu
    with open(FILE_MENU, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        baris_pertama = True
        for row in reader:
            if baris_pertama:
                baris_pertama = False
            else:
                if len(row) >= 5:
                    menu.append(row)
    return menu


def simpan_menu(menu):
    with open(FILE_MENU, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Nama", "Kategori", "Harga", "Stok"])
        for row in menu:
            w.writerow(row)


def baca_user():
    users = []
    if not FILE_USER.exists():
        return users
    with open(FILE_USER, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        baris_pertama = True
        for row in reader:
            if baris_pertama:
                baris_pertama = False
            else:
                if len(row) >= 3:
                    users.append(row)
    return users


def simpan_user(users):
    with open(FILE_USER, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Username", "Password", "Role"])
        for row in users:
            w.writerow(row)
            

def format_rp(angka):
    return f"Rp{int(angka):,}".replace(",", ".")


def minta_angka(teks):
    while True:
        val = input(teks).strip()
        if val.isdigit():
            return int(val)
        print("Harus berupa angka!")


def tampilkan_menu(menu=None):
    if menu is None:
        menu = baca_menu()
    if not menu:
        print("Belum ada menu tersedia.")
        return

    print("\n" + "=" * 65)
    print(f"{'ID':<5}{'Nama Menu':<22}{'Kategori':<12}{'Harga':<14}{'Stok':<6}{'Status'}")
    print("-" * 65)
    for m in menu:
        stok = int(m[4])
        status = "Tersedia" if stok > 0 else "Habis"
        print(f"{m[0]:<5}{m[1]:<22}{m[2]:<12}{format_rp(m[3]):<14}{stok:<6}{status}")
    print("=" * 65)


def cari_menu():
    menu = baca_menu()
    if not menu:
        print("Menu belum tersedia.")
        return

    print("\n1. Cari berdasarkan Nama")
    print("2. Cari berdasarkan Kategori")
    pilihan = input("Pilih (1/2): ").strip()

    hasil = []
    match pilihan:
        case "1":
            kata = input("Nama makanan/minuman: ").strip().lower()
            for m in menu:
                if kata in m[1].lower():
                    hasil.append(m)
        case "2":
            kata = input("Kategori (Makanan/Minuman/Snack): ").strip().lower()
            for m in menu:
                if kata in m[2].lower():
                    hasil.append(m)
        case _:
            print("Pilihan tidak valid!")
            return

    if len(hasil) > 0:
        tampilkan_menu(hasil)
    else:
        print("Menu tidak ditemukan.")


def tambah_menu():
    menu = baca_menu()
    print("\n=== TAMBAH MENU ===")
    nama = input("Nama menu: ").strip()

    print("1. Makanan  2. Minuman  3. Snack")
    pilihan_kat = input("Pilih kategori (1/2/3): ").strip()
    match pilihan_kat:
        case "1": kat = "Makanan"
        case "2": kat = "Minuman"
        case "3": kat = "Snack"
        case _:   kat = "Lainnya"

    harga = minta_angka("Harga: ")
    stok  = minta_angka("Stok: ")

    id_tertinggi = 0
    for m in menu:
        if int(m[0]) > id_tertinggi:
            id_tertinggi = int(m[0])
    id_baru = id_tertinggi + 1

    menu.append([str(id_baru), nama, kat, str(harga), str(stok)])
    simpan_menu(menu)
    print(f"\nMenu '{nama}' berhasil ditambahkan dengan ID {id_baru}!")


def hapus_menu():
    menu = baca_menu()
    tampilkan_menu(menu)
    if not menu:
        return

    id_hapus = input("\nMasukkan ID menu yang akan dihapus: ").strip()

    ditemukan = False
    for m in menu:
        if m[0] == id_hapus:
            menu.remove(m)
            ditemukan = True
            break

    if ditemukan:
        simpan_menu(menu)
        print("Menu berhasil dihapus!")
    else:
        print("ID menu tidak ditemukan!")


def update_stok():
    menu = baca_menu()
    tampilkan_menu(menu)
    if not menu:
        return

    id_menu = str(minta_angka("\nMasukkan ID menu: "))

    ditemukan = False
    for m in menu:
        if m[0] == id_menu:
            print(f"Stok '{m[1]}' saat ini: {m[4]}")
            m[4] = str(minta_angka(f"Stok baru untuk '{m[1]}': "))
            ditemukan = True
            break

    if ditemukan:
        simpan_menu(menu)
        print("Stok berhasil diperbarui!")
    else:
        print("ID menu tidak ditemukan.")


def riwayat_penjualan():
    if not FILE_TRANSAKSI.exists():
        print("Belum ada data transaksi.")
        return