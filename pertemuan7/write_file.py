print("Selamat datang di program biodata")
print("=================================")

#ambil input dari user
nama = input("Nama:")
umur = input("Umur:")
alamat = input("Alamat:")

#format teks
teks = "\nNama: {}\nUmur: {} \nAlamat: {}\n---".format(nama,umur,alamat)

#buka file untuk di tulis
file_bio = open("biodata.txt","a")

#tulis ke file
file_bio.write(teks)

#tutup file
file_bio.close()