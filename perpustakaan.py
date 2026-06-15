from menu_tambah import menu_tambah
from manajemen_koleksi import menu_hapus, menu_tampil

class Perpustakaan:
    def __init__(self):
        self.daftar_koleksi = []

    def wait_enter(self):
        input("Tekan [ENTER] untuk kembali ke menu program")
        print("\n" + "="*50 + "\n")

    def run(self):
        while True:
            print("-"*50)
            print("="*18, "MENU PROGRAM", "="*18)
            print("-"*50)
            print("  1. Tambah data koleksi")
            print("  2. Hapus data koleksi")
            print("  3. Tampil semua data koleksi")
            print("  4. Keluar\n")

            pilihan = input("Nomor yang dipilih: ")

            if pilihan == '1':
                menu_tambah(self.daftar_koleksi)
                self.wait_enter()
            elif pilihan == '2':
                menu_hapus(self.daftar_koleksi)
                self.wait_enter()
            elif pilihan == '3':
                menu_tampil(self.daftar_koleksi)
                self.wait_enter()
            elif pilihan == '4':
                print("\nTerima kasih telah menggunakan program perpustakaan.")
                break
            else:
                print("Pilihan tidak valid! Silakan coba lagi.\n")