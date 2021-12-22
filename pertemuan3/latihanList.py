list_buah = ['Nanas','Mangga','Apel','Durian']

print(list_buah[2:-1])
list_buah[2:-1] = ['Nangka']
print(list_buah[2:-1])

list_buah.append('Sirsak')
print(list_buah)

list_buah.insert(1, 'Semangka')
print(list_buah)

#hapus dengan pop()
list_buah.pop()
print(list_buah)

#hapus dengan remove()
list_buah.remove('Semangka')
print(list_buah)