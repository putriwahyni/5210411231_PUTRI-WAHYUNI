#Program dari pdf

#class Titik
class Titik:
  def _init_(self,x,y) :
    self.x = x
    self.y = y

titik_a = Titik(0,0)
titik_b = Titik(3,4)
print('Titik A memiliki koordinat ({},{})'. Format(titik_a.x,titik_a.y))
print('Titik B memiliki koordinat ({},{}))'. format(titik_b.x,titik_b.y))

#class menu
class menuminuman:
    def _init_(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

mnm1 = menuminuman('Jus Jambu','Jus Jambu Merah Tanpa Gula',8500)
mnm2 = menuminuman('Jus Alpukat','Jus Alpukat dengan gula merah',15000)
mnm3 = menuminuman("Jus Alpukat Xtra Milk",'Jus Alpukat dengan susu coklat',15000)
mnm4 = menuminuman('Red and Smooth','Smoothie dengan pisang dan susu',17500)

pilihan = [mnm1,mnm2,mnm3,mnm4]
print('Daftar menu minuman Healthy')
for mn in pilihan:
    t = '{} harga Rp {},{}'.format(mn.nama,mn.harga,mn.deskripsi)
    print(t)

#class buku
class Buku:
    def _init_(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit =  tahun_terbit

buku = Buku('Tenggelamnya Kapal Van Der Wijck','Hamka',1938)
t = 'Buku {} karangan {} pertama kali terbit {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
print(t)

#class garis 
#titik dibentuk posisi pada sumbu x dan y
class Titik:
    def _init_(self,x,y) :
        self.x = x
        self.y = y

#garis dibentuk dari dua titik
class Garis:
    def __init__(self,titik_pertama,titik_kedua):
        self.titik_pertama = titik_pertama
        self.titik_kedua = titik_kedua

    def panjang(self):
        pjg_x = self.titik_kedua.x - self.titik_pertama.x
        pjg_y = self.titik_kedua.y - self.titik_pertama.y
        pjg = (pjg_x**2 + pjg_y**2) ** 0.5
        return pjg

titik_a = Titik(0,0)
titik_b = Titik(3,4)
garis_ab = Garis(titik_a,titik_b)
print('panjang garis ab adalah {}'. format(garis_ab.panjang()))

#class mahasiswa
class Mahasiswa: 
    def _init_(self,nama,nim,prodi,thn_masuk):
        self.nama =  nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020)
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.formmat(m1.nama,m1.prodi,m1.thn_masuk,m1.nim)
print(teks)


#TUGAS github

#2 objek pada kelas Menu
#1
#class menu1
class makanan:
    def _init_(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

mkn1 = makanan('Nasi Goreng','Pedas Gila',13000)
mkn2 = makanan('Indomie Rebus','Rasa Soto Lamongan',5000)
mkn3 = makanan("Ayam Goreng",'Ayam Goreng Madu',14000)
mkn4 = makanan('Ayam Geprek','Pedas',17500)

pilihan = [mkn1,mkn2,mkn3,mkn4]
print('Daftar menu makanan sumber rezeky')
for mn in pilihan:
    t = '{} harga Rp {},{}'.format(mn.nama,mn.harga,mn.deskripsi)
    print(t)

#2
#class menu2
class Showroom:
    def _init_(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

srm1 = Showroom('Pajero Sport','Putih',700.000)
srm2 = Showroom('Avanza','Silver',200.000)
srm3 = Showroom("Ayla",'Merah',190.000)
srm4 = Showroom('Fortuner','Hitam',500.000)

pilihan = [srm1,srm2,srm3,srm4]
print('Daftar menu Showroom Mobil')
for sr in pilihan:
    s = '{} harga Rp {},{}'.format(sr.nama,sr.harga,sr.deskripsi)
    print(s)

#2 objek pada kelas Mahasiswa
#1
class Mahasiswa1: 
    def _init_(self,nama,nim,prodi,thn_masuk):
        self.nama =  nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk

m1 = Mahasiswa('Angkasa','521041543','Teknik Sipil',2018)
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.formmat(m1.nama,m1.prodi,m1.thn_masuk,m1.nim)
print(teks)

#2
class Mahasiswa2: 
    def _init_(self,nama,nim,prodi,thn_masuk):
        self.nama =  nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk

m1 = Mahasiswa('Aurora','10120445','Arsitektur',2021)
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.formmat(m1.nama,m1.prodi,m1.thn_masuk,m1.nim)
print(teks)

#2 objek pada kelas buku
#1
class Buku1:
    def _init_(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit =  tahun_terbit

buku = Buku('Rumah Kaca','Pramoedya Ananta Toer',2010)
b = 'Buku {} karangan {} pertama kali terbit {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
print(b)

#2
class Buku2:
    def _init_(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit =  tahun_terbit

buku = Buku('Laskar Pelangi','Andrea Hirata',2005)
b = 'Buku {} karangan {} pertama kali terbit {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
print(b)