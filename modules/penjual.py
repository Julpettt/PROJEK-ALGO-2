import csv
import pathlib

Base_DIR = pathlib.Path(__file__).resolve().parent.parent
file_menu = Base_DIR / 'data' / 'menu.csv'


def baca_menu():
    menu = []
    with open(file_menu, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            menu.append(row)

    return menu

def simpan_menu(menu):
    with open(file_menu, mode='w', newline='') as file:
        fieldnames = ['ID', 'Nama', 'Harga', 'Stok']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for item in menu:
            writer.writerow(item)

def tampilkan_menu():
    menu = baca_menu()

    print("\n=======DAFTAR MENU=======")
    if not menu:
        print("Belum Ada Menu Tersedia.")
        return
    for item in menu:
        print(
            f"{item['ID']:<5} "
            f"{item['Nama']:<20} "
            f"Rp{item['Harga']:<10} "
            f"{item['Stok']:<5}"
        )

def tambah_menu():
    menu = baca_menu()

    print("\n=======TAMBAH MENU=======")
    nama_menu = input("Masukkan nama menu: ")
    harga = input("Masukkan harga menu: ")
    stok = input("Masukkan stok menu: ")

    if menu:
        id_baru = max(int(item["ID"]) for item in menu) + 1
    else:
        id_baru = 1

    menu_baru = {
        "ID": str(id_baru),
        "Nama": nama_menu,
        "Harga": str(harga),
        "Stok": str(stok)
    }

    menu.append(menu_baru)
    simpan_menu(menu)

    print("\nMenu berhasil ditambahkan!")

def hapus_menu():
    menu = baca_menu()

    print("\n=======HAPUS MENU=======")
    tampilkan_menu()
    id_hapus = input("Masukkan ID menu yang ingin dihapus: ")

    menu_dihapus = False
    for item in menu:
        if item["ID"] == id_hapus:
            menu.remove(item)
            menu_dihapus = True
            break

    if menu_dihapus:
        simpan_menu(menu)
        print("\nMenu berhasil dihapus!")
    else:
        print("\nMenu dengan ID tersebut tidak ditemukan.")
