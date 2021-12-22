import sys

try:
    num = int(input("Masukkan nilai angka : "))
    num1 = int(input("Masukkan nilai angka kedua : "))
except ValueError:
    print("Nilai harus bertipe numerik")
else:
    hasil = num + num1
    print("Hasil penjumlahan adalah : ", hasil)
