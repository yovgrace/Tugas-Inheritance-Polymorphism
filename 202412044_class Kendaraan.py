class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Kendaraan {self.merk} tahun {self.tahun}"
