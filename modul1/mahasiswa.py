class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan
    def perkenalan_diri(self):
        return (
            f"Saya {self.nama}, NIM {self.nim}, "
            f"jurusan {self.jurusan}, "
            f"kuliah di {self.universitas}."
        )

    # Method update IPK
    def update_ipk(self, ipk_baru):
        if not 0.0 <= ipk_baru <= 4.0:
            return "IPK harus berada antara 0.0 sampai 4.0"

        self.ipk = ipk_baru
        return f"IPK {self.nama} diperbarui menjadi {self.ipk:.2f}"

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
            return "Belum Lulus"


# Membuat 3 object mahasiswa
mhs1 = Mahasiswa(
    "Bastian Nisfu Nugraha",
    "202512026",
    "Teknik Informatika",
    3.30
)

mhs2 = Mahasiswa(
    "Nadia",
    "202512027",
    "Teknik Informatika",
    2.70
)

mhs3 = Mahasiswa(
    "Raka",
    "202512028",
    "Teknik Informatika",
    2.20
)

# Demonstrasi method
for mahasiswa in (mhs1, mhs2, mhs3):
    print(mahasiswa.perkenalan_diri())
    print(f"IPK: {mahasiswa.ipk:.2f}")
    print(f"Predikat: {mahasiswa.predikat_kelulusan()}")
    print()

# Demonstrasi update IPK
print("=== UPDATE IPK ===")
print(mhs1.update_ipk(3.75))

print(
    f"Predikat setelah update: "
    f"{mhs1.predikat_kelulusan()}"
)

# Akses class attribute
print(f"Class attribute universitas: {Mahasiswa.universitas}")