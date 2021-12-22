listKota = [
    'Jakarta','Surabaya','Depok','Bekasi','Solo','Jogjakarta','Semarang','Makasar'
]

kotaYangDicari = input('ketik nama kota yang ingin dicari : ')

i = 0
while i < len(listKota):
    if listKota[i].lower()== kotaYangDicari.lower():
        print('ketemu di index ', i)
        break
    
    print('Bukan ', listKota[i])
    i += 1