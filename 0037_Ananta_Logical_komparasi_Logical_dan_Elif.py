# program 4.3 IF and ELIF

# 1. if nya
# 2. kondisnya
# 3. aksinya

nama = input("Masukan Nama Anda: ")

# 1. program if inline
if nama == "Ananta": print("Kamu Ganteng Abiezzz!!!!")
print("akhir dari program if inline")

# 2. program if identation
if nama == "Ananta":
     print("Kamu Ganteng Abiezzz!!!!")
     print("kamu juga pintar abiezzz!!!!")
print("akhir dari program if identation")

# 3. Else statement
if nama == "Abi":
     print("hai Abi si keren") 
else:
     print("ah kamu bukan Abi si keren")

print("akhir dari program else statement")



# Program untuk menentukan kategori usia berdasarkan input pengguna
usia = int(input("Masukan usia Anda: ")) # int untuk mengubah input menjadi integer

if usia >= 0 and usia <= 12: # if statement untuk kategori anak-anak
     print("Kategori: anak-anak")
elif usia >= 13 and usia <= 17: # elif statement untuk kategori remaja
     print("Kategori: Remaja")
elif usia >= 18 and usia <= 59: # elif statement untuk kategori dewasa
     print("Kategori: dewasa")
elif usia >= 60:
     print("Kategori: lansia")

else: # else statement untuk usia yang tidak valid
     print("usia tidak valid")