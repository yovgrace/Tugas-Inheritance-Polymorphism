class ManajerInventori:
    def __init__(self):
        # Inventori disimpan dalam dictionary: {nama_barang: jumlah}
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah > 0:
            if nama in self.inventori:
                self.inventori[nama] += jumlah
            else:
                self.inventori[nama] = jumlah
            return f"{jumlah} {nama} berhasil ditambahkan."
        return "Jumlah harus lebih dari 0."

    def hapus_barang(self, nama, jumlah):
        if nama in self.inventori:
            if 0 < jumlah <= self.inventori[nama]:
                self.inventori[nama] -= jumlah
                if self.inventori[nama] == 0:
                    del self.inventori[nama]
                return f"{jumlah} {nama} berhasil dihapus."
            return "Jumlah tidak valid."
        return f"{nama} tidak ditemukan dalam inventori."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        return "\n".join([f"{barang}: {jumlah}" for barang, jumlah in self.inventori.items()])
