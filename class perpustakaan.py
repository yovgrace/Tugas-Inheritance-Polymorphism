# Template awal untuk Tugas 1

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        # Implementasi: tambahkan atribut untuk koleksi buku dan daftar anggota
        print(f"Perpustakaan '{self.nama}' berhasil dibuat.")

    def tambah_buku(self, buku):
        # Implementasi: tambahkan buku ke koleksi
        print(f"Buku '{buku}' telah ditambahkan ke perpustakaan.")

    def daftar_anggota(self, anggota):
        # Implementasi: tambahkan anggota ke daftar
        print(f"Anggota '{anggota}' telah didaftarkan.")

    def pinjam_buku(self, anggota, buku):
        # Implementasi: proses peminjaman buku oleh anggota
        print(f"Anggota '{anggota}' meminjam buku '{buku}'.")


class Buku:
    def __init__(self, judul, penulis):
        # Implementasi: inisialisasi atribut buku
        print(f"Buku berjudul '{judul}' karya '{penulis}' telah dibuat.")


class Anggota:
    def __init__(self, nama):
        # Implementasi: inisialisasi atribut anggota
        print(f"Anggota baru '{nama}' telah dibuat.")


class Peminjaman:
    def __init__(self, anggota, buku, tanggal_pinjam):
        # Implementasi: inisialisasi transaksi peminjaman
        print(f"Peminjaman: {anggota} meminjam '{buku}' pada tanggal {tanggal_pinjam}.")


# ==========================
# Contoh Penggunaan Program
# ==========================

# Membuat objek perpustakaan
perpus = Perpustakaan("Perpustakaan Kampus")

# Membuat objek buku dan anggota
buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
anggota1 = Anggota("Yovitha Gracia")

# Menambahkan buku dan anggota ke perpustakaan
perpus.tambah_buku("Laskar Pelangi")
perpus.daftar_anggota("Yovitha Gracia")

# Proses peminjaman buku
perpus.pinjam_buku("Yovitha Gracia", "Laskar Pelangi")

# Membuat transaksi peminjaman
peminjaman1 = Peminjaman("Yovitha Gracia", "Laskar Pelangi", "9 Oktober 2025")
