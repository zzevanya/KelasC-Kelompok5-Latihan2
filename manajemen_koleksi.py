def menu_hapus(daftar_koleksi):
    print("- HAPUS DATA KOLEKSI -")
    kode = input("Masukkan Kode Koleksi   : ")

    ditemukan = False 
    for koleksi in daftar_koleksi:
        if koleksi.kode_koleksi == kode:
            daftar_koleksi.remove(koleksi)
            ditemukan = True
            break

    print("-"*50)

    if ditemukan:
        print("Hapus data koleksi sukses!!1 ")
    else:
        print("Data dengan kode tersebut tidak ditemukan.\n")

def menu_tampil(daftar_koleksi):
    print("-"*50)
    print("="*18, "DATA KOLEKSI", "="*18)
    print("-"*50)
    if not daftar_koleksi:
        print("[ Belum ada data koleksi ]\n")

    else:
        for i, koleksi in enumerate(daftar_koleksi, start=1):
            koleksi.tampilkan_info(i)
            print("-"*50)