class Mahasiswa:
    """
    ini dokumentasi multi line
    """
    def __init__(self, nama, asal):

        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f'perkenalkan saya {self.nama} dari {self.asal}')

deni = Mahasiswa('Deni', 'Jawa Timur')
#deni.nama = "Deni"
#deni.asal = "Jawa Timur"

lendis = Mahasiswa(asal='Sumatera', nama='Lendis Fabri')
#lendis.nama = "Lendis Fabri"
#lendis.asal = "Jawa Timur"

#panggi fungsi perkenalan
deni.perkenalan()
lendis.perkenalan()