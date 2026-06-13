from koleksi_data import Buku, Majalah, Jurnal

def menu_tambah(daftar_koleksi):
    print("- JENIS KOLEKSI YANG AKAN DITAMBAH -")
    print(" 1. Buku")
    print(" 2. Majalah")
    print(" 3. Jurnal\n")

    pilihan = input("Nomor yang dipilih: ")
    if pilihan not in ['1', '2', '3']:
        print("Pilihan tidak valid!\n")
        return

    print("\n" + "-"*40)

    if pilihan == '1':
        print("TAMBAH DATA BUKU\n")
        kode = input("Masukkan Kode Koleksi   : ")
        judul = input("Masukkan Judul          : ")
        tahun = input("Masukkan Tahun Terbit   : ")
        pengarang = input("Masukkan Pengarang      : ")
        penerbit = input("Masukkan Penerbit       : ")

        daftar_koleksi.append(Buku(kode, judul, tahun, penerbit, pengarang))
        print("Tambah Buku Sukses!!!")

    elif pilihan == '2':
        print("TAMBAH DATA MAJALAH\n")
        kode = input("Masukkan Kode Koleksi   : ")
        judul = input("Masukkan Judul          : ")
        tahun = input("Masukkan Tahun Terbit   : ")
        penerbit = input("Masukkan Penerbit       : ")
        edisi = input("Masukkan Edisi          : ")

        daftar_koleksi.append(Majalah(kode, judul, tahun, penerbit, edisi))
        print("Tambah Buku Sukses!!!")

    elif pilihan == '3':
        print("TAMBAH DATA JURNAL\n")
        kode = input("Masukkan Kode Koleksi   : ")
        judul = input("Masukkan Judul          : ")
        tahun = input("Masukkan Tahun Terbit   : ")
        penerbit = input("Masukkan Penerbit       : ")
        bidang = input("Masukkan Bidang Studi   : ")
        impact = input("Masukkan Impact Factor  : ")

        daftar_koleksi.append(Jurnal(kode, judul, tahun, penerbit, bidang, impact))
        print("Tambah Buku Sukses!!!")