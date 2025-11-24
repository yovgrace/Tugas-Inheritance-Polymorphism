class ManajerInventori:
    def __init__(self):
        # Menyimpan data inventori dalam bentuk dictionary
        self.inventori = {}   # {nama_barang: jumlah}

    def tambah_barang(self, nama, jumlah):
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0."
        
        if nama in self.inventori:
            self.inventori[nama] += jumlah   # Tambah stok
        else:
            self.inventori[nama] = jumlah    # Barang baru

        return f"Stok {nama} bertambah {jumlah}. Total: {self.inventori[nama]}"

    def kurangi_barang(self, nama, jumlah):
        if nama not in self.inventori:
            return f"{nama} tidak ada di inventori."

        if jumlah <= 0:
            return "Jumlah harus lebih dari 0."

        if jumlah > self.inventori[nama]:
            return "Stok tidak mencukupi."

        self.inventori[nama] -= jumlah   # Kurangi stok

        if self.inventori[nama] == 0:
            del self.inventori[nama]     # Hapus jika stok habis

        return f"Stok {nama} berkurang {jumlah}."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."

        return "\n".join([f"{barang}: {jumlah}" for barang, jumlah in self.inventori.items()])
