class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Halo, saya Dosen {self.nama} dengan NIDN {self.nidn}"

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Saya mengajar mata kuliah {mata_kuliah}"


# Pembuatan object
dsn1 = Dosen("Dr. Andi Pratama", "123456")
dsn2 = Dosen("Prof. Rina Kartika", "654321")

# Pemanggilan method
print(dsn1.perkenalan())
print(dsn1.ajar_mata_kuliah("Pemrograman Python"))

print(dsn2.perkenalan())
print(dsn2.ajar_mata_kuliah("Basis Data"))
