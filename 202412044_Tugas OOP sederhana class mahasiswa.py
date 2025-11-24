class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan diri
    def perkenalan_diri(self):
        print(f"Hallo, nama saya {self.nama} ({self.nim}) dari jurusan {self.jurusan}.")
        print(f"Saya berasal dari {Mahasiswa.universitas}.\n")

    # Method untuk update IPK
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        print(f"IPK {self.nama} telah diperbarui menjadi {self.ipk}\n")

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


# -----------------------------
# INSTANSIASI 3 OBJECT
# -----------------------------
m1 = Mahasiswa("Helwina", "202412040", "Teknik Informatika", 3.6)
m2 = Mahasiswa("Nazwa", "202413041", "Bisnis Digital", 3.1)
m3 = Mahasiswa("Zahra", "202414042", "Sistem Informasi", 2.4)

# Demonstrasi semua method
print("=== PERKENALAN DIRI ===")
m1.perkenalan_diri()
m2.perkenalan_diri()
m3.perkenalan_diri()

print("=== UPDATE IPK ===")
m3.update_ipk(2.8)  # memperbarui IPK Cici

print("=== PREDIKAT KELULUSAN ===")
print(f"{m1.nama}: {m1.predikat_kelulusan()}")
print(f"{m2.nama}: {m2.predikat_kelulusan()}")
print(f"{m3.nama}: {m3.predikat_kelulusan()}")
