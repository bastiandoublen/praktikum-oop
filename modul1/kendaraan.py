class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun


# Membuat object
mobil = Kendaraan("Toyota", "Hitam", 2022)
motor = Kendaraan("Honda", "Merah", 2023)

# Mengakses instance attribute
print("=== Instance Attribute ===")
print(f"Mobil: {mobil.merk}, {mobil.warna}, {mobil.tahun}")
print(f"Motor: {motor.merk}, {motor.warna}, {motor.tahun}")

# Mengakses class attribute
print("\n=== Class Attribute ===")
print(f"Melalui class: {Kendaraan.bahan_bakar}")
print(f"Melalui mobil: {mobil.bahan_bakar}")
print(f"Melalui motor: {motor.bahan_bakar}")