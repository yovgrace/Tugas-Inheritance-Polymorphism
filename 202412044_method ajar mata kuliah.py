class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Halo, saya Dosen {self.nama} dengan NIDN {self.nidn}"

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Saya mengajar mata kuliah {mata_kuliah}"
