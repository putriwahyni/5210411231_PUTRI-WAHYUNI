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

bk1 = Buku("098", "Dasar Dasar Teknik Informatika", "Buku Cetak", "Rak 3", "Ada", "978-623-02-0819-5", "Novega Pratama Adiputra", 100, "17×25")
bk2 = Buku("765","Basis Data", "Buku Ajar", "Rak 3", "Ada", "978-979-29-6943- 6", "Patwiyanto", 150, "17x25")
bk3 = Buku("432","Metode Penelitian Teknik Informatika", "Buku Referensi", "Rak 3", "Dipinjam", "978-602-8981-72-9", "Ade Djohar Maturidi", 200, "17×25")
bk4 = Buku("145","Pemrograman Berorientasi Obyek", "Buku Cetak", "Rak 3", "Dipinjam", "978-979-29-6951-1", "Patwiyanto", 300, "17x25")

maj1 = Majalah("476", "Info Komputer", "Majalah Cetak", "Rak 1", "Ada", "VI", "Komputer")
maj2 = Majalah("465", "Dimensi", "Majalah Cetak", "Rak 1", "Ada", "V", "Informatika")
maj3 = Majalah("458", "Bobo", "Majalah kartun", "Rak 1", "Dipinjam", "IX", "Kartun")
maj4 = Majalah("498", "One Piece", "Majalah Manga", "Rak 1", "Dipinjam", "LXXVI", "Anime")
maj5 = Majalah("421", "Otomotif", "Majalah cetak", "Rak 1", "Ada", "XI", "Otomotif")

dvd1 = DVD("222", "Fast And Furious", "softcopy", "Rak 3", "Ada", "Vin Diesel", "Action")
dvd2 = DVD("203", "Iron Man 3", "softcopy", "Rak 3", "Ada", "Tony Stark", "Marvel")
dvd3 = DVD("274", "Superman The Movie", "softcopy", "Rak 3", "Ada", "Henry cavil", "Action")
dvd4 = DVD("291", "Hulk", "softcopy", "Rak 3", "Ada", "Edward Harrison Norton", "Marvel")

b = [bk1, bk2, bk3, bk4]
maj = [maj1, maj2, maj3, maj4, maj5]
dvd = [dvd1, dvd2, dvd3, dvd4]

while True :
    print("-----------------------\n    MENCARI ITEM \n----------------------")
    print("1. CARI BUKU ")
    print("2. CARI MAJALAH")
    print("3. CARI DVD")
    print("0. Selesai")
    menu = input("Pilihan Menu : ")

    if menu == '1' :
        kode = input("Masukan Kode Buku\t: ")
        for x in b :
            if kode == x.kode :
                print("\n-----------------------------------------------")
                print(f"Judul : {x.judul}")
                print(f"Letak : {x.lokasi}")
                print(f"Status : {x.info}\n")
                print("-----------------------------------------------")

    elif menu == '2' :
        kode = input("Masukan Kode Majalah\t: ")
        for x in maj :
            if kode == x.kode :
                print("\n-----------------------------------------------")
                print(f"Judul : {x.judul}")
                print(f"Letak : {x.lokasi}")
                print(f"Status : {x.info}\n")
                print("-----------------------------------------------")

    elif menu == '3' :
        kode = input("Masukan Kode DVD\t: ")
        for x in dvd :
            if kode == x.kode :
                print("\n-----------------------------------------------")
                print(f"Judul : {x.judul}")
                print(f"Letak : {x.lokasi}")
                print(f"Status : {x.info}\n")
                print("-----------------------------------------------")

    elif menu == '0' :
        print("TERIMA KASIH \n")
        break

    else :
        print("\nPilihan Tidak Ada Menu\n")
    input("\nEnter Untuk Melanjutkan......")