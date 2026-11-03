#---LIST---
#Kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

#kumpulan data_string
data_string = ["ucup","adit","siti"]
print(data_string)

#kumpulan data_bolean
data_boolean = [True, False, True, True]
print(data_boolean)

#kumpulan data campuran
data_campuran = [1,"bakwan","2,","cireng","ucup",True,"adit",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop, list comprehension
list_for = [i **2 for i in range(0,10)]
print(list_for)

#membuat list pake for pake if
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_for_if)

## --- Operasi LIST ---

# index 0(-3)   1(-2)   2(-1)
data = ["Ucup", "Adit", "Dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

#data.insert(posisi, item)

data.insert(1, "Asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Ririn")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["Luffy", "Zoro", "Nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi jarwo
data[2] = "Jarwo"
print(f"data rubah = \n{data}")

# menghapus data
data.remove("Ucup")
print(f"data hapus = \n(data)")

# menghapus data paling belakang
data.pop()
print(f"data akhir = \n(data)")

# --- Operasi LIST ---
# index 0(-3) 1(-2) 2(-1)
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data angka = \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data
data = ["Rendi","Iqbal","Gana","Khairil"]
print(f"data = {data}")
index_Iqbal = data.index("Iqbal")
index_Gana = data.index("Gana")
print(f"index si Iqbal = {index_Iqbal}")
print(f"index si Gana = {index_Gana}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")
print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")

# --- Nested LIST ---
data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")
list_2D = [data_0, data_1, 6,7]
print(f"list 2D = {list_2D}")

# contoh penggunaan
peserta_0 = ["Rendi", 25, "Laki-laki"]
peserta_1 = ["Joni", 10, "Laki-laki"]
peserta_2 = ["Eka", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
  print(f"nama\t : {peserta[0]}")
  print(f"umur\t : {peserta[1]}")
  print(f"Gender\t : {peserta[2]}\n")


#Latihan
print("=== Jawaban Soal Nomor 1 ===")
#SOAL NOMOR 1
data_string = ["motor","mobil","sepeda","bus"]

# a. Tambahkan 'truk' di akhir list
data_string.append("truk")
print(f"tambah data : \n{data_string}")

# b . Sisipkan 'becak' pada index ke-1
data_string.insert(1,"becak")
print(f"data sesudah disisipkan = \n{data_string}")

# c. Hapus data yang berada paling belakang dari list tsb
data_string.pop()
print(f"hapus data paling belakang = \n{data_string}")

# d. Ubah elemen 'sepeda' menjadi 'sekuter'
data_string[2] = "skuter"
print(f"data setelah diubah = \n{data_string}")

# e. Tampilkan informasi jumlah total data di dalam list tsb
panjang_data = len(data_string)
print(f"panjang data = {panjang_data}")

print("=== Jawaban Soal Nomor 2 ===")
# SOAL NOMOR 2
data_angka = [75,80,90,75,85,100,65]
# a. Cari tahu di indeks keberapa skor 100 berada
index_100 = data_angka.index(100)
print(f"index 100 = {index_100}")

# b. hitung ada berapa banyak siswa yang mendapatkan skor 75
jumlah_data_75 = data_angka.count(75)
print(f"jumlah siswa yang mendapatkan nilai 75 = {jumlah_data_75}")

# c. urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar
print(f"data angka sebelum sort = \n{data_angka}") 
data_angka.sort()
print(f"data angka sort = {data_angka}")

# d. Balikkan urutan list yang sudah diurutkan tsb sehingga menjadi dari terbesar ke terkecil
data_angka.reverse()
print(f"data di reverse = {data_angka}")

print("=== Jawaban Soal Nomor 3 ===")
# SOAL NOMOR 3
# Gabungkan menu_tambahan ke dalammenu_utama menggunakan fungsi
menu_utama = ["Nasi goreng","mie ayam"]
menu_tambahan = ["kerupuk","es teh"]

menu_utama.extend(menu_tambahan)
print(f"list gabungan menu = {menu_utama}")

print("=== Jawaban Soal Nomor 4 ===")
# SOAL NOMOR 4
data_barang = [["buku", 5000], ["pensil", 2000], ["penggaris", 3000]]
# tampilkan harga pensil dgn memanggil indeks baris dan kolom
harga_pensil = data_barang[1][1]
print("Harga pensil:", harga_pensil)

# gunakan perulangan untuk membaca data satu per satu
print(f"barang = {data_barang}")
for barang in data_barang:
    print(f"nama\t : {barang[0]}")
    print(f"harga\t : {barang[1]}")


