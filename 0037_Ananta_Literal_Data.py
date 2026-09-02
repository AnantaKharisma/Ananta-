# LATIHAN LITERAL DATA

print ("Hello world!");

# variable (menyimpan nilai)
# tipe data
# string = karakter
# integer = bilangan bulat
# float = bilangan desimal
# biner = true/false

a = 10
b = 6

print(a)
print("nilai b adalah", b)

# variable
nilai_x = 90 # tidak boleh ada spasi
juta10 = 10000000 # tidak boleh ada angka di awal
Nilai_x = 8 # jangan menggunakan huruf kapital di awal
angkaSepuluhJuta = 10000000
x = 3.14

# a = 10, a adalah variable dengan nilai 10

# tipe data: Angka satuan yang gak ada komanya (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe ", type(data_integer))

# tipe data: Angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe ", type(data_float))
      
# tipe data: kumpulan karakter (string)
data_string = "ucup"
print("data : ", data_string)
print("- bertipe ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe ", type(data_bool))

# Kita belajar Casting
# merubah tipe data ke tipe data lain
# tipe data = int, float, str, bool

# INTEGER ke Tipe data lain

data_int = 9

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai integer = 0

print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

# FLOAT ke Tipe data lain

data_float = 9.2

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai integer = 0

print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

# STRING ke Tipe data lain

data_str = "10"

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str) # akan false jika string kosong
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_float,",type = ", type(data_float))
print("data = ", data_bool,",type = ", type(data_bool))





# TUGAS LITERAL DATA 

# membuat variabel dengan tipe data literal
nama = "Ananta Kharisma"
umur = 19
berat = 60.5

data_nama = str(nama) # string untuk teks
data_umur = int(umur) # integer untuk bilangan bulat
data_berat = float(berat) # float untuk bilangan desimal

print(f"{'nama':6} : {data_nama} ({type(data_nama)})") # f-string untuk menampilkan variabel dengan format tertentu
print(f"{'umur':6} : {data_umur} ({type(data_umur)})") # 6 adalah lebar kolom untuk menampilkan nama variabel
print(f"{'berat':6} : {data_berat} ({type(data_berat)})")

# konversi tipe data
angka_string = "123"
angka_float = 45.67
angka_integer = 89

# 1. Konversi angka_string menjadi integer
angka_string = int(angka_string)

# 2. Konversi angka_float menjadi integer
angka_float = int(angka_float)

# 3. Konversi angka_integer menjadi float
angka_integer_1 = float(angka_integer)

# 4. Konversi angka_integer menjadi string
angka_integer_2 = str(angka_integer)

print(angka_string, type(angka_string)) # 123
print(angka_float, type(angka_float))  # 45
print(angka_integer_1, type(angka_integer_1))  # 89.0
print(angka_integer_2, type(angka_integer_2))  # "89"

# Meminta input usia (integer)
usia = int(input("Masukkan usia: ")) # int() digunakan untuk mengkonversi input menjadi integer

# Meminta input tinggi badan (float)
tinggi_badan = float(input("Masukkan tinggi badan: ")) # float() digunakan untuk mengkonversi input menjadi float

# Meminta input nama (string)
nama = input("Masukkan nama: ") # input() digunakan untuk menerima input dari pengguna, secara default input akan dianggap sebagai string

# Menampilkan hasil
print(f"{'Nama'} : {nama}")
print(f"{'Usia'} : {usia} tahun")
print(f"{'Tinggi Badan'} : {tinggi_badan} cm")
