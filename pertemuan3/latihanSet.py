himpunan_hewan = {
    'Kucing','Anjing','Tikus','Beruang'
}
print(himpunan_hewan)

#add nilai baru satu satu
himpunan_hewan.add('Tupai')
himpunan_hewan.add('Kecoa')
print(himpunan_hewan)

#add nilai lebih dari satu gunakan fungsi update
himpunan_hewan.update({'Merpati','Rusa'})
print(himpunan_hewan)

#menghapus menggunakan fungsi remove
himpunan_hewan.remove('Rusa')
print(himpunan_hewan)
#himpunan_hewan.remove('Rusa')

#menghapus menggunakan fungsi discard
himpunan_hewan.discard('Rusa')
himpunan_hewan.discard('Kecoa')
print(himpunan_hewan)

#menghapus menggunakan fungsi pop
himpunan_hewan.pop()
print(himpunan_hewan)

#menghapus menggunakan clear
himpunan_hewan.clear()
print(himpunan_hewan)
