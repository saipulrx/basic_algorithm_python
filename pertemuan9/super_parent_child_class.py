class Orang:

    def __init__(self,nama,asal):
        self.nama = nama
        self.asal = asal
        print('fungsi Orang.__init__ di eksekusi')

    def perkenalan(self):
        print(f'perkenalkan nama saya {self.nama} dari {self.asal}')  

class Pelajar (Orang):

    def __init__(self,nama,asal,sekolah):
        super().__init__(nama, asal)
        self.sekolah = sekolah

class Pekerja (Orang):
    
    def __init__(self,nama,asal,tempat_kerja):
        Orang.__init__(self,nama,asal)
        self.tempat_kerja = tempat_kerja

andi = Orang("Andi","Surabaya")
andi.perkenalan()

deni = Pelajar("Deni", "Bandung","SMKN 20 bandung")
deni.perkenalan()
print(f'saya sekolah di {deni.sekolah}')

budi = Pekerja("Budi","Bogor","Facebook")
budi.perkenalan()
print(f'saya bekerja di {budi.tempat_kerja}')