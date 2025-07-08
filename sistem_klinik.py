# manajemen_klinik.py
# Program Manajemen Klinik Sederhana (OOP CRUD dengan class diakhiri 33)

# Class Pasien33
class Pasien33:  # Mendefinisikan class Pasien33 untuk menyimpan data pasien
    def __init__(self, nama, umur):  # Konstruktor dengan parameter nama dan umur
        self.nama = nama  # Menyimpan nama pasien ke atribut nama
        self.umur = umur  # Menyimpan umur pasien ke atribut umur

# Class Dokter33
class Dokter33:  # Mendefinisikan class Dokter33 untuk menyimpan data dokter
    def __init__(self, nama, spesialis):  # Konstruktor dengan parameter nama dan spesialis
        self.nama = nama  # Menyimpan nama dokter ke atribut nama
        self.spesialis = spesialis  # Menyimpan spesialis dokter ke atribut spesialis

# Class JadwalJanji33
class JadwalJanji33:  # Mendefinisikan class JadwalJanji33 untuk menyimpan data janji temu
    def __init__(self, pasien, dokter, tanggal):  # Konstruktor dengan parameter pasien, dokter, dan tanggal
        self.pasien = pasien  # Menyimpan objek pasien ke atribut pasien
        self.dokter = dokter  # Menyimpan objek dokter ke atribut dokter
        self.tanggal = tanggal  # Menyimpan tanggal janji temu ke atribut tanggal

# Class Klinik33
class Klinik33:  # Mendefinisikan class Klinik33 sebagai manajemen utama klinik
    def __init__(self):  # Konstruktor tanpa parameter tambahan
        self.pasien = []  # Membuat list kosong untuk menyimpan objek Pasien33
        self.dokter = []  # Membuat list kosong untuk menyimpan objek Dokter33
        self.jadwal = []  # Membuat list kosong untuk menyimpan objek JadwalJanji33

    # CREATE pasien
    def tambah_pasien(self):  # Method untuk menambahkan pasien baru
        nama = input("Masukkan nama pasien: ")  # Input nama pasien
        umur = input("Masukkan umur pasien: ")  # Input umur pasien
        self.pasien.append(Pasien33(nama, umur))  # Membuat objek Pasien33 dan menambahkannya ke list pasien
        print("Pasien berhasil ditambahkan.\n")  # Output konfirmasi berhasil

    # READ semua data pasien
    def lihat_pasien(self):  # Method untuk melihat semua data pasien
        print("\n=== Data Pasien ===")  # Judul tampilan
        if self.pasien:  # Jika list pasien tidak kosong
            for p in self.pasien:  # Loop setiap pasien dalam list
                print(f"Nama: {p.nama}, Umur: {p.umur}")  # Tampilkan nama dan umur pasien
        else:  # Jika list pasien kosong
            print("Belum ada data pasien.")  # Output jika tidak ada pasien
        print()  # Baris kosong

    # UPDATE data pasien
    def update_pasien(self):  # Method untuk mengupdate data pasien
        nama_cari = input("Masukkan nama pasien yang ingin diupdate: ")  # Input nama pasien yang akan dicari
        for p in self.pasien:  # Loop setiap pasien dalam list
            if p.nama == nama_cari:  # Jika nama pasien ditemukan
                p.nama = input("Masukkan nama baru: ")  # Input nama baru
                p.umur = input("Masukkan umur baru: ")  # Input umur baru
                print("Data pasien berhasil diupdate.\n")  # Output konfirmasi berhasil
                return  # Keluar dari method setelah update
        print("Pasien tidak ditemukan.\n")  # Output jika pasien tidak ditemukan

    # DELETE data pasien
    def hapus_pasien(self):  # Method untuk menghapus data pasien
        nama_cari = input("Masukkan nama pasien yang ingin dihapus: ")  # Input nama pasien yang akan dicari
        for p in self.pasien:  # Loop setiap pasien dalam list
            if p.nama == nama_cari:  # Jika nama pasien ditemukan
                self.pasien.remove(p)  # Ha pus objek pasien dari list
                print("Data pasien berhasil dihapus.\n")  # Output konfirmasi berhasil
                return  # Keluar dari method setelah hapus
        print("Pasien tidak ditemukan.\n")  # Output jika pasien tidak ditemukan

    # Menu utama dengan CRUD
    def menu(self):  # Method untuk menampilkan dan menjalankan menu utama
        while True:  
        # Looping tanpa batas sampai user memilih keluar
            print("=== Manajemen Klinik CRUD ===")  # Judul menu
            print("1. Tambah Pasien (Create)")  # Opsi 1
            print("2. Lihat Pasien (Read)")  # Opsi 2
            print("3. Update Data Pasien (Update)")  # Opsi 3
            print("4. Hapus Data Pasien (Delete)")  # Opsi 4
            print("5. Keluar")  # Opsi 5

            pilihan = input("Pilih menu (1-5): ")  # Input pilihan menu
            if pilihan == '1':  # Jika memilih 1
                self.tambah_pasien()  # Panggil method tambah_pasien
            elif pilihan == '2':  # Jika memilih 2
                self.lihat_pasien()  # Panggil method lihat_pasien
            elif pilihan == '3':  # Jika memilih 3
                self.update_pasien()  # Panggil method update_pasien
            elif pilihan == '4':  # Jika memilih 4
                self.hapus_pasien()  # Panggil method hapus_pasien
            elif pilihan == '5':  # Jika memilih 5
                print("Program selesai.")  # Output konfirmasi keluar
                break  
            # Hentikan loop dan keluar program
            else:  # Jika input tidak valid
                print("Pilihan tidak valid.\n")  
                # Output error

# Menjalankan program utama
if __name__ == "__main__": 
     # Mengecek jika file dijalankan langsung, bukan diimport
    klinik = Klinik33()  # Membuat objek Klinik33
    klinik.menu()  # Memanggil method menu untuk menjalankan program