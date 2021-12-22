import sys

try:
    num = int(input("Masukkan nilai angka : "))
    num1 = int(input("Masukkan nilai angka kedua : "))
except ValueError:
    print("Nilai harus bertipe numerik")
    sys.exit()
hasil = num + num1
print("Hasil penjumlahan adalah : ", hasil)
