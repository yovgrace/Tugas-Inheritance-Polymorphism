class Kendaraan:
    # Class attribute (dimiliki bersama oleh semua object)
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk          # Instance attribute
        self.warna = warna        # Instance attribute
        self.tahun = tahun        # Instance attribute

    def info(self):
        return f"{self.merk} - {self.warna} ({self.tahun})"


# Membuat object
mobil1 = Kendaraan("Toyota", "Merah", 2020)
mobil2 = Kendaraan("Honda", "Biru", 2022)

# Mengakses instance attribute (unik tiap object)
print(mobil1.info())  # menggunakan atribut merk, warna, tahun dari mobil1
print(mobil2.info())  # menggunakan atribut merk, warna, tahun dari mobil2

# Mengakses class attribute (sama untuk semua object)
print(mobil1.bahan_bakar)
print(mobil2.bahan_bakar)

# Mengakses class attribute langsung melalui nama class
print(Kendaraan.bahan_bakar)
