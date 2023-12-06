class Perpustakaan():
    def __init__(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek

    def lokasipenyimpanan(self):
        return "disimpan di perpus"

    def info(self):
        return "bukunya ada"


class DVD(Perpustakaan):
    def __init__(self, judul, subjek, aktor, genre):
        super().__init__(judul, subjek)
        self.aktor = aktor
        self.genre = genre


class Majalah(Perpustakaan):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue


class Katalog(Perpustakaan):
    def __init__(self, judul, subjek, cari):
        super().__init__(judul, subjek)
        self.cari = cari


class Buku(Perpustakaan):
    def __init__(self, judul, subjek, isbn, pengarang, jmlhal, ukuran):
        super().__init__(judul, subjek)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal
        self.ukuran = ukuran


class Pengarang(Buku):
    def __init__(self, judul, subjek, isbn, pengarang, jmlhal, ukuran, nama):
        super().__init__(judul, subjek, isbn, pengarang, jmlhal, ukuran)
        self.nama = nama

    def info(self):
        return f"Pengarang: {self.nama}, Judul: {self.judul}, ISBN: {self.isbn}"

    def cari(self):
        return f"Mencari buku berjudul {self.judul} yang ditulis oleh {self.nama}"


# contoh data
dvd1 = DVD("DVD CCTV", "menjaga", "satpam", "keamanan")
print(dvd1.lokasipenyimpanan())
print(dvd1.info())

dvd2 = DVD("ospek", "pelatihan", "mahasiswa", "pendididkan")
print(dvd2.lokasipenyimpanan())
print(dvd2.info())