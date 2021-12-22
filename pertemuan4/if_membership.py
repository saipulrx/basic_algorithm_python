mobil_yang_tersedia = ['Xenia','Avanza','Agya']
mobil_yang_dicari = input('Masukkan nama mobil dalam huruf kecil: ')

if(mobil_yang_dicari in mobil_yang_tersedia):
    print('Mobil tersedia')
else:
    print('Mobil tidak tersedia')