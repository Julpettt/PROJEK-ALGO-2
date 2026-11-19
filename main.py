from modules.login import halaman_utama_login
from modules.penjual import tambah_menu, hapus_menu, tampilkan_menu


def dashboard_penjual(username):
    while True:
        print("\n================================")
        print("       DASHBOARD PENJUAL")
        print("================================")
        print("1. Tambah Menu")
        print("2. Hapus Menu")
        print("3. Lihat Daftar Menu")
        print("4. Keluar")
        print("================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_menu()

        elif pilihan == "2":
            hapus_menu()

        elif pilihan == "3":
            tampilkan_menu()

        elif pilihan == "4":
            print("Keluar dari dashboard penjual.")
            break

        else:
            print("Pilihan tidak valid!")


def main():
    role, username = halaman_utama_login()

    if role == "admin":
        print(f"\nSelamat datang, Admin {username}!")
        dashboard_penjual(username)

    elif role == "user":
        print("Dashboard pembeli belum dibuat.")

    elif role == "guest":
        print("Masuk sebagai Guest.")

    else:
        print("Program selesai.")


if __name__ == "__main__":
    main()