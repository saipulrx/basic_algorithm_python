class Orang:

    def __init__(self,nama,asal):
        self.nama = nama
        self.asal = asal
        print('fungsi Orang.__init__ di eksekusi')


    def perkenalan(self):
        print(f'perkenalkan nama saya {self.nama} dari {self.asal}')  

class Pelajar (Orang):

    def __init__(self,nama,asal):
        self.nama = nama
        self.asal = asal

class Pekerja (Orang):
    
    def __init__(self,nama,asal):
        self.nama = nama
        self.asal = asal

andi = Orang("Andi","Surabaya")
andi.perkenalan()

deni = Pelajar("Deni", "Bandung")
deni.perkenalan()

budi = Pekerja("Budi","Bogor")
budi.perkenalan()