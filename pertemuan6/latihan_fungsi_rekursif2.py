def tampilkan_angka(batas, i=1):
    print(f'Perulangan ke {i}')

    if (i < batas):
        tampilkan_angka(batas, i+1)

tampilkan_angka(10)