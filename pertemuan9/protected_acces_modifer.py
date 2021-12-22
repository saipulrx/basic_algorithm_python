class Mobil:
    def __init__(self, merk):
        self.__merk = merk

    def tampilkan_merk(self):
        print(f'Merk : {self.__merk}')    


class MobilBalap(Mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear

    def pamer(self):
        # akses _merk dari subclass
        print(f'Ini mobil {self.__merk} dengan total gear {self._total_gear}')


""" sedan = Mobil('Toyota')
print(f'Merk : {sedan.__merk}') """

ferrari = MobilBalap('ferrari', 8)
ferrari.tampilkan_merk()

jip = Mobil('jip')
jip.tampilkan_merk()
