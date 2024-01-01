import os

class Kendaraan:
    def __init__(self, merk, warna, jumlah_roda, kecepatan_maksimum):
        self.merk = merk
        self.warna = warna
        self.jumlah_roda = jumlah_roda
        self.kecepatan_maksimum = kecepatan_maksimum
    def tampilkan_informasi(self):
        print("="*20)
        print(f"Merk: {self.merk}")
        print(f"Warna: {self.warna}")
        print(f"Jumlah roda: {self.jumlah_roda}")
        print(f"Kecepatan maksimum: {self.kecepatan_maksimum}")
    def tampilkan_jarak_tempuh(self, waktu):
        jarak = self.kecepatan_maksimum * waktu
        print(f"Jarak: {jarak} KM")

class Mobil(Kendaraan):
    def __init__(self, merk, warna, jumlah_roda, kecepatan_maksimum, jenis_transmisi):
        super().__init__(merk, warna, jumlah_roda, kecepatan_maksimum)
        self._jenis_transmisi = jenis_transmisi
    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Jenis transmisi: {self._jenis_transmisi}")

class Motor(Kendaraan):
    def __init__(self, merk, warna, jumlah_roda, kecepatan_maksimum, jenis_motor):
        super().__init__(merk, warna, jumlah_roda, kecepatan_maksimum)
        self._jenis_motor = jenis_motor
    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Jenis motor: {self._jenis_motor}")

class MobilSport(Mobil):
    def __init__(self, merk, warna, jumlah_roda, kecepatan_maksimum, jenis_transmisi, jumlah_turbo):
        super().__init__(merk, warna, jumlah_roda, kecepatan_maksimum, jenis_transmisi)
        self.__jumlah_turbo = jumlah_turbo
    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Jumlah turbo: {self.__jumlah_turbo} tabung")

#struktur awal (untuk mencoba testing saja, sebelum implementasi ke menu & perulangan)
#ms = MobilSport("honda", "hitam", 4, 100, "metik", 1)
#ms.tampilkan_informasi()
#ms.tampilkan_jarak_tempuh(2)

while True:
    print('='*20)
    print("informasi kendaraan")
    print("1. mobil")
    print("2. motor")
    print("3. mobil sport")
    print("4. exit")
    print('='*20)

    pilihan = input("inputan user: ")
    if pilihan == '1':
        merk = input("merk: ")
        warna = input("warna: ")
        jumlah_roda = int(input("jumlah roda: "))
        kecepatan_maksimum = int(input("kecepatan maksimum (km/jam): "))
        jenis_transmisi = input("jenis transmisi: ")
        mobil = Mobil(merk, warna, jumlah_roda, kecepatan_maksimum, jenis_transmisi)
        waktu = int(input("masukkan waktu (jam) untuk menghitung jarak tempuh: "))
        os.system('cls')
        mobil.tampilkan_informasi()
        mobil.tampilkan_jarak_tempuh(waktu)

    elif pilihan == '2':
        merk = input("merk: ")
        warna = input("warna: ")
        jumlah_roda = int(input("jumlah roda: "))
        kecepatan_maksimum = int(input("kecepatan maksimum (km/jam): "))
        jenis_motor = input("jenis motor: ")
        motor = Motor(merk, warna, jumlah_roda, kecepatan_maksimum, jenis_motor)
        waktu = int(input("masukkan waktu (jam) untuk menghitung jarak tempuh: "))
        os.system('cls')
        motor.tampilkan_informasi()
        motor.tampilkan_jarak_tempuh(waktu)

    elif pilihan == '3':
        merk = input("merk: ")
        warna = input("warna: ")
        jumlah_roda = int(input("jumlah roda: "))
        kecepatan_maksimum = int(input("kecepatan maksimum (km/jam): "))
        jenis_transmisi = input("jenis transmisi: ")
        jumlah_turbo = int(input("jumlah turbo: "))
        mobil_sport = MobilSport(merk, warna, jumlah_roda, kecepatan_maksimum, jenis_transmisi, jumlah_turbo)
        waktu = int(input("masukkan waktu (jam) untuk menghitung jarak tempuh: "))
        os.system('cls')
        mobil_sport.tampilkan_informasi()
        mobil_sport.tampilkan_jarak_tempuh(waktu)

    elif pilihan == '4':
        os.system('cls')
        print("program diakhiri")
        break

    else:
        os.system('cls')
        print("pilihan tidak valid")