import class_kucing

obj_kucing = class_kucing.kucing("ini class kucing ") 
nama_kucing = input("Nama Kucing : ")
usia_kucing = input("Usia Kucing : ")
warna_kucing = input("Warna Kucing : ")

obj_kucing.get_nama(nama_kucing)
obj_kucing.get_usia(usia_kucing)
obj_kucing.get_warna(warna_kucing)
obj_kucing.get_output()