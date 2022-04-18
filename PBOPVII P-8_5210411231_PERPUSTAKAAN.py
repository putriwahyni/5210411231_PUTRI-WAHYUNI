class Perpustakaan :
    def __init__(self, kode, judul, subjek, lokasi, info) :
        self.kode = kode
        self.judul = judul      
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info

class Buku(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, isbn, pengarang, jmlhal, ukuran):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal        
        self.ukuran = ukuran         

class Majalah(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, volume, issue):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue

class DVD(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.aktor = aktor
        self.genre = genre      

b = Buku("098", "Dasar Dasar Teknik Informatika", "Buku Cetak", "Rak 3", "Ada", "978-623-02-0819-5", "Novega Pratama Adiputra", 100, "17×25")
m = Majalah("465", "Dimensi", "Majalah Cetak", "Rak 1", "Ada", "V", "Informatika")
d = DVD("274", "Superman The Movie", "softcopy", "Rak 3", "Ada", "Henry cavil", "Action")
obj = [b, m, d]  

for object in obj : 
    print(f"Judul : {object.judul}")
    print(f"Kategori : {object.subjek}")
    print(f"Lokasi : {object.lokasi}")  
    print(f"Status : {object.info}\n")