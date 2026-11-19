class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0"

        self.inventori[nama] = self.inventori.get(nama, 0) + jumlah
        return f"Ditambah {jumlah} {nama}. Stok: {self.inventori[nama]}"

    def hapus_barang(self, nama, jumlah):
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0"

        if nama not in self.inventori:
            return f"Barang {nama} tidak ditemukan"

        if jumlah > self.inventori[nama]:
            return f"Stok {nama} tidak mencukupi"

        self.inventori[nama] -= jumlah
        sisa = self.inventori[nama]

        if sisa == 0:
            del self.inventori[nama]

        return f"Dikurangi {jumlah} {nama}. Sisa stok: {sisa}"

    def lihat_inventori(self):
        if not self.inventori:
            print("Inventori kosong")
            return

        print("=== DAFTAR INVENTORI ===")
        for nama, jumlah in self.inventori.items():
            print(f"{nama}: {jumlah} unit")


# Membuat object
manajer = ManajerInventori()

# Menambahkan barang
print(manajer.tambah_barang("Keyboard", 10))
print(manajer.tambah_barang("Mouse", 5))
print(manajer.tambah_barang("Keyboard", 3))

# Melihat inventori
manajer.lihat_inventori()

# Mengurangi stok
print("\n=== PENGURANGAN STOK ===")
print(manajer.hapus_barang("Keyboard", 4))
print(manajer.hapus_barang("Mouse", 2))

# Melihat inventori akhir
manajer.lihat_inventori()