listKota = [
    'Jakarta','Surabaya','Depok','Bekasi','Solo','Jogjakarta','Semarang','Makasar'
]

kotaYangDicari = input('ketik nama kota yang ingin dicari : ')

for i, kota in enumerate(listKota):
    #kita ubah katanya ke lowercase
    if kota.lower() == kotaYangDicari.lower():
        print('Kota yang anda cari berada pada index', i)
        break
else:
    print("maaf, kota yang anda cari tidak ada")