import csv
import pathlib

Base_DIR = pathlib.Path(__file__).resolve().parent.parent
FILE_USER = Base_DIR / 'data' / 'user.csv'



def baca_user():
    users = []
    with open(FILE_USER, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

def login_akun(role):
    users = baca_user()

    print("\n=======LOGIN PAGE=======")

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    for akun in users:
        if (
            akun["Username"] == username
            and akun["Password"] == password
            and akun["Role"] == role
        ):
            print("\nLogin berhasil!")
            print(f"Selamat datang, {username}!")
            return username

print("\nLogin gagal! Username atau password salah.")



def halaman_utama_login():
    while True:
        print("\n================================")
        print("🍔 SELAMAT DATANG 🍔")
        print("1. masuk sebagai pembeli(Guest)")
        print("2. login sebagai pembeli")
        print("3. login sebagai penjual(Admin)")
        print("4. keluar")
        print("\n================================")

        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

        if pilihan == "1":
            print("\nAnda masuk sebagai pembeli(Guest).")
            return "guest"
        elif pilihan == "2":
            username = login_akun("user")
            
            if username:
                return "user", username

        elif pilihan == "3":
            username = login_akun("Admin")

            if username:
                return "Admin", username

        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            exit()
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")  