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

    transaksi = []
    with open(FILE_TRANSAKSI, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        baris_pertama = True
        for row in reader:
            if baris_pertama:
                baris_pertama = False
            else:
                if len(row) >= 3:
                    transaksi.append(row)

    print("\n=== RIWAYAT PENJUALAN ===")
    if not transaksi:
        print("Belum ada data transaksi.")
        return

    print(f"{'No':<4}{'ID Transaksi':<15}{'User':<20}{'Total':>12}")
    print("-" * 55)
    grand_total = 0
    nomor = 1
    for t in transaksi:
        sub = int(t[2])
        grand_total += sub
        print(f"{nomor:<4}{t[0]:<15}{t[1]:<20}{format_rp(sub):>12}")
        nomor += 1
    print("-" * 55)
    print(f"{'Grand Total':>39}{format_rp(grand_total):>16}")
    
    
    def pesan_makanan(username="Guest"):
        menu = baca_menu()
        if not menu:
            print("Menu masih kosong.")
            return
    
        pesanan = []
    
        while True:
            tampilkan_menu(menu)
            id_pilih = str(minta_angka("Masukkan ID menu (0 = selesai): "))
    
            if id_pilih == "0":
                break
    
            target = None
            for m in menu:
                if m[0] == id_pilih:
                    target = m
                    break
    
            if target is None:
                print("ID menu tidak ditemukan!")
                continue
    
            stok  = int(target[4])
            jumlah = minta_angka("Jumlah: ")
    
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
            elif jumlah > stok:
                print(f"Stok tidak cukup! Sisa stok: {stok}")
            else:
                harga    = int(target[3])
                subtotal = harga * jumlah
                pesanan.append({
                    "id": id_pilih,
                    "nama": target[1],
                    "jumlah": jumlah,
                    "subtotal": subtotal
                })
                target[4] = str(stok - jumlah)
                print(f"\nBerhasil memesan: {target[1]} x {jumlah} ({format_rp(subtotal)})")
    
                print("\n--------------------------------")
                print("1. Pesan lagi")
                print("2. Selesai pesan")
                print("--------------------------------")
                if input("Pilih (1/2): ").strip() == "2":
                    break
    
        if not pesanan:
            print("\nTidak ada pesanan. Kembali ke menu utama...")
            return
    
        print("\n" + "=" * 45)
        print("TOTAL PEMBAYARAN PESANAN".center(45))
        print("=" * 45)
        total_bayar = 0
        for p in pesanan:
            print(f"- {p['nama']:<20} x {p['jumlah']:<3} = {format_rp(p['subtotal']):>14}")
            total_bayar += p["subtotal"]
        print("-" * 45)
        print(f"{'TOTAL HARGA:':<25}{format_rp(total_bayar):>20}")
        print("=" * 45)
    
        simpan_menu(menu)
    
        id_transaksi = 1
        if FILE_TRANSAKSI.exists():
            with open(FILE_TRANSAKSI, "r", newline="", encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                baris_pertama = True
                for row in reader:
                    if baris_pertama:
                        baris_pertama = False
                    else:
                        if len(row) >= 1 and int(row[0]) >= id_transaksi:
                            id_transaksi = int(row[0]) + 1
    
        with open(FILE_DETAIL, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            for p in pesanan:
                w.writerow([id_transaksi, p["id"], p["jumlah"], p["subtotal"]])
    
        with open(FILE_TRANSAKSI, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([id_transaksi, username, total_bayar])
    
        print(f"\nPesanan berhasil disimpan! ID Transaksi: #{id_transaksi}")
        print("Kembali ke menu utama...")
    
    
    def hitung_total():
        if not FILE_DETAIL.exists():
            print("Belum ada data transaksi.")
            return
    
        data = []
        with open(FILE_DETAIL, "r", newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            baris_pertama = True
            for row in reader:
                if baris_pertama:
                    baris_pertama = False
                else:
                    if len(row) >= 4:
                        data.append(row)
    
        if not data:
            print("Belum ada pesanan.")
            return
    
        id_terakhir = data[-1][0]
    
        menu      = baca_menu()
        menu_dict = {m[0]: m[1] for m in menu}
    
        print(f"\n=== RINCIAN PEMBAYARAN (Transaksi #{id_terakhir}) ===")
        total = 0
        for d in data:
            if d[0] == id_terakhir:
                nama = menu_dict.get(d[1], f"Menu {d[1]}")
                sub  = int(d[3])
                total += sub
                print(f"- {nama:<20} x {d[2]:<3} = {format_rp(sub):>12}")
        print("-" * 40)
        print(f"{'TOTAL PEMBAYARAN:':<24}{format_rp(total):>16}")
    
    
    def riwayat_transaksi(username):
        if not FILE_DETAIL.exists():
            print("Belum ada riwayat transaksi.")
            return
    
        id_milik_user = set()
        if FILE_TRANSAKSI.exists():
            with open(FILE_TRANSAKSI, "r", newline="", encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if len(row) >= 2 and row[1] == username:
                        id_milik_user.add(row[0])
    
        data = []
        with open(FILE_DETAIL, "r", newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            baris_pertama = True
            for row in reader:
                if baris_pertama:
                    baris_pertama = False
                else:
                    if len(row) >= 4 and row[0] in id_milik_user:
                        data.append(row)
    
        if not data:
            print("Belum ada riwayat transaksi.")
            return
    
        menu      = baca_menu()
        menu_dict = {m[0]: m[1] for m in menu}
    
        print("\n=== RIWAYAT TRANSAKSI ===")
        id_sebelumnya = ""
        total_semua   = 0
        for d in data:
            if d[0] != id_sebelumnya:
                print(f"\n[ Transaksi #{d[0]} ]")
                id_sebelumnya = d[0]
            nama = menu_dict.get(d[1], f"Menu {d[1]}")
            sub  = int(d[3])
            total_semua += sub
            print(f"  - {nama:<20} x {d[2]:<3} = {format_rp(sub):>12}")
        print("-" * 40)
        print(f"{'Total Semua:':<24}{format_rp(total_semua):>16}")
    
    
    def login_akun(role):
        users = baca_user()
        print("\n======= LOGIN PAGE =======")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
    
        for acc in users:
            if acc[0] == username and acc[1] == password and acc[2].lower() == role.lower():
                print(f"\nLogin berhasil! Selamat datang, {username}!")
                return username
    
        print("\nLogin gagal! Username atau password salah.")
        return None
    
    
    def signup():
        print("\n===== SIGN UP =====")
        username = input("Masukkan Username baru: ").strip()
        password = input("Buat Password: ").strip()
    
        if len(username) < 3:
            print("Username terlalu pendek (minimal 3 karakter). Silahkan coba lagi!")
            return
    
        if password == "":
            print("Password tidak boleh kosong. Silahkan coba lagi!")
            return
    
        users = baca_user()
        for acc in users:
            if acc[0].lower() == username.lower():
                print("Username sudah terdaftar. Silahkan login atau gunakan Username lain!")
                return
    
        users.append([username, password, "User"])
        simpan_user(users)
    
        print("\nPendaftaran berhasil!")
        print("Silahkan login menggunakan akun baru Anda.")
    
    
    def lupa_password():
        print("\n===== LUPA PASSWORD =====")
        username = input("Masukkan Username Anda: ").strip()
    
        users     = baca_user()
        ditemukan = False
    
        for acc in users:
            if acc[0].lower() == username.lower():
                new_password = input("Masukkan Password Baru: ").strip()
    
                if new_password == "":
                    print("Password baru tidak boleh kosong. Silakan coba lagi.")
                    return
    
                acc[1] = new_password
                ditemukan = True
                break
    
        if ditemukan:
            simpan_user(users)
            print("\nPassword berhasil diperbarui!")
        else:
            print("Username tidak ditemukan.")
    
    
    def menu_login_pembeli():
        while True:
            print("\n================================")
            print("     MENU LOGIN PEMBELI")
            print("================================")
            print("1. Login")
            print("2. Sign Up")
            print("3. Lupa Password")
            print("4. Kembali")
            print("================================")
    
            pilihan = input("Masukkan pilihan Anda (1/2/3/4): ").strip()
    
            match pilihan:
                case "1":
                    u = login_akun("User")
                    if u is not None:
                        return u
                case "2":
                    signup()
                case "3":
                    lupa_password()
                case "4":
                    return None
                case _:
                    print("\nPilihan tidak valid. Silakan coba lagi.")
    
    
    def dashboard_user(username):
        while True:
            print(f"\n=== DASHBOARD PEMBELI — {username} ===")
            print("1. Lihat Daftar Menu")
            print("2. Cari Menu")
            print("3. Pesan Makanan")
            print("4. Hitung Total Pembayaran")
            print("5. Riwayat Transaksi")
            print("6. Keluar")
    
            pilihan = input("Pilih menu (1-6): ").strip()
    
            match pilihan:
                case "1": tampilkan_menu()
                case "2": cari_menu()
                case "3": pesan_makanan(username)
                case "4": hitung_total()
                case "5": riwayat_transaksi(username)
                case "6":
                    print("Keluar dari dashboard pembeli.")
                    break
                case _:
                    print("Pilihan tidak valid!")
    
    
    def dashboard_admin(username):
        while True:
            print(f"\n=== DASHBOARD ADMIN — {username} ===")
            print("1. Tambah Menu")
            print("2. Hapus Menu")
            print("3. Lihat Daftar Menu")
            print("4. Update Stok Menu")
            print("5. Riwayat Penjualan")
            print("6. Keluar")
    
            pilihan = input("Pilih menu (1-6): ").strip()
    
            match pilihan:
                case "1": tambah_menu()
                case "2": hapus_menu()
                case "3": tampilkan_menu()
                case "4": update_stok()
                case "5": riwayat_penjualan()
                case "6":
                    print("Keluar dari dashboard admin.")
                    break
                case _:
                    print("Pilihan tidak valid!")
    
    
    def main():
        init_data()
    
        while True:
            print("\n================================")
            print("       🍔 SELAMAT DATANG 🍔     ")
            print("================================")
            print("1. Login sebagai pembeli")
            print("2. Login sebagai penjual (Admin)")
            print("3. Keluar")
            print("================================")
    
            pilihan = input("Pilih menu (1-3): ").strip()
    
            match pilihan:
                case "1":
                    u = menu_login_pembeli()
                    if u is not None:
                        dashboard_user(u)
                case "2":
                    u = login_akun("Admin")
                    if u is not None:
                        dashboard_admin(u)
                case "3":
                    print("Program selesai. Sampai jumpa!")
                    break
                case _:
                    print("Pilihan tidak valid!")
    
    
    if __name__ == "__main__":
        main()
    