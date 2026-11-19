class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"{self.nama} (NIDN: {self.nidn}) mengajar {mata_kuliah}"


# Membuat 2 object dosen
dosen1 = Dosen("Abadi Nugroho", "0012345678")
dosen2 = Dosen("Siti Rahma", "0098765432")

# Memanggil method
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Basis Data"))