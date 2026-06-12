from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit):
        self.kode_koleksi = kode_koleksi
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit
        
    @abstractmethod
    def tampilkan_info(self, index):
        pass
    
class Buku(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, pengarang):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.pengarang = pengarang
        
    def tampilkan_info(self, index):
        print(f" Koleksi {index}")
        print(f" Jenis: Buku \n Kode Koleksi: {self.kode_koleksi} \n Judul: {self.judul} \n Tahun Terbit: {self.tahun_terbit} \n Pengarang: {self.pengarang} \n Penerbit: {self.penerbit} \n")
        
class Majalah(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, edisi):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit,)
        self.edisi = edisi
        
    def tampilkan_info(self, index):
        print(f" Koleksi {index}")
        print(f" Jenis: Majalah \n Kode Koleksi: {self.kode_koleksi} \n Judul: {self.judul} \n Tahun Terbit: {self.tahun_terbit} \n Penerbit: {self.penerbit} \n Edisi: {self.edisi} \n")
        
        
class Jurnal(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, bidang_studi, impact_factor):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit,)
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor
        
    def tampilkan_info(self, index):
        print(f" Koleksi {index}")
        print(f" Jenis: Jurnal \n Kode Koleksi: {self.kode_koleksi} \n Judul: {self.judul} \n Tahun Terbit: {self.tahun_terbit} \n Penerbit: {self.penerbit} \n Bidang Studi: {self.bidang_studi} \n Impact Factor: {self.impact_factor} \n")