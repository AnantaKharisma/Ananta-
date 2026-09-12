usia = int(input("Masukan Usia Anda: "))

if usia >= 0 and usia <= 12:
     print("Kategori: anak-anak")
elif usia >= 13 and usia <= 17:
     print("Kategori: Remaja")
elif usia >= 18 and usia <= 59:
     print("Kategori: dewasa")
elif usia >= 60:
     print("Kategori: lansia")

else:
     print("usia tidak valid")