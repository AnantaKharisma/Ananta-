# CATATAN OPERASI ARITMATIKA DAN KOMPARASI
# Program 3.1
# Operasi Aritmatika

a = 10
b = 3

# Operasi Aritmatika

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)
# operasi kurang –
hasil = a - b
print(a,'-',b,'=',hasil)
# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)
# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)
# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)
# operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)
# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# Program 3.2
# Latihan Konversi satuan temperatur
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu adalah", celcius, "Celcius")
# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")
# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")
# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")

# Program 3.3
# Operasi Komparasi
# Setiap hasil dari operasi komparasi adalah boolean (True/False)

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# operasi lebih besar dari >
print("==== LEBIH BESAR DARI (>) ====")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# operasi lebih kecil dari <
print("==== LEBIH KECIL DARI (<) ====")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# operasi lebih besar dari sama dengan >=
print("==== LEBIH BESAR DARI SAMA DENGAN (>=) ====")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# operasi lebih kecil dari sama dengan <=
print("==== LEBIH KECIL DARI SAMA DENGAN (<=) ====")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# operasi sama dengan ==
print("==== SAMA DENGAN (==) ====")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# operasi tidak sama dengan !=
print("==== TIDAK SAMA DENGAN (!=) ====")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# `is` sebagai komparasi object identity,( bukan literal )
x = 5 # ini adalah assignment membuat object
y = 5
hasil = x is y
print(x,'is',y,'=',hasil)

# `is not` sebagai komparasi object identity, (bukan literal)
x = 5 # ini adalah assignment membuat object
y = 6
hasil = x is not y
print(x,'is not',y,'=',hasil)


# TUGAS 3 Operasi Aritmatika

# data bangunan
panjang = 12
lebar = 5
tinggi = 8

# menghitung luas permukaan bangunan
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print("Luas permukaan bangunan:", luas_permukaan)

# menghitung volume bangunan
volume = panjang * lebar * tinggi
print("Volume bangunan:", volume)

# menghitung keliling bangunan
keliling = 4 * (panjang + lebar + tinggi)
print("Keliling bangunan:", keliling)

# apakah luas bangunan tersebut lebih luas dari 50?
print("Apakah luas bangunan lebih luas dari 50?", luas_permukaan > 50)

# apakah volume bangunan bernilai 480?
print("Apakah volume bangunan bernilai 480?", volume == 480)


