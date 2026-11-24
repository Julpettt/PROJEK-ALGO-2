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