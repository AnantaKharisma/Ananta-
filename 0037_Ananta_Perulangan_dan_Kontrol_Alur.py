# PROGRAM 5.1 For
# perulangan (loop) for digunakan untuk melakukan perulangan terhadap suatu blok kode tertentu.

angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

# for kondisi : 
#    aksi

#dengan list
angka2 = [1, 2, 3, 4, 5] # ini adalah list
print(angka2)

for i in angka2:
    print(f"i sekarang → {i}") #print(f) -> kombinasi text dan variabel
print("akhiri dari program\n")
#dengan range
angka3 = range(5)

for i in angka3:
    print(f"i sekarang → {i}")
print("akhiri dari program\n")

angka4 = range(1,10)
for i in angka4:
    print(f"i sekarang → {i}")
#print(“saya keren”)
print("akhiri dari program\n")
# menggunakan string
data_str = "saya ganteng abiies"
for huruf in data_str:
    print(huruf)
print("akhiri dari program\n")

# PROGRAM 5.2 While loop
# While loop

# while kondisi:
#    aksi ini
#    aksi itu

# pass, continue, break

# pass
angka = 0 

while angka < 5:
    angka = angka + 1
    if(angka == 3):
        pass
        # print(angka)
print("berakhir")

# continue

angka = 1
while angka < 5:
    angka = angka + 1
    if(angka == 3):
        continue
        print(f"angka sekarang → {angka}")
# print("berakhir")

# break
# TUGAS PERTEMUAN 5 PERULANGAN DAN KOTROL ALUR
print("===MENENTUKAN BILANGAN GANJIL DAN GENAP===")

for i in range(1,51):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    else:
        print(f"{i} adalah bilangan ganjil")
print("akhiri dari program\n")

print("===MENENTUKAN BILANGAN PRIMA===")
for angka in range(2,101):
    prima = True

    for pembagi in range(2 , angka):
        if angka % pembagi == 0:
            prima = False
            break
    if prima:
        print(f"{angka} adalah bilangan prima")
print("akhiri dari program\n")