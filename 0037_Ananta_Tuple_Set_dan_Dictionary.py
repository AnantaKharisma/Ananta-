#LIST
# menggunakan kurung siku
data_list = [10,2,4,3,2]
print(data_list)

# tuple
data_tuples = (7,8,10,11)
print(data_tuples)
print(data_tuples[1])

# tidak bisa dilakukan
# data_tuples[1] = "ucup"
# data_tuples.append(1)

# sets (himpunan)
data_set = (10,4,3,2,7,6,5)
print(data_set)

print(data_set[0])

# Dictionary

# list → array, mengakses dengan menggunakan index

data_list = ['ucup','rendi','salsa']
print(data_list[0])

# dictionary (dict) → associative array
# identifier → key

data_dict = {
     'key':'value',
     'cp': 'ucup',
     'rd': 'rendi',
     'sl': 'salsa',
     'nmbr': 100,
     'list': data_list
}

print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'])

# --- Operasi Dictionary ---

data_dict = {
    "cup":"ucup surucup",
    "pet":"opet saripet",
    "ndo":"nando surundo"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")

# mengecek key exist atau tidak
KEY = "ucup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict : {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) #chechk key dengan message

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["de"] = "ade si adek"
print(data_dict)
data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"iwn":"iwan mang keren"}) # akan di tambah jika tidak ada
print(data_dict)
# menghapus data
del data_dict["iwn"]
print(data_dict)

# --- Looping Dictionary ---
teman_teman = {
    "cup":"ucup surucup",
    "tong":"sotong surotong",
    "lur":"lur sedulur",
    "wel":"bung towel"
}
# looping first try (yang keluar hanya key)

for teman in teman_teman:
      print(teman)
# operator untuk mengambil item
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
     print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
     print(value)

items = teman_teman.items()
print(items)
for item in teman_teman.items():
     print(item)
for key,value in teman_teman.items():
     print(f"key = {key}, value = {value}")

# LATIHAN
print(" === Jawaban Soal Nomor 1 === ")
# Tuple
# membuat tuple
mahasiswa = ("Ananta","2605060037","Teknologi informsi")
print(mahasiswa)

# menampilkan nim dan prodi
print(mahasiswa[1])
print(mahasiswa[2])

# mengubah isi tuple
# mahasiswa[2] = "Teknologi Informasi"


# membuat set nilai angka
nilai_angka = {10,4,3,2,4,10,7,5}
print(nilai_angka)

# SOAL 2 MANIPULASI DICTIONARY
print("=== jawaban Nomor 2 ===")
# membuat data mahasiswa
data_mahasiswa = {
      "nim":"240101",
      "nama":"Budi Santoso",
      "prodi":"Teknologi Informasi"
}
print(data_mahasiswa["nim"])
print(data_mahasiswa["nama"])
print(data_mahasiswa["prodi"])

# mengubah nilai
data_mahasiswa["prodi"] = "Sastra mesin"
data_mahasiswa["angkatan"] = "2026"
print(data_mahasiswa)

# hapus data nim
del data_mahasiswa["nim"]
print(data_mahasiswa)

# SOAL NOMOR 3 
print("=== Jawaban Nomor 3 ===")
# buat Dictionary
keranjang = {"apel":5000,"pisang":3000,"jeruk":7000,"anggur":15000}
print(keranjang)

# perulangan unuk menampilkan setiap barang dan harga
for key,value in keranjang.items():
      print(f"nama_buah = {key}, harga = Rp{value}")

# Tampilkan total belanja
total = 0
for harga in keranjang.values():
      total += harga
print(f" Total belanja :Rp{total}")
print("=== SELESAI ===")