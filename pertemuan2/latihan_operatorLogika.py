# Ambil input untuk mengisi nilai
print("Latihan Operator Perbandingan")
print("===========================")
a = input("Inputkan nilai a: ")
b = input("Inputkan nilai b: ")
c = input("Inputkan nilai c : ")
d = input("Inputkan nilai d : ")

nilai_a = int(a)
nilai_b = int(b)
nilai_c = int(c)
nilai_d = int(d)

# Menggunakan operator logika and
print("")
print("Contoh Operator logika and")
hasil = (nilai_a > nilai_b) and  (nilai_c <= nilai_d)
print ("Hasil (a > b) and (c <= d) = ", hasil)

# Operator  logika or
print("")
print("Contoh Operator logika or")
hasil = (nilai_a != nilai_b) or (nilai_c == nilai_d)
print ("Hasil (a != b) or (c == d) = ", hasil)

# Operator logika not
print("")
print("Contoh Operator logika not ")
hasil = not(nilai_a == nilai_b)
print ("Hasil not(a == b) = ",hasil)

print("===========================")