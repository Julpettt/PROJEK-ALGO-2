from modules.login import halaman_utama_login


def main():
    role, username = halaman_utama_login()

    if role == "user":
        print("\n========== HALAMAN PEMBELI ==========")
        print(f"Halo, {username}!")

    elif role == "Admin":
        print("\n========== HALAMAN ADMIN ==========")
        print(f"Halo, {username}!")

    else:
        print("\nProgram selesai.")


if __name__ == "__main__":
    main()