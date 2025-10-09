# Template Program: Sistem Manajemen Perusahaan

class Perusahaan:
    def __init__(self, nama):
        # Inisialisasi perusahaan dengan daftar proyek dan tim
        self.nama = nama
        self.daftar_proyek = []
        self.daftar_tim = []

    def buat_proyek(self, nama_proyek, deskripsi):
        # Membuat proyek baru dan menambahkannya ke daftar proyek
        proyek = Proyek(nama_proyek, deskripsi)
        self.daftar_proyek.append(proyek)
        print(f"Proyek '{nama_proyek}' berhasil dibuat.")
        return proyek

    def buat_tim(self, nama_tim):
        # Membuat tim baru dan menambahkannya ke daftar tim
        tim = Tim(nama_tim)
        self.daftar_tim.append(tim)
        print(f"Tim '{nama_tim}' berhasil dibuat.")
        return tim


class Proyek:
    def __init__(self, nama, deskripsi):
        # Inisialisasi proyek dengan daftar tugas
        self.nama = nama
        self.deskripsi = deskripsi
        self.daftar_tugas = []

    def tambah_tugas(self, deskripsi_tugas):
        # Menambahkan tugas baru ke proyek
        tugas = Tugas(deskripsi_tugas)
        self.daftar_tugas.append(tugas)
        print(f"Tugas '{deskripsi_tugas}' telah ditambahkan ke proyek '{self.nama}'.")
        return tugas


class Tim:
    def __init__(self, nama):
        # Inisialisasi tim dengan daftar developer
        self.nama = nama
        self.developer = []

    def tambah_developer(self, developer):
        # Menambahkan developer ke tim
        self.developer.append(developer)
        print(f"Developer '{developer.nama}' dengan keahlian '{developer.keahlian}' telah ditambahkan ke tim '{self.nama}'.")


class Developer:
    def __init__(self, nama, keahlian):
        # Inisialisasi developer dengan nama dan keahlian
        self.nama = nama
        self.keahlian = keahlian


class Tugas:
    def __init__(self, deskripsi):
        # Inisialisasi tugas dengan deskripsi dan developer kosong
        self.deskripsi = deskripsi
        self.developer = None

    def tugaskan_ke(self, developer):
        # Menugaskan tugas ke developer tertentu
        self.developer = developer
        print(f"Tugas '{self.deskripsi}' telah ditugaskan ke developer '{developer.nama}'.")


# ===========================================
# Contoh Penggunaan Program
# ===========================================

# Membuat perusahaan
perusahaan = Perusahaan("Tech Innovators")

# Membuat proyek dan tim
proyek1 = perusahaan.buat_proyek("Sistem HR", "Membangun sistem manajemen karyawan")
tim1 = perusahaan.buat_tim("Tim Backend")

# Membuat developer dan menambahkannya ke tim
dev1 = Developer("Yovitha Gracia", "Python Developer")
dev2 = Developer("Andi Setiawan", "Database Engineer")
tim1.tambah_developer(dev1)
tim1.tambah_developer(dev2)

# Menambahkan tugas ke proyek dan menugaskannya ke developer
tugas1 = proyek1.tambah_tugas("Membuat API untuk login")
tugas1.tugaskan_ke(dev1)
