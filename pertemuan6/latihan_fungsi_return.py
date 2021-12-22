def luas_persegi(sisi):
    return sisi * sisi

#tidak menghasilkan output
luas_persegi(10)

#menghasilkan output
print('Luas Persegi dengan sisi 4 adalah : ', luas_persegi(4))

persegi_besar = luas_persegi(1500)
persegi_kecil = luas_persegi(100)

print('Total Luas persegi besar dan kecil adalah : ', persegi_besar + persegi_kecil)