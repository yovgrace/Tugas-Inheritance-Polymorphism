class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info(self):
        return f"Kendaraan {self.merk} berwarna {self.warna} tahun {self.tahun}"
