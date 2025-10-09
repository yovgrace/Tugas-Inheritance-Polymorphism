# Template awal untuk Tugas 2

class Pelanggan:
    def __init__(self, nama, email):
        # Implementasi: inisialisasi pelanggan dengan keranjang dan riwayat pesanan
        print(f"Pelanggan '{nama}' dengan email '{email}' telah dibuat.")

    def buat_pesanan(self):
        # Implementasi: buat pesanan dari keranjang
        print("Pesanan baru telah dibuat dari keranjang.")


class Produk:
    def __init__(self, nama, harga, stok):
        # Implementasi: inisialisasi produk
        print(f"Produk '{nama}' dengan harga {harga} dan stok {stok} telah ditambahkan.")


class Keranjang:
    def __init__(self):
        # Implementasi: inisialisasi keranjang kosong
        print("Keranjang baru telah dibuat.")

    def tambah_produk(self, produk, jumlah):
        # Implementasi: tambahkan produk ke keranjang
        print(f"Produk '{produk}' sebanyak {jumlah} telah ditambahkan ke keranjang.")


class Pesanan:
    def __init__(self, pelanggan):
        # Implementasi: inisialisasi pesanan
        print(f"Pesanan untuk pelanggan '{pelanggan}' telah dibuat.")


class ItemPesanan:
    def __init__(self, produk, jumlah):
        # Implementasi: inisialisasi item pesanan
        print(f"Item pesanan: produk '{produk}', jumlah {jumlah}.")


# ==========================
# Contoh Penggunaan Program
# ==========================

# Membuat pelanggan
pelanggan1 = Pelanggan("Yovitha", "yovitha@email.com")

# Membuat produk
produk1 = Produk("Buku Catatan", 15000, 20)
produk2 = Produk("Pulpen", 5000, 50)

# Membuat keranjang
keranjang1 = Keranjang()

# Menambahkan produk ke keranjang
keranjang1.tambah_produk("Buku Catatan", 2)
keranjang1.tambah_produk("Pulpen", 3)

# Membuat pesanan
pesanan1 = Pesanan("Yovitha")

# Membuat item pesanan
item1 = ItemPesanan("Buku Catatan", 2)
item2 = ItemPesanan("Pulpen", 3)

# Pelanggan membuat pesanan
pelanggan1.buat_pesanan()
