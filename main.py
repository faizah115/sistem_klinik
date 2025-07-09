# main.py

from klinik_service import Klinik33
def main():
    klinik = Klinik33()
    while True:
        print("=== Manajemen Klinik CRUD ===")
        print("1. Tambah Pasien (Create)")
        print("2. Lihat Pasien (Read)")
        print("3. Update Data Pasien (Update)")
        print("4. Hapus Data Pasien (Delete)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            klinik.tambah_pasien()
        elif pilihan == '2':
            klinik.lihat_pasien()
        elif pilihan == '3':
            klinik.update_pasien()
        elif pilihan == '4':
            klinik.hapus_pasien()
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "_main_":
    main()