# Dalam program ini, mendefinisikan tiga kelas: Mahasiswa, Jurusan, dan Universitas.
# Kelas-kelas ini mewakili seorang mahasiswa, sebuah jurusan, dan sebuah universitas, secara berturut-turut.
# Kelas Mahasiswa mewakili seorang mahasiswa dan memiliki atribut seperti nama, NIM, dan jurusan yang diikuti mahasiswa tersebut.
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        
# Kelas ini juga memiliki metode 'tampilkan_info' yang menampilkan informasi lengkap tentang mahasiswa.
    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)

# Kelas Jurusan mewakili sebuah jurusan dan memiliki atribut seperti nama jurusan dan sebuah daftar untuk menyimpan mahasiswa-mahasiswa dalam jurusan tersebut.
class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

# Kelas ini juga memiliki metode untuk menambahkan mahasiswa ke jurusan 
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

# dan menampilkan daftar mahasiswa dalam jurusan tersebut.
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)
            print()

# Kelas Universitas mewakili sebuah universitas dan memiliki atribut seperti nama universitas dan sebuah daftar untuk menyimpan jurusan-jurusan dalam universitas tersebut.
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

# Kelas ini juga memiliki metode untuk menambahkan jurusan ke universitas 
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

# dan menampilkan daftar jurusan dalam universitas tersebut.
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)

# Pada bagian selanjutnya, program melakukan langkah-langkah berikut:
# 1. Membuat objek Universitas dengan nama "Bengkulu University"
universitas_bengkulu = Universitas("Bengkulu")

# 2. Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas Bengkulu
jurusan_ti = Jurusan("Teknik Informatika")
universitas_bengkulu.tambah_jurusan(jurusan_ti)

# 3. Membuat objek Mahasiswa dengan nama "Beny Esa Pratama", NIM "G1A022013",
#    dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas Bengkulu
mahasiswa_beny = Mahasiswa("Beny Esa Pratama", "G1A022013", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa_beny)

# 4. Menampilkan daftar jurusan yang ada di Universitas Bengkulu
universitas_bengkulu.tampilkan_daftar_jurusan()

# 5. Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas Bengkulu
jurusan_ti.tampilkan_daftar_mahasiswa()
