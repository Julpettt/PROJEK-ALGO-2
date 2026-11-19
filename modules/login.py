import csv
import pathlib

Base_DIR = pathlib.Path(__file__).resolve().parent.parent
FILE_USER = Base_DIR / "data" / "user.csv"


# Membaca data akun dari CSV
def baca_user():
    users = []

    with open(FILE_USER, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            users.append(row)

    return users


# Proses login akun
def login_akun(role):
    users = baca_user()

    print("\n======= LOGIN PAGE =======")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    for akun in users:
        print("DATA CSV:", repr(akun))

        csv_username = akun["Username"].strip()
        csv_password = akun["Password"].strip()
        csv_role = akun["Role"].strip().lower()

        if (
            csv_username == username
            and csv_password == password
            and csv_role == role.lower()
        ):
            print("\nLogin berhasil!")
            print(f"Selamat datang, {username}!")
            return username

    print("\nLogin gagal! Username atau password salah.")
    return None


# Halaman utama login
def halaman_utama_login():
    while True:
        print("\n================================")
        print("       🍔 SELAMAT DATANG 🍔")
        print("================================")
        print("1. Masuk sebagai pembeli (Guest)")
        print("2. Login sebagai pembeli")
        print("3. Login sebagai penjual (Admin)")
        print("4. Keluar")
        print("================================")

        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ").strip()

        if pilihan == "1":
            print("\nAnda masuk sebagai pembeli (Guest).")
            return "guest", "Guest"

        elif pilihan == "2":
            username = login_akun("user")

            if username:
                return "user", username

        elif pilihan == "3":
            username = login_akun("admin")

            if username:
                return "admin", username

        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            return None, None

        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
