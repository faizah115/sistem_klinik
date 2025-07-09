# services/klinik_service.py

from entities import Pasien33, Dokter33, JadwalJanji33

class Klinik33:
    def _init_(self):
        self.pasien = []
        self.dokter = []
        self.jadwal = []

    def tambah_pasien(self):
        nama = input("Masukkan nama pasien: ")
        umur = input("Masukkan umur pasien: ")
        self.pasien.append(Pasien33(nama, umur))
        print("Pasien berhasil ditambahkan.\n")

    def lihat_pasien(self):
        print("\n=== Data Pasien ===")
        if self.pasien:
            for p in self.pasien:
                print(f"Nama: {p.nama}, Umur: {p.umur}")
        else:
            print("Belum ada data pasien.\n")

    def update_pasien(self):
        nama_cari = input("Masukkan nama pasien yang ingin diupdate: ")
        for p in self.pasien:
            if p.nama == nama_cari:
                p.nama = input("Masukkan nama baru: ")
                p.umur = input("Masukkan umur baru: ")
                print("Data pasien berhasil diupdate.\n")
                return
        print("Pasien tidak ditemukan.\n")

    def hapus_pasien(self):
        nama_cari = input("Masukkan nama pasien yang ingin dihapus: ")
        for p in self.pasien:
            if p.nama == nama_cari:
                self.pasien.remove(p)
                print("Data pasien berhasil dihapus.\n")
                return
        print("Pasien tidak ditemukan.\n")
